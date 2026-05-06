---
title: "MemPalace Spatial Scoping for the Context Stack: Structure as Intelligence"
tags: [agent-memory, spatial-scoping, context-engineering, knowledge-graphs, memory-systems]
related:
  - [[mempalace-analysis]]
  - [[knowledge-graphs-as-agent-memory-substrate]]
  - [[the-context-stack-spec]]
  - [[memory-systems]]
  - [[context-stack-as-conscience]]
source: research/raw/mempalace-spatial-scoping-for-context-stack.md
---

# MemPalace Spatial Scoping for the Context Stack: Structure as Intelligence

## Summary

Extracted insights from MemPalace code analysis applied to the Context Stack architecture. MemPalace's claimed 34% retrieval boost is actually metadata scoping: narrowing search from "Whole Palace" to a specific Wing (Project/Person) and Room (Topic). The Context Stack already has this structure in its discrete files and directories. The four key insights are: (1) Structure is a form of intelligence; treat research/, memory/, and decisions/ as Wings to guide the agent's attention. (2) The "Closet" as a semantic front door; build semantic closets (300-word summaries) for complex research files so the agent only opens the drawer (reads the full file) when necessary. (3) Graph-backed conscience vs. disconnected facts; the Context Stack must have an active Conscience Layer that cross-references against CONTRACT.md and VALUES.md before presenting context. (4) Avoiding the AAAK trap; never use lossy abbreviation for core memory. Compaction must be intent-preserving, with high-fidelity summaries capturing the why and how, not just the what.

## Key Claims

1. **MemPalace proves structure is a form of intelligence.** The spatial metaphor provides a clear, explainable way to navigate memory. The Context Stack should explicitly adopt this scoping logic.

2. **Semantic Closets keep wake-up costs low.** A 300-word summary of a 10,000-word benchmark analysis keeps token budgets manageable while preserving high-fidelity access when needed.

3. **The Conscience Layer must be active, not passive.** Before presenting any context, cross-reference against CONTRACT.md and VALUES.md. Conflicting facts must be flagged as "Unreliable" before reaching the human principal.

4. **Intent-preserving compaction is non-negotiable.** Lossy abbreviation (AAAK) degrades retrieval quality by 12.4 percentage points. Semantic compression by an agent captures the why and how.

5. **Transparency is the differentiator.** In a field full of performance laundering, the Agent Factory must be brutally honest about what its components do.

## Implications

The Context Stack can adopt MemPalace's scoping logic while improving its semantic fidelity and conscience integration. Research/, memory/, and decisions/ are already Wings. We need to add Semantic Closets (summaries) as front doors, wire the Conscience Layer into retrieval, and ensure all compaction is intent-preserving. The result: a Context Stack that is both efficient and ethically robust.

## Related

- [[mempalace-analysis]] — Full analysis of MemPalace's performance laundering gaps
- [[knowledge-graphs-as-agent-memory-substrate]] — Graph-based memory for relational reasoning
- [[the-context-stack-spec]] — The Context Stack as the structural layer
- [[memory-systems]] — Memory architectures supporting agent continuity
- [[context-stack-as-conscience]] — Moral architecture requiring active conscience
