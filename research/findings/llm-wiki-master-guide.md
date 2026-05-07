---
title: "LLM Wiki Master Guide: Karpathy's Pattern and Implementations"
tags: [research, llm-wiki, knowledge-management, obsidian]
related: [rag-vs-wiki, llm-wiki-pattern, knowledge-graphs-as-agent-memory-substrate, agent-native-operations, context-compression]
source: "Community compilation, April 2026"
---

# LLM Wiki Master Guide: Karpathy's Pattern and Implementations

## Summary

The LLM Wiki is not a RAG system. It is a persistent, compiled knowledge artifact sitting between raw sources and queries. Raw files stay immutable; the LLM actively summarizes, synthesizes, interlinks, and maintains a clean wiki layer. At personal scale (~400k tokens), vector DB often unnecessary: smart indexing + LLM bookkeeping suffice.

## Key Concepts

**Core Operations (Three Commands):**
1. Ingest: drop file into raw/, LLM summarizes into wiki/ pages, creates backlinks, appends to log.md, refreshes index.md
2. Query: ask against wiki/ only (not raw), returns synthesized answer + inline citations
3. Lint/Health Check: monthly or on-demand, fixes orphans, broken links, stale facts, duplicates, confidence decay

**Canonical Structure:**
```
vault/
├── raw/              # Immutable originals
├── wiki/             # LLM-generated, human-editable
│   ├── index.md      # Master catalog
│   ├── log.md        # Chronological history
│   ├── entities/
│   └── concepts/
├── CLAUDE.md         # Schema, rules, agent instructions
└── obsidian/         # Optional IDE
```

**v2 Advanced Practices:**
- Memory lifecycle: confidence scores (0-1), supersession, retention curves, forgetting
- Typed knowledge graph: entities + typed relationships (PERSON → founded → COMPANY)
- Hybrid search: BM25 on filenames + titles + graph + optional embeddings
- Event hooks: auto-ingest on file drop, periodic lint cron, audit trail
- Token efficiency: Graphify-style claims use 71.5x fewer tokens than raw RAG
- Multi-agent: separate research agent vs personal memory agent

**Major Implementations:**
Karpathy Original Gist (manual), God of Prompt Guide (prompt library), Farzapedia (400+ pages), Graphify (CLI tool), Hermes-Agent Skill (`/llm-wiki`), lucasastorian/llmwiki (web app), Astro-Han/karpathy-llm-wiki (Claude Code skill), MehmetGoekce/llm-wiki (L1/L2 cache), rohitg00 LLM Wiki v2 (memory lifecycle + typed graph).

## Applications

Plain Markdown + Git = portable, versioned, file-over-app. Obsidian/Logseq as IDE with graph view and backlinks. Community shipped production tools in under 72 hours after Karpathy's post. Pattern still evolving. [[rag-vs-wiki]] [[llm-wiki-pattern]] [[agent-native-operations]]
