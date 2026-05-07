---
title: "Harness Engineering: Designing Environments for Coding Agents"
tags: [agent, development, operations, ai, codex, architecture]
related: [[codex]], [[ryan-lopopolo]], [[symphony-orchestrator]], [[dark-factory]], [[lean-software-development]], [[llm-wiki-pattern]]
source: research/raw/harness-engineering.md
---

# Harness Engineering: Designing Environments for Coding Agents

## Summary

Discipline of designing environments, specifying intent, and building feedback loops that enable coding agents to do reliable work at scale. The primary job shifts from writing code to enabling agents. Pioneered by Ryan Lopopolo at OpenAI Frontier.

## Core Philosophy

**"Humans steer. Agents execute."**

The engineering team's job becomes:
- Design environments
- Specify intent
- Build feedback loops
- Allow agents to do reliable work

## Key Principles

1. **No manually-written code** — Even AGENTS.md was written by Codex
2. **Work depth-first, build building blocks** — Early progress is 10x slower, then 10x faster
3. **Give agents a map, not a manual** — AGENTS.md as table of contents, knowledge in structured docs/
4. **Agent legibility is the goal** — Optimize for Codex's legibility first, human second
5. **Enforce architecture early** — Rigid layered model with custom linters
6. **Chrome DevTools MCP for QA** — DOM snapshots, screenshots, video recordings
7. **Local observability stack** — Ephemeral per-worktree: Vector → Victoria Logs/Metrics/Traces
8. **Full autonomy pipeline** — From prompt to PR to merge, escalating to human only for judgment
9. **Entropy and garbage collection** — Encode golden principles, run background agents to scan for deviations

## Throughput

- 0 lines human-written code, ~1M lines codebase
- 1,500 PRs merged by 7 engineers (started at 3)
- 3.5+ PRs/engineer/day, increasing over time
- 6+ hour autonomous runs while humans sleep

## The Ralph Wiggum Loop

Drive a PR to completion by instructing Codex to review its own changes, request additional agent reviews, respond to feedback, iterate until all agent reviewers are satisfied.

## Merge Philosophy

Minimal blocking gates, short-lived PRs, test flakes get follow-up runs not blocks. Agent throughput >> human attention → corrections are cheap, waiting is expensive.

## Historical Precedent: The Shusa

The Toyota Chief Engineer (Shusa) held complete product vision without doing detailed engineering, integrating specialists into coherent outcomes. A harness engineer is a Shusa for AI agents.

## Related

- [[codex]] — Primary tool used
- [[ryan-lopopolo]] — Pioneer of harness engineering
- [[symphony-orchestrator]] — OpenAI's internal orchestration system
- [[dark-factory]] — The development approach
- [[lean-software-development]] — Theoretical foundation
- [[llm-wiki-pattern]] — Knowledge visibility pattern (AGENTS.md as TOC)
