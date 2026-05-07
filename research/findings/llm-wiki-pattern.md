---
title: "LLM Wiki Pattern: Persistent Compounding Knowledge Base"
tags: [agent, memory, knowledge, tools, research]
related:
- hermes-agent
- nous-research
- karpathy-llm-knowledge-bases
- rag-vs-wiki
- memex
source: research/raw/llm-wiki-pattern.md
---
# LLM Wiki Pattern: Persistent Compounding Knowledge Base

## Summary

A persistent, compounding knowledge base maintained by LLMs as interlinked markdown files, instead of re-deriving answers from raw sources on each query. Pioneered by Andrej Karpathy and adopted by dozens of implementations within 72 hours.

## Architecture

Three layers:

1. **Raw Sources** — Immutable. LLM reads but never modifies.
2. **The Wiki** — LLM-generated markdown: summaries, entities, concepts, comparisons.
3. **The Schema** — Configuration telling the LLM how the wiki is structured.

## Operations

- **Ingest**: Drop source → LLM processes → updates 10-15 wiki pages
- **Query**: Search relevant pages → synthesize with citations
- **Lint**: Periodic health check for contradictions, orphans, stale claims

## Advanced Patterns

- Confidence scoring per fact (0-1) with timestamps
- Supersession: newer sources deprecate old ones
- Retention curves: outdated info naturally fades
- Typed knowledge graph: entities + typed relationships
- Hybrid search: BM25 + graph traversal + optional embeddings
- Self-healing: auto-ingest, periodic lint cron, audit trail

## Community Implementations

| Implementation | Focus |
|----------------|-------|
| Karpathy Original | Pure markdown, copy-paste agent prompt |
| Graphify | `pip install graphify`: zero-to-wiki in one command |
| Hermes-Agent Skill | Built-in `/llm-wiki <topic>` or `hermes update` |
| llmwiki.app | Full web app for non-technical users |
| MehmetGoekce/llm-wiki | Two-layer cache + Obsidian/Logseq support |

## Why It Works

The tedious part of knowledge management is not reading or thinking, it is bookkeeping: updating cross-references, keeping summaries current, noting contradictions. Humans abandon wikis because maintenance burden grows faster than value. LLMs do not get bored.

## Related

- [[hermes-agent]] — Bundles LLM wiki as a skill
- [[nous-research]] — Organization behind Hermes
- [[karpathy-llm-knowledge-bases]] — Gap analysis vs existing systems
- [[rag-vs-wiki]] — Comparison with traditional RAG
- [[memex]] — Vannevar Bush's original associative trails vision
