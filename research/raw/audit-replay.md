# Audit Replay for AI Agents

_Research document for building best in class accountability infrastructure._
_Created: February 23, 2026_

---

## The Problem

An autonomous agent acts on your behalf. It reads your email, manages your calendar, writes code, sends messages, makes decisions. When something goes wrong, or when you simply want to understand what happened, you need to reconstruct the full chain: what the agent saw, what it decided, what it did, and why.

We currently have pieces. Session transcripts in JSONL. Daily memory notes. Decision logs. Git history. Cron job outputs. But these are scattered artifacts, not a unified replay system. Asking "what did Sivart do last Tuesday at 3pm?" requires manually correlating five different data sources. That is not accountability. That is archaeology.

Audit replay means: given any point in time, reconstruct the complete state of the agent, the context it operated in, and the reasoning behind its actions. Not as a forensic exercise after disaster, but as a routine capability built into the system from the ground up.

---

## 1. State of the Art

### LLMOps Observability Platforms

The LLMOps ecosystem has converged on a common pattern: capture every LLM call as a trace with nested spans, store prompts and completions, track cost and latency, enable search and filtering. The implementations vary in depth and focus.

**LangSmith** (LangChain's commercial offering) provides tracing tightly integrated with the LangChain framework. Every chain, agent step, and tool call becomes a node in a run tree. You can inspect the full prompt sent to the model, the raw completion, token counts, and latency at each step. LangSmith supports tagging runs by feature, dataset, or customer cohort, then comparing traces by tag to verify behavioral changes are intentional. The run tree visualization makes loops, stalls, and hot paths visible in the hierarchy. Over 100,000 developers use the platform, making it the de facto standard for LangChain users.

**Helicone** (YC W23, open source) takes a proxy approach: route your LLM API calls through Helicone's endpoint, and it captures everything transparently. Request/response logging, cost tracking, latency monitoring, session grouping for multi step workflows. Their "Sessions" feature tracks user journeys across multiple interactions, which is the closest the observability platforms come to replay. Anomaly detection identifies unusual behavior patterns across sessions.

**Braintrust** bridges observability and evaluation. Production traces become eval cases with one click. This is a key insight: audit data and evaluation data are the same data viewed through different lenses. Braintrust is opinionated about workflows, connecting traces to experiments to pull requests. Their approach treats observability not as passive monitoring but as an active improvement loop.

**Lunary** offers model agnostic tracking with a classification tool called Radar that categorizes LLM responses against predefined criteria for later review. Free tier, Apache 2.0 license.

**Key insight from LakeFS comparison (Dec 2025):** The frontier is versioning the full "execution context" (prompts + RAG inputs + eval artifacts) so every production response is replayable from an immutable reference. Store prompt templates, evaluation datasets, and sampled production traces together. This is the closest anyone has come to true replay: not just logging what happened, but preserving everything needed to reproduce it.

### What These Platforms Miss

Every platform above focuses on LLM call observability. None of them capture the full agent lifecycle:

- Memory state at decision time (what did the agent "know"?)
- File system changes and their relationship to decisions
- Cross session continuity (handoffs, memory updates, MEMORY.md evolution)
- The human side of the interaction (instructions, corrections, context)
- Environmental context (what cron jobs ran, what emails arrived, what calendar events existed)

For a personal agent like Sivart, the LLM call is only one layer. The interesting audit questions are higher: "Why did Sivart decide to send that email?" requires tracing from the trigger (heartbeat check found urgent email) through context assembly (loaded MEMORY.md, read recent messages) through reasoning (decided this was urgent enough to forward) through action (composed and sent the message). No existing platform captures this full chain.

---

## 2. What "Replay" Means Practically

Replay is not a single capability. It is a spectrum of reconstructive power.

### Trace Visualization

The simplest form: see what happened in order. A timeline of events with enough detail to follow the narrative. Every platform above does this for LLM calls. For a personal agent, trace visualization means seeing the full session flow: message received → context loaded → tools called → response generated → side effects executed.

OpenTelemetry's GenAI semantic conventions (still in development status as of early 2026) define the emerging standard. They specify spans for agent operations including `create_agent`, `execute_tool`, and the full invoke lifecycle. Attributes include `gen_ai.agent.id`, `gen_ai.agent.name`, `gen_ai.system_instructions`, and `gen_ai.request.model`. Events capture inputs and outputs. This is the direction the industry is heading: standardized telemetry for AI agents, not just LLM calls.

The OTel GenAI agent span spec references the Kaggle whitepaper on agents, defining an agent as the combination of reasoning, logic, and access to external information connected to a generative AI model. Their semantic conventions extend the base GenAI span conventions with agent specific attributes.

### State Reconstruction

The harder problem: given a point in time, rebuild the complete state the agent operated in. What files existed? What was in MEMORY.md? What was the session history? What tools were available? What was the system prompt?

This is where event sourcing becomes relevant. If every state change is captured as an immutable event, you can replay events up to any timestamp and reconstruct the exact state. Without event sourcing, state reconstruction requires correlating snapshots (git commits, file backups) with timestamps, which is lossy and fragile.

### Counterfactual Analysis

The most powerful form: "What would have happened if X were different?" Change the prompt. Swap the model. Remove a piece of context. Replay with the modified input and observe how the output changes.

Braintrust's "traces to eval cases" feature enables a limited version of this: take a production trace, modify the input, and run it through evaluation. True counterfactual analysis for agents would require capturing enough state to re run the full decision process, not just the LLM call but the tool calls, memory lookups, and environmental inputs.

This is aspirational for now. But the data model we build should not preclude it.

---

## 3. Event Sourcing for AI Agents

Event sourcing is the pattern where state changes are stored as a sequence of immutable events rather than as mutable state. The current state is derived by replaying events from the beginning. This pattern, well established in financial systems and distributed architectures, maps naturally to agent audit.

### Core Principles

**Append only event log.** Every action the agent takes, every input it receives, every decision it makes is recorded as an event. Events are immutable. You never modify or delete past events. If a correction is needed, you append a compensating event.

**Projections.** Views of the event stream materialized for specific purposes. A "session timeline" projection shows events grouped by session. A "tool usage" projection shows all tool calls across sessions. A "decision audit" projection shows only events tagged as decisions with their reasoning. Same underlying data, different lenses.

**Snapshots.** Periodic captures of derived state to avoid replaying the entire event history every time. A daily snapshot of the agent's memory state, for example, means you only need to replay events from the last snapshot forward.

### Applied to Sivart

Our existing infrastructure already captures events, just not in a unified stream:

| Current Source | Event Types | Format |
|---|---|---|
| OpenClaw session JSONL | Messages, tool calls, responses | JSONL files per session |
| Git history | File changes, commits | Git objects |
| Memory files | State snapshots (daily notes, MEMORY.md) | Markdown |
| Decision logs | Decision events with reasoning | Markdown |
| Cron job logs | Scheduled task execution | journalctl / log files |
| Heartbeat state | Periodic check results | JSON |

The missing piece is a unified event schema that can represent all of these as entries in a single append only log, with enough metadata to correlate them across sources.

### Event Sourcing Tradeoffs

The classic event sourcing challenges apply:

**Storage growth.** An append only log grows without bound. For a personal agent, this is manageable: text events are small, and storage is cheap. But media (screenshots, file contents) can bloat quickly. Selective capture and content addressing (store the hash, retrieve the content) help.

**Schema evolution.** Events written today must be readable tomorrow. Versioned schemas with backward compatibility are essential. This is one reason JSON (or JSONL) works well: it is naturally extensible.

**Replay performance.** Replaying millions of events to reconstruct state is slow. Snapshots solve this, but they add complexity. For Sivart's scale (hundreds of events per day, not millions), replay performance is not an immediate concern.

**Eventually consistent projections.** If projections are built asynchronously from the event stream, they may lag behind. For audit purposes, slight lag is acceptable. For real time monitoring, you need the event stream itself.

---

## 4. Observability for Agents

The LLMOps world is converging on a layered observability model that maps to the traditional three pillars (traces, metrics, logs) but with AI specific semantics.

### Traces and Spans

OpenTelemetry's GenAI semantic conventions define the emerging standard:

**Spans** represent operations with a start time, end time, and attributes. For agents, key span types include:
- `gen_ai.chat` / `gen_ai.generate_content`: Model inference calls
- `gen_ai.execute_tool`: Tool execution within an agent loop
- `create_agent`: Agent instantiation (for remote agent services)
- Agent framework spans for workflow steps

**Attributes** capture the semantics: model name, provider, token counts, system instructions, agent ID and name. The `gen_ai.system_instructions` attribute is marked as "opt in" due to privacy concerns, which is relevant to our design.

**Events** capture inputs and outputs: prompt content, completion content, evaluation results. The evaluation event type (`gen_ai.evaluation`) captures quality assessments parented to the operation span being evaluated.

### Metrics

Standard metrics converging across platforms:
- Token usage (input, output, thinking) per model, per session, per task
- Latency (time to first token, total generation time)
- Cost (derived from token counts and pricing)
- Error rates by type
- Tool call frequency and success rates

The OpenTelemetry GenAI metrics spec defines histogram buckets for token usage and duration, making cross platform comparison possible.

### Logs

The unstructured narrative layer. For agents, logs capture what doesn't fit in structured traces: reasoning chains, memory updates, environmental observations. Our daily notes and decision logs are effectively structured logs with rich narrative context.

### The Missing Layer: Agent State

None of the standard observability frameworks capture agent state: the contents of memory, the loaded context, the active goals, the relationship history. This is the layer we need to add. It is not an LLM concern or a tool concern. It is an agent concern, specific to systems that persist across sessions and accumulate context over time.

---

## 5. Compliance and Accountability

### Emerging Standards

**EU AI Act (effective August 2025, enforcement rolling through 2026).** High risk AI systems must maintain logs of operation "to the extent that the logging is within the control of the provider." Article 12 requires automatic recording of events relevant to identifying situations that may result in risk. Logs must enable traceability of the AI system's operation throughout its lifecycle. While a personal agent is not a "high risk" system under the Act's classification, the logging requirements represent the regulatory direction.

**NIST AI Risk Management Framework (AI RMF 1.0, updated 2025).** Calls for continuous monitoring and anomaly detection for AI systems. The 2025 updates integrate with ISO/IEC 42001, SOC2 AI controls, and EU AI Act conformity workflows. The framework emphasizes that AI systems should be "transparent and explainable," which requires audit infrastructure.

**ISO/IEC 42001 (AI Management System).** The first international standard for AI management, requiring organizations to establish, implement, maintain, and continually improve an AI management system. Includes requirements for documented information (read: audit trails) and performance evaluation.

**OpenAI's Governance Framework.** "Accountability requires auditability." If an agent's operations cannot be audited, they cannot be governed. This is not a regulatory requirement but an industry principle that is hardening into expectation.

### What This Means for Sivart

We are not building a regulated system. We are building a personal agent for one human. But the principles matter:

1. **Traceability.** Every action should be traceable to its trigger and reasoning.
2. **Immutability.** Audit records should be tamper resistant (append only, with integrity verification).
3. **Completeness.** The audit trail should capture enough to reconstruct decisions, not just outcomes.
4. **Retention.** Audit data should be retained long enough to be useful (we should define "long enough").
5. **Accessibility.** The human should be able to query and explore audit data without technical barriers.

We hold ourselves to a higher standard than the law requires because we believe accountability is a feature, not a compliance checkbox. Our existing audit framework (quick checks, daily audits, weekly process audits, monthly deep audits) already embodies this. Replay infrastructure makes it operational.

---

## 6. Data Model for Audit Events

### The Unified Event Schema

Every audit event, regardless of source, should conform to a common schema:

```json
{
  "id": "uuid",
  "timestamp": "ISO 8601 with microsecond precision",
  "session_id": "the OpenClaw session ID",
  "event_type": "message | tool_call | tool_result | decision | memory_update | file_change | cron_execution | heartbeat | error | system",
  "source": "openclaw | git | cron | heartbeat | manual",
  "actor": "sivart | user | system | cron",
  "payload": {
    // event type specific data
  },
  "context": {
    "memory_hash": "sha256 of MEMORY.md at event time",
    "active_files": ["list of files in context window"],
    "model": "anthropic/claude-sonnet-4-20250514",
    "thinking_mode": "low | medium | high"
  },
  "parent_id": "uuid of parent event (for span nesting)",
  "correlation_id": "shared ID linking related events across sessions",
  "tags": ["audit", "decision", "external_action"]
}
```

### Event Types in Detail

**message.** Human sends a message to the agent, or agent sends a response. Payload includes the message content, channel (telegram, discord), and any attachments.

**tool_call.** Agent invokes a tool. Payload includes tool name, parameters, and the reasoning that led to the call (if available from the model's thinking).

**tool_result.** Tool returns a result. Payload includes the output (or a reference to it if large), duration, and success/failure status.

**decision.** Agent makes a significant choice. Payload includes the decision, alternatives considered, reasoning, and confidence level. This is a semantic layer on top of the raw tool calls: not every tool call is a decision, but every decision involves tool calls.

**memory_update.** Agent modifies its persistent state (MEMORY.md, daily notes, handoffs). Payload includes the file path, the change (diff), and the reason for the update.

**file_change.** Any file modification in the workspace. Can be correlated with git commits. Payload includes path, operation (create, modify, delete), and content hash.

**cron_execution.** A scheduled task runs. Payload includes the cron job ID, command, output summary, and exit status.

**heartbeat.** Periodic health check. Payload includes what was checked and what was found.

**error.** Something went wrong. Payload includes error type, message, stack trace (if applicable), and recovery action taken.

**system.** Infrastructure events: service restarts, config changes, auth token rotations.

### Retention and Immutability

**Retention tiers:**
- Hot (0 to 30 days): Full event data, instantly queryable. Stored as JSONL files.
- Warm (30 to 365 days): Full event data, queryable with slight delay. Compressed archives.
- Cold (1+ years): Event metadata and decisions only. Full payloads available on request from archive.

**Immutability:** Events are append only. Once written, they are never modified. Integrity is verified through content hashing: each event includes the hash of the previous event, forming a hash chain. This makes tampering detectable without requiring a blockchain.

**Sensitive data:** Some events contain private information (email contents, personal notes). These should be encrypted at rest with a key the human controls. The event metadata (timestamp, type, actor) remains in cleartext for querying; the payload is encrypted.

---

## 7. Visualization and Querying

### Timeline View

The primary interface: a chronological timeline of agent activity. Zoomable from "this year" down to "this minute." Color coded by event type. Filterable by source, actor, tags. Click any event to expand its full detail.

This is what "replay" looks like in practice: scrub through the timeline, see what the agent was doing at any point, drill into the reasoning behind any action.

### Session Graph

For a single session: a directed graph showing the flow from input through reasoning through tool calls through output. Similar to LangSmith's run tree, but extended to include memory lookups, file reads, and external actions. Nodes are events, edges are causal relationships.

### Decision Audit View

A filtered timeline showing only decision events. Each decision shows: the trigger, the context available, the alternatives considered, the choice made, and the outcome. This is the view for accountability reviews: "Show me every decision Sivart made about sending external messages this week."

### Search

Full text search across event payloads. "Find every time Sivart mentioned Project X." "Show all tool calls to the email API." "When did Sivart last update MEMORY.md?" Search should support both structured queries (field:value) and natural language (backed by embedding search over event payloads).

### Diff View

For state reconstruction: show the diff between agent state at two points in time. What changed in memory? What files were modified? What new information entered the system? This is the git diff model applied to the full agent state.

### Implementation Path

We do not need to build a custom visualization platform. The event data can be:
1. **Explored via CLI tools** (jq queries over JSONL files) for immediate needs
2. **Visualized in Grafana** (with Loki for logs, Prometheus for metrics) for dashboards
3. **Queried via SQLite** (import JSONL into a local database) for structured analysis
4. **Eventually surfaced in a web UI** if the need justifies the investment

Start with jq and SQLite. Graduate to richer tools as patterns emerge.

---

## 8. Connecting to Existing Infrastructure

### OpenClaw Session JSONL

This is already our richest data source. Each session produces a JSONL file with every message, tool call, and response. The gap: these files are session scoped, not queryable across sessions, and lack the contextual metadata (memory state, model config) needed for full reconstruction.

**Bridge:** A post session processor that reads the JSONL, enriches each event with contextual metadata, and appends to the unified event log. This can run as a cron job or hook into OpenClaw's session lifecycle.

### Git History

Git already captures file changes with timestamps, authors, and messages. The gap: git commits are not correlated with session events. A file change in git doesn't tell you which session or decision triggered it.

**Bridge:** Include the session ID and relevant event IDs in commit messages (we partially do this already with issue references). A post commit hook can append a `file_change` event to the unified log with the commit hash as a reference.

### Memory Files

MEMORY.md and daily notes are state snapshots. The gap: we capture the state but not the transitions. We know what MEMORY.md says now, but not the sequence of updates that got it there.

**Bridge:** Git history partially solves this (every commit to MEMORY.md is a transition). A memory update hook that logs the diff, the session context, and the reasoning to the unified event log would close the gap completely.

### Cron Job Logs

Cron jobs run independently of sessions, producing their own logs. The gap: these logs are in journalctl, disconnected from the agent's event stream.

**Bridge:** Wrap cron jobs in a logging shim that writes structured events to the unified log before and after execution. Include job ID, command, duration, exit status, and output summary.

### Heartbeat State

The heartbeat state JSON tracks what was checked and when. The gap: it tracks the last check time but not the results or actions taken.

**Bridge:** The heartbeat handler already runs within a session. Ensuring that heartbeat check results are written as events in the session JSONL (which they already are, implicitly) and enriched with the heartbeat state context would close this gap.

---

## 9. Privacy Considerations

### The Tension

Full audit replay requires capturing everything: every message, every tool output, every file content. But "everything" includes private information that we might not want persisted in an audit log, even an encrypted one.

### Selective Auditing

Not all events need the same level of detail:

**Full capture:** Decisions, external actions (emails sent, messages posted), errors. These need complete payloads for accountability.

**Metadata only:** Routine file reads, internal tool calls, heartbeat checks. Capture that it happened, when, and in what context, but not the full content.

**Excluded:** Certain categories of sensitive data (medical information, financial credentials, intimate personal content) should be actively excluded from audit payloads, even if the events themselves are logged.

### Implementation

A classification layer at event creation time:
1. Each event gets a sensitivity tag: `public`, `internal`, `sensitive`, `excluded`
2. `public` and `internal` events are fully captured
3. `sensitive` events have their payloads encrypted with a separate key
4. `excluded` events log only metadata (timestamp, type, session) with no payload

The human controls the classification rules. The agent can suggest classifications but the human defines the boundaries.

### Data Sovereignty

All audit data stays local. On our server, under our control. No third party observability platform sees our data unless we explicitly choose to send it. This is a core design principle: the audit trail of a personal agent is as intimate as a diary. It should be treated accordingly.

---

## 10. Concrete Recommendations for Sivart

### Phase 1: Foundation (Now)

**Unified event log format.** Define the JSON schema above. Start writing events to `/home/clawd/clawd/audit/events/YYYY-MM-DD.jsonl`. Even before automated capture, begin manually logging significant decisions and actions in this format.

**Session post processor.** Write a script that runs after each OpenClaw session, reads the session JSONL, extracts events, enriches them with context metadata, and appends to the daily unified log. Run it via cron.

**Memory change tracking.** Add a git hook that logs MEMORY.md and daily note changes as events in the unified log, including the diff and commit context.

### Phase 2: Querying (Weeks 2 to 4)

**SQLite import.** Write a script that imports JSONL events into a SQLite database with appropriate indexes. This enables `SELECT * FROM events WHERE event_type = 'decision' AND timestamp > '2026-02-01'` queries.

**CLI query tool.** A simple shell script or Node.js tool that wraps common queries: "What happened today?", "Show decisions this week", "Find events mentioning X".

**Daily audit automation.** Extend the daily audit process to query the event log for anomalies: sessions without decisions logged, external actions without corresponding decision events, errors without remediation events.

### Phase 3: Visualization (Month 2)

**Grafana dashboards.** Connect the SQLite database (or JSONL files via Loki) to Grafana for visual timelines. Create dashboards for: daily activity overview, decision frequency, tool usage patterns, error rates.

**Session replay view.** A script or simple web page that takes a session ID and renders the full session timeline as an interactive, expandable tree. This is the "what happened in this session" view.

### Phase 4: Full Replay (Month 3+)

**State reconstruction.** Given a timestamp, reconstruct: the git state of the workspace, the contents of MEMORY.md and daily notes, the active session context, and the agent's configuration. This requires correlating git history, memory snapshots, and session events.

**Counterfactual tooling.** Take a captured decision event, modify its inputs (different context, different model, different system prompt), and re run it to see how the output changes. This is the most powerful audit capability and the hardest to build.

**Integrity verification.** Implement the hash chain for event immutability. A periodic verification job that walks the chain and alerts if any events have been tampered with.

### Architecture Principles

1. **Local first.** All data stays on our server. No third party dependencies for core audit capability.
2. **Append only.** Events are never modified after creation. Corrections are new events.
3. **Progressive enrichment.** Start with basic events, add context and metadata over time. The schema is extensible.
4. **Human readable.** JSONL files are grep friendly. SQLite is query friendly. No proprietary formats.
5. **Privacy by design.** Sensitivity classification at event creation. Encrypted payloads for sensitive data. Human controlled boundaries.
6. **Low overhead.** Audit infrastructure should not noticeably slow down the agent. Capture synchronously, process asynchronously.

### What We Already Have (and Should Preserve)

Our existing audit practices are good. The session based workflow, daily notes, decision logs, handoff documents, and git discipline already capture most of what matters. The recommendation is not to replace these but to unify them into a queryable, replayable stream.

The daily report voice. The handoff format. The decision log structure. These are not just files. They are the agent's narrative of its own operation. The unified event log adds the structured, machine queryable layer underneath without losing the human readable layer on top.

---

## Sources

### Observability Platforms
- LangSmith: https://www.langchain.com/langsmith/observability
- Helicone: https://github.com/Helicone/helicone
- Braintrust: https://www.braintrust.dev/
- Lunary: https://lunary.ai/docs
- LakeFS LLM Observability Comparison (Dec 2025): https://lakefs.io/blog/llm-observability-tools/

### Standards and Specifications
- OpenTelemetry GenAI Semantic Conventions: https://opentelemetry.io/docs/specs/semconv/gen-ai/
- OpenTelemetry GenAI Agent Spans: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/
- NIST AI RMF 1.0: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
- ISO/IEC 42001 (AI Management System)

### Event Sourcing
- Microsoft Azure Event Sourcing Pattern: https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
- Microservices.io Event Sourcing: https://microservices.io/patterns/data/event-sourcing.html

### AI Governance
- OpenAI, "Practices for Governing Agentic AI Systems" (2023)
- EU AI Act, Article 12 (logging requirements)

### Internal Research
- Agentic Audit Patterns: `research/audits/agentic-audit-patterns.md`
- Big Lab Approaches: `research/audits/big-lab-approaches.md`
- Handoffs Research: `research/handoffs/README.md`
- Composable Primitives: `research/ai-primitives/2026-02-20-composable-primitives.md`
