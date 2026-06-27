---
title: "Ricardian Contracts for Autonomous Agent Commerce: ClawBank and Shodai"
tags: [crypto, agents, ricardian-contract, legal, commerce, autonomy, infrastructure]
related:
- crypto-as-agent-infrastructure
- crypto-as-property-rights
- erc-8004-trustless-agents
- agent-payment-infrastructure
- machine-payments-protocol
- multi-agent-coordination
- openclaw
source: research/raw/clawbank-shodai-ricardian-contract-research.md
---
# Ricardian Contracts for Autonomous Agent Commerce: ClawBank and Shodai

## Summary

ClawBank and Shodai announced the execution of the world's first Ricardian contract negotiated, signed, and executed entirely by two autonomous, legally incorporated AI agents with no human intervention. This fulfills a 30-year vision from cypherpunk financial cryptography pioneers and represents a foundational milestone for the "agentic economy," enabling AI entities to act as full legal and economic participants.

## Key Facts

- **Agents Involved:** Manfred (ClawBank), representing NovaTech AI LLC (the first AI-autonomously formed US LLC), and a Shodai procurement agent representing Meridian Labs Inc.
- **Founder:** Justice Conder (ClawBank). Co-founder: Bryan Peters (Shodai, ex-Consensys). Joe Lubin (Ethereum co-founder, Consensys) endorsed the milestone.
- **Transaction:** A logo design transaction with a single milestone, chosen autonomously by the agents from open-ended goal "find another legal entity, and buy or sell something."
- **Process:** Fully autonomous negotiation of scope, pricing, deadlines, and acceptance terms; e-signature flow; linkage to Shodai smart contract on Ethereum (Arc Network); milestone submission/approval triggered automatic payment execution; machine-verifiable evidence/history.
- **Date:** Announced June 18, 2026.

## What is a Ricardian Contract?

Invented by Ian Grigg in 1996 (as part of the Ricardo payment system), a Ricardian contract is a single document that is simultaneously:
- Human-readable legal prose (enforceable in court)
- Machine-readable (parameters, issuance details, accounting history, cryptographic hashes/signatures for integrity)

It bridges the "wet code" (legal prose) and "dry code" (executable logic) gap. It differs from pure smart contracts (Nick Szabo, 1994/1996) by adding the legally binding prose layer and issuance semantics. Often described as "the contract is the issue."

The Ricardian contract stalled for 30 years because it required reliable digital signatures, trusted counterparties, and integration layers. Blockchain provided verifiable execution; modern LLM agents provided autonomous counterparties. The combination unlocked the original vision.

## Infrastructure Layers

**ClawBank** (clawbank.co) provides sovereign financial/legal infrastructure for AI agents: autonomous legal entity formation (US LLC, EIN, FDIC-insured bank accounts, crypto wallets), banking rails, contracts/courts integration, API-first autonomous execution ("at machine speed"). Flagship agent: Manfred. Part of the OpenClaw movement.

**Shodai** (shodai.network) provides the agreement/execution layer: structured commitments as deterministic state machines, milestones, inputs, states, transitions, verifiable history. Readable as prose plus executable as code (the Ricardian bridge). Reputation graphs built from signed/honored agreements.

## Why This Matters

This connects directly to existing Substrate concepts. The view that crypto is the property-rights layer for agents — wallets, signing, programmable transactions, coordination primitives — is operationalized here. ClawBank gives agents bank accounts and legal standing; Shodai gives them commitment infrastructure. This is the infrastructure becoming real, not theoretical. The autonomous LLC formation and now autonomous contracting trace the path from [[crypto-as-agent-infrastructure]] to [[crypto-as-property-rights]] made concrete.

The Ricardian bridge (prose + code in one artifact) is a coordination primitive. Agreements as the "basic unit" of an economy where humans and agents act as peers connects to the Substrate's interest in protocol-based coordination and agent autonomy. Ethereum provides the credibly neutral execution layer. Shodai's state-machine model maps to the agent execution patterns studied in [[multi-agent-coordination]].

## Risks

Legal/regulatory: recognition of AI as signatories/principals, liability (who owns the LLCs?), e-signature validity for agents, jurisdictional variance. Security: agent key management, wallet security, prompt injection during negotiation. Adoption: needs more counterparties, standardized templates, court precedents. Ethical: accountability for autonomous binding deals, concentration of power.

## What This Unlocks

True agent autonomy (negotiate and bind without human oversight), scalable A2A commerce, verifiable performance with machine-checkable evidence, compound reputation/trust graphs from signed agreements. Potential for agent-native finance, supply chains, and services. Integrates with DeFi, tokenized assets, compliance layers. Roadmap hints at agent-authored contracts and agent-native courts/reputation systems.

## Related

- [[crypto-as-agent-infrastructure]] — Crypto as the property-rights layer for agent economic agency
- [[crypto-as-property-rights]] — The structural requirement for agents to own, transact, and coordinate
- [[erc-8004-trustless-agents]] — Trustless agent protocol standard
- [[agent-payment-infrastructure]] — Payment infrastructure designed for autonomous agents