---
title: "Dark Factory: Lights-Out Manufacturing and Software"
tags: [agent, operations, manufacturing, automation, ai]
related:
- harness-engineering
- codex
- lean-production
- ryan-lopopolo
- henry-ford
source: research/raw/dark-factory.md
---
# Dark Factory: Lights-Out Manufacturing and Software

## Summary

Fully automated production facilities operating without human presence. In software, the term describes autonomous development pipelines where agents work around the clock without human intervention.

## Origins

Term coined in the 1980s when manufacturers realized CNC machines could run overnight unsupervised. FANUC's robot factory operated for 30 days without human intervention, robots building other robots.

## Historical Examples

| Era | Example | Outcome |
|-----|---------|---------|
| 1910s | Ford Rouge Plant | Raw ore in, finished cars out — closest pre-computing analog |
| 1980s | GM Hamtramck | Failed: technology immature, quality issues required manual rework |
| 1990s | John Deere | Lights-out machining for agricultural parts |
| 2010s | Philips Drachten | 128 robots, handful of human supervisors |

## The Software Dark Factory

Ryan Lopopolo's OpenAI Frontier team:
- 1B tokens/day = 24/7 production
- 0 lines of human-written code
- 6-hour autonomous runs while humans sleep
- Agent-to-agent review = quality sensors
- Human role = design environments, handle exceptions only

## Key Principles

1. Self-monitoring systems with automated error detection
2. Predictive maintenance via observability
3. Standardized interfaces and modular design
4. Redundancy and graceful degradation
5. Continuous improvement via data feedback

## Challenges

- Exception handling for novel situations
- High initial investment
- Last 10% of automation costs 90% of budget
- Loss of tacit knowledge when humans leave

## Related

- [[harness-engineering]] — Methodology enabling dark factory software
- [[codex]] — Primary agent tool
- [[lean-production]] — Historical lineage
- [[ryan-lopopolo]] — Popularized the term in software
- [[henry-ford]] — Pre-computing analog
