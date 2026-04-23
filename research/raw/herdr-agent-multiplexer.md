---
title: "Herdr: The Agent Multiplexer"
source: "https://herdr.dev/"
date: 2026-04-23
tags: [herdr, tmux, agent-orchestration, terminal, cli]
---

# Herdr: The Agent Multiplexer

## Summary
**Herdr** is a lightweight, Rust-based agent multiplexer that lives in the terminal. It provides "tmux for agents" by offering persistent sessions, workspaces, and agent-aware state management (blocked, working, done) without the overhead of a GUI or Electron app.

## Key Features

### 1. Agent Awareness
Unlike standard `tmux`, Herdr understands the **state** of the agents running within it. It can visually indicate if an agent is:
*   **Blocked:** Waiting for input or stuck.
*   **Working:** Actively processing.
*   **Done:** Finished its task.
*   **Idle:** Waiting for instructions.

### 2. Universal Remote Access
Herdr sessions are persistent and detachable. You can:
*   Start agents on a server.
*   Detach (`ctrl+b q`) and close your laptop.
*   Reattach from any SSH client (even a phone) to see the exact same state.
*   No extra apps or GUI wrappers are required—just the terminal.

### 3. Agent-Native Orchestration
Herdr exposes a **local Unix socket** that allows agents to orchestrate each other. An agent can:
*   Create new workspaces or tabs.
*   Split panes and run commands in them.
*   Read output from other panes.
*   Wait for specific state changes (e.g., "wait until agent 1-1 is done").

### 4. Terminal-Native
It runs inside any terminal emulator (Ghostty, Alacritty, Kitty, WezTerm, iTerm2) and even works inside `tmux` itself. It is a single binary with no dependencies.

## How It Fits With Our TMUX Research

Our previous research on **TMUX** focused on using it as a "remote-control" interface for interactive CLIs. Herdr takes this concept and **specializes it for the agent economy**:

| Feature | Standard TMUX | Herdr |
| :--- | :--- | :--- |
| **State Awareness** | None (just text on a screen) | **Agent-Aware** (Blocked/Working/Done) |
| **Orchestration** | Manual key sends | **API-Native** (Unix socket for agents) |
| **Interface** | Terminal-only | **Terminal + Mouse-Native** |
| **Complexity** | High (config files, plugins) | **Low** (Single binary, zero config) |

## Implications for The Agent Factory

1.  **The "Ops" Agent:** Herdr is the perfect interface for our **Ops Agent**. It can spawn a workspace for "System Health," split a pane for "Disk Usage," and another for "Cron Logs," then monitor them for "Blocked" states.
2.  **Decoupled Execution:** We can start long-running "Deep Research" tasks on our Hetzner VPS via Herdr, detach, and only check back when the agent signals it is "Done."
3.  **Agent-to-Agent Handoffs:** Using the Unix socket, Sivart can spawn a Koda workspace for a specific coding task, wait for the "Done" signal, and then read the results to synthesize them into the Substrate.

## Related
- [[tmux-skill]]
- [[agent-orchestration-patterns]]
- [[the-substrate-spec]]