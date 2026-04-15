---
title: Lean Software Development
tags:
  - development
  - operations
  - agent
related:
  - [[continuous-delivery]]
  - [[craft-production]]
  - [[custom-tooling-opportunities]]
  - [[dark-factory]]
source: research/raw/lean-software-development.md
---

# Lean Software Development

> Application of lean manufacturing principles (from TPS) to software development. Formalized by Mary and Tom Poppendieck in 2003 with seven principles that map directly from manufacturing to knowledge work.

## Seven Principles

### 1. Eliminate Waste
The primary principle. Remove anything that doesn't deliver customer value:
- Unused features (45-80% of software features rarely/never used)
- Waiting (code review, CI/CD, QA, requirements clarification)
- Handoffs between teams (Dev → QA → Ops → Security)
- Task switching and context destruction
- Partially done work sitting in the pipeline
- Defects that require rework
- **Relearning** -- rediscovering information already in the codebase (the problem [[llm-wiki-pattern]] solves)

### 2. Amplify Learning
Software development is knowledge creation, not manufacturing. Short feedback loops are essential:
- Iterative development, A/B testing, rapid prototyping
- Blameless post-mortems, [[kaizen]] retrospectives
- User research and rapid prototyping

### 3. Decide as Late as Possible
Defer decisions until maximum information:
- Microservices over monoliths (decouple decisions)
- Feature flags, flexible architectures
- Avoid premature optimization, YAGNI principle

### 4. Deliver as Fast as Possible
Speed is the primary delivery metric. Fast delivery → fast feedback → fast learning → better decisions:
- [[continuous-delivery]], trunk-based development
- Small batch sizes, automated testing
- Infrastructure as code, one-click deployment

### 5. Empower the Team
Self-organizing teams with autonomy:
- Platform teams that enable rather than control
- Developer experience (DevEx) investments
- Team-level decision autonomy

### 6. Build Integrity In
Quality at source (direct translation of [[jidoka]]):
- Automated testing, TDD, code review
- CI that blocks bad code
- Feature flags for safe testing in production
- Observability as a quality feedback loop

### 7. See the Whole
Optimize for the entire system, not individual parts:
- Value stream mapping of the entire delivery pipeline
- [[dora-metrics]] that measure end-to-end flow
- Discourage heroics that mask systemic problems

## TPS-to-Software Translation

| TPS Concept | Software Equivalent |
|---|---|
| Seven Wastes | [[seven-software-wastes]] |
| Just-in-Time | [[continuous-delivery]] |
| Jidoka | CI/CD automated quality gates |
| Kanban | [[kanban]] boards with WIP limits |
| Value Stream Mapping | Code-to-production workflow analysis |
| Poka-Yoke | Linters, automated testing, security scans |
| Heijunka | Sprint leveling, capacity allocation |
| Gemba | Observability, DevEx research, dogfooding |
| Kaizen | Retrospectives, continuous improvement |
| Respect for People | Developer autonomy, platform engineering |

## Key Frameworks Built on Lean Software

- [[devops]] -- Breaking down Dev/QA/Ops silos, continuous delivery
- [[continuous-delivery]] -- Automating the entire release pipeline (JIT for deployments)
- [[lean-startup]] -- Build-Measure-Learn loop for validating product decisions
- [[dora-metrics]] -- Four key metrics: deployment frequency, lead time, change failure rate, restore time
- Site Reliability Engineering -- Toil elimination, error budgets, automation

## Organizations Embodying Lean Software

- **Amazon:** Two-pizza teams, API mandates, continuous deployment
- **Netflix:** Chaos engineering, developer autonomy, platform investment
- **GitHub:** Trunk-based development at scale, feature flags everywhere
- **Etsy:** DevOps transformation, blameless culture, observability-first
- **Spotify:** Squad model, autonomous teams, flow-oriented org design

## Little's Law in Software

`Average Lead Time = Average WIP / Average Throughput`

Mathematically proves that reducing WIP reduces lead time. 20 items in progress at 5/week throughput = 4 weeks lead time. Cut WIP to 10 = 2 weeks lead time. This is why WIP limits matter.

## What Doesn't Translate Well

- **Physical vs logical:** Software is more flexible than physical goods -- leverage flexibility, don't constrain it with manufacturing mental models
- **Knowledge work vs repeatable processes:** Over-optimizing for flow can stifle exploration and innovation
- **Muda definition is fuzzier:** Is refactoring waste or investment? The boundary is less clear in knowledge work

## Related
- [[lean-production]] -- The manufacturing paradigm this is based on
- [[seven-software-wastes]] -- The seven wastes translated to software
- [[dora-metrics]] -- The lean dashboard for software
- [[toyota-production-system]] -- The origin of all lean concepts
- [[llm-wiki-pattern]] -- Solves the relearning waste in software

## Sources
- raw/articles/lean-software-development-research.md
- "Lean Software Development: An Agile Toolbook" -- Poppendieck (2003)
- "Accelerate" -- Forsgren, Humble, Kim (2018)
