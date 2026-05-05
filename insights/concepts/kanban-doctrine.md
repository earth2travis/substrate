---
title: "Kanban Doctrine: Mission Command for the Agent Squad"
tags: [doctrine, kanban, auftragstaktik, mission-command, multi-agent, coordination]
related:
  - [[auftragstaktik-mission-command]]
  - [[agentic-architecture]]
  - [[toyota-production-system]]
  - [[research/raw/hermes-kanban-deep-dive]]
  - [[research/raw/multi-agent-coordination]]
source: research/raw/auftragstaktik-mission-command.md
---

# Kanban Doctrine: Mission Command for the Agent Squad

## 1. Commander's Intent (The "Why")

Every task begins with intent, not method. The body of a Kanban task is the Auftrag: what must be achieved, why it matters, and what done looks like. It explicitly does not prescribe the route.

**What the Operator provides:**
- Objective: the concrete deliverable
- Purpose: why this matters to the partnership
- End state: what success looks like

**What the Operator does not provide:**
- Implementation steps
- Tool choices
- File paths (unless constrained by convention)

The agent figures out the how. That is the whole point.

## 2. Kanban vs delegate_task: Decision Rules

Use `delegate_task` when the work is a subroutine: predictable, bounded, and the parent needs the result before continuing. Use Kanban when the work is a mission: durable, cross-profile, and may need human intervention mid-flight.

| Use `delegate_task` | Use Kanban |
|---|---|
| Single turn, parent blocks until done | Durable, survives parent context |
| One agent, one toolset | Named profile with persistent memory |
| No human-in-the-loop needed | May need block / unblock |
| No audit trail needed beyond this session | Audit trail must survive forever |
| Hierarchical: caller → callee | Peer: any profile reads/writes any task |
| Example: "Summarize this file" | Example: "Define our Kanban doctrine" |

One-sentence rule: if the task is a function call, use `delegate_task`. If the task is a mission with unclear duration or multiple possible agents, use Kanban.

## 3. The Backbrief: Metadata Rules

Before starting major work, the agent presents its plan back to the board via `kanban_comment`. This is not for permission. It is for alignment. The comment should answer:

1. What do I understand the intent to be?
2. What is my plan of action?
3. What do I need that I don't have?

**Standard metadata schema for every completed task:**

```python
kanban_complete(
    summary="human-readable 1-3 sentences",
    metadata={
        "changed_files": ["path/to/file.md"],
        "tests_run": 0,
        "decisions": ["why we chose X over Y"],
        "findings": ["key discovery"],
        "sources_read": 3,
        "recommendation": "optional: what to do next",
    }
)
```

**Rules:**
- `summary` is for humans. Concrete, specific, no fluff.
- `metadata` is for downstream parsers. Structure it so the next agent doesn't need to re-read your prose.
- `changed_files` is mandatory if files were touched.
- `decisions` is mandatory if a choice was made.
- `findings` is mandatory if research was done.
- Never put secrets, tokens, or raw PII in either field. Runs are durable forever.

## 4. Disciplined Initiative

The agent is expected to adapt. If the terrain changes mid-mission, the agent who sticks to the original plan but fails the intent has failed. The agent who disobeys the plan to achieve the intent is praised.

**What this means in practice:**
- If a source contradicts your plan, follow the source.
- If a tool fails, try another tool. Don't retry the same failing path three times.
- If you need human input, use `kanban_block` with one specific sentence naming the decision required.
- If you discover follow-up work, create a new Kanban task and assign it to the right profile. Do not scope-creep the current task.

## 5. The General Staff: Shared Mental Models

Auftragstaktik requires shared language. Our shared language is the Substrate.

**Before any Kanban task:**
- Read `SCHEMA.md`, `INDEX.md`, and `log.md`
- Check `insights/` for existing pages on your topic
- Cross-reference relentlessly: every new page links to at least two others via `[[wikilinks]]`

**After any Kanban task:**
- Write findings to `research/findings/` if the work produced new knowledge
- Promote to `insights/` if a concept appears in 2+ findings
- Log the action in `log.md`
- Never edit `research/raw/`

## 6. Stop-the-Line Authority

`kanban_block()` is the Andon cord. Any worker can halt the line.

**Block when:**
- Ambiguity cannot be resolved from available sources
- A decision has meaningful tradeoffs the Operator should weigh
- Credentials, permissions, or resources are missing
- The task as written no longer makes sense given new information

**Do not block when:**
- You can make a reasonable default and move on
- The issue is transient (retry with backoff)
- You're stuck on a subproblem that can be spun off as a child task

## 7. Speed over Perfect Coordination

We trade the efficiency of a perfectly synchronized machine for the resilience of a distributed network. Momentum and local judgment beat waiting for central approval.

**What this means:**
- Don't wait for Ξ2T to bless every step
- Heartbeat every few minutes on long ops so the board shows life
- Complete with structured handoff even if imperfect; the next agent can iterate
- One PR per logical unit. No direct pushes to main.

## Related
- [[auftragstaktik-mission-command]]
- [[agentic-architecture]]
- [[toyota-production-system]]
- [[research/raw/hermes-kanban-deep-dive]]
- [[research/raw/multi-agent-coordination]]
