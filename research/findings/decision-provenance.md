---
title: Decision Provenance for AI Agents
tags:
  - ai-agents
  - knowledge-management
  - process-philosophy
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/decision-provenance.md
---

# Decision Provenance for AI Agents

_Research document for Sivart's decision tracking infrastructure._
_Created: February 23, 2026_

---

## The Question

Why did the agent decide X? What did it know at the time?

These two questions sit at the heart of everything we're building. An agent that acts without being able to explain itself is a black box with API access. An agent that can trace every decision back to its inputs, reasoning, and alternatives considered is something fundamentally different: accountable, debuggable, improvable.

Decision provenance is the infrastructure that makes this possible. Not logging. Not observability. Provenance: the full causal chain from input to decision to outcome, preserved in a way that survives time and can answer questions about itself.

---

## State of the Art

The field is converging from three directions: observability platforms building downward toward reasoning, memory systems building upward toward explanation, and academic provenance models trying to unify everything.

### Observability Platforms

**LangSmith** (LangChain) and **Langfuse** represent the current industry standard for agent tracing. Both capture hierarchical traces of LLM invocations: prompt in, completion out, tool calls, latency, token counts. LangSmith integrates tightly with LangChain's ecosystem. Langfuse is open source and built on OpenTelemetry, making it framework agnostic.

Both platforms answer "what happened" well. They show you the sequence of LLM calls, which tools fired, what the inputs and outputs were. What they miss is "why." The reasoning that connects observation to action lives inside the model's generation, and these platforms treat that generation as an opaque blob. You can read it, but you can't query it structurally.

**OpenTelemetry for LLM** is the emerging standard layer. The OpenTelemetry community has defined semantic conventions for generative AI, covering model invocations, token usage, and embedding operations. Langfuse and LangSmith both support OTel ingestion. This matters because it means provenance data can flow through existing infrastructure without vendor lock in.

**Arize Phoenix** and **Weights & Biases** offer similar tracing with more emphasis on evaluation and drift detection. Phoenix is particularly interesting for its focus on embedding visualization and retrieval quality.

The limitation across all of these: they're built for debugging production systems, not for answering philosophical questions about why an agent did what it did. They capture the mechanics but not the epistemology.

### Memory and Knowledge Graph Systems

**Graphiti/Zep** represents the most sophisticated approach to temporal agent memory. The Zep paper (Rasmussen et al., January 2025) introduces a bi-temporal knowledge graph architecture where every fact has two timestamps: when it became true in the world, and when the agent learned about it. This distinction is critical for decision provenance because it lets you reconstruct the agent's epistemic state at any point in time.

Graphiti's architecture uses three subgraphs: an entity graph (nodes and semantic edges), an episodic graph (raw conversation episodes linked to extracted entities), and a community graph (higher order clusters). The episodic edges are bidirectional: you can trace from a fact back to the conversation where it was learned, or from a conversation forward to all facts extracted from it. This is genuine provenance, not just logging.

The bi-temporal model is the key insight. Most systems track "when was this stored." Zep tracks "when was this true" separately from "when did we learn it." For decision provenance, this means you can ask: "At time T, what did the agent believe about X?" and get an answer that accounts for information that existed but hadn't been ingested yet.

**Mem0** takes a lighter approach with a managed memory layer that handles summarization, conflict resolution, and retrieval. Less powerful for provenance but simpler to operate.

### Academic Provenance Models

**PROV-AGENT** (Souza et al., August 2025) is the most directly relevant academic work. It extends the W3C PROV standard to cover agentic workflows, introducing specific entity types for prompts, responses, model invocations, and agent decisions. The model integrates with MCP (Model Context Protocol) and captures provenance at the granularity of individual reasoning cycles.

PROV-AGENT's data model defines three core entity types from W3C PROV and specializes them:

- **Entities:** Prompts, responses, domain data, agent decisions
- **Activities:** AI model invocations, tool executions, data transformations
- **Agents:** The AI agents themselves, with attribution chains

The critical contribution is making agent decisions first class objects in the provenance graph, not just side effects of model invocations. Each decision is attributed to an agent, derived from specific prompts and responses, and connected to the data it consumed. This enables the key provenance queries: "What inputs led to this decision?" "What other decisions depended on this one?" "If this input were different, what would have changed?"

