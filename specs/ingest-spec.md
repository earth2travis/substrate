---
title: "Ingest Pipeline Specification"
date: 2026-04-22
status: "review"
version: "1.0"
---

# Ingest Pipeline Specification (`_ingest.py`)

## Purpose

Generate a mechanical digest of raw sources for agent-driven synthesis. The ingest script does NOT synthesize knowledge — it provides the machine-readable signal that the synthesis agent consumes.

This is the **hybrid ingest pattern**: scripts handle fast, deterministic mechanical work (sha256 comparison, drift detection). Agents handle semantic work (summarization, cross-referencing, insight promotion).

## Architecture

```
Mechanical layer:    _ingest.py  →  JSON digest
Agent layer:         reads digest →  synthesizes findings →  writes insights
```

The script is cron-friendly, idempotent, and requires only Python stdlib.

## Current Behavior

`_ingest.py` at `scripts/_ingest.py` implements:

1. Scan `research/raw/*.md`
2. Parse YAML frontmatter leniently (extracts what exists; does not validate)
3. Compute sha256 of file body (after frontmatter) for drift detection
4. Compare to previous run's hashes stored in `.ingest-state/`
5. Classify each file as: new, changed, unchanged, html-excluded, no-ingest-excluded
6. Detect orphaned findings (raw source deleted since last run)
7. Write machine-readable JSON digest

**What it does NOT do:**
- Write to `research/findings/` — synthesis is agent-driven
- Auto-tag — semantic tagging requires content understanding
- Cross-reference — wikilink discovery is agent work
- Promote to insights — promotion requires judgment
- Clean orphans — orphans are flagged in digest for manual review

## Digest JSON Structure

```json
{
  "run_id": "2026-05-04T06:00:00Z",
  "repo": "/home/sivart/substrate",
  "raw_scanned": 310,
  "new_files": ["new-source.md"],
  "changed_files": ["updated-source.md"],
  "unchanged_files": ["stable-source.md"],
  "html_excluded": ["bad-scrape.html"],
  "no_ingest_excluded": ["draft.md"],
  "orphan_findings": ["old-finding.md"],
  "files": [
    {
      "filename": "source.md",
      "stem": "source",
      "has_frontmatter": true,
      "title": "Source Title",
      "tags": ["tag-one"],
      "source_url": "https://...",
      "created": "2026-04-10",
      "updated": "2026-04-10",
      "sha256": "...",
      "is_html": false,
      "no_ingest": false
    }
  ]
}
```

The synthesis agent reads this digest, selects files to process, and performs the semantic workflow.

## Usage

```bash
python3 scripts/_ingest.py                          # Full run, digest to stdout
python3 scripts/_ingest.py --output /tmp/digest.json  # Write digest to file
python3 scripts/_ingest.py --dir research/raw/      # Scope to directory
```

## State Cache

Ingest stores per-file sha256 hashes in `.ingest-state/` (gitignored). This enables incremental detection across runs. Delete `.ingest-state/` to force a full re-scan.

## Integration with Agent Synthesis

The cron-driven synthesis workflow:

1. `_ingest.py` runs, emits digest
2. Agent reads digest, identifies new/changed files
3. Agent writes synthesized findings to `research/findings/`
4. Agent creates or updates insight pages in `insights/`
5. Agent updates `INDEX.md` and `log.md`
6. Agent commits to branch `auto/ingest-YYYYMMDD-HHMMSS`
7. Agent opens PR via `gh` CLI

Early exit: if digest shows no new/changed/orphan files, the agent exits clean without creating a branch or PR.

## Historical Note

Earlier versions of `_ingest.py` attempted full synthesis in Python (auto-tagging, phrase matching, orphan cleanup, insight promotion). These were removed because Python cannot do semantic understanding. The current architecture splits mechanical and semantic work at their natural boundary.
