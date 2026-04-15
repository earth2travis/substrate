---
title: Composio and Auth Management Analysis
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/composio-analysis.md
---

# Composio and Auth Management Analysis

**Date:** 2026-03-17
**Issue:** #419
**Context:** OAuth token expiry incident on 2026-03-12 caused ~2 hours of downtime. Misleading error messages compounded the problem. We need a systematic solution to credential lifecycle management.

## Overview: What Composio Does

Composio is an **AI agent tooling platform** that provides 1000+ pre-built integrations (GitHub, Gmail, Slack, Notion, etc.) with managed authentication. It is not primarily a secret management tool. It is a tool execution layer for AI agents that happens to solve auth as a side effect.

**Core value prop:** Your AI agent gets "meta tools" that can discover, authenticate, and execute actions across hundreds of apps at runtime. Composio handles OAuth flows, token storage, and automatic refresh behind the scenes.

**Architecture:**
- Cloud-hosted platform (composio.dev) with REST API
- SDKs for Python and TypeScript
- Provider packages for OpenAI, Anthropic, LangChain, LlamaIndex, Vercel AI, Google Gemini, CrewAI, Mastra, etc.
- MCP support (works with Claude Desktop, Cursor, etc.)
- Sessions scoped to user IDs with immutable configuration
- "Meta tools" pattern: agent discovers tools at runtime rather than loading all tool definitions upfront

**Open source:** Yes. GitHub repo `ComposioHQ/composio` has ~27K stars. Apache 2.0 license. SDKs are open source. The platform backend is cloud-hosted (not self-hostable without enterprise plan).

**Enterprise:** VPC/on-prem option available at enterprise tier. SOC-2 compliance mentioned for enterprise.

## Auth Lifecycle Management (The Core Question)

This is the critical evaluation for our use case.

### What Composio does well

1. **Automatic OAuth token refresh:** Composio explicitly states: "Composio automatically refreshes OAuth tokens before they expire. You don't need to handle re-authentication or token expiration." Connected accounts stay valid as long as the user doesn't revoke access.

2. **Managed OAuth apps:** For many integrations, Composio provides its own OAuth app credentials so you don't need to register your own. You can also bring your own OAuth credentials for white-labeling or custom scopes.

3. **Connect Links:** Hosted pages where users authorize access. Handles the full OAuth dance (redirects, token exchange, storage).

4. **Per-user credential isolation:** Each user gets their own "connected accounts" with individual credential storage.

### What Composio does NOT solve for us

1. **Not a general secret store.** Composio manages credentials for its own 1000+ supported toolkits. It does not manage arbitrary secrets like Anthropic OAuth tokens, OpenClaw auth-profiles.json entries, or 1Password service account tokens.

2. **No support for our specific pain point.** The 2026-03-12 incident was about an Anthropic Claude Max OAuth token used by OpenClaw's gateway. Composio has no integration for "OpenClaw gateway auth" or "Claude Max subscription token management." These are proprietary/custom auth flows.

3. **Cloud dependency.** Credentials are stored on Composio's servers (unless enterprise VPC). For a 2-person team, this means trusting a third party with all connected account tokens.

4. **Designed for multi-tenant SaaS.** The user_id/session model is built for apps where many end-users each connect their own accounts. We are one team managing our own infrastructure credentials.

5. **No API key rotation.** Composio handles OAuth refresh but does not rotate API keys, PATs, or service account tokens.

6. **No expiry alerting.** No built-in mechanism to notify when credentials are about to expire (for non-OAuth credentials).

## Integration Breadth and SDK

**Supported AI frameworks:** OpenAI, Anthropic, LangChain, LangGraph, LlamaIndex, Vercel AI, Google Gemini, CrewAI, Mastra, Cloudflare Workers AI, AutoGen. Also supports MCP protocol.

**Notable:** No native OpenClaw integration, though there's a community fork (`ComposioHQ/openclaw-composio`).

