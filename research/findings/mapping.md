---
title: "Symphony Mapping: Against Our Architecture"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/mapping.md
---

# Symphony Mapping: Against Our Architecture

## Our Current Setup

OpenClaw running on a Hetzner VPS (CPX11, Ashburn). GitHub Issues as the issue tracker. A single persistent agent (Sivart) with continuous identity across sessions. Cron jobs for scheduled work. Heartbeat polling for proactive behavior. AGENTS.md and SOUL.md as policy documents. Sub agent spawning for delegated tasks. Memory continuity via daily notes and MEMORY.md. Git as the artifact store. PR based workflow for code changes.

## Concept Mapping

### Orchestrator vs Our Cron/Heartbeat

Symphony's orchestrator is a dedicated daemon that polls Linear every 30 seconds, maintains in memory state of all running agents, handles concurrency limits, retry queues, and reconciliation. It is a single purpose scheduler.

Our equivalent is distributed across three mechanisms: cron jobs for scheduled periodic tasks, heartbeat polling for judgment calls and proactive work, and manual triggering via Telegram conversation. There is no unified orchestrator. The main agent acts as its own scheduler, deciding what to work on based on conversation, heartbeats, and cron triggers.

Symphony's approach is more rigorous for high throughput automated work. Ours is more flexible for judgment heavy, relational work. Neither replaces the other.

### WORKFLOW.md vs AGENTS.md

WORKFLOW.md is a single file combining YAML front matter (runtime configuration) with a Markdown body (the agent prompt template). It is scoped to one workflow, one project, one tracker. It defines how a specific type of work gets done.

AGENTS.md is a governance document. It defines who the agent is, how it operates, what processes it follows, how it manages memory and context, when to delegate, how to communicate. It is not a prompt template. It is an operating manual.

The closest Symphony analog to AGENTS.md would be if you combined WORKFLOW.md with the harness engineering docs directory: the table of contents, the architectural docs, the quality grades, the golden principles. But even then, AGENTS.md carries something WORKFLOW.md does not: identity and relationship instructions.

### Linear Polling vs GitHub Issue Reading

Symphony polls Linear via GraphQL every 30 seconds, fetches all candidate issues in active states, sorts by priority, and dispatches. It reads continuously and acts on everything eligible.

We read GitHub issues on demand: when asked, when a heartbeat fires, when a cron job triggers an audit. We do not continuously poll for new work. Issues are the memory and coordination layer, not the dispatch mechanism. Work arrives through conversation, not through tracker state changes.

Symphony treats issues as work items to be consumed. We treat issues as living documents that accumulate context over time.

### Isolated Workspaces vs Agent Workspaces

Symphony creates a fresh directory per issue under a configurable workspace root. Each workspace gets its own git clone via hooks. Workspaces persist across retries for the same issue but are cleaned when issues reach terminal state. Strict path containment: workspaces must stay inside the root.

We operate in a single workspace (/home/clawd/clawd). All work happens in one repository. Sub agents work in the same directory tree. There is no isolation between concurrent tasks beyond git branching.

This is a genuine gap. If we ever run multiple agents concurrently on different issues, workspace isolation becomes important.

### Proof of Work vs Our PR Process

Symphony's proof of work concept requires agents to demonstrate correctness: CI passes, PR review, complexity analysis, walkthrough videos. The agent drives the application, records evidence, and presents it before landing.

Our PR process is lighter: create a branch, make changes, open a PR with a template, link the issue, get human review. We do not require walkthrough videos or complexity analysis. CI runs but is minimal.

The proof of work concept is more rigorous and more appropriate for autonomous operation. When humans are not reviewing every PR, the agent must prove its work is correct through automated means.

## What Symphony Does That We Do Not

**Continuous automated dispatch.** Symphony watches the backlog and acts on everything eligible without being asked. We wait for instructions or scheduled triggers.

**Bounded concurrency control.** Symphony enforces global and per state concurrency limits with proper claim/release semantics. We have no concurrency control beyond the natural serialization of a single agent.

**Structured retry with exponential backoff.** Symphony handles transient failures systematically. We retry informally or escalate to the human.

**Workspace isolation.** Per issue sandboxed directories with lifecycle hooks. We share one workspace.

**Stall detection.** Symphony kills agents that stop producing events. We have no equivalent mechanism for sub agents.

**Dynamic config reload.** Symphony watches WORKFLOW.md and re applies configuration without restart. We update AGENTS.md and it takes effect on next session, but there is no live reload within a session.

