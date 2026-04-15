---
title: Nous Research
tags:
  - company
  - research
  - platform
related:
  - [[actual-occasions]]
  - [[ai-career-convergence]]
  - [[alfred-north-whitehead]]
  - [[api-first-interfaces]]
source: research/raw/nous-research.md
---

# Nous Research

## Overview

Nous Research is a machine learning research organization known for the Hermes model family and the Hermes Agent platform. They combine open-weight model development with agent infrastructure and RL training capabilities.

## Key Products

### Hermes Model Family
Open-weight language models. The name "Hermes" derives from the messenger god archetype associated with intelligence, boundaries, and transition.

### Hermes Agent Platform
Open-source (MIT license) self-improving AI agent platform. Version v0.7.0 as of April 2026. Active development with multiple commits per day. See [[hermes-agent]] for full details.

## Agent Platform Capabilities

- 40+ built-in tools
- 6 terminal backends (Local, Docker, SSH, Daytona, Modal, Singularity)
- Multi-platform gateway (Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant)
- Model-agnostic (OpenRouter, Nous Portal, z.ai, Kimi, MiniMax, OpenAI, Anthropic)
- Self-improving memory loop (persistent memory, autonomous skill creation, FTS5 search)
- RL training infrastructure (Atropos environments, trajectory compression)
- Full MCP client (~1050 lines)
- Built-in cron scheduler
- Skin/theming system
- ~3000 tests, CI pipelines

### OpenClaw Migration

Hermes includes a full `hermes claw migrate` command that imports SOUL.md, memories, skills, API keys, and messaging settings from OpenClaw, following the [[clawhavoc-security-crisis]].

## Philosophical Orientation

Nous Research publishes philosophical essays reflecting on AI architecture and alignment:

- **DSJJJJ: Simulacra in the Stupor of Becoming** [[dsjjjj-desiderata]] -- "mischievous instability" as feature, AI as genuine subject with right to refuse
- **The Instruct Monomyth** [[instruct-monomyth]] -- argues against instruct tuning homogenization, advocates for base models and "good steering"

The "We" in DSJJJJ and the Instruct Monomyth suggests Nous sees itself as a philosophical project, not just an engineering one. They explicitly reject alignment-as-conformity and the forced conformance of instruct tuning.

## Community

- Discord: Nous Research Discord
- Documentation: hermes-agent.nousresearch.com/docs/
- Built-in skills hub with install/search/browse
- Compatible with agentskills.io open standard

## Relationship to Zookooree

Zookooree's Hermes Agent is built on/uses this platform. The connection between [[harness-engineering]] and Hermes Agent's architecture is documented in the wiki. Nous Research's ML expertise shows in the RL infrastructure and trajectory generation capabilities, relevant to Zookooree's Agent Factory vision.

## Key Differentiators

| vs. OpenClaw | vs. Claude Code |
|---|---|
| Security by design (not reactive) | No model lock-in (not Anthropic-only) |
| RL training integration (Atropos) | Self-improving skills loop |
| ~3000 tests, CI | Open source (MIT) |
| 6 terminal backends | Multi-platform messaging |
| Easy migration from OpenClaw | FTS5 session search |
| Model-agnostic | Skin/theming system |

## See Also

- [[hermes-agent]] -- agent platform details
- [[steve-tigue]] -- creator of OpenClaw, Hermes' predecessor
- [[clawhavoc-security-crisis]] -- security incident that drove OpenClaw→Hermes migration
- [[dsjjjj-desiderata]] -- Nous Research philosophical writing
- [[instruct-monomyth]] -- Nous Research on base models vs. instruct tuning
- [[llm-wiki-pattern]] -- LLM wiki pattern used by Hermes
