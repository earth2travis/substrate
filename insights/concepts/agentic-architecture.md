---
title: "Agentic Architecture: Three-Layer Production Stack"
tags: [concept, architecture, agent, mcp, skills, workflows, orchestration]
related:
- progressive-disclosure
- agent-security
- agent-identity
- dark-factory
- harness-engineering
- ai-composable-primitives
source: research/findings/agentic-systems-synthesis.md
---
# Agentic Architecture: Three-Layer Production Stack

## Overview

Production agent systems require three distinct layers: capabilities (tools), knowledge (skills), and orchestration (workflows). Each layer answers a different question: what can I do, how should I do it, and when does work happen.

## The Three Layers

**Capability Layer (MCP Tools)**: "What can I do?" Individual capabilities discovered and executed through the Model Context Protocol. MCP is becoming the standard for tool integration. Moving toward stateless (June 2026 spec).

**Knowledge Layer (Skills)**: "How should I do it?" Procedural knowledge for composing capabilities. The Anthropic skill format is becoming the cross-platform standard. Skills are lightweight markdown files, portable and composable.

**Orchestration Layer (Workflows)**: "When and where does work happen?" Scheduling, isolation, lifecycle. Symphony's pattern: external work queue, isolated agent sessions, bounded concurrency, handoff states.

## Key Principles

**External orchestration beats internal orchestration.** Do not build complex agent-to-agent routing. Use an external work queue (issue tracker, task system) and dispatch isolated sessions. The orchestration lives in infrastructure, not in the agents.

**State machines for structure, LLMs for execution.** Use deterministic state machines for the workflow shell: what happens in what order, what are the error paths, where do humans intervene. Let LLMs handle the actual work within each state.

**Permission models are the unsolved problem.** Every framework punts on permissions. MCP says "hosts SHOULD get consent." Nobody has real per-tool policies, budget enforcement, or scope-based access control. This is the architectural opportunity: per-agent permissions, per-task budget caps, scope inheritance for sub-agents, complete audit trails.

**Stateless is the future.** MCP's move to stateless means the "hosted MCP server" model is transitional. Design for stateless from day one.

## Error Taxonomy (from LangGraph)

- **Transient**: retry
- **LLM-recoverable**: loop with additional context
- **User-fixable**: escalate to human
- **Catastrophic**: circuit break

## What to Adopt, Build, and Skip

**Adopt**: MCP for all tool integrations. Anthropic skill format. Symphony's dispatch pattern. LangGraph's error taxonomy.

**Build**: Permission and budget enforcement layer. Skill library for every recurring workflow. Stateless MCP servers.

**Skip**: CrewAI's role abstraction (define agents by capabilities, not characters). AutoGen's conversation-as-computing (too unpredictable). LangGraph as a dependency (implement the pattern directly). Framework-specific tool abstractions (go straight to MCP).

## Connection to TPS

The architecture maps to Toyota Production System principles:
- **Pull systems**: Agent work should be demand-driven, not pre-generated
- **Stop the line**: When an agent produces garbage, halt and diagnose
- **Small improvements**: Agent capabilities compound through incremental refinement
- **Problems as signals**: Every failure is information about where the system needs to improve
