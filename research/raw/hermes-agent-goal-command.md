# Hermes Agent /goal Command

## Source Information
- **Date researched**: 2026-05-15
- **Official documentation**: `hermes-agent.nousresearch.com/docs/user-guide/features/goals`, `hermes-agent.nousresearch.com/docs/reference/slash-commands`
- **GitHub repo**: `NousResearch/hermes-agent`
- **Research method**: Source code inspection (`hermes_cli/goals.py`), official docs, test files

## What /goal Is

`/goal` implements **Persistent Goals** — Hermes' take on the "Ralph loop" (directly inspired by OpenAI Codex CLI 0.128.0's `/goal` by Eric Traut). It gives Hermes a standing objective that survives across conversation turns. After every assistant turn, an auxiliary "judge" model checks if the goal is satisfied. If not, Hermes automatically feeds a continuation prompt back into the same session and keeps working.

## Command Syntax and Subcommands

| Command | Action |
|---------|--------|
| `/goal <text>` | Set or replace the standing goal; kicks off first turn immediately |
| `/goal` or `/goal status` | Show current goal, status, and turns used |
| `/goal pause` | Stop auto-continuation without clearing the goal |
| `/goal resume` | Resume the loop; resets turn counter to zero |
| `/goal clear` | Drop the goal entirely (marks `status=cleared` in DB) |
| `/subgoal <text>` | Add extra criteria to the active goal |
| `/subgoal remove N` | Remove subgoal by 1-based index |
| `/subgoal clear` | Remove all subgoals |

## How It Differs from a Regular Prompt

| Aspect | Regular Prompt | /goal |
|--------|---------------|-------|
| Scope | Single-turn response | Multi-turn until done |
| User interaction | Must re-prompt each turn | Auto-continues via judge |
| Persistence | Lost after turn | Stored in SessionDB across sessions |
| Budget | One inference | Up to N continuation turns (default 20) |
| Preemption | N/A | Real user messages always take priority |

## Session Behavior and Persistence

- Goal state is stored in `SessionDB.state_meta` keyed by `goal:<session_id>`
- `/resume` picks up exactly where left off — active, paused, or done
- The continuation prompt is appended as a **plain user-role message** to history
- Does **not** mutate the system prompt or swap toolsets, so prompt caching stays intact
- Goal state survives session restarts and cross-platform handoff (`/handoff`)
- Works identically on CLI and all gateway platforms (Telegram, Discord, Slack, WhatsApp, Matrix, SMS, web dashboard)

## Done Conditions (Termination)

The loop stops when any of these occur:

1. **Judge says done** — auxiliary model returns `{"done": true, "reason": "..."}` because the assistant response explicitly confirms completion, shows final deliverable, or states goal is unachievable/blocked
2. **Turn budget exhausted** — default 20 continuation turns (`goals.max_turns` in `config.yaml`). Auto-pauses with a message telling user to `/goal resume` or `/goal clear`
3. **User pauses or clears** — explicit `/goal pause` or `/goal clear`
4. **User sends a real message** — preempts continuation; judge re-runs after user's turn
5. **Consecutive judge parse failures** — after 3 consecutive failures where judge returns empty or non-JSON, loop auto-pauses and points user to fix `auxiliary.goal_judge` config
6. **Goal unachievable/blocked** — judge conservatively marks this as DONE to avoid burning budget on impossible tasks

**Fail-open semantics:** If judge errors (network blip, malformed response, unavailable aux client), verdict defaults to `continue`. A broken judge never wedges progress.

## Judge Model Configuration

Judge calls are routed through the `goal_judge` auxiliary task. Default falls back to the main model. To route to a cheap fast model, add to `~/.hermes/config.yaml`:

```yaml
auxiliary:
  goal_judge:
    provider: openrouter
    model: google/gemini-3-flash-preview
```

Judge output budget: default 4096 tokens (configurable via `auxiliary.goal_judge.max_tokens`).

## Key Technical Invariants (from `hermes_cli/goals.py`)

- Continuation prompt is just a normal user message appended via `run_conversation`
- No system-prompt mutation, no toolset swap — prompt caching stays intact
- Judge failures are fail-open (`continue`)
- Real user messages preempt the continuation loop and pause it for that turn
- Module has zero hard dependency on `cli.HermesCLI` or the gateway runner; both wire the same `GoalManager`

## Builder / Reviewer Workers: Separate Systems

There is NO explicit builder/reviewer worker architecture built into `/goal` itself.

- `/goal` is a **single-session continuation loop** within one agent instance
- The codebase has **Kanban (multi-agent board)** and **Subagent Delegation** features where tasks can be assigned to profiles (e.g., "reviewer") and dispatched to worker agents, but these are **separate systems**; they are **not** part of `/goal` semantics
- The `delegate_task` tool spawns child `AIAgent` instances with isolated context and restricted toolsets, but this is orthogonal to `/goal`
- In short: `/goal` = single-agent persistent loop; Kanban/delegation = multi-agent orchestration. They can be used together but `/goal` does not inherently create builder/reviewer workers

## Sources

- Official docs: `https://hermes-agent.nousresearch.com/docs/user-guide/features/goals`
- Slash commands reference: `https://hermes-agent.nousresearch.com/docs/reference/slash-commands`
- GitHub repo: `https://github.com/NousResearch/hermes-agent`
- Core source: `hermes_cli/goals.py`
- Tests: `tests/hermes_cli/test_goals.py`, `tests/tui_gateway/test_goal_command.py`
- Command registry: `hermes_cli/commands.py`
