---
title: Agentic Workflows Landscape (March 2026)
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/workflows-landscape.md
---

# Agentic Workflows Landscape (March 2026)

## The Field

Five frameworks dominate agent orchestration. Each embodies a different philosophy about how agents should collaborate. The choice is architectural destiny: it determines your failure modes, your scaling ceiling, and your operational costs.

## Framework Analysis

### OpenAI Symphony (March 2026)

Symphony is not a general orchestration framework. It is a **daemon that turns issue trackers into agent work queues**. Released March 2026, open source.

**Architecture:**
- Polls Linear (or similar tracker) for issues in a "Ready for Agent" state
- Creates deterministic, isolated per-issue workspaces
- Runs a coding agent session per issue with bounded concurrency
- Policy lives in-repo as WORKFLOW.md (YAML frontmatter + prompt template)
- Agent writes back to tracker (state transitions, PR links, comments)

**What works:**
- Clean separation: Symphony schedules/runs, agents do the work
- Per-issue workspace isolation prevents cross-contamination
- WORKFLOW.md means teams version their agent behavior with their code
- Exponential backoff for transient failures, restart recovery without persistent DB
- Handoff states (e.g., "Human Review") rather than forcing completion

**What doesn't:**
- Only handles issue-shaped work. Not a general orchestrator.
- No built-in multi-agent coordination within a single task
- Linear-specific in current spec (though abstraction layers exist)

**Key insight:** Symphony treats agents as workers on a factory floor. The orchestration is external (issue tracker), not internal (agent-to-agent). This is the simplest architecture that actually works in production.

### OpenAI Swarm / Assistants API

The "gateway framework." Everyone starts here. Most leave.

**Architecture:**
- Unified stack: model, memory (threads), tools (code interpreter, file search) under one roof
- Swarm provides lightweight agent-to-agent handoff (baton-passing)
- State managed by OpenAI (opaque)

**What works:**
- Time-to-value is unmatched. Working multi-agent system in 30 minutes
- Tool ecosystem (code interpreter, file search) is polished
- Good for proving concepts

**What doesn't:**
- Black box state management. When agents fail, diagnosing why is nearly impossible
- Vendor lock-in. Can't route tasks to local models to save costs
- Conversational handoff patterns are too vague for deterministic business logic
- Cost: long-running agents on GPT-5 get expensive fast

**Key insight:** Perfect prototyping environment, poor production foundation. The "OpenAI Ceiling" is real.

### LangGraph (LangChain)

The architect's framework. Most complex, most control.

**Architecture:**
- **State graphs**: Nodes are functions, edges are transitions, state is a typed shared object
- Each node reads state, does work, writes state updates, returns next destination
- Checkpointing for failure recovery and time-travel debugging
- Built-in human-in-the-loop patterns (interrupt nodes that pause for input)
- LangSmith for observability

**What works:**
- Full control over execution flow. Every transition is explicit
- State is raw data, prompts formatted on-demand (clean separation)
- Error taxonomy: transient failures get retries, LLM-recoverable errors loop back with context, user-fixable problems pause for input
- Checkpointing means you can resume from any point after a crash
- Multi-agent coordination through subgraphs

**What doesn't:**
- Steep learning curve. "Thinking in graphs" is not natural for most developers
- Boilerplate-heavy for simple workflows
- LangChain ecosystem dependency (though LangGraph can be used standalone)
- Overengineered for straightforward pipelines

**Key insight:** LangGraph is the right choice when you need deterministic, auditable workflows with complex branching. It's the wrong choice when you need to move fast or the workflow is simple.

### CrewAI

The pragmatist's choice. Role-based agent teams.

**Architecture:**
- Agents defined by role, goal, and backstory
- Tasks assigned to agents with expected outputs
- Sequential or hierarchical crew execution
- Built-in delegation between agents

**What works:**
- Intuitive mental model: "I need a researcher, a writer, and an editor"
- Fastest path from idea to working multi-agent workflow
- Role-based abstraction maps well to business processes
- Good for content pipelines, research workflows, reporting

