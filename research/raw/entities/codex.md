---
title: "OpenAI Codex"
created: 2026-04-09
updated: 2026-04-09
type: entity
tags: [model, tools]
sources: []
---

# OpenAI Codex

OpenAI's code generation model, descended from GPT-3.5/4 and fine-tuned specifically on code corpora. Used as the primary coding agent in the harness engineering and dark factory pipeline.

## Role in Dark Factory

Codex is the main workhorse agent in Ryan Lopopolo's OpenAI Frontier harness engineering pipeline. It generates, reviews, and iterates on code autonomously within scoped environments. Key capabilities:
- Autonomous coding runs of 6+ hours
- Agent-to-agent code review
- PR generation at 10-15 PRs/engineer/day rates
- Zero human-written code in production codebase

## Related

- [[harness-engineering]] -- The methodology that uses Codex as the primary agent
- [[ryan-lopopolo]] -- OpenAI Frontier, architect of the dark factory harness
- [[openai-frontier]] -- The organization driving harness engineering
