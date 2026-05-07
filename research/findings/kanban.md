---
title: "Kanban: Visual Signaling for Flow Control"
tags: [lean, tps, operations, tools, project-management]
related: [[toyota-production-system]], [[just-in-time]], [[lean-production]], [[kanban-doctrine]]
source: research/raw/kanban.md
---

# Kanban: Visual Signaling for Flow Control

## Summary

Kanban (看板, "signboard") is a visual system for managing work and controlling inventory, originating from the Toyota Production System. It is the signaling mechanism that enables just-in-time production.

## How It Works

1. Each workstation has input and output areas
2. When output drops below threshold, a kanban card signals upstream
3. Upstream produces only enough to replenish what was consumed
4. This creates a pull system where production is triggered by actual demand

## Evolution

- Physical cards at Toyota factories
- Software tools (Trello, Jira) for knowledge work
- Digital boards with WIP limits and swimlanes
- Hermes Agent Kanban: agent-native task orchestration with metadata schemas

## Benefits

- Visual transparency of work and bottlenecks
- Limits work-in-progress (WIP)
- Prevents overproduction
- Self-regulating inventory system

## Connection to Agent Systems

The [[kanban-doctrine]] maps military Auftragstaktik to agent operations. Kanban is not just a board; it is a signaling protocol. In agent systems, the signal is metadata: priority, intent, blockers, and backbrief status.

## Related

- [[toyota-production-system]] — Where Kanban originated
- [[just-in-time]] — The system Kanban enables
- [[lean-production]] — The broader paradigm
- [[kanban-doctrine]] — Our operating model for agent coordination
