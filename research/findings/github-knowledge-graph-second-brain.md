---
title: GitHub usage, knowledge graphs, and second brain (repo synthesis)
tags:
  - research
  - github
  - knowledge-graph
  - process
  - memory
related:
  - [[2026-02-10-ai-career-convergence]]
  - [[actual-occasions]]
  - [[alfred-north-whitehead]]
  - [[api-first-interfaces]]
source: research/raw/github-knowledge-graph-second-brain.md
---

# GitHub usage, knowledge graphs, and second brain

This file collects ideas that already live in this repository about **how GitHub is used**, how that connects to **knowledge graphs** and **institutional memory**, and adjacent **second brain** framing. It is a map to primary sources, not a replacement for them.

---

## 1. GitHub as the operating system for work

### 1.1 Strategic goal: mastery of Issues and Projects

`GOALS.md` states that mastering GitHub Issues and Projects is foundational. Operating principles called out there:

- **Issues are memory:** every task documented; comments are the log; read the issue before work; create an issue if none exists.
- **Labels, projects, assignments** should happen automatically, every time.
- **Comments are the heartbeat:** work start, decisions, and changes get commented; the issue is the single source of truth.
- **Projects v2:** custom fields, views, workflows, automation, continuous improvement as a discipline.

Success criterion: when someone asks for status of X, the answer is always in GitHub, not in someone's head.

### 1.2 Process and flow (patterns)

**`patterns/our-flow-map.md`** models work as:

`Signal → Capture (GitHub issue) → Backlog (Todo) → In Progress → Done → Integrated (PR merged)`.

Capture friction is called out: "Issue First" is sometimes skipped in the moment.

**`patterns/flow-management.md`** ties visible work to **GitHub Issues + Project Board**, WIP to context window and items in "In Progress", and flow measurement to issue open-to-closed time.

### 1.3 Agent operating rules

**`AGENTS.md`** and **`CLAUDE.md`** encode GitHub-centric workflow: issue first, branch from default branch, conventional commits, Prettier, PR per logical unit, templates, CI, automatic confirmation in responses (issue, files, commit, PR). Sub-agent rules stress writing to the repo on feature branches instead of temp space.

### 1.4 Practical skill surface