**AgentTrace** (February 2026) proposes a structured logging framework with three trace types: operational (method, status, duration), cognitive (thought, plan, reflection), and contextual (tool invocations, data access, provenance links). The cognitive trace layer is what distinguishes it from pure observability: it explicitly captures the reasoning excerpts that connect inputs to outputs.

**AgenTracer** introduces counterfactual replay for debugging agent failures. The approach systematically replaces agent actions with oracle actions to identify where the agent's reasoning diverged from correct behavior. This is the closest existing work to "what would have happened if the agent had decided differently?"

**SagaLLM** (VLDB 2025) brings database transaction concepts to LLM reasoning chains. It maintains an audit trail of computational steps with compensation metadata for recovery. The key idea: treat each reasoning step as a transaction that can be inspected, rolled back, or replayed with different inputs.

---

## What Needs to Be Captured

A decision provenance record answers five questions: What was decided? Why? What else was considered? How confident was the agent? What happened as a result?

### The Decision Record

Every significant decision should capture:

**Identity**
- Unique decision ID (content addressable hash or UUID)
- Timestamp (when the decision was made)
- Session context (which conversation, which turn)
- Agent identity (which agent, which model, which configuration)

**Inputs**
- What information was available at decision time
- Which sources were consulted (files read, searches performed, tools called)
- What the human said or asked (the trigger)
- Relevant memory state (what the agent believed to be true)

**Reasoning**
- The chain of thought that led to the decision
- Key factors that influenced the outcome
- Assumptions made (explicit and implicit)
- Confidence level (high/medium/low, or numeric if the model provides it)

**Alternatives**
- What other options were considered
- Why they were rejected
- Under what conditions they might have been preferred

**Outcome**
- What action was taken
- What the observable result was
- Whether the human accepted, modified, or rejected the decision
- Downstream effects (decisions that depended on this one)

**Metadata**
- Model used (including version/checkpoint)
- Temperature and sampling parameters
- Context window utilization at decision time
- Token counts (input, output, thinking)

### What Counts as a "Decision"

Not every model output is a decision worth tracking. The practical question is granularity. Track too little and you lose the chain. Track too much and you drown in noise.

A useful heuristic: a decision is worth tracking when it closes off alternatives. Choosing to send an email (versus not sending it) is a decision. Choosing how to format a bullet point is not. The test is reversibility and consequence. If the action is hard to undo or has effects beyond the current turn, it's a decision.

For Sivart specifically, decisions worth tracking include:

- External actions (emails sent, messages posted, files committed)
- Architectural choices (how to structure something, which approach to take)
- Information synthesis (conclusions drawn from research, summaries that compress away detail)
- Recommendations to the human (advice given, options presented)
- Process deviations (choosing not to follow an established procedure)
- Memory updates (what to remember, what to forget)

---

## Storage: The Architecture Question

Three approaches, each with real tradeoffs.

### Append Only Logs

The simplest model. Every decision gets a timestamped entry in a log. Immutable. Auditable. Easy to implement.

