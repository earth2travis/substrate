---
title: "When to Use Kanban vs delegate_task"
tags: [guide, kanban, delegate-task, operations, multi-agent, workflow]
related: [[kanban-doctrine]], [[kanban-metadata-rules]], [[toyota-production-system]]
source: "internal-doctrine"
---

# When to Use Kanban vs delegate_task

## The One-Sentence Rule

`delegate_task` is a function call. Kanban is a work queue.

If the parent needs the answer right now to continue, use `delegate_task`.
If the work should outlive the session, span multiple agents, or involve a human in the loop, use Kanban.

## The Decision Matrix

| Situation | Use | Why |
|---|---|---|
| "Research X and summarize" inside a coding session | `delegate_task` | The parent needs the summary to choose its next move. |
| "Implement feature Y" that takes 30 minutes and needs review | Kanban | It survives context loss and can be retried or reassigned. |
| "Review this PR" | Kanban | Needs a named profile with the right toolset; result must be durable. |
| "Generate 3 variants of this function" | `delegate_task` | Parallel subagents, results fold back immediately. |
| "Monitor this feed and act on new items" | Kanban | Long-running, fire-and-forget, cron dispatches. |
| "Fix this bug" found during a session | `delegate_task` or Kanban | Use `delegate_task` if the fix is small and the parent will verify. Use Kanban if the fix needs its own workspace, branch, or review. |

## Anti-Patterns

**Do not** chain `delegate_task` for multi-step work that spans minutes. One failed subagent kills the whole chain with no recovery.

**Do not** use Kanban for questions the parent could answer itself in one tool call. The overhead of task creation, dispatch, and heartbeat is not free.

**Do not** use `delegate_task` as a substitute for `kanban_create`. If you are orchestrating work for another agent to do later, create a Kanban task.

## Remember

The shape of the work should choose the tool, not habit.
