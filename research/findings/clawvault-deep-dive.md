---
title: "ClawVault Deep Dive"
tags: [finding, memory, agent-memory, clawvault, knowledge-graph]
related: [[agent-memory]], [[context-stack]], [[knowledge-graphs-as-agent-memory-substrate]], [[memory-systems]]
source: research/raw/clawvault-deep-dive.md
ingested: 2026-05-07
---

# ClawVault Deep Dive

ClawVault is an open-source agent memory system (TypeScript, MIT, 173 GitHub stars) that implements typed markdown documents with auto-inferred categories and a knowledge graph extracted from wiki-links.

## Key Points

**Typed document model.** 14 predefined categories: decisions, preferences, rules, patterns, people, projects, goals, lessons, commitments, handoffs, tasks, backlog, research, transcripts. Each document is markdown with YAML frontmatter including priority (red/yellow/green), tags, and related links.

**Observation scoring.** Content is parsed with confidence and importance scores (0-1), or legacy emoji priority (red=critical, yellow=notable, green=background). Type inference uses regex patterns on content: "decided" infers decision, "prefer" infers preference, "committed" infers commitment.

**Knowledge graph extracted from links.** Documents connect via wiki-links, tags, and frontmatter relations. The graph index stores nodes (id, title, type, category, degree) and edges (source, target, link type). The graph emerges organically from natural writing rather than requiring explicit construction.

**Context profiles for task types.** Default, planning, incident, and handoff profiles load different memory subsets based on trigger keywords. This enables budget-aware injection: load high-priority first, then fill remaining context with lower priority.

**Session lifecycle.** Wake (start, load context), checkpoint (save progress mid-session), sleep (end with summary and next steps). Designed for OpenClaw hook integration.

**Benchmark insight.** File-based markdown (74.0%) outperformed specialized tools (68.5%) on LoCoMo long-term conversational memory. LLMs are trained on text, not database schemas.

## Relevance

ClawVault validates several Substrate design choices: file-based storage, typed frontmatter, wiki-link graphs, and priority-weighted context loading. It also shows diminishing returns: our simpler MEMORY.md covers 80% of the value with 20% of the complexity.

## Related

- [[agent-memory]] -- Concept page for agent memory architecture
- [[context-stack]] -- Agent memory layering system
- [[knowledge-graphs-as-agent-memory-substrate]] -- Knowledge graphs as agent memory
