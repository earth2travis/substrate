---
title: "Linting Specification"
date: 2026-04-22
status: "review"
version: "1.0"
---

# Linting Specification (`_lint.py`)

## Purpose

Enforce consistency across all Markdown files in the repo. The linter catches structural problems before they compound in the knowledge graph.

## Rules

| Rule | Severity | Check |
|---|---|---|
| `fm-missing` | ERROR | File has no YAML frontmatter block |
| `fm-title-missing` | ERROR | Frontmatter exists but has no `title` field |
| `fm-tags-empty` | WARNING | `tags` field exists but is empty or `[]` |
| `fm-related-missing` | WARNING | No `related` field or fewer than 2 wikilinks |
| `naming-convention` | ERROR | Filename contains underscores, spaces, or uppercase |
| `broken-wikilink` | ERROR | `[[page-name]]` points to no `.md` file in the repo |
| `orphan-finding` | WARNING | Finding exists but raw source is deleted |
| `no-h1` | INFO | No top-level `# Heading` in the body |
| `duplicate-title` | ERROR | Two files share the same `title` in frontmatter |
| `html-scrape` | ERROR | File contains `<html>` or `<!DOCTYPE` — raw HTML should not be in raw/ |

## Output

Structured report to stdout:

```
[ERROR] research/raw/some_file.md: fm-title-missing — no title in frontmatter
[WARNING] insights/concepts/foo-bar.md: fm-related-missing — 0 related links
[BROKEN] insights/entities/baz.md: broken-wikilink — [[missing-page]]
```

Exit code 0 if no errors (warnings OK). Exit code 1 if any ERRORs exist.

## Auto-fix behavior

The linter supports `--fix` for certain rules:

- `naming-convention`: Rename the file on disk (requires `git mv`)
- `fm-tags-empty`: Derive tags from strict phrase matching (same logic as ingest)
- `html-scrape`: Flag the file for manual review; move to `research/raw/` exclusion list

Non-fixable rules (must be manual): `broken-wikilink`, `duplicate-title`, `fm-missing` (if body is empty).

## Usage

```bash
python3 scripts/_lint.py                          # Check all files
python3 scripts/_lint.py --dir research/raw/      # Check specific directory
python3 scripts/_lint.py --fix                    # Auto-fix what it can
python3 scripts/_lint.py --format json            # Machine-readable output
```

## Integration

The linter runs:

1. On every PR (pre-merge check)
2. As part of the daily cron pipeline (before ingest)
3. On demand by agents before committing knowledge files
