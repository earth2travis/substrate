---
title: "just-bash: Virtual Shell for Agent Execution"
tags: [sandbox, security, agent-execution, typescript, isolation]
related: [[tools-landscape]], [[workflows-landscape]], [[agent-native-operations]], [[the-openclaw-lesson]]
source: research/raw/just-bash-analysis.md
---

# just-bash: Virtual Shell for Agent Execution

## Summary

just-bash is a TypeScript implementation of a bash interpreter with an in-memory virtual filesystem. It parses bash scripts into an AST and interprets them entirely in JavaScript, never spawning real child processes. ~79 built-in commands are reimplemented in TypeScript. Each Bash instance encapsulates a virtual filesystem, command registry, interpreter state, and execution limits.

Key design: state isolation per exec call, persistence via filesystem. Files written in one exec are visible in the next, but env vars and functions reset. Four filesystem implementations: InMemoryFs (pure sandbox), OverlayFs (read-only disk with copy-on-write), ReadWriteFs (real disk), and MountableFs (compose multiple zones).

Security model is unusually thorough: no child_process anywhere, path normalization with root containment, symlinks default-denied, network disabled by default with URL allow-lists, execution limits on loops/calls/expansion, re2js regex engine for linear-time guarantees, and prototype pollution guards throughout. Known gaps: no VM isolation (same V8 context), no total memory ceiling.

For Loom integration, just-bash is not a replacement for real OS access (no git, npm, test runners) but serves as a sandboxed pre-execution environment for script validation, data processing, and tool mediation via custom commands.
