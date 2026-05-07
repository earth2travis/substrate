---
title: "Progressive Autonomy"
tags: [concept, governance, feature-flags, agents]
related: [centaur-principle, institutional-ai-redesign, agent-native-operations, kanban-doctrine, feature-flags-best-practices]
---

# Progressive Autonomy

## Definition

The practice of using feature flags and graduated trust mechanisms to expand or contract an agent's autonomous scope based on demonstrated reliability, rather than fixing permissions in code.

## Core Idea

Autonomy is not binary. It is a dial. Progressive autonomy treats agent capabilities as runtime-configurable flags that can be toggled without redeployment, enabling:
- Graduated trust expansion (human approval → semi-autonomous → fully autonomous)
- Instant rollback when autonomy goes wrong (kill switches)
- A/B testing of agent behavior variants
- Environment-specific capability tiers

## Key Principles

**Start with Flags, Not Code**
Every new autonomous capability should ship behind a flag. This decouples deploy from release and creates a safety margin between "code exists" and "code runs."

**Canary for Agents**
Roll out autonomous behavior in stages:
1. Internal dogfooding (single operator)
2. 1% of tasks (monitor for anomalies)
3. 10% of tasks (measure against baseline)
4. 50% of tasks (compare outcomes)
5. General availability (with kill switch retained)

**Kill Switches Are Non-Negotiable**
Every autonomous capability needs a corresponding kill switch that can be flipped in seconds without a deployment. The cost of a mistaken autonomous action is higher than the cost of a delayed feature.

**Measure Before Expanding**
Progressive autonomy requires telemetry. Before expanding an agent's scope, you need baseline metrics: error rates, correction frequencies, escalation rates, and outcome quality.

## Applications

**Model Selection Flags**
Toggle which model handles which tasks based on cost/quality tradeoffs or availability.

**Tool Access Tiers**
Grant or revoke tool permissions per environment (development vs staging vs production) or per agent maturity level.

**Progressive Handoff**
Start with human-in-the-loop approval for novel actions. Gradually remove the loop as the agent demonstrates reliability.

**Multi-Agent Coordination**
Flags control which agent handles which domain, handoff protocols, and fallback chains when primary agents fail.

## Related

- [[centaur-principle]]: human-AI collaboration beats solo AI
- [[institutional-ai-redesign]]: redesign the factory, don't just swap the motor
- [[agent-native-operations]]: agents are first-class operators
- [[kanban-doctrine]]: visualizing work and limiting WIP applies to agent workflows too
- [[feature-flags-best-practices]]: implementation details and anti-patterns
