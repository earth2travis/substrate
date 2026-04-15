# x402: The Payment Protocol for the Agentic Internet

_Deep dive into the open standard for HTTP-native micropayments._

---

## Summary

x402 activates the long-dormant HTTP 402 ("Payment Required") status code to enable programmatic, per-request payments between any HTTP client and server. No accounts, no API keys, no subscriptions. A server says "pay me," a client pays, and the resource is served. The entire exchange happens within standard HTTP headers.

**Creator:** Coinbase (open source, Apache 2.0)
**Status:** Live in production
**Stats:** 75M+ transactions, $24M+ volume, 94K+ buyers, 22K+ sellers
**SDKs:** TypeScript, Python, Go
**GitHub:** [coinbase/x402](https://github.com/coinbase/x402)
**Docs:** [docs.x402.org](https://docs.x402.org)

## The Problem It Solves

Internet payments are fundamentally broken for the agentic era. The current stack requires:

1. **Account creation** with every API provider
2. **KYC and payment method attachment** (delays, approvals, human involvement)
3. **Prepaid credits or subscriptions** (overpay or run out)
4. **API key management** (security risk, rotation overhead)
5. **Settlement through legacy rails** (slow, expensive, chargebacks, minimum transaction amounts)

This model assumes a human on both sides. An AI agent that needs to call 50 different APIs to complete a task cannot create 50 accounts, attach 50 payment methods, and manage 50 API keys. The friction kills the use case.

x402 reduces this to: agent sends HTTP request, gets a 402 response with payment details, signs a stablecoin transaction, retries with payment proof in the header, receives the resource. Two HTTP round trips. No accounts anywhere.

## How It Works

### The Flow

```
Client                    Server                   Facilitator        Blockchain
  │                         │                          │                  │
  │──GET /weather──────────>│                          │                  │
  │                         │                          │                  │
  │<──402 Payment Required──│                          │                  │
  │   (PAYMENT-REQUIRED     │                          │                  │
  │    header: amount,      │                          │                  │
  │    token, address)      │                          │                  │
  │                         │                          │                  │
  │──GET /weather───────────>                          │                  │
  │   (PAYMENT-SIGNATURE    │                          │                  │
  │    header: signed       │                          │                  │
  │    payment payload)     │                          │                  │
  │                         │──verify(payload)────────>│                  │
  │                         │<──valid──────────────────│                  │
  │                         │                          │                  │
  │                         │   [serves resource]      │                  │
  │                         │                          │                  │
  │<──200 OK────────────────│                          │                  │
  │   (PAYMENT-RESPONSE     │                          │                  │
  │    header: settlement)  │──settle(payload)────────>│                  │
  │                         │                          │──submit tx──────>│
  │                         │                          │<──confirmed──────│
  │                         │<──settlement receipt─────│                  │
```

### Three Actors

**Client (buyer):** Any HTTP client, human or agent. Holds a crypto wallet. Constructs and signs payment payloads based on the server's requirements. Needs no accounts, credentials, or prior relationship with the server.

**Resource Server (seller):** Any HTTP service that wants to charge for access. Integrates payment middleware (literally one line of code in Express, Hono, or Next.js). Doesn't need to understand blockchain details.

**Facilitator:** An optional but recommended intermediary that handles payment verification and on-chain settlement. The facilitator never holds funds or acts as custodian. It verifies signatures, submits transactions, and monitors confirmations. This is the key abstraction: sellers don't need blockchain nodes, RPC connections, or settlement logic. Multiple facilitators operate in production across various networks.

### Payment Communication

Two HTTP headers carry the entire payment protocol:

- **`PAYMENT-REQUIRED`** (server to client): Base64-encoded JSON containing payment requirements (amount, token, destination address, network, scheme)
- **`PAYMENT-SIGNATURE`** (client to server): Base64-encoded signed payment payload proving the client has authorized the transfer
- **`PAYMENT-RESPONSE`** (server to client): Base64-encoded settlement confirmation returned with the successful response

Everything is standard HTTP. No WebSocket connections, no custom protocols, no out-of-band communication.

### Schemes

A "scheme" is a logical way of moving money. The abstraction exists because different use cases require different payment mechanics, and different blockchains implement those mechanics differently.

**`exact` (shipping now):** Transfer a specific amount. Example: pay $1 to read an article. This is the first scheme, implemented for EVM chains and Solana.

**`upto` (theoretical):** Transfer up to a maximum, based on actual resource consumption. Example: pay up to $5 for LLM token generation, settle the actual cost afterward.

Each scheme has network-specific implementations because submitting a transaction on Ethereum is fundamentally different from submitting one on Solana. The (scheme, network) pair defines the concrete payment flow.

### Supported Networks and Tokens

Production support includes:

- **EVM chains:** Base, Ethereum, Polygon, Avalanche, Arbitrum, and others
- **Solana**
- **Tokens:** USDC is the primary stablecoin; the standard is token-agnostic

The architecture is designed to accommodate fiat networks as well, though crypto-native payments are the priority and will never be deprioritized in favor of fiat.

## Integration Complexity

This is where x402 makes its strongest argument. The developer experience is remarkably simple.

### Seller (server-side)

```javascript
// Express middleware: one line per protected route
app.use(
  paymentMiddleware({
    "GET /weather": {
      accepts: [{ network: "base", token: "USDC", amount: "0.01" }],
      description: "Weather data",
    },
  }),
);
```

That's the entire integration. The middleware handles: responding with 402 when no payment is present, extracting and forwarding the payment payload to a facilitator, verifying the response, and passing through to the route handler on success.

### Buyer (client-side)

```javascript
// Wrap fetch with x402 payment handling
import { x402Fetch } from "@x402/fetch";

const response = await x402Fetch("https://api.example.com/weather", {
  wallet: myWallet,
});
```

The client wrapper automatically handles: detecting 402 responses, parsing payment requirements, constructing and signing the payment payload, and retrying the request with the payment header.

### SDK Availability

- **TypeScript:** `@x402/core`, `@x402/evm`, `@x402/svm`, `@x402/fetch`, `@x402/axios`, `@x402/express`, `@x402/hono`, `@x402/next`, `@x402/paywall`, `@x402/extensions`
- **Python:** `x402`
- **Go:** `github.com/coinbase/x402/go`

## Design Principles

**Open standard.** Apache 2.0 license. Will never force reliance on a single party. Anyone can build facilitators, clients, or server middleware.

**HTTP/transport-native.** No additional communication required beyond standard HTTP request/response cycles. Payment piggybacks on the existing data flow.

**Network and currency agnostic.** Contributions for new networks (crypto and fiat) are welcome. The standard will never deprecate support for existing networks.

**Backwards compatible.** No breaking changes to existing network support unless required for security.

**Trust-minimizing.** Facilitators cannot move funds except in accordance with client intentions. The payment payload is a signed authorization, not a custody transfer.

**Easy to use.** The explicit goal is 10x better than existing payment methods. Abstracts gas, RPC, and blockchain details away from both client and server.

## The HTTP 402 Connection

HTTP 402 ("Payment Required") was reserved in the HTTP/1.1 specification (RFC 7231) for "future use." It was defined in the early 1990s as a placeholder for internet-native payments that never materialized because the payment infrastructure didn't exist yet.

Three decades later, the infrastructure exists. Stablecoins provide the value transfer. Smart contracts provide the settlement. x402 provides the protocol that connects them to the existing web.

The choice to build on a reserved HTTP status code rather than inventing a new protocol is significant. It means x402 is compatible with every HTTP server, every reverse proxy, every load balancer, every CDN, and every monitoring tool. It's not fighting the web. It's completing a piece of the web that was always meant to exist.

## Production Traction

The numbers are notable for a protocol still in its early ecosystem phase:

- **75.41M transactions**
- **$24.24M volume**
- **94.06K buyers**
- **22K sellers**

Multiple facilitators are live, supporting various networks. The ecosystem includes client-side integrations, service endpoints, infrastructure tooling, and community resources.

## Limitations and Open Questions

1. **Stablecoin dependency.** While token-agnostic in theory, practical usage centers on USDC. Stablecoin regulatory risk (freezing, blacklisting) is a systemic concern that x402 inherits but cannot mitigate at the protocol level.

2. **Gas costs and finality.** Even on L2s, gas costs and confirmation times are nonzero. The trade-off between settlement speed and payment guarantee is acknowledged but not fully resolved. The `scheme` abstraction allows for future optimizations.

3. **Client wallet requirement.** Buyers need a funded crypto wallet. For human users, this is still a friction point. For AI agents with programmatic wallets, it's less of an issue.

4. **Facilitator centralization risk.** While facilitators are non-custodial, reliance on a small number of production facilitators creates a practical centralization concern. The protocol is designed for anyone to run a facilitator, but ecosystem diversity takes time.

5. **Roadmap is empty.** The ROADMAP.md currently says "update coming soon." This suggests either active development that hasn't been publicly documented or a project in transition.

6. **Fiat support is aspirational.** The principles state fiat networks may be supported, but no fiat scheme exists yet. Pure crypto limits the addressable market.

## Relationship to ERC-8004

x402 handles the payment rail. ERC-8004 handles everything around it:

- **Discovery:** How does a client find a server that offers the service it needs? (ERC-8004's Identity Registry)
- **Trust:** Should the client pay this server? Is it reliable? (ERC-8004's Reputation and Validation Registries)
- **Payment:** The actual value transfer. (x402)
- **Feedback loop:** Did the payment result in good service? (ERC-8004's reputation system, enriched by x402 proof of payment)

The protocols were designed to work together. x402 provides the economic action; ERC-8004 provides the context and trust signals that make that economic action rational.

## Source

[Documentation](https://docs.x402.org) | [GitHub](https://github.com/coinbase/x402) | [Website](https://x402.org)

---

_Part of the [Agent Economy Infrastructure](./overview.md) research._
