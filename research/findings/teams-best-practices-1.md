---
title: "GitHub Teams Best Practices Part 1: Structure, Access, and CODEOWNERS"
tags: [github, teams, access-control, codeowners, organization, permissions]
related:
- teams-best-practices-2
- microsolidarity-five-scales
- big-lab-approaches
source: research/raw/teams-best-practices-1.md
---
# GitHub Teams Best Practices Part 1: Structure, Access, and CODEOWNERS

Research for zookooree org. Teams: Operations, Marketing, Finance, Product. Members: earth2travis (human founder), agent-sivart (executive AI, all 4 teams), agent-koda (CTO AI, Operations + Product).

## Team Structure Patterns

**Flat vs Nested**
- Flat: all teams at same level. Simple, works for small orgs (under 20 people, under 10 teams)
- Nested: parent teams with child teams. Child inherits parent's repo access. Parent mentions notify all children
- Recommendation for zookooree now: **stay flat**. Four functional teams with 3 members is simple enough

**Team Size Guidelines**
- Ideal: 3-8 members (two-pizza rule)
- Review teams: 2-4 members for effective rotation
- Having agents on multiple teams is fine for small orgs

## Access Control

**Repository Permission Levels** (least to most): Read → Triage → Write → Maintain → Admin

**Recommended Strategy:**
- Org base permission: Read
- Operations → infra repos: Write; config/secrets: Maintain (earth2travis admin)
- Marketing → marketing/website repos: Write
- Finance → bookkeeping repos: Write
- Product → product/core repos: Write

**Layering:** Highest permission wins. Set org base to Read, grant Write/Maintain through teams, reserve Admin for individuals.

**Principle of Least Privilege for Agents:**
- Agents get Write, not Admin
- Only earth2travis has Admin on sensitive repos
- agent-sivart: Write on most, Maintain on managed repos
- agent-koda: Write on product/ops, Read on marketing/finance
- Branch protection rules constrain pushes to main/production

## CODEOWNERS Integration

File location priority: `.github/CODEOWNERS` → `CODEOWNERS` (root) → `docs/CODEOWNERS`. First found wins.

**Requirements for team-based CODEOWNERS:**
- Team must have write access to the repository
- Team must be visible (not secret)
- CODEOWNERS file must be on the base branch of the PR

**Example for zookooree:**
```
*                       @zookooree/operations
/src/                   @zookooree/product
/infra/                 @zookooree/operations
/docs/marketing/        @zookooree/marketing
/bookkeeping/           @zookooree/finance
```

**Review Assignment Algorithms:**
- Round Robin: least recent review request. Best for evenly distributed burden
- Load Balance: considers total recent requests AND outstanding reviews. **Recommended for zookooree** (agents handle more reviews than humans)

**Auto-Assignment Settings:**
- Enable per-team under Team Settings > Code review
- When enabled, team is removed as reviewer and replaced by assigned individuals
- Members with "Busy" status are skipped
- Can set how many reviewers to assign (e.g., 1 of 3)

## Team Discussions

**Deprecated by GitHub in February 2023.** Replacement: organization-level or repository-level Discussions.
- Org-level: cross-team topics, strategy, announcements
- Repo-level: technical topics within specific repos
- For small orgs, GitHub Issues may be sufficient
