---
title: "OpenAI Frontier"
tags: [finding, openai, frontier, entity, harness-engineering, dark-factory]
related: [[harness-engineering]], [[codex]], [[dark-factory]]
source: research/raw/openai-frontier.md
ingested: 2026-05-07
---

# OpenAI Frontier

The Frontier team at OpenAI, led by Ryan Lopopolo, working on the most advanced applications of AI agents. Responsible for harness engineering and dark factory research.

## Key Points

**Extreme Harness Engineering.** Building autonomous coding agent pipelines that process 1B+ tokens/day. The team's internal beta was built with 0 lines of manually-written code. Humans steer; agents execute.

**Dark Factory Software Pipeline.** 0 lines of human-written code, 10+ PRs/engineer/day. The product has internal daily users and external alpha testers. It ships, deploys, breaks, and gets fixed entirely by Codex agents.

**Symphony Orchestration.** Multi-agent workflow system built on Elixir/BEAM backbone. Handles agent spawning, task routing, and result aggregation at scale.

**Key insight: the scarce resource is human time.** Every design decision optimized for preserving human attention. Agents handle execution; humans provide direction, review, and judgment. The constraint is not compute or code generation but human cognitive capacity.

## Relevance

The Frontier team's work validates the Agent Factory thesis from the inside of OpenAI. Their constraint (no human-written code) forced them to build the scaffolding, feedback loops, and agent legibility patterns that define harness engineering.

## Related

- [[harness-engineering]] -- Core research area on agent scaffolding
- [[codex]] -- The primary agent model used by the Frontier team
- [[dark-factory]] -- Lights-out manufacturing as model for agent operations