**Toolkit count:** 1000+ including GitHub, Gmail, Google Calendar, Slack, Notion, Jira, Linear, HubSpot, Salesforce, Stripe, Twilio, Discord, etc.

**SDK quality:** Modern, well-documented. Python and TypeScript. v3 SDK with clean `Composio()` → `session` → `tools` pattern.

## Alternatives Comparison

### Comparison Table

| Feature | Composio | 1Password Connect | Doppler | Infisical | HashiCorp Vault | Native Daemon |
|---|---|---|---|---|---|---|
| **Primary purpose** | AI agent tools + auth | Secret storage/retrieval | Secret management | Secret management | Secret management | Custom solution |
| **OAuth auto-refresh** | ✅ (for supported toolkits) | ❌ | ❌ | ❌ | ✅ (with plugins) | ✅ (must build) |
| **API key rotation** | ❌ | ❌ | ❌ (manual versioning) | ✅ (dynamic secrets) | ✅ (dynamic secrets) | ✅ (must build) |
| **Expiry alerting** | ❌ | ❌ | ❌ | ✅ (cert lifecycle) | ✅ (lease expiry) | ✅ (must build) |
| **Multi-tool distribution** | ✅ (via SDK/MCP) | ✅ (REST API) | ✅ (CLI/API/env injection) | ✅ (CLI/API/K8s) | ✅ (API/agent) | ✅ (must build) |
| **Self-hostable** | Enterprise only | ✅ (Docker) | ❌ (cloud only) | ✅ (open source) | ✅ (open source) | ✅ (by definition) |
| **We already use it** | ❌ | ✅ (1Password Teams) | ❌ | ❌ | ❌ | ❌ |
| **Pricing (our scale)** | Free (20K calls/mo) | Included in Teams | $4/user/mo | Free (self-host) | Free (self-host) | Free (our time) |
| **Complexity** | Medium | Low | Low | Medium | High | Medium |
| **Manages Anthropic OAuth** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Manages GitHub PATs** | Partial (OAuth, not PATs) | Storage only | Storage only | Storage only | ✅ (dynamic) | ✅ (must build) |
| **Manages GCP SA keys** | ❌ | Storage only | Storage only | Storage only | ✅ (GCP secrets engine) | ✅ (must build) |

### Deep Dive on Each Alternative

#### 1Password Connect (Best fit for secret storage layer)

We already pay for 1Password Teams ($10.65/mo). 1Password Connect is a self-hosted REST API server that caches vault data locally. SDKs in Go, Python, JavaScript.

**Strengths:**
- Already in our stack. Zero new vendor.
- Self-hosted Docker container, low latency, works offline after initial sync.
- REST API for programmatic access. Service accounts already configured.
- Unlimited re-requests after initial fetch.

**Weaknesses:**
- No OAuth token refresh. It's a vault, not an auth manager.
- No dynamic secret generation.
- No expiry alerting (it stores what you put in it).
- Doesn't solve the core problem: tokens expire and nobody notices.

**Verdict:** Great secret storage layer. Does not solve lifecycle management.

#### Doppler

Cloud-only secret management platform. Syncs secrets to environments.

**Strengths:** Clean UI, environment-based config, good CI/CD integration.
**Weaknesses:** Cloud-only. No self-hosting. No OAuth refresh. No dynamic secrets. Another vendor to manage. $4/user/mo minimum.
**Verdict:** Overkill for our needs and doesn't solve the core problem.

#### Infisical

Open source secret management. Self-hostable. Certificate lifecycle management.

**Strengths:** Self-hostable, free tier, certificate auto-renewal, audit logs, approval workflows, dynamic secrets.
**Weaknesses:** Primarily focused on app secrets and PKI, not OAuth token lifecycle. Significant operational overhead to self-host. No Anthropic-specific integration.
**Verdict:** Interesting for certificate management. Overkill for a 2-person team. Doesn't solve OAuth refresh.

