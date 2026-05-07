---
title: Mission Critical Evals at Scale
tags:
- evals
- agents
- healthcare
- safety
- scaling
related:
- proof-of-work
- agent-native-operations
- harness-engineering
- reference-free-evaluation
source: research/raw/mission-critical-evals-at-scale.md
---




# Mission Critical Evals at Scale

Christopher Lovejoy, MD turned AI Engineer at Anterior, shares learnings from processing 100,000+ medical decisions daily for insurance providers covering 50 million American lives.

## The Core Problem

LLM MVPs are easy. Production at scale is where problems emerge. At 100k cases per day, a 1-in-10,000 failure rate produces 10 mistakes daily. In healthcare, finance, and legal, there is no room for error.

**The subtle failure:** An AI response said a brain MRI was "suspicious for multiple sclerosis." In medical language, "suspicious" implies no confirmed diagnosis. The patient had a confirmed diagnosis, making the answer technically wrong. A human might miss this. At scale, it compounds.

## Why Human Review Does Not Scale

| Scale | Decisions/Day | Reviews (50%) | Clinicians Required |
|-------|---------------|---------------|---------------------|
| MVP | 1,000 | 500 | 5 |
| Growth | 10,000 | 5,000 | 50 |
| Scale | 100,000 | 5,000 (5%) | 50 |

At 5% review rate, massive teams are still needed. One competitor hired 800+ nurses.

The critical questions: Which cases should we review? How did we perform on cases we did not review?

## The Solution: Real-Time Reference-Free Evals

**Reference-free (label-free):** Evaluate before knowing the true outcome, before human review.
**Real-time:** Respond to issues immediately as they arise.

### Architecture

```
Inputs → LLM Pipeline → Outputs → Reference-Free Evals → Confidence Grade
                                                          ↓
                                    ┌─────────────────────┴─────────────────────┐
                                    ↓                                           ↓
                            High Confidence                             Low Confidence
                                    ↓                                           ↓
                            Return to Customer                      Take Further Action
                                                                              ↓
                                                            ┌────────────────┼────────────────┐
                                                            ↓                ↓                ↓
                                                    More Expensive    Internal Human    Customer
                                                    LLM Pipeline      Review            Review Queue
```

### Three Uses of Reference-Free Evals

1. **Estimated Performance (Real-Time).** Process all incoming decisions through evals. Get predicted performance across ALL cases, not just reviewed ones.
2. **Alignment Measurement.** Compare eval outputs with human review outputs. Compute alignment score. Track how much you can trust the system.
3. **Dynamic Prioritization.** Combine confidence grading with contextual factors (cost, risk, previous errors, complexity) to prioritize which cases get human review.

## The Virtuous Cycle

```
Reference-Free Evals → Surface High Risk Cases → Human Review
         ↑                                              ↓
         └──────── Validate & Improve ←────────────────┘
```

"Validating the validator." Over time, edge cases shrink. Problem detection improves. The system becomes harder to replicate, built on high-volume real data plus iterations.

## Results at Anterior

| Metric | Result |
|--------|--------|
| Review team size | <10 clinical experts (vs competitor's 800+ nurses) |
| AI/Human alignment | Comparable to human/human alignment |
| F1 Score | ~96% on prior authorization |

## Three Principles for Building Eval Systems

1. **Build a system, think big.** Use review data to build, audit, and improve the auditing system itself.
2. **Evaluate on live production data.** Identify problems immediately. Respond quickly.
3. **Get the best reviewers and empower them.** Quality over quantity. Custom tooling (like Anterior's "Scalpel" dashboard) dramatically improves reviewer efficiency.

## Key Takeaways for AI Agents

- Reference-free evals enable trust at scale without linear growth in human reviewers
- Confidence grading plus contextual factors allow intelligent routing (expensive models, human review, escalation)
- The virtuous cycle of "validating the validator" creates compounding advantage
- Offline evals are necessary but insufficient for mission-critical applications
- Alignment measurement between AI and human reviews is the key metric for system trust
