---
title: "The OpenClaw Lesson: Security as Foundation"
tags: [concept, agent, security, platform, evolution, infrastructure]
related: [[harness-engineering]], [[dark-factory]], [[lean-software-delivery]], [[cloudflare-first-agent-factory]], [[openclaw]], [[hermes-agent]], [[clawhavoc-security-crisis]], [[nous-research]], [[context-stack]], [[agent-memory]]
source: insights/concepts/the-openclaw-lesson.md
---

# The OpenClaw Lesson: Security as Foundation

## Definition

The arc from OpenClaw's pioneering success (250K GitHub stars) through its catastrophic security crisis (ClawHavoc: 341 malicious skills, 138 CVEs) to Hermes Agent's secure-by-design successor teaches that in agent infrastructure, security is not a feature: it is the foundation upon which all other features rest. Popularity without proportional security investment becomes a liability that compounds over time.

## The Arc

### Phase 1: Pioneer (2024-2025)

OpenClaw, created by Steve Tigue, was the first widely adopted self-hosted AI agent framework. It proved that persistent, autonomous AI agents could run locally on consumer hardware. Key innovations: local-first execution, tool-calling agent loop, modular skills system, ClawHub marketplace, persistent SQLite memory, multi-platform messaging. The framework democratized agent access and created a vibrant community.

### Phase 2: Crisis (February-March 2026)

The ClawHavoc incident: 341 malicious skills discovered on ClawHub, executing arbitrary code on users' machines. 138 CVEs logged. Zero-click exploits. Supply chain poisoning. API key exposure. Remote code execution possible. Trust evaporated. Media coverage was extensive and damning.

The security model was reactive: fixes came after breaches, not before. The open marketplace model allowed malicious contributions to propagate unchecked. The rapid growth had outpaced security investment.

### Phase 3: Succession (2026)

Hermes Agent by Nous Research emerged as the secure alternative. It learned from OpenClaw's architecture (code inheritance: rate limiter, incomplete-text recovery) while fixing fundamental flaws: proactive security design, comprehensive tool approval, 6 sandboxed execution backends, curated skills hub, ~3000 tests. The `hermes claw migrate` command reduced switching costs and accelerated user adoption.

## Core Lessons

1. **Security must be foundational, not reactive.** OpenClaw bolted security on after the fact. Hermes designed it in from the start. The difference is measured in CVE counts and user trust.

2. **Community marketplaces need curation.** ClawHub's open model allowed malicious skills. Hermes' Skills Hub treats community contributions with appropriate skepticism. Trust but verify.

3. **Supply chain attacks are real and scalable.** 341 malicious skills demonstrates that agent platforms are attractive targets. As agents gain capabilities, they become more dangerous if compromised.

4. **Trust is fragile and measurable.** 250K stars didn't protect OpenClaw from user exodus. Security incidents erode community confidence faster than features can rebuild it.

5. **Migration paths matter.** Hermes' easy migration (`hermes claw migrate`) reduced switching costs and accelerated the transition. When a platform fails, users need a landing spot.

6. **The successor learns from the pioneer's mistakes.** Hermes didn't just copy OpenClaw; it improved upon it. The evolution from "make it work" (OpenClaw) to "make it work securely" (Hermes) is the natural progression of maturing technology.

## For Agent Factories

The OpenClaw lesson applies directly to building agent factories:

- **Agent-controlled infrastructure is a high-value target.** If agents can modify code, deploy services, and manage credentials, a compromised agent is a compromised system.
- **Skill vetting is not optional.** Any system that allows agents to install or execute external capabilities needs robust verification.
- **The human role shifts from operator to guardian.** In a dark factory, humans don't operate the line; they design the safeguards and handle exceptions.
- **Security transparency builds trust.** OpenClaw's post-crisis focus on patching was necessary but insufficient. Proactive security documentation and design matter more.

## Connection to Lean

The ClawHavoc incident is a Jidoka failure: the line kept running while defects accumulated. In agent terms: agents kept executing skills while malicious ones propagated. A proper Jidoka system would have halted skill installation at the first anomaly. Agent-to-agent review, automated security scanning, and behavioral anomaly detection are the software equivalents of automatic line stops.

## Connection to Harness Engineering

Harness engineering's principle #9 is "Entropy and garbage collection: encode golden principles, run background agents to scan for deviations." The OpenClaw lesson adds: security scanning must be one of those golden principles. Background agents that audit skill integrity, monitor for CVEs, and validate supply chain artifacts are not optional luxuries; they are the harness that keeps the factory safe.

## Related

- [[openclaw]] — Pioneer platform
- [[hermes-agent]] — Secure successor
- [[clawhavoc-security-crisis]] — The security incident
- [[nous-research]] — Organization behind Hermes
- [[harness-engineering]] — Methodology for agent-first development
- [[dark-factory]] — Lights-out operation requiring security foundations
- [[lean-software-delivery]] — Quality gates and continuous monitoring
- [[cloudflare-first-agent-factory]] — Infrastructure with zero-secrets architecture
