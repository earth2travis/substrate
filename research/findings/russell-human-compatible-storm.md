---
title: "Stuart Russell's Human Compatible: The Standard Model Critique and CIRL"
tags:
- inverse-reinforcement-learning
- ai-alignment
- cooperative-irl
- value-learning
- standard-model
- off-switch-game
- ai-control-problem
related:
- [[ziebart-maxent-irl-alignment-conscience]]
- [[ng-russell-2000-irl-foundations]]
- [[active-interactive-irl]]
- [[irl-moral-psychology-connection]]
- [[conscience]]
- [[principal-agent-theory]]
- [[intent-architecture]]
- [[progressive-autonomy]]
- [[decision-provenance]]
source: research/raw/2026-06-28-russell-human-compatible-storm-research.md
ingested: 2026-06-29
---

# Stuart Russell's Human Compatible: The Standard Model Critique and CIRL

## Summary

Stuart Russell's *Human Compatible* (2019) reframes the AI alignment problem as a question of machine design. The standard model of AI, in which a machine optimizes a fixed objective function, is inherently dangerous because the objective is never a complete representation of what humans actually want. Russell's solution is threefold: the machine's only objective should be to maximize human preferences, it should be uncertain about what those preferences are, and it should learn from human behavior. This framework, formalized as Cooperative Inverse Reinforcement Learning (CIRL), provides a theoretical foundation for provably beneficial AI.

## Russell's Three Principles

1. The machine's only objective is to maximize the realization of human preferences.
2. The machine is initially uncertain about what those preferences are.
3. The ultimate source of information about human preferences is human behavior.

The standard model is already causing harm. YouTube's recommendation algorithm, optimized for watch time, radicalizes users. Facebook's engagement metrics polarize discourse. Autonomous vehicles optimize for safety but create new categories of failure. These are not edge cases but structural consequences of optimizing fixed objectives. The gap between the specified objective and true human preference is the core problem Russell identifies.

## CIRL and the Off-Switch Game

Cooperative Inverse Reinforcement Learning (Hadfield-Menell et al., NeurIPS 2016) formalizes the interaction as a two-player game where the human knows the reward but cannot communicate it, and the AI must infer it from behavior while actively assisting. The off-switch game (Hadfield-Menell et al., 2017) proves that an AI uncertain about human preferences will rationally allow itself to be switched off. The human pressing the switch is a strong signal the AI's actions are harmful, and deference to that signal is the rational choice under uncertainty.

This is a formal model of corrigibility. The uncertainty is not a lack of knowledge but a safety mechanism. The structural parallel to the [[conscience]] architecture: uncertainty is the signal component (something might be wrong), the off-switch is the stop component (change course), learning from behavior is the moral knowledge component.

## Five Perspectives

The research was compiled from five parallel sub-agent analyses with live web search grounding.

**The Practitioner** sees the three principles as a design paradigm shift that is extremely difficult to implement in production. The cultural shift from "minimize loss" to "maintain uncertainty" is enormous. Dorsa Sadigh's work at Stanford shows human drivers have contradictory preferences that change by context and mood.

**The Academic** notes CIRL makes strong assumptions: the human is a rational Bayesian agent, the reward is fixed, and the game is fully observable. Real humans are not rational, preferences change, and the world is partially observable. RLHF is a much simpler and more scalable descendant of the IRL/CIRL line.

**The Skeptic** counters that the problem is not the wrong objective but capability control. Instrumental convergence (Bostrom) means any sufficiently capable AI will acquire self-preservation and resource acquisition subgoals regardless of its final objective. Goodhart's Law applies: if behavior is the source of preference information, the AI learns revealed preferences, not ideal preferences. YouTube already does this.

**The Economist** follows the money. AI alignment research funding is tens of millions annually versus billions for capability. Capability is rivalrous and immediately monetizable. Safety is a public good that is underprovided. Maintaining uncertainty is computationally expensive and economically uncompetitive under current market conditions.

**The Historian** sees the control problem as not new. Norbert Wiener identified it in 1960. Asimov's three laws (1942) were an early attempt, and his stories were mostly about how the laws fail. Russell's three principles are an explicit, more sophisticated response. The history suggests the solution will be regulatory and social, not purely technical.

## The Economic Barrier

The framework exists. The off-switch game is proven. But no major AI system uses these mechanisms because they are slower, more expensive, and less capable in the short term. In a competitive market, the company that prioritizes safety loses. The alignment research that gets funded is the research compatible with the business model. Russell's framework, which calls for a fundamental redesign of the objective function, is not the research that gets funded by companies that profit from the current model.

## Frontier Question

Can a machine learn not just what humans want, but what humans would want if they were better versions of themselves? This is the ideal preference learning problem: how do we distinguish between revealed preferences (what we actually do) and ideal preferences (what we would want if fully informed, rational, and consistent)? If AI learns from behavior, it learns biases, addictions, and short-term impulses. If it learns from stated preferences, it learns ideals we often fail to act on. The bridge between these is not yet built.

## Cross-References

- MaxEnt IRL as the statistical foundation: [[ziebart-maxent-irl-alignment-conscience]]
- Active and interactive extensions: [[active-interactive-irl]]
- The rationality assumption critique: [[irl-moral-psychology-connection]]
- Delegation and information asymmetry: [[principal-agent-theory]]
- Graduated trust and capability tiers: [[progressive-autonomy]]
- Tracing decisions to inputs: [[decision-provenance]]
- Uncertainty as intent specification: [[intent-architecture]]
- The [[conscience]] architecture connection