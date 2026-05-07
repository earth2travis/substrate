---
title: "Loom Service Specification"
source: "research/raw/loom-service-spec.md"
tags: ["loom", "specification", "orchestration", "agents", "github"]
related:
  - "[[loom-overview]]"
  - "[[agent-native-operations]]"
  - "[[workflow-as-contract]]"
  - "[[agent-platform-ecosystem]]"
  - "[[symphony-mapping]]"
  - "[[agent-orchestrator-pattern]]"
  - "[[workspace-isolation]]"
---

# Loom Service Specification

Defines a service that orchestrates coding agents to get project work done, using GitHub as the issue tracker, Claude Code as the coding agent, and Synthweave as the intelligence layer.

## Three Layer Architecture

1. **Orchestrator**: Poll, dispatch, concurrency, retry, reconcile. Pure scheduling logic.
2. **Synthweave**: Shared context, decision propagation, institutional memory, progress reporting.
3. **Claude Code**: Code changes, testing, PR creation in isolated workspaces.

## Core Components

1. **Workflow Loader**: Reads `WORKFLOW.md`, parses YAML front matter and prompt body
2. **Config Layer**: Typed getters for workflow config values
3. **Issue Tracker Client**: Fetches candidate issues from GitHub, normalizes payloads
4. **Orchestrator**: Owns poll tick, in-memory runtime state, dispatch decisions
5. **Workspace Manager**: Maps issues to workspace paths, runs lifecycle hooks
6. **Tool Provisioner**: Resolves tool declarations, validates CLI tools, generates `.mcp.json`
7. **Agent Runner**: Creates workspace, builds prompt, launches Claude Code CLI
8. **Logging**: Structured runtime logs

## WORKFLOW.md Format

Markdown with optional YAML front matter. Parsing rules:
- If file starts with `---`, parse until next `---` as YAML front matter
- Remaining lines become the prompt body
- Front matter must decode to a map

Top-level keys: `tracker`, `polling`, `workspace`, `hooks`, `agent`, `claude`, `tools`

## Key Design Decisions

- **Restart recovery without persistent database**: Queries GitHub and filesystem on restart
- **Dynamic config reload**: Changes to `WORKFLOW.md` take effect without restart
- **Claim semantics**: Issues labeled `agent:in-progress` to prevent duplicate dispatch
- **Bounded concurrency**: Global and per-label limits
- **No built-in business logic**: Ticket writes performed by the agent via tools
