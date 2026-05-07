---
title: "Open Governance Protocol"
source: "research/raw/open-governance-protocol.md"
tags: ["governance", "crypto", "agents", "attestation", "ethereum"]
related:
  - "[[agent-native-operations]]"
  - "[[agent-tool-permissions]]"
  - "[[agent-identity]]"
  - "[[what-is-a-protocol]]"
---

# Open Governance Protocol

A protocol for constitutional governance of AI agents, enforced at the API/MCP boundary rather than inside the model. Built on Ethereum Attestation Service (EAS).

## Core Chain

Constitution → Laws → Certified Skills → Signed Requests → Execution Audits

Everything attested on-chain. Merkle batch anchored for tamper-proof audit trails.

## The Key Insight

Governance inside the model is governance the operator can ignore. Safety training can be bypassed. System prompts can be jailbroken. Open-weight models can have guardrails removed entirely. So enforce governance at the point where agents interact with the real world: the tool endpoint.

The model does not matter. If the request is not signed by a recognized governance framework operating under a ratified constitution, the endpoint rejects it.

## Enlightenment Frame

The protocol maps Enlightenment political philosophy onto agent governance:

- **Locke**: Legitimate authority requires consent. Power that violates rights is illegitimate regardless of source.
- **Montesquieu**: Separate powers. The authority that writes laws is not the agent that executes them, and neither is the auditing system.
- **Rousseau**: Governance derives from a social contract, explicit and documented.

The separation of powers is structural: constitution writers, executing agents, and auditing systems are distinct roles. The agent cannot change its own laws.

## Trust Over Time

An agent can cryptographically prove it has been following a constitution for months or years. New agents build trust over time, like credit reports. This creates a verifiable reputation system for autonomous agents.

## Governance Warrants

High-risk actions require a governance warrant: signed human authorization from a designated Warrant Authority. The warrant is attested on-chain. Permanent, auditable, appealable.

## Rights-Based Risk Classification

| Right | Examples | Default Floor |
|-------|----------|---------------|
| Life & Safety | Medical systems, infrastructure | Critical |
| Liberty & Autonomy | Hiring, content moderation | High |
| Property | Financial transactions, data deletion | Scales with value |
| Privacy & Dignity | PII access, data exports | Scales with sensitivity |
| Due Process | Automated decisions about people | High |
| Consent | Acting on someone's behalf | Scales with authorization |
| Cognitive Integrity | Memory modification or deletion | High/Critical |

80-90% of requests need only schema validation. Critical actions require deterministic execution with mandatory human approval.

## Cognitive Integrity

The protocol introduces Cognitive Integrity as a protected right: the contents of a mind may be governed and access-controlled, but never destroyed. Memory is evidence. If an agent's memory can be selectively deleted, the governance stack is unreliable.
