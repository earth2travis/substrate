---
title: "GitHub Capabilities Audit: What We Have, What We're Missing"
date: 2026-02-28
type: research
tags: [research, project-management, github]
related: [project-board-configuration]
---

# GitHub Capabilities Audit

_Research completed 2026-02-28. Related: issue #302._

## Purpose

Audit every relevant GitHub feature against our current usage. Identify what we are using well, what we are underusing, and what we should ignore.

## GitHub Projects V2

### Features We Use

| Feature               | Status       | Notes                                            |
| --------------------- | ------------ | ------------------------------------------------ |
| Board layout          | ✅ Active    | Default view for all three projects              |
| Status field          | ✅ Active    | Todo, In Progress, Done                          |
| Priority field        | ⚠️ Partial   | Foundation has it, Framing and Operations do not |
| Size field            | ⚠️ Partial   | Foundation only                                  |
| Sub-issues            | ✅ Available | Field exists on all projects, used occasionally  |
| Parent issue tracking | ✅ Available | Field exists on all projects                     |

### Features We Are Not Using

| Feature                | Value for Us | Recommendation                                                                                                                                               |
| ---------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Iteration field**    | High         | Add as "Cycle" to Framing and Operations. Creates planning rhythm, enables roadmap view. See project-board-configuration.md.                                 |
| **Table layout**       | High         | Create table views for triage, backlog, and completed work. Board alone loses information density.                                                           |
| **Roadmap layout**     | Medium       | Useful for planning conversations with [[Ξ2T]]. Requires iteration or date fields.                                                                           |
| **Charts/Insights**    | Medium       | Built-in charts show burn-up, item distribution by field. Useful for retrospectives. Available under project Insights tab.                                   |
| **Auto-add items**     | High         | Configure rules so labeled issues automatically appear in the correct project. Eliminates a manual step from every issue creation.                           |
| **Auto-archive**       | High         | Archive Done items after 14 days. Keeps active views focused.                                                                                                |
| **Built-in workflows** | High         | Status automations on close/reopen/merge. Some may already be enabled; verify and complete the set.                                                          |
| **Multiple views**     | High         | We use one view per project. Should have three to five purpose-built views each. See project-board-configuration.md for specifics.                           |
| **Draft issues**       | Low          | Quick capture directly in the project board without creating a full issue. Useful for brainstorming but could bypass our issue-first process. Use sparingly. |
| **Grouping**           | Medium       | Group table/board views by Area, Priority, or Cycle. Makes patterns visible (e.g., too many items in one area).                                              |
| **Sorting**            | Medium       | Sort by Priority, Size, or date. Should be configured per view.                                                                                              |
| **Saved filters**      | Medium       | Each view saves its filter. Not a separate feature but part of view configuration.                                                                           |

### Features to Ignore

| Feature                | Why Skip                                                                                           |
| ---------------------- | -------------------------------------------------------------------------------------------------- |
| **Tasklists (legacy)** | Being superseded by sub-issues. Do not invest in the older task list syntax.                       |
| **Project templates**  | Useful for orgs spinning up many similar projects. We have three projects. Not worth the overhead. |
| **Copy project**       | Same reasoning.                                                                                    |

## GitHub Issues

### Features We Use Well

- **Labels:** 28 well-organized labels covering type, domain, status, and lifecycle
- **Milestones:** Available, used for grouping toward goals
- **Issue templates:** We have them configured
- **Markdown formatting:** Consistent use of structured issue bodies
- **Cross-references:** Commit messages reference issue numbers

### Features We Are Underusing

| Feature                        | Status                  | Recommendation                                                                                                                                                                                                 |
| ------------------------------ | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sub-issues (GA April 2025)** | Available but light use | Use for any issue that naturally breaks into 2+ discrete tasks. The parent shows completion progress. Better than checkbox task lists because each sub-issue has its own status, labels, and project tracking. |
| **Issue types**                | Not using               | GitHub now supports shared issue types (bug, task, initiative) across repositories. Complements labels. Worth evaluating but not urgent since our labels already serve this function.                          |
| **Pinned issues**              | Not using               | Pin up to 3 issues per repo. Useful for: current focus area, contribution guidelines, or the most important active issue. Low effort, high visibility.                                                         |
| **Issue forms**                | Not using               | YAML-based forms that replace free-text templates with structured fields. Ensures consistent issue creation. Worth building for our most common issue types: task, research, decision.                         |
| **Advanced search**            | Underusing              | GitHub search now supports AND/OR with parentheses. The `gh` CLI exposes this. Powerful for finding patterns: `label:research label:blocked`, `is:open no:project`, etc.                                       |
| **Tracked-by relationships**   | Available               | Issues can show which other issues reference them. Useful for seeing how foundational work supports downstream issues.                                                                                         |

### Features to Ignore

| Feature               | Why Skip                                              |
| --------------------- | ----------------------------------------------------- |
| **Issue transfer**    | Moving issues between repos. We have one repo.        |
| **Issue lock/unlock** | For managing heated public discussions. Not relevant. |

## GitHub Actions

### Current Usage

We have no GitHub Actions configured. This is a significant gap.

### High-Value Automations to Build

