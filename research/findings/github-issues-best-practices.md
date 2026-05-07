---
title: "Best Practices: GitHub Issues"
tags: [github, issues, project-management, best-practices]
related: [github-as-memory, github-project-best-practices, github-capabilities-audit]
source: research/raw/github-issues-best-practices.md
---


# Best Practices: GitHub Issues

## Summary

Guidelines for writing and managing GitHub Issues that serve as durable institutional memory. Covers anatomy, types, acceptance criteria, lifecycle, sizing, sub-issues, templates, and integration with existing systems.

## Key Insights

### Anatomy of a Good Issue

A great issue is one you can pick up cold in two weeks and immediately know what to do and why.

- **Title:** Start with a verb, be specific, include scope
- **Context:** Why this exists, what problem it solves
- **Acceptance Criteria:** Checkable, specific, independent outcomes that define "done"
- **Notes:** Links, references, constraints

### Issue Types (Lightweight)

| Type | Label | When to Use |
|------|-------|-------------|
| Task | `task` | Work that needs doing |
| Research | `research` | Exploration and learning |
| Decision | `decision` | Something that needs deciding |
| Bug | `bug` | Something broken |
| Idea | `idea` | Not yet actionable |

### Sizing

| Size | Effort | Examples |
|------|--------|----------|
| S | < 1 hour | Update a file, fix a typo |
| M | 1-4 hours | Write a guide, create templates |
| L | 4+ hours | Deep research, major refactoring |

### Issue Lifecycle

Created → Triaged → In Progress → Review → Closed

- Close aggressively; reopen if needed
- Always reference the closing commit or PR
- If closing without completing, leave a note explaining why

### Sub-Issues

GitHub now supports sub-issues for L-sized work. Parent tracks overall progress; children are actual work units. Each sub-issue has its own status, labels, and project tracking.

### Templates Recommended

- Task template (context, acceptance criteria, notes)
- Research template (question, scope, expected output)
- Decision template (context, options, constraints)

### Integration with Existing Systems

| System | Connection |
|--------|------------|
| Decision Journal | Decisions reference prompting issues |
| Guides | Guide updates have corresponding issues |
| Research | Research tasks start as issues |
| Memory | Daily memory files reference issue numbers |

## Synthesis

Issues are the atomic unit of memory. The discipline is in the closure: every issue must end with a clear outcome, artifact reference, and cross-link. Without this, the knowledge graph has dangling nodes.

## Related

- [[github-as-knowledge-graph]] — The promoted insight on GitHub as knowledge graph
- [[github-as-memory]] — The flagship document on GitHub as institutional memory
- [[github-project-best-practices]] — Issues, labels, milestones, projects
