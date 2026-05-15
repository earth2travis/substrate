---
title: "The /goal Primitive: Command by Intent for Coding Agents"
tags: [concept, goal, primitive, intent, codex, claude-code, hermes, agent-native, orchestration, mission-command, auftragstaktik, delegation]
related:
  - goal-primitive-three-implementations
  - mission-command
  - mission-execution-chain
  - principal-agent-theory
  - kanban-doctrine
  - agent-orchestrator-pattern
  - subagent-architecture
  - agent-platform-ecosystem
  - ai-composable-primitives
  - progressive-autonomy
  - centaur-principle
  - workflow-as-contract
source: research/findings/goal-primitive-three-implementations.md
created: 2026-05-15
updated: 2026-05-15
---

# The /goal Primitive: Command by Intent for Coding Agents

## The Claim

`/goal` is an emerging primitive for agent-native project management. It is not a feature of any single tool. It is a structural pattern: the human defines what "done" looks like, and the agent works toward it autonomously until completion, budget exhaustion, or explicit interruption. In May 2026, OpenAI Codex CLI, Anthropic Claude Code, and Hermes Agent all converged on the same syntax despite sharing nothing else. The convergence proves the pattern is not incidental. It is optimal.

## What /goal Actually Is

A regular prompt asks an agent for the next response. The user reads what comes back, decides if it is right, and pushes the agent forward. The user is driving every turn.

`/goal` inverts this. The user writes down what "done" looks like, submits it once, and the agent drives toward the target. The user steps back. The agent steps forward.

This is not "a prompt with the word goal in it." The real primitive lives inside an interactive worker session. You launch the CLI, submit `/goal`, and you walk away. The goal stays active until it is achieved, paused, blocked, cleared, or it runs out of budget.

## The Structural Parallel to Mission Command

`/goal` is Auftragstaktik in code. The user specifies intent (the objective). The agent chooses method. The agent has infinite correct answers and one way to fail: missing the intent.

| Military Mission Command | Agent /goal |
|---|---|
| Commander's Intent | The goal text: what "done" looks like |
| Disciplined Initiative | The agent selects tools, strategies, decomposition |
| Backbrief | Done detection: how the agent knows it achieved the goal |
| Tolerance for Friction | Budget enforcement and failure modes |
| Shared Mental Models | The Substrate: every agent reads the same knowledge base |

The parallel is not metaphorical. It is structural. Both systems solve the same problem: how to delegate purpose without destroying initiative.

## The Three Implementations: Convergence and Divergence

Three tools converged on the same syntax. Their implementations diverge in instructive ways:

| Dimension | OpenAI Codex CLI | Anthropic Claude Code | Hermes Agent |
|---|---|---|---|
| **Scope** | Thread-scoped (SQLite) | Session-scoped | Session-scoped (SessionDB) |
| **Persistence** | Survives thread restarts | Lost on `/clear` | Survives session restart and cross-platform handoff |
| **Done detection** | Model self-reports via tool call | Small evaluator model (Haiku) judges | Auxiliary judge model returns JSON verdict |
| **Budget** | Token budget (soft stop) | No explicit budget | Turn budget (default 20) |
| **Subcommands** | `pause`, `resume`, `clear`, `edit` | `clear` | `pause`, `resume`, `clear`, `subgoal` |

The convergence (same syntax, same intent) matters more than the divergence (different persistence, different done detection, different budgets). The primitive enables composition across tools that share nothing else.

## The Done Detection Problem

All three implementations face the same hard problem, and it is the agent-native equivalent of moral hazard: how does an agent know it is done when the principal cannot observe its reasoning?

**Self-report** (Codex): The model calls a tool to declare completion. Strength: the model knows its own intent. Weakness: overconfidence, false completion, restarting after done.

**Evaluator** (Claude Code): A separate small model reads the conversation and judges whether the condition is met. Strength: separation of concerns prevents false completion. Weakness: can get stuck in acknowledgement loops, no budget enforcement.

**Judge** (Hermes): A structured JSON verdict from an auxiliary model. Strength: fail-open semantics (broken judge defaults to continue), configurable, conservative on blocked goals. Weakness: adds latency, requires setup.

None of these solves the problem perfectly. All are engineering tradeoffs around the same theoretical boundary condition: the principal cannot observe the agent's hidden action.

## The Primitive Enables Composition

The tweet by @Saboo_Shubham_ describes the builder-reviewer-orchestrator pattern:
- **Builder** (Codex): takes a spec, implements via `/goal`
- **Reviewer** (Claude Code): reads the result, finds issues via `/goal`
- **Orchestrator** (Hermes): coordinates handoffs via Kanban cards, verifies final output

This pattern works because all three speak the same `/goal` syntax. The next coding tool that adopts `/goal` joins the pipeline without changing the orchestrator. This is what good primitives do: they enable composition across tools that were not designed to work together.

