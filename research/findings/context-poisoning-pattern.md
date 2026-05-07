---
title: "Context Poisoning: The Impulse Import Anti-Pattern"
tags: [finding, anti-pattern, context, agent-ops, quality]
related:
- agent-memory
- context-stack
- agent-native-operations
source: research/raw/context-poisoning-pattern.md
ingested: 2026-05-07
---
# Context Poisoning: The Impulse Import Anti-Pattern

Importing external configs, prompts, skills, and frameworks into an agent system without auditing them against existing material. Each import seems like an improvement but degrades system reliability through undetected conflicts.

## Key Points

**The pattern.** New configs conflict with existing rules. Imported skills collide with existing skills. Governance frameworks rewrite assumptions that routing depends on. System reliability degrades with each "improvement."

**Symptoms of a poisoned system.** Stale docs reported as current. Agents claiming "done" when nothing was completed. Rules written in multiple files getting violated in the same session they are cited. Corrections that vanish the next day. Health scores reporting "fine" while critical things fail underneath.

**The fix: structured reflection over impulse.** Ask "What's actually wrong right now?" instead of "What cool thing can I absorb?" Audit what exists before bolting on something new. When something breaks, document it and make the fix mechanical.

**Existing guards.** Skills audit before modification. The Floor (ops agent) catches silent failures: stale TODOs, failing crons, uncommitted work. Mechanical enforcement in AGENTS.md over behavioral intention. Evidence-based agent creation from 6 weeks of failure data, not imported templates.

**Core principle.** Knowledge does not produce behavior change. Only structure produces behavior change. Every external pattern must be evaluated against the existing system before adoption. The question is never "is this good?" but "does this fit what we already have without breaking it?"

## Relevance

Context poisoning is the agent equivalent of dependency hell. The antidote is not more imports; it is disciplined evaluation and mechanical enforcement.

## Related

- [[agent-memory]] -- Memory architecture vulnerable to poisoning
- [[context-stack]] -- Layered context susceptible to conflict
- [[agent-native-operations]] -- Ops design that prevents silent failures
