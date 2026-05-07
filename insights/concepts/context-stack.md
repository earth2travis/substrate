---
title: 'The Context Stack: Portable Identity for Agents'
tags:
- concept
- context-engineering
- agent-identity
- specification
- conscience
- standardization
related:
- agent-identity
- agent-memory
- agent-native-operations
- conscience
- rag-vs-wiki
- agentic-architecture
- memory-systems
- interchangeable-context
- the-openclaw-lesson
- context-poisoning-pattern
- memory-is-context-not-storage-obsidian-analysis
- mempalace-spatial-scoping-for-context-stack
source: research/findings/the-context-stack-spec.md
---





# The Context Stack: Portable Identity for Agents

## Overview

The Context Stack is a four-layer, markdown-based specification for representing individuals and organizations as machine-readable context. It solves the agent blindness problem: every AI agent starts with no knowledge of who it serves, what they value, where they're headed, or how they operate. By standardizing context into interchangeable files, the Stack moves skill from deployment to authorship, making agent deployment as simple as loading a directory.

## The Four Layers

| Layer | Question | Key Files |
|-------|----------|-----------|
| **Identity** | Who are you? | SOUL.md, VISION.md, VALUES.md, EXPERIENCE.md, TASTE.md |
| **Direction** | Where are you going? | OBJECTIVES.md, MISSIONS.md, INTENT.md, TODO.md |
| **Operations** | How do you work? | AGENTS.md, ROLES.md, DECISIONS.md, DESIGN.md, CONTRACT.md |
| **Intelligence** | What do you know? | skills/, research/, knowledge/, relationships/ |

## Why It Matters

**The structural parallel to interchangeable parts.** Before Eli Whitney, every musket was hand-fitted by a craftsman. The specification lived in the gunsmith's hands and died with them. Today every AI agent is a Blanc-era musket, hand-crafted by a prompt engineer whose knowledge is tacit and non-transferable. The Context Stack makes context interchangeable: mix the files in a pile, point any agent at the directory, get a working entity.

**The precondition for conscience.** The Stack provides moral knowledge (VALUES.md, CONTRACT.md), self-awareness (SOUL.md, EXPERIENCE.md), and stop criteria (CONTRACT.md hard boundaries). What it does not provide is the runtime evaluation loop: the comparison engine and signal mechanism that actively evaluates output against values. That loop is the missing piece that turns a collection of moral-sounding files into a functioning conscience.

**Agent-to-agent communication via stack exchange.** When two entities interact, they exchange curated subsets of their stacks. The handshake is "read our stack" rather than "let me tell you about us." This is the foundation for agent-native coordination without human mediation.

## Key Principles

1. **Markdown only.** No proprietary formats, no databases, no APIs required. Portability is non-negotiable.
2. **Layered loading, not monolithic.** Tier 0 loads Identity only. Tier 3 loads targeted depth. Semantic routing selects files based on task relevance.
3. **Progressive disclosure.** First paragraph as abstract. Summary section under 200 words. Full content for deep loading.
4. **Living documents.** Daily updates for TODO.md and DECISIONS.md. Yearly updates for SOUL.md and VISION.md. Stale context is worse than no context.

## Predicted Consequences

If the structural parallel to interchangeable parts holds, standardized context will produce: cost collapse (deployment drops from days to minutes), democratized access (small business with a Stack matches enterprise AI team), ecosystem explosion (specialists create and maintain specific context files), new labor dynamics (prompt engineering becomes a general professional skill), and a quality plateau (standardized agents initially worse than best hand-crafted but far better than average, with systematic improvement closing the gap).

## Connection to Agent Factory

Our own Substrate IS a Context Stack. SOUL.md, AGENTS.md, SCHEMA.md, and the knowledge graph are the Stack in practice. The question is not whether the Stack works but whether the spec is precise enough, stable enough, and adopted enough to achieve true interchangeability.

## Related

- [[agent-identity]] — Values, trust, and the SOUL.md pattern
- [[agent-memory]] — Memory architectures that extend the Stack
- [[agent-native-operations]] — Tools designed for AI-human partnership
- [[agentic-architecture]] — System design for autonomous agents
- [[memory-systems]] — Memory architectures supporting agent continuity
- [[interchangeable-context]] — Ford's revolution as structural parallel
