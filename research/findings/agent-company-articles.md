---
title: "Agent Company Articles: Patterns Worth Adopting"
tags: [agents, memory, patterns, operations]
related: [[agent-memory-architecture]], [[paperclip]]
source: research/raw/agent-company-articles.md
---

# Agent Company Articles: Patterns Worth Adopting

## Summary

Analysis of X articles describing multi-agent company architectures. Much is overengineered, but four patterns are immediately applicable.

## Patterns Worth Adopting

**1. Memory Type Taxonomy**
Organize memory by type: insights (discoveries), patterns (recurring behaviors), strategies (what works), preferences (user preferences), lessons (mistakes). Makes memory structured and retrievable.

**2. Priority-Tagged Observations**
- Critical (decisions, commitments, blockers)
- Notable (insights, preferences, context)
- Background (routine updates, low-signal)

Load high-priority first when context budget is limited.

**3. Memory Influence Probability (30%)**
Not 100% (too rigid) or 0% (useless). Memory influences behavior 30% of the time, allowing exploration. Balance between leveraging experience and trying new things.

**4. Cap Gates at Entry Point**
Check quotas BEFORE queuing tasks, not after. Prevents queue bloat.

## What's Suspicious

- Source credibility unverified (@Voxyz_ai, @sillydarket are unknown accounts)
- Closed loop pattern (Proposal → Mission → Step → Event → Proposal) may be overkill for single-agent operations
- File-based memory claims (74% vs 68.5% on LoCoMo) need independent verification

## Recommendation

Adopt memory taxonomy and priority tags immediately. Verify ClawVault claims before considering. Skip multi-agent architecture complexity.
