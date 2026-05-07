---
title: "Agentic Workflows Landscape: Orchestration Frameworks Compared"
tags: [workflows, orchestration, agent-frameworks, symphony, langgraph, production]
related:
- skills-landscape
- tools-landscape
- dark-factory
- harness-engineering
- kanban-doctrine
source: research/raw/workflows-landscape.md
---
# Agentic Workflows Landscape: Orchestration Frameworks Compared

## Summary

Five frameworks dominate agent orchestration, each embodying a different philosophy. OpenAI Symphony (March 2026) is a daemon that turns issue trackers into agent work queues: polls Linear, creates isolated per-issue workspaces, runs coding agents with bounded concurrency. It treats agents as factory workers with external orchestration, not internal agent-to-agent coordination. This is the simplest architecture that works in production.

OpenAI Swarm provides unified stack with black-box state management. Perfect for prototyping, poor for production. LangGraph offers full control through state graphs, checkpointing, and human-in-the-loop interrupt nodes. Best when reliability and auditability matter. CrewAI uses role-based agent teams with intuitive mental models but limited control. AutoGen models everything as conversation, unmatched for exploration but too unpredictable for production.

The emerging consensus for 2026: hybrid approaches win. Use state machines for outer orchestration (what happens when), dynamic planning for inner execution (how an agent accomplishes its step). Symphony exemplifies this pattern. Circuit breakers (token budgets, time limits, retry caps) are non-negotiable for production.
