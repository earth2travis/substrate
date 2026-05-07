---
title: "Multi-Agent Coordination Patterns"
tags: [concept, multi-agent, orchestration, hierarchy, blackboard, patterns]
related: [[agent-native-operations]], [[subagent-architecture]], [[kanban-doctrine]], [[agent-factory-production-system]]
---

# Multi-Agent Coordination Patterns

The architectural patterns for coordinating multiple agents toward shared goals.

## Four Core Patterns

**Hierarchical (Orchestrator + Workers).** One agent decomposes tasks and delegates to specialists. Workers report back; orchestrator synthesizes and decides next steps. This is the dominant pattern because it maps to how human organizations work. The orchestrator doesn't need to be the smartest agent; it needs to be the best at decomposition and synthesis. Tradeoffs: clear authority and global context, but orchestrator is a bottleneck and workers lack global context.

**Blackboard (Shared Workspace).** Agents monitor a common workspace, contribute when they can, and read others' contributions. No direct agent-to-agent communication. Git repositories are the canonical blackboard: versioning, conflict detection, full audit trail. This pattern scales better than hierarchical for loosely coupled work. Tradeoffs: decoupled and asynchronous, but coordination is implicit and conflicts require resolution.

**Peer-to-Peer (Debate / Discussion).** Agents communicate as equals with no central authority. Examples: multi-agent debate, Society of Mind, role-playing agents. Tradeoffs: diverse perspectives reduce groupthink, but convergence is not guaranteed, communication is expensive, and LLM sycophancy undermines genuine debate. Works best when agents have genuinely different information, not just different roles.

**Market-Based (Task Bidding).** Tasks posted as jobs; agents bid based on capabilities. Best-fit agent gets assigned. Model routing (using different models for different task complexities) is the practical version of this pattern. Tradeoffs: optimal allocation and self-organizing, but complex infrastructure and assumes accurate self-assessment. Premature for most systems.

## Hybrid Architecture

The most robust systems combine patterns. Our current architecture is hierarchical + blackboard hybrid: the main agent spawns sub-agents (hierarchical), sub-agents write to git repo, main agent reads and synthesizes (blackboard). This combines the clarity of hierarchy with the decoupling of shared workspace.

The through-line across all patterns: "Writes stay single-threaded; additional agents contribute intelligence." Multiple agents inject intelligence at every stage (planning, coding, review) while keeping final decision-making cohesive.

## When to Use Which

- Use **hierarchical** when tasks have clear decomposition and the orchestrator can maintain global context.
- Use **blackboard** when work is loosely coupled, asynchronous, and benefits from audit trail.
- Use **peer-to-peer** when factual accuracy is critical and agents have genuinely different knowledge.
- Use **market-based** when task complexity varies widely and model routing is the primary concern.

## Connection to Other Concepts

- [[agent-native-operations]] -- Executive layer as orchestrator
- [[subagent-architecture]] -- Sub-agent spawn and configuration
- [[kanban-doctrine]] -- Pull-based work assignment
- [[agent-factory-production-system]] -- Factory as coordinated system
