---
title: Symphony Orchestrator
created: 2026-04-08
updated: 2026-04-08
type: entity
tags: [agent, development, operations]
sources: [raw/transcripts/symphony-harness-engineering-transcript-2026-04-07.md]
---

# Symphony Orchestrator

> OpenAI Frontier's internal orchestration system for managing multiple coding agents simultaneously. Built in Elixir, it drives the "Dark Factory" approach where agents complete tasks autonomously without human monitoring.

## Origin Story

- Built in January 2026 after the team hit 5-10 PRs/engineer/day (up from 3.5)
- Response to human bottleneck: "Where are the humans spending their time? Switching between all these active TMUX panes to drive the agent forward"
- Purpose: Remove the need for humans to sit in front of their terminal

## Architecture

- Built in **Elixir** and the **BEAM** runtime
- Chosen for process supervision and resumability
- Handles "gnarly" refactorings with proper interface boundaries
- Manages concurrent agents without human intervention

## Key Features

### Rework State
When a PR is proposed and escalated to human for review:
- Human does a cheap review: mergeable or not
- If not mergeable, move to "rework"
- Elixir service trashes the entire work tree and PR
- Starts again from scratch
- Human can explain why it was trash to fix the root cause

### Distribution via "Spec"
- Takes proprietary repo scaffolding and asks Codex to write a "spec"
- The spec specifies everything needed for a coding agent to reassemble it locally
- Spawns disconnected Codex to implement the spec
- Spawns another Codex to review implementation vs upstream
- Loops until spec faithfully reproduces the system

### Team Knowledge Integration
- Slurps all agent trajectories into blob storage
- Runs daily loops over session logs to extract improvements
- Reflects learnings back into the repository automatically
- PR comments become signals for missing context
- Failed builds trigger updates to documentation

## Success Metrics

- 10x faster than human development
- 1500 PRs from zero to 1M+ lines of code
- No human-written code (not even infrastructure)
- Deploying billions of tokens per day
- 40% of work is product features, 30% is infra, 30% is everything else

## Related
- [[harness-engineering]] -- The discipline Symphony implements
- [[elixir-beam]] -- Runtime platform
- [[spec-driven-development]] -- Distribution methodology
- [[ryan-lopopolo]] -- Creator/lead of Symphony team
- [[dark-factory]] -- The development approach
- [[openai-frontier]] -- The team building Symphony

## Sources
- raw/transcripts/symphony-harness-engineering-transcript-2026-04-07.md
