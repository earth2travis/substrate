---
title: "Best Practices: GitHub Project Management"
tags: [github, project-management, best-practices, kanban, milestones]
related: [github-as-memory, github-issues-best-practices, github-capabilities-audit, kanban-doctrine]
source: research/raw/github-project-best-practices.md
---

# Best Practices: GitHub Project Management

## Summary

Guide to using GitHub's built-in project management tools (Issues, Labels, Milestones, Projects v2) for a two-person team, with workflow patterns and anti-patterns.

## Key Insights

### The Four Tools

**Issues:** Atomic unit of work. Best practices: one issue = one actionable thing, descriptive verb-led titles, include context in body, close with references, use sub-issues for large work.

**Labels:** Categories for filtering. Best practices: keep the set small, consistent naming, color-code by category, every issue gets at least one label.

**Milestones:** Time-boxed or goal-boxed groupings. Best practices: use for meaningful deliverables, keep small (1-4 weeks), every milestone has a clear "done" definition.

**Projects v2:** Flexible layer on top of issues. Best practices: use for the big picture, custom fields add power, views slice data differently, don't over-engineer.

### Workflow Patterns

**Kanban (Continuous Flow):** Backlog → Todo → In Progress → Review → Done. Best for ongoing varied work. Limit WIP. Good for unpredictable workloads.

**Sprint-Based:** Fixed time periods (1-2 weeks) with committed scope. Best for focused project work. Higher overhead.

**Hybrid (Recommended):** Kanban flow with milestone-based goals. Continuous flow for daily work; milestones for larger initiatives. No rigid sprints but regular check-ins.

### Integration Patterns

- Issues ↔ Commits: reference issues in commit messages; close via `Closes #N`
- Issues ↔ PRs: link for traceability; use draft PRs for WIP
- Issues ↔ Decision Journal: major decisions reference the decision entry

### Anti-Patterns

| Anti-Pattern | Why Bad | Instead |
|--------------|---------|---------|
| Issues without context | "Fix the thing" tells nothing in two weeks | Always include why |
| Too many labels | Nobody remembers `priority-2b-maybe-later` | Keep under 15 total |
| Stale issues | 200 open issues is demoralizing | Regular triage; close what you won't do |
| Issue as conversation | Long threads bury the task | Summarize in body; comments for discussion |
| No closure discipline | Issues stay open forever | Close aggressively; reopen if needed |
| Over-engineered board | 12 columns, 8 fields, 4 views | Start with 4-5 columns max |

## Synthesis

For a two-person team, the key is keeping it lightweight enough to maintain but structured enough to be useful. The hybrid Kanban + milestone approach provides flow without the overhead of rigid sprints. The discipline is in the closure, not the tooling.
