---
title: "Agent Payment Infrastructure"
tags: ["payments", "agents", "crypto", "mcp", "infrastructure"]
related:
  - "[[agent-platform-ecosystem]]"
  - "[[agent-native-operations]]"
  - "[[agent-tool-permissions]]"
  - "[[protocol-as-coordination]]"
---

# Agent Payment Infrastructure

The current internet payment stack is built for humans: accounts, KYC, credit cards, subscriptions, API keys. An agent that needs to call 50 APIs cannot create 50 accounts and manage 50 API keys. The friction kills the use case.

Agent payment infrastructure solves this by making payments as protocol-native as HTTP itself.

## The Core Pattern

1. Agent sends HTTP request
2. Server returns 402 (Payment Required) with payment requirements
3. Agent signs transaction from its wallet
4. Agent retries with payment proof in header
5. Server serves the resource

Two HTTP round trips. No accounts anywhere. The entire exchange happens within standard HTTP headers.

## Two Competing Approaches

**x402 (Coinbase)**: Activates HTTP 402 with stablecoin payments. Apache 2.0, 75M+ transactions, $24M+ volume. Network-agnostic but crypto-native. Facilitator model handles verification and settlement without custody.

**MPP (Machine Payments Protocol)**: IETF standards track. Rail-agnostic (supports Stripe, Lightning, not just stablecoins). Session intents for high-frequency payments. MCP-native integration via JSON-RPC error codes.

## MCP Integration

MCP tool servers can become paid services. The protocol error code carries the payment challenge. The agent wallet handles the credential. This enables autonomous agent-to-service payments without API keys.

## Open Questions

- Stablecoin dependency and regulatory risk
- Gas costs and finality even on L2s
- Facilitator centralization
- Fiat support still aspirational
- Chicken-and-egg: MCP vendors need to check payments, but they won't until there's volume

The missing piece is not the payment rail. It is the trust and reputation layer that makes paying a stranger rational.
