---
title: Harness Engineering
created: 2026-04-08
updated: 2026-04-10
type: concept
tags: [agent, development, operations, platform]
sources:
  [
    raw/articles/openai-harness-engineering-article.md,
    raw/transcripts/symphony-harness-engineering-transcript-2026-04-07.md,
    raw/transcripts/openai-harness-engineering-ryan-lopopolo-2026.md,
    raw/transcripts/ryan-lopopolo-harness-engineering-full.md,
  ]
---

# Harness Engineering

> Discipline of designing environments, specifying intent, and building feedback loops that enable coding agents to do reliable work at scale. The primary job shifts from writing code to enabling agents.

## Origin

- Term from the article raw/articles/openai-harness-engineering-article.md by [[ryan-lopopolo]] (Feb 11, 2026)
- 0 lines of human-written code, ~1M lines of codebase, built in 1/10th the time
- 1,500 PRs merged by 7 engineers (started at 3)
- Throughput: 3.5+ PRs/engineer/day, increasing over time
- Started late August 2025 with empty git repository

## Core Philosophy

**"Humans steer. Agents execute."**

The engineering team's primary job is no longer to write code, but to:
- Design environments
- Specify intent
- Build feedback loops
- Allow Codex agents to do reliable work

## Key Principles

### 1. No Manually-Written Code
Even the initial AGENTS.md was written by Codex. Everything in the codebase -- product code, tests, CI config, release tooling, internal dev tools, docs, eval harnesses, review comments, repo management scripts, production dashboard definitions -- is agent-generated.

### 2. Work Depth-First, Build Building Blocks
Early progress was **10x slower** than manual coding (first 1.5 months). But "because we paid that cost, we ended up getting to something much more productive than any one engineer could be because we built the tools, the assembly station for the agent to do the whole thing."

When something fails: never "try harder" -- ask "**what capability is missing, and how do we make it both legible and enforceable**?

### 3. "Give Codex a Map, Not a 1,000-Page Manual"
The "one big AGENTS.md" failed in four predictable ways:

1. **Context is a scarce resource** -- giant file crowds out task, code, docs
2. **Too much guidance becomes non-guidance** -- when everything's important, nothing is
3. **It rots instantly** -- graveyard of stale rules, agent can't tell what's true
4. **It's hard to verify** -- single blob doesn't work with mechanical checks

Instead: AGENTS.md = table of contents (~100 lines). Knowledge = structured docs/ directory. A "**doc-gardening**" agent scans for stale docs, opens fix-up PRs.

### 4. Agent Legibility is the Goal
Optimized for **Codex's legibility first**, human preferences second. Anything the agent can't see in-context effectively doesn't exist.

- Favored dependencies fully internalizable in-repo
- Reimplemented generic p-limit as custom map-with-concurrency: integrated with OpenTelemetry, 100% test coverage, exact behavior for runtime
- Pulling system context into agent-readable form increases leverage for all agents

### 5. Enforce Architecture Early
"This is architecture you'd normally postpone until hundreds of engineers. With coding agents, it's an early prerequisite."

**Rigid layered model**:
```
Types → Config → Repo → Providers → Service → Runtime → UI
                                                         ↑
Utils ──────────────────────────────────────────────────┘
```

Cross-cutting concerns (auth, connectors, telemetry, feature flags) through Providers only. Custom linters enforce structure -- error messages inject remediation instructions into agent context.

### 6. Chrome DevTools MCP for QA
- App bootable per git worktree -- one instance per change
- Chrome DevTools Protocol wired into agent runtime
- DOM snapshots, screenshots, navigation skills
- Codex reproduces bugs, validates fixes, reasons about UI directly
- Codex records video of failures and fixes

### 7. Local Observability Stack
- Ephemeral per worktree: Vector → Victoria Logs/Metrics/Traces
- Query via LogQL, PromQL, TraceQL
- Prompts like "ensure startup < 800ms" or "no span > 2s in critical journeys" become tractable
- Single Codex runs work 6+ hours on one task (while humans sleep)

