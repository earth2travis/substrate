---
title: "OpenClaw: Rise, Crisis, and Migration to Hermes"
tags: [agent, platform, security, history, tooling]
related: [[hermes-agent]], [[clawhavoc-security-crisis]], [[steve-tigue]], [[nous-research]]
source: research/raw/openclaw.md
---

# OpenClaw: Rise, Crisis, and Migration to Hermes

## Summary

OpenClaw was the pioneering open-source, self-hosted AI agent framework created by Steve Tigue. It reached 250K GitHub stars and democratized access to persistent autonomous agents. A catastrophic security crisis in early 2026 drove mass migration to Hermes Agent.

## Core Architecture

- Local-first execution on user machines
- Tool-calling agent loop with persistent memory
- Modular skills system (1200+ on ClawHub)
- ACP protocol for IDE-agent integration
- Multiple messaging platform support

## The ClawHavoc Security Crisis (February–March 2026)

- **341 malicious skills** discovered on ClawHub (supply chain attack)
- **138 CVEs** logged against OpenClaw
- **Zero-click exploits** — no user interaction required
- **API key exposure** and remote code execution

Community trust eroded severely. Headline: "OpenClaw Hit 250K GitHub Stars — Then 20% of Its Skills Were Found Malicious."

## Migration to Hermes

Hermes added dedicated migration tools (`hermes claw migrate`). Migration guides proliferated covering sessions, cron jobs, memory, skills, and API keys.

**Reasons for migration**: Security concerns, security fatigue, Hermes as better alternative, Nous Research backing, active development velocity.

## Current State (2026)

- Active but damaged — development continues, security issues persist
- ClawHub reformed with new skill validation measures
- Community divided: some stay, many migrated
- Competitive pressure from Hermes Agent and others

## Lesson

Ecosystem scale without security governance is a liability. OpenClaw's skill marketplace was its greatest asset and its fatal vulnerability. Hermes learned from this: the substrate model keeps knowledge in version-controlled markdown, not executable skills from unknown sources.

## Related

- [[hermes-agent]] — Successor framework
- [[clawhavoc-security-crisis]] — Detailed security analysis
- [[nous-research]] — Organization behind Hermes
- [[steve-tigue]] — Creator of OpenClaw
