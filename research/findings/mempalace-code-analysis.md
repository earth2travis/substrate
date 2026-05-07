---
title: "MemPalace Code Analysis: Structure vs. Reality"
tags: [finding, memory, mempalace, vector-search, spatial-scoping]
related: [[agent-memory]], [[context-stack]], [[knowledge-graphs-as-agent-memory-substrate]]
source: research/raw/mempalace-code-analysis.md
ingested: 2026-05-07
---

# MemPalace Code Analysis: Structure vs. Reality

MemPalace is a dual-system agent memory architecture using ChromaDB for verbatim conversations and SQLite for structured facts as entity-relationship triples. Its "spatial" organization (wings, rooms, halls) is metadata filtering over standard vector search.

## Key Points

**The dual-store architecture.** The Palace (ChromaDB) stores verbatim conversations with spatial metadata (wing, room, hall). The Knowledge Graph (SQLite) stores extracted facts as Subject-Predicate-Object triples with temporal validity. The MCP server coordinates search across both stores.

**Spatial scoping via metadata filtering.** The claimed "34% retrieval boost" is achieved by progressively narrowing ChromaDB queries with `where` clauses: search within wing first, then room, then hall. Wings and rooms are metadata tags; tunnels are identical room names across different wings. The spatial metaphor is a UI layer over standard vector search.

**Critical implementation gaps.** The "closet" (summary pointing to drawers) is just a metadata pointer; abbreviation logic exists but is not the default. The fact-checker utility is not wired into the main retrieval loop, so contradictory facts from different wings are returned without flagging. Heavy reliance on regex and keyword matching means conversations without trigger words fall into generic buckets.

**Lessons for agent memory.** The spatial scoping concept is valuable but the implementation is flawed. A Context Stack using directories as "wings" achieves the same retrieval boost without a separate database. Graph-backed contradiction detection should be active, not an afterthought. Semantic compression (not regex summaries) is needed for token efficiency.

**Verdict.** MemPalace is a "spatial UI for vector search." The value is in human-legible organization, not the vector search itself. Structure is a form of intelligence. Clear, named files with clear purposes are the agent equivalent of well-organized rooms.

## Relevance

The Substrate directory structure (research/, insights/, guides/) is already a spatial scoping system. The missing piece is active contradiction detection and semantic compression.

## Related

- [[agent-memory]] -- Agent memory architecture
- [[context-stack]] -- Layered memory as spatial organization
- [[knowledge-graphs-as-agent-memory-substrate]] -- Knowledge graphs for memory