## /goal and the Mission Execution Chain

`/goal` maps directly onto the five-domain chain:

| Chain Layer | /goal Equivalent |
|---|---|
| Why | The user's strategic intent (not explicitly in `/goal` text, but implied) |
| BHAG | The project or system being built |
| Mission | The specific `/goal` text |
| Objectives | The "done" criteria within the goal |
| Projects | The agent's plan of action |
| Tasks | Individual tool invocations |
| Execution | The tool output |

The handoff from Mission (goal text) to Objectives (done criteria) is where intent is most likely to be lost. A poorly written goal — "fix the bug" versus "ensure all API routes return proper error codes with logging" — creates the same cascade problem as a poorly written OPORD Paragraph 2.

## The Verification Principle

Without verification, `/goal` is just a fancier prompt. With verification, it becomes a contract.

Hermes implements this most completely: after Codex marks a build done, Hermes runs `npm test` and `npm run build` itself. It does not trust the worker's self-report. This is the agent-native equivalent of the backbrief: the subordinate presents results, but the commander verifies them.

The verification principle applies at every layer:
- Builder self-reports → orchestrator verifies
- Agent claims done → judge/evaluator verifies
- Model declares completion → human reviews

## The Budget Problem

Unbounded autonomous loops are dangerous. Only Codex (token budget) and Hermes (turn budget) enforce explicit budgets. Claude Code has no explicit budget mechanism. In an ecosystem where agents run in the background while humans sleep, budget enforcement is a safety precondition, not a convenience.

Budget is the agent-native equivalent of the military principle that subordinates must not expend resources indefinitely without reporting. It is also the civilian equivalent of Holmstrom's result: someone must bear the cost of runaway agency.

## The Persistence Problem

Goals that disappear when the session ends are not goals. They are prompts with delusions of grandeur.

Codex persists goals in SQLite across thread restarts. Hermes persists in SessionDB across session restarts and cross-platform handoff. Claude Code loses the goal on `/clear` and resets counters on `--resume`. For long-running agent-native operations, persistence is not optional. The agent must remember what it was doing when the human returns.

## /goal as a Coordination Primitive

`/goal` is not merely a coding convenience. It is a coordination primitive. It enables:

1. **Parallel execution**: Multiple `/goals` run in parallel across different repos, branches, or worktrees
2. **Sequential pipelines**: Builder goal → Reviewer goal → Fix goal, coordinated by an orchestrator
3. **Conditional work**: Skipped cards when review passes; fix loops when review blocks
4. **Visible state**: Kanban cards track goal status, PID, repo, done criteria

These patterns are impossible with one-shot prompting. They require a primitive that defines done and persists across turns.

## Implications for Agent-Native Operations

1. **Primitive > Implementation.** The syntax convergence matters more than the implementation divergence. A new tool that adopts `/goal` joins the ecosystem.

2. **Verification is mandatory.** Without it, the primitive collapses into a prompt. The orchestrator must verify worker output, not trust self-report.

3. **Budget enforcement is safety.** Unbounded loops are a distinct failure mode from incorrect output.

4. **Persistence is memory.** Goals must survive session boundaries.

5. **The done detection problem is open.** Self-report, evaluator, and judge are all approximations. The theoretical problem remains unsolved.

6. **Composition beats monopoly.** The builder-reviewer-orchestrator pattern works because three different teams converged on the same primitive. If they had invented incompatible formats, no orchestrator could route between them.

## Synthesis

`/goal` is the most concrete civilian implementation of mission command yet built. It takes the philosophy of Auftragstaktik — command by intent, not by instruction — and makes it executable. The human specifies what "done" looks like. The agent figures out how to get there. The orchestrator verifies that the goal was actually achieved.

The primitive is young. The implementations diverge. The theoretical problems (done detection, budget enforcement, persistence) are not solved. But the pattern is structural, not incidental. It will outlast any implementation.

The next coding tool that adopts `/goal` will join a pipeline that already works. That is what good primitives do.

## Related

- [[goal-primitive-three-implementations]] — Detailed comparison table and analysis
- [[mission-command]] — Auftragstaktik as agent operating system
- [[mission-execution-chain]] — The five-domain handoff chain
- [[principal-agent-theory]] — The economics of delegation
- [[kanban-doctrine]] — Auftragstaktik as agent operating system
- [[agent-orchestrator-pattern]] — Poll-dispatch-reconcile loop
- [[subagent-architecture]] — Seven design principles for coordinating sub-agents
- [[agent-platform-ecosystem]] — Gateway/specialist split across platforms
- [[ai-composable-primitives]] — Primitives as the building blocks of agent systems
- [[progressive-autonomy]] — Graduated trust via capability tiers
- [[centaur-principle]] — Human + AI + process beats any combination with inferior process
- [[workflow-as-contract]] — Agent behavior versioned in-repo via policy files
