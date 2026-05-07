---
title: "Decision Provenance for AI Agents"
tags: [finding, provenance, decision-tracking, observability, agent-ops]
related:
- agent-memory
- context-stack
- agent-native-operations
- subagent-architecture
source: research/raw/decision-provenance.md
ingested: 2026-05-07
---
# Decision Provenance for AI Agents

The infrastructure for tracing every agent decision back to its inputs, reasoning, and alternatives considered. Not logging. Not observability. Provenance: the full causal chain preserved in a way that survives time and can answer questions about itself.

## Key Points

**State of the art converges from three directions.** Observability platforms (LangSmith, Langfuse, OpenTelemetry) capture "what happened" via hierarchical traces of LLM invocations. Memory systems (Graphiti/Zep bi-temporal knowledge graph) build "why" through episodic edges linking facts to conversations where they were learned. Academic models (PROV-AGENT, AgentTrace, SagaLLM) unify everything with formal provenance graphs, structured logging, and transaction semantics.

**What must be captured.** A decision record answers: What was decided? Why? What else was considered? How confident? What happened as a result? Identity (decision ID, timestamp, session, agent), inputs (information available, sources consulted, human trigger, memory state), reasoning (chain of thought, key factors, assumptions, confidence), alternatives (other options, why rejected, conditions for preference), outcome (action taken, result, human response, downstream effects), metadata (model, temperature, context utilization, token counts).

**What counts as a "decision."** A decision is worth tracking when it closes off alternatives. Test: reversibility and consequence. For Sivart: external actions (emails, commits), architectural choices, information synthesis, recommendations to human, process deviations, memory updates.

**Storage architecture: hybrid (logs + index).** Append-only markdown files in `decisions/` as source of truth. Standardized YAML frontmatter with machine-parseable fields. Generated `decisions/index.json` for fast lookup. Git history provides immutability. When outgrown, structured frontmatter makes migration to graph database mechanical.

**Query patterns that matter.** Temporal (by date), topical (by tag), causal (backlinks and references), counterfactual (epistemic state reconstruction), audit (confidence filtering), pattern (aggregation across decisions).

**Multi-agent provenance.** Each sub-agent produces its own decision records with agent identity in metadata. Orchestrator's synthesis decision references sub-agent outputs explicitly. Delegation is an explicit relationship in the provenance graph.

**Integration path.** Phase 1: structured decision records with YAML frontmatter. Phase 2: automatic capture at key decision points (emails, commits, deployments). Phase 3: periodic review for missing outcomes and pattern detection. Phase 4: temporal queries via git history.

## Relevance

Decision provenance is not a feature; it is a discipline. The infrastructure supports the discipline, but the discipline comes first. We already make decisions worth tracking. Now we make the tracking worth the decisions.

## Related

- [[agent-memory]] -- Memory architecture for epistemic state
- [[context-stack]] -- Where reasoning and identity are encoded
- [[agent-native-operations]] -- Executive layer and process discipline
- [[subagent-architecture]] -- Multi-agent attribution and delegation
