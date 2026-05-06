---
title: "Symphony Orchestrator: Multi-Agent Coding Pipeline"
tags: [agent, development, operations, elixir, orchestration]
related: [[harness-engineering]], [[codex]], [[elixir-beam]], [[spec-driven-development]], [[ryan-lopopolo]], [[dark-factory]]
source: research/raw/symphony-orchestrator.md
---

# Symphony Orchestrator: Multi-Agent Coding Pipeline

## Summary

OpenAI Frontier's internal orchestration system for managing multiple coding agents simultaneously. Built in Elixir/BEAM, it drives the "dark factory" approach where agents complete tasks autonomously without human monitoring.

## Origin

Built in January 2026 after the team hit 5-10 PRs/engineer/day. Response to human bottleneck: "Where are the humans spending their time? Switching between TMUX panes to drive the agent forward."

## Architecture

- Built in **Elixir** and the **BEAM** runtime
- Chosen for process supervision and resumability
- Handles concurrent agents without human intervention
- Manages "gnarly" refactorings with proper interface boundaries

## Key Features

### Rework State
Human does a cheap review: mergeable or not. If not, the service trashes the work tree and PR, starts from scratch. Human explains why to fix the root cause.

### Distribution via "Spec"
Takes proprietary repo scaffolding, asks Codex to write a spec, spawns disconnected Codex to implement it, spawns another to review, loops until faithful.

### Team Knowledge Integration
Slurps all agent trajectories into blob storage, runs daily loops over session logs to extract improvements, reflects learnings back into the repository automatically.

## Success Metrics

- 10x faster than human development
- 1,500 PRs from zero to 1M+ lines
- No human-written code
- Deploying billions of tokens per day
- 40% product features, 30% infra, 30% everything else

## Related

- [[harness-engineering]] — The discipline Symphony implements
- [[codex]] — The agent it orchestrates
- [[elixir-beam]] — Runtime platform
- [[spec-driven-development]] — Distribution methodology
- [[ryan-lopopolo]] — Creator/lead
- [[dark-factory]] — The development approach
