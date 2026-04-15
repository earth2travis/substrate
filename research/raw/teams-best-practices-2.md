## 7. Team Maintainers vs Members

### Role Comparison

| Capability | Member | Maintainer |
|-----------|--------|------------|
| View team membership | ✅ | ✅ |
| Be assigned to team PRs | ✅ | ✅ |
| Receive team notifications | ✅ | ✅ |
| Add/remove team members | ❌ | ✅ |
| Edit team name/description | ❌ | ✅ |
| Change team visibility | ❌ | ✅ |
| Manage code review settings | ❌ | ✅ |
| Set up scheduled reminders | ❌ | ✅ |
| Delete the team | ❌ | ❌ (org owners only) |
| Manage team repo access | ❌ | ❌ (org owners only) |

### Who Should Be Maintainer

**earth2travis:** Maintainer on ALL teams (human oversight, can manage membership)

**agent-sivart:** Member on all teams, potentially Maintainer on Operations (if it needs to manage team settings autonomously). Be cautious giving agents Maintainer role since they can add/remove members.

**agent-koda:** Member on Operations and Product. No maintainer role needed.

**Principle:** Maintainer role controls team membership and settings, not repo access. Keep it minimal. Org owner (earth2travis) can always manage everything regardless.

---

## 8. Security

### Team Visibility: Visible vs Secret

**Visible teams:**
- Can be seen and @mentioned by any org member
- Can be nested (parent/child)
- Can be used in CODEOWNERS
- **Default and recommended for most teams**

**Secret teams:**
- Only visible to team members and org owners
- Cannot be nested
- Can still be used in CODEOWNERS (but other members can't see who's on the team)
- Use cases: security response teams, acquisition teams, HR-sensitive groups

**Recommendation for zookooree:** All four teams should be **visible**. No current need for secret teams.

### External Collaborators vs Team Members

**Team members** (org members on teams):
- Have org-level base permissions
- Can be on multiple teams
- Show up in org member list
- Can @mention and be @mentioned via teams

**Outside collaborators:**
- Cannot be added to teams
- Get repo-level access only (per-repo invitation)
- Don't count toward org member limits on some plans
- Use for: contractors, temporary contributors, external auditors

**For zookooree:** All three members (earth2travis, agent-sivart, agent-koda) should be full org members on teams. Use outside collaborator status only for humans or agents that need limited, temporary access.

### Additional Security Practices

- Enable **two-factor authentication requirement** for the org
- Use **branch protection rules** on all important branches
- Enable **audit log** monitoring (Enterprise feature) if available
- Review team membership quarterly
- For agents: use fine-grained personal access tokens with minimal scopes
- Consider **required status checks** (CI must pass before merge)

---

## 9. Scaling Patterns

### When to Add Teams

| Trigger | Action |
|---------|--------|
| New functional area (e.g., Legal, Sales) | Create new team |
| Team exceeds 8-10 members | Consider splitting |
| Subgroup needs different repo access | Create child team |
| New repo cluster with distinct ownership | Assign to existing or new team |
| Cross-functional project needs coordination | Create temporary project team |

### When to Split Teams

- **Size:** Over 8-10 members, review cycles slow down
- **Scope:** Team owns repos with very different concerns
- **Conflict:** Too many CODEOWNERS conflicts (multiple areas, one team)
- **Specialization:** Members develop distinct expertise areas

### Scaling Roadmap for zookooree

**Current (3 members, 4 teams):** Flat structure, all teams visible, simple CODEOWNERS.

**5-10 members:**
- Keep flat structure
- Start using auto-assignment with load balancing
- Formalize CODEOWNERS per repo
- Consider adding a "Security" team

**10-25 members:**
- Introduce nested teams where natural hierarchies emerge (e.g., Product > Frontend, Product > Backend)
- Create cross-functional project teams for major initiatives
- Implement scheduled reminders for review management
- Add Triage role for junior contributors

**25+ members:**
- Full nested team hierarchy
- Custom repository roles (Enterprise feature)
- Team sync with identity provider
- Formal team lead (Maintainer) structure per team
- Consider separate teams for different repos within same function

---

## 10. Agentic-Specific Patterns

### Best Practices for AI Agents on GitHub Teams

#### Identity and Access