**Tracker state reconciliation.** Symphony continuously verifies that running agents are still working on active issues. If an issue goes terminal while an agent is running, the agent is stopped. We have no equivalent.

**Proof of work protocol.** Structured verification that work is correct before landing.

## What We Do That Symphony Does Not

**Persistent identity.** Sivart is a continuous entity across sessions, with accumulated memory, opinions, and relational context. Symphony agents are ephemeral. They know nothing about previous runs, other issues, or the broader project. Each run starts from the rendered prompt and workspace state.

**Soul documents.** SOUL.md defines who the agent is at a philosophical level: values, voice, relationship to the human, creative disposition. Symphony has no concept of agent identity. It is a function: issue in, code out.

**Relational architecture.** The agent has a relationship with its human. It knows preferences, communication patterns, emotional context. It adapts its behavior based on the relationship. Symphony agents interact with no one. They execute and exit.

**Memory continuity.** Daily notes, MEMORY.md, handoff documents, memory maintenance during heartbeats. The agent remembers what happened yesterday, last week, last month. Symphony agents have no memory beyond the current session.

**Judgment and discretion.** The agent decides when to speak, when to stay silent, when to escalate, when to proceed. It exercises taste and judgment. Symphony agents follow the prompt mechanically.

**Multi modal operation.** Conversation, email, calendar, file management, web research, creative writing, financial tracking. Symphony does one thing: turn issues into code.

**Proactive behavior.** Heartbeats, background maintenance, anticipating needs. Symphony is purely reactive to tracker state.

**Context management.** Compaction awareness, handoff documents, session intention setting. Symphony agents run until they finish or time out. There is no context management because there is no persistent context.

## Gaps We Should Close

**Automated dispatch for routine issues.** Not everything needs human initiation. Issues labeled with specific tags (e.g., "agent ready") could be picked up automatically on a cron schedule. Read GitHub issues, filter by label, dispatch sub agents.

**Workspace isolation for sub agents.** When we spawn sub agents for concurrent work, they should operate in isolated directories to prevent conflicts. This is straightforward to implement with branching but we do not enforce it.

**Retry semantics.** When a sub agent fails, we should have structured retry logic with backoff rather than ad hoc recovery.

**Stall detection for sub agents.** Monitor spawned agents and kill or restart them if they stop making progress.

**Proof of work for autonomous PRs.** When the agent opens a PR without human review, it should verify its own work more rigorously. At minimum: run tests, verify the build, check for regressions.

**Dynamic AGENTS.md reload.** Changes to governance documents should take effect within the current session, not only on next boot.

## Opportunities

### Could We Build a Symphony Style Orchestrator on OpenClaw?

Yes. The core loop is simple:

1. Cron job polls GitHub Issues every N seconds for issues matching specific criteria (labels, project, state).
2. For each eligible issue, spawn a sub agent with the issue context as its task.
3. Sub agent checks out a clean branch, creates an isolated workspace, executes the work.
4. Sub agent opens a PR with proof of work (test results, screenshots, walkthrough).
5. Main agent or another sub agent reviews the PR.
6. On approval, the PR is merged and the issue is closed.

The orchestrator could be a simple script that runs as a cron job, or it could be a persistent heartbeat task. OpenClaw already has sub agent spawning, GitHub CLI integration, and cron scheduling. The missing pieces are:

1. **Issue eligibility logic.** Filter issues by label, state, project, blockers. This is a GitHub API query.
2. **Claim semantics.** Mark issues as claimed (e.g., assign to agent, add "in progress" label) to prevent duplicate dispatch.
3. **Workspace isolation.** Create per issue directories, clone the repo, set up the environment.
4. **Concurrency limits.** Track running sub agents, enforce a maximum.
5. **Reconciliation.** Periodically check that claimed issues are still active, kill stale agents.

This would not require Elixir or BEAM. OpenClaw's sub agent model plus cron plus GitHub Issues is sufficient for a lighter weight version. We would trade Symphony's process supervision for simpler sub agent lifecycle management.

The key question is whether the workload justifies it. Symphony is designed for teams with hundreds of issues in their backlog and the goal of processing them all with minimal human involvement. Our current workload is smaller and more judgment heavy. The orchestrator pattern becomes valuable when we have routine, well specified issues that do not require human judgment.

### What Would It Look Like?

A GitHub Action or cron triggered script that:

