---
title: Seven Software Wastes
created: 2026-04-08
updated: 2026-04-08
type: concept
tags: [development, operations]
sources: [raw/articles/lean-software-development-research.md]
---

# Seven Software Wastes

> Mary and Tom Poppendieck's translation of Taiichi Ohno's seven manufacturing wastes (muda) to software development, from "Lean Software Development: An Agile Toolbook" (2003).

## The Seven Wastes

### 1. Partially Done Work (→ Inventory Waste)
Code written but not shipped, features partially implemented, PRs waiting for review,
work-in-progress that delivers zero customer value until complete. Organizations
typically have 2-3x more WIP than they can process. Each additional WIP item
increases lead time and chance of waste.

### 2. Extra Features (→ Overproduction Waste)
Building features nobody uses. 45-80% of software features are rarely or never used.
Every unused feature costs money to build, test, document, maintain, and debug.

### 3. Relearning (→ Defect/Correction Waste)
Rediscovering information, relearning solutions, re-inventing tools or libraries
that already exist in the codebase. Developers spend significant time searching
for how things work and why decisions were made. This is the core problem the
[[llm-wiki-pattern]] was designed to solve.

### 4. Handoffs (→ Transportation Waste)
Work passed between teams (Dev → QA → Ops → Security). Each handoff loses context,
creates waiting, and introduces communication errors. Requirements start clear
and become distorted by the time they reach implementation.

### 5. Delays (→ Waiting Waste)
Waiting for code review, CI/CD, QA, dependencies, requirements clarification,
deployment windows. A feature that takes 2 hours to code might spend 3 weeks
in the pipeline -- most of that time is waiting, not working.

### 6. Task Switching (→ Motion Waste)
Context switching between multiple projects, meetings interrupting flow time,
interruptions from Slack/email/urgent requests. Takes 23 minutes to fully regain
focus after an interruption. Developers on 3+ projects simultaneously operate
at 20-40% efficiency.

### 7. Defects (→ Defect Waste)
Bugs, production incidents, security vulnerabilities, poor UX requiring redesign.
Cost of fixing a bug increases exponentially the later it's found:
- Design: 1x
- Coding: 5x
- Testing: 10x
- Production: 50-100x

## Elimination Strategies

- **WIP 1:** Limit WIP, ship fast, reduce batch sizes
- **WIP 2:** Pull-based development, [[lean-startup]] build-measure-learn loop
- **WIP 3:** Persistent knowledge bases, ADRs, wikis
- **WIP 4:** Cross-functional teams, DevOps culture
- **WIP 5:** Automate CI/CD, trunk-based development, frequent deploys
- **WIP 6:** Single-piece flow, protect flow time
- **WIP 7:** Automated testing, TDD, code review, observability

## Related
- [[lean-production]] -- Original seven wastes (muda) from TPS
- [[lean-software-development]] -- The framework that defines these wastes
- [[llm-wiki-pattern]] -- Solves the relearning waste

## Sources
- raw/articles/lean-software-development-research.md
- "Lean Software Development: An Agile Toolbook" -- Poppendieck (2003)
