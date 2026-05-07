---
title: "Gap Analysis: Our Memory System vs the Obsidian Stack"
tags: [finding, memory, obsidian, comparison, agent-memory]
related:
- agent-memory
- context-stack
- knowledge-graphs-as-agent-memory-substrate
source: research/raw/gap-analysis-our-memory-vs-obsidian-stack.md
ingested: 2026-05-07
---
# Gap Analysis: Our Memory System vs the Obsidian Stack

A structured comparison between the Substrate Context Stack and the Claude+Obsidian agent memory stack popularized by community practitioners.

## Key Points

**Where Substrate is ahead.** SOUL.md provides deep, evolving personality (they have nothing equivalent). GOALS.md embeds values and mission in the boot sequence. AGENTS.md covers full workflow, handoffs, and audits. USER.md and emotional context in handoffs provide relational depth. GitHub Issues as external knowledge store.

**Where Obsidian stack is ahead.** MEMORY.md discipline: under 200 lines as a routing doc only. Topic-based memory (debugging.md, patterns.md, architecture.md) vs daily files. Knowledge graph with linked atomic notes and semantic search via MCP. Prose titles ("memory graphs beat giant files.md") vs category names. Automated ingestion pipeline for video/audio/articles. Self-improving graph where agents notice contradictions and propose changes.

**What NOT to adopt.** Obsidian-specific tooling (our memory_search already does semantic search). Wikilinks syntax (standard markdown links work). Over-engineering (test one improvement at a time before restructuring everything).

**The lesson.** Patterns matter, not the tool. The routing pattern (small index pointing to detailed topic files) is the transferable insight. A monolithic memory file that grows unbounded is a failure mode regardless of the tool.

## Relevance

The gap analysis reveals that Substrate's strength is depth (identity, values, process, relational context), while the Obsidian stack's strength is structure (routing, atomic notes, ingestion, self-improvement). Both approaches are converging on the same insight: memory is an operating system for attention.

## Related

- [[agent-memory]] -- Agent memory architecture concept
- [[context-stack]] -- Layered agent memory system
- [[knowledge-graphs-as-agent-memory-substrate]] -- Knowledge graphs as memory
