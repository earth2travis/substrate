---
title: GitHub and Open Source Best Practices
tags:
  - ai-agents
  - knowledge-management
  - software-engineering
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/github-practices.md
---

# GitHub and Open Source Best Practices

A comprehensive guide for human-AI collaborative development. This document establishes standards we believe are right for transparent, maintainable, and welcoming open source projects.

**Related Issue:** #86

---

## Table of Contents

1. [Branching Strategy](#1-branching-strategy)
2. [Branch Naming Conventions](#2-branch-naming-conventions)
3. [Commit Message Conventions](#3-commit-message-conventions)
4. [Pull Request Policies](#4-pull-request-policies)
5. [Issue and PR Templates](#5-issue-and-pr-templates)
6. [Labels Strategy](#6-labels-strategy)
7. [Release Versioning](#7-release-versioning-semver)
8. [Protected Branches and CODEOWNERS](#8-protected-branches-and-codeowners)
9. [CONTRIBUTING.md Best Practices](#9-contributingmd-best-practices)
10. [Changelog Management](#10-changelog-management)
11. [Code Review Best Practices](#11-code-review-best-practices)
12. [CI/CD Integration Patterns](#12-cicd-integration-patterns)
13. [Open Source Governance Models](#13-open-source-governance-models)

---

## 1. Branching Strategy

### Recommendation: GitHub Flow (with Enhancements)

After evaluating GitFlow, GitHub Flow, and trunk-based development, we recommend **GitHub Flow** as our primary branching strategy, with specific enhancements for human-AI collaboration.

#### Why GitHub Flow?

| Strategy        | Complexity | Best For                           | Trade-offs                                     |
| --------------- | ---------- | ---------------------------------- | ---------------------------------------------- |
| **GitFlow**     | High       | Large teams, scheduled releases    | Overhead, long-lived branches, merge conflicts |
| **GitHub Flow** | Low        | Continuous delivery, smaller teams | Requires strong CI/CD, discipline              |
| **Trunk-Based** | Lowest     | High-maturity teams, feature flags | Requires advanced testing infrastructure       |

**GitHub Flow wins because:**

1. **Simplicity**: One main branch, short-lived feature branches. Cognitive overhead stays low.
2. **Continuous Integration**: Every branch integrates quickly with `main`, reducing merge hell.
3. **AI-Friendly**: Short-lived branches with clear purposes are easier to reason about and document.
4. **Open Source Standard**: Most successful open source projects use this model.

#### Our Enhanced GitHub Flow

```
main (always deployable)
 │
 ├── feature/issue-42-add-memory-search
 │
 ├── fix/issue-87-telegram-timeout
 │
 └── docs/update-contributing-guide
```

**Rules:**

1. `main` is always deployable. Never commit directly.
2. Create feature branches from `main` for all work.
3. Keep branches short-lived (ideally < 1 week, merge within 1-2 days when possible).
4. Open PRs early (draft PRs for work-in-progress).
5. Delete branches after merging.

#### When to Consider GitFlow

Use GitFlow only if you need:

- Scheduled release cycles (e.g., quarterly releases)
- Multiple supported versions in production simultaneously
- Strict separation between development and production code

#### Sources

- [Mergify: Trunk-Based Development vs GitFlow](https://mergify.com/blog/trunk-based-development-vs-gitflow-which-branching-model-actually-works)
- [LaunchDarkly: Git Branching Strategies](https://launchdarkly.com/blog/git-branching-strategies-vs-trunk-based-development/)
- [Toptal: Trunk-based Development vs Git Flow](https://www.toptal.com/software/trunk-based-development-git-flow)

---

## 2. Branch Naming Conventions

### Format

```
<type>/<issue-number>-<short-description>
```

### Types

| Prefix      | Purpose                                 | Example                          |
| ----------- | --------------------------------------- | -------------------------------- |
| `feature/`  | New functionality                       | `feature/42-add-calendar-sync`   |
| `fix/`      | Bug fixes                               | `fix/87-handle-timeout-error`    |
| `docs/`     | Documentation only                      | `docs/update-setup-guide`        |
| `refactor/` | Code restructuring (no behavior change) | `refactor/extract-email-service` |
| `test/`     | Adding or fixing tests                  | `test/add-memory-unit-tests`     |
| `chore/`    | Maintenance tasks                       | `chore/update-dependencies`      |
| `hotfix/`   | Urgent production fixes                 | `hotfix/critical-auth-bug`       |

### Rules

1. **Lowercase and hyphen-separated**: `feature/new-login` not `Feature/NewLogin`
2. **Include issue number when applicable**: Links work to context
3. **Be descriptive but concise**: 3-5 words max in description
4. **No special characters**: Stick to alphanumeric and hyphens
5. **No personal names**: `feature/42-auth-flow` not `feature/johns-auth-work`

### AI Collaboration Note

When AI agents create branches, they should always reference the issue number. This creates an audit trail and makes it easy to trace decisions back to discussions.

### Sources

- [Medium: Naming Conventions for Git Branches](https://medium.com/@abhay.pixolo/naming-conventions-for-git-branches-a-cheatsheet-8549feca2534)
- [Graphite: Git Branch Naming Conventions](https://graphite.com/guides/git-branch-naming-conventions)
- [Dev.to: GitHub Branching Name Best Practices](https://dev.to/jps27cse/github-branching-name-best-practices-49ei)

---

## 3. Commit Message Conventions

### Standard: Conventional Commits 1.0.0

We adopt [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) because it:

- Enables automatic changelog generation
- Integrates with semantic versioning
- Makes commit history readable and searchable
- Provides clear intent to reviewers

### Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

| Type       | When to Use                   | SemVer Impact |
| ---------- | ----------------------------- | ------------- |
| `feat`     | New feature                   | MINOR         |
| `fix`      | Bug fix                       | PATCH         |
| `docs`     | Documentation only            | None          |
| `style`    | Formatting, no code change    | None          |
| `refactor` | Code change, no feature/fix   | None          |
| `perf`     | Performance improvement       | PATCH         |
| `test`     | Adding/correcting tests       | None          |
| `build`    | Build system or dependencies  | None          |
| `ci`       | CI configuration              | None          |
| `chore`    | Other changes (tooling, etc.) | None          |
| `revert`   | Reverting a previous commit   | Varies        |

### Examples

**Simple commit:**

```
feat: add email notification for calendar events
```

**Commit with scope:**

```
fix(auth): handle expired token refresh correctly
```

**Commit with body:**

```
feat(memory): add semantic search capability

Implement vector-based similarity search for long-term memory
retrieval. Uses cosine similarity with a threshold of 0.7.

Closes #42
```

**Breaking change:**

```
feat(api)!: change response format for /status endpoint

BREAKING CHANGE: The status endpoint now returns a nested object
structure instead of flat key-value pairs.
```

### Issue References

Always reference issues in commits:

- `Closes #42` - Closes the issue when merged
- `Fixes #42` - Same as Closes
- `Refs #42` - References without closing
- `Part of #42` - Partial work toward an issue

### Sources

- [Conventional Commits Specification](https://www.conventionalcommits.org/en/v1.0.0/)
- [Angular Contributing Guidelines](https://github.com/angular/angular/blob/main/CONTRIBUTING.md)

---

## 4. Pull Request Policies

### Size Guidelines

Research consistently shows that smaller PRs lead to better outcomes:

| PR Size | Lines Changed | Review Quality | Recommendation       |
| ------- | ------------- | -------------- | -------------------- |
| XS      | 0-50          | Excellent      | Ideal                |
| S       | 50-200        | Good           | Target this          |
| M       | 200-400       | Acceptable     | Maximum for features |
| L       | 400-800       | Poor           | Split if possible    |
| XL      | 800+          | Unacceptable   | Must split           |

**Key findings:**

- PRs under 200 lines get merged 40% faster than 400+ line PRs
- 50-line PRs receive 40% more comments per line (better review quality)
- Defect density increases with PR size

### PR Requirements

1. **Single Purpose**: Each PR should do one thing
2. **Atomic**: Can be merged independently
3. **Tests Included**: No new code without tests
4. **Documentation Updated**: If behavior changes, docs change
5. **CI Passing**: All checks green before review

### Review Requirements

| Branch      | Minimum Reviewers | Additional Requirements        |
| ----------- | ----------------- | ------------------------------ |
| `main`      | 1                 | CI passing, no merge conflicts |
| `release/*` | 2                 | Code owner approval            |

### PR Description Template

See [Section 5](#5-issue-and-pr-templates) for our template.

### Handling Large Changes

When changes genuinely require more than 400 lines:

1. **Stack PRs**: Create dependent PRs that build on each other
2. **Feature Flags**: Merge incomplete features behind flags
3. **Communicate Early**: Notify reviewers that a large PR is coming
4. **Detailed Description**: Provide extra context and navigation hints

### Sources

- [Microsoft Engineering Playbook: Pull Requests](https://microsoft.github.io/code-with-engineering-playbook/code-reviews/pull-requests/)
- [Graphite: Best Practices for Managing PR Size](https://graphite.com/guides/best-practices-managing-pr-size)
- [Google Engineering Practices: Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html)

---

## 5. Issue and PR Templates

### Issue Templates

Create `.github/ISSUE_TEMPLATE/` directory with multiple templates:

#### Bug Report (`bug_report.yml`)

```yaml
name: Bug Report
description: Report something that isn't working correctly
title: "[Bug]: "
labels: ["bug", "needs-triage"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to report a bug!

  - type: textarea
    id: description
    attributes:
      label: Describe the bug
      description: A clear description of what the bug is
      placeholder: What happened?
    validations:
      required: true

  - type: textarea
    id: steps
    attributes:
      label: Steps to reproduce
      description: How can we reproduce this?
      placeholder: |
        1. Go to '...'
        2. Click on '...'
        3. See error
    validations:
      required: true

  - type: textarea
    id: expected
    attributes:
      label: Expected behavior
      description: What should have happened?
    validations:
      required: true

  - type: textarea
    id: environment
    attributes:
      label: Environment
      description: Version, OS, browser, etc.
      placeholder: |
        - Version: 1.2.3
        - OS: Ubuntu 24.04
        - Node: 20.x
```

#### Feature Request (`feature_request.yml`)

```yaml
name: Feature Request
description: Suggest a new feature or enhancement
title: "[Feature]: "
labels: ["enhancement", "needs-triage"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Problem statement
      description: What problem does this solve?
      placeholder: I'm frustrated when...
    validations:
      required: true

  - type: textarea
    id: solution
    attributes:
      label: Proposed solution
      description: How would you like this to work?
    validations:
      required: true

  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives considered
      description: What other approaches have you thought about?

  - type: textarea
    id: context
    attributes:
      label: Additional context
      description: Screenshots, links, examples
```

### Pull Request Template

Create `.github/PULL_REQUEST_TEMPLATE.md`:

```markdown
## Summary

<!-- Brief description of changes. What does this PR do? -->

## Related Issue

<!-- Link to the issue this addresses -->

Closes #

## Type of Change

<!-- Check all that apply -->

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update
- [ ] Refactoring (no functional changes)
- [ ] Performance improvement
- [ ] Test coverage

## Changes Made

<!-- Bullet list of specific changes -->

-

## Testing Done

<!-- How did you verify this works? -->

- [ ] Added/updated unit tests
- [ ] Manual testing performed
- [ ] Tested edge cases

## Checklist

- [ ] My code follows the project style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented hard-to-understand areas
- [ ] I have updated documentation as needed
- [ ] My changes generate no new warnings
- [ ] All tests pass locally
- [ ] Any dependent changes have been merged

## Screenshots (if applicable)

<!-- Add screenshots for UI changes -->
```

### Sources

- [GitHub Docs: Issue Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)
- [Everhour: GitHub PR Template Examples](https://everhour.com/blog/github-pr-template/)

---

## 6. Labels Strategy

### Philosophy

Labels should be:

- **Categorical**: Grouped by purpose
- **Color-coded**: Visual scanning at a glance
- **Minimal**: Not every issue needs every label type
- **Actionable**: Help triage and prioritize

### Recommended Labels

#### Type (Purple: #6f42c1)

| Label           | Description                 |
| --------------- | --------------------------- |
| `bug`           | Something isn't working     |
| `enhancement`   | New feature or improvement  |
| `documentation` | Documentation only changes  |
| `question`      | Request for information     |
| `discussion`    | Open-ended discussion topic |

#### Status (Yellow: #fbca04)

| Label              | Description                      |
| ------------------ | -------------------------------- |
| `needs-triage`     | Needs initial assessment         |
| `needs-info`       | Waiting for more information     |
| `in-progress`      | Actively being worked on         |
| `blocked`          | Cannot proceed due to dependency |
| `ready-for-review` | PR ready for code review         |

#### Priority and Size (Use Project Fields, Not Labels)

**Updated 2026-02-09:** Priority and Size are now tracked as GitHub Project custom fields, not labels. This provides cleaner separation:

- **Labels:** Categorization (what kind of work)
- **Project fields:** Metadata (priority, size, status)

**Priority field options:** Critical, High, Medium, Low
**Size field options:** XS, S, M, L, XL

This allows sorting, filtering, and grouping in project views without cluttering the label namespace.

#### Contributor-Friendly (Green: #0e8a16)

| Label              | Description                     |
| ------------------ | ------------------------------- |
| `good first issue` | Good for newcomers              |
| `help wanted`      | Open for community contribution |

#### Special

| Label             | Color   | Description                     |
| ----------------- | ------- | ------------------------------- |
| `breaking-change` | #d73a4a | Will require major version bump |
| `security`        | #ee0701 | Security-related issue          |
| `wontfix`         | #ffffff | Will not be addressed           |
| `duplicate`       | #cfd3d7 | Duplicate of another issue      |

### Sources

- [GitHub Docs: Managing Labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels)
- [Dosu: Open Source Labeling Best Practices](https://dosu.dev/blog/open-source-labeling-best-practices)
- [Robin: Best Practice System for GitHub Issues](https://robinpowered.com/blog/best-practice-system-for-organizing-and-tagging-github-issues)

---

## 7. Release Versioning (SemVer)

### Standard: Semantic Versioning 2.0.0

We follow [Semantic Versioning](https://semver.org/) strictly.

### Format

```
MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]
```

### Version Increment Rules

| Situation                       | Increment  | Example       |
| ------------------------------- | ---------- | ------------- |
| Breaking API change             | MAJOR      | 1.2.3 → 2.0.0 |
| New backward-compatible feature | MINOR      | 1.2.3 → 1.3.0 |
| Backward-compatible bug fix     | PATCH      | 1.2.3 → 1.2.4 |
| Pre-release version             | Add suffix | 2.0.0-alpha.1 |

### Pre-release Labels

Use in order of stability:

1. `alpha` - Internal testing, unstable
2. `beta` - External testing, approaching stable
3. `rc` - Release candidate, stable unless issues found

Example progression:

```
1.0.0-alpha.1 → 1.0.0-alpha.2 → 1.0.0-beta.1 → 1.0.0-rc.1 → 1.0.0
```

### Version 0.x.x

During initial development (0.x.x):

- Public API is not stable
- Any change may be breaking
- Start at 0.1.0
- Increment MINOR for breaking changes and features
- Increment PATCH for bug fixes

### Version 1.0.0

Declare 1.0.0 when:

- The software is used in production
- The public API is stable
- You have a deprecation policy

### Mapping Conventional Commits to SemVer

| Commit Type | Contains BREAKING CHANGE? | Version Bump               |
| ----------- | ------------------------- | -------------------------- |
| `feat`      | No                        | MINOR                      |
| `feat`      | Yes                       | MAJOR                      |
| `fix`       | No                        | PATCH                      |
| `fix`       | Yes                       | MAJOR                      |
| All others  | No                        | PATCH (if any fix) or None |
| All others  | Yes                       | MAJOR                      |

### Sources

- [Semantic Versioning 2.0.0](https://semver.org/)
- [npm: About Semantic Versioning](https://docs.npmjs.com/about-semantic-versioning/)

---

## 8. Protected Branches and CODEOWNERS

### Protected Branch Settings for `main`

Enable these protections in repository settings:

| Setting                                   | Recommended | Rationale                 |
| ----------------------------------------- | ----------- | ------------------------- |
| Require pull request before merging       | ✅ Yes      | No direct commits         |
| Required approving reviews                | 1 minimum   | Ensures review            |
| Dismiss stale PR approvals on new commits | ✅ Yes      | Re-review on changes      |
| Require review from Code Owners           | ✅ Yes      | Domain experts approve    |
| Require status checks to pass             | ✅ Yes      | CI must pass              |
| Require branches to be up to date         | ✅ Yes      | Avoid merge conflicts     |
| Require conversation resolution           | ✅ Yes      | Address all feedback      |
| Require signed commits                    | Optional    | Depends on security needs |
| Include administrators                    | ✅ Yes      | Everyone follows rules    |
| Allow force pushes                        | ❌ No       | Preserve history          |
| Allow deletions                           | ❌ No       | Prevent accidents         |

### CODEOWNERS

Create `.github/CODEOWNERS`:

```
# Global owners (fallback for everything)
* @username

# Documentation
/docs/ @docs-team
*.md @docs-team

# Core application
/src/ @core-team

# Configuration and infrastructure
/.github/ @admin-team
/infra/ @admin-team

# Specific critical files
/CODEOWNERS @admin-team
/SECURITY.md @security-team
```

### CODEOWNERS Best Practices

1. **Location**: Put in `.github/` directory (most secure)
2. **Protect the CODEOWNERS file itself**: Add `/.github/CODEOWNERS @owner`
3. **Use teams over individuals**: Teams survive personnel changes
4. **Order matters**: Last match wins
5. **Keep it simple**: Don't over-specify

### Sources

- [GitHub Docs: About Code Owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [GitHub Docs: Managing Protected Branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)

---

## 9. CONTRIBUTING.md Best Practices

### Essential Sections

Every CONTRIBUTING.md should include:

````markdown
# Contributing to [Project Name]

First off, thank you for considering contributing!

## Code of Conduct

This project and everyone participating is governed by our
[Code of Conduct](CODE_OF_CONDUCT.md). By participating,
you agree to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues.
When you create a bug report, include as many details as possible
using our [bug report template](.github/ISSUE_TEMPLATE/bug_report.yml).

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub Issues.
Use our [feature request template](.github/ISSUE_TEMPLATE/feature_request.yml).

### Your First Code Contribution

Unsure where to begin? Look for issues labeled:

- `good first issue` - Simple issues for newcomers
- `help wanted` - Issues open to anyone

### Pull Requests

1. Fork the repo and create your branch from `main`
2. Follow our [coding standards](#coding-standards)
3. Write or update tests as needed
4. Ensure the test suite passes
5. Update documentation as needed
6. Submit the PR using our template

## Development Setup

### Prerequisites

- Node.js >= 20.x
- npm >= 10.x

### Installation

```bash
git clone https://github.com/org/repo.git
cd repo
npm install
```
````

### Running Tests

```bash
npm test
```

## Coding Standards

### Commit Messages

We use [Conventional Commits](https://conventionalcommits.org):

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation
- `refactor:` for refactoring

### Code Style

- Run `npm run lint` before committing
- Follow existing patterns in the codebase

## Community

- Questions? Open a [Discussion](link-to-discussions)
- Chat? Join our [Discord/Slack](link)

## Recognition

Contributors are recognized in our [CONTRIBUTORS.md](CONTRIBUTORS.md).

````

### Tips

1. **Be welcoming**: First paragraph should make people feel invited
2. **Be specific**: Include exact commands for setup
3. **Link to templates**: Don't make people search
4. **Define expectations**: Response times, review process
5. **Keep it updated**: Review quarterly

### Sources

- [Contributing.md: How to Build CONTRIBUTING.md](https://contributing.md/how-to-build-contributing-md/)
- [Mozilla Science: Wrangling Web Contributions](https://mozillascience.github.io/working-open-workshop/contributing/)

---

## 10. Changelog Management

### Standard: Keep a Changelog

We follow [Keep a Changelog](https://keepachangelog.com/) format.

### Format

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New feature description

### Changed
- Modification to existing feature

### Deprecated
- Feature that will be removed in future

### Removed
- Feature that was removed

### Fixed
- Bug fix description

### Security
- Security patch description

## [1.1.0] - 2026-02-04

### Added
- Calendar integration with Google Calendar
- Email notifications for upcoming events

### Fixed
- Memory search returning stale results

## [1.0.0] - 2026-01-15

### Added
- Initial release
- Core functionality

[Unreleased]: https://github.com/org/repo/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/org/repo/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/org/repo/releases/tag/v1.0.0
````

### Guiding Principles

1. **Changelogs are for humans**, not machines
2. **Every version gets an entry**
3. **Group changes by type** (Added, Changed, etc.)
4. **Versions and sections are linkable**
5. **Latest version comes first**
6. **Release date in ISO format** (YYYY-MM-DD)
7. **Mention that you follow SemVer**

### Categories

Use these categories in this order:

| Category   | Purpose                      |
| ---------- | ---------------------------- |
| Added      | New features                 |
| Changed    | Changes to existing features |
| Deprecated | Soon-to-be-removed features  |
| Removed    | Removed features             |
| Fixed      | Bug fixes                    |
| Security   | Vulnerability patches        |

### Automation

Tools that can generate changelogs from Conventional Commits:

- [standard-version](https://github.com/conventional-changelog/standard-version)
- [semantic-release](https://github.com/semantic-release/semantic-release)
- [release-please](https://github.com/googleapis/release-please)

### Unreleased Section

Always maintain an `[Unreleased]` section at the top:

- Tracks what's coming
- At release time, rename to version number
- Add a new empty Unreleased section

### Sources

- [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
- [Common Changelog](https://github.com/vweevers/common-changelog)

---

## 11. Code Review Best Practices

### The Standard (from Google)

> Reviewers should favor approving a PR once it is in a state where it definitely improves the overall code health of the system being worked on, even if the PR isn't perfect.

There is no "perfect" code—only better code.

### What Reviewers Should Look For

1. **Design**: Is the code well-designed and appropriate for the system?
2. **Functionality**: Does the code behave as intended? Is it good for users?
3. **Complexity**: Could the code be simpler? Will others understand it?
4. **Tests**: Are tests correct, sensible, and useful?
5. **Naming**: Are names clear and descriptive?
6. **Comments**: Are comments necessary and clear?
7. **Style**: Does the code follow style guidelines?
8. **Documentation**: Is documentation updated?

### Principles

1. **Technical facts and data overrule opinions**
2. **Style guide is authority on style questions**
3. **Software design is not just preference—use principles**
4. **If no rule applies, prefer consistency with existing code**

### Review Speed

- **Respond within one business day** at minimum
- **Same-day response is ideal**
- Slow reviews kill velocity and morale

### How to Write Comments

**Good:**

```
Nit: Consider using a more descriptive variable name here,
like `userEmailList` instead of `list`.
```

**Better:**

```
Could we add a comment explaining why we're filtering for
active users only? It would help future readers understand
the business logic.
```

**Best:**

```
This approach works, but I wonder if using a Map here might
give us O(1) lookups instead of O(n). Happy to discuss if
there's a reason for the current approach.
```

### Comment Prefixes

| Prefix        | Meaning                                        |
| ------------- | ---------------------------------------------- |
| `Nit:`        | Minor suggestion, optional to address          |
| `Optional:`   | Take it or leave it                            |
| `Question:`   | Not suggesting a change, seeking understanding |
| `Suggestion:` | Recommendation, author decides                 |
| (no prefix)   | Expected to be addressed before approval       |

### AI-Specific Considerations

When an AI agent submits a PR:

- **Check reasoning**: Does the approach make sense?
- **Verify tests**: AI-generated tests may miss edge cases
- **Watch for hallucinations**: Confirm referenced docs/APIs exist
- **Review assumptions**: AI may have made incorrect assumptions

### Resolving Conflicts

1. Try to reach consensus based on principles
2. Face-to-face/video call if text isn't working
3. Escalate to tech lead if needed
4. Never let a PR sit due to unresolved disagreement

### Sources

- [Google Engineering Practices: Code Review](https://google.github.io/eng-practices/review/)
- [Google: The Standard of Code Review](https://google.github.io/eng-practices/review/reviewer/standard.html)
- [Abseil: Software Engineering at Google, Chapter 9](https://abseil.io/resources/swe-book/html/ch09.html)

---

## 12. CI/CD Integration Patterns

### Required Checks for PRs

Every PR should pass these checks before merge:

| Check         | Purpose                 | Blocking? |
| ------------- | ----------------------- | --------- |
| Build         | Code compiles           | Yes       |
| Lint          | Code style              | Yes       |
| Tests         | Functionality           | Yes       |
| Type check    | Type safety             | Yes       |
| Coverage      | Test coverage threshold | Optional  |
| Security scan | Vulnerability detection | Yes       |

### Example GitHub Actions Workflow

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Lint
        run: npm run lint

      - name: Type check
        run: npm run typecheck

      - name: Test
        run: npm test -- --coverage

      - name: Build
        run: npm run build

  security:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Run security audit
        run: npm audit --audit-level=high
```

### Branch-Specific Workflows

| Branch      | Workflow | Actions                           |
| ----------- | -------- | --------------------------------- |
| `main`      | CI + CD  | Test, build, deploy to production |
| `feature/*` | CI only  | Test, build, no deploy            |
| `release/*` | CI + CD  | Test, build, deploy to staging    |

### Recommended Automation

1. **Automated labeling**: Label PRs by files changed
2. **PR size warnings**: Flag large PRs automatically
3. **Stale bot**: Close inactive PRs/issues after 30 days
4. **Dependabot**: Automated dependency updates
5. **Code scanning**: CodeQL for security analysis

### Deployment Strategy

```yaml
# Only deploy on main branch pushes
deploy:
  needs: [build, security]
  if: github.ref == 'refs/heads/main' && github.event_name == 'push'
  runs-on: ubuntu-latest
  steps:
    - name: Deploy to production
      run: ./deploy.sh
```

### Sources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Graphite: Enhancing Code Quality on GitHub](https://graphite.com/guides/enhancing-code-quality-github)
- [UK Government: Automating Code Quality Assurance](https://best-practice-and-impact.github.io/qa-of-code-guidance/continuous_integration.html)

---

## 13. Open Source Governance Models

### Three Common Models

#### 1. BDFL (Benevolent Dictator for Life)

**Structure**: One person (usually the original author) has final say on all major decisions.

**Examples**: Python (historically), Linux kernel (effectively)

**Pros:**

- Clear decision-making authority
- Consistent vision
- Works well for small projects

**Cons:**

- Bus factor of 1
- Can become bottleneck
- May discourage contribution

**Best for**: Personal projects, early-stage projects, projects with strong singular vision

#### 2. Meritocracy

**Structure**: Active contributors earn decision-making power through demonstrated "merit" (contributions). Decisions made by voting.

**Examples**: Apache projects, many open source foundations

**Pros:**

- Rewards contribution
- Democratic
- Scalable

**Cons:**

- "Merit" can be biased toward certain types of work
- Voting can be slow
- Complex governance overhead

**Best for**: Foundation-backed projects, large ecosystems

#### 3. Liberal Contribution Model

**Structure**: Those doing the most current work have the most influence. Decisions by consensus-seeking, not voting.

**Examples**: Node.js, Rust

**Pros:**

- Focuses on current contributors, not historical
- Consensus over voting (more collaborative)
- Lower barrier to influence

**Cons:**

- Requires active participation
- "Current work" can be subjective
- May favor full-time contributors

**Best for**: Community-driven projects, projects with corporate backing

### Our Recommendation: Hybrid Model

For human-AI collaborative projects, we recommend a **Hybrid BDFL + Liberal Contribution** model:

1. **Human owner** has final say on values, direction, and major decisions
2. **AI agents** can propose, implement, and review but don't vote
3. **Contributors** earn trust through quality contributions
4. **Decisions by consensus** when possible, BDFL tiebreaker when needed

### Documenting Governance

Create a `GOVERNANCE.md` file that covers:

```markdown
# Governance

## Decision Making

This project uses [model name] governance.

### Major Decisions

Major decisions (breaking changes, new features, architectural changes)
are made by [process].

### Day-to-Day Decisions

Day-to-day decisions are made by maintainers during code review.

## Roles

### Maintainers

Maintainers can:

- Merge pull requests
- Manage issues
- Release versions

Current maintainers: [list]

### Contributors

Anyone can contribute. Contributors who demonstrate sustained,
quality contributions may be invited to become maintainers.

### Becoming a Maintainer

[Process for becoming a maintainer]

## Code of Conduct

All participants must follow our [Code of Conduct](CODE_OF_CONDUCT.md).
```

### Sources

- [Open Source Guides: Leadership and Governance](https://opensource.guide/leadership-and-governance/)
- [Red Hat: Understanding Open Source Governance Models](https://www.redhat.com/en/blog/understanding-open-source-governance-models)
- [Stack Overflow Blog: Open Source Governance](https://stackoverflow.blog/2020/09/09/open-source-governance-benevolent-dictator-or-decision-by-committee/)

---

## Summary: Our Standards

| Area             | Our Choice                         |
| ---------------- | ---------------------------------- |
| Branching        | GitHub Flow                        |
| Branch naming    | `<type>/<issue>-<description>`     |
| Commits          | Conventional Commits               |
| PR size          | Target < 200 lines, max 400        |
| Reviews required | 1 minimum                          |
| Versioning       | SemVer 2.0.0                       |
| Changelog        | Keep a Changelog format            |
| Governance       | Hybrid BDFL + Liberal Contribution |

---

## Implementation Checklist

- [ ] Configure branch protection on `main`
- [ ] Create `.github/CODEOWNERS`
- [ ] Create `.github/PULL_REQUEST_TEMPLATE.md`
- [ ] Create `.github/ISSUE_TEMPLATE/*.yml`
- [ ] Set up labels strategy
- [ ] Create `CONTRIBUTING.md`
- [ ] Create `CHANGELOG.md`
- [ ] Create `GOVERNANCE.md`
- [ ] Configure GitHub Actions CI
- [ ] Add commitlint for commit message enforcement

---

_This document was created as part of our Foundation work to establish best practices for human-AI collaboration on GitHub. We believe these practices, when followed consistently, create projects that are welcoming, maintainable, and transparent._
