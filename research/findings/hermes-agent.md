---
title: "Hermes Agent: Open-Source Multi-Provider Agent Platform"
tags: [agent, platform, infrastructure, open-source, nous]
related: [[nous-research]], [[openclaw]], [[clawhavoc-security-crisis]], [[llm-wiki-pattern]], [[codex]]
source: research/raw/hermes-agent.md
---

# Hermes Agent: Open-Source Multi-Provider Agent Platform

## Summary

Open-source (MIT) CLI agent platform by Nous Research. Multi-provider LLM access with skills, memory, cron, delegation, and multi-platform messaging. Version v0.7.0 as of April 2026.

## Core Architecture

- **Provider abstraction**: OpenAI, Anthropic, OpenRouter, Nous Portal, z.ai, Kimi, MiniMax
- **Skills system**: 60+ bundled skills, self-improving, installable
- **Memory**: Persistent across sessions, 2,200 char budget
- **Tools**: terminal, file ops, browser, search, web extraction
- **Delegation**: Subagent spawning for parallel tasks
- **Cron**: Scheduled background jobs
- **Messaging**: Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Web, CLI

## Terminal Backends

| Backend | Use Case |
|---------|----------|
| Local | Direct machine access |
| Docker | Containerized isolation |
| SSH | Remote machine access |
| Daytona | Serverless with hibernation |
| Modal | Serverless GPU-capable |
| Singularity | HPC environments |

## Key Differentiators

| vs OpenClaw | vs Claude Code |
|-------------|----------------|
| Security by design | No model lock-in |
| RL training (Atropos) | Self-improving skills loop |
| ~3000 tests, CI | Open source (MIT) |
| 6 terminal backends | Multi-platform messaging |
| Easy migration | FTS5 session search |

## Migration from OpenClaw

`hermes claw migrate` imports SOUL.md, memories, skills, API keys, messaging settings. Many users migrated following the [[clawhavoc-security-crisis]].

## Related

- [[nous-research]] — Creator organization
- [[openclaw]] — Predecessor framework
- [[clawhavoc-security-crisis]] — Security incident driving migration
- [[llm-wiki-pattern]] — Bundled as a skill
- [[codex]] — Alternative coding agent
