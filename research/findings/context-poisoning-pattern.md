---
title: "Context Poisoning: The Impulse Import Anti-Pattern"
tags:
  - ai-agents
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/context-poisoning-pattern.md
---

# Context Poisoning: The Impulse Import Anti-Pattern

**Source:** [@kloss_xyz](https://x.com/kloss_xyz/status/2032011756890177552) (March 2026)
**Filed:** 2026-03-11

## The Pattern

Importing external configs, prompts, skills, and frameworks into an agent system without auditing them against what already exists. Each import seems like an improvement but creates conflicts:

- New configs conflict with existing rules
- Imported skills collide with existing skills
- Governance frameworks rewrite assumptions routing depends on
- System reliability degrades with each "improvement"

Named failure mode: **context poisoning with good intentions.**

## The Fix

Replace impulse importing with structured reflection:

- "What's actually wrong right now?" instead of "What cool thing can I absorb?"
- Audit what exists before bolting on something new
- When something breaks, document it and make the fix mechanical

## Symptoms of a Poisoned System

- Stale docs the system reports as current
- Agents claiming "done" when nothing was actually completed
- Rules written in multiple files getting violated in the session they're cited in
- Corrections that vanish the next day (no persistence)
- Health scores reporting "fine" while critical things fail underneath

## How We Guard Against This

Already implemented:

1. **Skills audit against Anthropic guide** before modifying skills (not just importing patterns)
2. **The Floor (ops agent)** catches silent failures: stale TODOs, failing crons, uncommitted work
3. **Mechanical enforcement in AGENTS.md** over behavioral intention (issue closure protocol, PR steps, CI checks)
4. **Evidence-based agent creation**: reviewed 6 weeks of failure data before deciding who to build, not importing someone else's agent template
5. **"Knowledge does not produce behavior change. Only structure produces behavior change."** (March 7 lesson)

## Principle

Every external pattern must be evaluated against the existing system before adoption. The question is never "is this good?" but "does this fit what we already have without breaking it?"
