---
title: "GitHub Capabilities Audit: What We Have, What We're Missing"
tags: [github, audit, project-management, automation, gh-cli]
related: [github-as-memory, project-board-configuration, github-practices]
source: research/raw/github-capabilities-audit.md
---


# GitHub Capabilities Audit

## Summary

Comprehensive audit of GitHub feature usage against current practice. Identifies active features, underused capabilities, and ignored features across Projects v2, Issues, Actions, and the gh CLI.

## Key Insights

### Projects v2: Active Features

- Board layout, Status field, and Sub-issues are in active use
- Priority and Size fields are partially adopted (Foundation only)
- Parent issue tracking is available but lightly used

### Projects v2: Underused (High Value)

- **Iteration field:** Creates planning rhythm, enables roadmap view
- **Table layout:** Higher information density than board alone
- **Auto-add items:** Eliminates manual project assignment step
- **Auto-archive:** Keeps active views focused
- **Built-in workflows:** Status automations on close/reopen/merge
- **Multiple views:** Should have 3-5 purpose-built views per project

### Issues: Underused Features

- **Sub-issues (GA April 2025):** Better than checkbox task lists for tracking discrete tasks
- **Issue forms:** YAML-based structured fields for consistent creation
- **Pinned issues:** Up to 3 per repo for high visibility
- **Advanced search:** AND/OR with parentheses via gh CLI
- **Tracked-by relationships:** Shows downstream dependencies

### GitHub Actions: Significant Gap

No Actions configured. Priority automations:

1. Auto-add issues to projects (low effort, high value)
2. Prettier on PR (low effort, high value)
3. Commitlint on PR (low effort, high value)
4. Stale issue bot (low effort, medium value)
5. Weekly digest (medium effort, medium value)

### gh CLI: Underutilized

Current: one alias (`co` → `pr checkout`). Recommended additions:

- `new-issue`: quick issue creation with project assignment
- `my-issues`: list open issues across projects
- `orphans`: find issues not in any project

Extensions worth evaluating: `gh-dash` (terminal dashboard), `gh-poi` (branch cleanup).

### What Not to Automate

- Issue creation (requires judgment)
- Priority assignment (except security/incident labels)
- Complex workflow orchestration (keep YAML under 30 lines)

## Priority Actions

**This week:** Enable built-in automations, add Priority/Size/Area/Cycle fields, create recommended views, pin active issues.

**This month:** Add gh aliases, build Prettier and commitlint Actions, create issue forms, backfill Priority and Area.

**Next quarter:** Stale issue bot, weekly digest, project analytics scripts.
