---
title: "Loops as Orchestration Primitive: From ReAct to Continuous Agent Orchestration"
tags:
  - finding
  - loops
  - orchestration
  - ralph-loop
  - goal-primitive
  - agent-native
  - cron
  - skills
  - cost-control
  - guardrails
related:
  - goal-primitive
  - goal-primitive-three-implementations
  - agent-orchestrator-pattern
  - agentic-architecture
  - harness-engineering
  - skills-as-portable-knowledge
  - automation-leverage
  - karpathy-autoresearch
  - progressive-autonomy
  - feedback-loop-discipline
source: research/raw/loops-x-conversation-june-2026.md
ingested: 2026-06-30
---

# Loops as Orchestration Primitive: From ReAct to Continuous Agent Orchestration

## Summary

Peter Steinberger's June 2026 tweet, "you shouldn't be prompting coding agents anymore, you should be designing loops that prompt your agents," cleared 2.2 million views and ignited a brawl over what "loops" actually means. Boris Cherny, creator of Claude Code, supplied the cleanest definition: a loop is a small program that prompts the coding agent, reads what it produced, decides whether it is done, and if not, prompts it again. The human stops being the thing inside the loop typing prompts and becomes the author of the loop.

The thread that matters is not "prompt engineering is dead." It is the five-stage lineage from academic while-loops to continuous multi-agent orchestration, and the three hard stops every production system now converges on. Cherny deleted his IDE in November 2025 and has not opened it since. In the last 30 days, 100% of his Claude Code contributions were written by Claude Code. He landed 259 PRs. The job did not vanish; it moved up an altitude, from writing the code to writing the thing that writes the code.

## The Five-Stage Lineage

"Loop" hides at least five different things, oldest to newest.

**Stage One: Academic While-Loop (ReAct, 2022).** Yao et al. formalized the pattern at NeurIPS: the model reasons, calls a tool, reads the result, repeats until done. One model, one loop, a human watching. The seed everything later grew from.

**Stage Two: AutoGPT (2023).** Gave the agent a goal and let it prompt itself. Became famous for spinning forever doing nothing. That failure seeded years of "agents are a toy."

**Stage Three: The Ralph Loop (July 2025).** Geoffrey Huntley published an almost insultingly simple bash one-liner that pipes the same prompt file into the agent over and over: `while :; do cat PROMPT.md | claude-code ; done`. Its real innovation was discipline: every iteration resets the context to a fixed set of anchor files instead of letting the conversation grow. Huntley built an entire programming language with it for about $297. The spinoff ecosystem includes `mikeyobrien/ralph-orchestrator` (2.9k stars), a TypeScript port, a multi-agent extension with MemPalace memory (138 stars), and others.

**Stage Four: Productized Ralph (/goal, Spring 2026).** Both Codex and Claude Code shipped a `/goal` command that runs the Ralph loop until a small validator model confirms the task is done. This is the stage the Substrate's [[goal-primitive]] analysis covers in detail.

**Stage Five: Continuous Orchestration Loop (Now).** What Steinberger and Cherny actually mean. Four things changed: the loop became the unit of work, not the task; loops started supervising other loops, concurrently and on a schedule; scheduling replaced the human kickoff (runs on infrastructure time); and durability became explicit, with git-backed state and crash recovery. The single-agent Ralph loop is old hat; multi-agent supervision is the new layer.

## It's Just a Cron Job with a Hat On

The best skeptic line from the thread: "Cronjobs have funny re-branding rn."

This is half right. The scheduling layer is cron. Cherny runs his on cron. The `/loop` command in Claude Code uses cron under the hood. What cron never had is the part in the middle. A cron job runs a fixed script. A loop runs a model that looks at the current state, decides what to do next, does it, checks whether it worked, and decides whether to keep going. The decision belongs to the agent, not the scheduler.

Stack those, let one loop dispatch and supervise others, give them durable shared state, and you have something cron cannot express. The honest framing: loops are cron plus a decision-maker in the body.

## Gas Town: The Deep End

Steve Yegge's Gas Town, launched January 2026, is the most complete instantiation of the continuous orchestration loop: 20 to 30 Claude Code instances coordinated by a Mayor agent, with patrol agents running continuous loops and state stored in git so work survives a crash. Open source at `gastownhall/gastown`.

## The Cost Inversion

Every AI agent shipped is a for-loop, an LLM call, and a try/catch. Once the model writes the code for almost nothing, the cost moves to the loop running it. Uber capped its engineers at $1,500 per person per tool per month for Claude Code and Cursor after burning its annual AI budget in four months.

The failure mode every production team is scared of: the loop that does not stop.

## Three Hard Stops

Every serious 2026 write-up on loops converges on the same three guardrails:

1. **Maximum iteration count.** cap the loop at a fixed number of passes.
2. **No-progress detection.** halt when consecutive iterations produce no delta.
3. **Token or dollar budget ceiling.** hard stop when spend crosses a threshold.

Without all three, a loop that does not stop will find you at 3am with a four-figure API bill. These map directly onto the budget enforcement problem identified in the [[goal-primitive-three-implementations]] comparison: Codex enforces a token budget, Hermes enforces a turn budget, Claude Code has no explicit budget yet.

## It's Not Loops. It's Skills.

The durable half of Steinberger's point: if you do something more than once, turn it into an automated skill. A loop with no reusable skills inside it is just a while-true around a stranger. A loop that calls a library of sharp, tested, named skills is a system that compounds.

This connects directly to [[skills-as-portable-knowledge]]: the reusable unit inside the loop is a skill, not a prompt. The loop provides the cadence; the skills provide the substance. A loop calling ad hoc prompts is fragile. A loop calling a curated skill library inherits every lesson encoded in those skills.

## Anthropic's Formal Framework

Anthropic's "Building Effective Agents" (Dec 19, 2024) formalizes the distinction that the thread was arguing past:

- **Workflows**: predefined, predictable. Prompt chaining, routing, parallelization, orchestrator-workers.
- **Agents**: flexible, model-driven decision-making. The model dynamically directs its own process and tool usage.

The recommendation: start with LLM APIs directly, not frameworks. Frameworks add abstraction that obscures prompts and responses. This is the same advice the [[harness-engineering]] analysis reaches: the harness is the product, and over-frameworked harnesses hide the prompts that actually matter.

## The Sisyphus Read

The thread's mot juste is also its warning. A loop with no termination condition is not orchestration. It is [[myth-of-sisyphus-camus]] in production: the same prompt, the same model, the same output, forever, billed by the token. The three hard stops are the exit condition Camus never granted Sisyphus. The loop is only worth running if it can prove it is done.

## Cross-References

- [[goal-primitive]] and [[goal-primitive-three-implementations]] for the productized Ralph loop and done-detection across Codex, Claude Code, and Hermes
- [[agent-orchestrator-pattern]] for the poll-dispatch-reconcile coordination loop
- [[agentic-architecture]] for the broader nine-component harness taxonomy
- [[harness-engineering]] for why the harness, not the model, is where value accrues
- [[skills-as-portable-knowledge]] for the durable unit inside the loop
- [[automation-leverage]] for the cost inversion that makes loop management the expensive resource
- [[karpathy-autoresearch]] for an earlier autonomous loop with fixed budgets and NEVER STOP autonomy
- [[progressive-autonomy]] for graduated trust via capability tiers
- [[feedback-loop-discipline]] for the nested-loop cadence model this operationalizes