---
title: "Ng & Russell (2000): IRL as Linear Programs and the Ambiguity Problem"
tags:
- inverse-reinforcement-learning
- foundations
- reward-modeling
- ambiguity
- linear-programming
- value-learning
- ai-alignment
related:
- [[ziebart-maxent-irl-alignment-conscience]]
- [[irl-landscape-2000-2010]]
- [[irl-mathematical-formalism]]
- [[irl-theoretical-foundations]]
- [[principal-agent-theory]]
- [[conscience]]
- [[intent-architecture]]
source: research/raw/2026-06-28-ng-russell-2000-irl-summary.md
ingested: 2026-06-29
---

# Ng & Russell (2000): IRL as Linear Programs and the Ambiguity Problem

## Summary

Ng and Russell (2000) introduced Inverse Reinforcement Learning as a formal problem within the MDP framework: given an expert's optimal policy and an MDP without a reward function, recover the reward R that makes that policy optimal. This inversion is the logical dual of standard RL, where a reward is given and the task is to find an optimal policy. The motivation is practical: reward engineering is notoriously difficult, while expert demonstrations are abundant. If we can learn the reward from observation, we can deploy standard RL to generalize to new states or altered dynamics.

## The Ambiguity Problem

The paper's first theoretical insight is that the inversion is fundamentally ill-posed. For any observed policy, infinitely many reward functions make it optimal. The zero reward function makes every policy optimal. Positive affine transformations preserve all rankings. Potential-based shaping (adding a potential function to the reward) leaves the optimal policy unchanged. The set of consistent rewards forms a convex polyhedral cone, and exact recovery is impossible without additional constraints.

This ambiguity is not a technical inconvenience. It is the structural foundation of every IRL algorithm that followed. The Ng & Russell paper shifted the field's focus from naive reward recovery to principled selection among feasible rewards: margin maximization, Bayesian priors, maximum entropy regularization, or feature expectation matching.

## Three Algorithmic Responses

The linear programming formulation is the canonical entry point. For finite MDPs with known transition dynamics, the optimality constraints translate to linear inequalities in the reward vector. The LP maximizes the margin by which the expert action outperforms all alternatives, subject to a normalization constraint preventing infinite scaling. This provides a tractable, polynomial-time algorithm, but the recovered reward is not the true reward — it is merely a reward consistent with the demonstrations.

The feature-based approach handles large and continuous state spaces by parameterizing the reward as a linear combination of basis features: R(s) = w^T phi(s). The LP operates over the k-dimensional weight space rather than the full reward vector, making the method scalable. This formulation foreshadows the feature expectation perspective later formalized by Abbeel and Ng (2004), which is covered in [[irl-landscape-2000-2010]].

The Bayesian framework sketches a posterior over reward functions, treating the reward as a latent variable. The likelihood is a step function (the policy is either optimal or not), so the posterior is simply the prior restricted to the feasible polytope. This perspective influenced later Bayesian IRL work by Ramachandran and Amir (2007).

## Limitations That Set the Research Agenda

The paper's assumptions would drive two decades of research: known transition dynamics (model-free IRL would relax this), exactly optimal demonstrations (MaxEnt IRL would model suboptimality), deterministic expert policies, finite action spaces, hand-engineered features (deep IRL would learn them end to end), and computational complexity that scales with state space size.

The most enduring contribution is the formal articulation of the ambiguity problem. By proving the reward is underdetermined by the policy, Ng and Russell established that IRL is not a search for a unique R but a principled selection from a feasible set. This insight connects directly to [[principal-agent-theory]]: the principal's true preferences (reward) are never fully specified by their instructions (policy), and the agent must infer intent from incomplete information. The [[intent-architecture]] concept faces the same structural challenge at the organizational level.

## Cross-References

- The maximum entropy resolution of this ambiguity is detailed in [[ziebart-maxent-irl-alignment-conscience]].
- The broader intellectual lineage from inverse optimal control to IRL is traced in [[irl-landscape-2000-2010]].
- The mathematical formalism is consolidated in [[irl-mathematical-formalism]].
- Theoretical complexity bounds and identifiability conditions are analyzed in [[irl-theoretical-foundations]].
- The connection to [[conscience]] and machine value learning runs through all IRL descendant work.