#### HashiCorp Vault

Enterprise-grade secret management with dynamic secrets, lease management, and extensive plugin ecosystem.

**Strengths:** Dynamic secrets for AWS/GCP/GitHub. Lease-based expiry with auto-renewal. Plugin for almost everything. Self-hostable.
**Weaknesses:** Massive operational overhead. Designed for large orgs. Resource-hungry. Complex to operate. Our server has 2GB RAM; Vault wants more.
**Verdict:** The technically correct answer that's completely wrong for our scale. We'd spend more time managing Vault than managing tokens.

#### Native Token Refresh Daemon (Recommended approach)

A small script/service we build ourselves that:
1. Monitors token expiry for each credential type
2. Auto-refreshes OAuth tokens before they expire
3. Alerts via Telegram when credentials need manual rotation
4. Stores current credentials in 1Password (which we already have)

**Strengths:** Solves exactly our problem. No new vendors. Minimal resource usage. We control the logic. Can handle our weird auth flows (Claude Max paste-token, OpenClaw gateway).
**Weaknesses:** We have to build it. Maintenance burden.
**Verdict:** This is the right answer.

## Fit Assessment for Our Stack (Tool by Tool)

| Credential | Type | Expires? | Composio helps? | 1Password helps? | Native daemon helps? |
|---|---|---|---|---|---|
| **Anthropic OAuth (Claude Max)** | OAuth token via paste-token | Yes, regularly | ❌ No integration | Storage only | ✅ Can automate refresh |
| **OpenClaw auth-profiles.json** | Config file with tokens | When tokens expire | ❌ | Storage only | ✅ Can update config |
| **GitHub fine-grained PATs** | PAT | Yes (configurable) | ❌ (uses OAuth, not PATs) | Storage only | ✅ Can alert before expiry |
| **GCP service account key** | JSON key file | No (but can be rotated) | ❌ | Storage only | ✅ Can rotate |
| **Google Workspace delegation** | Service account + scopes | No expiry | N/A | N/A | N/A |
| **Brave Search API key** | API key | No | ❌ | Storage only | N/A (doesn't expire) |
| **1Password SA token** | Service account token | Configurable | ❌ | N/A (circular) | ✅ Can alert |
| **Cursor API keys** | Various | Depends on key type | ❌ | Storage only | ✅ Can distribute |
| **Cowork API keys** | Various | Depends on key type | ❌ | Storage only | ✅ Can distribute |

**Key insight:** Most of our credentials are either non-expiring (Brave API key, GCP SA key) or use proprietary auth flows (Anthropic paste-token). Composio's OAuth management is irrelevant for nearly all of them.

## Security Model

### Composio
- Credentials stored on Composio's cloud servers
- Enterprise tier offers VPC/on-prem deployment
- SOC-2 mentioned for enterprise only
- API key required for SDK access
- Connected accounts isolated by user_id
- Attack surface: Composio becomes a high-value target storing many users' OAuth tokens

### 1Password Connect (our current approach)
- Credentials stored in 1Password's zero-knowledge architecture
- Connect server self-hosted, caches locally
- SOC-2 Type 2 certified
- Service account token is the only secret to protect
- We already trust 1Password with everything

### Native daemon
- Credentials stored in 1Password (via existing integration)
- Daemon runs on our server, no external dependencies
- Attack surface: same as current (our server + 1Password)
- No new trust boundaries

## Pricing and Vendor Lock-in

| Solution | Monthly cost | Lock-in risk |
|---|---|---|
| Composio Free | $0 | Medium (proprietary platform, SDK dependency) |
| Composio Paid | $29/mo | Medium-High |
| 1Password Connect | $0 (included in Teams) | Low (we already depend on 1Password) |
| Doppler | $8/mo (2 users) | Medium (cloud-only) |
| Infisical (self-hosted) | $0 | Low (open source) |
| Vault (self-hosted) | $0 | Low (open source) but high ops cost |
| Native daemon | $0 | None |

## What We Should Steal Even If We Don't Use Composio

1. **The "meta tools" pattern.** Instead of hardcoding tool integrations, let the agent discover and authenticate tools at runtime. This is a good architectural idea for Synthweave.

2. **Connect Links as a UX pattern.** Hosted auth pages that handle the OAuth dance. If we ever build multi-user features, this is the right UX.

3. **MCP as integration protocol.** Composio's MCP support means any MCP-compatible client (Cursor, Claude Desktop) can use it. We should think about MCP for our own tool integrations.

4. **Auth config abstraction.** Separating "how to authenticate with this service" (auth config) from "this specific user's credentials" (connected account) is a clean pattern.

5. **Automatic token refresh as a first-class feature.** Whatever we build, token refresh should be proactive (before expiry), not reactive (after failure).

## Concrete Recommendation

### Do not adopt Composio for credential management.

**Reasoning:**
1. Composio solves a different problem (AI agent tool execution) than ours (credential lifecycle for infrastructure).
2. It does not support our most painful credential: Anthropic Claude Max OAuth via paste-token.
3. It does not support GitHub PATs, GCP service account keys, or 1Password tokens.
4. It adds a new vendor dependency for something that doesn't solve our core pain.
5. It's designed for multi-tenant SaaS, not a 2-person infrastructure team.

### Recommended approach: Build a lightweight token refresh daemon + leverage 1Password Connect

**Architecture:**
```
┌─────────────────────────────────────┐
│  token-guardian (systemd service)   │
│                                     │
│  ┌──────────┐  ┌──────────────────┐ │
│  │ Watchers │  │ Alert via        │ │
│  │          │  │ Telegram bot     │ │
│  │ - Claude │  └──────────────────┘ │
│  │   OAuth  │                       │
│  │ - GitHub │  ┌──────────────────┐ │
│  │   PAT    │  │ 1Password        │ │
│  │ - GCP SA │  │ (credential      │ │
│  │ - 1P SA  │  │  store)          │ │
│  └──────────┘  └──────────────────┘ │
└─────────────────────────────────────┘
```

## Implementation Plan

### Phase 1: Monitoring and Alerting (1-2 days)

1. **Create `scripts/token-guardian.sh`** (or Node.js):
   - Run `openclaw models status` and parse for `[cooldown]` flags
   - Check GitHub PAT expiry via `gh api user` response headers
   - Check 1Password SA token validity
   - Alert via Telegram bot when any credential is unhealthy

2. **Add systemd timer** to run every 15 minutes
3. **Add to HEARTBEAT.md** as a check item

### Phase 2: Auto-refresh for Claude Max OAuth (3-5 days)

This is the hard one. The current flow requires:
1. Run `claude setup-token` on a Mac (interactive)
2. Copy the token
3. Run `openclaw models auth paste-token --provider anthropic` on the server

**Options to automate:**
- Investigate if `claude setup-token` can run headlessly
- Check if Claude Max OAuth has a refresh_token flow we can use
- If not automatable: at minimum, alert 24h before expected expiry so the human can refresh proactively

### Phase 3: Credential Distribution (future)

If we add more tools (Cursor, Cowork), use 1Password Connect API to:
- Store all credentials in 1Password
- Have each tool read its credentials from 1Password at startup
- `token-guardian` updates 1Password when it refreshes a token
- Tools pick up new credentials on next read

### Phase 4: Consider Composio for tool integrations (future, separate decision)

If Synthweave needs to let agents interact with GitHub, Gmail, Slack, etc., Composio's tool execution layer is worth revisiting. But that's an agent capabilities decision, not a credential management decision.

---

*This analysis was written for the Sivart/Synthweave project, a 2-person team running an AI agent infrastructure on a single Hetzner VPS. Enterprise solutions are evaluated but not recommended at this scale.*