**What doesn't:**
- Limited control over execution flow compared to LangGraph
- Role definitions are prompt engineering in disguise (fragile)
- Debugging multi-agent interactions is difficult
- Scaling beyond 5-7 agents becomes unwieldy
- Less mature error recovery

**Key insight:** CrewAI wins when the problem naturally decomposes into human-like roles. It loses when you need fine-grained control or deterministic behavior.

### Microsoft AutoGen (v0.4/v0.5)

"Conversation as computing." Everything is a chat.

**Architecture:**
- Event-driven in newer versions (moving away from pure chat)
- User Proxy and Assistant patterns for code-write-execute-debug loops
- Group chat for multi-agent collaboration
- Docker sandboxing for code execution

**What works:**
- Unmatched for exploratory, non-linear problem solving
- Code-write-execute-debug loops are still best-in-class
- Good for R&D and creative problem exploration
- AutoGen Studio provides no-code team building

**What doesn't:**
- "Conversational Chaos": agents get stuck in politeness loops or infinite debugging
- "Token Bleeding": failed tasks can cost hundreds of dollars before anyone notices
- State management across 10+ agents is a headache
- Too unpredictable for high-stakes deterministic workflows

**Key insight:** AutoGen is a research tool, not a production framework. Use it when you don't know the steps. Don't use it when you need reliability.

## Orchestration Patterns

### State Machines vs DAGs vs Dynamic Planning

**State machines** (LangGraph): Best for workflows with clear states and transitions. Deterministic, auditable, recoverable. Overhead is justified when reliability matters.

**DAGs** (CrewAI sequential, Airflow-style): Best for pipelines where steps are known ahead of time. Simple mental model. Falls apart when you need conditional branching.

**Dynamic planning** (AutoGen, Swarm): Best for exploration. The agent decides what to do next. Maximum flexibility, minimum predictability. Production-hostile without guardrails.

**The emerging consensus (2026):** Hybrid approaches win. Use state machines for the outer orchestration (what happens when), dynamic planning for inner execution (how an agent accomplishes its assigned step). Symphony exemplifies this: static orchestration (poll tracker, assign work, manage lifecycle) with dynamic agent execution inside each workspace.

### Error Recovery Patterns

1. **Retry with backoff** (transient failures): Network errors, rate limits. Every framework supports this.
2. **Loop back with context** (LLM-recoverable): Feed the error message back to the agent. LangGraph does this elegantly.
3. **Human escalation** (user-fixable): Pause execution, surface to human. LangGraph's interrupt nodes. Symphony's handoff states.
4. **Circuit breakers** (budget protection): Kill the run after N failures or $X spent. Critical for AutoGen. Under-implemented everywhere.
5. **Checkpoint and resume** (crash recovery): LangGraph's checkpointing. Symphony's restart recovery.

### Human-in-the-Loop

The spectrum from most to least human involvement:

1. **Approval gates**: Human approves before each action (LangGraph interrupt nodes)
2. **Review and edit**: Agent produces draft, human modifies (Symphony's "Human Review" state)
3. **Exception handling**: Human only involved when agent fails or is uncertain
4. **Audit trail**: Agent acts autonomously, human reviews after the fact
5. **Full autonomy**: No human involvement (dangerous, cost-risky)

**What works in practice:** Exception handling (#3) with audit trails (#4). Approval gates (#1) are too slow for most workflows. Full autonomy (#5) bleeds money.

## What Synthweave/Loom Should Use

1. **Symphony's architecture for the outer loop**: Issue/task-driven orchestration. Work comes from a queue, gets isolated workspaces, runs with bounded concurrency. This is proven.

2. **LangGraph-style state graphs for complex inner workflows**: When an agent's task involves multiple steps with branching logic, use explicit state machines. Not LangGraph itself (too much ecosystem baggage), but the pattern.

3. **Handoff states over forced completion**: Agents should be able to say "I need a human" or "this requires a different agent." Model this as state transitions, not failures.

4. **Circuit breakers everywhere**: Token budgets, time limits, retry caps. Non-negotiable for production.

5. **Skip CrewAI's role abstraction**: It's prompt engineering with extra steps. Define agents by their tools and permissions, not their "backstory."

6. **Skip AutoGen's conversation-as-computing**: Too unpredictable. Use structured state instead.
