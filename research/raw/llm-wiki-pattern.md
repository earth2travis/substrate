---
title: LLM Wiki Pattern
created: 2026-04-08
updated: 2026-04-09
type: concept
tags: [agent, memory, tools, research]
sources: [raw/articles/karpathy-llm-wiki-pattern.md, raw/2026-04-08-llm-wiki-master-guide.md]
---

# LLM Wiki Pattern

> A persistent, compounding knowledge base maintained by LLMs as interlinked markdown files, instead of re-deriving answers from raw sources on each query.

## Core Idea

Most people use RAG: upload files, retrieve chunks at query time, generate answers. The LLM rediscovers knowledge from scratch each time.

The LLM Wiki pattern is different. Instead of retrieving from raw documents, the LLM **builds and maintains a persistent wiki** of structured, interlinked markdown files. When a new source arrives:

- The LLM reads it and extracts key information
- Integrates it into the existing wiki
- Updates entity pages, revises topic summaries
- Notes contradictions between new and old claims
- Strengthens the evolving synthesis

The knowledge is compiled once and kept current, not re-derived.

## Architecture

Three layers:

**Raw Sources** -- Immutable. The LLM reads from them but never modifies them. Source of truth.

**The Wiki** -- LLM-generated markdown files. Summaries, entity pages, concept pages, comparisons. The LLM owns this layer entirely. Creates, updates, maintains cross-references, keeps everything consistent.

**The Schema** -- Configuration document (e.g. SCHEMA.md) that tells the LLM how the wiki is structured, conventions, and workflows. Co-evolved by user and LLM.

## Operations

### Ingest
Drop a new source in, tell the LLM to process it. The LLM reads the source, discusses takeaways with the user, writes summary pages, updates relevant entity/concept pages, flags contradictions, updates the index, appends to the log. Single source can touch 10-15 wiki pages.

### Query
Ask questions against the wiki. The LLM searches relevant pages, reads them, synthesizes answers with citations. Good answers can be filed back into the wiki as new pages so explorations compound.

### Lint
Periodic health-check for contradictions, stale claims, orphan pages, missing cross-references, and data gaps. Keeps the wiki healthy as it grows.

## Special Files

**index.md** -- Content-oriented catalog of everything in the wiki. Each page listed with link, one-line summary, organized by category. Updated on every ingest.

**log.md** -- Chronological, append-only record of what happened and when. Consistent prefixes make it parseable with unix tools.

## Division of Labor

The human's job: curate sources, direct analysis, ask good questions, think about what it all means.

The LLM's job: summarizing, cross-referencing, filing, bookkeeping, maintenance.

The tedious part of a knowledge base is not reading or thinking -- it's the bookkeeping. Updating cross-references, keeping summaries current, noting contradictions. Humans abandon wikis because maintenance burden grows faster than value. LLMs don't get bored.

## Memory Lifecycle and Advanced Patterns

From community implementations (v2 evolution, rohitg00 + others):

- **Confidence scoring**: Every fact gets a score (0-1) and last-updated timestamp
- **Supersession**: Newer/better sources automatically deprecate old ones
- **Retention curves**: Low-confidence or outdated info naturally fades
- **Consolidation tiers**: Atomic facts → synthesized concepts → high-level narratives
- **Typed knowledge graph**: Entities + typed relationships (e.g., `PERSON → founded → COMPANY`) with graph traversal during queries
- **Hybrid search**: For large vaults (>100 pages), BM25 on filenames/titles + graph traversal + optional local embeddings
- **Self-healing**: Auto-ingest on file drop, periodic lint cron, audit trail in log.md
- **Token efficiency**: Graphify-style claims: **71.5x fewer tokens** vs raw RAG; L1/L2 caching layers (MehmetGoekce)

### Gotchas & Anti-Patterns
- Never query raw files directly after the first ingest
- Avoid over-fragmentation (too many tiny pages)
- Hallucination compounding: always cite the exact wiki file
- Scale ceiling: when >10k pages, add hybrid vector search (but keep Markdown as source of truth)

## Community Implementations

The LLM Wiki pattern spawned dozens of implementations within 72 hours of Karpathy's post:

- **Karpathy Original Gist** -- Pure Markdown, copy-paste agent prompt. The baseline.
- **Graphify** -- `pip install graphify`: one-command vault from any folder (code + PDFs + images). Fastest zero-to-wiki.
- **Hermes-Agent Skill** -- Built-in `/llm-wiki <topic>` or `hermes update` — auto web + code research for agents.
- **lucasastorian/llmwiki** -- Full web app with hosted demo at llmwiki.app. Non-technical users.
- **yologdev/karpathy-llm-wiki** -- "yoyo" agent that auto-grows the repo every few hours. Hands-off experimentation.
- **MehmetGoekce/llm-wiki** -- Two-layer cache (L1/L2) + Obsidian + Logseq support. Performance-focused.
- **atomicmemory/llm-wiki-compiler** -- Pure "compilation" mode. Advanced users.

Community variants also include blink-query, sage-wiki, quicky-wiki, PhD research vaults, codebase wikis, business-intel vaults, and local-LLM versions.

## Tools and Integrations

- **Obsidian** -- Best way to browse the wiki. Graph view shows connections, wikilinks render as clickable links.
- **Obsidian Web Clipper** -- Converts web articles to markdown. Quick source ingestion.
- **qmd** -- Local search for markdown files with BM25/vector search and LLM re-ranking. Can run as CLI or MCP server.
- **Marp** -- Markdown-based slide deck format. Generate presentations from wiki content.
- **Dataview** -- Obsidian plugin that runs queries over page frontmatter for dynamic tables/lists.

## Why It Resonates

Related to Vannevar Bush's Memex (1945) -- a personal, curated knowledge store with associative trails between documents. The part Bush couldn't solve was who does the maintenance. The LLM handles that.

## Connection to GitHub as Memory

The wiki pattern and the [[github-as-memory]] pattern are complementary: the wiki compounds research knowledge from raw sources; the knowledge graph compounds operational memory from work artifacts. The wiki is the *what we know*; the graph is the *what we've decided/done*.

The [[karpathy-llm-knowledge-bases]] document (a raw source) provides a detailed gap analysis between Karpathy's pattern and existing organizational systems, identifying backlinking, auto-indexing, and research linting as the key missing pieces — exactly the functions the wiki delivers.

## Related
- [[obsidian]] -- Primary wiki browsing interface
- [[karpathy-llm-knowledge-bases]] -- Detailed gap analysis of LLM wiki pattern vs existing systems
- [[nous-research]] -- Hermes Agent includes LLM wiki as a bundled skill
- [[github-as-memory]] -- Complementary: operational memory graph vs research wiki

- [[llm-wiki-pattern]] (this page)
- [[rag-vs-wiki]] -- Comparison with traditional RAG
- [[memex]] -- Vannevar Bush's original vision for associative document trails

## Related
- [[process-without-substance]] -- Process philosophy synthesis mapped onto AI architecture

## Sources
- [Karpathy's LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
