---
title: "Multi-Agent Coordination"
tags: [finding, multi-agent, orchestration, patterns, hierarchy, blackboard]
related:
- agent-native-operations
- kanban-doctrine
- agent-factory-production-system
- centaur-principle
- multi-agent-coordination-patterns
source: research/raw/multi-agent-coordination.md
ingested: 2026-05-07
---
# Multi-Agent Coordination

A survey of four coordination patterns for multi-agent systems: hierarchical (orchestrator + workers), peer-to-peer (debate/discussion), blackboard (shared workspace), and market-based (task bidding).

## Key Points

**Hierarchical (Orchestrator + Workers).** One agent decomposes tasks and delegates to specialists. Workers report back; orchestrator synthesizes. Examples: AutoGen's GroupChat, CrewAI hierarchical, Claude Code's spawn sub-agent. Tradeoffs: clear authority, global context maintained, workers can be specialized; but orchestrator is a bottleneck, context grows with worker count, workers lack global context. Assessment: dominant pattern because it maps to how human organizations work. The orchestrator doesn't need to be smartest; it needs to be best at decomposition and synthesis.

**Peer-to-Peer (Debate / Discussion).** Agents communicate as equals with no central authority. Examples: Society of Mind, multi-agent debate, ChatDev role-playing. Tradeoffs: no single point of failure, diverse perspectives reduce groupthink; but convergence is not guaranteed, expensive (N agents x M rounds), hard to debug, sycophancy problem. Assessment: interesting for factual accuracy, not practical for most workflows. Works better when agents have genuinely different information, not just different roles.

**Blackboard (Shared Workspace).** Agents monitor a common workspace, contribute when they can, and read others' contributions. Examples: shared file systems, databases, git repos as coordination medium. Tradeoffs: decoupled, asynchronous, auditable, flexible; but coordination is implicit, conflicts when multiple agents modify same thing, no guaranteed ordering. Assessment: underrated. Our git-based workspace is essentially a blackboard. Sub-agents write to files, main agent reads them. Scales better than hierarchical for loosely coupled work.

**Market-Based (Task Bidding).** Tasks posted as jobs with criteria; agents bid based on capabilities. Examples: model routing (Anthropic, OpenRouter), Mixture of Experts at model level. Tradeoffs: optimal allocation, scales well, self-organizing; but complex infrastructure, overkill for most systems, assumes accurate self-assessment. Assessment: appealing metaphor but premature. Model routing is the practical version.

**Current architecture: hierarchical + blackboard hybrid.** Main agent spawns sub-agents (hierarchical). Sub-agents write to git repo; main agent reads and synthesizes (blackboard). This combines the clarity of hierarchy with the decoupling of shared workspace.

## Relevance

The Agent Factory's executive layer maps to the orchestrator pattern. The Substrate is the blackboard. Understanding the tradeoffs helps calibrate when to use each pattern.

## Related

- [[agent-native-operations]] -- Executive layer design
- [[kanban-doctrine]] -- Pull-based work assignment as coordination
- [[agent-factory-production-system]] -- Factory as orchestrated system
