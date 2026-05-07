---
title: "Agent Architectures: ReAct, Plan-and-Execute, and Reflection"
tags: [agents, architecture, llm, patterns]
related:
- agent-skills-as-onboarding
- agentic-systems-synthesis
source: research/raw/agent-architectures.md
---
# Agent Architectures: ReAct, Plan-and-Execute, and Reflection

## Summary

Every agent architecture answers one question: how should the model decide what to do next? The three dominant patterns are ReAct (reason then act), Plan-and-Execute (plan first, then execute), and Reflection (self-critique after generation).

## ReAct (Reasoning + Acting)

The workhorse. Alternates between Thought and Action, observing results before deciding the next step. Used by OpenAI function calling, Anthropic tool use, LangChain agents.

- Pros: Simple, robust, naturally handles uncertainty
- Cons: Myopic (optimizes locally, not globally), can wander without a plan

## Plan-and-Execute

Create a complete plan first, then execute each step. Often two models: a planner and an executor.

- Pros: Global coherence, inspectable plan, can estimate cost upfront
- Cons: Planning costs tokens before work, plans go stale, re-planning is expensive

Best for well-defined tasks in known domains. "Plan loosely, execute tightly": sketch direction, then ReAct for each step.

## Reflection / Self-Critique

Generate output, then critique and iterate. Can be single-model or dual-model (separate critic).

- Pros: Catches first-pass errors, improves without external feedback
- Cons: 2-3x token cost

Use when quality matters more than speed: writing, code review, analysis.

## The Hybrid Pattern

Most production agents combine: Plan loosely for direction, ReAct for execution, Reflection for quality gates. No single architecture dominates all tasks.