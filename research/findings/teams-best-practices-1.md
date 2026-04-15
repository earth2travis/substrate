---
title: GitHub Teams Best Practices
tags:
  - ai-agents
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/teams-best-practices-1.md
---

# GitHub Teams Best Practices

Research for zookooree org. Teams: Operations, Marketing, Finance, Product.
Members: earth2travis (human founder), agent-sivart (executive AI, all 4 teams), agent-koda (CTO AI, Operations + Product).

Sources: GitHub official documentation (docs.github.com), community patterns, agentic workflow experience.

---

## 1. Team Structure Patterns

### Flat vs Nested Teams

**Flat structure:** All teams exist at the same level under the org. Simple, easy to understand, works well for small orgs (under 20 people, under 10 teams). This is where zookooree is now.

**Nested (hierarchical) structure:** Parent teams with child teams. Child teams inherit the parent's repository access permissions. Example: `Engineering > Backend > API Team`. When you @mention a child team, only that child team is notified. When you @mention a parent team, all child teams' members are notified.

**When to use child teams:**
- When a department has sub-specialties that need different repo access levels
- When you want cascading permissions (parent gets read, child gets write on specific repos)
- When teams grow beyond 8-10 people and need subdivision
- Example for zookooree: `Product > Frontend` and `Product > Backend` if product engineering scales

**When to stay flat:**
- Fewer than 5 teams total
- Teams don't have natural hierarchies
- Everyone needs similar access levels
- **Recommendation for zookooree now: stay flat.** Four functional teams with 3 members is simple enough.

**Constraints on nesting:**
- Secret teams cannot be nested (no parent, no children)
- Each child team has exactly one parent
- Multiple levels of nesting are supported

### Team Size Guidelines

