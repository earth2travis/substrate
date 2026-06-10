---
title: "Fable 5: Structural Betting and Memory as Outer Loop"
tags:
  - finding
  - agent
  - loop
  - memory
  - model
  - experiment
  - anthropic
related:
  - goal-primitive
  - harness-engineering
  - karpathy-autoresearch
  - agent-memory
  - subagent-architecture
  - centaur-principle
  - feedback-loop-discipline
  - per-run-learning
  - synthesis-over-retrieval
source: research/raw/2026-06-10-designing-loops-with-fable-5.md
ingested: 2026-06-10
---

# Fable 5: Structural Betting and Memory as Outer Loop

## Core Claim

Anthropic's Fable 5 demonstrates that the quality of an agent loop depends on the model's ability to make *structural* bets based on feedback, not just *scalar* adjustments. In a controlled Parameter Golf experiment, Fable 5 achieved approximately **6x improvement** over Opus 4.7. The difference was not loop infrastructure. It was loop strategy: Fable 5 changed architecture when feedback indicated the current approach had plateaued; Opus 4.7 tuned constants and spun.

This is evidence that [[synthesis-over-retrieval]] applies to agent loops themselves: the model that maintains a coherent strategy across iterations outperforms the model that rediscovers its approach each time.

## The Parameter Golf Experiment

A constrained ML engineering challenge: train the best model possible within 16MB artifact, 10 minutes, and 8xH100. The agent loop must edit training code, launch training, read logs, judge results, and decide the next step. It is structurally parallel to Karpathy's AutoResearch: a single metric, a fixed budget, and autonomous iteration.

Key design decision: a **verifier sub-Agent** independently scores results in an isolated context window. This avoids the self-critique trap where a model evaluates its own output and confirms its own biases. The verifier is a concrete implementation of the generator-critic pattern documented in [[subagent-architecture]].

### Results Stratified

| Model | Strategy | Outcome |
|-------|----------|---------|
| **Opus 4.7** | Scalar adjustments: tune one constant, test, keep if positive | Small initial gain, then plateaued |
| **Fable 5** | Structural bets: change architecture, persist through quantization regression | ~6x improvement over baseline |

The 6x gap is not a marginal improvement. It suggests that model class determines not just execution quality but *exploration quality*: the ability to recognize when local optimization has failed and to pivot to a different hypothesis.

## Memory: The Outer Loop Across Sessions

The article frames memory as an outer loop that spans sessions. The model writes memory during a session; that memory is retrieved in future sessions. This is not storage. It is a recursive loop with five steps:

1. **Failure recording**: document what went wrong
2. **Investigating cause**: understand why
3. **Verifying diagnosis**: confirm the hypothesis
4. **Distilling into general rules**: extract portable knowledge
5. **Consulting rules rather than re-deriving**: apply accumulated understanding

Only Fable 5 could complete all five steps. On the Continual Learning Bench 1.0 (filesystem memory across independent sessions), Fable 5 reached 73% verification coverage (22 of 30 questions). Opus 4.7 reached Step 3 with ~17% median verification. Sonnet 4.6 stayed at Step 1.

This validates the [[per-run-learning]] pattern: one learning file per workflow run, capturing what happened and what to do differently. The progression from failure recording to rule consultation is exactly the graduation path described there. When the same lesson appears across multiple runs, it gets baked into the workflow itself.

## The Verifier Pattern Confirmed

The article independently confirms what [[subagent-architecture]] calls the generator-critic or Jidoka principle: for quality-critical work, use two agents, one to generate and one to review. The generator is susceptible to instruction bias and context overload. The critic catches what the generator misses because it operates in an isolated context window with no stake in the generator's output.

This is not an architectural preference. It is an empirical result. Self-critique has been "proven ineffective multiple times." Isolated verification is the pattern that produces reliable judgments.

## Implications for Agent Design

**Loop design > prompting.** The article's core thesis is that the shift from "prompting agents" to "designing loops" is now backed by internal Anthropic experiments. The [[goal-primitive]] (/goal) and Outcomes grader in Claude Managed Agents are the infrastructure layer; Fable 5 is the capability layer that makes the infrastructure actually work.

**Model tiering matters for loop depth.** The stratified results across Sonnet 4.6, Opus 4.7, and Fable 5 suggest that not every model can benefit equally from the same loop infrastructure. Routing routine work to cheaper models and complex reasoning to capable models is not just a cost optimization. It is a capability match. The wrong model in a sophisticated loop is wasted infrastructure.

**Memory is not a feature. It is a prerequisite.** The five-step memory progression shows that without the ability to distill and consult rules, a model cannot compound learning across sessions. This connects to [[agent-memory]]: the problem is not technology but architecture. The filesystem-as-memory approach works because the model can read, write, and reason about files. Specialized memory infrastructure is unnecessary when the model can already operate on the same primitives humans use.

**Feedback loops must be nested.** The Parameter Golf loop (modify, train, measure, decide) operates within a single session. The memory loop (failure to cause to verification to rule to consultation) operates across sessions. This is [[feedback-loop-discipline]] in practice: different frequencies answering different questions about system health.

**Human designs the loop; model executes within it.** This is the [[centaur-principle]] at the loop level. Lance Martin (the human) designed the verifier pattern, the scoring criteria, and the environment. Fable 5 executed within those constraints. The quality of the collaboration between human intent and model execution is what produced the 6x result.

## Sources

- Lance Martin, "Designing loops with Fable 5," X, June 9, 2026: https://x.com/RLanceMartin/status/2064397389189071163
- Continual Learning Bench 1.0: filesystem memory benchmark by @pgasawa's team
- Claude Managed Agents documentation: https://platform.claude.com/docs/en/managed-agents/overview