- Each agent gets its own GitHub account (agent-sivart, agent-koda)
- Agents are full org members, not outside collaborators (they need team membership)
- Use **fine-grained personal access tokens** (PATs) with minimal required scopes
- Rotate tokens on a schedule (quarterly minimum)
- Agents should NOT have org owner role; use team membership for access

#### PR Creation by Agents

- Agents create PRs with structured, descriptive titles (conventional commits)
- PR descriptions should include: what changed, why, testing done, related issues
- Agents should self-assign PRs they create
- Use labels to indicate agent-created PRs (e.g., `agent-created`, `automated`)
- Set up branch protection to require human review on agent PRs for critical repos

#### Automated Review by Agents

- Agents CAN be CODEOWNERS and receive review requests
- For agent-to-agent review: ensure at least one human is in the review chain for critical paths
- Agents should leave structured review comments (approve/request changes with clear rationale)
- Consider a policy: agent reviews are advisory, human review required for merge on main
- Use auto-assignment load balancing so agent reviews don't overwhelm one agent

#### Issue Triage by Agents

- Agents with Triage or Write access can label, assign, and close issues
- Use GitHub Actions + agent accounts for automated triage workflows
- Pattern: agent scans new issues, applies labels, assigns to appropriate team
- Agents can create issues from monitoring/alerting systems
- Use issue templates to ensure structured input that agents can parse

#### Review Workflow for Mixed Human/Agent Teams

Recommended flow for zookooree:

```
1. Agent creates PR (agent-sivart or agent-koda)
2. CODEOWNERS auto-requests review from relevant team
3. Auto-assignment routes to specific reviewer
4. If reviewer is an agent: agent reviews within minutes
5. If reviewer is earth2travis: waits for human review
6. Critical repos: ALWAYS require earth2travis approval
7. Routine repos: any team member (including agents) can approve
```

#### Notification Strategy for Agents

- Agents don't use email/Slack notifications like humans
- Instead: use GitHub webhooks or polling via API to detect review requests
- Configure agent accounts to NOT send email notifications (reduces noise)
- Use GitHub Actions `pull_request_review_requested` event to trigger agent review workflows

#### Guardrails

- **Branch protection:** Agents cannot push directly to protected branches
- **Required reviews:** At least 1 human approval for production branches
- **CODEOWNERS:** Ensure human is CODEOWNER for sensitive paths (secrets, config, CI)
- **Audit trail:** All agent actions are logged in GitHub's audit log
- **Rate limiting:** Be aware of GitHub API rate limits for agent automation
- **Dismiss stale reviews:** Enabled, so agents can't approve then push more code to bypass review

#### Anti-Patterns to Avoid

- ❌ Giving agents Admin access "for convenience"
- ❌ Agent-only review chains with no human oversight
- ❌ Agents as org owners
- ❌ Shared agent accounts (each agent should have its own identity)
- ❌ Agents managing team membership (keep this human-controlled)
- ❌ Bypassing branch protection for agent speed
- ❌ Secret teams for agents (makes auditing harder)

---

## Summary: Recommended Configuration for zookooree

### Immediate Actions

1. **Org base permission:** Read
2. **Team visibility:** All visible
3. **Team structure:** Flat (4 teams, no nesting needed yet)
4. **Maintainers:** earth2travis on all teams
5. **Agent roles:** Member (not Maintainer) on assigned teams
6. **Branch protection:** Require 1 review, dismiss stale, require CODEOWNERS

### Team Permission Matrix

| Team | earth2travis | agent-sivart | agent-koda |
|------|-------------|-------------|-----------|
| Operations | Maintainer | Member | Member |
| Marketing | Maintainer | Member | - |
| Finance | Maintainer | Member | - |
| Product | Maintainer | Member | Member |

### Repo Access Pattern

| Repo Type | Operations | Marketing | Finance | Product |
|-----------|-----------|-----------|---------|---------|
| Infrastructure | Write | Read | Read | Read |
| Marketing site | Read | Write | Read | Read |
| Financial data | Read | Read | Write | Read |
| Product code | Read | Read | Read | Write |
| Shared/org-wide | Write | Write | Write | Write |

### CODEOWNERS Strategy

- Every repo gets a CODEOWNERS file
- Default owner: `@zookooree/operations` (catch-all)
- Path-specific owners for team domains
- earth2travis as individual owner on: `.github/`, security-sensitive files, deployment configs

---

*Research compiled 2026-03-22. Sources: GitHub official documentation, community best practices.*
