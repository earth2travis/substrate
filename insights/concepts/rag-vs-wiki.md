---
title: "RAG vs Wiki"
tags: [concept, memory, knowledge-management, rag, wiki, agent-design]
related: [[agent-memory]], [[context-stack]], [[llm-wiki-pattern]], [[knowledge-graphs-as-agent-memory-substrate]], [[synthesis-over-retrieval]], [[per-run-learning]]
source: research/findings/rag-vs-wiki.md
---

# RAG vs Wiki

## Definition

The fundamental architectural choice in agent knowledge management: retrieval-augmented generation (RAG) versus persistent structured wiki. They are not competitors but different layers. RAG is a search tool. The wiki is a memory system.

## RAG: Retrieval Strategy

**How it works.** Documents are embedded into vectors. At query time, relevant chunks are retrieved and fed to the LLM for synthesis. The LLM answers from retrieved fragments.

**Strengths.** No maintenance required; upload and query. Works well for single-document lookup against static corpora. Established tooling and infrastructure.

**Weaknesses.** The LLM rediscovers knowledge from scratch on every question. No accumulation of understanding across sessions. Cross-document synthesis is hit-or-miss. The corpus degrades as more documents are added (noise increases). Nothing is built over time.

## LLM Wiki: Knowledge Structure

**How it works.** The LLM reads sources and writes structured, interlinked pages. Updates occur when new sources arrive. Queries are answered from the wiki, not raw sources.

**Strengths.** Knowledge compounds over time. Cross-references already exist. Contradictions are flagged, not ignored. Synthesis reflects everything read so far. Good answers can be filed back as permanent pages. Maintenance burden shifts from human to LLM.

**Weaknesses.** Requires upfront structure and convention. Benefits emerge gradually, not immediately. Needs periodic linting to prevent drift. Small wikis do not benefit from compounding.

## The Fundamental Difference

RAG asks: "What in my documents relates to this question?"

The wiki asks: "What does my accumulated knowledge say about this question?"

One is search. The other is memory.

## When to Use Each

| Scenario | RAG | Wiki |
|----------|-----|------|
| Quick lookup against static docs | Yes | Overkill |
| Deep topic research over weeks/months | No | Yes |
| Team knowledge base staying current | Degrades | Yes |
| Personal knowledge management | Poor | Yes |
| One-off document analysis | Yes | Overkill |
| Competitive intelligence tracking | No | Yes |
| Building understanding as you go | No | Yes |

## Hybrid Model

The wiki can use RAG as a fallback. When a question is not covered by existing pages, RAG against raw sources and file the answer as a new wiki page. The wiki is persistent memory; RAG is the out-of-coverage safety net.

The Substrate pipeline (_ingest.py → findings → insights) is the wiki approach. Raw sources are not queried directly. They are compiled into durable, cross-referenced knowledge.

## Related

- [[agent-memory]] -- Agent memory architecture
- [[context-stack]] -- Layered memory system
- [[llm-wiki-pattern]] -- The wiki approach to agent knowledge
- [[knowledge-graphs-as-agent-memory-substrate]] -- Graph topology for wiki navigation
