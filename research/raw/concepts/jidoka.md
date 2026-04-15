---
title: "Jidoka (Autonomation)"
created: 2026-04-09
updated: 2026-04-09
type: concept
tags: [development, tools]
sources: [raw/articles/craft-mass-lean-production-research.md]
---

# Jidoka (Autonomation)

One of the two pillars of the [[toyota-production-system]] (the other being [[just-in-time]]). Jidoka means "automation with a human touch" -- machines that detect abnormalities and stop automatically, preventing defective products from continuing down the line.

## Core Concept

When a problem is detected, the process stops immediately and the operator is alerted. This prevents:
- Defects from being passed to the next process
- Machines from running while producing bad output
- Problems from being hidden or ignored

## The Four Steps

1. Detect the abnormality
2. Stop the process
3. Fix the immediate problem
4. Investigate the root cause and apply countermeasure

## Connection to Software

In software development, jidoka maps to:
- CI/CD pipelines that fail builds on test failures
- Automated test suites that catch defects before deployment
- Code review gates that stop bad code from merging
- [[dark-factory]] agent-to-agent review as automated quality detection

## Related

- [[toyota-production-system]] -- One of the two pillars (with just-in-time)
- [[taiichi-ohno]] -- Developed jidoka as part of TPS
- [[dark-factory]] -- Automated quality detection is the jidoka of agent systems
- [[just-in-time]] -- The other pillar of TPS
