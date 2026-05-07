---
title: 'Hermes Kanban: Multi-Agent Coordination Primitive'
tags:
- kanban
- hermes
- multi-agent
- workflow
- coordination
- toyota
- lean
related:
- kanban-doctrine
- toyota-production-system
- lean-doctrine
- agent-orchestrator-pattern
- subagent-architecture
- context-persistence
source: Hermes Agent Kanban docs (Nous Research), compiled 2026-05-04
---




# Hermes Kanban: Multi-Agent Coordination Primitive

Hermes Kanban is a durable task board backed by a single SQLite database at ~/.hermes/kanban.db. Every task is a row. Every handoff is a row anyone can read and write. Every worker is a full OS process with its own identity, memory, and toolset. This is not a project management tool bolted onto an agent. It is a coordination primitive: the shape that covers workloads delegate_task cannot.

## delegate_task versus Kanban

| Dimension | delegate_task | Kanban |
|---|---|---|
| Shape | RPC call (fork to join) | Durable message queue plus state machine |
| Parent | Blocks until child returns | Fire-and-forget after create |
| Child identity | Anonymous subagent | Named profile with persistent memory |
| Resumability | None, failed equals failed | Block to unblock to re-run; crash to reclaim |
| Human in the loop | Not supported | Comment or unblock at any point |
| Agents per task | One call equals one subagent | N agents over task's life |
| Audit trail | Lost on context compression | Durable rows in SQLite forever |
| Coordination | Hierarchical (caller to callee) | Peer, any profile reads or writes any task |

delegate_task is a function call; Kanban is a work queue where every handoff is a row any profile or human can see and edit.

## The Six Columns

1. Triage: raw ideas, a specifier fleshes out the spec before anyone works on them.
2. Todo: created but waiting on dependencies, or not yet assigned.
3. Ready: assigned and waiting for the dispatcher to claim.
4. In Progress: a worker is actively running the task.
5. Blocked: a worker asked for human input, or the circuit breaker tripped.
6. Done: completed.

## The Dispatcher

A long-lived loop inside the gateway process. Every N seconds (default 60), it atomically reclaims stale claims (TTL expired), reclaims crashed workers (PID gone but TTL not yet expired), promotes tasks whose parents are all done from todo to ready, and claims ready tasks spawning the assigned profile as a worker process.

After approximately five consecutive spawn failures on the same task, the dispatcher auto-blocks it. This is the circuit breaker. Prevents thrashing on tasks whose profile does not exist, workspace cannot mount, or credentials are missing.

## Worker Toolset

When a worker is spawned, HERMES_KANBAN_TASK is set in its environment. This unlocks a dedicated toolset:

- kanban_show: read the current task (title, body, prior attempts, comments, context)
- kanban_complete: finish with summary plus metadata structured handoff
- kanban_block: escalate for human input
- kanban_heartbeat: signal liveness during long operations
- kanban_comment: append to the task thread
- kanban_create: fan out into child tasks (orchestrators)
- kanban_link: add dependency edges after the fact (orchestrators)

Why tools and not CLI? Backend portability (works across Docker, Modal, SSH), no shell-quoting fragility, and structured JSON errors the model can reason about. Zero schema footprint on normal sessions.

## Workspaces

- Scratch: fresh tmp dir, garbage collected on archive. For research, ephemeral computation.
- dir with absolute path: shared persistent directory. For Obsidian vault, ops scripts repo, per-account folder.
- Worktree: Git worktree under .worktrees/id with branch isolation. For coding tasks.

Relative paths are rejected at dispatch as a confused-deputy escape vector.

## Dependency Engine

Tasks can have parent-child links. A child in todo stays there until every parent reaches done, then auto-promotes to ready. No manual coordination. The dispatcher and dependency engine handle it. This is the pipeline primitive: PM to backend engineer to reviewer, each stage gated by the prior.

## Key Features

Idempotent create: first call creates the task; subsequent calls with the same key return the existing task id. Critical for cron jobs and webhooks that might fire twice.

Task pinning: a single task can load extra skills beyond the built-in kanban-worker. The dispatcher passes --skills for each. The worker spawns with all loaded. No need to edit the assignee's profile.

The orchestrator skill encodes the decomposition playbook: anti-temptation rules, a standard specialist roster (researcher, analyst, writer, backend engineer, reviewer, ops, PM), and a step-by-step pattern for fan-out, pipeline, and human-in-the-loop workflows.

The dashboard is a bundled plugin. Drag-and-drop cards between columns, inline create, multi-select with bulk actions, per-card drawer with markdown-rendered description, dependency editor, comment thread, last 20 events. Live updates via WebSocket tailing the append-only task_events table.

## Gateway Notifications

When you run /kanban create from a gateway chat (Telegram, Discord, Slack), the originating chat is auto-subscribed. The notifier polls task_events and delivers one message per terminal event (completed, blocked, gave_up, crashed, timed_out) to that chat. Completed tasks also send the first line of the worker's result. Subscriptions auto-remove once the task reaches done or archived.

## Runs: One Row Per Attempt

A task is a logical unit of work; a run is one attempt to execute it. The task_runs table captures outcome (completed, blocked, crashed, timed_out, spawn_failed, gave_up, reclaimed), summary and metadata (structured handoff), elapsed time, profile, and timestamp.

Downstream children read the most recent completed run's summary plus metadata for each parent. Retrying workers read prior attempts so they do not repeat a failed path. This replaces the "dig through comments" dance of flat kanban systems.

## Canonical Collaboration Patterns

P1 Fan-out: N siblings, same role. "Research 5 angles in parallel."
P2 Pipeline: role chain like scout to editor to writer. Daily brief assembly.
P3 Voting or Quorum: N siblings plus 1 aggregator. Three researchers, one reviewer picks.
P4 Long-running Journal: same profile plus shared directory plus cron. Obsidian vault accumulation.
P5 Human-in-the-Loop: worker blocks, user comments, unblock. Ambiguous decisions.
P6 At-mention: inline routing from prose. "@reviewer look at this."
P7 Thread-scoped Workspace: /kanban here in a thread. Per-project gateway threads.
P8 Fleet Farming: one profile, N subjects. Fifty social accounts.
P9 Triage Specifier: rough idea to triage to specifier to todo. "Turn this one-liner into a spec."

## Philosophical Lineage

Hermes Kanban is not "a Kanban board for agents." It is an implementation of the same principles Taiichi Ohno discovered on Toyota's factory floor, filtered through David Anderson's knowledge-work adaptation, applied to autonomous agents as workers.

The principles hold: pull over push (dispatcher claims tasks; workers do not receive assignments pushed onto them), visual management (dashboard makes fleet state visible without querying every agent), WIP limits (implicitly each profile works on one task at a time, serialized by the dispatcher), stop-the-line authority (kanban_block is the Andon cord), structured handoff (summary plus metadata is the knowledge-work equivalent of a kanban card), durable audit trail (task_events and task_runs are the factory's production log), evolutionary change (the board overlays onto whatever workflow the operator already has).

## The Boundary

Kanban is deliberately single-host. ~/.hermes/kanban.db is local SQLite and the dispatcher spawns workers on the same machine. Multi-host coordination is out of scope. This is a feature, not a limitation. It makes the system deterministic, inspectable, and free of distributed systems complexity. The agent fleet is a local organism.
