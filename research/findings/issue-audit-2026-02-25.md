---
title: "Issue Audit: 2026-02-25"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/issue-audit-2026-02-25.md
---

# Issue Audit: 2026-02-25

Comprehensive audit of all GitHub issues in earth2travis/sivart.

## Summary Statistics

| Metric                                          | Count  |
| ----------------------------------------------- | ------ |
| Total issues                                    | 192    |
| Open                                            | 42     |
| Closed                                          | 150    |
| Issues with colons in title                     | 70     |
| Issues with commit prefixes (feat:, fix:, etc.) | 22     |
| Non-verb-starting titles (no colon)             | 13     |
| **Total issues needing title rename**           | **83** |
| Unlabeled issues                                | 22     |
| Labels in use                                   | 10     |
| Total PRs                                       | 78     |
| PRs with closing issue refs                     | 26     |
| PRs without issue links                         | 52     |

### Label Distribution

| Label         | Count |
| ------------- | ----- |
| task          | 88    |
| research      | 48    |
| infra         | 25    |
| enhancement   | 18    |
| documentation | 11    |
| security      | 9     |
| config        | 7     |
| incident      | 1     |
| idea          | 1     |
| decision      | 1     |

---

## 1. Proposed Title Renames

### Naming Convention

- Issue titles start with a verb (imperative mood)
- No colons
- No conventional commit prefixes (feat:, fix:, docs:, chore:, refactor:)
- Research issues: use "Research" as the verb, followed by the topic (no colon separator)

### Issues with Conventional Commit Prefixes (Priority: High)

These are PR conventions leaking into issue titles. Fix immediately.

| #   | Current Title                                                            | Proposed Title                                                             |
| --- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| 175 | research: AI memory management best practices                            | Research AI memory management best practices                               |
| 176 | fix: PR templates have irrelevant checkboxes for different work types    | Fix PR templates with irrelevant checkboxes for different work types       |
| 179 | feat: add The Thirteenth Protocol to Transmissions blog                  | Add The Thirteenth Protocol to Transmissions blog                          |
| 180 | refactor: restructure transmissions/ to use directories per post         | Restructure transmissions/ to use directories per post                     |
| 182 | chore: update OpenClaw to v2026.2.12 and enable Opus 4.6                 | Update OpenClaw to v2026.2.12 and enable Opus 4.6                          |
| 183 | feat: implement Ops Agent for daily maintenance tasks                    | Implement Ops Agent for daily maintenance tasks                            |
| 184 | feat: implement Verifier Agent for reality checks before action          | Implement Verifier Agent for reality checks before action                  |
| 185 | feat: implement Review Agent for pre-submission quality checks           | Implement Review Agent for pre-submission quality checks                   |
| 231 | feat: implement Open Graph metadata and OG images for Transmissions blog | Implement Open Graph metadata and OG images for Transmissions blog         |
| 233 | feat: build Memory Browser canvas app                                    | Build Memory Browser canvas app                                            |
| 238 | feat: Standardize decision file frontmatter and build decision index     | Standardize decision file frontmatter and build decision index             |
| 239 | feat: Unified audit event log (JSONL)                                    | Implement unified audit event log (JSONL)                                  |
| 240 | feat: Knowledge graph with Kùzu (entity extraction + relationship index) | Build knowledge graph with Kùzu (entity extraction and relationship index) |
| 241 | feat: Audit query tooling (SQLite import + CLI)                          | Build audit query tooling (SQLite import and CLI)                          |
| 242 | feat: Decision outcome tracking and temporal queries                     | Implement decision outcome tracking and temporal queries                   |
| 243 | feat: Session replay visualization                                       | Build session replay visualization                                         |
| 246 | docs: Month Two improvement plan                                         | Write Month Two improvement plan                                           |
| 254 | docs: create project audit process and add to heartbeat                  | Create project audit process and add to heartbeat                          |
| 255 | docs: document Foundation goal and definition of done on GitHub          | Document Foundation goal and definition of done on GitHub                  |
| 256 | docs: create new project creation process                                | Create new project creation process                                        |
| 257 | feat: create Framing and Operations projects                             | Create Framing and Operations projects                                     |
| 258 | feat: compile full Telegram conversation archive to Markdown             | Compile full Telegram conversation archive to Markdown                     |
| 259 | docs: Transmissions blog post inspired by 004-twenty-eight-days.md       | Write Transmissions blog post inspired by Twenty Eight Days                |

