---
title: "Lean Software Delivery"
tags: [concept, lean, software-delivery, devops, metrics, waste]
related: [[dora-metrics]], [[continuous-delivery]], [[devops]], [[seven-software-wastes]], [[lean-software-development]], [[lean-production]], [[lean-doctrine]], [[toyota-production-system]], [[dark-factory]], [[cloudflare-first-agent-factory]], [[the-openclaw-lesson]], [[agent-native-operations]]
source: research/findings/dora-metrics.md
---

# Lean Software Delivery

## Definition

Lean software delivery is the application of lean manufacturing principles to the software development lifecycle: eliminating waste, maximizing flow, building quality in, and measuring outcomes through empirical metrics. It encompasses the practices (continuous delivery, DevOps), the metrics (DORA), and the waste categories (seven software wastes) that together enable high-performance software teams.

## Core Claim

Software delivery is not a craft activity that resists measurement. It is a production system with flow, bottlenecks, waste, and quality gaps — and it can be measured, improved, and optimized using the same principles that transformed manufacturing.

## The Measurement Framework: DORA

The DevOps Research and Assessment team identified four metrics that capture the entire delivery pipeline:

| Metric | Lean Equivalent | Elite Benchmark (2023) |
|--------|----------------|----------------------|
| Deployment Frequency | Production takt time | Multiple times per day |
| Lead Time for Changes | Flow time / lead time | Under 1 hour |
| Change Failure Rate | First-pass yield | 0–15% |
| Time to Restore Service | MTTR | Within 1 hour |

These metrics balance speed and stability. Optimizing one at the expense of others degrades overall performance.

## The Practice Layer: Continuous Delivery + DevOps

**Continuous Delivery** is just-in-time for software: deploy only what is validated, when ready, in small increments. **DevOps** breaks down the Dev/QA/Ops silos that create handoff waste. Together they create the infrastructure for flow.

In dark-factory agent systems, this pipeline becomes autonomous: agents write code, CD validates it, DevOps infrastructure deploys and monitors it.

## The Waste Lens: Seven Software Wastes

Poppendieck's translation of Ohno's muda to software:

1. **Partially Done Work** — code written but not shipped (inventory waste)
2. **Extra Features** — 45–80% of features are rarely or never used (overproduction)
3. **Relearning** — rediscovering solved problems (defect/correction)
4. **Handoffs** — Dev → QA → Ops, losing context at each transfer (transportation)
5. **Delays** — waiting for review, CI, deployment windows (waiting)
6. **Task Switching** — context switching destroys focus; 3+ projects = 20–40% efficiency (motion)
7. **Defects** — bugs found in production cost 50–100x more than design-phase defects

## Little's Law in Software

`Average Lead Time = Average WIP / Average Throughput`

This mathematically proves what lean advocates argue: reducing WIP reduces lead time. If you have 20 items in progress and throughput of 5/week, average lead time is 4 weeks. Cut WIP to 10 and lead time drops to 2 weeks.

## Related

- [[dora-metrics]] — the measurement framework for software delivery performance
- [[continuous-delivery]] — just-in-time deployment practice
- [[devops]] — culture and practices that break down delivery silos
- [[seven-software-wastes]] — Poppendieck's translation of manufacturing waste to software
- [[lean-software-development]] — the research base connecting lean manufacturing to software
- [[lean-production]] — the manufacturing origin of these principles
- [[lean-doctrine]] — the philosophical foundation of lean operations
- [[toyota-production-system]] — the system that demonstrated lean at industrial scale
- [[dark-factory]] — the endpoint where lean software delivery becomes fully autonomous
