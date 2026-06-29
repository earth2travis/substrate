---
title: "Theoretical Foundations of IRL: Identifiability, Sample Complexity, and Complexity"
tags:
- inverse-reinforcement-learning
- theoretical-foundations
- identifiability
- sample-complexity
- computational-complexity
- statistical-learning-theory
- ai-alignment
related:
- [[ng-russell-2000-irl-foundations]]
- [[ziebart-maxent-irl-alignment-conscience]]
- [[irl-mathematical-formalism]]
- [[irl-landscape-2000-2010]]
- [[active-interactive-irl]]
- [[post-2018-irl-landscape]]
- [[principal-agent-theory]]
source: research/raw/2026-06-29-irl-theoretical-foundations.md
ingested: 2026-06-29
---

# Theoretical Foundations of IRL: Identifiability, Sample Complexity, and Complexity

## Summary

IRL asks a question that is, in a precise mathematical sense, harder than the forward RL problem: given behavior, recover the reward that rationalizes it. The difficulty is not merely algorithmic but structural. The mapping from reward functions to optimal policies is many-to-one, so the inverse is fundamentally ill-posed without additional constraints. This document surveys the theoretical foundations across nine domains: identifiability, sample complexity, regret bounds, computational complexity, information-theoretic lower bounds, generalization, robustness, comparative guarantees across variants, and reward overfitting.

## Identifiability: When Can the True Reward Be Recovered?

Ng and Russell (2000) established that the set of reward functions for which a given policy is optimal is a non-empty convex polyhedral cone of dimension at least |S| minus rank of the constraint matrix. If the rank is less than the number of states, the reward is not uniquely identifiable. The degrees of freedom include positive scaling and potential-based shaping. Ng, Harada, and Russell (1999) proved that adding a potential-based shaping function to the reward does not change the optimal policy. This means the reward is identifiable only up to an additive shaping term, the discrete-time analog of the null-space transformation in inverse optimal control (Kalman, 1964).

Unique recovery is possible under additional structural assumptions: restricting to a known linear feature basis with full-rank constraints, observing the actual value function (not just the policy), assuming sparsity, or assuming monotonicity in a known feature. In practice, no single assumption is universally applicable, and the community has shifted from exact recovery to reasonable recovery via regularization.

## Sample Complexity: How Many Demonstrations Are Needed?

The feature expectation matching framework (Abbeel & Ng, 2004) provides the foundational sample complexity result. If the reward is a linear combination of k known features, and the expert policy's feature expectations are estimated from m trajectories, then matching feature expectations to within epsilon requires O(k / epsilon^2 * (1 / (1-gamma)^2)) samples. This is polynomial in the number of features and the desired accuracy, independent of the state space size, which is a significant result for scalability.

For active IRL, Bajgar et al. (2025) proved PAC guarantees with Thompson sampling, showing that active learning can provably reduce the required number of queries. The bound is polynomial in the number of features, horizon, and accuracy. See [[active-interactive-irl]] for details.

## Computational Complexity

The LP formulation of Ng & Russell (2000) requires inverting the matrix (I - gamma P^pi), which is O(|S|^3) in the worst case. MaxEnt IRL requires computing the partition function via soft Bellman dynamic programming, which is O(|S| * |A| * T) per iteration for a finite horizon T. Deep IRL methods replace the tabular computation with neural network forward passes, but the underlying need to evaluate or approximate the partition function remains the computational bottleneck.

## Generalization and Robustness

The learned reward function may not generalize to new environments. Distributional shift is a fundamental challenge: the optimal policy under a learned reward in a new MDP may be completely misaligned with the expert's intent. Inverse Reward Design (Hadfield-Menell et al., 2017) treats the specified reward as a proxy for a latent design objective, using Bayesian inference to recover the true objective. Adversarial IRL (AIRL, Fu et al., 2018) enforces a potential-based shaping structure to recover rewards invariant to dynamics changes.

## The Unifying Thread

Every practical IRL algorithm implicitly or explicitly regularizes the solution space. The ambiguity problem is not solvable by more data. It is managed by structural assumptions: priors, inductive biases, constraints on the hypothesis space. The choice of regularization is not value-neutral. When we assume human behavior is approximately Boltzmann-optimal, we make a claim about human agency. When we regularize toward sparse or smooth rewards, we embed philosophical commitments about what values look like. This connects [[irl-theoretical-foundations]] directly to [[irl-moral-psychology-connection]]: the mathematical assumptions encode psychological commitments.

## Cross-References

- Foundational ambiguity result: [[ng-russell-2000-irl-foundations]]
- MaxEnt regularization: [[ziebart-maxent-irl-alignment-conscience]]
- Mathematical notation: [[irl-mathematical-formalism]]
- Active learning sample bounds: [[active-interactive-irl]]
- Modern approximation methods: [[post-2018-irl-landscape]]
- Structural parallels to delegation: [[principal-agent-theory]]