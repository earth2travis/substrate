---
title: "Kanban Doctrine: Auftragstaktik as Operating System"
tags: [concept, kanban, auftragstaktik, mission-command, operations, multi-agent]
related: [[toyota-production-system]], [[a3-thinking]], [[taiichi-ohno]], [[kanban-vs-delegate-task]], [[kanban-metadata-rules]], [[agent-native-operations]], [[centaur-principle]], [[institutional-ai-redesign]], [[subagent-architecture]], [[multi-agent-coordination-patterns]]
source: research/raw/auftragstaktik-mission-command.md
---

# Kanban Doctrine: Auftragstaktik as Operating System

## Summary

We run our agent squad on **Auftragstaktik** principles: a commander gives intent, the subordinate owns execution. Hermes Kanban is the substrate on which this philosophy runs. This insight connects Prussian military doctrine to agent operations, establishing the rules by which the squad coordinates.

## From Prussia to the Terminal

Auftragstaktik was built because rigid, top-down command fails in uncertain environments. The same is true of agent fleets.

| Auftragstaktik | Our Equivalent |
|---|---|
| Commander's Intent | The "Why" in a Kanban task body |
| Subordinate's Initiative | The worker agent choosing the right tools to solve the problem |
| The Backbrief | The worker reads the task, plans its approach, then executes |
| Disciplined Disobedience | Block if the task body is ambiguous; do not guess |
| The General Staff | The Substrate: shared knowledge, skills, and conventions |

## Why delegate_task Is Not Enough

`delegate_task` is a **function call**: synchronous, anonymous, and ephemeral. It is the right tool when one agent needs a quick sub-task inside its own context.

Kanban is a **work queue**: asynchronous, named, and durable. It is the right tool when the task has its own identity, must survive context loss, or requires human review.

The distinction is not "which is better." It is: "which shape covers the work?"

## The Doctrine: Three Rules

**Rule One: Intent Over Instruction**

Every Kanban task must state the objective and the end state, not the method. The worker chooses the path. If the method matters, that belongs in a skill, not a task.

**Rule Two: Block Before Guess**

When the fog of war descends (API changes, missing credentials, ambiguous requirements), the worker halts and escalates. A blocked task with context is more valuable than a completed task that solved the wrong problem.

**Rule Three: Handoff Is Signal**

`kanban_complete` is not "I am done." It is "Here is what happened, what changed, and what the next agent needs to know." The metadata field carries the signal.

## Related

- [[kanban-vs-delegate-task]] — Decision record on when to use each primitive
- [[kanban-metadata-rules]] — The metadata schema for squad handoffs
