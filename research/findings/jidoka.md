---
title: "Jidoka: Autonomation as Quality Stop-Line"
tags: [lean, tps, quality, operations, manufacturing]
related: [[toyota-production-system]], [[just-in-time]], [[taiichi-ohno]], [[dark-factory]]
source: research/raw/jidoka.md
---

# Jidoka: Autonomation as Quality Stop-Line

## Summary

Jidoka (自働化, "automation with a human touch") is one of the two pillars of the Toyota Production System. It means machines and processes detect abnormalities and stop automatically, preventing defects from propagating downstream.

## Core Mechanism

1. **Detect** — Build quality checks into the process itself
2. **Stop** — Halt production immediately when deviation occurs
3. **Fix** — Address the immediate problem at the source
4. **Investigate** — Root-cause analysis to prevent recurrence

## Software Mapping

| Manufacturing | Software Equivalent |
|---------------|---------------------|
| Machine stops on defect | CI/CD pipeline fails on test failure |
| Andon cord | Alerting / paging on anomaly |
| Line halt | Merge block on failed checks |
| Operator empowerment | Developer stop-the-line authority |

## Connection to Agent Systems

In a [[dark-factory]] of autonomous agents, jidoka becomes agent-to-agent review: each agent runs checks on the output of the previous agent before passing work forward. The "andon cord" is a `kanban_block` or automated rollback.

## Related

- [[toyota-production-system]] — Jidoka is one of its two pillars
- [[just-in-time]] — The other pillar
- [[taiichi-ohno]] — Developed jidoka at Toyota
