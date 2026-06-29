---
title: "Fleet of Agents and IBM Multi-Agent Collaboration: Genetic Filtering and Enterprise Frameworks"
tags:
- multi-agent
- fleet-of-agents
- genetic-filtering
- particle-filtering
- beeai
- watsonx
- agent-orchestration
- ibm
related:
- [[multi-agent-coordination-patterns]]
- [[subagent-architecture]]
- [[kanban-doctrine]]
- [[cross-agent-reporting-patterns]]
- [[centaur-principle]]
- [[cloudflare-first-agent-factory]]
- [[agent-native-operations]]
source: research/raw/fleet-of-agents-and-ibm-multi-agent-collaboration.md
ingested: 2026-06-29
---

# Fleet of Agents and IBM Multi-Agent Collaboration: Genetic Filtering and Enterprise Frameworks

## Summary

Two sources inform how we think about our fleet of specialist agent profiles. Klein et al.'s Fleet of Agents (FOA) provides the most rigorous formal treatment of fleet coordination in the LLM agent literature, applying genetic particle filtering to parallel exploration. IBM's multi-agent collaboration documentation covers both the conceptual framework and their open-source BeeAI Framework plus the commercial Watsonx Orchestrate product. The most strategically important finding: a fleet of small models, properly coordinated, beats a single large model.

## Fleet of Agents (FOA): Genetic Particle Filtering

FOA applies genetic particle filtering to LLM-based reasoning. A fleet of n agents explores the search space in parallel. After k exploration steps, a selection phase resamples the population: high-performing states are duplicated, low-performing ones replaced. This balances exploration and exploitation with predictable cost.

Key insight: this borrows from particle filtering, not swarm intelligence. Agents do not communicate with each other. They explore independently, then are pruned and resampled by a central value function. This is evolutionary search, not emergent cooperation.

The headline finding: FOA with LLaMA3.2-11B surpassed LLaMA3.2-90B working alone. A fleet of small models, properly coordinated, beats a single large model. This validates the core premise of the specialist profile architecture: multiple focused agents with cheaper models can outperform a single expensive generalist, provided the coordination layer is principled.

FOA's coordination model differs fundamentally from ours. FOA coordinates through a central value function that resamples agent states. Our fleet coordinates through shared substrate (knowledge graph), SITREPs, and Kanban work assignments. FOA is evolutionary search. We are mission command. The convergence is the conclusion, not the method: many cheap coordinated agents beat one expensive uncoordinated one.

## IBM's Five-Element Agent Model

IBM defines every agent as having five components: Foundation Model (reasoning engine), Objective (goal), Environment (situation including other agents and tools), Perception (input from surroundings), and Output/Action (response). This maps cleanly: Foundation Model is the Venice API model per profile, Objective is the mission or Kanban card, Environment is the Substrate plus tool gateway, Perception is the SITREP inbox and Substrate readings, Output is the SITREP and substrate commits.

Three collaboration strategies: rule-based (tightly controlled state machines), role-based (agents assigned specific roles with permissions), and model-based (probabilistic models of self, environment, and others). Our fleet is primarily role-based with elements of rule-based coordination (Contribution Protocol, SITREP format, Kanban rules). We are not doing model-based coordination (no probabilistic modeling of other agents), and probably should not.

## BeeAI Framework

IBM's open-source BeeAI framework (3.3k stars, Apache 2.0, Linux Foundation) implements multi-agent coordination. Architecture features: RequirementAgent for predictable behavior across LLMs, handoff tools for task delegation, serialization for state persistence, workflows for complex execution flows, A2A and MCP protocol support, and backend abstraction. The multi-agent pattern (named role-agents with scoped tools and instructions, coordinated by a dispatch layer) is structurally identical to how Hermes specialist profiles are configured. The difference: BeeAI is a library you write code against. Hermes is a runtime you configure.

## Watsonx Orchestrate

IBM's commercial product has five layers: Skills (independent agents in a registry), Intent Parser (NLP maps input to skills), Flow Orchestrator (execution logic with sequencing, branching, error handling), Shared Context and Memory Store (common space for data and decisions), and LLM Assistant (reasoning and context navigation). This is essentially the same five-layer model our fleet uses: dispatch/intent, orchestration, shared state, specialist execution, and reasoning.

## Cross-Cutting Observations

The fleet metaphor holds up. IBM explicitly uses it. FOA formalizes it academically. Alternatives are weaker: "swarm" implies emergent behavior we do not have. "Crew" implies tight coupling we avoid. "Multi-agent system" is accurate but sterile. Fleet captures the managed, semi-autonomous nature without overpromising autonomy.

Small models, properly coordinated, beat large models alone. FOA's result gives academic backing. IBM's docs independently argue the same case. Our specialist profiles run cheaper models and achieve breadth through specialization. The [[centaur-principle]] applies: quality of collaboration matters more than capability of either party alone.

## Cross-References

- Coordination patterns: [[multi-agent-coordination-patterns]]
- Subagent design principles: [[subagent-architecture]]
- Our operating model: [[kanban-doctrine]]
- Fleet reporting: [[cross-agent-reporting-patterns]]
- Human-AI collaboration quality: [[centaur-principle]]
- Factory and fleet metaphors align: [[cloudflare-first-agent-factory]]
- Operations domain: [[agent-native-operations]]