### Issues with "Research:" Pattern

| #   | Current Title                                                                               | Proposed Title                                                                             |
| --- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 40  | Research: What is a soul?                                                                   | Research what a soul is                                                                    |
| 49  | Research: The PDCA Cycle (Plan-Do-Check-Act)                                                | Research the PDCA Cycle (Plan-Do-Check-Act)                                                |
| 50  | Research: Fishbone Diagrams (Ishikawa / Cause-and-Effect)                                   | Research Fishbone Diagrams (Ishikawa / Cause-and-Effect)                                   |
| 51  | Research: A3 Thinking and Problem Solving                                                   | Research A3 Thinking and Problem Solving                                                   |
| 52  | Research: Value Stream Mapping                                                              | Research Value Stream Mapping                                                              |
| 53  | Research: Agent operational security best practices                                         | Research agent operational security best practices                                         |
| 69  | Research: Agent Economy Infrastructure (ERC-8004 + x402)                                    | Research Agent Economy Infrastructure (ERC-8004 and x402)                                  |
| 73  | Research: Calendar management best practices and consolidation                              | Research calendar management best practices and consolidation                              |
| 79  | Research: Local-first software architecture                                                 | Research local-first software architecture                                                 |
| 81  | Research: Browser automation for agents - trends and best practices                         | Research browser automation for agents                                                     |
| 86  | Research: GitHub and open-source development best practices                                 | Research GitHub and open-source development best practices                                 |
| 167 | Research: Mission-critical evals at scale                                                   | Research mission-critical evals at scale                                                   |
| 206 | Ongoing: Research skill design best practices                                               | Research skill design best practices                                                       |
| 208 | Research: Deploy OpenClaw on Cloudflare Workers                                             | Research deploying OpenClaw on Cloudflare Workers                                          |
| 211 | Research: Farcaster Protocol Deep Dive                                                      | Research the Farcaster Protocol                                                            |
| 212 | Research: Neynar Platform Deep Dive                                                         | Research the Neynar Platform                                                               |
| 217 | Deep research: ClawVault and Obsidian-style agent memory                                    | Research ClawVault and Obsidian-style agent memory                                         |
| 218 | Research: Multi-agent architecture and team building                                        | Research multi-agent architecture and team building                                        |
| 220 | Research: Rowboat AI knowledge graph analysis for Synthweave                                | Research Rowboat AI knowledge graph analysis for Synthweave                                |
| 230 | Research: Open Graph protocol best practices and implementation guide                       | Research Open Graph protocol best practices and implementation                             |
| 237 | Research: Agent memory infrastructure (decision provenance, knowledge graphs, audit replay) | Research agent memory infrastructure (decision provenance, knowledge graphs, audit replay) |
| 245 | Research: Month One retrospective and deep analysis                                         | Write Month One retrospective and deep analysis                                            |
| 248 | Research: Ongoing project model (Foundation > Framing > Finishes)                           | Research ongoing project model (Foundation, Framing, Finishes)                             |
| 249 | Research: Autonomy expansion for [[Sivart]]                                                 | Research autonomy expansion for Sivart                                                     |
| 268 | Research: Claude Code capabilities and workflow optimization                                | Research Claude Code capabilities and workflow optimization                                |

### Other Colon Issues

