---
title: "Security Scan Specification"
date: 2026-04-22
status: "review"
version: "1.0"
---

# Security Scan Specification (`_scan.py`)

## Purpose

Detect security regressions in the Substrate — primarily around secrets, unsafe tooling patterns, and policy violations. The Substrate is the shared brain; if it's poisoned, all agents trust the poison.

## Checks

| Check | Description |
|---|---|
| `leaked-secret` | Scan for patterns matching API keys, tokens, passwords in markdown files |
| `dangerous-command` | Flag markdown containing patterns like `rm -rf`, `DROP TABLE`, `curl | bash` |
| `external-link-rot` | Check external URLs in source fields for 404s (warning only) |
| `policy-violation` | Flag files not following SCHEMA.md conventions (redundant with linter) |
| `stale-source` | Flag findings whose raw source was modified more than N days ago |
| `circular-reference` | Detect wikilink cycles (A→B→C→A) that waste context budget |
| `overlinked` | Files with >10 related links (likely spammy auto-linking) |

## Secret Detection Patterns

```python
SECRET_PATTERNS = [
    r'(?i)(api[_-]?key|token|password|secret)\s*[:=]\s*["\']?[a-zA-Z0-9]{16,}',
    r'ghp_[a-zA-Z0-9]{36,}',           # GitHub PAT
    r'sk-[a-zA-Z0-9]{20,}',            # OpenAI/DashScope keys
    r'(?i)bearer\s+[a-zA-Z0-9\-._~+/]+=*',  # Bearer tokens
    r'BEGIN\s+(RSA|EC|DSA|OPENSSH)\s+PRIVATE KEY',  # Private keys
]
```

## Output

```
[CRITICAL] research/raw/some-file.md: leaked-secret — found pattern matching GitHub PAT
[WARNING] insights/concepts/foo.md: overlinked — 14 related links (max 10)
[WARNING] research/findings/bar.md: stale-source — raw source last modified 45 days ago
[INFO] No circular references detected
```

Exit code 0 if no CRITICALs. Exit code 1 if any CRITICAL exists.

## Usage

```bash
python3 scripts/_scan.py                       # Run all checks
python3 scripts/_scan.py --only leaked-secret  # Single check
python3 scripts/_scan.py --format json          # Machine-readable
```

## Integration

Security scan runs:

1. On every PR merge
2. Daily as a cron job
3. Before any automated promotion to insights/
