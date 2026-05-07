---
title: "Loom: Autonomous Coding Agent Orchestration"
source: "research/raw/loom-overview.md"
tags: ["loom", "agents", "orchestration", "github", "claude-code"]
related:
  - "[[agent-native-operations]]"
  - "[[workflow-as-contract]]"
  - "[[agent-platform-ecosystem]]"
  - "[[harness-engineering]]"
  - "[[loom-service-spec]]"
  - "[[symphony-mapping]]"
---

# Loom: Autonomous Coding Agent Orchestration

Loom is a system that turns a backlog of GitHub issues into completed, verified code without humans writing any of it.

## How It Works

You label an issue `agent:ready`. Loom picks it up, creates an isolated workspace, launches a Claude Code agent, and that agent reads the issue, searches for relevant context in Synthweave, writes the code, runs the tests, opens a PR, and reports back. If it fails, Loom retries with exponential backoff. If the issue gets closed while the agent is working, Loom kills the agent and cleans up.

Humans steer. Agents execute.

## The Three Layers

1. **Orchestrator**: Polls GitHub every 30 seconds, dispatches work, manages concurrency, retries, reconciliation. Pure scheduling logic.
2. **Claude Code**: The execution engine. Fresh invocation per issue in an isolated workspace. Swappable.
3. **Synthweave**: The intelligence layer. Shared team context, decision propagation, institutional memory, progress reporting.

## Workspace Lifecycle

Each issue gets its own directory under the workspace root. Hooks run at each stage:
- `after_create`: git clone, dependency installation
- `before_run`: git fetch, rebase on main, create branch
- `after_run`: cleanup
- `before_remove`: final cleanup before deletion

## Stall Detection

Because Claude Code is a CLI tool (not a persistent process with streaming events), the orchestrator cannot observe the agent directly. Instead, the agent reports progress to Synthweave periodically. If no progress report arrives within `stall_timeout_ms` (default: 5 minutes), the agent is considered stalled, killed, and retried.

## WORKFLOW.md

Everything about how Loom behaves is defined in one file, checked into the repo alongside the code. YAML front matter configures the system. The Markdown body is the prompt template, rendered with issue data at dispatch time. Changes are picked up automatically without restart.

## Differences from OpenAI's Symphony

| Aspect | Original Symphony | Loom |
|--------|-------------------|------|
| Issue tracker | Linear (GraphQL) | GitHub Issues + Projects |
| Coding agent | Codex app server (persistent JSON-RPC) | Claude Code CLI (invocation-based) |
| Intelligence layer | None | Synthweave MCP |
| Tool provisioning | Implicit | Explicit, declarative |
| Agent communication | Bidirectional stdio pipe | MCP + CLI output |
| Stall detection | Event stream monitoring | Synthweave progress reports |
| Claim visibility | Internal only | GitHub label (`agent:in-progress`) |
| Default concurrency | 10 | 3 |

## Prerequisites

1. A well structured codebase with tests, types, linters, CI
2. Well specified issues with clear acceptance criteria
3. Willingness to invest in the harness

Loom does not replace engineering judgment. It replaces the mechanical translation of well understood requirements into working code.
