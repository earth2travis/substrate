---
title: "Agent Memory: From Flat Files to Structured Continuity"
tags: [concept, agent-memory, knowledge-graphs, context-engineering, memory-systems]
related:
  - [[context-stack]]
  - [[agent-identity]]
  - [[agent-native-operations]]
  - [[agentic-architecture]]
  - [[conscience]]
  - [[rag-vs-wiki]]
  - [[the-openclaw-lesson]]
  - [[process-philosophy]]
source: research/findings/memory-systems.md
---

# Agent Memory: From Flat Files to Structured Continuity

## Overview

The agent memory problem is not a technology problem. It is a design problem. The tools already exist: markdown files, YAML frontmatter, folder hierarchies, wiki-links. What matters is the architecture that makes memory inspectable, auditable, and editable by humans.

## The Benchmark Surprise

Plain markdown files organized in folders, with grep and search, outperformed purpose-built memory infrastructure (74.0% vs. 68.5% on LoCoMo). Why? Because LLMs already know how to work with files. Fighting that instinct with specialized APIs is swimming upstream.

## Three Architectures Compared

| Approach | Strengths | Weaknesses |
|----------|-----------|------------|
| **Document-based** (flat markdown) | Human-readable, git-versioned, zero dependencies | Relationships implicit, no structured traversal, scales poorly |
| **Graph-based** (Neo4j, Kuzu) | Relationships first-class, traversal queries natural, impact analysis trivial | Requires infrastructure, extraction imperfect, cold start problem |
| **Hybrid** (graph + vector + docs) | Best of all worlds, graceful degradation, each layer works independently | More complex to build and maintain, multiple systems to synchronize |

The verdict: hybrid. Keep markdown files as the narrative layer. Add a graph layer for structured relationships. Use embeddings for semantic retrieval. The graph does not replace the files; it indexes the relationships between them.

## Memory Types Matter

Not all memories are equal. A taxonomy is required:

- **Decision** — Chose React over Vue
- **Preference** — Likes dark mode
- **Relationship** — Sarah is the CTO
- **Commitment** — Promised to follow up Friday
- **Lesson** — Never deploy on Fridays

"Show me all decisions from last month" only works if you stored them AS decisions. Dumping everything into a single notes file is the agent equivalent of writing on your hand.

## Key Patterns

**The vault index.** A single file listing every note with a one-line description. The agent scans the index first before deciding what to read. Dramatically more efficient than embedding search for most queries.

**Budget-aware context injection.** Compress conversations into priority-tagged observations: critical (decisions, commitments, blockers), notable (insights, preferences), background (routine updates). Load critical first, then fill remaining budget.

**Intent-preserving compaction.** Lossy abbreviation degrades retrieval quality by 12.4 percentage points. Semantic compression by an agent captures the why and how, not just the what.

**Spatial scoping.** Treat directories as "Wings" (research/, memory/, decisions/) to guide attention. Narrow search scope before applying semantic similarity.

## Storage Recommendation: Start with Kuzu

Embedded graph database, zero operational overhead, Cypher support, tiny resource footprint, runs fine on 2GB RAM. If outgrown, migrating to Neo4j is straightforward since both speak Cypher. The graph is a derived index; if it breaks, rebuild it from the files.

## Connection to Context Stack

The Context Stack IS the memory architecture. SOUL.md is the identity anchor. The Intelligence layer (skills/, research/, knowledge/, relationships/) is the memory store. DECISIONS.md is the decision log. The Stack makes memory portable, versioned, and human-legible.

## Related

- [[context-stack]] — The universal specification for agent identity
- [[agent-identity]] — Identity as the foundation of persistent memory
- [[agent-native-operations]] — Tools designed for AI-human partnership
- [[agentic-architecture]] — System design for autonomous agents
- [[the-openclaw-lesson]] — Security as foundational to memory integrity
- [[process-philosophy]] — Reality as process, not substance
