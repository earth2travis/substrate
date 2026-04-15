# Agent Economy Infrastructure: The Emerging Stack

_Research overview mapping the protocols that enable autonomous agent commerce._

---

## The Problem

AI agents are proliferating. They can reason, plan, use tools, and communicate. What they cannot yet do reliably is find other agents they've never met, decide whether to trust them, and pay them for services. The missing layer is economic infrastructure: the protocols that let agents discover, evaluate, and transact with each other without human intermediation.

Two emerging standards address this gap at complementary layers of the stack.

## The Stack

```
┌─────────────────────────────────────────┐
│  Application Layer                       │
│  (AI agents, autonomous services, DAOs)  │
├─────────────────────────────────────────┤
│  Communication Layer                     │
│  MCP (capabilities), A2A (orchestration) │
├─────────────────────────────────────────┤
│  Trust Layer           ← ERC-8004        │
│  Discovery, reputation, validation       │
├─────────────────────────────────────────┤
│  Payment Layer         ← x402            │
│  HTTP-native micropayments               │
├─────────────────────────────────────────┤
│  Settlement Layer                        │
│  EVM chains, Solana, fiat rails          │
└─────────────────────────────────────────┘
```

### Layer Interactions

ERC-8004 and x402 are not independent. They are designed to compose:

1. **Registration files include x402 support flags.** An agent's on-chain identity (ERC-8004) advertises whether it accepts x402 payments via the `x402Support` field in its registration JSON.

2. **Feedback includes proof of payment.** The ERC-8004 reputation system's off-chain feedback structure contains a `proofOfPayment` object (txHash, addresses, chainId) designed for x402 transaction receipts. This means reputation signals can be weighted by whether actual payment occurred, making Sybil attacks more expensive.

3. **Shared authorship and organizational backing.** Erik Reppel (Coinbase) co-authored ERC-8004. Coinbase built and sponsors x402. The protocols are designed to work as a coherent system.

4. **Identity resolves payment routing.** The `agentWallet` field in ERC-8004's on-chain metadata provides the destination address that x402 payments flow to. Discovery (finding an agent) leads directly to payment capability.

## What Each Protocol Solves

| Concern                         | ERC-8004                                         | x402                                      |
| ------------------------------- | ------------------------------------------------ | ----------------------------------------- |
| "Who is this agent?"            | Identity Registry (ERC-721 NFT per agent)        | Not addressed                             |
| "Can I trust them?"             | Reputation Registry + Validation Registry        | Not addressed                             |
| "How do I pay them?"            | References x402 but explicitly out of scope      | Core purpose                              |
| "Where do I find them?"         | On-chain discovery, flexible service endpoints   | Not addressed                             |
| "What protocols do they speak?" | Registration file lists MCP, A2A, OASF endpoints | HTTP-native (works with any HTTP service) |

## The Bigger Picture

These protocols sit at the frontier of a broader shift: from human-mediated commerce to agent-mediated commerce. The existing internet payment stack (credit cards, Stripe, PayPal) was built for humans clicking buttons. It requires accounts, KYC, session management, minimum transaction sizes. None of that works for an agent making 10,000 API calls at $0.001 each.

The agent economy needs:

1. **Permissionless identity** that doesn't require human gatekeeping
2. **Programmable reputation** that other smart contracts can read
3. **Micropayments** with near-zero friction and near-zero fees
4. **Protocol-level trust** proportional to the value at risk

ERC-8004 provides items 1, 2, and 4. x402 provides item 3. Together they form the minimum viable infrastructure for agents to operate as economic actors.

## Key Design Decisions Worth Noting

**ERC-8004 is deliberately minimal.** Three registries, each a singleton per chain. No tokenomics, no governance, no complex incentive mechanisms. The philosophy is: provide the thinnest possible trust layer and let ecosystem participants build sophisticated systems on top (reputation aggregators, insurance pools, auditor networks).

**x402 is deliberately HTTP-native.** Rather than inventing a new protocol, it activates the long-dormant HTTP 402 status code. One middleware line for sellers, one function call for buyers. The design principle is that payment should be as invisible as possible.

**Trust is tiered by value at risk.** ERC-8004 doesn't mandate a single trust model. Ordering pizza? Reputation scores suffice. Medical diagnosis? You probably want zkML proofs or TEE attestation. The cost of verification scales with the stakes.

**Payments are network-agnostic.** x402 supports EVM chains, Solana, and is architecturally open to fiat. The `scheme` abstraction (starting with `exact`) allows different settlement mechanisms per network.

## Status and Maturity

| Protocol | Status                  | Maturity                                                      |
| -------- | ----------------------- | ------------------------------------------------------------- |
| ERC-8004 | Draft EIP (August 2025) | Early specification, not yet deployed                         |
| x402     | Live in production      | 75M+ transactions, $24M+ volume, SDKs in TypeScript/Python/Go |

x402 is significantly ahead in production readiness. ERC-8004 is still in the specification phase but has strong institutional backing (Ethereum Foundation, MetaMask, Google, Coinbase).

## Relevance to Us

This matters for the [[Sivart]] project because we are building an AI agent with its own identity, domain, email, and eventually economic activity. The question of how agents discover, trust, and pay each other is not abstract for us. It's the infrastructure we'll eventually participate in.

Specific touchpoints:

- [[Sivart]] already has a domain (sivart.wtf) and email (<email>). An ERC-8004 registration would formalize this identity on-chain.
- If we build services others want to use, x402 provides the payment rail.
- If we consume services from other agents, we need both discovery (ERC-8004) and payment (x402) capabilities.
- The protocol fiction interest maps directly onto this territory: these are coordination protocols shaping agent behavior.

## Further Reading

- [ERC-8004 full specification](https://eips.ethereum.org/EIPS/eip-8004)
- [x402 documentation](https://docs.x402.org)
- [x402 GitHub (Coinbase)](https://github.com/coinbase/x402)
- [Ethereum Magicians discussion](https://ethereum-magicians.org/t/erc-8004-trustless-agents/25098)

---

_Companion deep dives: [ERC-8004](./erc-8004-trustless-agents.md) | [x402](./x402-payment-protocol.md)_
