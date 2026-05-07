---
title: "Hermes Agent Self-Evolution Framework"
tags: [hermes-agent, evolution, optimization, agents, skills, dspy]
related:
- hermes-agent
- harness-engineering
- lean-software-delivery
- dark-factory
source: research/raw/hermes-self-evolution.md
---
# Hermes Agent Self-Evolution Framework

## Summary

Hermes Agent Self-Evolution is a standalone optimization pipeline that improves agent skills, prompts, tool descriptions, and code through automated search. It uses DSPy + GEPA (Genetic-Pareto Prompt Evolution, ICLR 2026 Oral) to evolve text artifacts without GPU training. Cost per run: ~$2-10.

## Key Claims

1. **Separate Optimization Repo:** The evolution system is completely separate from the agent. The agent doesn't know it's being optimized. Improvements deploy via git PRs, never auto-merged.
2. **Three Engines:** GEPA (reflective prompt evolution reading execution traces), MIPROv2 (Bayesian optimization fallback), Darwinian Evolver (git-based code evolution with test-driven fitness).
3. **Execution Trace-Driven Mutation:** GEPA reads execution traces to understand WHY things fail, producing targeted mutations rather than random search. Works with as few as 3 examples.
4. **Constraint Gates:** Every evolved variant must pass tests, size limits, caching compatibility, and semantic preservation. Prevents optimization from breaking the system.
5. **Phased Rollout:** Skills first (highest value, lowest risk), then tool descriptions, then prompts, then code. Each phase proves itself before the next begins.

## Patterns for Agent Factories

1. Keep agent runtime and improvement system separate
2. Instrument execution with structured traces for targeted optimization
3. Design configuration as discrete, independently optimizable text artifacts
4. Define constraint gates for any auto-generated agent configuration
5. All improvements go through reviewable artifacts (PRs, diffs)
6. Mine real conversation history for evaluation datasets

## Related

- [[hermes-agent]] — Parent agent platform
- [[harness-engineering]] — Agent-first development
- [[lean-software-delivery]] — Quality gates and continuous improvement
- [[dark-factory]] — Autonomous optimization as lights-out operation
