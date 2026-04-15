---
title: Machine Payments Protocol (MPP)
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/machine-payments-protocol.md
---

# Machine Payments Protocol (MPP)

**Source:** https://mpp.dev
**Spec:** https://paymentauth.org (IETF Internet Draft)
**SDK:** `mppx` (TypeScript)
**Built by:** Tempo (tempoxyz)
**Date researched:** 2026-03-19

## What It Is

Open protocol standardizing HTTP 402 for machine-to-machine payments. Three-step flow: Challenge (402 + WWW-Authenticate) → Credential (Authorization: Payment) → Receipt (Payment-Receipt header).

## Payment Methods (Production)

| Method | Rails | Notes |
|--------|-------|-------|
| Tempo | Stablecoin on Tempo L1 | ~500ms finality, sub-cent fees, fee sponsorship |
| Stripe | Cards via Shared Payment Tokens | Both parties need Stripe accounts |
| Lightning | Bitcoin over Lightning Network | Self-custodial via Spark wallets |

Custom methods supported. Protocol is rail-agnostic.

## Payment Intents

- **Charge**: One-time per request. Simple.
- **Session**: Payment channel with off-chain vouchers. Sub-100ms, near-zero cost per request. Built for LLM streaming, metered APIs.

## Transports

- **HTTP**: Standard headers (WWW-Authenticate, Authorization, Payment-Receipt)
- **MCP**: JSON-RPC error -32042 for challenges, _meta fields for credentials/receipts
- **JSON-RPC**: Generic non-MCP JSON-RPC services

## MCP Integration

MCP tool servers can become paid services. Agent calls tool → server returns -32042 with payment challenge → agent pays → retries with credential in _meta → server returns result with receipt. This enables autonomous agent-to-service payments without API keys.

## vs x402 (Coinbase)

MPP advantages: payment-method agnostic (not blockchain-only), session intent for high-frequency payments, idempotency/receipts/request-binding as primitives, IETF standards track, backward compatible with x402 clients.

## SDK (mppx)

TypeScript. Middleware for Next.js, Hono, Elysia, Express. ~5 lines to gate an endpoint. Client SDK handles 402 loop automatically.

## Relevance to Synthweave

1. **Consumer**: Loom agents pay for third-party services (LLM, search, image gen) without API keys
2. **Provider**: Synthweave services accept MPP payments, instantly accessible to any agent with a wallet
3. **MCP native**: Fits directly into MCP tool architecture we're already building toward

## Key Links

- Docs: https://mpp.dev
- IETF Specs: https://paymentauth.org
- GitHub: https://github.com/tempoxyz/mpp
- Tempo blockchain: https://docs.tempo.xyz
- Stripe MPP docs: https://docs.stripe.com/payments/machine/mpp
- Tempo Wallet CLI: https://wallet.tempo.xyz
