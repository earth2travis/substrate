---
title: "Agent Provenance Graph"
tags: [agents, knowledge-graph, provenance, multi-agent, governance]
related:
  - [[proof-of-work]]
  - [[decision-provenance]]
  - [[agent-native-operations]]
  - [[context-stack]]
  - [[agent-memory]]
source: research/findings/hyperstack-evaluation.md
---

# Agent Provenance Graph

A structured knowledge graph for tracking what an agent knew, when it knew it, and what it decided based on that knowledge. Not a log. A queryable, traversable, time-indexed graph.

## The Core Idea

Traditional audit captures what happened: "Agent X wrote file Y at time Z."
Provenance captures why: "Agent X knew facts A, B, and C; they implied dependency D; therefore Agent X wrote file Y."

The difference between a log and a provenance graph is the difference between a receipt and a ledger. One records events. The other makes them explainable.

## Key Primitives

**The Card.** A fact, decision, or entity. Typed and timestamped.

**Typed Relations.** `blocks`, `depends-on`, `owns`, `decided`. Not generic "related to." Semantic edges that carry meaning.

**Decision Replay.** Reconstruct exact graph state at any point in time. "What did the agent know when it decided X?" Detect hindsight changes: facts that were added after the decision and might distort retrospective judgment.

**Impact and Blocker Queries.** Traversal for dependency and blast radius. `blockers("deploy-prod")` returns `[migration-23, staging-tests]`. `impact("use-clerk")` surfaces everything that would change if that decision were reversed.

**Deterministic Trust Resolution.** When multiple agents store conflicting facts, resolve without LLM calls. Agent provenance stamps and scores provide a gradient of confidence, not a binary true/false.

## When Provenance Becomes Necessary

For a single agent, markdown plus git plus memory search is sufficient. The provenance graph becomes critical when:

1. **Two or more agents coordinate decisions.** A shared graph replaces message passing. Agents don't ask each other what they think. They read what the graph says.

2. **Deterministic conflict resolution is needed.** When agents disagree, the resolution rule must be inspectable, repeatable, and independent of any single agent's judgment.

3. **Cross-temporal reasoning is required.** "What did Agent X know when Agent Y decided Z?" requires reconstructing another agent's knowledge state at a specific moment, not querying their current state.

4. **Governance is the goal.** The Moravec/DAO thesis: when agents and smart contracts ARE the organization, their decisions are the governed assets. Provenance is not observability. It is governance infrastructure.

## Design Principles

**Append only.** Facts are never modified. Corrections are new cards linked via `supersedes` relations. The graph grows; it does not mutate.

**Typed over connected.** A graph where every edge is labeled with its semantic type is more valuable than a graph with more edges. Prefer meaning over density.

**Local over centralized.** Each agent maintains its own subgraph. Shared spaces are explicitly contracted, not implicitly assumed. The graph is federated by default.

**Queryable over readable.** The primary interface is traversal, not display. A good provenance graph answers questions faster than it tells stories.

## Comparison to Alternatives

| Approach | Strength | Weakness |
|----------|----------|----------|
| Event sourcing | Immutable history, replayable | No semantic relationships; hard to traverse |
| Traditional logging | Simple, universal | Flat; no knowledge state reconstruction |
| Vector RAG | Semantic search | No causality, no temporal reasoning |
| Git history | Versioned files | No reasoning, no cross-file dependencies |
| Provenance graph | Semantic + temporal + traversable | Higher overhead, requires schema discipline |

## Connection to Our Architecture

Our current system has the pieces: session JSONL (events), git history (versions), MEMORY.md (state), decision logs (reasoning). What it lacks is the unified schema that connects them.

The HyperStack evaluation shows one implementation. The principle is more important than the tool. Whether we adopt HyperStack, build our own, or incrementally unify existing sources, the goal is the same: every decision traceable to its inputs, every input traceable to its source, every source immutable and inspectable.

The Context Stack (SOUL, CONTRACT, TASTE, MEMORY) is the agent's internal provenance. The provenance graph is its external complement: the shared, inspectable, queryable record of what the agent did and why.

## Open Questions

- What is the minimal schema that captures 80% of provenance value without drowning in metadata?
- How do we handle sensitive data in a shared graph? Encryption at the card level? Separate subgraphs with different access rules?
- When does the overhead of maintaining the graph outweigh its value? What is the threshold of agent count or decision frequency where provenance becomes essential rather than nice-to-have?
- How do we prevent the graph itself from becoming a source of context bloat? Not every fact needs to be in the graph. What is the curation rule?
