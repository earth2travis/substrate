---
title: "Agent Harness Architecture: Nine Components and the /goal Primitive"
tags:
- agent-architecture
- harness
- goal-primitive
- orchestration
- tooling
- convergence
related:
- [[agent-filesystems-infrastructure]]
- [[agent-native-operations]]
- [[skills-as-portable-knowledge]]
- [[goal-primitive]]
- [[clanker-agent-deployment-patterns]]
- [[karpathy-autoresearch]]
source: research/raw/agent-harness-architecture.md
ingested: 2026-06-29
---

# Agent Harness Architecture: Nine Components and the /goal Primitive

## Summary

The agent harness has emerged as the product, not the model. Every major provider (Anthropic, OpenAI, xAI) is building a coding harness, confirming that the harness is where value accrues. Aparna Dhinak's taxonomy identifies nine components that every harness converges on. The /goal primitive is emerging as a cross-platform standard for agent task assignment. Peter Steinberger's Printing Press extends the harness concept into a tool factory.

## Nine Components of Harness Architecture

1. **Outer Iteration Loop** — the while loop. Model decides what tools to call, iterates until done.
2. **Context Management and Compression** — what to pull into context, how to simplify large data.
3. **Skills/Tools Management** — tool registry, composition, data passing.
4. **SubAgent Management** — spawning child agents when tasks get too big.
5. **Built-in pre-packaged skills** — shipping with working capabilities.
6. **Session Persistence and Recovery** — surviving crashes, resuming work.
7. **System Prompt Assembly / Project Context Injection** — building the prompt from project state.
8. **Life Cycle Hooks** — extensible checkpoints in the agent execution flow.
9. **Permission and Safety Layer** — controls on what the agent can do.

The key distinction: a harness works out of the box. It ships as a working agent with fixed architecture. No assembly step. The alternative (LangChain, LangGraph) is a framework for humans to build agents. The harness is born bottom-up from coding agents solving real problems.

## The /goal Primitive

/goal is not a feature. It is a primitive, like HTTP or JSON. A regular prompt asks an agent for the next response; /goal flips that. You write down what "done" looks like, submit it once, and the agent works toward it until it gets there. The goal stays active until achieved, paused, blocked, cleared, or budget runs out. This is a shift from prompting (you driving) to assigning (the agent driving toward a target).

Three tools speak /goal: Codex (OpenAI), Claude Code (Anthropic), and Hermes Agent (orchestrator). What /goal needs next: a common schema, a shared registry of verified goal types, and a protocol for handing off goals between tools. This directly validates the Mission Contract philosophy and the [[goal-primitive]] concept in the Substrate.

## The Harness Is the Backend

Mike Piccolo's thesis: the most important architectural question is not which model to use but how much infrastructure is required to build something useful with it. The spectrum of harness thickness runs from thin (Anthropic: elegant loop, model decides everything) to thick (LangGraph: every decision a node, every transition an edge). The hidden assumption that the harness is extrinsic to the backend is temporary. A backend has workers, triggers, and functions. The harness and backend will merge.

## Scientific Harness Optimization

The Agentic Harness Engineering paper (arxiv 2604.25850) applies scientific rigor to harness evolution. Three layers: components as revertible files, experience as condensed evidence from millions of trajectory tokens, decisions as falsifiable predictions checked against task outcomes. Results: pass@1 Terminal-Bench 2 improved from 69.7% to 77.0% in ten iterations, beating human-designed Codex-CLI (71.9%). The harness improves itself. Transfers across model families with +5.1 to +10.1 point gains. Uses 12% fewer tokens.

## Breadth of the Harness Category

Grok Build (xAI) confirms every major model provider is building a harness. Symphony (OpenAI) enters orchestration, turning task trackers into always-on systems for agentic work. Claude Managed Agents adds dreaming (offline learning), outcomes (quality bar enforcement), and multiagent orchestration. Autobrowse graduates browser agent runs into durable reusable skills (markdown). Printing Press generates token-efficient CLIs, skills, and MCP servers from any API spec.

## Cross-References

- Filesystems that store harness artifacts: [[agent-filesystems-infrastructure]]
- Agent-native operations as the domain: [[agent-native-operations]]
- Skills as portable knowledge: [[skills-as-portable-knowledge]]
- /goal as coordination primitive: [[goal-primitive]]
- Deployment patterns: [[clanker-agent-deployment-patterns]]
- Constraint architecture parallel: [[karpathy-autoresearch]]