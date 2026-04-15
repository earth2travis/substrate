---
title: "Karpathy LLM Knowledge Bases"
created: 2026-04-13
updated: 2026-04-13
type: entity
tags: [person, product, research]
sources:
  - raw/karpathy-llm-knowledge-bases.md
---

# Karpathy LLM Knowledge Bases

## Overview

Andrej Karpathy's April 2, 2026 X/Twitter post describing a personal knowledge base architecture where LLMs are the primary operators of a markdown wiki. This is the companion piece to his [LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), focusing on the product insight and gap analysis.

## Key Observation

The closing line: **"I think there is room here for an incredible new product instead of a hacky collection of scripts."**

## Gap Analysis: Karpathy's Pattern vs Existing Systems

The post includes a detailed gap analysis between Karpathy's vision and his current team's system:

| Gap | Status |
|---|---|
| **`raw/` directory for source material** | Missing. Research goes directly to `research/` as processed files -- sources are lost after extraction |
| **LLM compiles wiki from raw** | Partial. LLM extraction exists but no automated compilation step |
| **Auto-maintained index files** | Close. Tiered memory (L0/L1/L2) serves similar function but isn't auto-maintained |
| **Backlinks between articles** | Major gap. 167 research files with no cross-referencing |
| **Q&A against the wiki** | Broken. `memory_search` non-functional due to missing OpenAI embedding key |
| **Output feeds back into wiki** | Partial. Not systematic |
| **Linting / health checks** | Missing. No wiki-level consistency checking |

## Priority Fixes Identified

1. **Fix memory_search** -- Single highest-leverage fix; enables Q&A against the corpus
2. **Auto-index research directory** -- `research/INDEX.md` summarizing every file, maintained automatically
3. **Cross-referencing / backlinking** -- Lint pass identifying related files, adding "Related" sections
4. **Research linting cron** -- Periodic checks for inconsistencies, outdated info, missing links, coverage gaps
5. **Raw capture discipline** -- Keep raw versions of sources (URL + date accessed)
6. **Output-feeds-back loop** -- Formalize where exploration answers get filed
7. **Visualization layer** -- Topic map showing which topics are deep, which are thin, how they connect

## Connection to Context Stack

Karpathy's architecture maps to the Context Stack spec's Intelligence layer (`knowledge/` directory):
- `raw/` = raw Intelligence
- Compiled wiki = processed Intelligence
- Index files = routing layer within Intelligence
- Q&A = semantic routing

The key difference: Karpathy treats the LLM as sole maintainer; the Zookooree system treats LLM as co-maintainer. Karpathy's "you rarely ever write or edit the wiki manually" is worth considering for the research directory specifically.

## Product Insight

The gap between Karpathy's vision and the existing system is: the structure (Context Stack) and the agents (Factory) exist, but the **compilation pipeline** that turns raw sources into a maintained, interlinked, queryable wiki was the missing piece.

This is exactly what the [[llm-wiki-pattern]] now delivers.

## See Also
- [[llm-wiki-pattern]] -- The compilation pipeline Karpathy was envisioning
- [[llm-wiki-pattern]] -- The original LLM Wiki gist
- [[nous-research]] -- Hermes Agent includes LLM wiki as a bundled skill
- [[github-as-memory]] -- Complementary knowledge system for operational memory
