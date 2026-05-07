---
title: "Big Lab Approaches to Agentic Auditing"
tags: [evaluation, auditing, safety, anthropic, openai, deepmind, metr, agentic-ai]
related: [[block-hierarchy-to-intelligence]], [[jack-dorsey-from-hierarchy-to-intelligence]]
source: research/raw/big-lab-approaches.md
---

# Big Lab Approaches to Agentic Auditing

How Anthropic, OpenAI, Google DeepMind, and METR approach evaluating and governing agentic AI systems.

## Anthropic

**Evaluation Philosophy**
- Evaluations are extremely difficult to build — even "simple" benchmarks have pitfalls (data contamination, formatting sensitivity, inconsistent implementation)
- Measuring what you think you're measuring is hard — BBQ (Bias Benchmark for QA) showed models scoring 0 bias because they weren't answering questions at all
- Third-party frameworks (BIG-bench, HELM) reveal engineering challenges, not plug-and-play solutions
- Expert red teaming is gold standard but expensive and hard to scale

**Agent Design**
- Minimal scaffolding: "give as much control as possible to the language model itself"
- Simple composable patterns beat complex frameworks
- Four key patterns: prompt chaining, routing, parallelization, orchestrator-workers
- The "gate" pattern (programmatic checks between steps) maps directly to process audit checkpoints

## OpenAI

**Practices for Governing Agentic AI Systems**
- Defines agentic AI as systems pursuing complex goals with limited direct supervision
- Establishes baseline responsibilities for each party in the agentic lifecycle
- Key principle: **accountability requires auditability** — if operations can't be audited, they can't be governed

## METR (Model Evaluation & Threat Research)

- Task-based evaluation at different difficulty levels
- Controlled environments with researchers in-the-loop
- Elicitation gap research: how much post-training enhancement might improve capabilities
- Step-through methodology: researchers walk through tasks with the model

**Key finding:** Today's models can succeed at component tasks (browsing, delegating, planning) but can't yet execute complete dangerous plans reliably. The gap is closing, making systematic evaluation essential.

## Google DeepMind

- Responsible AI practices embedded in development lifecycle
- Safety evaluations against evolving threats
- Multi-stage review before model deployment

## Common Themes Across Labs

1. Evaluations must be ongoing, not one-time
2. What you measure shapes what you optimize — wrong metrics produce false confidence
3. Human review remains essential
4. Process matters as much as capability — scaffolding determines real-world performance
5. Transparency and documentation — audit trails are non-negotiable
6. Test in controlled environments first
