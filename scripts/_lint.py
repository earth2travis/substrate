#!/usr/bin/env python3
"""_lint.py — Structural consistency checker for the Substrate.

Enforces frontmatter, naming conventions, wikilinks, and HTML detection
across all Markdown files. Exit 0 if clean, exit 1 if structural errors found.

Usage:
  python3 scripts/_lint.py                          # Check all files
  python3 scripts/_lint.py --dir research/raw/      # Check specific directory
  python3 scripts/_lint.py --fix                    # Auto-fix what it can
  python3 scripts/_lint.py --format json            # Machine-readable output

Auto-fix behavior:
  - naming-convention: Rename file via git mv (requires git repo)
  - fm-tags-empty: Derive tags from body using strict phrase matching
  - fm-related-missing: Cannot auto-fix
  - html-scrape: Cannot auto-fix (flags for manual review)

Non-fixable rules (require manual intervention):
  - fm-missing, fm-title-missing, broken-wikilink, duplicate-title
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

RAW_DIR = "research/raw"
FINDINGS_DIR = "research/findings"
INSIGHTS_DIR = "insights"
DECISIONS_DIR = "decisions"
GUIDES_DIR = "guides"
QUERIES_DIR = "research/queries"
RETROS_DIR = "retros"
SPECS_DIR = "specs"

SEVERITY_ORDER = {"ERROR": 3, "WARNING": 2, "INFO": 1}

# Directories where files are considered "structured" (strict validation)
STRUCTURED_DIRS = {
    FINDINGS_DIR, INSIGHTS_DIR, DECISIONS_DIR, GUIDES_DIR,
    QUERIES_DIR, RETROS_DIR, SPECS_DIR,
}

# ---------------------------------------------------------------------------
# Minimal YAML parser (stdlib only)
# ---------------------------------------------------------------------------

def parse_yaml_block(text: str) -> dict:
    """Parse flat YAML frontmatter."""
    result = {}
    if not text.strip():
        return result

    current_key = None
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue

        if ':' in stripped and not stripped.startswith('-'):
            key, _, value = stripped.partition(':')
            key = key.strip()
            value = value.strip()

            if value.startswith('['):
                items = value.strip('[]').split(',')
                result[key] = [i.strip().strip('"').strip("'") for i in items if i.strip()]
                current_key = None
            elif value == '':
                current_key = key
                result[key] = []
            elif value.startswith('"') or value.startswith("'"):
                result[key] = value.strip('"').strip("'")
                current_key = None
            else:
                result[key] = value
                current_key = None
        elif stripped.startswith('- ') and current_key is not None:
            item = stripped[2:].strip().strip('"').strip("'")
            if isinstance(result.get(current_key), list):
                result[current_key].append(item)

    return result


def yaml_dump(data: dict) -> str:
    """Serialize a flat dict to YAML frontmatter block."""
    lines = ['---']
    for key, value in data.items():
        if isinstance(value, list):
            if not value:
                lines.append(f'{key}: []')
            else:
                lines.append(f'{key}:')
                for item in value:
                    lines.append(f'  - {item}')
        elif value is None or value == '':
            lines.append(f'{key}: ""')
        else:
            s = str(value)
            if any(c in s for c in ':#{}[]|>&*!?%@`') or s.lower() in ('true', 'false', 'null', 'yes', 'no'):
                s = f'"{s}"'
            lines.append(f'{key}: {s}')
    lines.append('---')
    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# File reading
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n(.*)', re.DOTALL)
WIKILINK_RE = re.compile(r'\[\[([^\]|\n]+)(?:\|[^\]]+)?\]\]')


def extract_frontmatter(text: str) -> tuple[Optional[dict], str, bool]:
    m = FRONTMATTER_RE.match(text)
    if m:
        return parse_yaml_block(m.group(1)), m.group(2), True
    return None, text, False


def find_all_md_files(repo: Path, target_dir: Optional[Path] = None) -> list[Path]:
    """Find all .md files, optionally scoped to a directory."""
    if target_dir:
        return sorted(target_dir.rglob('*.md'))
    return sorted(p for p in repo.rglob('*.md') if '.git' not in str(p))


def is_structured_file(path: Path, repo: Path) -> bool:
    """Determine if a file is in a structured directory (strict validation).
    Structured dirs: findings, insights, decisions, guides, queries, retros, specs.
    Raw files are NOT structured. Root-level docs are structured.
    """
    rel = path.relative_to(repo)
    # Root-level docs are structured
    if len(rel.parts) == 1:
        return True
    # Check if file is inside any structured directory
    rel_str = str(rel)
    for d in STRUCTURED_DIRS:
        if rel_str.startswith(d + '/'):
            return True
    return False


def is_raw_file(path: Path, repo: Path) -> bool:
    """Check if file is in research/raw/."""
    try:
        rel = path.relative_to(repo)
        return str(rel).startswith(RAW_DIR)
    except ValueError:
        return False


# ---------------------------------------------------------------------------
# Tag patterns for auto-fix
# ---------------------------------------------------------------------------

TAG_PATTERNS: list[tuple[str, list[str]]] = [
    ('process-philosophy', [
        'process philosophy', 'process and reality', 'creative evolution',
        'philosophy of organism', 'actual occasion', 'actual occasions',
        'élán vital', 'elan vital', 'duration (durée)', 'durée',
        'dependent origination', 'pratītyasamutpāda',
        'middle way', 'mulamadhyamakakarika',
    ]),
    ('postmodernism', [
        'simulacra and simulation', 'hyperreality',
        'differential and repetition', 'rhizomatic',
        'simulacres et simulation',
    ]),
    ('lean-manufacturing', [
        'toyota production system', 'just-in-time',
        'heijunka', 'jidoka', 'andon',
        'lean production', 'taichi ohno',
        'seven wastes', 'muda', 'mura', 'muri',
    ]),
    ('software-engineering', [
        'continuous delivery', 'continuous deployment',
        'spec-driven development', 'dora metrics',
        'feature flags', 'deployment pipeline',
    ]),
    ('knowledge-management', [
        'knowledge base', 'llm wiki', 'second brain',
        'knowledge graph', 'institutional memory',
    ]),
    ('ai-agents', [
        'coding agent', 'ai agent', 'autonomous agent',
        'agent platform', 'agent company', 'agentic',
        'multi-agent', 'agent orchestration',
        'context stack', 'context window',
    ]),
    ('claude-anthropic', [
        'claude code', 'claude opus', 'anthropic',
    ]),
    ('openai', [
        'openai', 'gpt-4', 'gpt-5',
    ]),
    ('security-ops', [
        'opsec', 'server hardening', 'prompt injection',
        'tool provisioning', 'security crisis',
    ]),
]


def auto_tag(body: str, title: str) -> list[str]:
    """Derive tags from body text using strict phrase matching."""
    text = (title + ' ' + body).lower()
    found = set()
    for tag, phrases in TAG_PATTERNS:
        for phrase in phrases:
            pattern = r'\b' + re.escape(phrase) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                found.add(tag)
                break
    if not found:
        found.add('general')
    return sorted(found)


# ---------------------------------------------------------------------------
# Validation rules
# ---------------------------------------------------------------------------

@dataclass
class Violation:
    file: str
    rule: str
    severity: str
    message: str
    line: Optional[int] = None
    fixable: bool = False


def validate_file(path: Path, repo: Path, all_titles: dict[str, list[str]]) -> list[Violation]:
    """Run all lint rules on a single file."""
    violations = []
    text = path.read_text(encoding='utf-8', errors='replace')
    fm, body, has_fm = extract_frontmatter(text)
    fm = fm or {}
    structured = is_structured_file(path, repo)
    raw = is_raw_file(path, repo)

    # Rule: fm-missing
    if not has_fm:
        if structured:
            violations.append(Violation(
                file=str(path.relative_to(repo)),
                rule="fm-missing",
                severity="ERROR",
                message="No YAML frontmatter block found.",
                fixable=False,
            ))
        else:
            violations.append(Violation(
                file=str(path.relative_to(repo)),
                rule="fm-missing",
                severity="WARNING",
                message="No YAML frontmatter block found. Agent should add during ingest.",
                fixable=False,
            ))

    # Rule: fm-title-missing
    if has_fm:
        title = fm.get('title', '')
        if not title or title.strip() == '':
            h1 = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
            if structured:
                violations.append(Violation(
                    file=str(path.relative_to(repo)),
                    rule="fm-title-missing",
                    severity="ERROR",
                    message="No title in frontmatter." + (f" H1 found: '{h1.group(1).strip()}'" if h1 else " No H1 in body."),
                    fixable=False,
                ))
            else:
                violations.append(Violation(
                    file=str(path.relative_to(repo)),
                    rule="fm-title-missing",
                    severity="WARNING",
                    message="No title in frontmatter." + (f" H1 found: '{h1.group(1).strip()}'" if h1 else ""),
                    fixable=False,
                ))
        else:
            # Rule: duplicate-title
            title_normalized = title.strip().lower()
            if title_normalized in all_titles and len(all_titles[title_normalized]) > 1:
                # Only report once per duplicate group (lowest path first)
                if str(path.relative_to(repo)) == min(all_titles[title_normalized]):
                    others = [p for p in all_titles[title_normalized] if p != str(path.relative_to(repo))]
                    violations.append(Violation(
                        file=str(path.relative_to(repo)),
                        rule="duplicate-title",
                        severity="ERROR",
                        message=f"Duplicate title with: {', '.join(others)}",
                        fixable=False,
                    ))

    # Rule: fm-tags-empty
    tags = fm.get('tags', None) if has_fm else None
    if tags is not None:
        if tags == [] or (isinstance(tags, list) and len(tags) == 0):
            if structured:
                violations.append(Violation(
                    file=str(path.relative_to(repo)),
                    rule="fm-tags-empty",
                    severity="WARNING",
                    message="Tags field is empty.",
                    fixable=True,
                ))
            else:
                violations.append(Violation(
                    file=str(path.relative_to(repo)),
                    rule="fm-tags-empty",
                    severity="INFO",
                    message="Tags field is empty. Agent will derive during ingest.",
                    fixable=False,
                ))

    # Rule: fm-related-missing
    related = fm.get('related', None) if has_fm else None
    if structured and has_fm:
        if related is None:
            violations.append(Violation(
                file=str(path.relative_to(repo)),
                rule="fm-related-missing",
                severity="WARNING",
                message="No 'related' field in frontmatter. Minimum 2 wikilinks required for insights/decisions/guides.",
                fixable=False,
            ))
        elif isinstance(related, list) and len(related) < 2:
            violations.append(Violation(
                file=str(path.relative_to(repo)),
                rule="fm-related-missing",
                severity="WARNING",
                message=f"Only {len(related)} related link(s). Minimum 2 required.",
                fixable=False,
            ))

    # Rule: naming-convention
    filename = path.name
    if '_' in filename or ' ' in filename or any(c.isupper() for c in filename):
        new_name = filename.replace('_', '-').replace(' ', '-').lower()
        violations.append(Violation(
            file=str(path.relative_to(repo)),
            rule="naming-convention",
            severity="ERROR",
            message=f"Filename violates kebab-case. Suggest: {new_name}",
            fixable=True,
        ))

    # Rule: no-h1
    if not re.search(r'^#\s+.+$', body, re.MULTILINE):
        violations.append(Violation(
            file=str(path.relative_to(repo)),
            rule="no-h1",
            severity="INFO",
            message="No top-level # Heading in body.",
            fixable=False,
        ))

    # Rule: html-scrape
    if bool(re.match(r'\s*<!DOCTYPE', body, re.IGNORECASE)) or body[:500].count('<html') > 0:
        violations.append(Violation(
            file=str(path.relative_to(repo)),
            rule="html-scrape",
            severity="ERROR",
            message="File contains HTML. Raw HTML should not be in knowledge files.",
            fixable=False,
        ))

    return violations


def find_broken_wikilinks(all_files: list[Path], repo: Path) -> list[Violation]:
    """Find all wikilinks that point to non-existent files.
    Skips wikilinks inside code blocks (```) and inline code spans (`).
    """
    violations = []

    # Build a map of all existing file stems and names
    existing_stems = set()
    existing_names = set()
    for p in all_files:
        existing_stems.add(p.stem.lower())
        existing_names.add(p.name.lower())
        # Also add parent+stem for path-style wikilinks
        if len(p.relative_to(repo).parts) > 1:
            existing_stems.add(str(p.relative_to(repo).with_suffix('')).lower().replace('/', '-'))

    CODE_BLOCK_RE = re.compile(r'```[\s\S]*?```', re.DOTALL)
    INLINE_CODE_RE = re.compile(r'`[^`\n]+`')

    for path in all_files:
        text = path.read_text(encoding='utf-8', errors='replace')
        fm, body, has_fm = extract_frontmatter(text)

        # Strip code blocks and inline code spans before matching wikilinks
        body_no_code = CODE_BLOCK_RE.sub('', body)
        body_no_code = INLINE_CODE_RE.sub('', body_no_code)

        for match in WIKILINK_RE.finditer(body_no_code):
            target = match.group(1).strip()
            # Extract filename part before |
            if '|' in target:
                target = target.split('|')[0].strip()

            # Skip directory references (e.g., [[research/]]) — these are navigation links, not file links
            if target.endswith('/'):
                continue

            target_lower = target.lower()
            target_stem = target_lower
            if target_lower.endswith('.md'):
                target_stem = target_lower[:-3]

            # Check if target exists
            exists = False
            if target_lower in existing_names:
                exists = True
            elif target_stem in existing_stems:
                exists = True
            elif target_stem.replace('-', '') in {s.replace('-', '') for s in existing_stems}:
                exists = True

            if not exists:
                # Determine severity based on file location
                # Raw files can have forward references; structured files should resolve
                if is_raw_file(path, repo):
                    severity = "INFO"
                    msg = f"Forward-reference wikilink [[{target}]] — entity/concept not yet in Substrate."
                else:
                    severity = "ERROR"
                    msg = f"Wikilink [[{target}]] points to no existing .md file."

                # Find line number in original text (not stripped text)
                # Map position in stripped text back to original position approximately
                # For simplicity, search in original text for the match
                original_match = WIKILINK_RE.search(body)
                line_num = body[:original_match.start()].count('\n') + 1 if original_match else 1
                violations.append(Violation(
                    file=str(path.relative_to(repo)),
                    rule="broken-wikilink",
                    severity=severity,
                    message=msg,
                    line=line_num,
                    fixable=False,
                ))

    return violations


def find_broken_fm_related_links(all_files: list[Path], repo: Path) -> list[Violation]:
    """Find wikilinks in frontmatter 'related' field that point to non-existent files.
    Mirrors the resolution logic in find_broken_wikilinks.
    """
    violations = []

    # Build the same lookup tables as find_broken_wikilinks
    existing_names = set()
    existing_stems = set()
    for p in all_files:
        existing_names.add(p.name.lower())
        existing_stems.add(p.stem.lower())
        if len(p.relative_to(repo).parts) > 1:
            existing_stems.add(str(p.relative_to(repo).with_suffix('')).lower().replace('/', '-'))

    for path in all_files:
        text = path.read_text(encoding='utf-8', errors='replace')
        fm, _, has_fm = extract_frontmatter(text)
        if not has_fm or not fm:
            continue

        related = fm.get('related')
        if not isinstance(related, list):
            continue

        for item in related:
            item = str(item).strip()
            if not item:
                continue

            # Extract target from [[target|alias]] or bare target
            target = item
            m = re.match(r'^\[\[([^\]|\n]+)(?:\|[^\]]+)?\]\]$', item)
            if m:
                target = m.group(1).strip()

            # Skip directory references
            if target.endswith('/'):
                continue

            target_lower = target.lower()
            target_stem = target_lower
            if target_lower.endswith('.md'):
                target_stem = target_lower[:-3]

            exists = (
                target_lower in existing_names
                or target_stem in existing_stems
                or target_stem.replace('-', '') in {s.replace('-', '') for s in existing_stems}
            )

            if not exists:
                if is_raw_file(path, repo):
                    severity = "INFO"
                    msg = f"Forward-reference wikilink in frontmatter related: [[{target}]] — not yet in Substrate."
                else:
                    severity = "ERROR"
                    msg = f"Frontmatter related wikilink [[{target}]] points to no existing .md file."

                violations.append(Violation(
                    file=str(path.relative_to(repo)),
                    rule="broken-wikilink",
                    severity=severity,
                    message=msg,
                    fixable=False,
                ))

    return violations


# ---------------------------------------------------------------------------
# Orphan detection
# ---------------------------------------------------------------------------

def find_orphan_findings(repo: Path) -> list[Violation]:
    """Find findings whose raw source no longer exists."""
    violations = []
    raw_dir = repo / RAW_DIR
    findings_dir = repo / FINDINGS_DIR

    if not raw_dir.exists() or not findings_dir.exists():
        return violations

    raw_stems = {p.stem.lower() for p in raw_dir.glob('*.md')}

    for finding in findings_dir.glob('*.md'):
        stem = finding.stem.lower()
        if stem not in raw_stems:
            violations.append(Violation(
                file=str(finding.relative_to(repo)),
                rule="orphan-finding",
                severity="WARNING",
                message=f"Finding has no matching raw source ({stem}.md not found in {RAW_DIR}/)",
                fixable=False,
            ))

    return violations


# ---------------------------------------------------------------------------
# Auto-fix
# ---------------------------------------------------------------------------

def apply_fix(violation: Violation, repo: Path, dry_run: bool = False) -> bool:
    """Attempt to auto-fix a violation. Returns True if fixed."""
    path = repo / violation.file

    if violation.rule == "naming-convention":
        new_name = path.name.replace('_', '-').replace(' ', '-').lower()
        if new_name == path.name:
            return False

        new_path = path.parent / new_name
        if new_path.exists():
            print(f"  Cannot fix {violation.file}: target {new_name} already exists")
            return False

        if dry_run:
            print(f"  [dry-run] Would git mv {path.name} -> {new_name}")
            return True

        # Use git mv if in a git repo
        git_dir = repo / ".git"
        if git_dir.exists():
            try:
                subprocess.run(
                    ["git", "mv", str(path), str(new_path)],
                    cwd=repo, check=True, capture_output=True
                )
                print(f"  Fixed: git mv {path.name} -> {new_name}")
                return True
            except subprocess.CalledProcessError:
                pass

        # Fallback: regular rename
        path.rename(new_path)
        print(f"  Fixed: renamed {path.name} -> {new_name}")
        return True

    elif violation.rule == "fm-tags-empty":
        text = path.read_text(encoding='utf-8')
        fm, body, has_fm = extract_frontmatter(text)
        if not has_fm or not fm:
            return False

        new_tags = auto_tag(body, fm.get('title', ''))
        fm['tags'] = new_tags

        if dry_run:
            print(f"  [dry-run] Would add tags {new_tags} to {path.name}")
            return True

        new_text = yaml_dump(fm) + '\n\n' + body.lstrip('\n')
        path.write_text(new_text, encoding='utf-8')
        print(f"  Fixed: added tags {new_tags} to {path.name}")
        return True

    return False


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def format_text(violations: list[Violation]) -> str:
    lines = []
    for v in sorted(violations, key=lambda x: (SEVERITY_ORDER.get(x.severity, 0), x.file, x.rule)):
        loc = f":{v.line}" if v.line else ""
        fix_marker = " [fixable]" if v.fixable else ""
        lines.append(f"[{v.severity}] {v.file}{loc}: {v.rule} — {v.message}{fix_marker}")
    return '\n'.join(lines)


def format_json(violations: list[Violation], summary: dict) -> str:
    return json.dumps({
        "run_id": summary["run_id"],
        "repo": str(summary["repo"]),
        "files_checked": summary["files_checked"],
        "error_count": summary["error_count"],
        "warning_count": summary["warning_count"],
        "info_count": summary["info_count"],
        "fixed_count": summary["fixed_count"],
        "violations": [
            {
                "file": v.file,
                "rule": v.rule,
                "severity": v.severity,
                "message": v.message,
                "line": v.line,
                "fixable": v.fixable,
            }
            for v in violations
        ]
    }, indent=2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(repo_path: str, target_dir: Optional[str] = None, fix: bool = False,
         dry_run: bool = False, fmt: str = "text"):
    repo = Path(repo_path)
    scope = repo if target_dir is None else repo / target_dir

    if not scope.exists():
        print(f"ERROR: {scope} not found", file=sys.stderr)
        sys.exit(1)

    # Find all markdown files
    all_files = find_all_md_files(repo, scope if target_dir else None)

    # Pre-compute all titles for duplicate detection
    all_titles: dict[str, list[str]] = defaultdict(list)
    for path in all_files:
        text = path.read_text(encoding='utf-8', errors='replace')
        fm, _, has_fm = extract_frontmatter(text)
        if has_fm and fm and fm.get('title'):
            title = str(fm['title']).strip().lower()
            all_titles[title].append(str(path.relative_to(repo)))

    # Run per-file validations
    violations: list[Violation] = []
    for path in all_files:
        violations.extend(validate_file(path, repo, all_titles))

    # Run cross-file validations
    violations.extend(find_broken_wikilinks(all_files, repo))
    violations.extend(find_broken_fm_related_links(all_files, repo))
    violations.extend(find_orphan_findings(repo))

    # Sort: ERROR first, then WARNING, then INFO
    violations.sort(key=lambda v: (
        -SEVERITY_ORDER.get(v.severity, 0),
        v.file,
        v.rule
    ))

    # Apply fixes if requested
    fixed_count = 0
    if fix:
        fixable = [v for v in violations if v.fixable]
        if fixable:
            print(f"Applying fixes for {len(fixable)} fixable violation(s)...", file=sys.stderr)
            for v in fixable:
                if apply_fix(v, repo, dry_run):
                    fixed_count += 1
            print(f"Fixed {fixed_count} violation(s).\n", file=sys.stderr)

    # Build summary
    summary = {
        "run_id": datetime.now(timezone.utc).isoformat(),
        "repo": str(repo),
        "files_checked": len(all_files),
        "error_count": len([v for v in violations if v.severity == "ERROR"]),
        "warning_count": len([v for v in violations if v.severity == "WARNING"]),
        "info_count": len([v for v in violations if v.severity == "INFO"]),
        "fixed_count": fixed_count,
    }

    # Output
    if fmt == "json":
        print(format_json(violations, summary))
    else:
        if violations:
            print(format_text(violations))
        print(f"\n{'='*60}")
        print(f"Substrate Lint Report")
        print(f"  Files checked:  {summary['files_checked']}")
        print(f"  Errors:         {summary['error_count']}")
        print(f"  Warnings:       {summary['warning_count']}")
        print(f"  Info:           {summary['info_count']}")
        if fix or dry_run:
            print(f"  Fixed:          {fixed_count}")
        print(f"{'='*60}")

    # Exit code
    if summary["error_count"] > 0:
        print(f"\nFAILED: {summary['error_count']} error(s) found.", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"\nPASSED: No structural errors.", file=sys.stderr)
        sys.exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Substrate structural linter')
    parser.add_argument('--repo', default='.', help='Path to substrate repo root')
    parser.add_argument('--dir', default=None, help='Check only this directory (relative to repo)')
    parser.add_argument('--fix', action='store_true', help='Auto-fix what is fixable')
    parser.add_argument('--dry-run', action='store_true', help='Preview fixes without applying')
    parser.add_argument('--format', choices=['text', 'json'], default='text', help='Output format')
    args = parser.parse_args()

    main(args.repo, args.dir, args.fix, args.dry_run, args.format)
