---
title: "Claude + Obsidian Memory Stack: Context Amnesia as the Real Bottleneck"
tags: [agent-memory, obsidian, context-engineering, knowledge-graphs, memory-systems]
related:
  - [[solving-memory]]
  - [[knowledge-graphs-as-agent-memory-substrate]]
  - [[the-context-stack-spec]]
  - [[memory-systems]]
  - [[agent-identity]]
source: research/raw/memory-is-context-not-storage-obsidian-analysis.md
---

# Claude + Obsidian Memory Stack: Context Amnesia as the Real Bottleneck

## Summary

Analysis of a Claude + Obsidian memory stack architecture from @nyk_builderz on X (March 2026). The thesis: "Memory is not a feature. It's an operating system for attention." Context amnesia is the real bottleneck, not reasoning. Fix memory, and output compounds. The architecture has three layers: Session Memory (CLAUDE.md as teaching document, MEMORY.md as router under 200 lines, topic files for patterns/architecture/debugging/preferences), Knowledge Graph (Obsidian vault with wikilinks, MCP bridge for semantic search and structured queries), and Ingestion Pipeline (brain-ingest tool for video/audio to structured knowledge notes). A gap analysis compares this architecture to Sivart's existing system: Sivart is ahead on identity (SOUL.md), values/mission (GOALS.md), process (AGENTS.md), relational context (USER.md), and external memory (GitHub Issues). The other system is ahead on MEMORY.md size discipline, topic-based memory files, knowledge graph with semantic search, prose-as-title naming, atomic composable notes, automated ingestion, and self-improving graph maintenance.

## Key Claims

1. **"Scanning is not knowing."** The mere presence of information in a file does not mean an agent knows it. Structure, linking, and retrieval strategy determine whether stored information is actually usable.

2. **MEMORY.md must be a router, not a dump.** Under 200 lines, routing to topic files. Details live in topic files. This prevents the unbounded growth that makes memory files unwieldy.

3. **Prose-as-title naming makes search meaningful.** "memory graphs beat giant memory files.md" is self-documenting. Search results are meaningful before opening the file. Category names like "analysis.md" are opaque.

4. **Atomic notes over monoliths.** One idea per note, composable, searchable independently. The test: "would this note be useful on its own?" Some things need length (specs, guides). Most research findings do not.

5. **Ingestion as a core capability.** Every piece of content shared by the principal becomes permanent, searchable knowledge instead of a conversation that gets compacted. Automated extraction of claims, frameworks, action items, and examples.

## Implications

The gap analysis reveals concrete improvements: adopt MEMORY.md size discipline, implement topic-based memory files, consider prose-as-title naming for knowledge notes, move toward atomic composable notes, and build an ingestion skill. What NOT to adopt: Obsidian-specific tooling (we have memory_search), wikilinks syntax (standard markdown links suffice), over-engineering before testing, and brain-ingest as a dependency (build our own skill for more control).

## Related

- [[solving-memory]] — ClawVault's markdown-based memory architecture
- [[knowledge-graphs-as-agent-memory-substrate]] — Graph-based memory for relational queries
- [[the-context-stack-spec]] — The Context Stack as portable identity
- [[memory-systems]] — Memory architectures supporting agent continuity
- [[agent-identity]] — Identity as the foundation of persistent memory
