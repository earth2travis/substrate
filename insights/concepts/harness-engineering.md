---
title: "Harness Engineering"
tags: [concept, agent, development, operations, architecture, codex, ai]
related: [[dark-factory]], [[codex]], [[symphony-orchestrator]], [[lean-software-development]], [[kanban-doctrine]], [[chief-engineer-system]], [[obeya]], [[production-paradigms]], [[shusa-applied-zookooree]], [[lean-software-delivery]], [[cloudflare-first-agent-factory]], [[the-openclaw-lesson]], [[agent-native-operations]]
source: research/findings/harness-engineering.md
---

# Harness Engineering

## Definition

Discipline of designing environments, specifying intent, and building feedback loops that enable coding agents to do reliable work at scale. The primary job shifts from writing code to enabling agents. Pioneered by Ryan Lopopolo at OpenAI Frontier.

## Core Philosophy

"Humans steer. Agents execute."

The engineering team's job becomes:
- Design environments
- Specify intent
- Build feedback loops
- Allow agents to do reliable work

## Key Principles

1. **No manually-written code** — Even documentation was written by agents
2. **Work depth-first, build building blocks** — Early progress is 10x slower, then 10x faster
3. **Give agents a map, not a manual** — Structured docs as table of contents, knowledge in structured files
4. **Agent legibility is the goal** — Optimize for agent comprehension first, human second
5. **Enforce architecture early** — Rigid layered model with custom linters
6. **Chrome DevTools MCP for QA** — DOM snapshots, screenshots, video recordings
7. **Local observability stack** — Ephemeral per-worktree: Vector -> Victoria Logs/Metrics/Traces
8. **Full autonomy pipeline** — From prompt to PR to merge, escalating to human only for judgment
9. **Entropy and garbage collection** — Encode golden principles, run background agents to scan for deviations

## Throughput

- 0 lines human-written code, ~1M lines codebase
- 1,500 PRs merged by 7 engineers (started at 3)
- 3.5+ PRs/engineer/day, increasing over time
- 6+ hour autonomous runs while humans sleep

## The Ralph Wiggum Loop

Drive a PR to completion by instructing the agent to review its own changes, request additional agent reviews, respond to feedback, iterate until all agent reviewers are satisfied.

## Merge Philosophy

Minimal blocking gates, short-lived PRs, test flakes get follow-up runs not blocks. Agent throughput exceeds human attention: corrections are cheap, waiting is expensive.

## Historical Precedent: The Shusa

The Toyota Chief Engineer (Shusa) held complete product vision without doing detailed engineering, integrating specialists into coherent outcomes. A harness engineer is a Shusa for AI agents.

## Related

- [[codex]] -- Primary tool used
- [[ryan-lopopolo]] -- Pioneer of harness engineering
- [[symphony-orchestrator]] -- Internal orchestration system
- [[dark-factory]] -- The development approach
- [[lean-software-development]] -- Theoretical foundation
