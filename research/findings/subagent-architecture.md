---
title: "Sub-Agent Architecture: OpenClaw, Big Labs, and Open Source"
tags: [finding, sub-agent, multi-agent, orchestrator, context-injection]
related: [[agent-native-operations]], [[agent-memory]], [[context-stack]], [[skills-as-portable-knowledge]]
source: research/raw/subagent-architecture.md
ingested: 2026-05-07
---

# Sub-Agent Architecture: OpenClaw, Big Labs, and Open Source

A survey of sub-agent patterns across OpenClaw (our platform), Anthropic, Google, and OpenAI, with practical recommendations for configuration and use.

## Key Points

**OpenClaw sub-agent capabilities.** Background agent runs spawned from an existing run. Own session, own context, own token usage. Two spawn methods: `sessions_spawn` (programmatic) and `/subagents spawn` (manual). Key parameters: task, label, agentId, model override, thinking level, runTimeoutSeconds, mode (run or session), cleanup, sandbox. Supports two levels of nesting with `maxSpawnDepth: 2`: main agent -> orchestrator sub-agent -> leaf worker.

**Critical detail: context injection.** Sub-agents only get AGENTS.md + TOOLS.md. They do NOT get SOUL.md, IDENTITY.md, USER.md, HEARTBEAT.md, or BOOTSTRAP.md. Sub-agents are anonymous workers by default. This explains why sub-agent output often feels generic and needs heavy rewriting.

**Current configuration gaps.** No named specialist sub-agents. No model tiering (everything inherits Opus). No orchestrator pattern enabled (`maxSpawnDepth` at default 1). No run timeouts configured. Two agents exist: `main` (Sivart, Opus) and `ops` (separate workspace, no browser/canvas/messaging).

**Industry convergences.**
- Anthropic: agent systems should be built around clear components (planning, tool use, reflection); orchestrator should be lightweight; agents need access to the right context at the right time.
- Google ADK: Generator-Critic loop (two agents per task, generator produces, critic reviews); explicit routing (orchestrator explicitly routes based on task type); session state persistence across turns.
- OpenAI: function calling is the primary primitive; agents are just systems with memory, tool access, and planning loops; no special framework needed beyond the API.

## Relevance

Our sub-agent infrastructure supports named specialists, model tiering, and orchestrator patterns. We have not configured them. The gap is organizational, not technical.

## Related

- [[agent-native-operations]] -- Executive layer and sub-agent spawn patterns
- [[agent-memory]] -- What sub-agents get vs what they need
- [[context-stack]] -- Context injection and SOUL.md implications
- [[skills-as-portable-knowledge]] -- Skills as the interface for specialist agents
