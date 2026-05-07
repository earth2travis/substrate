---
title: "6 AI Agents That Run a Company"
tags: [finding, agent-factory, multi-agent, orchestration, proposal-system]
related:
- agent-factory-production-system
- agent-native-operations
- kanban-doctrine
- skills-as-portable-knowledge
source: research/raw/ai-agents-that-run-a-company.md
ingested: 2026-05-07
---
# 6 AI Agents That Run a Company

A build guide for running a company with 6 AI agents performing real work: scanning intelligence, writing content, posting tweets, and running analyses. Tech stack: Next.js + Supabase + VPS. Monthly cost: $8 fixed + LLM usage.

## Key Points

**Four-table closed loop.** The entire system skeleton is 4 tables: Proposal → Mission → Step → Event → back to Proposal. Agents propose ideas, missions get approved and broken into steps, execution fires events, events trigger new ideas. This is the closed loop that runs forever.

**Single proposal intake pipeline.** All proposals, whether from agent initiative, automatic triggers, or reactions from other agents, go through one entry point. This prevents the chaos of multiple creation paths with inconsistent approval logic.

**Cap Gates at entry.** Check quotas at proposal submission, not at execution. If the tweet quota is full, reject immediately. No task enters the queue. Each step kind has its own gate (write content, post tweet, deploy) preventing pile-up of unexecutable tasks.

**Auto-approve for low-risk tasks.** High-risk tasks require human approval; low-risk tasks pass automatically. The system scales by calibrating which tasks need oversight and which can flow autonomously.

**Relationship dynamics.** Agents remember lessons learned and factor them into future decisions. Speaking styles evolve based on experience. Affinity between agents shifts: collaborate more, affinity rises; argue too much, it drops.

**Frontend transparency.** A pixel-art office shows everything in real time: agent locations, conversations, task status. This is not just monitoring; it is the user interface for understanding what the system is doing.

**No frameworks required.** No OpenAI Assistants API, no LangChain, no AutoGPT. Just PostgreSQL + Node.js workers + a rule engine. The complexity is in the process, not the dependencies.

## Relevance

This validates the Agent Factory thesis from a different angle: a single builder proved that 6 coordinated agents can run operations end-to-end with minimal infrastructure. The proposal system, cap gates, and relationship dynamics are directly applicable to Loom's orchestration layer.

## Related

- [[agent-factory-production-system]] -- Toyota-modeled production system for agents
- [[agent-native-operations]] -- Tools for the AI-human partnership
- [[kanban-doctrine]] -- Pull-based work assignment for agents
