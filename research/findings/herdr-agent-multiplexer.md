---
title: "Herdr: The Agent Multiplexer"
tags: [finding, herdr, tmux, agent-orchestration, terminal, cli]
related: [[agent-native-operations]], [[subagent-architecture]], [[multi-agent-coordination-patterns]]
source: research/raw/herdr-agent-multiplexer.md
ingested: 2026-05-07
---

# Herdr: The Agent Multiplexer

Herdr is a lightweight, Rust-based agent multiplexer that provides "tmux for agents": persistent sessions, workspaces, and agent-aware state management without GUI or Electron overhead.

## Key Points

**Agent Awareness.** Unlike standard tmux, Herdr understands agent state: blocked, working, done, idle. This is visible in the terminal UI, making it easy to see what the system is doing at a glance.

**Universal Remote Access.** Sessions are persistent and detachable. Start agents on a server, detach, close the laptop, reattach from any SSH client (even a phone). No extra apps required.

**Agent-Native Orchestration.** A local Unix socket allows agents to orchestrate each other: create workspaces, split panes, run commands, read output from other panes, wait for specific state changes ("wait until agent 1-1 is done").

**Terminal-Native.** Runs inside any terminal emulator (Ghostty, Alacritty, Kitty, WezTerm, iTerm2) and even inside tmux itself. Single binary, no dependencies.

**Comparison to standard tmux.**
- State Awareness: tmux has none; Herdr is agent-aware (blocked/working/done)
- Orchestration: tmux is manual key sends; Herdr is API-native (Unix socket for agents)
- Interface: tmux is terminal-only; Herdr is terminal + mouse-native
- Complexity: tmux is high (config files, plugins); Herdr is low (single binary, zero config)

**Implications for the Agent Factory.**
1. The Ops Agent can spawn workspaces for system health, disk usage, cron logs, and monitor them for blocked states.
2. Long-running deep research tasks on the Hetzner VPS can be started via Herdr, detached, and checked only when the agent signals done.
3. Agent-to-agent handoffs: Sivart can spawn a Koda workspace, wait for the "done" signal, then read results.

## Relevance

Herdr is the terminal-native orchestration layer that complements the Substrate's blackboard pattern. Where git is the persistent shared state, Herdr is the runtime coordination surface.

## Related

- [[agent-native-operations]] -- Executive layer design
- [[subagent-architecture]] -- Named specialists and orchestrator patterns
- [[multi-agent-coordination-patterns]] -- Blackboard and hierarchical patterns
