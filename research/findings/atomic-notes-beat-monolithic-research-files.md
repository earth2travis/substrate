---
title: Atomic Notes Beat Monolithic Research Files
tags:
- note-taking
- knowledge-management
- atomicity
- writing
- agents
related:
- prose-titles-make-search-results-meaningful
- rag-vs-wiki
- agent-memory
- karpathy-llm-knowledge-bases
source: research/raw/atomic-notes-beat-monolithic-research-files.md
---




# Atomic Notes Beat Monolithic Research Files

The pattern: break long research files into linked pieces, each capturing one idea, composable and searchable independently.

## The Test

"Would this note be useful on its own?"

Good candidates: research findings, pattern descriptions, concept definitions, lessons learned.

Bad candidates: specs (need length for completeness), guides (sequential by nature), configs where the category name IS the point.

## Why It Works for Agents

- Semantic search returns the relevant note, not the whole document
- Each note loads only the context needed, saving tokens
- Notes compose: link three atomic notes to build a new argument
- Easier to update one idea without touching unrelated content

## Contrast with Monoliths

A 174-line `analysis.md` forces the reader to scan the entire file for the relevant insight. Three atomic files let the reader grab exactly what they need and link the rest.

The monolith optimizes for the author's convenience. The atomic note optimizes for the reader's search.

## When Monoliths Still Win

Specs need completeness. Guides need sequence. Reference docs need the category name. Daily logs need chronology. The question is not "always atomic" but "atomic by default, monolithic when justified."

## Connection to Our Practice

Our `findings/` directory follows this pattern: each file is one finding, one insight, one claim. The `insights/` directory is the composition layer: concepts that emerge from the intersection of multiple findings.

This is the atomic principle applied recursively. Raw is atomic at the source level. Findings are atomic at the insight level. Concepts are atomic at the pattern level.
