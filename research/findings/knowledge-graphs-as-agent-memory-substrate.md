---
title: "Knowledge Graphs as Agent Memory Substrate: From Flat Files to Structured Relationships"
tags: [agent-memory, knowledge-graphs, graphrag, agentic-architecture, memory-systems]
related:
  - [[memory-systems]]
  - [[the-context-stack-spec]]
  - [[mempalace-analysis]]
  - [[rag-vs-wiki]]
  - [[agent-identity]]
  - [[context-stack-as-conscience]]
source: research/raw/knowledge-graphs-as-agent-memory-substrate.md
---

# Knowledge Graphs as Agent Memory Substrate: From Flat Files to Structured Relationships

## Summary

Flat markdown files hit a wall when you need to answer graph traversal questions: "What decisions affect the deployment pipeline?" "If we change the auth provider, what breaks?" These require following typed relationships between entities, something no amount of vector search over flat text can reliably answer. The field has converged on hybrid architectures that combine vector similarity for fast initial retrieval with graph traversal for relational reasoning. Five approaches dominate: Graphiti/Zep (temporal knowledge graphs, 94.8% on Deep Memory Retrieval), Microsoft GraphRAG (community detection for hierarchical summarization), Mem0 (universal memory layer with conflict detection), Neo4j plus LLM patterns, and the emerging ecosystem (Cognee, Memary, LangMem, Letta). For Sivart, the verdict is hybrid: keep markdown files as the narrative layer, add a graph layer for structured relationships, use embeddings for semantic retrieval. The graph does not replace the files; it indexes the relationships between them.

## Key Claims

1. **Document-based memory (what we have) has real strengths:** human-readable, git-versioned, zero dependencies, surprisingly good for narrative context. But it fails on relational queries, deduplication, and impact analysis.

2. **Graph-based memory makes relationships first-class citizens.** Traversal queries ("what's downstream of X?") are natural. Impact analysis is trivial: follow the edges. Temporal metadata enables point-in-time queries.

3. **Hybrid is where the field is going.** Graph for structured relationships, vector store for semantic similarity, documents for narrative context. Each layer works independently; graceful degradation.

4. **Schema design for a personal AI agent requires nine node types:** Person, Decision, Task, Project, Tool, Concept, Event, File, Session. Every edge is typed and directional. Temporal metadata on everything. Source provenance on every fact.

5. **Storage recommendation: start with Kuzu.** Embedded graph database, zero operational overhead, Cypher support, tiny resource footprint, runs fine on 2GB RAM. If outgrown, migrating to Neo4j is straightforward.

## Implications

The migration path is incremental, not big bang. Phase 1: extract and index existing markdown into a graph. Phase 2: dual write path (markdown plus graph updates). Phase 3: use graph for relational queries while keeping markdown for narrative. The graph is a derived index; if it breaks, rebuild it from the files. Zero risk.

## Related

- [[memory-systems]] — Memory architectures supporting agent continuity
- [[the-context-stack-spec]] — The Context Stack as the narrative layer
- [[mempalace-analysis]] — Spatial memory scoping and its performance laundering gaps
- [[agent-identity]] — Identity as the foundation of persistent memory
- [[context-stack-as-conscience]] — Moral architecture requiring integrated memory
