---
title: Prose Titles Make Search Results Meaningful
tags:
- writing
- naming
- search
- knowledge-management
- conventions
related:
- atomic-notes-beat-monolithic-research-files
- karpathy-llm-knowledge-bases
source: research/raw/prose-titles-make-search-results-meaningful.md
---




# Prose Titles Make Search Results Meaningful

## The Pattern

Name files with prose that captures the key insight, not category labels.

Instead of: `research/paperclip/analysis.md`
Use: `research/paperclip/paperclip-is-an-os-for-autonomous-businesses.md`

## Why It Matters

- Search results are meaningful before opening the file
- Titles become self-documenting in directory listings
- Forces the author to crystallize the key takeaway
- Browsing a folder gives you the conclusions, not just the topics

## When NOT to Use Prose Titles

- Specs and reference docs: `SPEC.md`, `SKILL.md` are better as category names
- Config files: the format IS the name
- Daily logs: date-based naming is correct (`2026-03-27.md`)
- Files that will be programmatically referenced

## The Test

Can someone browsing the directory tell what you concluded without opening the file? If yes, the title works. If no, it is a category label masquerading as a title.

## Connection to Atomic Notes

Prose titles and atomic notes reinforce each other. A prose title forces the atomic note to have a single claim. An atomic note gives the prose title something specific to name. Together they make the knowledge base browsable and searchable.
