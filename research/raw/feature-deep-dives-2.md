**Free vs Team:** CODEOWNERS only works in private repos on Team (or Pro for personal repos). Essential Team unlock.

### 2.9 GitHub Pages (Team unlock for private repos)

**What it does:** Static site hosting from a repository. Supports Jekyll, custom GitHub Actions build pipelines, and custom domains. Sites are public by default; private Pages requires Enterprise Cloud.

**Agentic application:**
- **Public-facing site:** Organization website, agent documentation, reports
- **Knowledge base:** Published documentation from markdown in repos
- **Agent portfolios:** Each agent could have a public page showcasing their work

**Configuration recommendations:**
- Create `zookooree.github.io` repo for org site
- Use GitHub Actions to build and deploy (more flexible than Jekyll)
- Custom domain if desired
- Note: Pages sites are always PUBLIC on Team plan. Private Pages requires Enterprise Cloud.

**Free vs Team:** Free only allows Pages in public repos. Team allows Pages from private repos, but the published site is still public.

### 2.10 Wikis (Team unlock for private repos)

**What it does:** Each repo gets a wiki (separate git repo behind the scenes). Markdown-based, versioned, searchable. Can be edited via web UI or by cloning the wiki repo directly.

**Agentic application:**
- **Organizational knowledge base:** Runbooks, procedures, agent guides
- **API-accessible:** Wikis are git repos, so agents can clone, edit, and push wiki content programmatically
- **Searchable:** Quick reference for operational knowledge

**Configuration recommendations:**
- Enable wiki on `the-agent-factory` for org-wide knowledge
- Consider using wiki for stable reference docs, Discussions for evolving conversations
- Agents can update wiki via git: `git clone https://github.com/zookooree/the-agent-factory.wiki.git`
- Alternative: just use markdown files in the repo (more integrated with PRs and reviews). Wikis bypass PR review.

**Caveat:** Wikis bypass the PR review workflow. For an agent factory that values reviewed changes, keeping docs in the main repo with PR review may be preferable. Use wikis for lightweight, fast-changing reference material.

**Free vs Team:** Wikis only available on private repos with Team plan.

### 2.11 Environment Deployment Branches and Secrets

**What it does:** GitHub Actions environments define deployment targets with protection rules. You can:
- Restrict which branches can deploy to an environment
- Require manual approval before deployment
- Set environment-specific secrets (separate from repo secrets)
- Configure wait timers

**Agentic application:**
- **Production deployment gates:** Require human approval for production deploys
- **Staging auto-deploy:** Agents can auto-deploy to staging, but production needs earth2travis approval
- **Secret isolation:** Each environment gets its own secrets (API keys, tokens). Agents only access secrets for their environment.
- **Branch restrictions:** Only `main` can deploy to production

**Configuration recommendations:**
- Environments: `development` (auto), `staging` (auto), `production` (manual approval)
- Production reviewers: `earth2travis`
- Branch restrictions: production only from `main`
- Store agent API tokens as environment secrets, not repo secrets
- Use environment secrets for service credentials (database, external APIs)

**Free vs Team:** Deployment protection rules for private repos require Team. Environment secrets available on all plans but protection rules gate their use.

### 2.12 Packages Storage (500MB Free → 2GB Team)

**What it does:** GitHub Packages hosts packages (npm, Docker, Maven, NuGet, RubyGems). Storage is shared across the org. Bandwidth and storage billed by plan.

**Agentic application:**
- **Docker images:** Publish agent runtime images to GitHub Container Registry (ghcr.io)
- **Shared libraries:** If agents produce reusable packages, publish them internally
- **Versioned artifacts:** Store build outputs, models, or data packages

**Configuration recommendations:**
- Use ghcr.io for Docker images (agent environments)
- Set up cleanup policies (delete old image tags) to manage 2GB limit
- Consider: 2GB is tight for Docker images. Monitor usage. May need to pay for additional storage or use external registry.

**Free vs Team:** 4x storage increase (500MB → 2GB).

### 2.13 Scheduled Reminders (Team exclusive)

**What it does:** Configure Slack or Microsoft Teams notifications for pending PR reviews, stale PRs, etc. on a schedule.

**Agentic application:** Limited value if agents don't use Slack/Teams. But could:
- Remind earth2travis about pending reviews
- Alert a monitoring channel about stale PRs

**Configuration recommendations:**
- Set up if using Slack/Teams integration
- Otherwise, achieve similar functionality with GitHub Actions scheduled workflows

### 2.14 Security Overview (Team exclusive)

**What it does:** Dashboard showing security alerts across all org repos. Aggregates Dependabot alerts, secret scanning alerts, and code scanning alerts.

**Agentic application:**
- Single view of security posture across all agent repos
- Track which repos have enabled security features
- Monitor for exposed secrets (critical when agents handle API tokens)

**Configuration recommendations:**
- Enable Dependabot alerts on all repos (free)
- Enable secret scanning on all repos (free for public, needs Secret Protection add-on for private)
- Review security overview weekly

### 2.15 GitHub Advanced Security Add-ons

#### Secret Protection ($19/month per active committer)
- Scans for secrets (API keys, tokens) in code and prevents them from being pushed
- Push protection blocks commits containing detected secrets
- Custom patterns for org-specific secrets

#### Code Security ($30/month per active committer)
- CodeQL code scanning (finds vulnerabilities in code)
- Dependency review (blocks PRs that introduce vulnerable dependencies)

**Agentic application:** High value for an agent factory:
- **Secret Protection:** Agents might accidentally commit API tokens. Push protection prevents this.
- **Code Security:** Automated vulnerability detection on agent-written code.

**Cost consideration:** These are per-active-committer. With 3+ agents committing, costs add up:
- Secret Protection: 3 committers × $19 = $57/month
- Code Security: 3 committers × $30 = $90/month
- Both: $147/month for 3 committers

**Recommendation:** Start without these. Use repository rulesets (push rules restricting .env, .key files) and free Dependabot for basic security. Add Secret Protection first if agents start handling sensitive credentials.

### 2.16 Web-based Support (Team)

**What it does:** Email support from GitHub (vs community-only on Free).

**Agentic application:** Useful when hitting platform issues, billing questions, or org configuration problems.

**Free vs Team:** Community support only on Free. Team gets email support.

---

