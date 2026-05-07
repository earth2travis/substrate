---
title: "Symphony Mapping: Against Our Architecture"
source: "research/raw/symphony-mapping.md"
tags: ["symphony", "orchestration", "openclaw", "architecture", "comparison"]
related:
  - "[[agent-native-operations]]"
  - "[[workflow-as-contract]]"
  - "[[agent-platform-ecosystem]]"
  - "[[the-openclaw-lesson]]"
  - "[[loom-overview]]"
  - "[[loom-service-spec]]"
  - "[[gateway-integration]]"
  - "[[agent-orchestrator-pattern]]"
  - "[[proof-of-work]]"
  - "[[workspace-isolation]]"
---

# Symphony Mapping: Against Our Architecture

Concept mapping between Symphony (OpenAI's agent orchestration spec) and our current OpenClaw-based architecture.

## Concept Mapping

### Orchestrator vs Our Cron/Heartbeat

Symphony's orchestrator is a dedicated daemon that polls Linear every 30 seconds. Our equivalent is distributed across cron jobs, heartbeat polling, and manual Telegram triggers. There is no unified orchestrator. The main agent acts as its own scheduler.

Symphony is more rigorous for high throughput automated work. Ours is more flexible for judgment heavy, relational work.

### WORKFLOW.md vs AGENTS.md

WORKFLOW.md is a single file combining YAML front matter (runtime config) with a Markdown body (agent prompt template). It is scoped to one workflow.

AGENTS.md is a governance document. It defines who the agent is, how it operates, what processes it follows. It is not a prompt template. It is an operating manual.

### Isolated Workspaces vs Agent Workspaces

Symphony creates a fresh directory per issue with its own git clone. We operate in a single workspace (/home/clawd/clawd). All work happens in one repository. This is a genuine gap for concurrent agent execution.

### Proof of Work vs Our PR Process

Symphony's proof of work requires agents to demonstrate correctness: CI passes, PR review, complexity analysis, walkthrough videos. Our PR process is lighter: branch, changes, PR template, human review.

## What Symphony Does That We Do Not

- Continuous automated dispatch
- Bounded concurrency control with claim/release
- Structured retry with exponential backoff
- Workspace isolation
- Stall detection
- Dynamic config reload
- Tracker state reconciliation
- Proof of work protocol

## What We Do That Symphony Does Not

- Persistent identity across sessions
- Soul documents (SOUL.md) defining values and voice
- Relational architecture with the human
- Memory continuity (daily notes, MEMORY.md)
- Judgment and discretion
- Multi-modal operation
- Proactive behavior via heartbeats
- Context management and compaction awareness

## Gaps We Should Close

1. Automated dispatch for routine issues (cron + label filtering)
2. Workspace isolation for sub agents (branch-based or directory-based)
3. Structured retry semantics for sub agents
4. Stall detection for sub agents
5. Proof of work for autonomous PRs
6. Dynamic AGENTS.md reload within session

## Connection to the DAO Thesis

Symphony is the closest thing to a production implementation of the Moravec automated corporation thesis. Work is defined in a tracker. Agents autonomously execute. Verification is automated. Landing is automated. The human role is steering, not executing.

What Symphony lacks from the full DAO thesis:
- No agent economy (no transactions, bidding, or negotiation)
- No agent memory or learning (each run is independent)
- No agent identity or autonomy (pure executors)
- No interorganizational coordination

Our architecture adds the agent as a persistent member of the organization with identity, memory, and relationships. The synthesis: take Symphony's orchestration discipline and apply it within an architecture that preserves agent identity and memory. That is the gap between a job scheduler and an autonomous organization.
