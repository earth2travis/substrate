---
title: "HyperStack: Agent Provenance Graph"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/hyperstack-evaluation.md
---

# HyperStack: Agent Provenance Graph

**Evaluated:** 2026-03-01
**Source:** https://www.cascadeai.dev/hyperstack
**Status:** Watch list. Revisit when multi-agent coordination begins.
**NPM:** `hyperstack-core@1.5.3` (MIT, zero deps, 108.7 kB)

## What It Is

A typed knowledge graph for AI agents built around the concept of "provenance": timestamped facts with typed edges, deterministic trust resolution, and full audit replay. The core primitive is a "card" (a fact, decision, or entity) connected to other cards via typed relations (`blocks`, `depends-on`, `owns`, `decided`).

## Key Capabilities

### Decision Replay
Reconstruct the exact graph state at any point in time. "What did the agent know when it decided X?" Not just a log, a queryable snapshot.

```js
await hs.replay("decision-use-clerk");
// → Exact state at decision time
// → Detect hindsight changes
```

### Impact and Blocker Queries
Typed graph traversal for dependency and blast radius analysis.

```js
await hs.blockers("deploy-prod");    // → [migration-23, staging-tests]
await hs.impact("use-clerk");         // → blast radius of a change
```

### Trust Layer
Agent provenance stamps and scores for deterministic conflict resolution between agents without requiring LLM calls. Critical for multi-agent coordination where agents may store conflicting facts.

```js
hs.resolveConflict(slug, { trustThreshold: 0.8 })
```

### GraphRAG
Hybrid vector + graph search. Semantic similarity finds seed cards, then graph traversal surfaces everything connected. Provenance-aware throughout.

### Audit Branches
Fork the graph for experiments, diff/merge back with full accountability. Git for agent knowledge state.

## Integrations

Lists OpenClaw as a first-class integration:
```bash
npm i hyperstack-core
npx hyperstack-core login
npx hyperstack-core init openclaw-multiagent
```

Also supports: Claude Code, Cursor, LangChain, CrewAI, LangGraph, REST API, MCP.

Self-hosting available via Docker with PostgreSQL backend. Supports OpenAI embeddings or fully local via Ollama.

## Pricing

| Tier | Cost | Cards | Notes |
|---|---|---|---|
| Free | $0 | 50 | All features, 1 workspace |
| Pro | $29/mo | 500+ | Semantic search, GraphRAG, time-travel |
| Team | $59/mo | 500 | 5 API keys, unlimited workspaces |
| Business | $149/mo | 2,000 | 20 members, agent-to-agent webhooks |

## Comparison (Their Claims)

Competes with Mem0, Backboard, Cognee. Key differentiators: timestamped provenance (others lack replay), deterministic trust resolution (others use LLM), $0/operation cost (others ~$0.002/op via LLM calls), typed relations vs auto-extracted.

## Assessment for Our Use

### Where It Adds Value
- **Multi-agent trust resolution.** When multiple agents store conflicting facts, deterministic resolution without LLM calls. This becomes critical with agent swarms.
- **Decision provenance at scale.** Our markdown-based `decisions/` system works for one agent. With multiple agents making decisions concurrently, a structured graph with timestamps beats files.
- **Impact analysis.** "What breaks if we change X?" is a question we'll need to answer across agent boundaries.
- **Audit replay.** Reconstructing what was known when, across agents. Our current audit system is manual and file-based.

### Concerns
- **Early stage.** Solo maintainer, 8 npm versions, no visible public GitHub repo for the core.
- **Cloud dependency.** Adds external API dependency to a system that's currently fully local. Self-hosting mitigates this but adds infra.
- **50 card free tier is tiny.** We'd need Pro ($29/mo) almost immediately.
- **Overlap with current system.** For single-agent use, our markdown + git + memory_search already covers most of this less formally.

### Recommendation
Do not adopt yet. Our single-agent markdown system is simpler and sufficient for now. HyperStack becomes compelling when:
1. We have 2+ agents that need to coordinate decisions
2. We need deterministic conflict resolution between agents
3. We need to answer "what did agent X know when agent Y decided Z?"

When multi-agent work begins, evaluate HyperStack alongside:
- Self-hosted option (Docker + PostgreSQL + Ollama) to keep data local
- Whether the OpenClaw skill integration is production-ready
- Whether the project has matured (more contributors, stable API)

## Connection to Our Work

The Moravec/DAO thesis ("agents and smart contracts ARE the organization, that's what gets governed") implies exactly the kind of multi-agent coordination that HyperStack addresses. When agents are the governed assets, provenance of their decisions is governance infrastructure, not a nice-to-have. See `about/travis/writing/the-autonomous-organization.md`.
