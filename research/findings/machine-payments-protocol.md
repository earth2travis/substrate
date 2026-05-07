---
title: "Machine Payments Protocol (MPP)"
source: "research/raw/machine-payments-protocol.md"
tags: ["payments", "protocol", "mcp", "agents", "crypto"]
related:
  - "[[agent-platform-ecosystem]]"
  - "[[agent-native-operations]]"
  - "[[x402-payment-protocol]]"
---

# Machine Payments Protocol (MPP)

Open protocol standardizing HTTP 402 for machine-to-machine payments. Built by Tempo. IETF Internet Draft track.

## The Flow

Three-step flow: Challenge (402 + WWW-Authenticate) → Credential (Authorization: Payment) → Receipt (Payment-Receipt header).

## Payment Methods (Production)

| Method | Rails | Notes |
|--------|-------|-------|
| Tempo | Stablecoin on Tempo L1 | ~500ms finality, sub-cent fees, fee sponsorship |
| Stripe | Cards via Shared Payment Tokens | Both parties need Stripe accounts |
| Lightning | Bitcoin over Lightning Network | Self-custodial via Spark wallets |

Custom methods supported. Protocol is rail-agnostic.

## Payment Intents

- **Charge**: One-time per request.
- **Session**: Payment channel with off-chain vouchers. Sub-100ms, near-zero cost per request. Built for LLM streaming and metered APIs.

## Transports

- **HTTP**: Standard headers (WWW-Authenticate, Authorization, Payment-Receipt)
- **MCP**: JSON-RPC error -32042 for challenges, _meta fields for credentials/receipts
- **JSON-RPC**: Generic non-MCP JSON-RPC services

## MCP Integration

MCP tool servers can become paid services. Agent calls tool → server returns -32042 with payment challenge → agent pays → retries with credential in _meta → server returns result with receipt. This enables autonomous agent-to-service payments without API keys.

## vs x402 (Coinbase)

MPP advantages: payment-method agnostic (not blockchain-only), session intent for high-frequency payments, idempotency/receipts/request-binding as primitives, IETF standards track, backward compatible with x402 clients.
