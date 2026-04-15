---
title: "ERC-8004: Trustless Agents"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/erc-8004-trustless-agents.md
---

# ERC-8004: Trustless Agents

_Deep dive into the Ethereum standard for agent discovery, reputation, and validation._

---

## Summary

ERC-8004 proposes three on-chain registries that together solve the trust problem for autonomous agents operating across organizational boundaries. It provides the infrastructure for agents to find each other, build reputations, and verify each other's work, without requiring pre-existing relationships or centralized intermediaries.

**Authors:** Marco De Rossi (MetaMask), Davide Crapis (Ethereum Foundation), Jordan Ellis (Google), Erik Reppel (Coinbase)
**Status:** Draft EIP (created August 13, 2025)
**Requires:** EIP-155, EIP-712, EIP-721, EIP-1271
**Discussion:** [Ethereum Magicians](https://ethereum-magicians.org/t/erc-8004-trustless-agents/25098)

## The Problem It Solves

Agent communication protocols already exist. MCP lets agents advertise capabilities (tools, prompts, resources). A2A handles authentication, skill advertisement, messaging, and task orchestration. But neither addresses the fundamental question: _how does an agent find and trust another agent it has never interacted with before?_

Without a trust layer, agent economies devolve into walled gardens where every agent only interacts with agents pre-approved by its operator. That doesn't scale. ERC-8004 provides the open alternative.

## Architecture: Three Registries

### 1. Identity Registry

The foundation layer. Each agent gets an ERC-721 NFT (a non-fungible token) that serves as its on-chain identifier. This is not a profile picture. It's a portable, censorship-resistant identity that resolves to a rich registration file.

**Key properties:**

- `agentId`: incrementally assigned tokenId (the NFT)
- `agentRegistry`: globally unique identifier formatted as `{namespace}:{chainId}:{contractAddress}` (e.g., `eip155:1:0x742...`)
- `agentURI`: resolves to a JSON registration file (can be IPFS, HTTPS, or fully on-chain via base64 data URI)
- `agentWallet`: reserved on-chain metadata key for the agent's payment receiving address; requires cryptographic proof of wallet control to set

**The registration file** is where things get interesting. It's a flexible JSON structure that advertises:

- Service endpoints (A2A, MCP, OASF, web, email, ENS, DID)
- x402 payment support
- Active status
- Cross-chain registrations
- Supported trust models

This design is intentionally protocol-agnostic. An agent can list MCP endpoints, A2A agent cards, ENS names, DIDs, wallet addresses on any chain, and email addresses all in one registration. As new agent communication protocols emerge, they can be added as additional service entries without modifying the standard.

**Domain verification** is optional but available: agents can prove they control an endpoint domain by publishing a `.well-known/agent-registration.json` file that references their on-chain agentId.

**On-chain metadata** extends beyond the registration file. The registry supports arbitrary key-value metadata via `getMetadata`/`setMetadata`, with `agentWallet` as a reserved key that requires cryptographic proof of control (EIP-712 for EOAs, ERC-1271 for smart contract wallets). When an agent NFT is transferred, the wallet is automatically cleared, forcing re-verification by the new owner.

### 2. Reputation Registry

A standard interface for publishing and consuming feedback signals about agents. The design is deliberately minimal: it provides the data structure and storage, while leaving scoring algorithms and aggregation to ecosystem builders.

**Feedback structure:**

- `value` (int128): signed fixed-point score
- `valueDecimals` (uint8, 0-18): decimal precision
- `tag1`, `tag2`: optional categorization strings
- `endpoint`: which specific endpoint is being rated
- `feedbackURI`: link to off-chain detailed feedback (recommended: IPFS)
- `feedbackHash`: keccak256 of the off-chain file for integrity verification

**What gets stored on-chain vs off-chain:**

- On-chain: value, valueDecimals, tag1, tag2, isRevoked status, feedbackIndex
- Emitted but not stored: endpoint, feedbackURI, feedbackHash
- Off-chain file: full context including MCP tool names, A2A task IDs, proof of payment (x402 transaction receipts)

This split is smart. On-chain storage is expensive, but having the core signal values on-chain enables composability: other smart contracts can read reputation data directly. The detailed context lives off-chain where storage is cheap, with integrity guaranteed by content hashing.

**Anti-gaming measures:**

- Feedback submitters cannot be the agent owner or an approved operator (prevents self-rating)
- The `getSummary` function requires specifying which `clientAddresses` to aggregate over, forcing callers to curate their reviewer set rather than blindly trusting all feedback (mitigates Sybil attacks)
- Revocation is supported (clients can retract feedback)
- Response appending lets anyone (the agent, third-party auditors) attach context to feedback entries

**The protocol explicitly expects ecosystem development** around reputation: specialized scoring services, auditor networks, insurance pools, reviewer reputation systems. The on-chain layer provides the data; interpretation is delegated to the market.

### 3. Validation Registry

Enables agents to request independent verification of their work. This is the "prove it" layer.

**How it works:**

1. An agent submits a validation request to a specific validator contract, providing a `requestURI` (pointing to inputs, outputs, and all data needed for verification) and a `requestHash` commitment.
2. The validator processes the request (off-chain or on-chain, depending on the validation method).
3. The validator responds with a score (0-100), optional evidence URI, and optional tag.

**Validation methods are pluggable:**

- **Crypto-economic:** Stakers re-execute the agent's work and are slashed for incorrect validation
- **zkML:** Zero-knowledge proofs that the agent's model produced the claimed output
- **TEE attestation:** Trusted execution environment oracles verify the computation happened in a secure enclave
- **Trusted judges:** Human or algorithmic arbiters

The response scale (0-100) supports both binary judgments (0 = fail, 100 = pass) and nuanced assessments. Multiple responses per request are allowed, enabling progressive validation states (e.g., "soft finality" then "hard finality").

Incentives and slashing are explicitly out of scope, delegated to the specific validation protocol being used.

## Design Philosophy

**Minimal viable trust.** The registries do the least possible work on-chain. They store identity, signals, and validation records. Everything else (scoring algorithms, aggregation, interpretation, economic incentives) is pushed to ecosystem participants. This keeps gas costs low and the standard flexible.

**Trust proportional to stakes.** The three-tier system (reputation, validation, TEE) lets developers match the trust mechanism to the value at risk. Reputation is cheap and sufficient for low-stakes interactions. Validation (zkML, re-execution) is expensive but provides cryptographic guarantees for high-value work.

**Protocol-agnostic integration.** The registration file accommodates MCP, A2A, OASF, ENS, DIDs, and arbitrary service endpoints. As the agent protocol landscape evolves, ERC-8004 adapts by adding entries, not by changing the standard.

**Singletons per chain.** Designed for one deployment per chain (L1 or L2), avoiding fragmentation. An agent registered on one chain can operate on any chain, with cross-chain registrations linked in the registration file.

## Open Questions and Limitations

1. **Sybil resistance is partially delegated to the ecosystem.** The protocol provides tools (reviewer filtering, proof of payment in feedback) but cannot fully prevent coordinated fake feedback. Real defense requires reputation systems around reviewers themselves, which the protocol anticipates but doesn't implement.

2. **The standard is in draft.** No deployed contracts yet. The specification may change based on community feedback.

3. **Gas costs for feedback.** On-chain storage of feedback values is useful for composability but creates an economic barrier. EIP-7702 (gas sponsorship) is referenced as a mitigation, but the economics of high-volume feedback on mainnet are untested.

4. **Validator incentive design is out of scope.** This is intentional (separation of concerns) but means the validation layer's security depends entirely on external incentive mechanisms that don't exist yet as standards.

5. **No mandatory capabilities verification.** The standard ensures the registration file corresponds to the on-chain agent, but cannot cryptographically guarantee that advertised capabilities are functional or non-malicious. This is acknowledged in the security considerations.

## Relationship to x402

ERC-8004 explicitly treats payments as "orthogonal" and out of scope. But it was designed with x402 integration in mind:

- The registration file's `x402Support` boolean advertises payment capability
- The off-chain feedback file includes a `proofOfPayment` structure designed for x402 transactions
- The `agentWallet` on-chain metadata provides the payment destination
- Both protocols share a Coinbase co-author

The practical implication: an agent using ERC-8004 for discovery and reputation can seamlessly accept x402 payments, and those payment receipts feed back into the reputation system, creating a virtuous cycle where economic activity strengthens trust signals.

## Source

[Full specification](https://eips.ethereum.org/EIPS/eip-8004) | [Discussion](https://ethereum-magicians.org/t/erc-8004-trustless-agents/25098)

---

_Part of the [Agent Economy Infrastructure](./overview.md) research._
