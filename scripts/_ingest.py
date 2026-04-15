#!/usr/bin/env python3
"""_ingest.py — Read raw sources, normalize frontmatter, find relationships,
write findings and promote to insights when cross-file patterns emerge.

Usage:
  python3 scripts/_ingest.py [--dry-run] [--repo /path/to/repo]

The pipeline:
  1. Scan research/raw/*.md
  2. Parse YAML frontmatter (or infer if missing)
  3. Normalize to SCHEMA: title, tags, related, source
  4. Cross-reference files to auto-populate related links
  5. Write normalized findings → research/findings/
  6. Promote to insights/ when a topic appears in 2+ findings

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
    """Minimal YAML parser for frontmatter. Handles scalars, lists, simple
    nested structures. Good enough for our frontmatter shapes."""
    result = {}
    if not text.strip():
        return result

    current_key = None
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue

        # New key-value pair
        if ':' in stripped and not stripped.startswith('-'):
            key, _, value = stripped.partition(':')
            key = key.strip()
            value = value.strip()

            # Inline list: tags: [a, b, c]
            if value.startswith('['):
                items = value.strip('[]').split(',')
                result[key] = [i.strip().strip('"').strip("'") for i in items if i.strip()]
                current_key = None
            # Inline list on next lines (starts an indented list)
            elif value == '':
                current_key = key
                result[key] = []
            # Quoted string
            elif value.startswith('"') or value.startswith("'"):
                result[key] = value.strip('"').strip("'")
                current_key = None
            # Unquoted value
            else:
                result[key] = value
                current_key = None
        # List item under current key
        elif stripped.startswith('- ') and current_key is not None:
            item = stripped[2:].strip().strip('"').strip("'")
            if isinstance(result.get(current_key), list):
                result[current_key].append(item)

    return result


def yaml_dump(data: dict) -> str:
    """Serialize a flat dict (with optional list values) to YAML."""
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
            # Quote values that might be interpreted specially
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
    """Normalize a filename stem to kebab-case with hyphens only.
    SCHEMA: kebab-case, lowercase. Date-prefixed files use hyphens, not underscores.
    e.g. '2026-04-08_bergson...' -> '2026-04-08-bergson...'
    """
    # Replace underscores with hyphens (except within date prefix YYYY-MM-DD)
    # The date prefix always ends with a _ or digit, then concept
    # Replace all underscores with hyphens
    return stem.replace('_', '-').lower()


@dataclass
class RawFile:
    path: Path
    filename: str
    stem: str                            # normalized stem (kebab-case, hyphens)
    raw_fm: dict                         # whatever frontmatter existed
    body: str                            # content after frontmatter
    title: str                          # normalized title
    tags: list[str]                     # normalized tags
    related: list[str]                  # wikilinks to related files
    source: str                         # path to raw file
    is_html: bool = False               # true if file starts with HTML
    has_frontmatter: bool = False       # true if had YAML frontmatter


def read_raw_file(path: Path) -> RawFile:
    text = path.read_text(encoding='utf-8', errors='replace')

    # Detect HTML scrapes
    is_html = bool(re.match(r'\s*<!DOCTYPE', text, re.IGNORECASE)) or text.count('<html') > 0

    # Extract frontmatter if present
    fm = {}
    body = text
    has_fm = False

    m = FRONTMATTER_RE.match(text)
    if m:
        has_fm = True
        fm = parse_yaml_block(m.group(1))
        body = m.group(2)

    # Normalize title
    title = fm.get('title', '')
    if not title:
        # Try to extract from first H1
        h1 = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
        if h1:
            title = h1.group(1).strip()
        else:
            # Derive from filename
            title = path.stem.replace('-', ' ').replace('_', ' ').title()

    # Normalize tags
    tags = []
    for fk in ('tags', 'tag'):
        if fk in fm and isinstance(fm[fk], list):
            tags.extend(fm[fk])
            break

    # Normalize related
    related = []
    for fk in ('related', 'links', 'see_also'):
        if fk in fm and isinstance(fm[fk], list):
            related.extend(fm[fk])
            break

    # Normalize source
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
# Auto-tagging: scan body text for known themes
# ---------------------------------------------------------------------------

TAG_PATTERNS: list[tuple[str, list[str]]] = [
    # Process philosophy
    ('process-philosophy', ['whitehead', 'bergson', 'deleuze', 'concrescence',
                            'prehension', 'duration', 'actual occasion',
                            'élán vital', 'elan vital', 'process and reality',
                            'creative evolution', 'nagarjuna',
                            'dependent origination', 'sunyata', 'emptiness']),
    ('postmodernism', ['baudrillard', 'simulacra', 'hyperreality', 'simulacra']),

    # Lean / manufacturing
    ('lean-manufacturing', ['toyota production system', 'just-in-time', 'jit',
                           'kaizen', 'jidoka', 'kanban', 'obeya', 'andōn',
                           'lean production', 'taichi ohno', 'seven wastes']),

    # Software engineering
    ('software-engineering', ['continuous delivery', 'devops', 'dora metrics',
                             'spec-driven development', 'lean software']),

    # Knowledge management
    ('knowledge-management', ['wiki', 'knowledge base', 'llm', 'karpathy',
                              'second brain', 'obsidian', 'memex',
                              'rag', 'retrieval', 'graph']),

    # AI / agents
    ('ai-agents', ['agent', 'llm', 'openai', 'frontier', 'hermes',
                   'openclaw', 'codex', 'nous research']),

    # Systems thinking
    ('systems-thinking', ['system', 'feedback', 'network', 'architecture',
                          'orchestration', 'rhizome']),
]


def auto_tag(body: str, title: str) -> list[str]:
    """Derive tags from body text and title using keyword matching."""
    text = (title + ' ' + body).lower()
    found = set()
    for tag, keywords in TAG_PATTERNS:
        if any(kw in text for kw in keywords):
            found.add(tag)

    if not found:
        found.add('general')

    return sorted(found)


# ---------------------------------------------------------------------------
# Cross-reference discovery
# ---------------------------------------------------------------------------

def find_related(raw_files: list[RawFile]) -> dict[str, list[str]]:
    """For each file, find 2+ related peers by:
    1. Already-existing wikilinks in the body
    2. Shared tags
    3. Title/keyword matching against other file titles
    """
    # Build index: normalized stem → RawFile
    by_stem = {}
    for rf in raw_files:
        by_stem[rf.stem] = rf

    # Collect all wikilinks that appear in bodies
    wikilinks_re = re.compile(r'\[\[([^\]]+)\]\]')

    related_map: dict[str, list[str]] = {}

    for rf in raw_files:
        links = set()

        # 1. Existing wikilinks in body
        for match in wikilinks_re.finditer(rf.body):
            link = match.group(1).strip()
            # Convert wikilink to normalized filename stem
            link_stem = normalize_filename(link.lower().replace(' ', '-'))
            if link_stem in by_stem:
                links.add(by_stem[link_stem].stem)

        # 2. Shared tags (if file already has tags)
        if rf.tags:
            for other in raw_files:
                if other.stem == rf.stem:
                    continue
                if set(rf.tags) & set(other.tags):
                    links.add(other.stem)

        # 3. Existing related list from frontmatter
        for rel in rf.related:
            rel_stem = normalize_filename(rel.lower().replace(' ', '-').split('/')[-1].split('.')[0])
            if rel_stem in by_stem:
                links.add(by_stem[rel_stem].stem)

        # Ensure at least 2 links (SCHEMA minimum)
        if len(links) < 2:
            # Fallback: find files that mention each other's concepts
            for other in raw_files:
                if other.stem == rf.stem:
                    continue
                if other.stem.replace('-', ' ') in rf.body.lower()[:500]:
                    links.add(other.stem)
                if rf.stem.replace('-', ' ') in other.body.lower()[:1000]:
                    links.add(other.stem)
                if len(links) >= 4:
                    break

        related_map[rf.stem] = sorted(list(links))[:4]

    return related_map


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

    # 1. Read all raw files
    raw_files = [read_raw_file(p) for p in sorted(raw_dir.glob('*.md'))]

    print(f"Found {len(raw_files)} raw files in {raw_dir}")

    # Classify
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

    # 2. Auto-tag files missing useful tags
    for rf in valid_files:
        if not rf.tags:
            rf.tags = auto_tag(rf.body, rf.title)

    # 3. Discover cross-references
    related_map = find_related(valid_files)

    # 4. Collect findings — write normalized frontmatter + body
    findings_written = 0
    tag_index = defaultdict(list)   # tag → filenames
    topic_index = defaultdict(list) # topic words → filenames

    for rf in valid_files:
        # Build normalized frontmatter
        fm = {
            'title': rf.title,
            'tags': rf.tags,
            'related': ['[[' + slug + ']]' for slug in related_map.get(rf.path.stem, [])],
            'source': f'research/raw/{rf.filename}',
        }

        output = yaml_dump(fm) + '\n\n' + rf.body.lstrip('\n')

        # Write finding using normalized stem (SCHEMA: kebab-case, hyphens only)
        out_path = find_dir / f"{rf.stem}.md"

        if dry_run:
            print(f"\n[Dry-run] Would write: {out_path}")
            print(f"  Frontmatter: {fm}")
            findings_written += 1
        else:
            out_path.write_text(output, encoding='utf-8')
            print(f"Wrote finding: {out_path}")
            findings_written += 1

        # Update indexes for promotion logic
        for tag in rf.tags:
            tag_index[tag].append(rf.stem)

        # Scan for key topic mentions (for promoting to concepts/entities)
        for other in valid_files:
            if other.stem == rf.stem:
                continue
            other_title = other.stem.replace('-', ' ').lower()
            if other_title in rf.body.lower():
                topic_index[other.stem].append(rf.stem)

    print(f"\nWrote {findings_written} findings to {find_dir}")

    # 5. Promote to insights/ — when a topic appears in 2+ findings
    promoted = 0
    for stem, mentioned_by in topic_index.items():
        if len(mentioned_by) >= 2:  # SCHEMA: "appears in 2+ findings"
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
