---
title: "Synthesis: Agentic Systems for Synthweave/Loom (March 2026)"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/agentic-systems-synthesis.md
---

# Synthesis: Agentic Systems for Synthweave/Loom (March 2026)

## The Three Layers

After surveying the landscape across workflows, tools, and skills, one architecture emerges clearly:

```
┌─────────────────────────────────────────┐
│  Orchestration Layer (Workflows)        │
│  Symphony-style: task queues, isolation, │
│  bounded concurrency, handoff states    │
├─────────────────────────────────────────┤
│  Knowledge Layer (Skills)               │
│  Anthropic-format: progressive          │
│  disclosure, MCP tool orchestration,    │
│  portable procedural knowledge          │
├─────────────────────────────────────────┤
│  Capability Layer (Tools)               │
│  MCP: standardized tool discovery,      │
│  execution, auth. Moving to stateless.  │
└─────────────────────────────────────────┘
```

Each layer answers a different question:
- **Tools (MCP)**: "What can I do?" Individual capabilities.
- **Skills**: "How should I do it?" Procedural knowledge for composing capabilities.
- **Workflows**: "When and where does work happen?" Scheduling, isolation, lifecycle.

## Five Key Insights

### 1. External orchestration beats internal orchestration

Symphony's insight is profound: don't build complex agent-to-agent routing. Instead, use an external work queue (issue tracker, task system) and dispatch isolated agent sessions. The orchestration is in the infrastructure, not in the agents.

This maps directly to how we already work. Our issue tracker, workspace isolation, bounded concurrency via sub-agents: we're already doing Symphony's architecture informally. Loom should formalize it.

### 2. State machines for structure, LLMs for execution

The 2026 consensus: use deterministic state machines for the workflow shell (what happens in what order, what are the error paths, where do humans intervene) and let LLMs handle the actual work within each state. LangGraph proved the pattern; Symphony operationalized it.

Don't let agents decide the workflow. Let them execute within it.

### 3. Skills are the missing middleware

MCP gives you tools. Workflows give you scheduling. But between "I can query a database" and "process this customer request" there's a knowledge gap: the procedural expertise of knowing which tools to use in what order with what error handling.

Skills fill this gap. They're lightweight (markdown files), portable (cross-platform), and composable (multiple skills can coexist). The Anthropic format is becoming standard. Use it.

### 4. Permission models are the unsolved problem

Every framework punts on permissions. MCP says "hosts SHOULD get consent." LangGraph has interrupt nodes. CrewAI assigns tools to agents. Nobody has real per-tool policies, budget enforcement, or scope-based access control.

This is our opportunity. Build it right from the start:
- Per-agent tool permissions (read/write/execute)
- Per-task budget caps (tokens and dollars)
- Scope inheritance for sub-agents
- Complete audit trails

### 5. Stateless is the future

MCP moving to stateless (June 2026 spec). The "hosted MCP server" business model is on borrowed time as complexity simplifies to REST-like patterns. Design for stateless from day one.

## Recommendations for Synthweave/Loom

### Adopt

- **MCP** for all tool integrations. It's the standard. Don't fight it.
- **Anthropic Skill format** for reusable procedural knowledge. Already cross-platform.
- **Symphony's architectural pattern** for work dispatch: external queue, isolated workspaces, bounded concurrency, handoff states.
- **LangGraph's error taxonomy**: transient (retry), LLM-recoverable (loop with context), user-fixable (escalate), catastrophic (circuit break).

### Build

- **Permission/budget enforcement layer**: The gap in the market. Per-tool policies, per-task budgets, audit trails.
- **Skill library**: Every recurring workflow as a skill. Deployment, research, review, debugging.
- **Stateless MCP servers**: Prepare for the June 2026 spec now.

### Skip

- **CrewAI's role abstraction**: It's prompt engineering with extra steps. Define agents by capabilities, not characters.
- **AutoGen's conversation-as-computing**: Too unpredictable for production. Use structured state.
- **LangGraph as a dependency**: The pattern is great. The LangChain ecosystem dependency is not. Implement the state graph pattern directly.
- **Framework-specific tool abstractions**: LangChain's `@tool`, CrewAI's tool classes. Go straight to MCP.

### Watch

- **MCP Apps**: Full applications as MCP servers. Could change how we think about tool composition.
- **MCP Sampling with tool support**: Server-initiated LLM calls that can use tools. Enables server-side workflow orchestration.
- **Agent AI Foundation**: Now governs MCP, Skills, agents.md. Will likely define future standards.
- **Stateless MCP adoption**: Timeline and ecosystem readiness through 2026.

## The Architecture We Should Build

```
Issue Tracker / Task Queue
         │
         ▼
┌──────────────────────┐
│  Loom Orchestrator    │  Symphony-pattern daemon
│  - Polls for work     │  
│  - Creates workspaces │  
│  - Manages lifecycle  │  
│  - Budget enforcement │  
└──────┬───────────────┘
       │ per-task
       ▼
┌──────────────────────┐
│  Agent Session        │  Isolated workspace
│  - Loads relevant     │  
│    Skills             │  
│  - Connects to MCP   │  
│    servers            │  
│  - Executes with      │  
│    permission scope   │  
│  - Reports completion │  
│    or handoff         │  
└──────────────────────┘
       │
       ▼
  MCP Servers (tools)
  Skills (knowledge)
  State graph (workflow logic within task)
```

This is not a framework. It's an architecture. The components are simple, the interfaces are standard (MCP, Skills format, issue tracker APIs), and each piece can evolve independently.

The key differentiator from existing frameworks: we're not building another CrewAI or LangGraph. We're building the operational layer that makes agents actually work in production, with the permission model and budget enforcement that nobody else has built yet.