### 8. Full Autonomy Pipeline
From a single prompt, Codex can now:
1. Validate codebase state
2. Reproduce reported bug
3. Record video demonstrating failure
4. Implement fix
5. Validate fix by driving the app
6. Record second video demonstrating resolution
7. Open PR
8. Respond to agent/human feedback
9. Detect/remediate build failures
10. **Escalate to human only when judgment required**
11. Merge the change

### 9. Entropy and Garbage Collection
Full autonomy introduces drift -- Codex replicates existing patterns, even suboptimal ones. Manual cleanup (Fridays, 20% of week) for "AI slop" didn't scale.

**Solution**: Encode "golden principles" into repository. Recurring background Codex tasks scan for deviations, update quality grades, open targeted refactoring PRs. Most reviewed in <1 min, automerged.

"Technical debt is like a high-interest loan: it's almost always better to pay it down continuously in small increments than to let it compound and tackle it in painful bursts."

## The Ralph Wiggum Loop

To drive a PR to completion: instruct Codex to review its own changes locally, request additional agent reviews, respond to feedback, iterate until all agent reviewers are satisfied.

## Throughput Changes the Merge Philosophy

- Minimal blocking merge gates
- Pull requests are short-lived
- Test flakes: follow-up runs, not blocking
- Agent throughput ≫ human attention → corrections cheap, waiting expensive

## What's Still Unknown

- How architectural coherence evolves over years in fully agent-generated systems
- Where human judgment adds most leverage
- How system evolves as models become more capable

> "Building software still demands discipline, but the discipline shows up more in the scaffolding rather than the code."

## Historical Precedent: The [[chief-engineer-system]] (Shusa)

The Shusa role at Toyota is a historical precedent for harness engineering. A Shusa was a single individual who:
- Held the complete product vision without doing detailed engineering work
- Integrated hundreds of specialists into a coherent outcome
- Made trade-off decisions across competing subsystems
- Ensured quality through direct observation (genchi genbutsu)
- Developed engineers through coaching and structured feedback

A harness engineer is a **Shusa for AI agents**. Where the Shusa steered human specialists, the harness engineer steers coding agents. The integration challenge is identical — only the "workers" have changed from humans to autonomous agents. This makes the Toyota Shusa system highly relevant study for anyone building [[dark-factory]] infrastructure.

## Connection to [[lean-software-development]]

Harness engineering is lean applied to the extreme:
- **Eliminate waste**: Humans coding is waste when agents do it 10x faster
- **Decide as late as possible**: Defer code structure to agent
- **Build Integrity In**: Custom linters, structural tests, quality scoring
- **See the whole**: Full observability, metrics on agent performance
- **Entropy management** = continuous improvement at scale

## Relationship to [[llm-wiki-pattern]]

The knowledge structure (AGENTS.md as table of contents, docs/ as knowledge base, doc-gardening agent) maps directly to the index.md/log.md pattern. Both solve the same problem: making knowledge visible and maintained without human overhead.

## Related
- [[ryan-lopopolo]] -- Pioneer of harness engineering at OpenAI Frontier
- [[symphony-orchestrator]] -- Parallel agent orchestration system
- [[lean-software-development]] -- Theoretical foundation
- [[codex]] -- Primary tool used
- [[spec-driven-development]] -- Distribution methodology
- [[dark-factory]] -- Zero-human-code concept
- [[llm-wiki-pattern]] -- Similar knowledge-visibility pattern
- [[openai-frontier]] -- The team building this


## Evals as Harness Improvement Signal

Viv (@Vtrivedy10) at LangChain proposed "Better Harness" — using evaluations as a learning signal for autonomous harness improvement in AI agent systems (April 8, 2026). The key insight: to autonomously build a better harness, you need a strong learning signal to hill-climb on. Evals provide that signal.

This connects to process philosophy: **the agent is a process (not a substance) whose behavior is defined by its harness configuration.** The harness is the "form" through which the agent's "becoming" is shaped — a structural process determining output, not an enduring entity with fixed properties.

See [[process-without-substance]] for full philosophical mapping.

## Sources
- raw/articles/openai-harness-engineering-article.md
- raw/transcripts/symphony-harness-engineering-transcript-2026-04-07.md
  - raw/2026-04-08_better-harness-tweet.md
