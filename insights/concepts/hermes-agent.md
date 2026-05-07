---
title: "Hermes Agent: Secure Multi-Provider Agent Platform"
tags: [concept, agent, platform, open-source, nous, infrastructure]
related:
- openclaw
- the-openclaw-lesson
- nous-research
- llm-wiki-pattern
- codex
- agent-native-operations
- context-stack
- agent-memory
source: research/findings/hermes-agent.md
---

# Hermes Agent: Secure Multi-Provider Agent Platform

## Thesis

Hermes Agent by Nous Research is the secure-by-design successor to OpenClaw. Where OpenClaw proved demand for local autonomous agents, Hermes proves that security, multi-provider flexibility, and self-improvement can coexist in a single open-source platform. The migration path (`hermes claw migrate`) reduced switching costs and accelerated community transition.

## Architecture

- **Provider abstraction**: OpenAI, Anthropic, OpenRouter, Nous Portal, z.ai, Kimi, MiniMax
- **Skills system**: 60+ bundled skills, self-improving, installable
- **Memory**: Persistent across sessions with 2,200 character budget and FTS5 search
- **Terminal backends**: Local, Docker, SSH, Daytona, Modal, Singularity
- **Delegation**: Subagent spawning for parallel task execution
- **Cron**: Scheduled background jobs for continuous operation
- **Messaging**: Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Web, CLI

## Security Model

Unlike OpenClaw's reactive patching, Hermes was designed with security from the start: comprehensive tool approval flows, sandboxed execution, curated skills hub, and ~3000 tests. The `hermes claw migrate` command imports SOUL.md, memories, skills, API keys, and messaging settings from OpenClaw.

## Related

- [[openclaw]] — Predecessor framework
- [[the-openclaw-lesson]] — Security lessons that shaped Hermes design
- [[nous-research]] — Organization behind the platform
- [[llm-wiki-pattern]] — Bundled as a skill
- [[codex]] — Alternative coding-focused agent
