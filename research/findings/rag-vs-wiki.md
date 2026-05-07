---
title: "RAG vs LLM Wiki"
tags: [finding, comparison, memory, rag, wiki, knowledge-management]
related: [[agent-memory]], [[context-stack]], [[llm-wiki-pattern]]
source: research/raw/rag-vs-wiki.md
ingested: 2026-05-07
---

# RAG vs LLM Wiki

Comparison between traditional retrieval-augmented generation (RAG) and the persistent wiki approach to knowledge management for agents.

## Key Points

**RAG: retrieval strategy.** Upload documents, embed into vectors, retrieve relevant chunks at query time, synthesize answer from fragments. The LLM rediscovers knowledge from scratch on every question. No accumulation across sessions. The corpus degrades as more documents are added.

**LLM Wiki: knowledge structure.** LLM reads sources, writes structured wiki of interlinked pages, updates when new sources arrive, answers from the wiki not raw sources. Knowledge compounds over time. Cross-references already exist. Contradictions are flagged, not ignored. Synthesis reflects everything read so far.

**When to use each.** RAG wins for quick lookup against static docs and one-off document analysis. The wiki wins for deep topic research over weeks, team knowledge bases that need staying current, personal knowledge management, competitive intelligence tracking, and reading that builds understanding over time.

**Hybrid model.** The wiki can use RAG as a fallback: when a question is not covered by existing pages, RAG against raw sources, then file the answer as a new wiki page. The wiki is persistent memory; RAG is the out-of-coverage safety net.

**Fundamental difference.** RAG asks "what in my documents relates to this question?" The wiki asks "what does my accumulated knowledge say about this question?" One is search; the other is memory.

## Relevance

Substrate is an LLM Wiki. The _ingest.py → findings → insights pipeline is the compounding knowledge structure. RAG would not capture cross-references, promoted insights, or the graph topology.

## Related

- [[agent-memory]] -- Agent memory architecture
- [[context-stack]] -- Layered memory system
- [[llm-wiki-pattern]] -- The wiki approach to agent knowledge
