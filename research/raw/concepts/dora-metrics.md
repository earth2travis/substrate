---
title: DORA Metrics
created: 2026-04-08
updated: 2026-04-08
type: concept
tags: [development, operations, agent]
sources: [raw/articles/lean-software-development-research.md]
---

# DORA Metrics

> Four key metrics identified by the DevOps Research and Assessment (DORA) team that measure software delivery performance. They directly map to lean manufacturing concepts: delivery speed, flow efficiency, quality at source, and recovery capability.

## The Four Metrics

| Metric | Lean Equivalent | What It Measures |
|---|---|---|
| **Deployment Frequency** | Production takt time | How often you deliver value |
| **Lead Time for Changes** | Flow time / lead time | Code commit to deploy time |
| **Change Failure Rate** | First-pass yield | % of deployments causing incidents |
| **Time to Restore Service** | MTTR | Recovery speed after failure |

## Elite Performance Benchmarks (DORA 2023)

- Deploy multiple times per day
- Lead time under 1 hour
- Change failure rate 0-15%
- Restore within 1 hour

## Connection to Lean Manufacturing

- **Deployment Frequency** maps to takt time -- the rhythm of production
- **Lead Time for Changes** maps to flow time -- total time from start to finish
- **Change Failure Rate** maps to first-pass yield -- how often you get it right the first time
- **Time to Restore** maps to MTTR -- already a standard lean metric

## Why These Four?

They capture the entire delivery pipeline:
1. How often do you ship? (frequency)
2. How long does it take? (lead time)
3. How often do you break things? (failure rate)
4. How fast do you recover? (restore time)

Together they balance speed and stability. Optimizing one at the expense of others
degrades overall performance.

## Related
- [[lean-software-development]] -- The framework that uses these metrics
- [[continuous-delivery]] -- The practice that improves these metrics
- [[devops]] -- The movement that popularized them

## Sources
- raw/articles/lean-software-development-research.md
- "Accelerate" -- Forsgren, Humble, Kim (2018)
