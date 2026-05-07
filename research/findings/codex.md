---
title: "OpenAI Codex: The Coding Agent Workhorse"
tags: [agent, model, tools, codex, openai]
related:
- harness-engineering
- ryan-lopopolo
- dark-factory
- symphony-orchestrator
source: research/raw/codex.md
---
# OpenAI Codex: The Coding Agent Workhorse

## Summary

OpenAI's code generation model, descended from GPT-3.5/4 and fine-tuned on code corpora. The primary coding agent in the harness engineering and dark factory pipeline at OpenAI Frontier.

## Role in Dark Factory

- Autonomous coding runs of 6+ hours
- Agent-to-agent code review
- PR generation at 10-15 PRs/engineer/day
- Zero human-written code in production codebase
- Validates codebase state, reproduces bugs, implements fixes, records video demos

## Capabilities

- Full autonomy pipeline: validate → reproduce → fix → validate → PR → respond → merge
- Chrome DevTools integration: DOM snapshots, screenshots, navigation
- Local observability: LogQL, PromQL, TraceQL queries
- Video recording of failures and fixes

## Architecture Context

Codex operates within the harness engineering framework: environments designed for agent legibility, structured docs, custom linters, and observability stacks. The agent is only as good as its harness.

## Related

- [[harness-engineering]] — Methodology that uses Codex
- [[ryan-lopopolo]] — Pioneer of Codex-based dark factory
- [[dark-factory]] — Development approach
- [[symphony-orchestrator]] — System that orchestrates Codex
