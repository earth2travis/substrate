---
title: "Heijunka for Agent Orchestration"
tags: [finding, lean, agent-factory, heijunka, scheduling, mura]
related:
- lean-doctrine
- kanban-doctrine
- toyota-production-system
source: research/raw/heijunka-for-agent-orchestration.md
ingested: 2026-05-07
---
# Heijunka for Agent Orchestration

Heijunka, or production leveling, applies directly to agent orchestration. The core problem: agents and humans both suffer from batching work (research for days, then code for days), which creates Mura (unevenness) and imposes a setup-time penalty at every context switch.

## Key Points

**Interleaving reduces cognitive load.** Alternating strategy and execution (Strategy, Code, Strategy, Code) keeps all lines of thought warm and active, reducing the total cognitive burden compared to large sequential blocks.

**The Heijunka Box as project board.** A leveled schedule can be implemented in GitHub Projects or markdown: rows represent agents (Sivart/Strategy, Koda/Execution, Ξ2T/Review), columns represent daily intervals, and cards are small, distributed tasks rather than monolithic blocks like "Build Loom."

**Takt Time for agents.** Defining the rate at which strategic insights or shipped features must be produced prevents Muri (overburden). The customer is the human operator; the takt time is their sustainable absorption rate.

**Leveling shared memory.** Dumping large research outputs all at once creates bottlenecks for downstream agents. Heijunka dictates distributing inputs: one strategic spec per day, one code spec per day, keeping the shared nervous system flowing smoothly.

## Relevance

The feast-or-famine cycle of startup and agent work is not a capacity problem; it is a scheduling problem. Heijunka provides the antidote: predictable, flexible, sustainable flow.

## Related

- [[lean-doctrine]] -- Waste elimination and flow maximization
- [[kanban-doctrine]] -- Pull-based work assignment
- [[toyota-production-system]] -- Historical origin of Heijunka
