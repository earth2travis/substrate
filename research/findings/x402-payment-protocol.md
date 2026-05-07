---
title: x402 Payment Protocol
source: research/raw/x402-payment-protocol.md
tags:
- payments
- protocol
- http
- agents
- crypto
related:
- agent-platform-ecosystem
- agent-native-operations
- agent-payment-infrastructure
- protocol-as-coordination
---



# x402 Payment Protocol

x402 activates the long-dormant HTTP 402 ("Payment Required") status code to enable programmatic, per-request payments between any HTTP client and server. No accounts, no API keys, no subscriptions.

**Creator:** Coinbase (open source, Apache 2.0)
**Stats:** 75M+ transactions, $24M+ volume, 94K+ buyers, 22K+ sellers

## The Problem

Internet payments are broken for the agentic era. The current stack requires account creation, KYC, prepaid credits, and API key management for every provider. An AI agent calling 50 different APIs cannot create 50 accounts and manage 50 API keys.

x402 reduces this to: agent sends HTTP request, gets 402 with payment details, signs a stablecoin transaction, retries with payment proof in header, receives resource. Two HTTP round trips. No accounts anywhere.

## How It Works

**Three actors:**
- **Client (buyer)**: Any HTTP client with a crypto wallet. Constructs and signs payment payloads.
- **Resource Server (seller)**: Any HTTP service that wants to charge. Integrates payment middleware in one line of code.
- **Facilitator**: Optional intermediary handling verification and on-chain settlement. Non-custodial.

**Three HTTP headers carry the entire protocol:**
- `PAYMENT-REQUIRED` (server → client): amount, token, destination address
- `PAYMENT-SIGNATURE` (client → server): signed payment payload
- `PAYMENT-RESPONSE` (server → client): settlement confirmation

## Schemes

- **`exact`**: Transfer a specific amount. Live for EVM chains and Solana.
- **`upto`**: Transfer up to a maximum, based on actual resource consumption.

## Design Principles

- Open standard (Apache 2.0)
- HTTP/transport-native
- Network and currency agnostic
- Backwards compatible
- Trust-minimizing (facilitators cannot move funds except per client intention)
- Easy to use (10x better than existing payment methods)

## Limitations

1. Stablecoin dependency (primarily USDC)
2. Gas costs and finality even on L2s
3. Client wallet requirement
4. Facilitator centralization risk
5. Fiat support is aspirational, not implemented

## Relationship to ERC-8004

x402 handles the payment rail. ERC-8004 handles discovery, trust, and reputation. The protocols were designed to work together: x402 provides the economic action; ERC-8004 provides the context and trust signals.
