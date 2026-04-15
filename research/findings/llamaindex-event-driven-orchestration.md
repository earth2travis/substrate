---
title: "LlamaIndex Workflows: Event-Driven Agent Orchestration"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/llamaindex-event-driven-orchestration.md
---

# LlamaIndex Workflows: Event-Driven Agent Orchestration
## Source: llamaindex.ai/blog/llamaagents-builder + developers.llamaindex.ai/python/llamaagents/workflows/
## Analyzed: 2026-03-10

## What It Is

LlamaIndex Workflows is an event-driven, step-based orchestration framework for AI applications. It replaced their previous DAG-based system. Open source Python framework.

## Why They Abandoned DAGs

Three explicit reasons from their docs:
1. Loops and branches encoded in graph edges made them hard to read
2. Data passing between DAG nodes created complexity around optional/default values
3. DAGs didn't feel natural to developers building complex, branching AI applications

## The Architecture

### Core Primitives
- **Workflow**: A Python class that subclasses `Workflow`
- **Step**: A method decorated with `@step` that receives an event and emits an event
- **Event**: A Pydantic model that carries data between steps
- **StartEvent / StopEvent**: Special events for workflow entry and exit

### How Routing Works
Steps declare their input/output types via Python type hints. The framework infers the execution graph automatically. No manual wiring.

```python
class JokeFlow(Workflow):
    @step
    async def generate_joke(self, ev: StartEvent) -> JokeEvent:
        # StartEvent triggers this step
        return JokeEvent(joke=response)

    @step
    async def critique_joke(self, ev: JokeEvent) -> StopEvent:
        # JokeEvent triggers this step automatically
        return StopEvent(result=critique)
```

Steps don't know about each other. They only know about events. Adding a new step that handles a new event type doesn't require modifying existing steps.

### Key Features
- **Type-inferred validation**: Broken workflows caught at build time (emit an event no step handles = error)
- **Concurrent execution**: Steps handling different event types run in parallel automatically
- **Checkpointing**: Save and restore workflow state mid-execution
- **Human-in-the-loop**: First-class support for pausing, collecting input, resuming
- **Context/state**: Shared mutable state across steps via Context object

## LlamaAgents Builder

Natural language -> generated Workflow Python code -> deployed. "Vibe coding" for agent workflows.

Currently limited to document extraction workflows only (classification, routing, extraction). The generated code is real Python using the open source Workflows framework. Can deploy to LlamaParse managed infrastructure or self-host.

**Assessment**: The Builder is a nice demo but the value is in the Workflows framework underneath. The Builder is a code generation UI; the Workflows framework is the actual architectural contribution.

## Patterns Worth Adopting

### 1. Events as the Orchestration Primitive
**Current Loom approach**: Orchestrator explicitly dispatches tasks to agents by name/role.
**LlamaIndex approach**: Define event types as contracts. Steps emit events. The right handler picks them up.

**Why this is better**: More composable. Adding new capabilities doesn't require modifying the orchestrator. New steps just handle new event types. The orchestrator doesn't need to know the full graph.

### 2. Type Safety as Workflow Validation
**Current Loom approach**: No build-time validation of workflow definitions.
**LlamaIndex approach**: Type annotations on steps create a compile-time check. Emit an event nobody handles? Fail before running.

**Application to Loom**: If agents declare what event types they emit and consume, we can validate entire pipelines at definition time. Catch broken workflows before they cost API credits.

### 3. Steps, Not Agents, as Unit of Work
**Current Loom approach**: Hard boundary between orchestrator and agent. Agents are heavyweight.
**LlamaIndex approach**: A step can be a single LLM call, a tool invocation, a human checkpoint, or a full agent. The abstraction is flat.

**Implication**: The orchestrator/agent boundary in Loom might be unnecessary overhead. A "step" that happens to spawn a Claude Code session is just a step, not a fundamentally different concept.

### 4. Implicit Concurrency from Event Graph
**Current Loom approach**: `max_concurrent: 3` as a global setting.
**LlamaIndex approach**: Steps that handle independent events run in parallel automatically.

**Why this is better**: Concurrency emerges from the data dependencies, not from a configuration knob. If two steps need different events that are both available, they run concurrently. No tuning needed.

### 5. Checkpointing and Human-in-the-Loop
First-class support for pausing a workflow, serializing state, collecting human input, and resuming. Exactly the pattern needed for approval gates.

## Patterns to NOT Adopt

### Python-only
The Workflows framework is Python-native. Our stack is TypeScript/Node. The patterns transfer; the implementation doesn't.

### LlamaParse/LlamaCloud Lock-in
The Builder deploys to their managed infrastructure. The open source framework is the value; the hosted platform is their business model.

### Over-abstraction
The Workflow class + Event system adds framework overhead. For simple orchestration (dispatch task, get result), it's heavier than our current approach. The event pattern pays off when workflows are complex (branches, loops, concurrent paths). Don't adopt it for simple linear pipelines.

## Comparison to Other Orchestration Approaches

| Dimension | LlamaIndex Workflows | LangGraph | Symphony/Loom | CrewAI |
|-----------|---------------------|-----------|---------------|--------|
| Orchestration model | Event-driven steps | State machine graphs | Orchestrator dispatch | Role-based delegation |
| Routing | Type-inferred | Explicit edges | Orchestrator decides | Manager agent |
| Concurrency | Implicit from events | Explicit branching | Config-based | Sequential default |
| Validation | Build-time type check | Runtime | None currently | None |
| Human-in-loop | First-class | Supported | Planned | Limited |
| Complexity | Medium | High | Low | Low |

## Bottom Line

The event-driven pattern is the most important architectural idea here. It's cleaner than orchestrator-dispatches-to-agents for complex workflows. If Loom agents communicate through typed events instead of direct commands, the system becomes more composable, testable, and extensible.

The LlamaAgents Builder is marketing on top of a solid engineering foundation. The foundation (Workflows framework) is worth studying deeply. The Builder is interesting as a product concept (natural language -> deployed workflow) but limited in current form.
