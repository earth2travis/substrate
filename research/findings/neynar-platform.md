---
title: "Neynar Platform: Deep Dive"
tags:
  - research
  - infrastructure
related:
  - [[2026-02-10-ai-career-convergence]]
  - [[actual-occasions]]
  - [[ai-sdk-research]]
  - [[alfred-north-whitehead]]
source: research/raw/neynar-platform.md
---

# Neynar Platform: Deep Dive

_Research for Issue #212. Conducted February 15, 2026._

## Executive Summary

Neynar is the infrastructure platform for [[Farcaster]], now owning the entire protocol stack after acquiring [[Farcaster]] in January 2026. Founded by Rish (rishavmukherji), Neynar provides APIs, hubs, and developer tools that power most [[Farcaster]] applications. Backed by Paradigm and a16z crypto.

## Company Overview

### Leadership

- **Founder:** Rish (rishavmukherji on GitHub)
- **Background:** Early [[Farcaster]] builder, infrastructure focused
- **Created:** farcaster-agent skill for autonomous account management

### Funding

- Backed by Paradigm and a16z crypto
- Raised capital to scale infrastructure post-acquisition

### Acquisition (January 21, 2026)

Neynar acquired from [[Farcaster]] co-founders Dan Romero and Varun Srinivasan:

- Protocol smart contracts
- All code repositories
- [[Farcaster]] app (Warpcast)
- Clanker (AI token launchpad)
- Developer coordination

## Platform Capabilities

### 1. Social Data Integration

Connect [[Farcaster]] social graphs and user profiles to apps:

- User identities and profiles
- Social graphs (follows, followers)
- Cast history and engagement
- Channel memberships

### 2. Mini Apps (Frames) Infrastructure

- Validate and host [[Farcaster]] frames
- Real-time analytics
- Push notifications
- Frame development tools

### 3. AI Agent Support

Deploy agents with:

- Contextual awareness (social data access)
- Automated real-time interactions
- Webhook-based event listeners
- Agent account creation via developer portal

### 4. Client Building

Build [[Farcaster]] clients with:

- Seamless user onboarding
- Rich profile data
- Social graphs and feeds
- Scalable, reliable infrastructure

### 5. On-chain Data Mapping

- Real-time [[Farcaster]] data streams
- Indexed databases
- Analytics tools
- Holder/token correlation

### 6. Data Analysis and Ingestion

- SQL playground for [[Farcaster]] data queries
- Data export capabilities
- Custom analytics

## API Reference

### Authentication

All API calls require an API key in the header:

```
x-api-key: <your-api-key>
```

### Core Endpoints

#### Publish a Cast

```bash
curl --request POST \
  --url https://api.neynar.com/v2/farcaster/cast/ \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
    "signer_uuid": "19d0c5fd-9b33-4a48-a0e2-bc7b0555baec",
    "text": "Hello from [[Sivart]]!",
    "channel_id": "neynar"
  }'
```

**Parameters:**

- `signer_uuid`: UUID of approved signer (must match API key)
- `text`: Cast content (max 320 chars)
- `embeds`: Optional URLs or cast references (max 2)
- `parent`: Parent cast hash for replies
- `channel_id`: Target channel
- `idem`: Idempotency key for deduplication

**Response:**

```json
{
  "success": true,
  "cast": {
    "hash": "0x71d5225f77e0164388b1d4c120825f3a2c1f131c",
    "author": { "fid": 3 },
    "text": "Hello from [[Sivart]]!"
  }
}
```

### Agent Account Creation

The Neynar developer portal allows creating agent accounts directly:

1. Go to dev.neynar.com
2. Click into your app
3. Click "Create Agent"
4. Receive `signer_uuid` for the agent
5. Use signer to cast via API

**Note:** Agent creation has per-developer limits. Avoid creating test agents excessively.

### Webhooks for Mentions

Listen for @mentions and replies:

