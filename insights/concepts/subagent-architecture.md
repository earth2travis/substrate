---
title: "Sub-Agent Architecture"
tags: [concept, sub-agent, orchestrator, model-tiering, generator-critic, multi-agent]
related: [[agent-native-operations]], [[agent-memory]], [[context-stack]], [[kanban-doctrine]], [[centaur-principle]], [[institutional-ai-redesign]]
---

# Sub-Agent Architecture

The design patterns for spawning, configuring, and coordinating sub-agents within a multi-agent system.

## The Core Problem

Sub-agents are typically treated as anonymous temp workers: same model, same context, no identity, no quality gates. The industry has converged on the opposite: named specialists with defined roles, tiered models matched to task complexity, and generator-critic pairs for quality.

The OpenClaw infrastructure already supports all of this. The gap is organizational, not technical.

## Seven Design Principles

**1. Named Specialists.** Every sub-agent should have an identity: role, goal, voice, and task-specific instructions. Anonymous agents produce generic output because they lack orientation. Named agents with agent-specific AGENTS.md files produce output that matches the system's tone and standards.

**2. Model Tiering.** Not every task needs the most capable model. Routine work (research extraction, file organization, linting) runs on cheaper/faster models. Complex reasoning (creative writing, architectural decisions) escalates to the most capable model. The default should be the cheaper model; escalation should be explicit.

**3. Orchestrator Pattern.** A two-level nesting (main agent -> orchestrator -> leaf workers) allows parallel work without making the main agent the bottleneck. The orchestrator fans out to workers, synthesizes their output, and announces the combined result. Depth limits prevent runaway recursion.

**4. Generator-Critic (Jidoka).** For quality-critical work, use two agents: one generates, one reviews. This is the jidoka principle (self-inspection) implemented as a multi-agent pattern. The critic catches what the generator misses due to instruction bias or context overload.

**5. Rich Task Prompts.** Since sub-agents don't get the full identity stack (SOUL.md, USER.md, IDENTITY.md), the task prompt must carry everything: what to do, voice/style, output location, quality expectations, conventions, relevant file links. The prompt is the interface contract.

**6. Timeouts and Resource Limits.** Sub-agents need bounded execution: run timeouts, token limits, and concurrency caps. Without limits, a stuck sub-agent blocks slots indefinitely. The system degrades silently until all slots are occupied.

**7. Context Injection Awareness.** Sub-agents only receive what the platform injects. If the platform omits identity documents, the sub-agent is anonymous. If the platform omits user preferences, the sub-agent produces generic output. The task prompt must compensate for whatever the platform does not provide.

## The Specialist Roster

A mature multi-agent system defines specialists by capability, not by name:

- **Researcher:** Deep extraction, source analysis. Cheap model. Parallelizable.
- **Writer:** Creative output, transmissions, blog posts. Capable model. Sequential.
- **Auditor:** Code review, PR checks, quality gates. Cheap model. Must be independent.
- **Builder:** Code generation, skill creation, scripts. Medium model. Tool-heavy.
- **Ops:** Infrastructure, monitoring, cron tasks. Cheap model. Restricted tools.

Each specialist gets its own workspace, tool restrictions, and model assignment. The orchestrator routes tasks to the right specialist based on task type and complexity.

## Connection to Other Concepts

- [[agent-native-operations]] -- Executive layer and spawn patterns
- [[agent-memory]] -- What sub-agents get vs what they need
- [[context-stack]] -- Context injection and identity documents
- [[kanban-doctrine]] -- Pull-based assignment for specialist agents
- [[centaur-principle]] -- Process design as differentiator in multi-agent systems
- [[institutional-ai-redesign]] -- Sub-agent architecture as organizational redesign
