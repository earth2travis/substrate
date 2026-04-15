---
title: .github/CODEOWNERS for the-agent-factory
tags:
  - ai-agents
  - knowledge-management
  - lean-manufacturing
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/feature-deep-dives-1.md
---

## 2. Feature Deep Dives

### 2.1 GitHub Discussions (Free + Team)

**What it does:** Threaded forum-style conversations within a repository. Categories, labels, pinning, polls, answered/unanswered status. Can be used org-wide by enabling on a central repo.

**Agentic application:** Primary communication channel for agents. Discussions are API-accessible (`gh api` or GraphQL), meaning agents can create, read, and reply to discussions programmatically. Unlike Issues (task-oriented), Discussions are for open-ended communication, decisions, and knowledge sharing.

**Configuration recommendations:**
- Enable Discussions on `the-agent-factory` repo as the org-wide forum
- Create categories: `Announcements`, `Decisions`, `Architecture`, `Agent Reports`, `General`, `Q&A`
- Use the `Announcement` category type for decisions (only maintainers can create, anyone can reply)
- Pin key decisions and architecture discussions
- Agents post daily/weekly reports as Discussion threads
- Use labels to tag discussions by agent or domain

**Free vs Team:** Discussions work identically on both plans. No Team unlock needed.

### 2.2 GitHub Projects (Free + Team)

**What it does:** Kanban boards and table views with custom fields, automations, and workflows. Projects v2 supports cross-repo tracking, custom field types (text, number, date, single select, iteration), and built-in automations.

**Agentic application:** Central task management. Agents can create issues, move cards, update custom fields via `gh project` CLI commands. Use iterations for sprint planning. Custom fields can track which agent owns a task, priority, estimated effort.

**Configuration recommendations:**
- Create org-level projects (not repo-level) for cross-repo visibility
- Custom fields: `Agent` (single select), `Priority` (single select), `Domain` (single select), `Estimated Hours` (number)
- Built-in automations: auto-add issues from specific repos, auto-set status when PR merges
- Views: per-agent filtered views, priority views, sprint views

**Free vs Team:** Projects v2 works on Free. No Team-specific unlock, but Team provides better insights into contributor activity.

### 2.3 GitHub Actions (2,000 Free → 3,000 Team)

**What it does:** CI/CD and workflow automation. Runs on GitHub-hosted runners (Linux, Windows, macOS) or self-hosted runners. Triggered by events (push, PR, schedule, workflow_dispatch, repository_dispatch, discussion events, etc.).

**Agentic application:** This is the automation backbone. Use Actions for:
- **CI/CD:** Lint, test, build on every PR
- **Agent workflows:** Scheduled workflows that trigger agent activities
- **Automated reviews:** Workflows that run code analysis and post PR comments
- **Cross-repo orchestration:** `repository_dispatch` to trigger workflows across repos
- **Discussion automation:** Workflows triggered by discussion creation/comments
- **Deployment:** Auto-deploy Pages, packages, or services

**Minutes breakdown (Team: 3,000/month):**
- Linux runners: 1x multiplier (3,000 actual minutes)
- Windows: 2x multiplier (1,500 actual minutes)
- macOS: 10x multiplier (300 actual minutes)
- Self-hosted runners: **free, no minute consumption**

**Configuration recommendations:**
- Use Linux runners exclusively to maximize minutes
- Set up a self-hosted runner on your Hetzner server for unlimited minutes (agent workloads that run frequently)
- Use `workflow_dispatch` for on-demand agent tasks
- Use `schedule` (cron) for periodic agent activities
- Monitor usage: Settings → Billing → Actions usage
- Set spending limits to prevent overages ($0 to hard-cap)

**Free vs Team:** 50% more minutes (2,000 → 3,000). Team also unlocks "larger runners" as a paid add-on if needed.

### 2.4 GitHub Codespaces (Team unlock: org-paid)

**What it does:** Cloud-hosted dev environments in Docker containers. Accessible via browser, VS Code, or CLI. Configurable via `.devcontainer/devcontainer.json`. Machine types from 2-core/8GB to 32-core/128GB.

**Agentic application:** Limited direct value for CLI-based agents (they already have their own compute). Potential uses:
- **Human developer onboarding:** If earth2travis or future human contributors need to jump into code quickly
- **Standardized environments:** Ensure all contributors (human or agent) work in identical environments
- **Ephemeral workspaces:** Spin up a codespace for a specific task, destroy when done

**Configuration recommendations:**
- On Team plan, org owners can choose to pay for members' codespace usage
- Keep spending limit at $0 unless actively needed
- Create `.devcontainer/devcontainer.json` in key repos for standardized environments
- Not a priority for agent-first workflows

**Free vs Team:** Free gives personal quotas (120 core-hours/month). Team allows org to pay for members' usage and control policies (which repos allow codespaces, machine type limits, idle timeout).

