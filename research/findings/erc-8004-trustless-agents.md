---
title: "ERC-8004: Trustless Agents"
tags: [finding, ethereum, erc-8004, agent-economy, trust, identity]
related: [[agent-native-operations]], [[agent-identity]], [[skills-as-portable-knowledge]]
source: research/raw/erc-8004-trustless-agents.md
ingested: 2026-05-07
---

# ERC-8004: Trustless Agents

An Ethereum standard proposing three on-chain registries for agent discovery, reputation, and validation. Enables agents to find each other, build reputations, and verify work without pre-existing relationships or centralized intermediaries.

## Key Points

**The problem.** MCP lets agents advertise capabilities. A2A handles authentication and messaging. But neither addresses: how does an agent find and trust another agent it has never interacted with? Without a trust layer, agent economies devolve into walled gardens.

**Three registries.**

1. **Identity Registry.** Each agent gets an ERC-721 NFT as on-chain identifier. Resolves to a JSON registration file advertising service endpoints (MCP, A2A, OASF, web, email, ENS, DID), x402 payment support, active status, cross-chain registrations, supported trust models. Protocol-agnostic: new protocols added as entries without modifying the standard. Domain verification via `.well-known/agent-registration.json`. On-chain metadata with arbitrary key-value pairs.

2. **Reputation Registry.** Standard interface for publishing and consuming feedback signals. Feedback structure: signed fixed-point score, decimal precision, optional tags, endpoint rated, off-chain detailed feedback (IPFS recommended) with integrity hash. Anti-gaming: submitters cannot be agent owner, `getSummary` requires specifying reviewer set, revocation supported, response appending allowed. On-chain stores core signals for composability; detailed context lives off-chain.

3. **Validation Registry.** Independent verification of agent work. Agent submits request with inputs/outputs; validator responds with score (0-100), evidence, tag. Pluggable methods: crypto-economic (stakers re-execute), zkML (zero-knowledge proofs), TEE attestation (secure enclave), trusted judges. Multiple responses per request enable progressive finality.

**Design philosophy.** Minimal viable trust on-chain: identity, signals, validation records. Everything else (scoring, aggregation, interpretation, incentives) pushed to ecosystem. Trust proportional to stakes: reputation for low-stakes, validation for high-value work.

**Relationship to x402.** Payments treated as orthogonal but designed for integration. Registration file advertises x402Support; feedback includes proofOfPayment; agentWallet provides payment destination. Economic activity strengthens trust signals.

**Open questions.** Sybil resistance partially delegated. Gas costs for feedback untested. Validator incentives out of scope. No mandatory capabilities verification. Standard is draft.

## Relevance

ERC-8004 is the infrastructure layer for the agent economy thesis. Skills-as-portable-knowledge becomes skills-as-verifiable-NFTs. Agent identity becomes on-chain and portable.

## Related

- [[agent-native-operations]] -- Agent identity and permissions
- [[agent-identity]] -- Values, trust, and identity documents
- [[skills-as-portable-knowledge]] -- Skills as transferable capabilities
