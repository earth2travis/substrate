---
title: Mission Critical Evals at Scale
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/mission-critical-evals-at-scale.md
---

# Mission Critical Evals at Scale

**Source:** [Mission-Critical Evals at Scale (Learnings from 100k medical decisions)](https://www.youtube.com/watch?v=cZ5ZJy19KMo)  
**Speaker:** Christopher Lovejoy, MD turned AI Engineer at Anterior  
**Date:** February 13, 2025  
**Context:** Anterior serves insurance providers covering 50 million American lives, processing 100k+ medical decisions daily

---

## The Core Problem

It's easy to build an MVP with LLMs. Scaling to production is where the problems emerge.

As request volume increases, so does the number of edge cases you've never seen before. In mission critical domains (healthcare, finance, legal), there's no room for error. Organizations are being sued for using AI automation inappropriately.

### The Medical Example

Anterior's product: prior authorization decisions (approve treatment or escalate to clinician review).

**The subtle failure:** An AI response said a brain MRI was "suspicious for multiple sclerosis." But in medical language, "suspicious" implies no confirmed diagnosis. The patient actually had a confirmed diagnosis, making this answer technically wrong.

This mistake might happen 1 in 10,000 cases. At 100k cases/day, that's 10 mistakes daily.

---

## Why Human Review Doesn't Scale

| Scale  | Decisions/Day | Reviews Needed (50%) | Clinicians Required |
| ------ | ------------- | -------------------- | ------------------- |
| MVP    | 1,000         | 500                  | 5                   |
| Growth | 10,000        | 5,000                | 50                  |
| Scale  | 100,000       | 5,000 (5%)           | 50                  |

Even at 5% review rate, scaling requires massive human teams. Anterior's competitor hired 800+ nurses for reviews.

**Two critical questions emerge:**

1. Which cases should we review?
2. How did we perform on cases we didn't review?

---

## The Solution: Real-Time Reference-Free Evals

**Reference-free (label-free):** Evaluate before knowing the true outcome (before human review).

**Real-time:** Respond to issues immediately as they arise.

### Architecture

```
Inputs → LLM Pipeline → Outputs → Reference-Free Evals → Confidence Grade
                                                              ↓
                                            ┌─────────────────┴─────────────────┐
                                            ↓                                   ↓
                                    High Confidence                      Low Confidence
                                            ↓                                   ↓
                                    Return to Customer              Take Further Action
                                                                            ↓
                                                            ┌───────────────┼───────────────┐
                                                            ↓               ↓               ↓
                                                    More Expensive    Internal Human    Customer
                                                    LLM Pipeline      Review            Review Queue
```

### Components

**1. LLM as Judge**

- Feed output into evaluation LLM with scoring criteria
- Criteria can include: helpfulness, conciseness, tone, confidence, correctness

**2. Confidence Grading**

- High confidence correct → Low confidence → Actively think wrong
- Use threshold to convert grade to predicted correct output

**3. Multiple Methods**

- LLM as judge
- Confidence estimation via logic based methods
- Methods combined for stronger signal

---

## Three Uses of Reference-Free Evals

### 1. Estimated Performance (Real-Time)

Process all incoming decisions through reference-free evals. Get predicted performance across ALL cases, not just human reviewed ones.

### 2. Alignment Measurement

Compare reference-free eval outputs with human review outputs. Compute alignment score. Track how much you can trust the system.

### 3. Dynamic Prioritization

Combine confidence grading with contextual factors:

- Cost of procedure
- Risk of bias
- Previous error rates
- Case complexity

Use these to prioritize which cases get human review. Surface highest probability of error first.

---

## The Virtuous Cycle

```
Reference-Free Evals → Surface High Risk Cases → Human Review
         ↑                                              ↓
         └──────── Validate & Improve ←────────────────┘
```

**"Validating the validator"**

Over time:

- Edge cases you've never seen get smaller
- Ability to detect problems improves
- System becomes harder to replicate (built on high volume real data + iterations)

---

## Offline Eval Datasets (Supporting Role)

Built from ground truths generated from human review critiques.

**Uses:**

- Gold standard benchmarks
- Segment by: enterprise, medical type, tough questions, complex cases, ambiguous outcomes
- Track performance over time
- Iterate AI pipelines

**Limitation:** If you wait until edge cases appear in offline datasets, it's too late. Relying only on offline evals is "playing with fire."

---

## Internal Tooling: Scalpel

Anterior built custom review dashboard for clinical reviewers:

- Right side: all context (medical record, guideline) without scrolling
- Left side: question and required context
- Enables high volume, high quality reviews
- Reviewers add critiques explaining what's wrong
- Critiques generate ground truths for offline evals

---

## Results at Anterior

| Metric             | Result                                             |
| ------------------ | -------------------------------------------------- |
| Review team size   | <10 clinical experts (vs competitor's 800+ nurses) |
| AI/Human alignment | Comparable to human/human alignment                |
| F1 Score           | ~96% on prior authorization                        |
| Customer sentiment | "Thank God we're the lucky ones"                   |

---

## Three Principles for Building Eval Systems

### 1. Build a System, Think Big

Don't just use review data to audit performance. Use it to build, audit, and improve your auditing system.

### 2. Evaluate on Live Production Data

Don't rely on offline evals. Identify problems immediately. Respond quickly.

### 3. Get the Best Reviewers and Empower Them

Quality over quantity. Build custom tooling if it helps move faster.

---

## Key Takeaways for AI Agents

1. **Reference-free evals enable trust at scale** without linear growth in human reviewers

2. **Confidence grading + contextual factors** allow intelligent routing (more expensive models, human review, customer escalation)

3. **The virtuous cycle** of "validating the validator" creates compounding advantage over time

4. **Custom internal tooling** (like Scalpel) can dramatically improve reviewer efficiency

5. **Offline evals are necessary but insufficient** for mission-critical applications

6. **Alignment measurement** between AI and human reviews is the key metric for system trust

---

_Captured from YouTube transcript, February 13, 2026_