- **Ideal team size:** 3-8 members (aligns with two-pizza rule)
- **Review teams:** 2-4 members for effective code review rotation
- **Cross-functional teams** (like zookooree's current setup): Having agents on multiple teams is fine and expected for small orgs
- At current size (3 members), having all 3 on most teams is normal

---

## 2. Access Control

### Repository Permission Levels

From least to most access:

| Role | Key Capabilities |
|------|-----------------|
| **Read** | View code, clone, open issues, comment |
| **Triage** | Manage issues and PRs without write access (label, assign, close) |
| **Write** | Push to non-protected branches, merge PRs, manage issues |
| **Maintain** | Manage repo settings (minus destructive actions), push to protected branches |
| **Admin** | Full access including settings, deletion, managing access |

### Recommended Permission Strategy for zookooree

```
Organization base permission: Read (all members can see all repos)

Operations team → infra repos: Write
                → config/secrets repos: Maintain (earth2travis admin)
Marketing team → marketing repos: Write
                → website repos: Write
Finance team   → bookkeeping repos: Write
                → all other repos: Read (default)
Product team   → product repos: Write
                → core codebase: Write
```

### Layering Team + Individual Permissions

- GitHub uses the **highest permission wins** rule. If a user has Read via team and Write individually, they get Write.
- Org base permissions set the floor for all members.
- Team permissions layer on top of base permissions.
- Individual permissions layer on top of team permissions.
- **Best practice:** Set org base to Read, grant Write/Maintain through teams, reserve Admin for individuals (earth2travis).

### Principle of Least Privilege for Agents

**Critical for AI agents:**
- Agents should get **Write** access, not Admin, on repos they work in
- Only earth2travis should have Admin on sensitive repos
- agent-sivart (executive, all teams): Write on most repos, Maintain on repos it manages day-to-day
- agent-koda (CTO, Ops + Product): Write on product/ops repos, Read on marketing/finance repos
- Use branch protection rules to constrain what agents can push to (require PR reviews for main/production branches)
- Consider requiring human approval (earth2travis review) for merges to critical branches even if agents can create PRs

---

## 3. CODEOWNERS Integration

### Using @org/team in CODEOWNERS

CODEOWNERS file location (checked in order): `.github/CODEOWNERS`, `CODEOWNERS` (root), `docs/CODEOWNERS`. First found wins.

**Requirements for team-based CODEOWNERS:**
- The team must have **write** access to the repository
- The team must be **visible** (not secret)
- CODEOWNERS file must be on the base branch of the PR

### Example CODEOWNERS for zookooree

```
# Default owners (executive oversight)
*                       @zookooree/operations

# Product code
/src/                   @zookooree/product
/packages/              @zookooree/product

# Infrastructure
/infra/                 @zookooree/operations
/.github/               @zookooree/operations
Dockerfile              @zookooree/operations

# Documentation
/docs/marketing/        @zookooree/marketing
/docs/finance/          @zookooree/finance

# Financial data
/bookkeeping/           @zookooree/finance
```

### Review Assignment Algorithms

When a team is requested for review via CODEOWNERS, GitHub can auto-assign individual reviewers instead of notifying the whole team. Two algorithms:

**Round Robin:**
- Assigns based on who received the least recent review request
- Alternates through all team members regardless of current load
- Best for: evenly distributed review burden, teams where all members are equally capable

**Load Balance:**
- Considers each member's total number of recent review requests AND outstanding (incomplete) reviews
- Tries to equalize reviews over a 30-day rolling window
- Best for: teams with varying availability, prevents pile-up on one person
- **Recommended for zookooree:** Load balance, since agents can handle more reviews than humans

### Auto-Assignment Settings

- Enable per-team under Team Settings > Code review
- When enabled, the team is removed as reviewer and replaced by assigned individuals
- Exception: if branch protection requires code owner review, the team stays AND individuals are added
- Members with "Busy" status are skipped
- You can set how many reviewers to assign (e.g., 1 of 3 team members)
- You can exclude specific members from auto-assignment rotation

---

## 4. Team Discussions

### Status: Deprecated

**Team Discussions were sunset by GitHub in February 2023.** They no longer exist as a feature.

### Replacement: GitHub Discussions

GitHub now recommends **organization-level Discussions** or **repository-level Discussions** as the replacement.

**Repository Discussions:**
- Tied to a specific repo
- Best for: technical discussions about that repo's code, feature requests, Q&A
- Supports categories, polls, marking answers

**Organization Discussions:**
- Available at the org level
- Best for: cross-team communication, org-wide announcements, policies
- Not tied to any specific repo

### Recommendation for zookooree

- Use **org-level Discussions** for cross-team topics (strategy, announcements, decisions)
- Use **repo-level Discussions** for technical topics within specific repos
- For small org size, GitHub Issues may be sufficient for most communication
- Consider using GitHub Projects for coordination instead of discussions

---

## 5. Review Workflows

### Required Reviewers from Teams

Configure via branch protection rules (Settings > Branches > Branch protection rules):

- **Require pull request reviews before merging:** Set minimum number of approvals
- **Require review from Code Owners:** PRs touching CODEOWNERS-matched files need approval from designated owners
- **Dismiss stale reviews:** When new commits are pushed, previous approvals are dismissed (forces re-review)
- **Restrict who can dismiss reviews:** Limit to admins or specific people

### Recommended Review Workflow for zookooree

```
Branch protection on main:
  - Require 1 approval minimum
  - Require review from CODEOWNERS
  - Dismiss stale reviews on new pushes
  - Restrict dismissal to earth2travis (human oversight)
```

**For agent-created PRs:**
- Agents create PRs with clear descriptions
- CODEOWNERS routes review to appropriate team
- Auto-assignment picks the reviewer (load balanced)
- For critical repos: require earth2travis approval
- For routine repos: any team member approval suffices

### Team Review Request Routing

When you request review from a team:
1. If auto-assignment is ON: team is replaced by individual assignees
2. If auto-assignment is OFF: entire team is notified
3. You can also request review from specific individuals in addition to teams

### Dismissing Stale Reviews

- Enable "Dismiss stale pull request approvals when new commits are pushed"
- This is critical for agent workflows: if an agent pushes follow-up commits after approval, the approval resets
- Prevents merging code that wasn't reviewed in its final form
- **Strongly recommended for zookooree** given agents may iterate on PRs

---

## 6. Notifications

### Team Notification Settings

Each team can configure:
- **Notify entire team** vs **Only notify requested team members** (under Code review settings)
- "Only notify requested" reduces noise when auto-assignment routes to specific individuals

### @mention Routing

- `@zookooree/operations` notifies all Operations team members
- `@zookooree/product` notifies all Product team members
- For nested teams: mentioning a parent notifies parent + all child team members
- Mentioning a child team notifies only that child team

### Avoiding Notification Fatigue

**For a 3-person org with AI agents:**
1. **Enable auto-assignment** on all teams: prevents duplicate notifications (team + individual)
2. **Set "Only notify requested team members"** on teams
3. **Use Scheduled Reminders** (Slack integration): Daily digest of pending reviews instead of real-time pings
4. **Agent notification strategy:** Agents don't need email/Slack notifications. They should poll or use webhooks.
5. **Limit CODEOWNERS breadth:** Don't make every file owned by every team. Use specific paths.
6. **Unwatch repos** that don't need attention from specific team members

### Scheduled Reminders

- Available for teams via Slack integration
- Team maintainers and org owners can configure
- Sends digest of PRs awaiting team review at specified times
- Limited to 5 repos per reminder (can create multiple reminders)
- Up to 20 oldest PRs shown per repo

---

