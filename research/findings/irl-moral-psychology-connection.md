---
title: "IRL and Moral Psychology: The Rationality Assumption and Its Failure"
tags:
- inverse-reinforcement-learning
- moral-psychology
- rationality
- value-learning
- ai-alignment
- dual-process-theory
- moral-foundations
- bounded-rationality
related:
- [[ziebart-maxent-irl-alignment-conscience]]
- [[russell-human-compatible-storm]]
- [[ng-russell-2000-irl-foundations]]
- [[active-interactive-irl]]
- [[conscience]]
- [[principal-agent-theory]]
source: research/raw/irl-moral-psychology-connection.md
ingested: 2026-06-29
---

# IRL and Moral Psychology: The Rationality Assumption and Its Failure

## Summary

IRL makes a critical assumption: humans are approximately rational optimizers of some stable reward function. Moral psychology tells us this assumption is false. This is not a technical detail. It is the fundamental problem at the intersection of value learning and moral psychology. If you apply IRL to human behavior, you infer the reward function that would produce the observed behavior if the agent were a rational optimizer. But humans are not rational optimizers, so what does the inferred reward function actually mean?

## The Rationality Assumption and What It Misses

Standard IRL assumes the expert has a stable reward function, approximately maximizes expected cumulative reward, and that observed behavior reveals this function. Moral psychology dismantles each of these.

Kahneman and Greene's dual-process theory shows human moral judgment is dominated by System 1: fast, automatic, affective, heuristic-driven. System 2 (slow, deliberative, controlled) is used to rationalize System 1 judgments, not generate them. The reward function driving a snap moral judgment is not the same as the one System 2 would endorse upon reflection. Which system should IRL infer?

Haidt's moral foundations theory identifies evolved moral taste receptors: care/harm, fairness/cheating, loyalty/betrayal, authority/subversion, sanctity/degradation, liberty/oppression. These are not learned through optimization. They are evolved priors. IRL assumes the reward function is learned from behavior, but moral foundations suggest some rewards are hardwired.

Bounded rationality and cognitive biases (loss aversion, framing effects, status quo bias, anchoring, availability heuristics) are not noise around a rational optimum. They are systematic deviations. IRL applied to biased behavior infers a reward function that encodes the bias: R_inferred = R_true + Bias. You cannot separate true values from cognitive biases without additional assumptions.

## Stated vs. Revealed Preferences

IRL infers revealed preferences from behavior. In moral domains, stated and revealed preferences diverge sharply. People say they value honesty, fairness, and environmental stewardship. Their behavior reveals preferences for convenience, self-interest, and short-term comfort. IRL watching behavior learns a reward function favoring convenience. IRL watching surveys learns a reward function favoring honesty. Neither is the true reward function.

Harry Frankfurt's distinction between first-order desires (wanting a cigarette) and second-order volitions (wanting to want to quit) marks the gap. Human values are often what we endorse upon reflection, not what we do under impulse. An IRL agent that never asks whether the demonstrator endorses their behavior is not learning values. It is learning behavioral regularities. It is a behaviorist about value, and behaviorism was abandoned in psychology for good reason.

## The Three-Level Model

Three levels of human values create a three-level inference problem for IRL:

1. **Revealed preferences** (what behavior shows) — what IRL observes
2. **Stated preferences** (what surveys show) — what preference learning observes
3. **Ideal preferences** (what we would endorse fully informed) — what alignment aims for

IRL operates at level 1. Moral philosophy operates at level 3. The gap between levels is the gap between what we do and what we would endorse, and it is the space where addiction, bias, and coercion live. A machine conscience built on pure behavioral inference would be a conscience of surfaces, not depths.

## Implications for Alignment

If behavior is not a clean window into values, then value learning from behavior alone is insufficient. Multiple sources of evidence are needed: behavior, stated preferences, reflective equilibrium, institutional design, and biological signals. Maintaining uncertainty (CIRL's approach, see [[russell-human-compatible-storm]]) is not just a safety mechanism but an epistemic necessity given that the data itself is corrupted by bias.

The [[conscience]] architecture provides a structural parallel: moral knowledge (what is right) must be combined with self-awareness (knowing your knowledge is bounded) and the signal/stop components (recognizing when something might be wrong and deferring). IRL without the signal and stop components is just a learned reward function, not a conscience.

## Cross-References

- The MaxEnt IRL formalism: [[ziebart-maxent-irl-alignment-conscience]]
- Russell's uncertainty mechanism: [[russell-human-compatible-storm]]
- Active learning as partial remedy: [[active-interactive-irl]]
- The conscience architecture: [[conscience]]
- Principal-agent information asymmetry: [[principal-agent-theory]]