---
title: "GitHub and Open Source Best Practices"
tags: [github, open-source, best-practices, branching, commits, ci-cd]
related: [github-as-memory, github-issues-best-practices, agent-native-operations]
source: research/raw/github-practices.md
---

# GitHub and Open Source Best Practices

## Summary

Comprehensive guide for human-AI collaborative development, covering branching strategy, branch naming, commit conventions, PR policies, templates, labels, versioning, protected branches, and CI/CD integration.

## Key Insights

### Branching Strategy: Enhanced GitHub Flow

After evaluating GitFlow, GitHub Flow, and trunk-based development, GitHub Flow is recommended with enhancements for human-AI collaboration.

**Why GitHub Flow wins:**
- Simplicity: one main branch, short-lived feature branches
- Continuous integration: every branch integrates quickly
- AI-friendly: short-lived branches with clear purposes are easier to reason about
- Open source standard

**Rules:**
- `main` is always deployable; never commit directly
- Create feature branches from `main`
- Keep branches short-lived (< 1 week ideally)
- Open PRs early (draft for WIP)
- Delete branches after merging

### Branch Naming

Format: `<type>/<issue-number>-<short-description>`

Types: feature, fix, docs, refactor, test, chore, hotfix

Rules: lowercase, hyphen-separated, include issue number, be descriptive (3-5 words), no personal names.

### Commit Messages: Conventional Commits 1.0.0

Format: `<type>[optional scope]: <description>`

Types and SemVer impact: feat (MINOR), fix (PATCH), docs/style/refactor/test/build/ci/chore (None), perf (PATCH), revert (Varies).

Always reference issues: `Closes #42`, `Fixes #42`, `Refs #42`, `Part of #42`.

### PR Policies

Size guidelines: XS (0-50 lines, excellent review), S (50-200, good, target), M (200-400, acceptable max), L (400-800, poor, split), XL (800+, unacceptable).

Research: PRs under 200 lines merge 40% faster; 50-line PRs receive 40% more comments per line.

Requirements: single purpose, atomic, tests included, docs updated, CI passing.

### Issue and PR Templates

Issue templates (YAML-based forms): Bug Report, Feature Request. PR template: summary, related issue, type of change, changes made, testing done, checklist.

### Labels Strategy

Keep labels minimal and actionable. Recommended categories:
- Type (purple): bug, enhancement, documentation, question, discussion
- Status (yellow): needs-triage, needs-info, in-progress, blocked, ready-for-review
- Contributor-friendly (green): good first issue, help wanted
- Special: breaking-change, security, wontfix, duplicate

Priority and Size tracked as GitHub Project custom fields, not labels.

### Protected Branches and CODEOWNERS

Require: 1 review for main, CI passing, no merge conflicts. Release branches: 2 reviews + code owner approval.

### CI/CD Integration

Recommended Actions: Prettier on PR, commitlint on PR, stale issue bot, auto-label PRs, auto-add issues to projects.

## Synthesis

These practices create a codebase that is readable, maintainable, and welcoming to both human and AI contributors. The commit history becomes a narrative; the PR queue becomes a quality gate. For an AI agent operating in this repo, conventional commits and issue references are not style preferences. They are signal.

## Related

- [[github-as-knowledge-graph]] — The promoted insight on GitHub as knowledge graph
- [[github-as-memory]] — The flagship document on GitHub as institutional memory
- [[github-project-best-practices]] — Issues, labels, milestones, projects
