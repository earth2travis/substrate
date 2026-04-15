---
title: RAG vs LLM Wiki
created: 2026-04-08
updated: 2026-04-08
type: comparison
tags: [agent, research, memory]
sources: [raw/articles/karpathy-llm-wiki-pattern.md]
---

# RAG vs LLM Wiki

> Comparison between traditional RAG (retrieval-augmented generation) and the persistent wiki approach to knowledge management.

## RAG

**How it works:** Upload documents -> embed them into vectors -> at query time, retrieve relevant chunks -> LLM synthesizes an answer from retrieved fragments.

**Pros:**
- No maintenance required -- just upload and query
- Works well for single-document lookup
- Well-established tooling and infrastructure
- Good for one-off questions against a static corpus

**Cons:**
- LLM rediscovers knowledge from scratch on every question
- No accumulation of understanding across sessions
- Subtle questions requiring synthesis across multiple sources are hit-or-miss
- Nothing is built up over time
- The corpus degrades as more documents are added (noise increases)

**Used by:** NotebookLM, ChatGPT file uploads, most RAG systems, enterprise knowledge bases.

## LLM Wiki

**How it works:** LLM reads sources -> writes a structured wiki of interlinked pages -> updates the wiki when new sources arrive -> queries are answered from the wiki, not raw sources.

**Pros:**
- Knowledge compounds over time
- Cross-references already exist
- Contradictions are flagged, not ignored
- Synthesis reflects everything read so far
- Good answers can be filed back as permanent pages
- Maintenance burden shifts from human to LLM

**Cons:**
- Requires more upfront structure and convention
- Benefits emerge gradually, not immediately
- Needs periodic linting to prevent drift
- Small wikis don't benefit as much from the compounding effect

**The fundamental difference:** RAG is a retrieval strategy. The wiki is a knowledge structure. RAG asks "what in my documents relates to this question?" The wiki asks "what does my accumulated knowledge say about this question?"

## When to Use Each

| Scenario | RAG | Wiki |
|---|---|---|
| Quick lookup against static docs | Yes | Overkill |
| Deep topic research over weeks/months | No | Yes |
| Team knowledge base that needs staying current | Degrades over time | Yes |
| Personal knowledge management | Poor | Yes |
| One-off document analysis | Yes | Overkill |
| Competitive intelligence tracking | No | Yes |
| Reading a book (building understanding as you go) | No | Yes |

## Can They Work Together?

Yes. The wiki could use RAG as one of its tools:
- New source arrives -> wiki update (primary flow)
- User asks a question not covered by existing wiki pages -> RAG against raw sources -> answer gets filed as a new wiki page
- Lint pass identifies a data gap -> RAG searches the web -> results add to existing pages

The wiki is the persistent memory; RAG is a fallback for out-of-coverage queries.

## Related
- [[llm-wiki-pattern]] -- The wiki approach
- [[hermes-agent]] -- Platform where both approaches can be implemented

## Sources
- [Karpathy's LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
