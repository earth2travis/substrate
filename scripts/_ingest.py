#!/usr/bin/env python3
"""_ingest.py — Mechanical digest generator. No validation, no synthesis.

Responsibilities:
  1. Scan research/raw/*.md
  2. Parse YAML frontmatter (leniently, extract what exists)
  3. Compute sha256 of each raw file body (after frontmatter)
  4. Detect new, changed, and unchanged files vs previous run
  5. Detect orphaned findings whose raw source was deleted
  6. Write a machine-readable digest JSON for the agent to consume

What this script does NOT do:
  - Validate frontmatter against SCHEMA.md (that's _lint.py)
  - Write findings/ or insights/
  - Auto-tag, auto-promote, or synthesize
  - Entity resolution

Those are agent responsibilities, handled by the llm-wiki skill.

Usage:
  python3 scripts/_ingest.py [--repo /path/to/substrate] [--output /path/to/digest.json]
  python3 scripts/_ingest.py --repo /path/to/substrate --output /path/to/digest.json

The digest JSON is consumed by the agent to decide what to ingest next.
"""

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

RAW_DIR = "research/raw"
FINDINGS_DIR = "research/findings"
STATE_DIR = ".ingest-state"
STATE_FILE = "hashes.json"

# ---------------------------------------------------------------------------
# Minimal YAML parser (stdlib only — no external deps)
# ---------------------------------------------------------------------------

def parse_yaml_block(text: str) -> dict:
    """Parse flat YAML frontmatter. Handles key: value, lists, quoted strings."""
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


# ---------------------------------------------------------------------------
# Frontmatter extraction
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n(.*)', re.DOTALL)


def extract_frontmatter(text: str) -> tuple[Optional[dict], str, bool]:
    """Extract YAML frontmatter and body. Returns (fm, body, has_fm)."""
    m = FRONTMATTER_RE.match(text)
    if m:
        return parse_yaml_block(m.group(1)), m.group(2), True
    return None, text, False


def compute_sha256(text: str) -> str:
    """Compute sha256 of text content."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def normalize_filename(stem: str) -> str:
    return stem.replace('_', '-').lower()


@dataclass
class RawFileDigest:
    """Lightweight digest of a raw file for agent consumption."""
    filename: str
    stem: str
    has_frontmatter: bool
    title: Optional[str] = None
    tags: Optional[list] = None
    source_url: Optional[str] = None
    created: Optional[str] = None
    updated: Optional[str] = None
    sha256: str = ""
    is_html: bool = False
    no_ingest: bool = False


def extract_source_url(fm: dict, body: str) -> Optional[str]:
    """Extract source URL from frontmatter or body."""
    # Try frontmatter first
    for key in ('source_url', 'source', 'url', 'origin'):
        val = fm.get(key)
        if val and isinstance(val, str) and val.strip():
            return val.strip()
        if val and isinstance(val, list) and val:
            first = val[0]
            if isinstance(first, str) and first.strip():
                return first.strip()

    # Try body (common patterns in scraped content)
    patterns = [
        r'\*\*Source:\*\*\s*(https?://[^\s\n]+)',
        r'Source:\s*(https?://[^\s\n]+)',
        r'\[Source\]\((https?://[^)]+)\)',
        r'(https?://(?:www\.)?x\.com/\S+)',
        r'(https?://(?:www\.)?twitter\.com/\S+)',
        r'(https?://(?:www\.)?github\.com/\S+)',
        r'(https?://(?:arxiv\.org|papers\.ssrn\.com)/\S+)',
    ]
    for pat in patterns:
        m = re.search(pat, body, re.IGNORECASE)
        if m:
            return m.group(1)

    return None


def extract_title(fm: dict, body: str, filename: str) -> str:
    """Extract title from frontmatter, H1, or filename."""
    if fm.get('title'):
        return str(fm['title'])
    h1 = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
    if h1:
        return h1.group(1).strip()
    return filename.replace('-', ' ').replace('_', ' ').title()


def process_raw_file(path: Path) -> RawFileDigest:
    """Read and digest a single raw file."""
    text = path.read_text(encoding='utf-8', errors='replace')
    fm, body, has_fm = extract_frontmatter(text)
    fm = fm or {}

    # Compute sha256 of body (after frontmatter), per llm-wiki skill spec
    sha = compute_sha256(body)

    # Detect HTML
    is_html = bool(re.match(r'\s*<!DOCTYPE', body, re.IGNORECASE)) or body[:500].count('<html') > 0

    # Detect no-ingest flag
    no_ingest = False
    if has_fm:
        flag = str(fm.get('no-ingest', '')).lower()
        no_ingest = flag in ('true', 'yes', '1')

    return RawFileDigest(
        filename=path.name,
        stem=normalize_filename(path.stem),
        has_frontmatter=has_fm,
        title=extract_title(fm, body, path.name),
        tags=fm.get('tags') if isinstance(fm.get('tags'), list) else None,
        source_url=extract_source_url(fm, body),
        created=fm.get('created') or fm.get('date'),
        updated=fm.get('updated'),
        sha256=sha,
        is_html=is_html,
        no_ingest=no_ingest,
    )


# ---------------------------------------------------------------------------
# State management
# ---------------------------------------------------------------------------

def load_previous_hashes(state_path: Path) -> dict:
    """Load previous run's sha256 hashes."""
    if state_path.exists():
        try:
            return json.loads(state_path.read_text(encoding='utf-8'))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def save_hashes(state_path: Path, hashes: dict):
    """Save current run's hashes for next comparison."""
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(hashes, indent=2, sort_keys=True), encoding='utf-8')


