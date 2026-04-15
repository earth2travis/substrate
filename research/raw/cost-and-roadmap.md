## 4. Cost Projections

### Base Cost: Team Plan at $4/user/month

| Phase | Members | Seats | Monthly Cost | Annual Cost |
|-------|---------|-------|-------------|-------------|
| **Launch** | earth2travis, agent-sivart, agent-koda | 3 | $12 | $144 |
| **Growth (3-6 months)** | +2 specialist agents | 5 | $20 | $240 |
| **Scale (6-12 months)** | +3 more agents | 8 | $32 | $384 |
| **Full Factory (12+ months)** | +4 more agents | 12 | $48 | $576 |

### Additional Costs to Consider

| Item | Cost | When |
|------|------|------|
| Actions minutes overage | $0.008/min (Linux) | If exceeding 3,000 min/month |
| Packages storage overage | $0.25/GB/month | If exceeding 2 GB |
| Secret Protection add-on | $19/active committer/month | When handling sensitive credentials |
| Code Security add-on | $30/active committer/month | When code quality is critical |
| Larger runners | $0.008-$0.064/min | For compute-heavy CI jobs |
| Codespaces (org-paid) | $0.18/core-hour + $0.07/GB/month | If using cloud dev environments |

### Projected Monthly Costs by Phase

| Phase | Base | Extras (est.) | Total |
|-------|------|---------------|-------|
| Launch (3 seats) | $12 | $0 (self-hosted runner) | $12 |
| Growth (5 seats) | $20 | $5 (storage overage) | $25 |
| Scale (8 seats) | $32 | $10 (storage + minutes) | $42 |
| Full + Security (12 seats) | $48 | $228 (Secret Protection for 12) | $276 |

**Key cost insight:** The Team plan itself is extremely affordable. The expensive add-ons (Advanced Security) are where costs jump. Delay those until genuinely needed.

### Self-hosted Runner: The Budget Hack

Running a self-hosted Actions runner on your existing Hetzner server:
- **Cost:** $0 additional (server already paid for)
- **Benefit:** Unlimited Actions minutes
- **Setup:** Install the runner agent, register with org
- **Caveat:** Shares resources with other workloads on the server

This single optimization effectively makes the 3,000-minute limit irrelevant.

---

## 5. Implementation Roadmap

### Week 1: Foundation
- [ ] Create org `zookooree` on Team plan
- [ ] Invite earth2travis, agent-sivart, agent-koda
- [ ] Create teams: founders, agents, engineering, reviewers
- [ ] Create repos: the-agent-factory, infrastructure
- [ ] Enable Discussions on the-agent-factory with category structure
- [ ] Create org-level GitHub Project

### Week 2: Governance
- [ ] Set up repository rulesets on the-agent-factory (main branch protection)
- [ ] Create CODEOWNERS files
- [ ] Configure required reviewers (2 for main repo, 1 for workspaces)
- [ ] Enable Dependabot alerts on all repos
- [ ] Set up push rules (block credential file extensions)

### Week 3: Automation
- [ ] Set up self-hosted Actions runner on Hetzner server
- [ ] Create CI workflow templates in infrastructure repo
- [ ] Configure environment deployments (staging auto, production manual)
- [ ] Set up scheduled workflows for agent reporting
- [ ] Create cross-repo dispatch patterns

### Week 4: Knowledge & Polish
- [ ] Enable wikis on key repos, seed with initial documentation
- [ ] Set up zookooree.github.io for public presence
- [ ] Configure team review assignment (round-robin)
- [ ] Create agent onboarding template/checklist
- [ ] Document all conventions in the-agent-factory README

---

## Summary: Why Team Plan is Perfect for an Agent Factory

The GitHub Team plan at $4/user/month is the sweet spot for an agentic organization because:

1. **CODEOWNERS + required reviewers** = automated governance. Agents get reviewed by the right entities automatically.
2. **Repository rulesets** = layered, transparent rules. Agents can read the rules that apply to them.
3. **Discussions** = async communication native to the platform. No context switching.
4. **Projects** = task management via API. Agents can self-manage work items.
5. **Actions** = automation backbone. With a self-hosted runner, effectively unlimited.
6. **Wikis + Pages** = knowledge publication. Org memory lives where the code lives.
7. **Per-seat pricing** = scales linearly. Adding an agent costs $4/month, not $4,000.

The Team plan provides enterprise-grade governance (review requirements, CODEOWNERS, rulesets, environment protections) at startup pricing. The only features you miss compared to Enterprise are SAML SSO, org-wide rulesets, and audit log streaming, none of which are critical for a small agent factory.

**Bottom line:** At $12/month for 3 seats with a self-hosted runner, you get a fully governed, automated, API-accessible organizational platform. That's less than a single ChatGPT Plus subscription.

---
