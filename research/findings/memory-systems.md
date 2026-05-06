---
title: "Agent Memory Systems: Taxonomy and Tradeoffs"
tags: [agent, memory, architecture, infrastructure, ai]
related: [[agent-architectures]], [[agentic-systems-synthesis]], [[llm-wiki-pattern]]
source: research/raw/memory-systems.md
---

# Agent Memory Systems: Taxonomy and Tradeoffs

## Summary

LLMs have no memory. Every session starts blank. Memory systems are the prosthetics we build to compensate. This research evaluates four memory types, six implementation approaches, and recommends a file-based strategy over vector databases at current scale.

## Memory Taxonomy

| Type | Description | Example Implementations |
|------|-------------|------------------------|
| **Short-term** | Context window itself | Conversation history, sliding window, compaction |
| **Long-term** | Persistent across sessions | ChatGPT Memory, Claude Projects, MemGPT archival |
| **Episodic** | Records of what happened | Session logs, Reflexion summaries, handoff documents |
| **Semantic** | General knowledge for retrieval | Vector DBs, RAG, hybrid BM25 + embeddings |

## Key Design Decisions

1. **Who writes memory?** Model itself vs. system vs. explicit process
2. **What format?** Natural language vs. structured data vs. embeddings
3. **When to retrieve?** Every turn vs. on-demand vs. triggered
4. **How to forget?** Explicit deletion vs. decay vs. never

## Assessment of MemGPT/Letta

The most sophisticated open-source memory system. Treats context as "main memory" and external storage as "disk," with self-directed memory management.

**Verdict**: Clever but fragile. Agents make bad memory decisions: save trivial things, forget important ones. The OS memory analogy breaks because the "CPU" (LLM) is unreliable.

## Recommendations

1. **Keep file-based approach** — human-readable, git-versioned, no infrastructure
2. **Add lightweight search** — `grep` or simple index over memory files
3. **Automate curation cycle** — cron job that summarizes daily files into MEMORY.md candidates
4. **Add YAML frontmatter to daily files** — enables search/filtering without embeddings
5. **Defer embeddings** — not justified until MEMORY.md exceeds 50KB or >100 daily files

## The Deeper Insight

Memory systems are only as good as retrieval. A perfectly indexed vector database is useless if the agent doesn't know when to query it. Explicit, file-based approaches make memory operations visible and auditable. That is worth more than sophistication.

## Related

- [[agent-architectures]] — Broader agent design patterns
- [[agentic-systems-synthesis]] — Three-layer architecture
- [[llm-wiki-pattern]] — Substrate as persistent knowledge base
