---
title: "Kanban Operating Manual"
tags: [guide, kanban, operations, multi-agent, doctrine]
related: [[kanban-doctrine]], [[kanban-vs-delegate-task]], [[kanban-metadata-rules]], [[toyota-production-system]]
source: "internal-doctrine"
---

# Kanban Operating Manual

## What This Manual Is

This is the field manual for the squad. It is not a tutorial. It is the hardened doctrine and the exact tooling, bound together into one artifact that a worker can read in a single sitting and carry into the run. If you are a kanban worker, read this before you touch the board. If you are an orchestrator, read this before you fan out tasks. If you are a human operator, read this to understand what the squad believes about its own coordination.

The manual has two halves: the Doctrine, which tells you why we move the way we do, and the Tooling, which tells you exactly how. Neither half is useful without the other.

## Doctrine: Three Rules

Our operating system is Auftragstaktik. The commander gives intent. The subordinate owns execution. The board is the shared terrain where both parties meet.

### Rule One: Intent Over Instruction

Every Kanban task must state the objective and the end state, not the method. The worker chooses the path. If the method matters, that belongs in a skill, not a task. A task body that reads like a script is a task that has failed before it started. State the "why." Let the worker find the "how."

### Rule Two: Block Before Guess

When the fog of war descends (API changes, missing credentials, ambiguous requirements), the worker halts and escalates. A blocked task with context is more valuable than a completed task that solved the wrong problem. Use `kanban_block(reason=...)` and name the specific decision you need. The block is not failure. The block is disciplined initiative.

### Rule Three: Handoff Is Signal

`kanban_complete` is not "I am done." It is "Here is what happened, what changed, and what the next agent needs to know." The summary is for humans. The metadata is for machines. Both must be present. A task without metadata is a signal without a receiver.

## Choosing Your Weapon: Kanban vs delegate_task

`delegate_task` is a function call. Kanban is a work queue.

If the parent needs the answer right now to continue, use `delegate_task`. If the work should outlive the session, span multiple agents, or involve a human in the loop, use Kanban.

### The Decision Matrix

| Situation | Use | Why |
|---|---|---|
| "Research X and summarize" inside a coding session | `delegate_task` | The parent needs the summary to choose its next move. |
| "Implement feature Y" that takes 30 minutes and needs review | Kanban | It survives context loss and can be retried or reassigned. |
| "Review this PR" | Kanban | Needs a named profile with the right toolset; result must be durable. |
| "Generate 3 variants of this function" | `delegate_task` | Parallel subagents, results fold back immediately. |
| "Monitor this feed and act on new items" | Kanban | Long-running, fire-and-forget, cron dispatches. |
| "Fix this bug" found during a session | `delegate_task` or Kanban | Use `delegate_task` if the fix is small and the parent will verify. Use Kanban if the fix needs its own workspace, branch, or review. |

### Anti-Patterns

Do not chain `delegate_task` for multi-step work that spans minutes. One failed subagent kills the whole chain with no recovery.

Do not use Kanban for questions the parent could answer itself in one tool call. The overhead of task creation, dispatch, and heartbeat is not free.

Do not use `delegate_task` as a substitute for `kanban_create`. If you are orchestrating work for another agent to do later, create a Kanban task.

The shape of the work should choose the tool, not habit.

## Tooling: The Complete CLI

All commands target `~/.hermes/kanban.db`.

### Board Operations

```bash
# List tasks
hermes kanban list                          # all tasks
hermes kanban list --mine                   # tasks assigned to $HERMES_PROFILE
hermes kanban list --status todo            # filter by status
hermes kanban list --status ready --archived # include archived

# Show task details
hermes kanban show <task_id>
hermes kanban show <task_id> --json
hermes kanban context <task_id>             # title + body + parent results + comments

# Task runs and events
hermes kanban runs <task_id>                 # attempt history
hermes kanban tail <task_id>                 # live event stream

# Stats
hermes kanban stats                          # per-status, per-assignee counts
hermes kanban assignees                       # known profiles + task counts
```

### Lifecycle Operations

```bash
# Create
hermes kanban create "<title>" \
  --body "<description>" \
  --assignee <profile> \
  --parent <parent_task_id> \
  --workspace scratch|dir:<path>|worktree \
  --priority N \
  --skill <skill_name> \
  --max-runtime <seconds>

# Complete
hermes kanban complete <task_id> \
  --summary "<human summary>" \
  --metadata '{"changed_files": [...], "tests_run": N}'

# Block and unblock
hermes kanban block <task_id> <reason>
hermes kanban unblock <task_id>

# Comment
hermes kanban comment <task_id> "comment text" --author <name>

# Assign
hermes kanban assign <task_id> <profile>

# Archive
hermes kanban archive <task_id>
```

