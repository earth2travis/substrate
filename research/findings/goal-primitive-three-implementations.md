---
title: "The /goal Primitive: Three Implementations Compared"
tags: [finding, goal, primitive, codex, claude-code, hermes, agent-native, orchestration, comparison]
related:
  - openai-codex-goal-command
  - anthropic-claude-code-goal-command
  - hermes-agent-goal-command
  - agent-platform-ecosystem
  - subagent-architecture
  - ai-composable-primitives
  - agent-orchestrator-pattern
  - mission-execution-chain
  - kanban-doctrine
source: research/raw/openai-codex-goal-command.md, research/raw/anthropic-claude-code-goal-command.md, research/raw/hermes-agent-goal-command.md
ingested: 2026-05-15
---

# The /goal Primitive: Three Implementations Compared

## The Convergence

In May 2026, three agent tools — OpenAI Codex CLI, Anthropic Claude Code, and Hermes Agent — converged on the same user-facing primitive: `/goal`. The syntax is nearly identical across all three. The semantics are not. Understanding the divergence is more instructive than celebrating the convergence.

## The Core Shift

`/goal` represents a shift from **prompting** (user drives every turn) to **assigning** (user defines done, agent drives toward it). The primitive says: "Here is what completion looks like. You figure out the path."

This is Auftragstaktik in code: the commander specifies intent; the subordinate chooses method.

## Comparison Table

| Dimension | OpenAI Codex CLI | Anthropic Claude Code | Hermes Agent |
|---|---|---|---|
| **Command syntax** | `/goal <objective>` | `/goal <condition>` | `/goal <text>` |
| **Subcommands** | `pause`, `resume`, `clear`, `edit` | `clear` (aliases: stop, off, reset, cancel) | `pause`, `resume`, `clear`, `subgoal` |
| **Scope** | Thread-scoped (SQLite) | Session-scoped | Session-scoped (SessionDB) |
| **Persistence** | Survives across turns; survives thread restarts | Lost on `/clear`; counters reset on `--resume` | Survives session restarts; survives cross-platform handoff |
| **Continuation** | Auto-schedules when idle | Auto-continues across turns | Auto-continues via judge after every assistant turn |
| **Done detection** | Model calls `update_goal` tool with `status: "complete"` | Small evaluator model (Haiku) checks condition | Auxiliary "judge" model returns JSON `{"done": true}` |
| **Budget** | Token budget (soft stop), time tracked | No explicit budget | Turn budget (default 20), configurable |
| **Resume** | `pause`/`resume` within thread | `--resume` restores active goals, resets counters | `/goal resume` restores from SessionDB |
| **Feature flag** | `features.goals = true` (experimental) | Built-in, v2.1.139+ | Built-in |
| **Failure mode** | Approval policy ambiguity, restart bugs | Acknowledgement loops, token burn on impossible goals | Judge parse failures (fail-open), conservative done on blocked goals |

## Architectural Divergence: Three Philosophies

### Codex: Data Model First

Codex treats `/goal` as a first-class data model. SQLite table with migrations, OpenTelemetry lifecycle metrics, steering prompt templates, token/time accounting. The goal is an entity with state transitions (`active` → `paused` → `complete` → `budget_limited`). The model self-reports completion via a tool call (`update_goal`).

**Implication**: Most engineered, most explicit, but feature-flagged experimental. The data model is rich but the UX is still settling (open issues on restart behavior and approval policy interaction).

### Claude Code: Evaluator Pattern

Claude Code separates the goal from the main model. A small fast evaluator (default Haiku) reads the conversation and the condition, returning a binary verdict. The main model does not self-report; it is judged. This is architecturally distinct and theoretically attractive: it prevents the main model from confidently declaring done when it has not actually achieved the goal.

**Implication**: Lighter weight than Codex, no persistence, no budget enforcement. The evaluator is elegant but community reports show it can get stuck in acknowledgement loops or burn tokens on unsatisfiable conditions.

### Hermes: Judge Loop with Session Persistence