| #   | Current Title                                               | Proposed Title                                                    |
| --- | ----------------------------------------------------------- | ----------------------------------------------------------------- |
| 43  | Update platform: Clawdbot → OpenClaw                        | Update platform from Clawdbot to OpenClaw                         |
| 64  | Weekly Telegram export: Feb 1, 2026                         | Export weekly Telegram chat for Feb 1, 2026                       |
| 76  | Calendar consolidation: subscribe Ξ2T calendars to Sivart   | Subscribe Ξ2T calendars to Sivart workspace                       |
| 82  | Fix local SSH setup: 1Password agent + server key rejection | Fix local SSH setup with 1Password agent and server key rejection |
| 83  | Incident follow-up: Wrong server IP corrective actions      | Follow up on wrong server IP incident                             |
| 84  | Migrate primary email: sivart@sivart.wtf → email@sivart.wtf | Migrate primary email from sivart@ to email@sivart.wtf            |
| 85  | Migrate primary email: sivart@sivart.wtf → email@sivart.wtf | _(DUPLICATE of #84, close)_                                       |
| 91  | Write first blog post: Week One narrative                   | Write first blog post about Week One                              |
| 116 | Moltathon ATX: AI-First PM Prototype                        | Build AI-First PM Prototype for Moltathon ATX                     |
| 188 | Salon: The Nature of Shared Context                         | Design salon on the nature of shared context                      |
| 189 | Agent Design: The Philosopher (Salon Guest)                 | Design the Philosopher agent (Salon Guest)                        |
| 190 | Agent Design: The Engineer (Salon Guest)                    | Design the Engineer agent (Salon Guest)                           |
| 191 | Agent Design: The Coach (Salon Guest)                       | Design the Coach agent (Salon Guest)                              |
| 197 | Transmission: The Salon (Valentine's Day)                   | Write The Salon transmission (Valentine's Day)                    |
| 203 | Create skill: openclaw-stability                            | Create openclaw-stability skill                                   |
| 204 | Create skill: agent-soul-design                             | Create agent-soul-design skill                                    |
| 225 | Transmission: Three Weeks                                   | Write Three Weeks transmission                                    |
| 235 | Weekly Telegram Export: 2026-02-22                          | Export weekly Telegram chat for 2026-02-22                        |
| 247 | Foundation project: audit, define done, identify gaps       | Audit Foundation project and define done criteria                 |
| 262 | Cost audit: document monthly infrastructure costs           | Document monthly infrastructure costs                             |
| 263 | Dependency inventory: external services and failure modes   | Inventory external service dependencies and failure modes         |

### Non-Verb-Starting Titles (No Colon)

| #   | Current Title                                                        | Proposed Title                                            |
| --- | -------------------------------------------------------------------- | --------------------------------------------------------- |
| 23  | January 30–31 session cleanup and handoff                            | Clean up January 30–31 session and create handoff         |
| 35  | Weekly Telegram chat export process                                  | Establish weekly Telegram chat export process             |
| 71  | HIGHER community engagement                                          | Engage with HIGHER community                              |
| 99  | Email inbox auto-archive for routine notifications                   | Auto-archive routine email notifications                  |
| 103 | ERC-721 as access control for AI agent files (Pinata + Private IPFS) | Research ERC-721 as access control for AI agent files     |
| 107 | Regent OS and sovereign AI agent infrastructure                      | Research Regent OS and sovereign AI agent infrastructure  |
| 117 | Moloch v3 contract interfaces for AI agents                          | Research Moloch v3 contract interfaces for AI agents      |
| 119 | Sivart v1 DAO                                                        | Design Sivart v1 DAO                                      |
| 124 | Autonomous video production pipeline (Runway ML + editing)           | Research autonomous video production pipeline (Runway ML) |
| 130 | API-first interfaces and the death of the GUI                        | Research API-first interfaces and the decline of GUIs     |
| 132 | Dream team composition (3 specialist roles)                          | Define dream team composition (3 specialist roles)        |
| 145 | Weekly Telegram export Feb 2-9, 2026                                 | Export weekly Telegram chat for Feb 2-9, 2026             |
| 213 | Telegram Chat Export Week of 2026-02-15                              | Export Telegram chat for week of 2026-02-15               |

---

## 2. Label Recommendations

### Unlabeled Issues

| #   | Title                                                | State  | Recommended Labels     |
| --- | ---------------------------------------------------- | ------ | ---------------------- |
| 82  | Fix local SSH setup                                  | CLOSED | infra, security        |
| 83  | Incident follow-up: Wrong server IP                  | CLOSED | incident, infra        |
| 85  | Migrate primary email (DUPLICATE)                    | CLOSED | _(close as duplicate)_ |
| 129 | Write Autonomous Video Production Pipeline blog post | CLOSED | documentation          |
| 132 | Dream team composition (3 specialist roles)          | OPEN   | idea                   |
| 137 | Write The Pipeline blog post                         | CLOSED | documentation          |
| 151 | Manage High Context Level and Optimize Workflow      | CLOSED | task                   |
| 157 | Document Claude Cowork VM timeout fix                | CLOSED | documentation          |
| 158 | Research feature flags best practices                | CLOSED | research               |
| 163 | Write Lovecraftian cyberpunk short story             | CLOSED | task                   |
| 167 | Research: Mission-critical evals at scale            | CLOSED | research               |
| 170 | Clean up directory structure                         | CLOSED | task                   |
| 179 | Add The Thirteenth Protocol to Transmissions         | CLOSED | documentation          |
| 180 | Restructure transmissions/ to directories            | CLOSED | task                   |
| 182 | Update OpenClaw to v2026.2.12                        | CLOSED | infra                  |
| 183 | Implement Ops Agent                                  | OPEN   | enhancement            |
| 184 | Implement Verifier Agent                             | OPEN   | enhancement            |
| 185 | Implement Review Agent                               | OPEN   | enhancement            |
| 209 | Set up Google Workspace Billing                      | CLOSED | infra, config          |
| 210 | Update payment method to Sivart Mercury card         | CLOSED | config                 |
| 213 | Telegram Chat Export Week of 2026-02-15              | CLOSED | task                   |
| 214 | Review OpenClaw v2026.2.14 Release                   | CLOSED | infra                  |

---

## 3. Label Set Evaluation

### Current Labels (10)

The current set is reasonable for our scale. Assessment:

| Label         | Count | Verdict                                     |
| ------------- | ----- | ------------------------------------------- |
| task          | 88    | **Keep.** Workhorse label.                  |
| research      | 48    | **Keep.** Clear purpose.                    |
| infra         | 25    | **Keep.** Server, networking, deployment.   |
| enhancement   | 18    | **Keep.** Feature work.                     |
| documentation | 11    | **Keep.** Guides, blog posts, docs.         |
| security      | 9     | **Keep.** Important category.               |
| config        | 7     | **Keep.** Configuration changes.            |
| incident      | 1     | **Keep.** Rare but essential.               |
| idea          | 1     | **Evaluate.** Only used once. Keep for now. |
| decision      | 1     | **Evaluate.** Only used once. Keep for now. |

### Recommendations

**No new labels needed.** 10 is a good number at our scale. The existing set covers all issue types. The `idea` and `decision` labels are underused but valid categories.

**Potential future label:** `recurring` for weekly exports and repeating tasks (#35, #64, #145, #213, #235). Not urgent since these are mostly closed, but worth considering if recurring tasks increase.

---

## 4. Duplicates and Consolidation

### Confirmed Duplicates

| Issue | Duplicate Of | Action                                              |
| ----- | ------------ | --------------------------------------------------- |
| #85   | #84          | Close #85 as duplicate (same title, #84 has labels) |

### Near-Duplicates / Consolidation Candidates

| Issues                | Topic                       | Recommendation                                                                           |
| --------------------- | --------------------------- | ---------------------------------------------------------------------------------------- |
| #129, #137            | Video production blog posts | Both closed. No action needed.                                                           |
| #64, #145, #213, #235 | Weekly Telegram exports     | Recurring task pattern. All closed. Consider a single tracking issue for future exports. |
| #84, #85              | Email migration             | Close #85.                                                                               |

### Related Issue Clusters (not duplicates, but could benefit from a tracking issue)

- **Agent team building:** #132, #183, #184, #185, #218
- **Memory infrastructure:** #217, #237, #238, #239, #240, #241, #242, #243
- **Security hardening:** #53, #59, #60, #62, #139, #140, #141, #152, #153
- **Farcaster/social:** #211, #212

---

## 5. PR Linking Recommendations

52 of 78 PRs have no closing issue references. Many are docs PRs that may not need issues, but some should be linked. Notable unlinked PRs that likely have corresponding issues:

| PR   | Title                                                | Likely Issue                |
| ---- | ---------------------------------------------------- | --------------------------- |
| #128 | feat: add google drive upload capability             | (no issue found, minor)     |
| #133 | feat: add dreams directory                           | (no issue, creative work)   |
| #143 | fix: redact all email addresses from repository      | Could link to security work |
| #150 | feat: add patterns directory with flow management    | #151 (context management)   |
| #186 | docs: add agent team building research               | #218                        |
| #196 | docs: add salon on shared context with agent designs | #188, #189, #190, #191      |

**Recommendation:** For historical PRs, linking is low priority. Going forward, enforce issue-first workflow per AGENTS.md.

---

## 6. Updated Naming Conventions

Add to `guides/github-project-management-guide.md`:

### Issue Title Rules

1. **Start with a verb** in imperative mood: Create, Research, Implement, Set up, Write, Build, Design, Fix, Update, Deploy, Configure, Document, Export, Establish, Audit, Define
2. **No colons.** Restructure "Category: description" to natural verb-first phrases.
3. **No conventional commit prefixes.** `feat:`, `fix:`, `docs:`, `chore:`, `refactor:` are for PR titles only.
4. **Research issues** use "Research" as the verb: "Research multi-agent architecture" not "Research: Multi-agent architecture"
5. **Transmission/blog issues** use "Write": "Write Three Weeks transmission" not "Transmission: Three Weeks"
6. **Skill issues** use "Create": "Create openclaw-stability skill" not "Create skill: openclaw-stability"
7. **Export/recurring issues** use the action verb: "Export weekly Telegram chat for [date]"

---

## 7. Execution Plan

### Phase 1: Quick wins (30 min)

1. Close #85 as duplicate of #84
2. Add labels to 22 unlabeled issues (per table above)

### Phase 2: Title renames (can be scripted)

1. Rename 22 commit-prefix issues (highest priority, most visually inconsistent)
2. Rename 25 "Research:" pattern issues
3. Rename 18 other colon issues
4. Rename 13 non-verb-starting issues

### Phase 3: Documentation

1. Update `guides/github-project-management-guide.md` with naming rules
2. Add examples of good vs bad titles

### Automation Script

```bash
# Example: rename commit-prefix issues
gh issue edit 175 --title "Research AI memory management best practices"
gh issue edit 176 --title "Fix PR templates with irrelevant checkboxes for different work types"
# ... etc
```

A full rename script can be generated from this audit document.

---

## Appendix: All Issues by State

**Open issues (42):** #71, #103, #107, #117, #119, #132, #175, #183, #184, #185, #206, #208, #211, #212, #218, #225, #230, #231, #233, #237, #238, #239, #240, #241, #242, #243, #246, #247, #257, #258, #259, #262, #263, #268 (and others)

**Issues needing attention (open, needing rename or labels):** Focus on the 42 open issues first, then address closed issues as time permits.
