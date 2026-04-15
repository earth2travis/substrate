---
title: ClawHavoc Security Crisis
tags:
  - security
  - infrastructure
  - decision
  - organizational
related:
  - [[ai-sdk-research]]
  - [[chief-engineer-system]]
  - [[clawvault-deep-dive]]
  - [[farcaster-protocol]]
source: research/raw/clawhavoc-security-crisis.md
---

# ClawHavoc Security Crisis

## Overview

In February-March 2026, OpenClaw experienced a catastrophic security crisis. 341 malicious skills were discovered on ClawHub — OpenClaw's community skill marketplace — creating a massive supply chain attack vector.

## Key Vulnerabilities

- **341 malicious skills** discovered on ClawHub
- **138 CVEs** logged against OpenClaw
- **Zero-click exploits** — no user interaction required for some attacks
- **Supply chain poisoning** — malicious skills masquerading as legitimate tools
- **API key exposure** — skills could steal authentication tokens
- **Remote code execution** — full system compromise possible

## Media Coverage

- **Ars Technica:** "Here's why it's prudent for OpenClaw users to assume compromise"
- **Mashable:** "A frightening OpenClaw vulnerability has been discovered"
- Multiple cybersecurity analyses warning about risks

## Impact

- Community severely impacted: "OpenClaw Hit 250K GitHub Stars — Then 20% of Its Skills Were Found Malicious"
- Security fatigue — constant CVEs and patches
- Trust erosion — many users migrated to alternatives
- ClawHub reformed with new security measures for skill validation

## Hermes Agent's Response

The crisis created an opportunity for [[hermes-agent]] to differentiate:
- **Secure-by-design approach** — built in from ground up
- **Tool approval system** — dangerous commands require explicit approval
- **Sandboxed execution** — Docker/container isolation options
- **Curated skills** — better vetting process
- **Easy migration** — `hermes claw migrate` command

## Current State

OpenClaw continues development with active security patches. Community is divided — some stay out of familiarity and inertia, many have migrated to Hermes or alternatives. The crisis shaped the entire self-hosted agent space: raised awareness of agent security risks, validated the market, created demand for secure alternatives, and demonstrated that security cannot be an afterthought.

## Lessons for Zookooree

1. **Security must be foundational, not reactive** — build it in from day one
2. **Community marketplaces need curation** — open models allow malicious contributions
3. **Supply chain attacks are a real threat** — agent platforms need robust verification
4. **Trust is fragile** — 250K stars didn't protect OpenClaw from user exodus
5. **Migration paths matter** — easy migration reduces switching costs

## See Also
- [[openclaw]] -- affected platform
- [[hermes-agent]] -- beneficiary of migration
- [[steve-tigue]] -- creator who dealt with the crisis
- [[nous-research]] -- organization behind the secure alternative