**`skills/github-issues/SKILL.md`** documents repos (sivart, the-agent-factory, moltch), **Framing (#6)** as default project for new issues, **Operations (#7)** for infra, **Foundation (#4)** as closing out, label notes (`experiment`, `idea`), and `gh` oriented workflows.

---

## 2. GitHub as memory and as an institutional knowledge graph

### 2.1 Core thesis and protocol

**`research/project-management/github-as-memory.md`** (#432, 2026-03-31) is the flagship document. Summary of its claims:

- **Thesis:** GitHub Issues are not only a task tracker; they are **nodes in an institutional knowledge graph**. Issues hold decisions and context; the commit log is a timeline; PRs narrate change; comments preserve reasoning.
- **Audit:** twenty recent issues scored ~2.96/5 on memory quality; gaps in labels, closure comments, cross-references, and linking research to decisions.
- **Mindset:** teams that use GitHub as memory write issues **for the reader six months later**, not only for the person doing the work today.
- **GitHub Memory Protocol** (conventions): rich issue bodies, mandatory cross-references ("Related" section), closure protocol (outcome, artifacts, lessons, PR link), label hygiene, optional **knowledge issues** (decisions, learnings, patterns), search-oriented titles, optional Discussions for architecture, monthly health checks.
- **Loomrunner link:** issue quality is framed as **data quality for the knowledge graph** agents will consume; better issues improve downstream agent performance.

### 2.2 Decision record: automation and governance

**`decisions/2026-02-04-github-best-practices.md`** (#86, #87): GitHub Flow, conventional commits, squash merge, CI (commitlint, Prettier, PR size), templates, auto-labeling, stale bot, PR title validation, branch protection (CODEOWNERS, checks, up to date, no force push). References **`research/github-practices/overview.md`** for full rationale; that path was **not present** in the repo at the time of this synthesis (only other `overview.md` files exist under `research/`). Treat the decision file and **`research/engineering/open-source-best-practices.md`** (GitHub community standards, templates, branch protection, SemVer, stale issues, iteration plans) as the surviving detailed pointers.

### 2.3 Agent-native PM and GitHub limits

**`research/project-management/custom-tooling-opportunities.md`** (#302) argues GitHub does not model **session context**, **process compliance for an AI agent**, **capacity/WIP** beyond basic charts, **research discoverability**, or a unified **decision primitive**. Proposed mitigations include session briefing scripts, process audits, capacity reports, research index generation, and decision logs with backlinks to issues.

Design principles there reinforce **writing everything down**, **structured data** (frontmatter, project fields), and **short feedback loops** for an AI PM.

---

## 3. Living project graph, observation, and second brain language

### 3.1 Living project graph

**`research/project-management/living-project-graph.md`** defines a **living project graph**: entities (tasks, decisions, people, code, conversations) as nodes; relationships as edges; the graph updates by **observing** work, not only by manual status updates.

**Intellectual lineage** explicitly includes:

- **Knowledge graphs** (Google, 2012): entities and typed relationships, "things not strings."
- **Event sourcing:** history and causality, not only current state.
- **Distributed tracing:** causality chains across a "distributed system" of project work.
- **Digital twins:** real-time mirror; **sensors** include GitHub (PRs, commits, reviews, deploys).
- **Zettelkasten / tools for thought (Roam, Obsidian):** atomic notes, backlinks, **second brain** style emergence of structure.

**Partial implementations:** Linear, Notion, **GitHub Projects** (native to code, automation; gap: siloed from conversations and full decision trail), Backstage, Roam/Obsidian, bolt-on AI features.

**Synthweave opportunity** called out: Meet transcripts, Slack, **GitHub Projects** as integration points; meetings as graph inputs; weekly planning fed by graph state.

### 3.2 Obsidian, wiki-links, and emergent graphs in the repo

**`decisions/2026-02-17-obsidian-native-workspace.md`** (#222): adopt frontmatter and **`[[wiki-links]]`** so the workspace is Obsidian-friendly; **ClawVault research (#217)** is cited for the idea that wiki-links yield an **emergent knowledge graph** when entities are linked consistently. Outcome includes **visual graph in Obsidian** and backlinks.

### 3.3 "Second brain" phrasing elsewhere

- **`research/project-management/ai-native-pm-operating-system.md`:** interview notes describe MCP-connected Confluence + Figma workflows as a **second brain** for gap analysis (external quote, not a definition of GitHub itself).
- **Telegram exports** under `exports/telegram/` echo graph and Rowboat themes; the **canonical, versioned** treatment remains the markdown research and decisions above, not HTML exports.

---

## 4. Knowledge graph technology in memory and agent research

These files discuss **knowledge graphs** in product or architecture sense, sometimes adjacent to GitHub:

| Topic                                                                                          | Where                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Rowboat: markdown + folders + LLM extraction + `[[backlinks]]`; graph not novel vs integration | `research/tools/rowboat-analysis.md`                                                                                                                                                       |
| ClawVault / Obsidian-style memory and graph layer                                              | `research/tools/clawvault-deep-dive.md`, `research/memory-architecture/memory-is-context-not-storage-obsidian-analysis.md`, gap analysis notes under `research/memory-architecture/notes/` |
| Temporal / bi-temporal graphs, Graphiti, Zep paper                                             | `research/process/decision-provenance.md`                                                                                                                                                  |
| MemPalace SQLite triple store                                                                  | `research/agents/mempalace-analysis.md`, `insights/mempalace-spatial-scoping-for-context-stack.md`                                                                                         |
| Hyperstack "cards" as typed graph                                                              | `research/agents/hyperstack-evaluation.md`                                                                                                                                                 |
| Loom: `manage_reference_links`, knowledge graph language                                       | `research/loom/OVERVIEW.md`                                                                                                                                                                |

**`research/memory-architecture/memory-is-context-not-storage-obsidian-analysis.md`** contrasts a **knowledge graph** layer (linked atomic notes, semantic search via MCP) with flatter monolithic files; includes the line that **a knowledge graph is an agent's library** (also in `research/memory-architecture/notes/agents-need-writing-for-the-same-reason-humans-do.md`).

---

## 5. GitHub in agent orchestration specs

**`research/symphony/SPEC-github-claude.md`:** Symphony-style service adapted from OpenAI's Symphony spec, with **GitHub Issues** and optional **GitHub Projects v2** as the tracker, **Claude Code** as the worker, **`WORKFLOW.md`** as versioned policy, per-issue workspaces, polling, reconciliation, and agent-side writes via **`gh`** / API. Treats the tracker as the **authoritative work queue** and stresses boundaries (orchestrator reads; agent mutates tickets as configured).

---

## 6. Miscellaneous repo references

- **Email triage → GitHub:** `research/operations/email-management.md` maps GTD-style handling to creating issues.
- **Incidents → issues:** `guides/incident-report-guide.md` corrective actions beyond immediate fix become GitHub issues on Foundation.
- **New project checklist:** `guides/new-project-guide.md` includes GitHub project setup steps.
- **NVIDIA Nemoguard:** `research/agents/nvidia-nemoguard-analysis.md` discusses read vs write GitHub API boundaries for agents.
- **Intercom plugin sketch:** `research/claude-code/intercom-plugin-architecture.md` session gaps → GitHub issues feedback loop.
- **Reports:** `reports/2026-03-11.md` states **GitHub is the memory** and ties that to issue closure integrity and `CONTRIBUTING.md`.

---

## 7. Source index (primary)

1. `GOALS.md` — GitHub mastery goal, issues as memory, comments as heartbeat.
2. `AGENTS.md`, `CLAUDE.md` — issue-first, branches, PRs, confirmation discipline.
3. `patterns/our-flow-map.md`, `patterns/flow-management.md` — flow and visibility via GitHub.
4. `skills/github-issues/SKILL.md` — projects, labels, `gh` commands.
5. `research/project-management/github-as-memory.md` — thesis, audit, GitHub Memory Protocol, Loomrunner.
6. `decisions/2026-02-04-github-best-practices.md` — automation and branch protection.
7. `research/engineering/open-source-best-practices.md` — GitHub practices in broader OSS context.
8. `research/project-management/custom-tooling-opportunities.md` — agent-native PM gaps and scripts.
9. `research/project-management/living-project-graph.md` — graph vision, lineage, GitHub as partial implementation.
10. `decisions/2026-02-17-obsidian-native-workspace.md` — wiki-links and emergent graph in-repo.
11. `research/symphony/SPEC-github-claude.md` — automated issue-driven coding agent harness.
12. `research/tools/rowboat-analysis.md`, `research/process/decision-provenance.md`, `research/memory-architecture/*` — knowledge graph and memory architecture angles.

---

_Synthesis compiled from repository contents on 2026-04-11. Update primary sources first, then refresh this index when the story changes._
