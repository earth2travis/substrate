---
title: "LLM Wiki Pattern: Compounding Knowledge Base"
tags: [concept, memory, knowledge, agent, tools, pattern]
related:
- rag-vs-wiki
- agent-memory
- knowledge-graphs-as-agent-memory-substrate
- memex
- living-project-graph
- synthesis-over-retrieval
- per-run-learning
source: research/findings/llm-wiki-pattern.md
---

# LLM Wiki Pattern: Compounding Knowledge Base

## Thesis

The LLM wiki pattern replaces re-deriving answers from raw sources on every query with persistent, interlinked markdown maintained by the LLM itself. Raw sources are immutable. The wiki is the accumulated understanding. This is not search; it is memory that compounds.

## Architecture

Three layers:

1. **Raw Sources** — Immutable inputs. The LLM reads but never modifies.
2. **The Wiki** — LLM-generated markdown: summaries, entities, concepts, comparisons.
3. **The Schema** — Configuration telling the LLM how the wiki is structured and linted.

## Operations

- **Ingest**: Drop source → LLM processes → updates 10-15 wiki pages
- **Query**: Search relevant pages → synthesize with citations
- **Lint**: Periodic health check for contradictions, orphans, stale claims

## Why It Works

The tedious part of knowledge management is not reading or thinking. It is bookkeeping: updating cross-references, keeping summaries current, noting contradictions. Humans abandon wikis because maintenance burden grows faster than value. LLMs do not get bored.

## Substrate as Implementation

The `_ingest.py → findings → insights` pipeline is the wiki pattern in production. Raw sources compile into durable, cross-referenced knowledge. Every finding links to at least two others. Every concept traces to a source. The graph grows denser, not noisier, with each addition.

## Related

- [[rag-vs-wiki]] — Architectural comparison with retrieval-augmented generation
- [[agent-memory]] — Broader memory system taxonomy
- [[knowledge-graphs-as-agent-memory-substrate]] — Graph topology for wiki navigation
- [[synthesis-over-retrieval]] — Why accumulated understanding beats search
