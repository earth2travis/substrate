---
title: "Workspace Isolation"
tags: ["agents", "concurrency", "infrastructure", "git", "safety"]
related:
  - "[[agent-native-operations]]"
  - "[[agent-orchestrator-pattern]]"
  - "[[agent-factory-production-system]]"
  - "[[agent-platform-ecosystem]]"
---

# Workspace Isolation

When multiple agents run concurrently on different issues, workspace isolation becomes essential. Without it, agents overwrite each other's work, corrupt the git state, and produce irreproducible results.

## The Pattern

Each issue gets its own directory under a configurable workspace root:

```
~/workspaces/
├── _123/          # Issue #123
├── _124/          # Issue #124
└── _125/          # Issue #125
```

Each workspace gets its own git clone via lifecycle hooks. Workspaces persist across retries for the same issue but are cleaned when issues reach terminal state. Strict path containment: workspaces must stay inside the root.

## Lifecycle Hooks

- `after_create`: Runs when a workspace is first created (git clone, dependency installation)
- `before_run`: Runs before each agent attempt (git fetch, rebase on main, create branch)
- `after_run`: Runs after each attempt (cleanup, metrics collection)
- `before_remove`: Runs before workspace deletion (final cleanup)

## Why It Matters

A single shared workspace works for one agent at a time. As soon as you run multiple agents concurrently, whether on different issues or different parts of the same issue, isolation is required. This is not just about preventing conflicts. It is about making agent behavior reproducible. An agent that depends on the state left by a previous agent is not reproducible.

## Current Gap

Our architecture operates in a single workspace (/home/clawd/clawd). All work happens in one repository. Sub agents work in the same directory tree. There is no isolation between concurrent tasks beyond git branching. This is a genuine gap that should be closed before scaling concurrent agent execution.
