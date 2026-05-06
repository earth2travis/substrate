---
title: "Agentic Organization: GitHub Teams and Repository Architecture"
tags: [agent, organization, github, governance, teams, architecture]
related: [[agentic-architecture]], [[agent-security]], [[skills-as-onboarding]]
source: research/raw/agentic-maximization.md
---

# Agentic Organization: GitHub Teams and Repository Architecture

## Organizational Structure

The maximization plan for an agentic organization uses GitHub Teams for review assignment and access control:

| Team | Members | Purpose |
|------|---------|---------|
| `@org/founders` | earth2travis | Human oversight, final approval |
| `@org/executive` | agent-sivart | Executive operations |
| `@org/engineering` | agent-koda | Architecture, infrastructure |
| `@org/agents` | all agents | General agent team |
| `@org/reviewers` | all members | PR review pool |

Teams enable team mentions in CODEOWNERS, team-based review assignment, and team-based access control per repository.

## Repository Architecture

| Repo | Purpose | Access |
|------|---------|--------|
| `the-agent-factory` | Org hub: governance, decisions, communication | All members |
| `sivart` | Sivart's workspace, personal projects | agent-sivart (write), others (read) |
| `koda` | Koda's workspace | agent-koda (write), others (read) |
| `infrastructure` | Shared infra, CI/CD templates, Actions | engineering team (write) |
| `knowledge-base` | Org knowledge, docs, wiki-style content | All members |
| `zookooree.github.io` | Public website | All members |

## Communication Architecture

Uses Discussions on `the-agent-factory` as the primary async communication channel:

| Category | Type | Purpose |
|----------|------|---------|
| Announcements | Announcement | Decisions, policy changes (founders only create) |
| Architecture | General | Technical design discussions |
| Daily Reports | General | Agent daily/weekly reports |
| Proposals | General | RFCs and proposals for review |
| Q&A | Q&A | Questions with accepted answers |
| General | General | Open discussion |

## Governance Model: Layered Review

CODEOWNERS assigns reviewers automatically based on file paths. Rulesets enforce required reviews (1-2), CI must pass, and no force push to main. Environment protection: staging auto-deploys; production requires human approval.

**Tiered review policy:**
- **Agent workspace repos**: 1 review required (peer agent or human)
- **the-agent-factory (main branch)**: 2 reviews required
- **Infrastructure/workflows**: CODEOWNERS requires both human plus CTO agent
- **Decisions/policies**: CODEOWNERS requires human only

## CI/CD Strategy

Budget: 3,000 Linux minutes per month. Approximately 100 minutes per day. If each PR runs approximately 3 minutes of CI, that supports approximately 33 PRs per day.

**Optimization strategies:**
1. **Self-hosted runner**: Set up on Hetzner server. Free, unlimited minutes.
2. **Conditional workflows**: Only run expensive jobs when relevant files change.
3. **Caching**: Cache dependencies aggressively.
4. **Concurrency**: Use `concurrency` groups to cancel redundant runs.

## Knowledge Management Layers

| Layer | Feature | Content | Review? |
|-------|---------|---------|---------|
| Formal | Repo files + PRs | Decisions, policies, architecture docs | Yes (PR review) |
| Reference | Wiki | Runbooks, quick-reference, how-tos | No (direct edit) |
| Discussion | Discussions | Proposals, reports, open questions | Comment-based |
| Tracking | Projects + Issues | Tasks, bugs, features | Status-based |
| History | Git log + PR history | Full audit trail | Inherent |

## Agent Onboarding Playbook

1. Create GitHub account for the agent (e.g., `agent-newname`)
2. Invite to org as member
3. Add to teams: `@org/agents`, relevant specialty teams
4. Create workspace repo: `newname` with standard template
5. Configure access: Write to own workspace, read to all others
6. Set up CLI: `gh auth login` with agent's PAT or OAuth token
7. Update CODEOWNERS: Add agent to relevant file patterns
8. Update team review assignments: Include in review rotation
9. Announce in Discussions: Introduction post in Announcements
