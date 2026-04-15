---
title: "Best Practices: GitHub Issues"
tags:
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/github-issues-best-practices.md
---

# Best Practices: GitHub Issues

## What Makes a Great Issue

A great issue is one you can pick up cold in two weeks and immediately know what to do and why.

### Anatomy of a Good Issue

```markdown
## Title: [Verb] [Clear Description]

e.g., "Define SOUL.md with Le Guin × Gibson Identity"

### Context

Why this issue exists. What problem it solves or what value it creates.
Link to relevant decisions, conversations, or research.

### Acceptance Criteria

- [ ] Specific, checkable outcomes
- [ ] That define "done"
- [ ] Without ambiguity

### Notes

Any relevant context, links, references, or constraints.
```

### Title Conventions

- **Start with a verb** — matches our decision journal heading convention.
- **Be specific** — "Update docs" is bad. "Update decision journal guide with sizing criteria" is good.
- **Include scope** — If it's about a specific area, name it.

Good: `Create issue templates for the sivart repo`
Bad: `Templates`

Good: `Research GitHub Projects best practices`
Bad: `Look into project management`

---

## Issue Types

For a two-person team, keep types simple:

| Type         | When to Use                                      | Label      |
| ------------ | ------------------------------------------------ | ---------- |
| **Task**     | Work that needs doing                            | `task`     |
| **Research** | Exploration and learning                         | `research` |
| **Decision** | Something that needs to be decided               | `decision` |
| **Bug**      | Something broken that needs fixing               | `bug`      |
| **Idea**     | Something worth capturing but not yet actionable | `idea`     |

---

## Writing Good Acceptance Criteria

Acceptance criteria define "done." They should be:

- **Checkable** — You can look at each one and say yes/no.
- **Specific** — Not "make it better" but "response time under 200ms."
- **Independent** — Each criterion stands on its own.

Examples:

**Bad:**

- [ ] Fix the guide
- [ ] Make it look good

**Good:**

- [ ] Guide includes step-by-step setup instructions
- [ ] All code blocks are tested and working
- [ ] Guide is linked from the decisions README
- [ ] Committed and pushed to sivart repo

---

## Issue Lifecycle

```
Created → Triaged → In Progress → Review → Closed
```

1. **Created** — Issue exists with context and acceptance criteria.
2. **Triaged** — Labeled, sized, prioritized, and optionally assigned.
3. **In Progress** — Someone is actively working on it.
4. **Review** — Work is done, needs a second look (when applicable).
5. **Closed** — Acceptance criteria met, or intentionally abandoned (with a note why).

### Closing Discipline

- Close issues when done. Don't let them linger.
- If you close without completing, leave a comment explaining why.
- Reference the closing commit or PR: "Closed by commit abc123" or "Closes #12."

---

## Sizing Issues

Align with our decision sizing for consistency:

| Size  | Effort    | Examples                                                |
| ----- | --------- | ------------------------------------------------------- |
| **S** | < 1 hour  | Update a file, fix a typo, add a label                  |
| **M** | 1-4 hours | Write a guide, create issue templates, research a topic |
| **L** | 4+ hours  | Deep research, major refactoring, new system setup      |

Add size as a label: `size:S`, `size:M`, `size:L`

---

## Sub-Issues

GitHub now supports sub-issues — breaking a parent issue into child tasks. Use these for L-sized work:

```markdown
Parent: Set Up GitHub Project Management
├── Sub: Create label taxonomy
├── Sub: Set up project board
├── Sub: Create issue templates
└── Sub: Write project management guide
```

The parent issue tracks overall progress; sub-issues are the actual work units.

---

## Templates

Issue templates ensure consistency. For our repo, we should have:

### Task Template

```markdown
---
name: Task
about: A piece of work that needs doing
labels: task
---

## Context

<!-- Why does this task exist? What problem does it solve? -->

## Acceptance Criteria

- [ ]

## Notes

<!-- Links, references, constraints -->
```

### Research Template

```markdown
---
name: Research
about: Exploration and learning
labels: research
---

## Question

<!-- What are we trying to understand? -->

## Scope

<!-- How deep should we go? What's out of bounds? -->

## Expected Output

- [ ]

## Notes

<!-- Starting points, references -->
```

### Decision Template

```markdown
---
name: Decision
about: Something that needs to be decided
labels: decision
---

## Context

<!-- Why does this decision need to be made? -->

## Options

<!-- What are the alternatives? -->

## Constraints

<!-- Deadlines, dependencies, limitations -->

## Notes

<!-- Relevant research, prior decisions -->
```

---

## Linking Issues to Our Existing Systems

| System               | How Issues Connect                                                                                        |
| -------------------- | --------------------------------------------------------------------------------------------------------- |
| **Decision Journal** | Major decisions reference the issue that prompted them. Issues reference the decision that resolved them. |
| **Guides**           | When a guide needs creating or updating, there's an issue for it.                                         |
| **Research**         | Research tasks start as issues, output goes into `research/` directory.                                   |
| **Memory**           | Daily memory files can reference issue numbers for context.                                               |
