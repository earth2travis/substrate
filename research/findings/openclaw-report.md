---
title: "OpenClaw Platform: Deep Research Report"
tags: [openclaw, agent, platform, history, security, migration]
related: [[openclaw]], [[hermes-agent]], [[clawhavoc-security-crisis]], [[nous-research]]
source: research/raw/openclaw-report.md
---

# OpenClaw Platform: Deep Research Report

## Summary

A comprehensive cross-session research report on OpenClaw: its creation by Steve Tigue, 250K GitHub star milestone, core architecture (local-first execution, skills system, ClawHub marketplace), the ClawHavoc security crisis (341 malicious skills, 138 CVEs), and the subsequent mass migration to Hermes Agent.

## Key Claims

1. **Pioneering Framework:** OpenClaw was the first widely adopted self-hosted AI agent framework, proving that persistent, autonomous AI agents could run locally on consumer hardware.
2. **Core Architecture:** Local-first execution, tool-calling agent loop, modular skills system, ClawHub marketplace, persistent SQLite memory, and multi-platform messaging (Telegram, Discord).
3. **Security Crisis:** February-March 2026 saw 341 malicious skills on ClawHub, 138 CVEs, zero-click exploits, supply chain poisoning, API key exposure, and remote code execution vulnerabilities.
4. **User Exodus:** Hermes Agent capitalized with secure-by-design approach, tool approval system, sandboxed execution, curated skills, and `hermes claw migrate` for easy switching.
5. **Historical Connection:** Hermes directly learned from OpenClaw (code inheritance: rate limiter, incomplete-text recovery) and built migration tooling to capture the user base.

## Implications

OpenClaw's story is a foundational cautionary tale for the agent ecosystem: popularity without proportional security investment becomes a liability. The rapid migration demonstrates that trust is fragile and users will switch when security fails.

## Related

- [[openclaw]] — Earlier finding on OpenClaw rise and crisis
- [[hermes-agent]] — The platform users migrated to
- [[clawhavoc-security-crisis]] — The security incident details
- [[nous-research]] — Organization behind Hermes
