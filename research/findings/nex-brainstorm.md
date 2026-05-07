---
title: "Nex AI Brainstorm: Team Agent on OpenClaw"
tags: [nex, team-agent, openclaw, multiplayer, synthweave, brainstorming]
related:
- agent-orchestrator-pattern
- multi-agent-coordination-patterns
- full-visual-blueprint
- single-player-vs-multiplayer
source: research/raw/nex-brainstorm.md
---
# Nex AI Brainstorm: Team Agent on OpenClaw

_February 19, 2026. Synthweave team session._

## The Core Problem

OpenClaw is deeply single player. Built for one human, one agent. Synthweave hacked around this by treating the company as the "single user" and team members as "employees." Works well enough to be mind blowing, but breaks predictably:

- Memory is per user, not per team member
- MCP access goes through one user's permissions
- Can't read DMs between team members
- No per person notification preferences
- Heartbeat is global, not per individual

## Infrastructure

Running on Render in Docker (not ideal). Homebrew in persistent storage. Connected to Synthweave (MCP) and GitHub. Heartbeat every 30 minutes. Container rebuilds require manual rewiring.

## What Each Person Wanted

| Person | Need |
|---|---|
| Mak | Standup assistance, weekly reports, reminders |
| Travis | Celebration and visibility (not surveillance) |
| Andrei | Product feedback tracking, DM notifications |
| Emiliano | Project progress, milestone tracking |
| Alexey | Enhanced PR notifications, sync PRs with issues |
| Le | Individual agent per member with custom instructions |
| Micah | Automated ticket management, multiplayer coding |

## Three Big Insights

1. **OpenClaw is not multiplayer.** Memory, permissions, notifications all assume one human. The gap MultiClaw could fill.

2. **Synthweave snips as agent memory.** Instead of local markdown files, use bases as the knowledge layer. Team visibility, collaborative editing, path toward "git for context files."

3. **Multi-agent dashboard as hosted service.** Each team member has their own agent. The business is the brain; agents are the hands. Synthweave becomes the substrate that connects them.

## Key Quote

Emiliano: "Our build velocity is starting to get really fast and really impressive... but visibility and alignment around priorities and backlog states, that stuff is falling behind."

Micah: "OpenClaw is deeply single player. It was built to service one person."