**Strengths:** Integrity (nothing gets silently modified), simplicity (it's just files), compatibility with git (every append is a diff), natural chronological ordering.

**Weaknesses:** Querying across decisions requires scanning. No structural relationships between decisions. "What decisions were influenced by fact X?" requires full text search or external indexing. Scales linearly in storage but poorly in queryability.

**Best for:** Single agent systems with low decision volume where chronological review is the primary access pattern. Which is, notably, where we are right now.

### Knowledge Graphs

The Graphiti/Zep approach. Decisions are nodes. Relationships are edges. The graph structure encodes causal chains, dependency relationships, and temporal ordering natively.

**Strengths:** Rich querying ("show me all decisions that depended on this piece of information"), natural representation of causal chains, temporal queries ("what did the agent believe at time T"), scales to multi-agent (each agent is a node with attribution edges).

**Weaknesses:** Operational complexity (requires a graph database like Neo4j), harder to version control, overkill for low decision volumes, the schema design problem (getting the ontology right is hard and getting it wrong is expensive).

**Best for:** Multi-agent systems with high decision volumes where causal analysis and temporal queries are primary access patterns.

### Hybrid: Logs + Index

Append only markdown files as the source of truth, with a lightweight index (SQLite, JSON, or even grep friendly structured headers) that makes them queryable.

**Strengths:** Git compatible source of truth, queryable without a database, incrementally adoptable (start with logs, add indexing later), human readable at every layer.

**Weaknesses:** Index can drift from source, requires maintenance, less powerful querying than a full graph.

**Best for:** Systems that start simple and need to scale. Which is exactly our trajectory.

### The Recommendation for Sivart

Start with the hybrid approach. Here's why:

Our existing infrastructure is git and markdown. Our decision volume is low (dozens per day, not thousands). Our primary access pattern is "what happened recently and why," not "trace the causal chain across six months of decisions." The hybrid approach respects what we already have while creating a path toward richer querying.

The concrete architecture:

1. **Source of truth:** Markdown files in `decisions/` (already exists)
2. **Structure:** Standardized frontmatter with machine parseable fields
3. **Index:** A generated `decisions/index.json` that summarizes all decisions for fast lookup
4. **Git history:** The append only log is git itself. Every decision file is a commit. The immutability comes from version control.

When (if) we outgrow this, the structured frontmatter makes migration to a graph database mechanical rather than archaeological.

---

## Making It Queryable

Archived decisions that nobody can find are worse than no decisions at all. They create false confidence: "we're tracking everything" while nobody can answer "why did we do X?"

### Query Patterns That Matter

1. **Temporal:** "What decisions were made on February 15?" (index scan by date)
2. **Topical:** "What decisions have we made about email handling?" (full text search or tag filtering)
3. **Causal:** "What led to the decision to use 1Password?" (backlinks and references)
4. **Counterfactual:** "What would have changed if we'd known X earlier?" (requires epistemic state reconstruction)
5. **Audit:** "Show me all decisions where confidence was low" (frontmatter query)
6. **Pattern:** "Are we making the same type of mistake repeatedly?" (aggregation across decisions)

### Making Queries Practical

**For queries 1 and 2:** A simple index with date, tags, and title gets you there. `grep` and `jq` against `index.json` handles most cases.

**For query 3:** Explicit cross references in decision files. "This decision relates to #42" or "This supersedes decisions/2026-02-10-email-provider.md." Links create the causal web.

**For query 4:** This is the hard one. It requires knowing what the agent knew at decision time, which means the decision record must capture its epistemic state (or at least reference the memory files and context that were loaded). Git history helps here: you can check out the repo at the commit timestamp to see exactly what files existed.

**For queries 5 and 6:** Structured frontmatter with confidence levels, decision categories, and outcome tracking. This is where the index earns its keep.

### The Agent as Its Own Historian

The most powerful queryability feature is the agent itself. If decision records are well structured, the agent can read them, synthesize patterns, and answer natural language questions about its own decision history. "Why did I decide to use Mercury for banking?" becomes a retrieval problem, not an archaeological expedition.

This is where our file based approach has an unexpected advantage over database approaches: the decision records are in the agent's native format (text), stored where the agent already looks (the workspace), and readable without any special tooling.

---

## Connecting to Our Infrastructure

### What We Already Have

Our existing infrastructure provides more decision provenance than we might realize:

- **`decisions/` folder:** Named decision records with context and reasoning. This is already the core of the system.
- **`memory/YYYY-MM-DD.md` files:** Daily logs that capture what happened in sequence. The raw material from which decisions can be reconstructed.
- **`MEMORY.md`:** Curated long term memory. The agent's beliefs at any point (check git history for temporal state).
- **Git history:** Every file change is timestamped, attributed, and diffable. The commit log is a coarse grained decision log.
- **OpenClaw session transcripts:** The full conversation history for each session. The richest source of reasoning, but the least structured.
- **Handoff documents:** `handoffs/YYYYMMDD-HHMM-description.md` files capture state at session boundaries, including decisions made and reasoning.

### What's Missing

1. **Structured frontmatter on decision files.** Current decisions are free form markdown. Adding YAML frontmatter with date, tags, confidence, status, and related decisions would make them machine queryable without changing the human experience.

2. **Explicit epistemic state snapshots.** Decision files should reference what memory files and context were loaded when the decision was made. Not a full dump, just a manifest: "At decision time, I had loaded MEMORY.md (commit abc123), memory/2026-02-23.md, and the results of 3 web searches."

3. **Outcome tracking.** Most decisions are recorded when made but never revisited. Adding a "status" field (proposed/accepted/rejected/superseded) and an "outcome" section that gets filled in later closes the feedback loop.

4. **Cross referencing.** Decisions should link to related decisions, issues, and memory entries. These links are the lightweight version of graph edges.

5. **An index.** A generated file that lets the agent (or a script) quickly find decisions by date, topic, or status without reading every file.

### The Integration Path

**Phase 1: Structured Decision Records (Now)**
Add YAML frontmatter to the decision file template. Fields: id, date, tags, confidence, status, related, context_refs. Continue writing decisions in markdown. Generate `decisions/index.json` with a simple script.

**Phase 2: Automatic Capture (Near Term)**
Instrument key decision points so the agent automatically creates decision records for external actions (emails, commits, deployments). The agent already knows when it's making a significant choice; it just needs the habit of writing it down in a structured way.

**Phase 3: Retrospective Analysis (Medium Term)**
Build a periodic review process (heartbeat task or cron job) that reads recent decisions, checks for missing outcomes, identifies patterns, and updates the index. The agent becomes its own auditor.

**Phase 4: Temporal Queries (Future)**
If we outgrow file based querying, migrate the structured frontmatter into a lightweight database (SQLite) or a temporal knowledge graph (Graphiti). The structured files make this migration straightforward because the data model already exists in the frontmatter.

---

## The Data Model

### Decision File Template

```yaml
---
id: DEC-2026-0223-001
date: 2026-02-23T16:00:00Z
title: "Use hybrid storage for decision provenance"
tags: [architecture, infrastructure, decisions]
confidence: high
status: proposed
related:
  - decisions/2026-02-1password-vault-structure.md
  - "#47"
context_loaded:
  - MEMORY.md@abc1234
  - memory/2026-02-23.md
  - "web_search: decision provenance AI agents"
outcome: null
supersedes: null
---

# Use Hybrid Storage for Decision Provenance

## Context

[What situation prompted this decision]

## Considered Alternatives

1. **Append only logs:** [Why rejected or deferred]
2. **Knowledge graph:** [Why rejected or deferred]
3. **Hybrid approach:** [Why chosen]

## Decision

[What we decided and why]

## Consequences

[Expected effects, both positive and negative]

## Outcome

[Filled in later: what actually happened]
```

### Index Schema

```json
{
  "decisions": [
    {
      "id": "DEC-2026-0223-001",
      "date": "2026-02-23T16:00:00Z",
      "title": "Use hybrid storage for decision provenance",
      "tags": ["architecture", "infrastructure", "decisions"],
      "confidence": "high",
      "status": "proposed",
      "file": "decisions/2026-02-use-hybrid-storage.md",
      "related": ["decisions/2026-02-1password-vault-structure.md"],
      "has_outcome": false
    }
  ],
  "last_updated": "2026-02-23T16:30:00Z",
  "total": 1
}
```

---

## Scaling to Multi-Agent

When Sivart spawns subagents (which it already does via OpenClaw's `sessions_spawn`), decision provenance gets harder. Each subagent has its own context, makes its own decisions, and reports back to the orchestrator who synthesizes the results.

### The Multi-Agent Provenance Problem

1. **Attribution:** Which agent made which decision? The orchestrator and subagents may both contribute reasoning to a final output.
2. **Information flow:** What did the orchestrator tell the subagent? What did the subagent report back? These handoffs are lossy.
3. **Aggregation:** When the orchestrator combines subagent outputs, the combination itself is a decision that needs provenance.
4. **Temporal coordination:** Subagents run in parallel. Their decisions may depend on information that changes during execution.

### The Approach

Each subagent should produce its own decision records with its agent identity in the metadata. The orchestrator's synthesis decision references the subagent outputs explicitly. The PROV-AGENT model's attribution chains are the right conceptual framework here: every decision is attributed to an agent, and delegation is an explicit relationship.

For our current setup, this means subagent task outputs should include a "decisions made" section that the orchestrator can reference. Not a new system, just a convention that makes the existing handoff pattern provenance aware.

---

## Counterfactual Replay

The most ambitious capability: "What would have happened if the agent had known X?" or "What if it had chosen differently at step Y?"

### Why It Matters

Counterfactual replay is how you learn from decisions. Not just "that decision was wrong" but "here's specifically what information or reasoning would have changed the outcome." It's the difference between incident reports that say "we made a mistake" and incident reports that say "if we had checked the calendar before sending the email, we would have seen the conflict."

### What It Requires

1. **Complete epistemic state:** You need to know exactly what the agent knew at decision time. Not approximately. Exactly.
2. **Deterministic replay:** You need to be able to re-run the decision with modified inputs and get a meaningful result. LLMs are stochastic, so "deterministic" means "controlled enough to be informative."
3. **Causal isolation:** You need to modify one variable while holding others constant. This requires understanding which inputs actually influenced the decision.

### What's Practical Today

Full counterfactual replay is a research problem. But partial versions are achievable:

- **Epistemic reconstruction:** Using git history and context_loaded references to rebuild what the agent knew. This is achievable now with our proposed data model.
- **Manual replay:** A human reads the decision record, changes one input mentally, and reasons about what would have changed. Low tech but useful for incident analysis.
- **Prompted replay:** Give the agent the original decision context with one modified input and ask "what would you decide now?" Not rigorous, but informative for calibration.

---

## Concrete Recommendations for Sivart

### Do Now

1. **Standardize decision file frontmatter.** Add the YAML template above to all new decision files. Backfill existing ones as encountered.

2. **Add context_loaded to decision records.** When making a significant decision, note which files were read and what searches were performed. This is the minimum viable epistemic state.

3. **Create a decision index generator.** A simple Node.js script that parses `decisions/*.md` frontmatter and produces `decisions/index.json`. Run it as a pre-commit hook or periodic task.

4. **Establish the "decisions worth tracking" heuristic.** External actions, architectural choices, recommendations to the human, process deviations, and information synthesis. Everything else is noise.

### Do Soon

5. **Add outcome tracking.** Revisit decisions monthly. Update the status field. Fill in the outcome section. This is where provenance becomes learning, not just logging.

6. **Cross reference decisions.** Use the `related` field to link decisions that depend on or supersede each other. These links are the lightweight causal chain.

7. **Build a decision review into the audit cycle.** The weekly process audit should include: "Were all significant decisions this week captured? Do they have adequate context?"

### Do Eventually

8. **Instrument automatic decision capture.** When the agent sends an email, creates a PR, or pushes a commit, automatically generate a decision stub with the action and context.

9. **Build temporal query capability.** A script or agent skill that can answer "what did Sivart believe about X on date Y?" by checking out the relevant git state.

10. **Evaluate graph migration.** When decision volume exceeds what file scanning can handle (probably hundreds of cross referenced decisions), evaluate migrating the index to SQLite or a graph database. The structured frontmatter makes this a mechanical transformation.

---

## Sources

### Academic

- Souza et al., "PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows," arXiv:2508.02866 (August 2025). Extends W3C PROV for agentic workflows.
- Rasmussen et al., "Zep: A Temporal Knowledge Graph Architecture for Agent Memory," arXiv:2501.13956 (January 2025). Bi-temporal knowledge graph for agent memory.
- "AgentTrace: A Structured Logging Framework for Agent System Observability," arXiv:2602.10133 (February 2026). Three-layer trace model: operational, cognitive, contextual.
- "AgenTracer: Counterfactual Replay for Diagnosing Agent Failures," OpenReview (2025). Counterfactual replacement of agent actions with oracle actions.
- "SagaLLM: Context Management, Validation, and Transaction," VLDB vol.18 (2025). Database transaction patterns applied to LLM reasoning chains.

### Industry

- LangSmith Observability: https://www.langchain.com/langsmith/observability
- Langfuse (open source LLM observability): https://langfuse.com
- Graphiti (temporal knowledge graphs): https://github.com/getzep/graphiti
- OpenTelemetry Semantic Conventions for GenAI: https://opentelemetry.io/docs/specs/semconv/gen-ai/
- Arize Phoenix: https://phoenix.arize.com

### Internal

- [Agentic Audit Patterns](/research/audits/agentic-audit-patterns.md): Audit trail as first class artifact, decision audit patterns.
- [Handoffs Research](/research/handoffs/README.md): Context preservation across session boundaries, epistemic state at handoff time.
- [Composable Primitives](/research/ai-primitives/2026-02-20-composable-primitives.md): Memory as a primitive, context engineering, the composition model.

---

_Decision provenance is not a feature you add. It's a discipline you practice. The infrastructure supports the discipline, but the discipline comes first. We already make decisions worth tracking. Now we make the tracking worth the decisions._