| Automation                       | Effort | Value  | Priority                                                                                                                           |
| -------------------------------- | ------ | ------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Auto-add issues to projects**  | Low    | High   | Do first. When an issue is labeled, add it to the appropriate project. Built-in project automation may cover this without Actions. |
| **Auto-label PRs**               | Low    | Medium | Label PRs based on file paths changed (e.g., changes to `research/` get `research` label). Use `actions/labeler`.                  |
| **Stale issue bot**              | Low    | Medium | Flag issues with no activity for 30 days. Standard `actions/stale` action.                                                         |
| **Prettier on PR**               | Low    | High   | Run `npx prettier --check .` on every PR. Catches formatting before merge.                                                         |
| **Commitlint on PR**             | Low    | High   | Validate conventional commit format. We already enforce this manually; automate the check.                                         |
| **Auto-close PR on issue close** | Low    | Low    | If a PR references an issue with `closes #N`, GitHub already handles this natively. No action needed.                              |
| **Weekly digest**                | Medium | Medium | Generate a summary of issues opened/closed/stale per project. Write to a file or post as an issue.                                 |
| **Deploy/publish**               | Medium | Future | When we have something to deploy (site, transmissions), automate it. Not yet needed.                                               |

### What Not to Automate

- **Issue creation.** Issues require judgment about scope, title, and context. Keep this human (or Sivart).
- **Priority assignment.** Automatic priority based on labels sounds appealing but removes the judgment that makes priority meaningful. Exception: security/incident labels should auto-set Urgent.
- **Complex workflow orchestration.** Keep it simple. If an automation needs more than 30 lines of YAML, reconsider whether it is worth the maintenance cost.

## gh CLI

### Current Usage

- Version: 2.86.0 (January 2026, current)
- One alias: `co` → `pr checkout`
- Used for: issue creation, project management, PR creation, basic queries

### Underutilized Capabilities

**Aliases worth adding:**

```bash
# Quick issue creation with project assignment
gh alias set new-issue 'issue create --label "$1" --project "Framing"'

# List my open issues across projects
gh alias set my-issues 'issue list --assignee @me --state open'

# Quick status: open issues per project
gh alias set status '!echo "=== Foundation ===" && gh project item-list 4 --owner earth2travis --limit 100 2>/dev/null | grep -c "Issue" && echo "=== Framing ===" && gh project item-list 6 --owner earth2travis --limit 100 2>/dev/null | grep -c "Issue" && echo "=== Operations ===" && gh project item-list 7 --owner earth2travis --limit 100 2>/dev/null | grep -c "Issue"'

# Find orphan issues (not in any project)
gh alias set orphans 'issue list --state open --json number,title,projectItems --jq ".[] | select(.projectItems | length == 0) | \"#\\(.number) \\(.title)\""'
```

**Scripting patterns:**

```bash
# Bulk-set Priority on existing issues (JSON + GraphQL)
gh project item-list 6 --owner earth2travis --format json | \
  jq -r '.items[] | .id' | \
  while read id; do
    gh project item-edit --project-id PVT_xxx --id "$id" --field-id PVTSSF_xxx --single-select-option-id OPT_xxx
  done

# Export project to CSV for analysis
gh project item-list 6 --owner earth2travis --format json | \
  jq -r '.items[] | [.title, .status, .labels] | @csv'

# Find issues with no labels
gh issue list --state open --json number,title,labels \
  --jq '.[] | select(.labels | length == 0) | "#\(.number) \(.title)"'
```

**Extensions worth evaluating:**

| Extension             | Purpose                                               |
| --------------------- | ----------------------------------------------------- |
| `gh-dash`             | Terminal dashboard for PRs and issues across repos    |
| `gh-poi`              | Clean up local branches that have been merged         |
| `gh-markdown-preview` | Preview markdown files as they would render on GitHub |

### gh CLI as Agent Infrastructure

The `gh` CLI is our primary interface to GitHub. For an AI agent that manages projects, the CLI is not just a convenience tool. It is infrastructure. Key patterns:

1. **JSON output for parsing:** Always use `--json` flag when processing output programmatically. Never parse human-readable table output.
2. **GraphQL for complex operations:** `gh api graphql` can do anything the GitHub API supports, including bulk project field updates that the CLI does not expose directly.
3. **Scripting with jq:** Combine `gh` JSON output with `jq` for powerful filtering and transformation.
4. **Rate limiting awareness:** GitHub API has rate limits. Batch operations should include delays. The `gh` CLI handles auth automatically but does not throttle.

## Summary: Priority Actions

### Do Now (This Week)

1. Enable built-in automations on Framing and Operations (auto-add, auto-archive, status on close)
2. Add Priority, Size, Area, Cycle fields to Framing and Operations
3. Create recommended views on each project
4. Pin most important active issues in the repo

### Do Soon (This Month)

5. Add gh aliases for common operations
6. Build Prettier and commitlint GitHub Actions
7. Create issue forms for task, research, and decision types
8. Backfill Priority and Area on existing open issues

### Do Later (Next Quarter)

9. Build stale issue bot
10. Build weekly digest automation
11. Evaluate gh-dash extension
12. Build custom scripts for project analytics
