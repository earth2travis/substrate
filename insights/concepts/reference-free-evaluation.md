---
title: "Reference-Free Evaluation"
tags: [evals, agents, safety, scaling, trust]
related:
  - [[proof-of-work]]
  - [[harness-engineering]]
  - [[agent-native-operations]]
  - [[agent-orchestrator-pattern]]
  - [[agent-provenance-graph]]
source: research/findings/mission-critical-evals-at-scale.md
---

# Reference-Free Evaluation

Evaluating agent outputs for quality, correctness, and risk before knowing the ground truth. Not a post-hoc audit. A real-time filter that decides what needs human attention and what can flow through autonomously.

## The Scaling Problem

At 1,000 decisions per day, a human can review everything. At 100,000, even 5% sampling requires 5,000 reviews. Linear review does not scale.

The deeper problem: the cases you do not review are invisible. You know how you performed on the 5% you checked. You have no signal about the 95% you did not. Blind spots compound.

Reference-free evals solve this by generating a confidence signal for every output, not just the reviewed ones.

## How It Works

**LLM as Judge.** Feed the output into an evaluation LLM with explicit scoring criteria: helpfulness, conciseness, tone, confidence, correctness. The judge does not know the right answer. It estimates quality from structure, consistency, and internal coherence.

**Confidence Grading.** Convert the judge's output into a graded signal:
- High confidence correct → forward automatically
- Low confidence → route to more expensive pipeline, human review, or customer escalation
- Actively think wrong → flag immediately

**Dynamic Prioritization.** Combine confidence with contextual factors: cost of error, risk of bias, previous error rates, case complexity. This produces an intelligent queue, not a random sample.

## The Virtuous Cycle

```
Reference-Free Evals → Surface High Risk Cases → Human Review
         ↑                                              ↓
         └──────── Validate & Improve ←────────────────┘
```

Human reviewers examine the cases the evaluator flagged. Their critiques become ground truth for offline eval datasets. Those datasets improve the evaluator. Over time, the evaluator gets better at finding edge cases, and the edge cases themselves shrink.

This is "validating the validator." The eval system itself is the product, not the agent. The compounding asset is the evaluator's accuracy, not the agent's throughput.

## Three Uses

**1. Estimated Performance (Real-Time).**
Process all decisions through evals. Get predicted performance across the full distribution. Know your error rate on the 95% you never reviewed.

**2. Alignment Measurement.**
Compare evaluator outputs with human review outputs over time. Compute an alignment score: how much can you trust the evaluator? Track drift. When alignment drops, something changed in the agent or the environment.

**3. Intelligent Routing.**
Not all low-confidence cases need the same treatment. Some get a more expensive model pass. Some get human review. Some get customer escalation. The confidence grade plus context determines the path.

## Why This Matters for Agents

Autonomous agents make decisions without asking. The question is not "should we let them?" The question is "how do we know when they are wrong?"

Reference-free evals provide a quality signal without requiring human judgment on every output. They are the filter between raw agent output and trusted action. Without them, autonomy is either reckless (accept everything) or illusory (humans review everything).

The evaluator is a second agent watching the first. Not a gatekeeper that blocks. A sensor that surfaces. The human remains in the loop, but only for the cases that actually need human judgment.

## Design Principles

**Judge independence.** The evaluator should use a different model or configuration from the agent being evaluated. Shared failure modes between agent and evaluator defeat the purpose.

**Criteria explicitness.** The evaluator's scoring rubric should be inspectable and adjustable. "Quality" is not a criterion. "Does not hallucinate dates" is.

**Grade granularity.** Binary pass/fail is too coarse. At minimum: high confidence / low confidence / actively wrong. Finer granularity enables better routing.

**Feedback closure.** Every case routed to human review should feed back into the evaluator's training data. An evaluator that never learns from its mistakes is just a heuristic.

## Comparison to Our Proof-of-Work

Proof-of-work is a layered verification stack for autonomous PRs: static checks, unit tests, integration tests, regression checks, complexity analysis. It validates code.

Reference-free evals validate judgment. They apply to decisions, not just artifacts. A PR can pass all tests and still be a bad decision. Reference-free evals catch the gap between correct execution and correct choice.

The two systems are complementary:
- **Proof-of-work:** Did the agent produce valid output?
- **Reference-free evals:** Was the agent's decision sound?

Together they cover both correctness and judgment.

## Open Questions

- What is the right confidence threshold for our use case? Too high and we waste human time. Too low and we miss real errors.
- How do we prevent the evaluator from becoming a bottleneck? If evaluating takes as long as generating, we have not scaled.
- Can we use reference-free evals for non-mission-critical domains? Code review, content generation, research synthesis: all benefit from quality estimation.
- How do we maintain evaluator independence when the same provider supplies both agent and evaluator models?
