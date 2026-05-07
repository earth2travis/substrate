---
title: "Lean Software Development: From Factory Floor to Codebase"
tags: [lean, development, operations, agile, software]
related:
- lean-production
- toyota-production-system
- continuous-delivery
- dora-metrics
- seven-software-wastes
- llm-wiki-pattern
source: research/raw/lean-software-development.md
---
# Lean Software Development: From Factory Floor to Codebase

## Summary

Application of lean manufacturing principles to software development. Formalized by Mary and Tom Poppendieck in 2003 with seven principles that map directly from manufacturing to knowledge work.

## The Seven Principles

1. **Eliminate Waste** — Remove anything not delivering customer value: unused features, waiting, handoffs, task switching, partially done work, defects, relearning
2. **Amplify Learning** — Short feedback loops: iterative dev, A/B testing, blameless postmortems
3. **Decide as Late as Possible** — Defer decisions until maximum information: microservices, feature flags, YAGNI
4. **Deliver as Fast as Possible** — Speed = fast feedback = fast learning = better decisions
5. **Empower the Team** — Self-organizing teams with autonomy: platform teams enable rather than control
6. **Build Integrity In** — Quality at source: automated testing, TDD, CI gates, observability
7. **See the Whole** — Optimize for entire system: value stream mapping, DORA metrics

## TPS-to-Software Translation

| TPS Concept | Software Equivalent |
|-------------|---------------------|
| Seven Wastes | [[seven-software-wastes]] |
| Just-in-Time | [[continuous-delivery]] |
| Jidoka | CI/CD automated quality gates |
| Kanban | Kanban boards with WIP limits |
| Value Stream Mapping | Code-to-production workflow analysis |
| Poka-Yoke | Linters, automated testing, security scans |
| Gemba | Observability, DevEx research, dogfooding |
| Kaizen | Retrospectives, continuous improvement |

## Little's Law

`Average Lead Time = Average WIP / Average Throughput`

Mathematically proves reducing WIP reduces lead time. 20 items at 5/week = 4 weeks. Cut WIP to 10 = 2 weeks.

## What Doesn't Translate

- Software is more flexible than physical goods
- Over-optimizing for flow can stifle innovation
- Is refactoring waste or investment? Boundary is fuzzier in knowledge work

## Related

- [[lean-production]] — Manufacturing paradigm this is based on
- [[toyota-production-system]] — Origin of all lean concepts
- [[continuous-delivery]] — JIT for deployments
- [[dora-metrics]] — The lean dashboard for software
- [[seven-software-wastes]] — Wastes translated to software
- [[llm-wiki-pattern]] — Solves the "relearning" waste