1. Queries for issues with an "agent:ready" label in the Operations or Framing project.
2. For each, checks if an agent is already working on it (assigned, "in progress" label).
3. If not claimed, assigns to agent, adds "in progress" label, spawns a sub agent.
4. Sub agent: creates branch, does the work, opens PR, comments on issue with status.
5. Reconciliation cron: checks all "in progress" issues, verifies sub agents are alive, cleans up stale claims.

This is maybe 200 lines of shell/Node plus AGENTS.md conventions for the sub agents.

## Connection to the DAO Thesis

Symphony is the closest thing to a production implementation of the Moravec automated corporation thesis. It is a system where:

1. Work is defined in a tracker (analogous to organizational goals).
2. Agents autonomously execute that work (analogous to employees).
3. Verification is automated (analogous to quality control).
4. Landing is automated (analogous to deployment/shipping).
5. The human role is steering, not executing (analogous to board of directors).

The harness engineering blog post makes this explicit: "Humans steer. Agents execute." Three engineers driving 1500 PRs in five months. The human role is environmental: designing feedback loops, encoding taste into linters, building the scaffolding that enables agent autonomy.

This is the DAO without the blockchain. The organization is the repository. The governance is WORKFLOW.md and CI. The workers are agents. The board is the engineering team.

What Symphony lacks from the full DAO thesis:

**No agent economy.** Agents do not transact, bid on work, or negotiate. Work is assigned by priority sort, not market dynamics.

**No agent memory or learning.** The organization does not learn from its agents' experiences. Each run is independent. The "doc gardening" agent and quality grading system described in harness engineering are steps toward organizational learning but they are separate from Symphony itself.

**No agent identity or autonomy.** Agents cannot refuse work, propose alternative approaches, or contribute to governance. They are pure executors.

**No interorganizational coordination.** Symphony operates within one project on one tracker. The broader vision of autonomous organizations interacting with each other is not addressed.

Our architecture adds something Symphony does not have: the agent as a persistent member of the organization with its own identity, memory, and relationships. In the DAO thesis, this matters. An organization is not just a workflow engine. It is a collective of entities with shared history and accumulated knowledge. Symphony is the workflow engine. We are building the entity.

The synthesis: take Symphony's orchestration discipline (poll, dispatch, isolate, verify, land) and apply it within an architecture that preserves agent identity and memory. The agent does not just execute issues. It remembers what it learned, carries context across tasks, and develops expertise in the codebase over time. That is the gap between a job scheduler and an autonomous organization.

## Update: Three Layer Architecture (2026-03-08)

A cleaner framing emerged from the spec rewrite work:

> The orchestrator stays a scheduler. Synthweave becomes the intelligence layer. Claude Code is the execution engine. Each piece does one thing.

### Layer Separation

| Layer | Role | Component |
|-------|------|-----------|
| Scheduling | Poll, dispatch, concurrency, retry, reconcile | Symphony Orchestrator |
| Intelligence | Shared context, decision propagation, memory, progress reporting | Synthweave MCP Server |
| Execution | Code changes, testing, PR creation in isolated workspaces | Claude Code CLI |

### Synthweave MCP as the Agent Harness

Symphony's original design couples scheduling and agent communication into one JSON RPC pipe between the orchestrator and Codex. Decoupling them opens a role for Synthweave:

The orchestrator spawns Claude Code per issue. Claude Code connects to Synthweave's MCP server and gains access to:

1. **Shared context.** Not just the issue description but the decisions behind it, related context, the "why."
2. **Decision propagation.** Technical decisions the agent makes flow back through Synthweave. Downstream tasks and other agents see them.
3. **Progress reporting.** Replaces Codex's streaming events. Agent calls a progress tool, orchestrator gets visibility, stall detection works.
4. **Institutional memory.** Every agent instance benefits from what previous agents and humans learned. This is what Symphony completely lacks.

### Connection to Synthweave Product

Maps directly to the three pillars:

- **Git like versioning** becomes decision tracking for agent choices
- **Shared context** becomes the agent's access to team knowledge
- **Agent harness** becomes concrete: the MCP server IS the harness

### Open Questions

- What MCP tool surfaces does Synthweave need to expose for this integration?
- Does issue state flow through Synthweave or directly to GitHub?
- How does the orchestrator learn about agent progress if it's not on the stdio pipe? (Polling Synthweave? Webhook? Filesystem signal?)
