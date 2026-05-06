---
title: "Atomic Notes Beat Monolithic Research Files"
source_url: ""
ingested: 2026-05-01
sha256: 8f88f3a98e9cf6b0f4aabe57c05105a5be767caaef4caa4cb0c5b9bc28a63cc7
---

# Atomic Notes Beat Monolithic Research Files

_Pattern from claude-obsidian memory stack analysis._

## The Pattern

Break long research files into linked pieces. Each note captures one idea, composable and searchable independently.

Instead of one 174 line analysis.md:
- `agency-agents-is-a-prompt-library-not-a-framework.md`
- `deliverable-templates-improve-sub-agent-output.md`
- `success-metrics-in-prompts-enable-self-evaluation.md`

## When to Atomize

The test: "Would this note be useful on its own?"

Good candidates: research findings, pattern descriptions, concept definitions, lessons learned.

Bad candidates: specs (need length for completeness), guides (sequential by nature), configs and reference docs where the category name IS the point.

## Why It Works for Agents

- Semantic search returns the relevant note, not the whole document
- Each note loads only the context needed, saving tokens
- Notes compose: link three atomic notes to build a new argument
- Easier to update one idea without touching unrelated content

## Related

- [prose-titles-make-search-results-meaningful.md](prose-titles-make-search-results-meaningful.md)
- [memory-is-an-operating-system-for-attention.md](memory-is-an-operating-system-for-attention.md)
