---
title: "Hermes Agent Platform: Deep Research Report"
tags: [hermes-agent, agent, platform, architecture, tools, memory]
related: [[hermes-agent]], [[openclaw]], [[nous-research]], [[harness-engineering]]
source: research/raw/hermes-agent-report.md
---

# Hermes Agent Platform: Deep Research Report

## Summary

Hermes Agent v0.7.0 is an open-source (MIT), self-improving AI agent platform by Nous Research. It features 40+ tools, 6 terminal backends, multi-platform gateway, model-agnostic design, and a genuine closed learning loop with autonomous skill creation and FTS5 session search.

## Key Claims

1. **Self-Improving Memory Loop:** Persistent memory across sessions, autonomous skill creation after complex tasks (5+ tool calls), skills self-improve during use, FTS5 session search with LLM summarization, Honcho dialectic user modeling.
2. **40+ Tool Ecosystem:** Terminal execution (6 backends), file operations, web extraction, browser automation, subagent delegation, Python sandbox, full MCP client, cron scheduling, TTS, vision analysis, dangerous command approval, background process management, image generation.
3. **Six Terminal Backends:** Local, Docker, SSH, Daytona (serverless with hibernation), Modal (serverless GPU), Singularity (HPC). Runs from $5 VPS to GPU clusters.
4. **Multi-Platform Gateway:** Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant with conversation continuity and cross-platform history.
5. **Active Development:** Multiple commits per day with focus on quality (test isolation, approval security, edge-case handling). ~3000 tests.

## Implications

Hermes is the most ambitious open-source agent platform available. The closed learning loop (experience → skill → memory → better performance) is genuinely novel and positions it as potential foundational AI infrastructure.

## Related

- [[hermes-agent]] — Earlier finding on Hermes
- [[openclaw]] — Platform Hermes evolved from
- [[nous-research]] — Organization behind Hermes
- [[harness-engineering]] — Methodology for agent-first development
