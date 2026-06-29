---
title: "Active and Interactive IRL: Query-Based Learning and Cooperative Teaching"
tags:
- inverse-reinforcement-learning
- active-learning
- cooperative-irl
- preference-learning
- human-in-the-loop
- query-based-learning
- ai-alignment
related:
- [[ziebart-maxent-irl-alignment-conscience]]
- [[russell-human-compatible-storm]]
- [[irl-landscape-2000-2010]]
- [[irl-theoretical-foundations]]
- [[irl-moral-psychology-connection]]
- [[post-2018-irl-landscape]]
- [[conscience]]
- [[principal-agent-theory]]
source: research/raw/2026-06-29-active-interactive-irl.md
ingested: 2026-06-29
---

# Active and Interactive IRL: Query-Based Learning and Cooperative Teaching

## Summary

Traditional IRL operates in a fundamentally passive mode: the agent receives a batch of demonstrations, infers a reward, and deploys. Active and interactive IRL transforms this from a unidirectional data flow into bidirectional interaction. The agent asks questions, requests demonstrations, proposes comparisons. The human responds with feedback. This changes IRL from a statistical inference problem into an interactive epistemology problem: how should an agent optimally acquire information about human values through structured interaction?

## Cooperative IRL (Hadfield-Menell et al., 2016)

CIRL reconceptualizes the problem by treating the human and robot as cooperative agents in a two-player game, rather than treating the human as an exogenous information source. In standard IRL the human's behavior is assumed independent of the robot's presence. In reality, the human teaches, corrects, demonstrates, and behaves differently knowing the robot is learning. The human's optimal policy includes a teaching objective: they may choose physically suboptimal actions if those actions disambiguate the reward function. The robot's optimal policy includes active learning: it must balance exploiting its current best estimate with exploring to improve its belief. See [[russell-human-compatible-storm]] for the full CIRL analysis.

## Active Preference-Based Learning (Sadigh et al., 2017)

Sadigh, Dragan, Sastry, and Seshia introduced active preference-based reward learning. Humans are better at comparing trajectories than providing absolute reward values. The robot queries with pairwise comparisons modeled via a Bradley-Terry probabilistic choice function. The active component selects queries that maximize expected information gain about the reward parameters: the pair of trajectories that, when compared, most reduces the entropy of the posterior over reward weights. This focuses querying on decision-boundary cases where preferences are most informative. Demonstrated on driving and manipulation tasks with fewer queries than passive learning.

## Risk-Aware Active IRL (Brown, Cui, Niekum, 2019)

Standard active IRL selects queries to maximize information gain about reward parameters. But information gain is only a proxy for the true objective: a policy that performs well. Brown et al. formalize performance risk as the expected performance loss under the true reward, and select queries to minimize the expected risk of the final policy rather than maximize information gain. A query about a rare edge case may be highly informative but irrelevant to typical performance. Risk-aware active learning leads to safer policies, especially early in learning when the reward is highly uncertain.

## PAC Apprenticeship Learning (Bajgar et al., 2025)

Bajgar, Gould, Liu, Abate, Gatsis, and Osborne proved Probably Approximately Correct guarantees for Bayesian active IRL using Thompson sampling. At each step, the agent samples a reward function from the posterior and selects the query optimal under that sampled reward. This balances exploration and exploitation naturally. The sample complexity is polynomial in the number of features, horizon, and desired accuracy. This is the first PAC guarantee for active IRL in the apprenticeship learning setting: active IRL can be provably efficient, not just empirically effective.

## Online and Incremental IRL

Batch IRL assumes all demonstrations are available at the start. Online IRL maintains a running reward estimate updated as new data arrives, without reprocessing history. Maximum entropy IRL is well-suited to online updates because the Boltzmann model parameters can be updated via online gradient descent: the gradient for a new trajectory is the difference between its empirical feature counts and the expected counts under the current model. This enables adaptation to changing expert preferences, important for personalized systems where preferences evolve.

## Interactive Teaching and Machine Teaching

The human is not merely a data source but a strategic teacher. The CIRL framework shows the human's optimal strategy involves teaching behaviors distinct from physical optimality. Machine teaching (Zhu 2013, Zhu et al. 2018) formalizes the dual problem: the teacher has a target model and selects examples to make the learner converge efficiently. Seita et al. (2019) draw on Vygotsky's Zone of Proximal Development to design teaching curricula: demonstrations should be within the agent's learning capacity, not too easy (agent could self-learn) and not too hard (agent cannot learn even with help). This connects IRL to educational psychology.

## Connections to Substrate

CIRL connects directly to [[conscience]]: uncertainty about preferences is the signal component, deference to humans is the stop component, learning from behavior is the moral knowledge component. The preference-based learning framework connects to the [[irl-moral-psychology-connection]]: active querying is a partial remedy for the rationality assumption problem because it lets the agent probe edge cases rather than passively accepting biased demonstrations.

The active learning model maps to [[principal-agent-theory]]: the principal (human) and agent (AI) are in a cooperative game where information flows bidirectionally. The agent's queries are effort to reduce information asymmetry, the same structural problem at the heart of delegation economics.

## Cross-References

- MaxEnt IRL as the statistical foundation for active learning: [[ziebart-maxent-irl-alignment-conscience]]
- CIRL and the off-switch game: [[russell-human-compatible-storm]]
- The rationality assumption and its failure: [[irl-moral-psychology-connection]]
- Theoretical bounds on sample complexity: [[irl-theoretical-foundations]]
- Modern RLHF as preference-based descendant: [[post-2018-irl-landscape]]
- Information asymmetry in delegation: [[principal-agent-theory]]