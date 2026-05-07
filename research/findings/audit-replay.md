---
title: Audit Replay for AI Agents
tags:
- agents
- audit
- provenance
- observability
- compliance
related:
- agent-native-operations
- decision-provenance
- proof-of-work
- rag-vs-wiki
- agent-provenance-graph
source: research/raw/audit-replay.md
---




# Audit Replay for AI Agents

_Research document for building best-in-class accountability infrastructure._

## The Problem

An autonomous agent reads email, manages calendars, writes code, sends messages, makes decisions. When something goes wrong, or when you want to understand what happened, you need the full chain: what the agent saw, decided, did, and why.

Currently we have pieces. Session transcripts in JSONL. Daily memory notes. Decision logs. Git history. Cron job outputs. But these are scattered artifacts, not a unified replay system. "What did Sivart do last Tuesday at 3pm?" requires manually correlating five data sources. That is not accountability. That is archaeology.

## What "Replay" Means Practically

### Trace Visualization
See what happened in order. A timeline of events with enough detail to follow the narrative. For a personal agent: message received → context loaded → tools called → response generated → side effects executed.

### State Reconstruction
Given a point in time, rebuild the complete state the agent operated in. What files existed? What was in MEMORY.md? What tools were available? Event sourcing is the relevant pattern: capture every state change as an immutable event, replay events up to any timestamp.

### Counterfactual Analysis
"What would have happened if X were different?" Change the prompt. Swap the model. Remove a piece of context. Replay with modified input and observe output changes. Aspirational for now, but the data model should not preclude it.

## State of the Art in LLMOps Observability

**LangSmith** (LangChain): Tracing integrated with LangChain framework. Every chain, agent step, and tool call becomes a node in a run tree. Supports tagging runs by feature, dataset, or cohort.

**Helicone** (YC W23, open source): Proxy approach. Route LLM API calls through Helicone endpoint; captures everything transparently. "Sessions" feature tracks user journeys across multiple interactions.

**Braintrust:** Bridges observability and evaluation. Production traces become eval cases with one click. Key insight: audit data and evaluation data are the same data viewed through different lenses.

**What these platforms miss:** Memory state at decision time, file system changes and their relationship to decisions, cross-session continuity, human side of interaction, environmental context. The LLM call is only one layer.

## Event Sourcing for AI Agents

**Append-only event log.** Every action, input, and decision recorded as an immutable event. Never modify past events; append compensating events.

**Projections.** Views of the event stream materialized for specific purposes: session timeline, tool usage, decision audit.

**Snapshots.** Periodic captures of derived state to avoid replaying entire history.

### Current Sources (Already Capturing Events)

| Source | Event Types | Format |
|--------|-------------|--------|
| OpenClaw session JSONL | Messages, tool calls, responses | JSONL per session |
| Git history | File changes, commits | Git objects |
| Memory files | State snapshots | Markdown |
| Decision logs | Decision events with reasoning | Markdown |
| Cron job logs | Scheduled task execution | journalctl / log files |
| Heartbeat state | Periodic check results | JSON |

The missing piece: a unified event schema that can represent all of these as entries in a single append-only log.

## Data Model for Audit Events

Every event should conform to a common schema:

```json
{
  "id": "uuid",
  "timestamp": "ISO 8601",
  "session_id": "openclaw session id",
  "event_type": "message | tool_call | tool_result | decision | memory_update | file_change | cron_execution | heartbeat | error | system",
  "source": "openclaw | git | cron | heartbeat | manual",
  "actor": "sivart | user | system | cron",
  "payload": {},
  "context": {
    "memory_hash": "sha256 of MEMORY.md",
    "active_files": [],
    "model": "anthropic/claude-sonnet-4-20250514"
  },
  "parent_id": "uuid of parent event",
  "correlation_id": "shared ID across sessions",
  "tags": []
}
```

## Compliance and Accountability

**EU AI Act (effective August 2025):** High-risk systems must maintain operation logs. While a personal agent is not "high-risk," the logging requirements represent regulatory direction.

**NIST AI Risk Management Framework:** Calls for continuous monitoring and anomaly detection. Emphasizes transparent and explainable AI systems.

**ISO/IEC 42001:** First international standard for AI management. Requires documented audit trails and performance evaluation.

**OpenAI Governance Framework:** "Accountability requires auditability." If operations cannot be audited, they cannot be governed.

## Concrete Recommendations

### Phase 1: Foundation (Now)
- Define unified event log format (JSON schema above)
- Write events to daily JSONL files
- Build session post-processor that reads OpenClaw JSONL, enriches with context metadata, appends to unified log
- Add git hook for MEMORY.md changes

### Phase 2: Querying (Weeks 2-4)
- Import JSONL events into SQLite with indexes
- Build CLI query tool for common questions
- Extend daily audit to query event log for anomalies

### Phase 3: Visualization (Month 2)
- Grafana dashboards for activity overview, decision frequency, tool usage, error rates
- Session replay view: interactive timeline per session

### Phase 4: Full Replay (Month 3+)
- State reconstruction from timestamp
- Counterfactual tooling
- Integrity verification via hash chain

### Architecture Principles
1. **Local first.** All data stays on our server.
2. **Append only.** Events never modified after creation.
3. **Progressive enrichment.** Start basic, add context over time.
4. **Human readable.** JSONL files are grep-friendly; SQLite is query-friendly.
5. **Privacy by design.** Sensitivity classification at event creation; encrypted payloads for sensitive data.
6. **Low overhead.** Capture synchronously, process asynchronously.

## What We Already Have

Session-based workflow, daily notes, decision logs, handoff documents, and git discipline already capture most of what matters. The recommendation is not to replace these but to unify them into a queryable, replayable stream. The daily report voice, handoff format, and decision log structure are the agent's narrative of its own operation. The unified event log adds the structured, machine-queryable layer underneath without losing the human-readable layer on top.
