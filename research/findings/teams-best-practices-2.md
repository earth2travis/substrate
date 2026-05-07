---
title: "GitHub Teams Best Practices Part 2: Security, Scaling, and Agentic Patterns"
tags: [github, teams, security, agents, scaling, automation, permissions]
related:
- teams-best-practices-1
- microsolidarity-five-scales
- big-lab-approaches
source: research/raw/teams-best-practices-2.md
---
# GitHub Teams Best Practices Part 2: Security, Scaling, and Agentic Patterns

## Team Maintainers vs Members

| Capability | Member | Maintainer |
|---|---|---|
| View/be assigned/receive notifications | Yes | Yes |
| Add/remove members | No | Yes |
| Edit team name/description | No | Yes |
| Change visibility | No | Yes |
| Manage code review settings | No | Yes |
| Set up scheduled reminders | No | Yes |
| Delete team | No | Org owners only |
| Manage repo access | No | Org owners only |

**Principle:** Maintainer controls team membership and settings, not repo access. Keep it minimal.
- earth2travis: Maintainer on ALL teams
- agent-sivart: Member on all teams (cautious about giving agents Maintainer — they can add/remove members)
- agent-koda: Member on Operations and Product

## Security

**Team Visibility:**
- Visible teams: can be seen, @mentioned, nested, used in CODEOWNERS. **Default and recommended**
- Secret teams: only visible to members and org owners, cannot be nested. Use for: security response, acquisition, HR-sensitive

**Recommendation for zookooree:** All teams visible.

**External Collaborators vs Team Members:**
- Team members: org-level base permissions, can be on multiple teams, show in org member list
- Outside collaborators: repo-level access only, cannot be on teams. Use for: contractors, temporary contributors

**Additional Security:**
- Require two-factor authentication for org
- Branch protection on all important branches
- Review team membership quarterly
- For agents: use fine-grained PATs with minimal scopes
- Rotate tokens quarterly

## Scaling Patterns

| Trigger | Action |
|---|---|
| New functional area | Create new team |
| Team exceeds 8-10 members | Consider splitting |
| Subgroup needs different repo access | Create child team |
| Cross-functional project | Create temporary project team |

**Scaling Roadmap for zookooree:**
- Current (3 members, 4 teams): flat structure, visible teams, simple CODEOWNERS
- 5-10 members: keep flat, enable auto-assignment, formalize CODEOWNERS
- 10-25 members: introduce nested teams, cross-functional project teams, scheduled reminders
- 25+ members: full nested hierarchy, custom roles, team sync with identity provider

## Agentic-Specific Patterns

**Identity and Access:**
- Each agent gets its own GitHub account
- Agents are full org members (not outside collaborators)
- Use fine-grained PATs with minimal scopes
- Rotate tokens quarterly
- Agents should NOT have org owner role

**PR Creation by Agents:**
- Structured, descriptive titles (conventional commits)
- PR descriptions: what changed, why, testing done, related issues
- Self-assign PRs they create
- Labels: `agent-created`, `automated`
- Require human review on critical repos

**Automated Review by Agents:**
- Agents CAN be CODEOWNERS and receive review requests
- For agent-to-agent review: ensure at least one human in the review chain for critical paths
- Agent reviews are advisory; human review required for merge on main

**Issue Triage by Agents:**
- Agents with Triage or Write access can label, assign, close
- Use GitHub Actions + agent accounts for automated triage
- Pattern: scan new issues, apply labels, assign to appropriate team

**Notification Strategy:**
- Agents don't use email/Slack. Use webhooks or API polling
- Configure agent accounts to NOT send email notifications
- Use GitHub Actions `pull_request_review_requested` event to trigger agent workflows

**Guardrails:**
- Branch protection: agents cannot push directly to protected branches
- Required reviews: at least 1 human approval for production branches
- CODEOWNERS: human is CODEOWNER for sensitive paths (secrets, config, CI)
- Dismiss stale reviews: enabled so agents can't approve then push more code

**Anti-Patterns:**
- Giving agents Admin access "for convenience"
- Agent-only review chains with no human oversight
- Agents as org owners
- Shared agent accounts
- Agents managing team membership
- Bypassing branch protection for agent speed
- Secret teams for agents (makes auditing harder)

## Recommended Configuration for zookooree

**Immediate:**
1. Org base permission: Read
2. Team visibility: All visible
3. Team structure: Flat (4 teams, no nesting)
4. Maintainers: earth2travis on all teams
5. Agent roles: Member (not Maintainer)
6. Branch protection: Require 1 review, dismiss stale, require CODEOWNERS

**Team Permission Matrix:**
| Team | earth2travis | agent-sivart | agent-koda |
|---|---|---|---|
| Operations | Maintainer | Member | Member |
| Marketing | Maintainer | Member | - |
| Finance | Maintainer | Member | - |
| Product | Maintainer | Member | Member |
