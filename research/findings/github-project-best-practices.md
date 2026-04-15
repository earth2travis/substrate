---
title: "Best Practices: GitHub Project Management"
tags:
  - lean-manufacturing
related:
  - [[5-whys]]
  - [[a3-thinking]]
  - [[ai-agents-that-run-a-company]]
  - [[composable-primitives]]
source: research/raw/github-project-best-practices.md
---

# Best Practices: GitHub Project Management

## The GitHub Toolkit

GitHub provides four primary project management tools. Each serves a different purpose:

### Issues

The atomic unit of work. An issue is a task, bug, feature, idea, question, or anything else worth tracking. Issues live in a repository and can be labeled, assigned, milestoned, and linked to pull requests.

**Best practices:**

- One issue = one actionable thing. If it can't be completed and closed, it's too vague.
- Use descriptive titles that start with a verb (matches our decision journal convention).
- Include context in the body — why this matters, not just what to do.
- Close issues with references (`Closes #12`) in commit messages or PR descriptions for automatic linking.
- Use sub-issues to break large work into smaller pieces without losing the parent context.

### Labels

Categories you apply to issues for filtering and visual scanning. GitHub provides defaults (bug, enhancement, documentation, etc.) but custom labels are where the real value is.

**Best practices:**

- Keep the label set small. Too many labels means nobody uses them consistently.
- Use a consistent naming convention. At small scale, short unprefixed names work best: `task`, `research`, `infra`.
- Color-code by category for visual scanning.
- Every issue should have at least one label.

### Milestones

Time-boxed or goal-boxed groupings of issues. Think of them as "this batch of work achieves this goal."

**Best practices:**

- Use milestones for meaningful deliverables, not arbitrary time periods.
- Keep milestones small enough to close within a reasonable timeframe (1-4 weeks for a two-person team).
- Every milestone should have a clear "done" definition.
- Use the milestone completion percentage as a health check.

### Projects (GitHub Projects v2)

A flexible layer on top of issues. Projects can display as tables, kanban boards, or roadmap timelines. They pull issues from one or more repositories.

**Best practices:**

- Use Projects for the big picture — what are we working on, what's the status, what's next?
- Custom fields add power: priority, size, status, category.
- Views let you slice the same data differently: "my tasks," "this week," "blocked items."
- Don't over-engineer the project board. Start simple, add complexity only when you feel the need.

---

## Workflow Patterns

### Kanban (Continuous Flow)

Columns: `Backlog → Todo → In Progress → Review → Done`

- Best for ongoing, varied work without fixed sprints.
- Work gets pulled from the backlog as capacity opens up.
- Limit work-in-progress (WIP) to avoid context switching.
- Good for two-person teams with unpredictable workloads.

### Sprint-Based

Fixed time periods (1-2 weeks) with committed scope.

- Best for focused project work with clear deliverables.
- Use milestones as sprints.
- Heavier process overhead — may be too much for two people.

### Hybrid (Recommended for Us)

Kanban flow with milestone-based goals.

- Continuous flow for daily work.
- Milestones for larger initiatives (e.g., "Define SOUL.md," "Establish Protocols").
- No rigid sprints, but regular check-ins on milestone progress.

---

## Integration Patterns

### Issues ↔ Commits

- Reference issues in commit messages: `💠 update SOUL.md (#5)`
- Close issues via commits: `Closes #5` in the commit message auto-closes the issue.

### Issues ↔ Pull Requests

- Link PRs to issues for traceability.
- Use draft PRs for work-in-progress visibility.

### Issues ↔ Decision Journal

- Major decisions that spawn work should reference the decision entry.
- e.g., "Per decision [Adopt File Naming Conventions](../decisions/2026-01.md#adopt-file-naming-conventions), applying kebab-case to all new files."

---

## Anti-Patterns to Avoid

| Anti-Pattern                  | Why It's Bad                                          | What to Do Instead                                                 |
| ----------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------ |
| Issues without context        | "Fix the thing" tells you nothing in two weeks        | Always include why, not just what                                  |
| Too many labels               | Nobody remembers what `priority-2b-maybe-later` means | Keep it under 15 labels total                                      |
| Stale issues                  | A backlog of 200 open issues is demoralizing          | Regularly triage; close what you won't do                          |
| Issue as conversation         | Long threads bury the actual task                     | Summarize decisions in the issue body; use comments for discussion |
| No closure discipline         | Issues stay open forever                              | Close aggressively; reopen if needed                               |
| Over-engineered project board | 12 columns, 8 custom fields, 4 views                  | Start with 4-5 columns max; add complexity only when earned        |
