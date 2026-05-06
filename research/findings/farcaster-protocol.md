---
title: "Farcaster: Decentralized Social Protocol"
tags: [social, infrastructure, crypto, protocol, identity]
related: [[nous-research]], [[hermes-agent]], [[neynar-platform]], [[decentralized-social]]
source: research/raw/farcaster-protocol.md
---

# Farcaster: Decentralized Social Protocol

## Summary

Farcaster is a decentralized social network protocol using blockchain for identity and CRDTs for data synchronization. Acquired by Neynar in January 2026, consolidating protocol and infrastructure under one entity.

## Core Architecture

- **Identity**: Farcaster IDs (FIDs) — numeric, on-chain, recoverable
- **Messages**: Signed user actions (casts, likes, follows, profile updates)
- **Authentication**: Signers — delegated signing authority for apps
- **Hubs**: Servers hosting the message-graph, synchronizing via CRDTs
- **Mini Apps**: Interactive HTML/CSS/JS applications embedded in casts

## AI Agent Integration

- Crypto-native identity aligns with agent sovereignty
- Programmatic APIs designed for bots and agents
- Micropayments built-in for agent operations
- Signer delegation: human account delegates to agent for specific actions

## Cost Structure

- FID registration: ~$0.20 on Optimism
- Posting: ~0.001 USDC per cast via Neynar
- Storage: free within per-user limits

## Current State

Neynar acquired Farcaster (January 2026), gaining protocol smart contracts, code repos, Warpcast app, and Clanker token launchpad. Protocol development is now builder-focused, backed by Paradigm and a16z crypto.

## Related

- [[nous-research]] — Organization behind Hermes Agent
- [[hermes-agent]] — Can integrate with Farcaster for social operations
