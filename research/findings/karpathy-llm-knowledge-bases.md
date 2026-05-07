---
title: "Karpathy: LLM Knowledge Bases"
tags: [agents, knowledge-management, wiki, obsidian, automation, llm]
related:
  - [[rag-vs-wiki]]
  - [[agent-memory]]
  - [[context-stack]]
  - [[automation-leverage]]
  - [[synthesis-vs-retrieval-paradigm]]
source: research/raw/karpathy-llm-knowledge-bases.md
---

# Karpathy: LLM Knowledge Bases

**Source:** https://x.com/karpathy/status/2039805659525644595
**Author:** Andrej Karpathy, April 2026

## Architecture

Karpathy describes a knowledge base where LLMs are the primary operators of a markdown wiki, not humans. The human curates sources and asks questions. The LLM compiles, maintains, indexes, lints, and enhances.

### 1. Data Ingest

Raw sources indexed into `raw/`. LLM incrementally compiles into a wiki: summaries, backlinks, categorization, interlinked concept articles.

**Tooling:** Obsidian Web Clipper for converting web articles. Hotkey to download images locally for LLM reference.

### 2. IDE Layer

Obsidian as viewing frontend. **Critical point: the LLM writes and maintains all wiki data. The human rarely touches it directly.**

### 3. Q&A Against the Wiki

At scale (~100 articles, ~400K words), the LLM researches complex questions. Karpathy expected to need "fancy RAG" but found the LLM handles it by auto-maintaining index files and brief summaries.

### 4. Output as Wiki Enrichment

**Explorations and query outputs get filed back into the wiki.** Every question enriches the knowledge base for future queries. The system compounds.

### 5. Linting / Health Checks

LLM "health checks" over the wiki: find inconsistent data, impute missing data, find interesting connections, suggest new article candidates.

### 6. Extra Tools

Vibe-coded tools for processing data. Example: naive search engine over the wiki, usable directly and as CLI tool for the LLM.

### 7. Future Direction

Synthetic data generation + finetuning to embed knowledge into model weights rather than relying solely on context windows.

## The Gap Analysis

Karpathy's pattern maps to our system with gaps:

| Karpathy's Pattern | Our Current System | Gap? |
|---|---|---|
| `raw/` directory for source material | No formal raw ingest | **Yes.** We skip raw capture. |
| LLM compiles wiki from raw | We write research files directly | **Partial.** No automated compilation |
| Auto-maintained index files | MEMORY.md, tiered memory | **Close.** Not auto-maintained |
| Backlinks between articles | No backlinking | **Yes.** 167 files, no cross-referencing |
| Q&A against the wiki | `memory_search` broken | **Yes.** Missing capability |
| Output feeds back into wiki | Manual, not systematic | **Partial.** |
| Linting / health checks | GitHub issue checks only | **Yes.** No wiki-level linting |
| Obsidian as viewer | Cursor for viewing | **Different.** Git-native vs Obsidian-native |

## The Product Insight

"I think there is room here for an incredible new product instead of a hacky collection of scripts."

Our Context Stack + Agent Factory could become exactly this. The spec describes the structure. The factory produces agents that maintain it. The skills encode how to compile, lint, and query. What Karpathy does manually with scripts is what we are trying to systematize.

The missing piece: the compilation pipeline that turns raw sources into a maintained, interlinked, queryable wiki. That pipeline is the gap between his vision and our system.
