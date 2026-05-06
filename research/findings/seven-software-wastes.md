---
title: "Seven Software Wastes"
tags: [lean, waste, software-development, efficiency, process]
related: [[lean-production]], [[lean-software-development]], [[dora-metrics]], [[lean-startup]], [[llm-wiki-pattern]]
source: research/raw/seven-software-wastes.md
---

# Seven Software Wastes

## Summary

Mary and Tom Poppendieck translated Taiichi Ohno's seven manufacturing wastes (muda) to software development in their 2003 book "Lean Software Development: An Agile Toolbook." The seven software wastes are: (1) Partially Done Work — code written but not shipped, PRs waiting for review, work-in-progress that delivers zero value until complete; (2) Extra Features — building features nobody uses (45–80% of features are rarely or never used); (3) Relearning — rediscovering information, relearning solutions, re-inventing tools; (4) Handoffs — work passed between teams (Dev → QA → Ops → Security), losing context at each transfer; (5) Delays — waiting for code review, CI/CD, QA, dependencies, deployment windows; (6) Task Switching — context switching between projects, meetings interrupting flow; and (7) Defects — bugs, incidents, vulnerabilities, poor UX requiring redesign. The cost of fixing defects increases exponentially the later they are found: 1x in design, 5x in coding, 10x in testing, 50–100x in production.

## Key Claims

- Organizations typically have 2–3x more WIP than they can process; each item increases lead time and waste risk
- 45–80% of software features are rarely or never used — the most expensive form of waste
- Developers on 3+ projects simultaneously operate at 20–40% efficiency due to context switching
- Defect cost increases exponentially with detection latency: production defects cost 50–100x more than design-phase defects

## Related

- [[lean-production]] — original seven wastes (muda) from TPS
- [[lean-software-development]] — the framework that defines and operationalizes these wastes
- [[dora-metrics]] — quantitative measures that help identify where waste accumulates
- [[lean-startup]] — eliminates the "extra features" waste before it is created
- [[llm-wiki-pattern]] — solves the "relearning" waste through persistent knowledge graphs
