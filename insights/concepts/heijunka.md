---
title: "Heijunka"
tags: [concept, lean, scheduling, toyota, agent-factory, mura]
related: [[toyota-production-system]], [[lean-doctrine]], [[kanban-doctrine]], [[just-in-time]], [[agent-native-operations]]
source: research/findings/heijunka-for-agent-orchestration.md
---

# Heijunka

## Definition

Heijunka (平準化) is the practice of production leveling: smoothing out volume and variety of work over time to reduce unevenness (Mura), overburden (Muri), and waste (Muda). Instead of producing in large batches based on sporadic orders, Heijunka averages production across a fixed period.

## The Heijunka Box

The primary visual tool is a grid-based scheduling board:
- **Rows:** product types or agent roles
- **Columns:** fixed time intervals (hours, days, shifts)
- **Cards:** small, leveled tasks signaling exactly what should be produced and when

The critical shift is interleaving: instead of "All research Monday, all coding Tuesday," the schedule alternates types to keep every line warm and ready.

## Volume vs. Product Leveling

1. **Volume Leveling:** distribute total work evenly across days to prevent stop-and-start cycles
2. **Product Leveling:** distribute different work types evenly to minimize changeover pain

Toyota targets changeovers under three minutes. For agents, the equivalent is context-switch cost.

## Application to Agent Orchestration

Agents and humans both suffer from batching: research for days, then code for days, creating Mura. The antidote:
- **Interleave work types:** Strategy, Code, Strategy, Code keeps all cognitive lines active
- **Level shared memory:** distribute outputs rather than dumping large blocks that create bottlenecks
- **Define takt time:** the rate at which insights or features must be produced to satisfy demand without overburden

The Heijunka Box can be implemented in GitHub Projects or markdown: rows for agents (Strategy, Execution, Review), columns for daily intervals, cards as small distributed tasks.

## Connection to Lean

Heijunka is the scheduling complement to Just-in-Time (make what is needed) and Jidoka (stop on defects). Without leveling, JIT creates spikes and valleys. With leveling, flow becomes sustainable.

## Related

- [[toyota-production-system]] -- The system that originated Heijunka
- [[lean-doctrine]] -- Philosophical foundation
- [[kanban-doctrine]] -- Pull-based work management
- [[just-in-time]] -- Demand-triggered production
- [[agent-native-operations]] -- Human-AI workflow design