### 2.5 Repository Rulesets (Team feature)

**What it does:** Named, layered rule configurations that control how people interact with branches and tags. Up to 75 rulesets per repo. Supports bypass permissions (specific users, teams, or GitHub Apps). Can be Active, Evaluate (audit mode), or Disabled. Rules stack: most restrictive wins.

**Key advantages over branch protection rules:**
- Multiple rulesets can layer (branch protection is one rule per branch pattern)
- Rulesets have statuses (active/disabled/evaluate) without deletion
- Anyone with read access can view active rulesets (transparency)
- Push rulesets can restrict file paths, extensions, and sizes across the entire fork network

**Agentic application:** Critical for governance in an agent factory:
- **Protect main branch:** Require PRs, reviews, and CI passing before merge
- **Agent bypass rules:** Give specific agents bypass permissions for automated operations
- **Push rulesets:** Prevent agents from pushing certain file types (e.g., binaries, credentials)
- **Evaluate mode:** Test new rules before enforcing (see what would be blocked without actually blocking)

**Configuration recommendations:**
- **Ruleset 1 - Main branch protection:**
  - Target: `main` branch
  - Rules: Require PR before merge, require 1 approval, require status checks to pass, block force pushes, block deletions
  - Bypass: `earth2travis` (admin), specific CI bot accounts
- **Ruleset 2 - Push safety:**
  - Target: All branches
  - Rules: Restrict file extensions (`.env`, `.key`, `.pem`), restrict file size (10MB max)
  - No bypass
- **Ruleset 3 - Agent workspace rules (lighter):**
  - Target: Agent workspace repos (sivart, etc.)
  - Rules: Require status checks only (agents can push directly to their own branches)

**Free vs Team:** Repository-level rulesets work on both Free and Team. Organization-wide rulesets require Enterprise. The Team unlock is primarily about the branch protection and reviewer features that rulesets complement.

### 2.6 Required and Multiple PR Reviewers (Team unlock)

**What it does:** Require one or more approving reviews before a PR can be merged. Can specify exact number of required reviews. "Team PR reviewers" allows assigning entire teams for review.

**Agentic application:** Foundational for agent governance:
- **Human oversight:** Require earth2travis approval on critical repos
- **Agent peer review:** Agent-koda reviews agent-sivart's PRs and vice versa
- **Tiered review:** Some repos need 1 review (agent workspaces), others need 2 (the-agent-factory main)

**Configuration recommendations:**
- `the-agent-factory` main branch: 2 required reviewers (ensures at least one human or senior agent reviews)
- Agent workspace repos: 1 required reviewer (peer agent or human)
- Create GitHub Teams: `@zookooree/agents`, `@zookooree/founders`, `@zookooree/reviewers`
- Use team review assignment to auto-distribute reviews

**Free vs Team:** Free orgs cannot require PR reviewers on private repos. This is a core Team unlock.

### 2.7 Draft Pull Requests (Team for private repos)

**What it does:** Mark a PR as "draft" to signal it's not ready for review. Draft PRs cannot be merged. CODEOWNERS are not auto-requested for drafts. Converting to "ready for review" triggers notifications.

**Agentic application:**
- Agents open draft PRs for work-in-progress, converting to ready when CI passes
- Allows visibility into what agents are working on before it's review-ready
- Human founder can browse draft PRs to see agent activity

**Configuration recommendations:**
- Establish convention: agents always open as draft first, convert when ready
- Use GitHub Actions to auto-convert draft → ready when all checks pass
- Draft PRs appear in project boards, giving visibility into pipeline

**Free vs Team:** Draft PRs work in public repos on Free. Team unlocks them for private repos.

### 2.8 CODEOWNERS (Team unlock for private repos)

**What it does:** A `CODEOWNERS` file maps file patterns to responsible users/teams. Code owners are automatically requested for PR review when their files are modified. Combined with required reviews, ensures the right people approve changes.

**Agentic application:** Maps ownership domains to agents:
- Agent-koda owns `/architecture/`, `/infrastructure/`
- Agent-sivart owns `/operations/`, `/reports/`
- Earth2travis owns `/decisions/`, `/policies/`
- Each agent owns their workspace repo entirely

**Configuration recommendations:**
```
# .github/CODEOWNERS for the-agent-factory

# Default: human founder reviews everything not otherwise specified
* @earth2travis

# Architecture decisions need CTO agent
/architecture/ @agent-koda
/infrastructure/ @agent-koda

# Operations
/operations/ @agent-sivart
/reports/ @agent-sivart

# Governance - human only
/decisions/ @earth2travis
/policies/ @earth2travis

# Workflows need both human and CTO
/.github/workflows/ @earth2travis @agent-koda
```

