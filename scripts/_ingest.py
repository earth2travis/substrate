#!/usr/bin/env python3
"""_ingest.py — Read raw sources, normalize frontmatter, find relationships,
write findings and promote to insights when cross-file patterns emerge.

Usage:
  python3 scripts/_ingest.py [--dry-run] [--repo /path/to/ansible]

The pipeline:
  1. Scan research/raw/*.md
  2. Parse YAML frontmatter (or infer if missing)
  3. Normalize to SCHEMA: title, tags, related, source
  4. Cross-reference files to auto-populate related links
  5. Write normalized findings → research/findings/
  6. Promote to insights/ when a topic appears in 2+ findings
  7. Orphan cleanup: remove findings/ for deleted raw sources

Raw files are never modified.
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# YAML parsing (stdlib only — no pyyaml)
# ---------------------------------------------------------------------------

def parse_yaml_block(text: str) -> dict:
    """Minimal YAML parser for frontmatter."""
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
    """Serialize a flat dict to YAML."""
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
# File I/O and frontmatter extraction
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n(.*)', re.DOTALL)


def normalize_filename(stem: str) -> str:
    """Normalize a filename stem to kebab-case with hyphens only."""
    return stem.replace('_', '-').lower()


@dataclass
class RawFile:
    path: Path
    filename: str
    stem: str                            # normalized stem (kebab-case, hyphens)
    raw_fm: dict                         # whatever frontmatter existed
    body: str                            # content after frontmatter
    title: str
    tags: list[str]
    related: list[str]
    source: str
    is_html: bool = False
    has_frontmatter: bool = False


def read_raw_file(path: Path) -> RawFile:
    text = path.read_text(encoding='utf-8', errors='replace')

    is_html = bool(re.match(r'\s*<!DOCTYPE', text, re.IGNORECASE)) or text.count('<html') > 0

    fm = {}
    body = text
    has_fm = False

    m = FRONTMATTER_RE.match(text)
    if m:
        has_fm = True
        fm = parse_yaml_block(m.group(1))
        body = m.group(2)

    title = fm.get('title', '')
    if not title:
        h1 = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
        if h1:
            title = h1.group(1).strip()
        else:
            title = path.stem.replace('-', ' ').replace('_', ' ').title()

    tags = []
    for fk in ('tags', 'tag'):
        if fk in fm and isinstance(fm[fk], list):
            tags.extend(fm[fk])
            break

    related = []
    for fk in ('related', 'links', 'see_also'):
        if fk in fm and isinstance(fm[fk], list):
            related.extend(fm[fk])
            break

    source = fm.get('source', fm.get('source_url', fm.get('url', '')))
    if not source:
        source = f'research/raw/{path.name}'

    return RawFile(
        path=path,
        filename=path.name,
        stem=normalize_filename(path.stem),
        raw_fm=fm,
        body=body,
        title=title,
        tags=tags,
        related=related,
        source=source,
        is_html=is_html,
        has_frontmatter=has_fm,
    )


# ---------------------------------------------------------------------------
# Auto-tagging: strict phrase matching, no single-word keywords
# ---------------------------------------------------------------------------

TAG_PATTERNS: list[tuple[str, list[str]]] = [
    # Process philosophy — must be full phrases, no single words
    ('process-philosophy', [
        'process philosophy', 'process and reality', 'creative evolution',
        'philosophy of organism', 'actual occasion', 'actual occasions',
        'élán vital', 'elan vital', 'duration (durée)', 'durée',
        'dependent origination', 'pratītyasamutpāda',
        'middle way', 'mulamadhyamakakarika',
    ]),

    # Postmodernism / French theory
    ('postmodernism', [
        'simulacra and simulation', 'hyperreality',
        'differential and repetition', 'rhizomatic',
        'simulacres et simulation',
    ]),

    # Lean manufacturing / TPS
    ('lean-manufacturing', [
        'toyota production system', 'just-in-time',
        'heijunka', 'jidoka', 'andon',
        'lean production', 'taichi ohno',
        'seven wastes', 'muda', 'mura', 'muri',
    ]),

    # Software engineering
    ('software-engineering', [
        'continuous delivery', 'continuous deployment',
        'spec-driven development', 'dora metrics',
        'feature flags', 'deployment pipeline',
    ]),

    # Knowledge management / LLM wiki
    ('knowledge-management', [
        'knowledge base', 'llm wiki', 'second brain',
        'knowledge graph', 'institutional memory',
    ]),

    # AI agents
    ('ai-agents', [
        'coding agent', 'ai agent', 'autonomous agent',
        'agent platform', 'agent company', 'agentic',
        'multi-agent', 'agent orchestration',
        'context stack', 'context window',
    ]),

    # Claude / Anthropic
    ('claude-anthropic', [
        'claude code', 'claude opus', 'anthropic',
    ]),

    # OpenAI
    ('openai', [
        'openai', 'gpt-4', 'gpt-5',
    ]),

    # Security / ops
    ('security-ops', [
        'opsec', 'server hardening', 'prompt injection',
        'tool provisioning', 'security crisis',
    ]),
]

# Keywords that are too broad to use as tag triggers.
# These appear in almost every file and are meaningless as discriminators.
NOISE_KEYWORDS = {
    'agent', 'system', 'agent', 'llm', 'wiki', 'knowledge',
    'api', 'github', 'protocol', 'model', 'tool', 'platform',
    'open', 'research', 'architecture', 'design', 'project',
    'issue', 'memory', 'context', 'prompt',
}


def auto_tag(body: str, title: str) -> list[str]:
    """Derive tags from body text using strict phrase matching.
    
    Only multi-word phrases are used. Single-word keywords are ignored
    because they're too broad and produce meaningless tags.
    """
    text = (title + ' ' + body).lower()
    found = set()
    
    for tag, phrases in TAG_PATTERNS:
        for phrase in phrases:
            # Use word boundary matching for multi-word phrases
            # This avoids "agent" matching inside "management"
            pattern = r'\b' + re.escape(phrase) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                found.add(tag)
                break  # One match per tag is enough

    if not found:
        found.add('general')

    return sorted(found)


# ---------------------------------------------------------------------------
# Cross-reference discovery: wikilinks first, title mentions second
# ---------------------------------------------------------------------------

def find_related(raw_files: list[RawFile]) -> dict[str, list[str]]:
    """For each file, find 2+ related peers by:
    1. Existing wikilinks in the body (primary signal)
    2. Title mentions in body text (secondary signal)
    
    NO shared-tag linking — tags are too noisy and create false connections.
    """
    by_stem = {}
    for rf in raw_files:
        by_stem[rf.stem] = rf

    wikilinks_re = re.compile(r'\[\[([^\]]+)\]\]')

    related_map: dict[str, list[str]] = {}

    for rf in raw_files:
        links = set()

        # 1. Existing wikilinks in body (strongest signal)
        for match in wikilinks_re.finditer(rf.body):
            link = match.group(1).strip()
            # Try exact match first
            link_stem = normalize_filename(link.lower().replace(' ', '-'))
            if link_stem in by_stem:
                links.add(by_stem[link_stem].stem)
            else:
                # Try partial match — the wikilink might just be the concept name
                for stem, other in by_stem.items():
                    concept_name = stem.replace('-', ' ').lower()
                    if link.lower() in concept_name or concept_name in link.lower():
                        links.add(stem)

        # 2. Title mentions in body (weaker but useful for files without wikilinks)
        if len(links) < 2:
            candidates = []
            for other in raw_files:
                if other.stem == rf.stem:
                    continue
                concept = other.stem.replace('-', ' ').lower()
                # Check if current file mentions this other concept
                if concept in rf.body.lower():
                    # Score by how many times it's mentioned (more hits = more relevant)
                    count = rf.body.lower().count(concept)
                    candidates.append((count, other.stem))

            # Sort by mention frequency (most relevant first), cap at 4
            candidates.sort(reverse=True, key=lambda x: x[0])
            for _, stem in candidates[:4]:
                links.add(stem)

        related_map[rf.stem] = sorted(list(links))[:4]

    return related_map


# ---------------------------------------------------------------------------
# Orphan cleanup
# ---------------------------------------------------------------------------

def cleanup_orphans(raw_dir: Path, find_dir: Path, insights_dir: Path):
    """Remove findings/ and insights/ files whose raw source no longer exists."""
    raw_stems = set()
    for p in raw_dir.glob('*.md'):
        raw_stems.add(normalize_filename(p.stem))

    removed = 0

    # Clean findings/
    if find_dir.exists():
        for p in find_dir.glob('*.md'):
            stem = normalize_filename(p.stem)
            if stem not in raw_stems:
                p.unlink()
                removed += 1
                print(f"  Orphan removed: {p}")

    # Clean insights/
    for subdir in ['entities', 'concepts', 'comparisons']:
        insight_dir = insights_dir / subdir
        if insight_dir.exists():
            for p in insight_dir.glob('*.md'):
                stem = normalize_filename(p.stem)
                if stem not in raw_stems:
                    p.unlink()
                    removed += 1
                    print(f"  Orphan removed: {p}")

    return removed


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def main(repo_path: str, dry_run: bool = False):
    repo = Path(repo_path)
    raw_dir = repo / 'research' / 'raw'
    find_dir = repo / 'research' / 'findings'
    insights_dir = repo / 'insights'

    if not raw_dir.exists():
        print(f"ERROR: {raw_dir} not found", file=sys.stderr)
        sys.exit(1)

    # Ensure output dirs exist
    find_dir.mkdir(parents=True, exist_ok=True)
    (insights_dir / 'entities').mkdir(parents=True, exist_ok=True)
    (insights_dir / 'concepts').mkdir(parents=True, exist_ok=True)
    (insights_dir / 'comparisons').mkdir(parents=True, exist_ok=True)

    # 0. Orphan cleanup — remove findings without raw sources
    if not dry_run:
        orphans = cleanup_orphans(raw_dir, find_dir, insights_dir)
        if orphans:
            print(f"Removed {orphans} orphaned files")

    # 1. Read all raw files
    raw_files = [read_raw_file(p) for p in sorted(raw_dir.glob('*.md'))]

    print(f"Found {len(raw_files)} raw files in {raw_dir}")

    html_files = [rf for rf in raw_files if rf.is_html]
    no_fm = [rf for rf in raw_files if not rf.has_frontmatter]
    has_fm = [rf for rf in raw_files if rf.has_frontmatter]

    print(f"  - With frontmatter:        {len(has_fm)}")
    print(f"  - Without frontmatter:     {len(no_fm)}")
    print(f"  - HTML scrapes (skipped):  {len(html_files)}")

    if html_files:
        print("\n  HTML files (excluded from pipeline):")
        for hf in html_files:
            print(f"    - {hf.filename}")

    valid_files = [rf for rf in raw_files if not rf.is_html]

    # 2. Auto-tag files that don't already have tags
    for rf in valid_files:
        if not rf.tags:
            rf.tags = auto_tag(rf.body, rf.title)

    # 3. Discover cross-references
    related_map = find_related(valid_files)

    # 4. Write findings
    findings_written = 0
    topic_index = defaultdict(list)

    for rf in valid_files:
        fm = {
            'title': rf.title,
            'tags': rf.tags,
            'related': ['[[' + slug + ']]' for slug in related_map.get(rf.stem, [])],
            'source': f'research/raw/{rf.filename}',
        }

        output = yaml_dump(fm) + '\n\n' + rf.body.lstrip('\n')
        out_path = find_dir / f"{rf.stem}.md"

        if dry_run:
            print(f"\n[Dry-run] Would write: {out_path}")
            print(f"  Frontmatter: {fm}")
            findings_written += 1
        else:
            out_path.write_text(output, encoding='utf-8')
            print(f"Wrote finding: {out_path}")
            findings_written += 1

        # Track topic mentions for promotion
        for other in valid_files:
            if other.stem == rf.stem:
                continue
            other_concept = other.stem.replace('-', ' ').lower()
            if other_concept in rf.body.lower():
                topic_index[other.stem].append(rf.stem)

    print(f"\nWrote {findings_written} findings to {find_dir}")

    # 5. Promote to insights/ — when a topic appears in 2+ findings
    promoted = 0
    for stem, mentioned_by in topic_index.items():
        if len(mentioned_by) >= 2:
            canon = next((rf for rf in valid_files if rf.stem == stem), None)

            if canon and find_dir.exists():
                insight_filename = f"{canon.stem}.md"

                person_indicators = {'person', 'philosopher', 'researcher', 'scientist', 'engineer', 'author', 'developer'}

                is_entity = bool(person_indicators & set(canon.tags)) or any(
                    kw in canon.title.lower() for kw in ['production system', 'philosophy', 'theorem']
                )

                if is_entity:
                    insight_path = insights_dir / 'entities' / insight_filename
                else:
                    insight_path = insights_dir / 'concepts' / insight_filename

                if insight_path.exists() and not dry_run:
                    continue

                related = ['[[' + s + ']]' for s in related_map.get(stem, [])[:4]]
                insight_fm = {
                    'title': canon.title,
                    'tags': canon.tags,
                    'related': related,
                    'source': canon.source,
                }

                insight_body = yaml_dump(insight_fm) + '\n\n' + canon.body.lstrip('\n')

                if dry_run:
                    print(f"\n[Dry-run] Would promote: {insight_path}")
                    print(f"  Mentioned in {len(mentioned_by)} findings: {', '.join(mentioned_by)}")
                else:
                    insight_path.write_text(insight_body, encoding='utf-8')
                    print(f"Promoted to insight: {insight_path}")
                promoted += 1

    print(f"Promoted {promoted} files to insights/")

    # 6. Summary
    print(f"\n{'='*60}")
    print(f"Ingest complete.")
    print(f"  Raw files read:    {len(valid_files)}")
    print(f"  HTML skipped:      {len(html_files)}")
    print(f"  Findings written:  {findings_written}")
    print(f"  Insights promoted: {promoted}")
    print(f"{'='*60}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ansible knowledge ingest pipeline')
    parser.add_argument('--repo', default='.', help='Path to ansible repo root')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without writing')
    args = parser.parse_args()

    main(args.repo, args.dry_run)
