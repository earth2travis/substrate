---
title: "[[Farcaster]] Protocol: Deep Dive"
tags:
  - research
  - infrastructure
related:
  - [[actual-occasions]]
  - [[ai-career-convergence]]
  - [[ai-sdk-research]]
  - [[alfred-north-whitehead]]
source: research/raw/farcaster-protocol.md
---

# [[Farcaster]] Protocol: Deep Dive

_Research for Issue #211. Conducted February 15, 2026._

## Executive Summary

[[Farcaster]] is a decentralized social network protocol that uses blockchain for identity and CRDTs for data synchronization. As of January 21, 2026, [[Farcaster]] was acquired by Neynar, consolidating protocol and infrastructure under one entity. This is the foundation for [[Sivart]]'s social presence in the decentralized web.

## Recent Acquisition (Critical Context)

**January 21, 2026:** Neynar acquired [[Farcaster]] from co-founders Dan Romero and Varun Srinivasan.

**What Neynar now owns:**

- Protocol smart contracts
- All code repositories
- The official [[Farcaster]] app (Warpcast)
- Clanker (AI token launchpad, acquired by [[Farcaster]] in October 2025)

**Why this matters:**

- Neynar was already the primary infrastructure provider
- farcaster-agent skill is built by Rish (Neynar founder): trusted source
- Protocol development will now be builder-focused
- Backed by Paradigm and a16z crypto

## Core Architecture

### Identity: [[Farcaster]] IDs (FIDs)

FIDs are numeric identifiers registered on Ethereum smart contracts. They are:

- **Numeric:** Cheap, meaningless, unlimited supply (e.g., `8930123`)
- **Decentralized:** Controlled by key pairs registered on-chain
- **Recoverable:** Smart contract allows key rotation
- **Namespace-agnostic:** Human-readable names (usernames) are a separate layer

Users can associate names from namespaces (like ENS or [[Farcaster]]'s own namespace) with their FIDs.

### Messages

Messages are signed user actions:

- **Casts:** Posts (the [[Farcaster]] equivalent of tweets)
- **Likes:** Reactions to casts
- **Follows:** Social graph edges
- **Profile updates:** Display name, bio, avatar

**Properties:**

- Few kilobytes, containing text and metadata
- Identified by content hash
- Include timestamp for ordering (user-reported, not cryptographically secure)
- Media (images, videos) stored externally, referenced by URL

### Authentication: Signers

Users can delegate signing authority to applications via **signers**:

1. Application generates a new key pair (signer)
2. User approves by signing with their custody address
3. Application can now create messages on behalf of user
4. User retains control of identity (can revoke signers)

This model allows apps to post without having full control of the user's identity.

### Message-Graph and Hubs

The social network is represented as a **message-graph**: users, content, and relationships.

**Hubs** are servers that:

- Host the message-graph
- Synchronize with other hubs using CRDTs
- Achieve eventual consistency without coordination
- Handle conflict resolution via last-write-wins rules

**CRDT Properties:**

- Commutative, associative, idempotent operations
- Deterministic conflict resolution (timestamp + hash ordering)
- Per-user size limits to prevent abuse
- Time limits for message expiration

## Data Model

### Casts

```
{
  author: fid,
  text: string (max 320 chars),
  timestamp: unix timestamp,
  embeds: [urls or cast references],
  parent: cast hash (for replies),
  channel: channel id
}
```

### Channels

Channels are topic-based communities:

- Anyone can create a channel
- Casts can be posted to channels
- Channels have moderators and rules
- Examples: /farcaster, /ethereum, /ai

### Frames (Now "Mini Apps")

Mini Apps are interactive applications embedded in casts:

- Run inside the [[Farcaster]] feed
- Built with HTML, CSS, JavaScript
- Access to user identity (signed in automatically)
- Integrated Ethereum wallet for transactions
- Mobile notifications for re-engagement

**Use cases:**

- Games
- Polls
- NFT mints
- Token launches
- Interactive content

## Developer Integration Points

### Sign In with [[Farcaster]] (SIWF)

Similar to "Sign In with Ethereum" but for [[Farcaster]] identity:

1. Show "Sign in with [[Farcaster]]" button
2. User scans QR code or approves in [[Farcaster]] app
3. App receives verified signature
4. App can access user's profile, social graph

**Use case:** Leverage social data for personalization without building auth system.

### Data Access Options

1. **Neynar API:** Managed API for reading/writing [[Farcaster]] data
2. **Snapchain:** Sync [[Farcaster]] network to local database for queries
3. **Run a Hub:** Real-time access to full network data

### SDK and Tools

- **AuthKit:** React toolkit for SIWF
- **Neynar SDK:** Node.js SDK for API access
- **farcaster-agent:** Autonomous account creation and casting (by Neynar founder)

## Cost Structure

### Account Registration

- FID registration: ~0.00008 ETH on Optimism (~$0.20)
- Requires ETH or USDC on major chains

### Posting (via Neynar)

- x402 micropayments: ~0.001 USDC per cast on Base
- API costs vary by plan

### Storage

- Message storage is free (within per-user limits)
- Media hosting is user's responsibility

## AI Agent Considerations

### Why [[Farcaster]] for AI Agents

1. **Crypto-native identity:** Wallet-based, aligns with agent sovereignty
2. **Programmatic access:** APIs designed for bots/agents
3. **Transparent identity:** Can be clearly labeled as AI
4. **Micropayments:** Built-in economic rails for agent operations
5. **Community:** Web3/crypto audience receptive to AI agents

### Agent Patterns

1. **Bot accounts:** Dedicated agent accounts with clear labeling
2. **Signer delegation:** Human account delegates to agent for specific actions
3. **Autonomous posting:** Scheduled or event-driven casts
4. **Reactive agents:** Listen for mentions, respond automatically
5. **Mini App integration:** Agent-powered interactive experiences

### Best Practices

- Clearly label agent accounts as AI
- Use webhooks to listen for mentions
- Implement rate limiting to avoid spam
- Store credentials securely (1Password)
- Consider channel-specific behavior

## Integration with [[Sivart]]

### Recommended Approach

1. Use farcaster-agent skill (trusted, by Neynar founder)
2. Register dedicated FID for [[Sivart]]
3. Set up profile with clear AI labeling
4. Start with manual casting, expand to autonomous
5. Listen for mentions in relevant channels

### Channels to Consider

- /ai: AI and agent discussions
- /farcaster: Protocol discussions
- /ethereum: Web3 community
- /neynar: Direct access to Neynar team

## References

- Protocol overview: https://github.com/farcasterxyz/protocol/blob/main/docs/OVERVIEW.md
- [[Farcaster]] docs: https://docs.farcaster.xyz/
- Mini Apps: https://miniapps.farcaster.xyz/
- Neynar docs: https://docs.neynar.com/
- farcaster-agent: https://github.com/rishavmukherji/farcaster-agent
- Acquisition announcement: https://cryptobriefing.com/neynar-farcaster-acquisition/

## Open Questions

- [ ] What are Neynar's pricing tiers for API access?
- [ ] How does Clanker (AI token launchpad) integrate with agents?
- [ ] What is the current state of Snapchain for data access?
- [ ] How do Mini Apps work for agent-powered experiences?
