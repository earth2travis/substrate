# OpenAI Codex CLI /goal Command

## Source Information
- **Date researched**: 2026-05-15
- **Official documentation**: `developers.openai.com/codex/cli/slash-commands`
- **GitHub repo**: `openai/codex`
- **Research method**: Source code inspection, GitHub issue analysis, official docs

## What /goal Is

`/goal` is an experimental slash command in OpenAI's Codex CLI. It sets or views an experimental goal for a long-running task. To enable it, set `features.goals = true` in `config.toml` or toggle via `/experimental`.

## Command Syntax and Subcommands

| Command | Action |
|---------|--------|
| `/goal <objective>` | Create or replace the current thread goal |
| `/goal` | View current goal (status, objective, tokens used, budget) |
| `/goal pause` | Pause the active goal |
| `/goal resume` | Resume a paused goal |
| `/goal clear` | Remove the goal entirely |
| `/goal edit` | Open editor to change objective (added in PR #21954) |

## Data Model and Session Semantics

- **Thread-scoped**: One goal per thread, stored in SQLite `thread_goals` table keyed by `thread_id`
- **Fields**: `objective` (string, max 4,000 chars), `status`, `token_budget` (optional), `tokens_used` (cumulative), `time_used_seconds` (cumulative), timestamps
- **Statuses**: `active`, `paused`, `budget_limited`, `complete`
- **Persistence**: The goal survives across turns. Ending one turn does not shrink the objective
- **Auto-continuation**: When idle and a goal is `active`, the runtime schedules continuation turns automatically

## Steering Prompts

Hidden `<goal_context>` user-context fragments are injected via templates:
- `continuation.md` — tells model to keep working toward the objective
- `budget_limit.md` — injected when token budget is exhausted; tells model to wrap up
- `objective_updated.md` — injected when user edits the objective

## Done and Terminal States

1. **`complete`** — Model calls `update_goal` tool with `status: "complete"`. Only allowed when objective is fully achieved. Returns a completion budget report (tokens/time used)
2. **`budget_limited`** — Soft stop when `tokens_used >= token_budget`. Runtime marks goal `budget_limited` and injects wrap-up prompt. No hard abort
3. **`paused`** — User-initiated via `/goal pause`. Continuation turns stop
4. **`cleared`** — User removes goal via `/goal clear`

## Limitations and Parameters

- Feature flag required (`features.goals = true`)
- One goal per thread: `create_goal` fails if a goal already exists
- Objective length limit: max 4,000 characters. Longer instructions should be placed in a file and referenced
- Model-side restrictions: `update_goal` can ONLY set status to `complete`. Pause/resume/budget-limited are reserved for user/system
- Token budget: optional; soft-stops at exhaustion
- Time budget: tracked for reporting only
- Not available in side conversations
- Approval policy ambiguity: open issue #22362 notes that `/goal` does not explicitly define how goal mode interacts with inherited repo/AGENTS approval policies

## Key Implementation Files (openai/codex repo)

- `codex-rs/core/src/goals.rs` — Core runtime, lifecycle, accounting, continuation scheduling
- `codex-rs/core/src/tools/handlers/goal.rs` — Dispatcher
- `codex-rs/core/src/tools/handlers/goal/create_goal.rs` — `create_goal` handler
- `codex-rs/core/src/tools/handlers/goal/update_goal.rs` — `update_goal` handler (complete only)
- `codex-rs/core/src/tools/handlers/goal/get_goal.rs` — `get_goal` handler
- `codex-rs/core/src/tools/handlers/goal_spec.rs` — Tool specs exposed to the model
- `codex-rs/core/templates/goals/continuation.md` — Continuation steering prompt
- `codex-rs/core/templates/goals/budget_limit.md` — Budget-limit steering prompt
- `codex-rs/core/templates/goals/objective_updated.md` — Objective-edit steering prompt
- `codex-rs/tui/src/app/thread_goal_actions.rs` — TUI CRUD actions
- `codex-rs/tui/src/chatwidget/goal_menu.rs` — TUI menu rendering
- `codex-rs/tui/src/chatwidget/goal_status.rs` — Status-line indicator
- `codex-rs/tui/src/chatwidget/goal_validation.rs` — Objective length validation
- `codex-rs/state/migrations/0029_thread_goals.sql` — SQLite schema
- `codex-rs/state/src/model/thread_goal.rs` — State model

## Notable GitHub Issues

| # | Title | State |
|---|-------|-------|
| #20536 | Document the /goal CLI command and Goals lifecycle in slash-command docs | Closed |
| #21176 | /goal does not actually complete the goal when doing review loops | Open |
| #22253 | /goal keeps restarting work after the goal is already completed | Closed |
| #22362 | /goal should define how goal mode interacts with inherited approval policies | Open |
| #21954 | Fix goal update and add /goal edit command in TUI | Closed |
| #22045 | Improve goal continuation based on feedback | Closed |
| #20790 | Keep paused goals paused on thread resume | Closed |
| #20799 | Add goal lifecycle metrics | Closed |
| #22644 | Restate goal in full when context is compacted | Open |
| #22049 | Codex macOS app should natively support /goal | Open |

## Lifecycle Metrics (OpenTelemetry)

- `codex.goal.created`
- `codex.goal.completed`
- `codex.goal.budget_limited`
- `codex.goal.token_count`
- `codex.goal.duration_s`

## Comparison Context

- **Claude Code**: Does not have an explicit `/goal` command; sessions are turn-based without a persisted long-running objective state (NOTE: This was accurate at time of research, but Claude Code later added `/goal`)
- **Hermes Agent**: Uses task delegation and subagent patterns; goals are typically session-scoped directives rather than persisted thread-level objectives
- **Codex `/goal`** is unique in its explicit persistence across turns, auto-continuation when idle, token/time accounting, and budget-limited soft-stop behavior
