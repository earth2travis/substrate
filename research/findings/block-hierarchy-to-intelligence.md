---
title: "Block: From Hierarchy to Intelligence"
tags:
  - organizational-design
  - ai-coordination
  - agent-factory
  - context-stack
related: []
source: research/raw/block-hierarchy-to-intelligence.md
---

# Block: From Hierarchy to Intelligence

## Summary

Jack Dorsey and Sequoia Capital published a thesis for replacing organizational hierarchy with AI coordination. The argument: hierarchy exists because humans are bottlenecked information routers (span of control: 3 to 8 people, unchanged since Rome). AI can replace that routing function, eliminating permanent middle management.

## Historical Arc

The piece traces organizational structure through 2,000 years:

1. **Roman Army** (contubernium → century → cohort → legion): Information routing protocol built around human cognitive limits. 8 → 80 → 480 → 5,000.
2. **Prussian General Staff** (post-1806): Created middle management. Officers whose job was not to fight but to "plan operations, process information, and coordinate across units." Designed to "support incompetent Generals."
3. **American Railroads** (1840s-1850s): West Point engineers brought military org design to business. Daniel McCallum's org chart (1850s) was the first ever created. Train collisions were killing people. Hierarchy was the safety mechanism.
4. **Frederick Taylor** (1856-1915): Scientific Management. Broke work into specialized tasks. Created the functional pyramid.
5. **Manhattan Project** (1944): First real cross-functional coordination under pressure. Oppenheimer organized around the problem, not the function. Worked, but was a wartime exception.
6. **McKinsey Matrix** (1959): Clee and di Scipio's "Creating a World Enterprise." Combined functional specialties with divisional units.
7. **Modern experiments**: Spotify squads (reverted to hierarchy at scale), Zappos Holacracy (significant attrition), Valve flat structure (couldn't scale past hundreds). All revealed limitations of traditional hierarchy but none solved the underlying problem.

**Key insight:** "Two thousand years of organizational innovation has been an attempt to work around this tradeoff without breaking it." More layers = slower information flow. Fewer layers = span of control exceeds human capacity.

## Block's Four Layer Architecture

1. **Capabilities**: Atomic financial primitives (payments, lending, card issuance, banking, BNPL, payroll). No UIs. Reliability, compliance, performance targets. Hard to acquire and maintain.

2. **World Model** (two sides):
   - **Company world model**: How the company understands itself. Replaces information that used to flow through management layers. Built from artifacts of remote work (decisions, discussions, code, designs, plans).
   - **Customer world model**: Per-customer, per-merchant, per-market representation built from proprietary transaction data. "Money is the most honest signal in the world."

3. **Intelligence layer**: Composes capabilities into solutions for specific customers at specific moments. Delivers proactively. Examples: a restaurant's cash flow tightening before a seasonal dip the model has seen before; a Cash App user's spending pattern shifting in ways associated with a city move.

4. **Interfaces**: Square, Cash App, Afterpay, TIDAL, bitkey, proto. Delivery surfaces. "Important, but not where the value is created."

## Three Roles (Replacing Hierarchy)

- **ICs**: Deep specialists who build and operate capabilities, the model, the intelligence layer, and interfaces. The world model provides context that a manager used to provide.
- **DRIs** (Directly Responsible Individuals): Own specific cross-cutting problems or customer outcomes. Time-boxed (e.g., 90 days). Full authority to pull resources across teams. May persist or move to new problems.
- **Player-coaches**: Combine building with developing people. Replace traditional managers. Still write code or build models. No status meetings, alignment sessions, or priority negotiations. "The world model handles alignment. The DRI structure handles strategy and priority. The player-coach handles craft and people."

"There is no need for a permanent middle management layer."

## The Self-Generating Roadmap

"When the intelligence layer tries to compose a solution and can't because the capability doesn't exist, that failure signal is the future roadmap."

Traditional roadmaps, where product managers hypothesize about what to build next, are "any company's ultimate limiting factor." In this model, customer reality generates the backlog directly.

## The Defining Question

"What does your company understand that is genuinely hard to understand, and is that understanding getting deeper every day? If the answer is nothing, AI is just a cost optimization story. You cut headcount, improve margins for a few quarters, and eventually get absorbed by something smarter."

## Connections to Our Work

### Context Stack = Company World Model

Block's company world model is built from the artifacts of remote work. Our Context Stack (`research/context-stack/spec.md`) is the same concept at startup scale: Identity, Direction, Operations, Intelligence layers that give any agent (or person) full context without hierarchical information routing.

### Agent Factory = Block's Four Layers

| Block Layer | Agent Factory Equivalent |
|---|---|
| Capabilities | Agent skills (atomic, composable, no interface) |
| World Model | Context Stack (company + customer understanding) |
| Intelligence Layer | Loom (orchestrator that composes skills into workflows) |
| Interfaces | Telegram, Discord, CLI, web surfaces |

### Self-Generating Roadmap = Failure-Driven Skill Development

When an agent tries to do something and lacks the skill, that gap IS the next skill to build. We see this already but haven't formalized it. Every "I can't do X" moment should auto-generate an issue.

### Brain Fry Connection

The HBR "AI Brain Fry" research (#546) found that copilots increase cognitive load. Block's thesis is the organizational answer: don't give everyone copilots (that keeps hierarchy intact). Replace the hierarchy's information routing function with AI. Fundamentally different approach.

### Three Roles Map to Agent Factory

- **ICs** = specialist agents (Skill Architect, QA Agent)
- **DRIs** = agents assigned to cross-cutting problems (Loomrunner)
- **Player-coaches** = executive agents (Sivart, Koda) that build AND develop other agents

### AFPS (Agent Factory Production System)

Block's architecture validates the Toyota-inspired AFPS framework. Toyota's jidoka (quality at the source) maps to Block's "people on the edge" making calls the model shouldn't make: ethical decisions, novel situations, high-stakes moments. The intelligence is in the system. The judgment is at the edge.

## Key Quotes

> "The constraint is the same one the Romans faced: narrowing span of control means adding layers of command, but more layers mean slower information flow."

> "Most companies using AI today are giving everyone a copilot, which makes the existing structure work slightly better without changing it. We're after something different: a company built as an intelligence."

> "A world model that can't touch the world is just a database."

> "The model is not the product. The understanding is the product."

> "Block is far enough along to show the idea is more than theory."

## Open Questions

1. How does this work when the world model is wrong? Block has honest signal (money). Most companies don't.
2. The DRI model assumes a pool of people capable of owning cross-cutting problems. That's a rare skill set. Does the model produce these people or require them?
3. "Parts of it will likely break before they work." Which parts? The essay is optimistic about the destination but vague about the transition path.
4. How does this interact with the three-tool cognitive ceiling from the brain fry research? Even with hierarchy removed, individual humans still have working memory limits.