# ---------------------------------------------------------------------------
# Orphan detection
# ---------------------------------------------------------------------------

def find_orphaned_findings(raw_dir: Path, findings_dir: Path) -> list[Path]:
    """Find findings whose raw source no longer exists."""
    if not findings_dir.exists():
        return []

    raw_stems = {normalize_filename(p.stem) for p in raw_dir.glob('*.md')}
    orphans = []

    for finding in findings_dir.glob('*.md'):
        stem = normalize_filename(finding.stem)
        if stem not in raw_stems:
            orphans.append(finding)

    return orphans


# ---------------------------------------------------------------------------
# Digest generation
# ---------------------------------------------------------------------------

def build_digest(repo: Path, raw_files: list[RawFileDigest]) -> dict:
    """Build the machine-readable digest."""
    state_path = repo / STATE_DIR / STATE_FILE
    prev_hashes = load_previous_hashes(state_path)

    new_files = []
    changed_files = []
    unchanged_files = []
    html_files = []
    no_ingest_files = []
    current_hashes = {}

    for rf in raw_files:
        current_hashes[rf.stem] = rf.sha256

        if rf.is_html:
            html_files.append(rf.filename)
            continue

        if rf.no_ingest:
            no_ingest_files.append(rf.filename)
            continue

        if rf.stem not in prev_hashes:
            new_files.append(rf.filename)
        elif prev_hashes[rf.stem] != rf.sha256:
            changed_files.append(rf.filename)
        else:
            unchanged_files.append(rf.filename)

    # Detect orphans
    orphans = find_orphaned_findings(repo / RAW_DIR, repo / FINDINGS_DIR)

    # Save hashes
    save_hashes(state_path, current_hashes)

    return {
        "run_id": datetime.now(timezone.utc).isoformat(),
        "repo": str(repo),
        "raw_scanned": len(raw_files),
        "new_files": new_files,
        "changed_files": changed_files,
        "unchanged_files": unchanged_files,
        "html_excluded": html_files,
        "no_ingest_excluded": no_ingest_files,
        "orphan_findings": [str(p.name) for p in orphans],
        "files": [
            {
                "filename": rf.filename,
                "stem": rf.stem,
                "has_frontmatter": rf.has_frontmatter,
                "title": rf.title,
                "tags": rf.tags,
                "source_url": rf.source_url,
                "created": rf.created,
                "updated": rf.updated,
                "sha256": rf.sha256,
                "is_html": rf.is_html,
                "no_ingest": rf.no_ingest,
            }
            for rf in raw_files
        ],
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(repo_path: str, output_path: Optional[str] = None):
    repo = Path(repo_path)
    raw_dir = repo / RAW_DIR

    if not raw_dir.exists():
        print(f"ERROR: {raw_dir} not found", file=sys.stderr)
        sys.exit(1)

    # Process all raw files
    raw_files = [process_raw_file(p) for p in sorted(raw_dir.glob('*.md'))]

    # Build digest
    digest = build_digest(repo, raw_files)

    # Output
    digest_json = json.dumps(digest, indent=2, sort_keys=False)

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(digest_json, encoding='utf-8')
        print(f"Digest written to: {out}")
    else:
        print(digest_json)

    # Summary to stderr
    new = len(digest["new_files"])
    changed = len(digest["changed_files"])
    unchanged = len(digest["unchanged_files"])
    orphans = len(digest["orphan_findings"])
    html = len(digest["html_excluded"])
    no_ingest = len(digest["no_ingest_excluded"])
    total_valid = new + changed + unchanged

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"Substrate Ingest Digest", file=sys.stderr)
    print(f"  Raw files scanned:    {digest['raw_scanned']}", file=sys.stderr)
    print(f"  Valid (non-HTML):     {total_valid}", file=sys.stderr)
    print(f"  New:                  {new}", file=sys.stderr)
    print(f"  Changed (drift):      {changed}", file=sys.stderr)
    print(f"  Unchanged:            {unchanged}", file=sys.stderr)
    print(f"  HTML excluded:        {html}", file=sys.stderr)
    print(f"  no-ingest excluded:   {no_ingest}", file=sys.stderr)
    print(f"  Orphan findings:      {orphans}", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)

    if orphans > 0:
        print(f"\nNOTE: {orphans} orphaned finding(s) detected. Agent will decide whether to remove them.", file=sys.stderr)

    sys.exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Substrate ingest digest generator')
    parser.add_argument('--repo', default='.', help='Path to substrate repo root')
    parser.add_argument('--output', default=None, help='Path to write digest JSON (default: stdout)')
    args = parser.parse_args()

    main(args.repo, args.output)
