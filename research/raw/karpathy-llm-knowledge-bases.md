# Karpathy: LLM Knowledge Bases

**Source:** https://x.com/karpathy/status/2039805659525644595
**Author:** Andrej Karpathy
**Date:** April 2, 2026
**Extracted:** 2026-04-02

## The Pattern

Karpathy describes a personal knowledge base architecture where LLMs are the primary operators of a markdown wiki, not humans. The human curates sources and asks questions. The LLM compiles, maintains, indexes, lints, and enhances the knowledge base.

## Architecture

### 1. Data Ingest

Raw sources (articles, papers, repos, datasets, images) indexed into a `raw/` directory. LLM incrementally "compiles" this into a wiki: a collection of `.md` files in a directory structure.

The wiki includes:
- Summaries of all data in `raw/`
- Backlinks between articles
- Categorization into concepts
- Articles for each concept, interlinked

**Tooling:** Obsidian Web Clipper extension for converting web articles to `.md`. Hotkey to download related images locally for LLM reference.

### 2. IDE Layer

Obsidian as the viewing frontend. Human views raw data, the compiled wiki, and derived visualizations. **Critical point: the LLM writes and maintains all wiki data. The human rarely touches it directly.** Marp plugin for slides, other plugins for alternative views.

### 3. Q&A Against the Wiki

At scale (~100 articles, ~400K words), the LLM can research complex questions against the wiki. Karpathy expected to need "fancy RAG" but found the LLM handles it at this scale by auto-maintaining index files and brief summaries.

### 4. Output as Wiki Enrichment

Outputs render as markdown files, slide shows (Marp), or matplotlib images, all viewable in Obsidian. Key insight: **explorations and query outputs get filed back into the wiki.** Every question you ask enriches the knowledge base for future queries. The system compounds.

### 5. Linting / Health Checks

LLM "health checks" over the wiki:
- Find inconsistent data
- Impute missing data (with web searches)
- Find interesting connections for new article candidates
- Incrementally improve data integrity
- Suggest further questions to investigate

### 6. Extra Tools

Vibe-coded tools for processing data. Example: naive search engine over the wiki, usable both directly (web UI) and as a CLI tool handed to the LLM for larger queries.

### 7. Future Direction

Synthetic data generation + finetuning to embed knowledge into model weights rather than relying solely on context windows.

## Comparison to Our Workspace

| Karpathy's Pattern | Our Current System | Gap? |
|---|---|---|
| `raw/` directory for source material | No formal raw ingest. Research goes directly to `research/` as processed files | **Yes.** We skip the raw capture step. Sources are summarized inline or lost. |
| LLM compiles wiki from raw | We write research files directly, sometimes from transcripts/articles | **Partial.** We do LLM extraction (like the Figma livestream today) but no automated compilation step |
| Auto-maintained index files | `MEMORY.md` as L1 index, `memory/L0-core.md` as essential index | **Close.** Our tiered memory (L0/L1/L2) serves a similar function but isn't auto-maintained by a compile step |
| Backlinks between articles | No backlinking. Research files are standalone | **Yes.** Major gap. 167 research files with no cross-referencing |
| Q&A against the wiki | `memory_search` (broken, OpenAI key missing) | **Yes.** This is exactly the capability we're missing and feeling the pain of |
| Output feeds back into wiki | We do this manually (research informs decisions, memory files) | **Partial.** Not systematic |
| Linting / health checks | `scripts/memory-health-check.sh` for GitHub issues. No wiki-level linting | **Yes.** No consistency checking across research files |
| Obsidian as viewer | Ξ2T uses Cursor for file viewing. No dedicated wiki viewer | **Different approach.** Our files are git-native, not Obsidian-native |
| Compounding knowledge | landscape.md tracks themes. Connection-making in HEARTBEAT.md | **Partial.** We have the intention but not the mechanism |

## What We Should Change

### High Priority

**1. Fix memory_search.** This is the Q&A layer and it's been broken. The OpenAI embedding key needs to be restored. Without it, we can't query our own 167 research files or 55 memory files. This is the single highest-leverage fix. Karpathy's whole pattern depends on being able to ask questions against the corpus.

**2. Auto-index research directory.** Create an index file (`research/INDEX.md`) that summarizes every research file with one-line descriptions. Maintain it automatically (cron or on-commit). This is Karpathy's "brief summaries" pattern that lets the LLM find relevant material without reading everything.

### Medium Priority

**3. Cross-referencing / backlinking.** Our 167 research files don't reference each other. A linting pass that identifies related files and suggests links would increase the value of the corpus significantly. Not full Obsidian-style wikilinks, but a "Related" section at the bottom of each file.

**4. Research linting cron.** A periodic job that checks for: inconsistencies across files, outdated information, files that should reference each other but don't, and gaps in coverage. This is Karpathy's "health check" pattern applied to our wiki.

**5. Raw capture discipline.** When we ingest a source (transcript, article, tweet), keep the raw version somewhere (even just a reference URL + date accessed). Right now, the raw material is lost after extraction.

### Lower Priority

**6. Output-feeds-back loop.** Formalize the pattern where explorations enrich the knowledge base. When we research a question, the answer should be filed in a discoverable location, not just in a daily memory note or chat transcript.

**7. Visualization layer.** We don't need Obsidian specifically, but a way to see the shape of our knowledge (which topics are deep, which are thin, how they connect) would be valuable. Could be a simple script that generates a topic map.

## Connection to Context Stack

Karpathy's architecture maps to our Context Stack spec's Intelligence layer (`knowledge/` directory). His `raw/` is raw Intelligence. His compiled wiki is processed Intelligence. His index files are the routing layer within Intelligence. His Q&A is semantic routing.

The key difference: Karpathy treats the LLM as the sole maintainer of the wiki. We treat the LLM (me) as a co-maintainer with Ξ2T. Both are valid, but his pattern of "you rarely ever write or edit the wiki manually" is worth considering for our research directory specifically.

## The Product Insight

Karpathy's closing line: "I think there is room here for an incredible new product instead of a hacky collection of scripts."

This is exactly what the Context Stack + Agent Factory could become. The spec describes the structure. The factory produces agents that maintain it. The skills encode how to compile, lint, and query. What Karpathy is doing manually with scripts is what we're trying to systematize.

The gap between his vision and our system is: we have the structure (Context Stack) and the agents (Factory), but we don't yet have the compilation pipeline that turns raw sources into a maintained, interlinked, queryable wiki. That pipeline is the missing piece.
