---
title: "HyperStack: Agent Provenance Graph"
tags: [agents, knowledge-graph, provenance, security, multi-agent]
related:
  - [[agent-native-operations]]
  - [[proof-of-work]]
  - [[decision-provenance]]
source: research/raw/hyperstack-evaluation.md
---

# HyperStack: Agent Provenance Graph

A typed knowledge graph for AI agents built around "provenance": timestamped facts with typed edges, deterministic trust resolution, and full audit replay.

## Core Primitives

**The "card"** is a fact, decision, or entity connected to other cards via typed relations: `blocks`, `depends-on`, `owns`, `decided`.

**Decision Replay** reconstructs exact graph state at any point in time: "What did the agent know when it decided X?" Not a log, a queryable snapshot.

**Impact and Blocker Queries** traverse typed graphs for dependency and blast radius analysis.

**Trust Layer** provides agent provenance stamps and deterministic conflict resolution between agents without LLM calls. Critical for multi-agent coordination.

**GraphRAG** combines semantic similarity (vector) with graph traversal. Seed cards from similarity, surface connected context via relations.

**Audit Branches** fork the graph for experiments, then diff and merge with full accountability. Git for agent knowledge state.

## Key Capabilities

- `hs.replay("decision-use-clerk")` → exact state at decision time, detect hindsight changes
- `hs.blockers("deploy-prod")` → `[migration-23, staging-tests]`
- `hs.impact("use-clerk")` → blast radius of a change
- `hs.resolveConflict(slug, { trustThreshold: 0.8 })` → deterministic resolution

## Architecture and Economics

- Zero dependencies, 108.7 kB, MIT license
- Self-hosting via Docker with PostgreSQL backend
- Free tier: 50 cards. Pro: $29/mo for 500+
- OpenAI embeddings or fully local via Ollama

## Comparison to Alternatives

Competes with Mem0, Backboard, Cognee. Differentiators: timestamped provenance (others lack replay), deterministic trust resolution (others use LLM), $0/op cost, typed relations vs auto-extracted.

## Assessment

**When to adopt:** Not yet for single-agent use. Markdown + git + memory_search covers most needs less formally. Becomes compelling when:
1. Two or more agents need to coordinate decisions
2. Deterministic conflict resolution is needed
3. "What did agent X know when agent Y decided Z?" must be answerable

**Concerns:** Solo maintainer, 8 npm versions, no visible public GitHub repo for core. Cloud dependency adds external API surface. 50-card free tier is tiny.

## Connection to Our Work

The Moravec/DAO thesis ("agents and smart contracts ARE the organization, that's what gets governed") implies exactly the kind of multi-agent coordination HyperStack addresses. When agents are the governed assets, provenance of their decisions is governance infrastructure, not a nice-to-have.
