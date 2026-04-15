---
title: "OpenClaw"
created: 2026-04-13
updated: 2026-04-13
type: entity
tags: [agent, platform, company, tools]
sources:
  - raw/openclaw-report.md
  - raw/openclaw-vs-hermes-coding.md
  - raw/hermes-agent-report.md
---

# OpenClaw

## Overview

OpenClaw is the pioneering open-source, self-hosted AI agent framework created by [[steve-tigue]] (creator of llmstxt.org). It reached **250K GitHub stars** and was arguably the first widely adopted self-hosted AI agent framework.

## Core Architecture

- **Local-first execution** — runs on your machine, not in the cloud
- **Tool-calling agent loop** — similar to modern agent architectures
- **Skills system** — modular, installable capabilities
- **ClawHub** — marketplace for community-contributed skills (1200+ skills)
- **Persistent memory** — agent remembers context between sessions
- **Multiple messaging platform support** — Telegram, Discord, etc.
- **Python-based, config-driven** — YAML configuration, plugin architecture
- **Dreaming feature** — background memory consolidation (recent addition)

### ACP Protocol

OpenClaw pioneered the Agent Client Protocol for connecting AI agents to IDEs. Multiple tutorials exist on "bridging IDEs to AI agents" using OpenClaw. Hermes Agent inherits this pattern through its own ACP adapter.

## Rise

- 250K GitHub stars — massive adoption
- ClawHub marketplace — hundreds of community skills
- Active Discord community
- Extensive media coverage in major tech publications

Before OpenClaw, most agent work was either cloud-based (ChatGPT, Claude), academic/research, or simple scripts. OpenClaw democratized access to persistent, autonomous AI agents.

## The [[clawhavoc-security-crisis]] (2026)

In February-March 2026, OpenClaw experienced a catastrophic security crisis:
- **341 malicious skills** discovered on ClawHub (supply chain attack)
- **138 CVEs** logged against OpenClaw
- **Zero-click exploits** — no user interaction required for some attacks
- **API key exposure** and **remote code execution**
- Coverage by Ars Technica, Mashable, and multiple cybersecurity outlets

This eroded community trust severely. As one analysis noted: "OpenClaw Hit 250K GitHub Stars — Then 20% of Its Skills Were Found Malicious."

## Migration to Hermes

Following the security crisis, many users migrated to [[hermes-agent]]:
- Hermes added dedicated migration tools: `hermes claw migrate` command
- Migration guides proliferated (lushbinary.com, official Hermes docs)
- Comprehensive migration coverage: sessions, cron, memory, skills, API keys

Reasons for migration: security concerns, security fatigue (constant CVEs), Hermes as better alternative, Nous Research backing, active development velocity.

## Current State (2026)

- Active but damaged — continues development but security issues persist
- Security patches ongoing — regular CVE fixes
- Community divided — some stay, many migrated
- ClawHub reformed — new security measures for skill validation
- Competitive pressure from Hermes Agent and others

## Strengths
- **Developer-first design** — evolved from developer needs, strong terminal integration
- **Massive skill ecosystem** — 1200+ skills on ClawHub
- **ACP protocol** — pioneered IDE-agent integration
- **Dreaming feature** — background memory consolidation
- **Academic research skills** — OpenAlex API integration, paper search
- **Enterprise features** — agent council, cost monitoring, audit trails

## See Also
- [[steve-tigue]] -- creator
- [[hermes-agent]] -- successor/successor framework, learned from OpenClaw's architecture
- [[clawhavoc-security-crisis]] -- security incident that drove migration
- [[nous-research]] -- organization behind Hermes
- [[llm-wiki-pattern]] -- LLM wiki pattern as parallel knowledge system
- [[harness-engineering]] -- discipline of designing environments for coding agents
- [[openclaw-vs-hermes]] -- Detailed comparison: ecosystem approach and memory architecture as real differentiators
