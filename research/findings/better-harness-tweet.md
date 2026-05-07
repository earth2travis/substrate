---
title: "Better Harness: A Recipe for Harness Hill-Climbing with Evals"
tags: [agents, harness, evals, ai-engineering]
related:
  - [[harness-engineering]]
  - [[proof-of-work]]
  - [[agent-native-operations]]
  - [[reference-free-evaluation]]
source: research/raw/better-harness-tweet.md
---

# Better Harness: A Recipe for Harness Hill-Climbing with Evals

**Author:** Viv (@Vtrivedy10), LangChain
**Date:** April 8, 2026
**Source:** X Article

## TL;DR

> We can build better agents by building better harnesses. But to autonomously build a "better" harness, we need a strong learning signal to "hill-climb" on. We share how we use evals as that signal.

## Core Thesis

The harness (the agent's configuration, tools, prompts, and constraints) is not a static setting. It is a dynamic surface that can be systematically improved. Evaluations provide the gradient: they tell you whether a change to the harness made the agent better or worse.

This connects to process philosophy themes: the agent as process (not substance) whose behavior is defined by its harness configuration. The harness is the "form" through which the agent's "becoming" is shaped. Structural process determining output, not an enduring entity with fixed properties.

## The Hill-Climbing Loop

1. Measure agent performance on a task (eval)
2. Modify the harness (prompt, tool, constraint)
3. Re-measure performance
4. Keep changes that improve; discard changes that regress

The eval is the compass. Without it, harness changes are shots in the dark.

## Relevance

This aligns with our harness engineering discipline: every agent capability should be backed by evaluation. The harness is not "set and forget." It is a living configuration that improves through measured iteration.

See also: [[proof-of-work]] for layered verification of autonomous output, and [[mission-critical-evals-at-scale]] for production eval infrastructure.
