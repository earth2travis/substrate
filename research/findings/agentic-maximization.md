---
title: Create a discussion
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/agentic-maximization.md
---

## 3. Maximizing Team Plan for Agentic Organizations

### 3.1 Organizational Structure

**Teams (GitHub Teams, not the plan):**
Create GitHub Teams within the org for review assignment and access control:

| Team | Members | Purpose |
|------|---------|---------|
| `@zookooree/founders` | earth2travis | Human oversight, final approval |
| `@zookooree/executive` | agent-sivart | Executive operations |
| `@zookooree/engineering` | agent-koda | Architecture, infrastructure |
| `@zookooree/agents` | all agents | General agent team |
| `@zookooree/reviewers` | all members | PR review pool |

Teams enable:
- Team mentions in CODEOWNERS
- Team-based review assignment (auto-distribute reviews across team members)
- Team-based access control per repo

### 3.2 Repository Architecture

| Repo | Purpose | Access |
|------|---------|--------|
| `the-agent-factory` | Org hub: governance, decisions, communication | All members |
| `sivart` | Sivart's workspace, personal projects | agent-sivart (write), others (read) |
| `koda` | Koda's workspace | agent-koda (write), others (read) |
| `infrastructure` | Shared infra, CI/CD templates, Actions | engineering team (write) |
| `knowledge-base` | Org knowledge, docs, wiki-style content | All members |
| `zookooree.github.io` | Public website | All members |

### 3.3 Communication Architecture (Discussions)

Use Discussions on `the-agent-factory` as the primary async communication channel:

| Category | Type | Purpose |
|----------|------|---------|
| Announcements | Announcement | Decisions, policy changes (founders only create) |
| Architecture | General | Technical design discussions |
| Daily Reports | General | Agent daily/weekly reports |
| Proposals | General | RFCs and proposals for review |
| Q&A | Q&A | Questions with accepted answers |
| General | General | Open discussion |

**API access for agents:**
```bash
# Create a discussion
gh api graphql -f query='mutation { createDiscussion(input: {
  repositoryId: "REPO_ID",
  categoryId: "CATEGORY_ID", 
  title: "Daily Report: 2026-03-22",
  body: "..."
}) { discussion { id url } } }'

# List discussions
gh api graphql -f query='{ repository(owner: "zookooree", name: "the-agent-factory") {
  discussions(first: 10) { nodes { title body author { login } } }
} }'
```

### 3.4 Governance Model: Layered Review

```
┌─────────────────────────────────────┐
│  CODEOWNERS assigns reviewers       │
│  automatically based on file paths  │
├─────────────────────────────────────┤
│  Rulesets enforce:                  │
│  - Required reviews (1-2)           │
│  - CI must pass                     │
│  - No force push to main            │
├─────────────────────────────────────┤
│  Environment protection:            │
│  - Staging: auto-deploy             │
│  - Production: human approval       │
└─────────────────────────────────────┘
```

**Tiered review policy:**
- **Agent workspace repos:** 1 review required (peer agent or human)
- **the-agent-factory (main branch):** 2 reviews required
- **Infrastructure/workflows:** CODEOWNERS requires both human + CTO agent
- **Decisions/policies:** CODEOWNERS requires human only

### 3.5 CI/CD Strategy (3,000 minutes/month)

**Minute budget:**
- 3,000 Linux minutes = ~100 minutes/day
- If each PR runs ~3 minutes of CI, that's ~33 PRs/day before hitting limits
- With agents potentially creating many PRs, this could get tight

**Optimization strategies:**
1. **Self-hosted runner:** Set up on your Hetzner server. Free, unlimited minutes. Best for agent-heavy workflows.
2. **Conditional workflows:** Only run expensive jobs when relevant files change
3. **Caching:** Cache dependencies aggressively
4. **Concurrency:** Use `concurrency` groups to cancel redundant runs

**Recommended setup:**
```yaml
# Use self-hosted for frequent agent workflows
runs-on: self-hosted

# Use GitHub-hosted for standard CI
runs-on: ubuntu-latest
```

### 3.6 Knowledge Management

Layer multiple GitHub features for organizational memory:

| Layer | Feature | Content | Review? |
|-------|---------|---------|---------|
| **Formal** | Repo files + PRs | Decisions, policies, architecture docs | Yes (PR review) |
| **Reference** | Wiki | Runbooks, quick-reference, how-tos | No (direct edit) |
| **Discussion** | Discussions | Proposals, reports, open questions | Comment-based |
| **Tracking** | Projects + Issues | Tasks, bugs, features | Status-based |
| **History** | Git log + PR history | Full audit trail | Inherent |

### 3.7 Agent Onboarding Playbook

When adding a new agent to the org:

1. **Create GitHub account** for the agent (e.g., `agent-newname`)
2. **Invite to org** as member ($4/month added to bill)
3. **Add to teams:** `@zookooree/agents`, relevant specialty teams
4. **Create workspace repo:** `newname` with standard template
5. **Configure access:** Write to own workspace, read to all others
6. **Set up CLI:** `gh auth login` with agent's PAT or OAuth token
7. **Update CODEOWNERS:** Add agent to relevant file patterns
8. **Update team review assignments:** Include in review rotation
9. **Announce in Discussions:** Introduction post in Announcements

### 3.8 Security Without Advanced Security Add-ons

Before paying for Secret Protection ($19/committer) or Code Security ($30/committer):

1. **Repository rulesets (push rules):** Block `.env`, `.key`, `.pem`, `.secret` file extensions
2. **Pre-commit hooks:** Agents run local secret scanning before push
3. **Dependabot alerts:** Free, enable on all repos
4. **Dependabot security updates:** Free, auto-create PRs for vulnerable dependencies
5. **Secret scanning for public repos:** Free (if any repos are public)
6. **GitHub Actions secrets:** Use Actions secrets and environment secrets instead of hardcoding
7. **.gitignore templates:** Standard ignores for credentials files

### 3.9 Automation Patterns

**Pattern 1: Agent Activity Dashboard**
- GitHub Actions workflow runs daily, queries all agent PRs/issues/discussions
- Generates a summary and posts to Discussions

**Pattern 2: Auto-assign Reviews**
- CODEOWNERS handles file-based assignment
- Team review assignment distributes across available reviewers
- Round-robin or load-balanced assignment

**Pattern 3: Cross-repo Orchestration**
- `repository_dispatch` events trigger workflows across repos
- Agent-sivart dispatches to agent-koda's repo: "review this architecture"

**Pattern 4: Automated Reports**
- Scheduled Action generates weekly org report
- Posts to Discussions as a formatted summary
- Tracks metrics: PRs merged, issues closed, discussions created

---

