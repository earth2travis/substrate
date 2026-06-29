---
title: "IRL Mathematical Formalism: MDP Notation and Core Problem Structure"
tags:
- inverse-reinforcement-learning
- mathematics
- formalism
- reward-modeling
- value-learning
related:
- [[ng-russell-2000-irl-foundations]]
- [[ziebart-maxent-irl-alignment-conscience]]
- [[irl-theoretical-foundations]]
- [[irl-landscape-2000-2010]]
- [[principal-agent-theory]]
source: research/raw/irl-mathematical-formalism.md
ingested: 2026-06-29
---

# IRL Mathematical Formalism: MDP Notation and Core Problem Structure

## Summary

A compact reference document consolidating the mathematical notation and core problem structure of Inverse Reinforcement Learning. The forward problem (standard RL) and the inverse problem (IRL) share the same MDP formalism but operate in opposite directions. Understanding the shared notation is prerequisite to following any IRL algorithm.

## Forward Problem: Standard RL

A Markov Decision Process is defined as M = (S, A, T, gamma, R, s0), where S is the state space, A is the action space, T(s'|s,a) is the transition function, gamma is the discount factor, R: S to reals is the reward function, and s0 is the initial state distribution. The goal is to find a policy pi: S -> A maximizing expected cumulative discounted reward. The optimal value function satisfies the Bellman equation, and the optimal policy selects actions maximizing the Q-value at each state.

## Inverse Problem: IRL

In IRL, we observe expert demonstrations and must find a reward function R such that the expert policy is approximately optimal under R. The identifiability problem is critical: the mapping from R to optimal policy is many-to-one. Multiple reward functions produce the same optimal policy (e.g., zero everywhere, constant, or penalizing alternatives). Without additional constraints, the problem is ill-posed.

## Ng & Russell Maximum Margin

Instead of finding any R that makes the expert optimal, find the R that makes the expert's behavior look most optimal relative to all alternatives. This is formulated as a linear program maximizing the margin between the expert's Q-values and all alternative actions' Q-values, subject to normalization constraints.

## Maximum Entropy Extension

Ziebart et al. model behavior probabilistically: the probability of a trajectory is proportional to exp(total reward of the trajectory). The partition function normalizes this over all trajectories. The gradient of the log-likelihood has a clean form: the difference between the empirical feature counts from demonstrations and the expected feature counts under the current model.

## Cross-References

- Foundational paper analysis: [[ng-russell-2000-irl-foundations]]
- The MaxEnt resolution: [[ziebart-maxent-irl-alignment-conscience]]
- Theoretical bounds and complexity: [[irl-theoretical-foundations]]
- Intellectual lineage: [[irl-landscape-2000-2010]]
- The principal-agent structural parallel: [[principal-agent-theory]]