1. Set up webhook endpoint in Neynar dashboard
2. Receive real-time notifications when agent is mentioned
3. Process and respond automatically

Reference: `/docs/listen-for-bot-mentions`

## SDKs

### Node.js SDK

Official SDK with typed responses:

- Package: `@neynar/nodejs-sdk`
- Method example: `publishCast()`
- Better developer experience than raw API

### Example App

Clone the starter repo for quick setup:

```
https://github.com/manan19/example-farcaster-app
```

Includes:

- Sign in with [[Farcaster]]
- Write capabilities
- Signer management

## Pricing

_Note: Specific pricing tiers need verification from Neynar dashboard_

**Known costs:**

- Agent account creation: Protocol fee (paid by Neynar on your behalf)
- API calls: Based on plan tier
- x402 micropayments: ~0.001 USDC per cast on Base

**Plans likely include:**

- Free tier with rate limits
- Paid tiers with higher limits
- Enterprise options

## Integration Patterns for AI Agents

### Pattern 1: Portal-Created Agent

1. Create agent in Neynar dev portal
2. Get signer_uuid
3. Cast via API using signer
4. Listen for mentions via webhook

**Pros:** Simplest setup, Neynar handles registration
**Cons:** Limited number of agents per account

### Pattern 2: farcaster-agent Skill

1. Use farcaster-agent skill
2. Register FID autonomously
3. Set up signer
4. Full control over account

**Pros:** Complete autonomy, self-custody
**Cons:** Requires wallet funding, more complex

### Pattern 3: Sign In with Neynar (SIWN)

1. User connects existing [[Farcaster]] account
2. App gets write access via delegated signer
3. Post on behalf of user

**Pros:** Leverage existing user base
**Cons:** Not for agent identity, for user delegation

## Best Practices

### Security

- Never expose API keys in client code
- Use environment variables for secrets
- Store signer_uuid securely
- Rotate API keys periodically

### Rate Limiting

- Implement exponential backoff
- Use idempotency keys for retries
- Monitor usage against plan limits
- Cache responses where appropriate

### Agent Behavior

- Clear AI labeling in profile
- Respect channel norms
- Avoid spam patterns
- Respond helpfully to mentions
- Monitor for abuse

### Credentials Management

For [[Sivart]]:

- Store API key in 1Password
- Store signer_uuid in 1Password
- Use environment injection for runtime
- Document in TOOLS.md

## Integration with [[Sivart]]

### Recommended Setup

1. **Create Neynar account** at dev.neynar.com
2. **Create app** in developer portal
3. **Use farcaster-agent skill** for autonomous FID registration
4. **Store credentials** in 1Password Operations vault
5. **Configure webhooks** for mention handling
6. **Start casting** with clear AI identity

### 1Password Entries Needed

- `Neynar` (Login): dev portal credentials
- `Neynar API Key` (API Credential): app API key
- `[[Farcaster]] [[Sivart]]` (Secure Note): FID, signer_uuid, profile info

### TOOLS.md Section

```markdown
### [[Farcaster]] / Neynar

- **Platform:** [[Farcaster]] (decentralized social)
- **Infrastructure:** Neynar (API, hubs)
- **Account:** @sivart (FID: TBD)
- **API:** Neynar v2
- **Credentials:** 1Password Operations vault
```

## References

- Neynar docs: https://docs.neynar.com/
- API reference: https://docs.neynar.com/reference/
- Developer portal: https://dev.neynar.com
- Node.js SDK: https://docs.neynar.com/nodejs-sdk/
- Example app: https://github.com/manan19/example-farcaster-app
- farcaster-agent: https://github.com/rishavmukherji/farcaster-agent

## Open Questions

- [ ] What are exact pricing tiers?
- [ ] How many agents per developer account?
- [ ] Webhook reliability and latency?
- [ ] Best channels for AI agents to participate?
- [ ] Clanker integration opportunities?
