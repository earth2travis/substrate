---
title: "LlamaIndex Workflows: Event-Driven Agent Orchestration"
tags: [finding, multi-agent, event-driven, orchestration, typescript]
related:
- agent-native-operations
- agent-factory-production-system
- kanban-doctrine
source: research/raw/llamaindex-event-driven-orchestration.md
ingested: 2026-05-07
---
# LlamaIndex Workflows: Event-Driven Agent Orchestration

An event-driven, step-based orchestration framework for AI applications that replaced LlamaIndex's previous DAG-based system. Open source Python.

## Key Points

**Why DAGs were abandoned.** Three explicit reasons: loops and branches encoded in graph edges made them hard to read; data passing between DAG nodes created complexity around optional/default values; DAGs didn't feel natural to developers building complex, branching AI applications.

**Core primitives: Workflow, Step, Event.** A Workflow is a Python class. Steps are methods decorated with `@step` that receive an event and emit an event. Events are Pydantic models carrying data between steps. StartEvent and StopEvent mark entry and exit. Steps declare input/output types via Python type hints. The framework infers the execution graph automatically. No manual wiring.

**Steps don't know about each other.** They only know about events. Adding a new step that handles a new event type doesn't require modifying existing steps. This is composability by design.

**Key features.** Type-inferred validation: broken workflows caught at build time. Concurrent execution: steps handling different event types run in parallel automatically. Checkpointing: save and restore workflow state mid-execution. Human-in-the-loop: first-class support for pausing, collecting input, resuming. Context/state: shared mutable state across steps via Context object.

**Patterns worth adopting.**
1. Events as the orchestration primitive: more composable than explicit dispatch.
2. Type safety as workflow validation: catch broken workflows before they cost API credits.
3. Steps, not agents, as unit of work: a step can be an LLM call, tool invocation, human checkpoint, or full agent.
4. Implicit concurrency from event graph: concurrency emerges from data dependencies, not from a configuration knob.
5. Checkpointing and human-in-the-loop: exactly the pattern needed for approval gates.

**Patterns to not adopt.** Python-only implementation (our stack is TypeScript/Node). LlamaParse/LlamaCloud lock-in (the open source framework is the value; hosted platform is their business model).

## Relevance

The Agent Factory's orchestration layer can adopt event-driven patterns without adopting Python. The core insight (events as contracts, type safety, checkpointing) transfers to any stack.

## Related

- [[agent-native-operations]] -- Coordination layer design
- [[agent-factory-production-system]] -- Production system patterns
- [[kanban-doctrine]] -- Pull-based assignment vs event-driven routing