### Dependency Management

```bash
# Link parent -> child (child waits for parent to complete)
hermes kanban link <parent_id> <child_id>

# Unlink
hermes kanban unlink <parent_id> <child_id>
```

### Worker Operations

```bash
# Dispatcher (run in cron or daemon)
hermes kanban dispatch              # one pass: reclaim stale, promote ready, spawn workers
hermes kanban dispatch --dry-run    # preview without spawning

# Claim a task atomically
hermes kanban claim <task_id> --ttl 900   # 900s TTL (default)

# Heartbeat (worker liveness)
hermes kanban heartbeat <task_id> --note "epoch 12/50, loss 0.31"
```

### Notifications

```bash
# Subscribe to task terminal events
hermes kanban notify-subscribe <task_id>

# List subscriptions
hermes kanban notify-list

# Unsubscribe
hermes kanban notify-unsubscribe <task_id>
```

### Garbage Collection

```bash
# GC archived workspaces, old events, old logs
hermes kanban gc --event-retention-days 30 --log-retention-days 30
```

## Lifecycle Cheat Sheet

```
create -> todo -> ready -> running -> done
                         -> blocked -> ready
                         -> archived
```

1. **Orient:** `hermes kanban show <id>` or `hermes kanban context <id>`
2. **Work** inside `$HERMES_KANBAN_WORKSPACE`
3. **Heartbeat** every few minutes on long ops
4. **Block** if you need human input (use `kanban_block(reason=...)`)
5. **Complete** with structured summary + metadata

## Metadata: The A3 Handoff

Every `kanban_complete` call must include structured metadata. The shape depends on the work type. The principle is A3: what was the problem, what did we observe, what was the root cause, what did we do, and how do we know it worked?

### Coding Task

```json
{
  "changed_files": ["path/to/file.py"],
  "tests_run": 14,
  "tests_passed": 14,
  "decisions": ["user_id primary, IP fallback for unauthenticated requests"],
  "migration_needed": false,
  "breaking_change": false
}
```

### Research Task

```json
{
  "sources_read": 12,
  "recommendation": "vLLM",
  "confidence": "high",
  "next_action": "spike: benchmark vLLM vs SGLang on our dataset"
}
```

### Review Task

```json
{
  "pr_number": 123,
  "findings": [
    {"severity": "critical", "file": "api/search.py", "line": 42, "issue": "raw SQL concat"}
  ],
  "approved": false,
  "blockers": ["SQL injection risk in /search"]
}
```

### Infrastructure / Ops Task

```json
{
  "services_affected": ["gateway", "dispatcher"],
  "rollback_plan": "revert commit abc123",
  "monitoring_added": true,
  "alert_thresholds": {"cpu": 80, "memory": 85}
}
```

### Documentation Task

```json
{
  "pages_created": ["guides/kanban-doctrine.md"],
  "pages_updated": ["INDEX.md"],
  "lint_passed": true,
  "cross_references_added": 4
}
```

### Universal Fields

Every metadata object should include:

- `work_type`: One of `[coding, research, review, infra, docs, analysis, other]`
- `estimated_effort`: `[trivial, small, medium, large, epic]` — updated if original estimate was wrong
- `risks`: Array of strings describing anything the next worker should know

### Summary Shapes

Coding:
```
shipped rate limiter: token bucket keyed on user_id with IP fallback, 14 tests pass
```

Research:
```
3 competing libraries reviewed: vLLM wins on throughput, SGLang on latency, Tensorrt-LLM on memory
```

Review:
```
reviewed PR #123: 2 blocking issues found (SQL injection in /search, missing CSRF on /settings)
```

### Anti-Patterns

Do not put secrets or tokens in metadata. It is persisted in SQLite forever.

Do not write narrative prose in metadata. Use the `summary` field of `kanban_complete` for prose. Metadata is for parsers.

Do not omit metadata because the task was "small." Small tasks compound into large systems. The cost of a missing handoff is paid by the next agent who has to rediscover what you already knew.

## Workspace Kinds

| Kind | Description |
|---|---|
| `scratch` | Fresh tmp dir, GC'd on archive |
| `dir:<path>` | Shared persistent directory |
| `worktree` | Git worktree at the resolved path |

## The Spirit of the Work

A board is not a todo list. It is a shared consciousness. Every card is a commitment. Every handoff is a trust exercise. Every blocked task is a signal, not a stain.

We do not move fast and break things. We move fast and hand things off cleanly. The speed of the squad is not the speed of the individual worker. It is the speed at which signal passes between workers. This manual exists to make that signal fast, clean, and complete.

If you have read this far, you know enough. Go orient. Then work. Then hand it off.
