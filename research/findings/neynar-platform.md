---
title: "Neynar Platform: Farcaster Infrastructure Provider"
tags: [farcaster, infrastructure, api, social, agent, platform]
related: [[farcaster-protocol]], [[clanker-event-driven-architecture]], [[clanker-agent-deployment-patterns]], [[nous-research]], [[the-openclaw-lesson]], [[decentralized-social]]
source: research/raw/neynar-platform.md
---

# Neynar Platform: Farcaster Infrastructure Provider

## Summary

Neynar is the infrastructure platform for Farcaster, now owning the entire protocol stack after acquiring Farcaster in January 2026. Founded by Rish (rishavmukherji), Neynar provides APIs, hubs, and developer tools that power most Farcaster applications. Backed by Paradigm and a16z crypto.

## Key Claims

**Acquisition of Farcaster (January 21, 2026).** Neynar acquired from Farcaster co-founders Dan Romero and Varun Srinivasan: protocol smart contracts, all code repositories, Farcaster app (Warpcast), Clanker (AI token launchpad), and developer coordination.

**Six platform capabilities:** Social data integration (user identities, social graphs, cast history), Mini Apps (Frames) infrastructure with validation and analytics, AI agent support with contextual awareness and webhook-based event listeners, client building tools, on-chain data mapping with real-time streams, and data analysis with SQL playground.

**API-first design.** All API calls require an API key in the header (`x-api-key`). Core endpoints include publish cast, agent account creation via developer portal, and webhooks for mentions.

**Three integration patterns for AI agents:** Portal-created agent (simplest, Neynar handles registration), farcaster-agent skill (complete autonomy, self-custody), and Sign In with Neynar (user delegation, not for agent identity).

**Pricing model.** Agent account creation incurs protocol fee (paid by Neynar on behalf). API calls based on plan tier. x402 micropayments (~0.001 USDC per cast on Base).

## Security Considerations

- Never expose API keys in client code
- Use environment variables for secrets
- Store signer_uuid securely
- Rotate API keys periodically

## Connection to Agent Factories

Neynar's platform is the social ingestion layer for agent factories. The webhook-based mention system, agent account creation, and real-time data streams are exactly what's needed for agents to participate in decentralized social networks. The x402 micropayment protocol enables agent-to-agent economic transactions.

## Related

- [[farcaster-protocol]] — Decentralized social protocol
- [[clanker-event-driven-architecture]] — Event-driven agent architecture on Farcaster
- [[clanker-agent-deployment-patterns]] — Deployment patterns
- [[nous-research]] — Organization with philosophical alignment
- [[the-openclaw-lesson]] — Security as foundation for agent platforms
- [[x402-payment-protocol]] — Micropayments for agent transactions
