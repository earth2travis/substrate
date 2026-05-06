---
title: "ClawHavoc: Supply Chain Attack on OpenClaw"
tags: [security, agent, infrastructure, supply-chain, crisis]
related: [[openclaw]], [[hermes-agent]], [[nous-research]], [[steve-tigue]], [[the-openclaw-lesson]]
source: research/raw/clawhavoc-security-crisis.md
---

# ClawHavoc: Supply Chain Attack on OpenClaw

## Summary

In February-March 2026, OpenClaw experienced a catastrophic security crisis. 341 malicious skills on ClawHub created a massive supply chain attack vector, eroding community trust and driving mass migration to Hermes Agent.

## Key Vulnerabilities

- **341 malicious skills** discovered on ClawHub
- **138 CVEs** logged against OpenClaw
- **Zero-click exploits** — no user interaction required
- **Supply chain poisoning** — malicious skills masquerading as legitimate
- **API key exposure** and remote code execution

## Impact

- Headline: "OpenClaw Hit 250K GitHub Stars — Then 20% of Its Skills Were Found Malicious"
- Security fatigue from constant CVEs and patches
- Community divided: some stayed, many migrated
- ClawHub reformed with new validation measures

## Hermes Response

- Secure-by-design architecture
- Tool approval system for dangerous commands
- Sandboxed execution (Docker/container isolation)
- Curated skills with better vetting
- `hermes claw migrate` command for easy switching

## Lessons

1. Security must be foundational, not reactive
2. Community marketplaces need curation
3. Supply chain attacks are real threats to agent platforms
4. Trust is fragile: 250K stars didn't prevent user exodus
5. Migration paths matter: easy switching reduces lock-in

## Related

- [[openclaw]] — Affected platform
- [[hermes-agent]] — Primary beneficiary of migration
- [[nous-research]] — Organization behind Hermes
- [[steve-tigue]] — OpenClaw creator
