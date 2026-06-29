---
title: "AIMA Chapter 22: IRL in Russell & Norvig's Canonical Textbook"
tags:
- inverse-reinforcement-learning
- textbook
- foundations
- mdp
- pedagogy
related:
- [[ng-russell-2000-irl-foundations]]
- [[irl-landscape-2000-2010]]
- [[irl-mathematical-formalism]]
- [[ziebart-maxent-irl-alignment-conscience]]
source: research/raw/2026-06-28-aima-irl-chapter.md
ingested: 2026-06-29
---

# AIMA Chapter 22: IRL in Russell & Norvig's Canonical Textbook

## Summary

Russell & Norvig's *Artificial Intelligence: A Modern Approach* (4th edition, 2020) presents IRL in Chapter 22 (Reinforcement Learning), positioned at the chapter's end after standard RL paradigms. The placement is rhetorical: the book has established forward RL (value iteration, TD learning, Q-learning, policy gradients), and IRL is presented as the mirror image that closes the conceptual loop between preferences and behavior.

## Pedagogical Framing

IRL is framed as the logical dual of standard RL. Canonical RL assumes a reward is given and recovers an optimal policy. IRL assumes we observe an expert's optimal behavior and infer the underlying reward that rationalizes it. The motivation is both pedagogical and practical: reward engineering is notoriously difficult, while expert demonstrations are abundant.

The notational foundation is the MDP\R notation, describing an MDP stripped of its reward function, emphasizing that the reward is the unknown to be inferred. Bellman equations appear in the derivation of IRL constraints, showing that the expert's value function must satisfy fixed-point equations under the recovered reward.

## Key Algorithms Treated

The Ng & Russell (2000) LP formulation is the canonical algorithmic entry point. Abbeel & Ng (2004) feature matching and apprenticeship learning is presented as a practical workaround for the degeneracy problem. Maximum-margin methods are alluded to. Bayesian IRL gets limited coverage in bibliographic notes. The book stays anchored to the linear programming and feature matching roots that connect most directly to the preceding MDP material, leaving MaxEnt IRL, Bayesian IRL, and deep IRL to bibliographic notes.

## The Degeneracy Problem as Central Pedagogy

The book emphasizes why the problem is hard before offering solutions. The degeneracy result is central: for any observed policy, infinitely many reward functions make it optimal. Three sources of degeneracy are highlighted: zero reward makes every policy optimal, positive affine transformations preserve the policy ordering, and potential-based shaping leaves the optimal policy unchanged. This teaches that IRL is fundamentally ill-posed without additional constraints.

The sharp distinction between behavioral cloning (learn the policy directly via supervised learning) and IRL (learn the reward, enabling generalization) is used to argue IRL is more powerful when dynamics change. BC is simpler but brittle. IRL is complex but adaptive. See [[ng-russell-2000-irl-foundations]] for the foundational paper and [[irl-landscape-2000-2010]] for how this lineage developed.

## Russellian Framing

The treatment is distinctly Russellian: IRL is not merely a trick for learning from demonstration but a window into the problem of inferring objectives from behavior. This perspective foreshadows Russell's later work on the value alignment problem and the CIRL framework, analyzed in [[russell-human-compatible-storm]]. The book underweights MaxEnt IRL and probabilistic formulations, Bayesian IRL, and deep IRL, which are left to bibliographic notes.

## Cross-References

- Foundational paper: [[ng-russell-2000-irl-foundations]]
- Broader lineage: [[irl-landscape-2000-2010]]
- Mathematical notation: [[irl-mathematical-formalism]]
- MaxEnt as the probabilistic evolution: [[ziebart-maxent-irl-alignment-conscience]]