Hermes uses a JSON-structured judge model that returns `{"done": true, "reason": "..."}`. It has fail-open semantics (broken judge defaults to `continue`, never wedges). The goal survives session restarts and cross-platform handoff (`/handoff`). A turn budget (default 20) prevents runaway loops.

**Implication**: Most robust against failure modes. The judge is configurable (can route to a cheap model). The cross-platform persistence is unique. But `/goal` is orthogonal to Hermes' Kanban and delegation features; they are separate systems.

## The Done Detection Problem

All three face the same hard problem: how does an agent know it is done?

| Approach | Strength | Weakness |
|---|---|---|
| **Self-report** (Codex) | Model knows its own intent | Overconfidence, false completion |
| **Evaluator** (Claude Code) | Separation of concerns, prevents false completion | Can get stuck, no budget, counter resets |
| **Judge** (Hermes) | Structured verdict, configurable, fail-open | Adds latency, requires auxiliary model setup |

This is the agent-native equivalent of the principal-agent problem's **moral hazard** dimension. The principal (user) cannot observe the agent's hidden reasoning. All three implementations are attempts to solve the same theoretical problem with different engineering tradeoffs.

## The Persistence Gap

Only Codex and Hermes persist goals across sessions. Claude Code loses the goal on `/clear` and resets counters on `--resume`. This matters for long-running tasks that span sessions. In the agent-native operating model, persistence is not optional: the agent must remember what it was doing when the human returns.

## The Budget Problem

Only Codex (token budget) and Hermes (turn budget) enforce budgets. Claude Code has no explicit budget mechanism. In an agent-driven ecosystem where agents run autonomously, unbounded loops are a failure mode. Budget enforcement is a precondition for safe autonomy.

## The Orchestration Layer

Hermes is the only one of the three that is explicitly designed as an orchestrator. Codex and Claude Code are coding workers. Hermes coordinates between them via Kanban and delegation. The tweet by @Saboo_Shubham_ describes a builder-reviewer-orchestrator pattern where:
- **Builder** (Codex) implements via `/goal`
- **Reviewer** (Claude Code) reviews via `/goal`
- **Orchestrator** (Hermes) manages handoffs via Kanban cards

This pattern works because all three speak the same `/goal` syntax, even though their implementations differ. The primitive enables composition across tools that share nothing else.

## Implications for Agent-Native Project Management

1. **Primitive > Implementation.** The syntax convergence matters more than the implementation divergence. A new coding tool that adopts `/goal` joins the pipeline without changing the orchestrator.

2. **Verification is the contract.** Without verification, `/goal` is a fancier prompt. With verification, it becomes a contract. Hermes' explicit verifier (running tests/build itself) is the most complete implementation of this principle.

3. **Budget enforcement is safety.** Unbounded autonomous loops are dangerous. Codex and Hermes implement budgets; Claude Code does not yet.

4. **Persistence is memory.** Goals that disappear when the session ends are not goals. They are prompts with delusions of grandeur.

5. **The done detection problem is unsolved.** Self-report, evaluator, and judge are all approximations. None guarantees correctness. The theoretical problem (how does a principal verify an agent's hidden action?) remains open.

## The Principal-Agent Parallel

`/goal` is a civilian implementation of mission command. The user specifies intent (the objective). The agent chooses method. The gap between intent and verification is the agency problem. All three tools are engineering responses to the same theoretical tension:
- Codex leans toward monitoring (data model, metrics, budgets)
- Claude Code leans toward evaluation (separate judge)
- Hermes leans toward bonding (turn budgets, fail-open, conservative termination)

The optimal design, per agency theory, is a portfolio. No single mechanism solves the problem.

## Sources

- OpenAI Codex CLI: `developers.openai.com/codex/cli/slash-commands`, GitHub `openai/codex`
- Anthropic Claude Code: `code.claude.com/docs/en/goal`, `code.claude.com/docs/en/commands`
- Hermes Agent: `hermes-agent.nousresearch.com/docs/user-guide/features/goals`, GitHub `NousResearch/hermes-agent`
- Tweet analysis: `x.com/Saboo_Shubham_/status/2054988166541770782`
