# Anthropic Claude Code /goal Command

## Source Information
- **Date researched**: 2026-05-15
- **Official documentation**: `code.claude.com/docs/en/goal`, `code.claude.com/docs/en/commands`, `code.claude.com/docs/en/whats-new`
- **Min version**: v2.1.139+
- **Research method**: Documentation scraping, GitHub issue tracker analysis

## What /goal Is

`/goal` is a session-scoped built-in command (not a skill/MCP prompt) that sets a completion condition. Claude autonomously works across turns until a small fast evaluator model (default Haiku) confirms the condition is met.

## Command Syntax

| Command | Action |
|---------|--------|
| `/goal <condition>` | Set or replace the current standing goal |
| `/goal` | Check status (turns, tokens) |
| `/goal clear` | Remove the goal early (aliases: stop, off, reset, none, cancel) |

## Session Semantics

- **Scope**: Session-scoped within a single Claude Code conversation
- **Done state**: Clears automatically when the evaluator model returns "yes"
- **Recording**: Records an "achieved" entry in the transcript
- **Clearing**: Also cleared by `/clear` (starts a new conversation)
- **Resume behavior**: Active goals are restored on `--resume` or `--continue`, but turn count, timer, and token baseline reset. Achieved or cleared goals are NOT restored

## Done Detection: The Evaluator Pattern

Claude Code uses a separate small model (default Haiku) to evaluate whether the goal condition is satisfied after each assistant response. This is architecturally distinct from Codex (model self-reports via tool call) and Hermes (judge model returns JSON verdict).

The evaluator reads the conversation context and the goal condition, then returns a binary yes/no on whether the condition is met.

## Limitations

- Requires workspace trust
- Blocked by `disableAllHooks` or `allowManagedHooksOnly` settings
- One active goal per session
- No built-in circuit breaker (community reports token burn on unsatisfiable conditions)
- No explicit token or turn budget
- Goal state does not persist across sessions (resets on `--resume`)

## Platform Availability

Works across all Claude Code surfaces:
- Interactive CLI
- Non-interactive (`claude -p`)
- Desktop app
- Remote Control

## GitHub Issues Related to /goal

~19 tracked issues including:
- Acknowledgement loops (evaluator repeatedly says "not yet" but never reaches done)
- JSON validation failures in stop hooks
- Prompt-too-long errors during goal execution
- Silent auto-compact failures
- Feature requests for hierarchical goals and intent locks

## Comparison to Related Features

### vs. `/loop`
`/loop` repeats a single action; `/goal` defines a target condition and lets Claude navigate the path autonomously.

### vs. Stop Hooks
Stop hooks trigger when specific text appears in output; `/goal` evaluates semantic completion against a condition.

### vs. Auto Mode
Auto mode lets Claude suggest actions without waiting; `/goal` gives Claude a target to reach without intervention.

## Writing Effective Goal Conditions

Good conditions are specific and verifiable:
- "Add error handling to all API routes" — good
- "Fix the bug" — too vague
- "Refactor the auth module to use the new pattern" — good
- "Make it better" — too vague

## Comparison Context

- **Codex**: Codex `/goal` persists in SQLite, has explicit subcommands (pause/resume/edit), and uses token budgets. Claude Code `/goal` is lighter, session-only, and uses an evaluator model
- **Hermes**: Hermes `/goal` has a judge model (JSON verdict), turn budget, and survives session restarts. Claude Code's evaluator is simpler but lacks budget enforcement
