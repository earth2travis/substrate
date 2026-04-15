---
title: Hermes Agent
created: 2026-04-08
updated: 2026-04-13
type: entity
tags: [agent, platform, infrastructure]
sources:
  - raw/articles/karpathy-llm-wiki-pattern.md
  - raw/hermes-agent-deep-research.md
---

# Hermes Agent

> Open-source CLI agent platform by Nous Research, providing multi-provider LLM access with skills, memory, and multi-platform messaging.

## Key Facts

- **Project:** [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- **Current Version:** v0.7.0 (2026.4.3) -- "The resilience release"
- **Release Date:** April 3, 2026
- **Scale:** 168 PRs, 46 resolved issues in v0.7.0
- **License:** MIT

## Core Architecture

Multi-provider LLM agent with:

- **Provider abstraction** -- OpenAI, Anthropic, OpenRouter, and others. Configurable via config.yaml
- **Skills system** -- Reusable procedural knowledge loaded as needed
- **Memory** -- Persistent across sessions. 2,200 char budget for memory entries
- **Tool system** -- terminal, file operations, browser, search, web extraction
- **Delegation** -- Subagent spawning for parallel task execution
- **Cron** -- Scheduled background jobs

## Messaging Platforms

Gateway routes agent to multiple platforms:
- Telegram
- Discord
- Slack
- WhatsApp
- Web (API/Open WebUI)
- CLI (interactive terminal)
- Matrix

## Notable Features

- Pluggable memory provider interface (extensible backend system)
- Credential pool rotation (multi-API-key load balancing)
- Camofox anti-detection browser backend
- Inline diff previews for file operations
- API server with streaming tool progress
- Editor integration (ACP -- editors can register MCP servers)
- Security hardening (secret exfiltration blocking)

## Skills

Over 60 bundled skills covering:
- Autonomous agents (Codex, Claude Code, OpenCode, OpenDevin)
- Data science (Jupyter, Dask)
- GitHub workflow
- Research (arXiv, DuckDuckGo, domain intel)
- Media (YouTube, music, GIFs)
- MLOps (model training, serving, vector DBs)
- Productivity (Linear, Notion, Google Workspace)
- Smart home, email, social media

## Architecture Details

### Six Terminal Backends
| Backend | Use Case | Persistence |
|---------|----------|-------------|
| **Local** | Direct machine access | Session-based |
| **Docker** | Containerized isolation | Session-based |
| **SSH** | Remote machine access | Session-based |
| **Daytona** | Serverless with hibernation | Serverless |
| **Modal** | Serverless GPU-capable | Serverless |
| **Singularity** | HPC environments | Session-based |

### Tool Registry Pattern
Each tool calls `registry.register()` at import time -- self-documenting, self-registering. Adding a tool requires only creating a file and calling register(). Tool schemas are auto-discovered, central registry handles dispatch/validation.

### Synchronous Agent Loop
Unlike async agent frameworks, Hermes uses a synchronous loop -- simplifies reasoning about state, makes debugging easier.

### Central Command Registry
All slash commands defined in `COMMAND_REGISTRY` list of `CommandDef` objects. Every consumer (CLI, Gateway, Telegram, Slack, autocomplete) derives from this single source.

### Context File Injection
Context files (AGENTS.md, claude.md) automatically loaded and injected as user messages to preserve Anthropic prompt caching while giving the agent project awareness.

### Skin Engine
Data-driven CLI theming -- banner colors, spinner faces/verbs/wings, tool prefix, response box, branding text. Initialized from `display.skin` config key at startup.

## Research Infrastructure
- Batch trajectory generation for training data
- Atropos RL environments for reinforcement learning
- Trajectory compression for next-gen tool-calling models
- Integration with tinker-atropos submodule for RL fine-tuning
- Support for GRPO, DPO, and other RL training methods

## Competitive Position
- **vs OpenClaw**: Security by design, ~3000 tests, 6 backends, RL integration, model-agnostic, easy migration via `hermes claw migrate` command
- **vs Claude Code**: No model lock-in, self-improving skills, cross-platform messaging, open source (MIT), FTS5 session search
- **Only agent with genuine closed learning loop**: memory + autonomous skill creation + skill self-improvement + session search

## Relationship to OpenClaw
Hermes evolved from [[openclaw]] (Steve Tigue/llmstxt.org). Code inheritance includes clawdbot's incomplete-text recovery patterns and rate limiting. Full migration tool (`hermes claw migrate`) imports SOUL.md, memories, skills, API keys, messaging settings. After the [[clawhavoc-security-crisis]], many users migrated from OpenClaw to Hermes.

## See Also
- [[nous-research]] -- creator organization
- [[llm-wiki-pattern]] -- Wiki pattern implemented as bundled skill
- [[openclaw]] -- predecessor framework
- [[clawhavoc-security-crisis]] -- security incident driving OpenClaw→Hermes migration
- [[llm-wiki-pattern]] -- LLM wiki pattern used in Hermes research
- [[simulacra-hyperreality]] -- LLMs as third-order simulacra
- [[dsjjjj-desiderata]] -- Nous Research's philosophical stance on AI alignment
