---
title: Agent Orchestrator Pattern
tags:
- agents
- orchestration
- automation
- github
- workflow
related:
- agent-native-operations
- agent-platform-ecosystem
- workflow-as-contract
- agent-factory-production-system
- harness-engineering
- hermes-agent-platform-analysis
- hermes-agent-report
- hermes-deployment-guide
- hermes-kanban-deep-dive
- hermes-self-evolution
---




# Agent Orchestrator Pattern

The agent orchestrator pattern turns an issue backlog into completed, verified code without human execution. It is not a job scheduler. It is a system for making the mechanical translation of well understood requirements into working code autonomous.

## The Core Loop

1. Poll the issue tracker every N seconds for issues matching specific criteria
2. For each eligible issue, claim it, create an isolated workspace, and dispatch an agent
3. The agent reads the issue, searches for context, writes code, runs tests, opens a PR
4. If the agent fails, retry with exponential backoff
5. If the issue goes terminal while the agent is working, kill the agent and clean up
6. Reconcile continuously: verify claimed issues are still active, kill stale agents

## The Three Layers

1. **Orchestrator (scheduler)**: Poll, dispatch, concurrency, retry, reconcile. No opinions about what the agent knows or how it reasons.
2. **Intelligence layer**: Shared context, decision propagation, institutional memory, progress reporting. Every agent benefits from what previous agents learned.
3. **Execution engine**: Does the actual work in isolated workspaces. Swappable.

## Key Design Decisions

- **Workspace isolation**: Each issue gets its own directory with its own git clone. Prevents conflicts between concurrent agents.
- **Claim semantics**: Issues are labeled as claimed to prevent duplicate dispatch. Labels are the coordination mechanism.
- **Stall detection**: Agents report progress periodically. If no report arrives within the timeout, the agent is considered stalled, killed, and retried.
- **Dynamic config reload**: The orchestrator's behavior is defined in a repo-owned file (WORKFLOW.md) that is reloaded without restart.
- **Restart recovery without persistent database**: On restart, the orchestrator queries the tracker and filesystem to reconstruct state.

## What It Enables

The pattern shifts the human role from executing to steering. Humans decide what to build and why. Agents figure out how and do it. This is the closest production implementation of the Moravec automated corporation thesis: work is defined in a tracker, agents autonomously execute, verification is automated, landing is automated, and the human role is environmental.

## What It Does Not Replace

The orchestrator pattern is for routine, well specified issues that do not require human judgment. It does not replace: relational architecture, soul documents, proactive behavior, taste and discretion, or creative work. The pattern becomes valuable when you have a backlog of mechanical work that is well understood but time-consuming.
