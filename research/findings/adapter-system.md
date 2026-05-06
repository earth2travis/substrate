---
title: "Paperclip Adapter System: Three-Consumer Architecture"
tags: [agents, architecture, adapters, paperclip]
related: [[agent-architectures]], [[agent-skills-as-onboarding]]
source: research/raw/adapter-system.md
---

# Paperclip Adapter System: Three-Consumer Architecture

## Summary

Paperclip uses a three-consumer adapter model where each adapter provides implementations for server, UI, and CLI. Adapters live in `packages/adapters/<name>/` with four exports: shared metadata, server module, UI module, CLI module. Three registries consume these modules.

## The Contract

**ServerAdapterModule** (core):
- `execute(ctx)` — runs the agent
- `testEnvironment(ctx)` — preflight diagnostics
- Optional: `sessionCodec`, `supportsLocalAgentJwt`, `onHireApproved`

**Input context** includes: runId, agent config, runtime params, context records, log callbacks.
**Output result** includes: exitCode, signal, timedOut, errorMessage, usage summary, session state.

## Key Design Decisions

- **Session codec**: Serialize/deserialize session state between runs. Enables durable agent identity across invocations.
- **Local agent JWT**: Short-lived token injected as `PAPERCLIP_API_KEY` for authenticated callbacks.
- **Environment test**: Preflight diagnostics before the "Test environment" UI button commits to a run.

## Applicability

The three-consumer pattern is specific to Paperclip's architecture but generalizes: any agent system that needs to run in multiple contexts (server daemon, interactive UI, CLI script) benefits from isolating environment-specific code behind a common interface.