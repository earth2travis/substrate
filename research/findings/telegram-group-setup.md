---
title: "Telegram Group Setup: Forum-Based Multi-Agent Workspace"
tags: [telegram, agent, communication, workspace, multi-agent, operations]
related: [[openclaw]], [[hermes-agent]], [[harness-engineering]], [[dark-factory]], [[custom-tooling-opportunities]], [[agent-native-operations]]
source: research/raw/telegram-group-setup.md
---

# Telegram Group Setup: Forum-Based Multi-Agent Workspace

## Summary

Research for moving from flat DM chat to a Telegram forum group with topic-based channels for project threading. Telegram "forum mode" (Topics) turns a supergroup into a threaded workspace. Each topic is an independent thread with its own message history. OpenClaw has first-class support for per-topic isolated sessions.

## Key Claims

**One bot, multiple topics (simpler, recommended now).** Single bot token, one identity in the group. Each topic is an isolated session. Can set per-topic systemPrompt to specialize behavior. All topics share the same agent workspace and tools. Lower config overhead.

**Multiple bots, multiple topics (multi-agent future).** Each bot gets its own workspace, tools, memory, SOUL.md. True isolation between agents. Requires separate BotFather token per bot. More config, more infra. Dan Malone's setup runs 4 agents this way successfully.

**Proposed topic structure:** General (default, catch-all), Operations (infra, server, OpenClaw, tooling), Research (deep dives, reading, analysis), Framing (project work, issues, PRs), Writing (transmissions, essays, creative), Comms (Farcaster, social, external).

**Session isolation.** Each topic is a separate session. Conversation in Research won't be visible in Framing. Context stays focused. The DM channel continues alongside the group.

**Routing cron outputs.** Cron jobs can target specific topics. Email triage results → Operations. Calendar alerts → General. Project audit results → Framing. Release monitor → Operations.

**createForumTopic tool.** OpenClaw can programmatically create new topics when new projects spin up. No need to do it manually every time.

## Architecture Decision: One Bot vs Multiple Bots

| Aspect | One Bot + Topics | Multiple Bots |
|--------|------------------|---------------|
| Config overhead | Low | High |
| Session isolation | Per-topic | Per-bot |
| Tool sharing | Shared | Separate |
| Memory | Shared | Separate |
| Cross-agent comms | sessions_send | sessions_send |
| Recommendation | Start here | Future phase |

## Setup Steps

1. Create Telegram group, convert to supergroup, enable Topics
2. Add Sivart bot, make admin
3. Create topics manually: General, Operations, Research, Framing, Writing, Comms
4. Note group chat ID and topic threadIds from logs
5. Update OpenClaw config with per-topic settings
6. Set BotFather privacy to OFF (bot sees all messages)

## Connection to Agent Factories

The Telegram group structure is the human-agent interface for the Agent Factory. Topic-based threading prevents context contamination. Per-topic specialization allows different agents to handle different domains. The pattern is proven: Dan Malone runs 4 agents in a single group this way.

## Related

- [[openclaw]] — Platform with first-class Telegram forum support
- [[hermes-agent]] — Secure successor with Telegram integration
- [[harness-engineering]] — Methodology for agent-first development
- [[dark-factory]] — Lights-out operation requiring clear routing
- [[custom-tooling-opportunities]] — Agent-native tooling for workspace management
