---
title: 1Password Integration for AI Agent Credential Management
tags:
  - ai-agents
  - systems-thinking
related:
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
  - [[accounting-bookkeeping-research]]
source: research/raw/1password-integration.md
---

# 1Password Integration for AI Agent Credential Management

_Supporting document for the Agent OpSec research (Issue #53)._

## Overview

This document covers the practical details of integrating 1Password with an AI agent running as a systemd service on a headless Linux server. The goal: remove API keys from the systemd environment and manage them through 1Password instead.

## Recommended Approach: Service Account + `op run`

### Why Service Accounts

A 1Password Service Account is a non-human identity with its own authentication token. It can be scoped to specific vaults with specific permissions (read-only, read-write, or create). The token (`OP_SERVICE_ACCOUNT_TOKEN`) is the only secret that needs to live on the server.

Benefits over personal account auth:

- No interactive login required (critical for headless servers).
- Permissions are immutable after creation (principle of least privilege enforced at creation time).
- Can be revoked instantly without affecting the human's 1Password access.
- Rate limits apply per service account, not per personal account.

### Setup Steps

1. **Create a "[[Sivart]] Secrets" vault** in 1Password (via web or desktop app).

2. **Store secrets in the vault**: Telegram bot token, Claude OAuth token, OpenAI API key, GitHub PAT, Gateway token, any future API keys.

3. **Create a service account** on 1Password.com (Developer > Service Accounts).
   - Name: `sivart-server`
   - Vault access: "[[Sivart]] Secrets" (read-only)
   - Cannot create vaults (minimizes blast radius)

4. **Save the service account token** in 1Password itself (meta, but important: never store it in plaintext on disk).

5. **Install 1Password CLI on the server**:

   ```bash
   # Add the 1Password apt repository
   curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
     gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg
   echo "deb [arch=amd64 signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] https://downloads.1password.com/linux/debian/amd64 stable main" | \
     tee /etc/apt/sources.list.d/1password-cli.list
   apt update && apt install -y 1password-cli
   ```

6. **Set the service account token** in the systemd environment (this is the one secret that must remain in the environment):

   ```bash
   systemctl --user edit clawdbot-gateway.service
   # Add:
   # [Service]
   # Environment=OP_SERVICE_ACCOUNT_TOKEN=<token>
   ```

7. **Create a secrets environment file** using 1Password secret references:

   ```bash
   # ~/.clawdbot/secrets.env
   TELEGRAM_BOT_TOKEN=op://[[Sivart]] Secrets/Telegram Bot/token
   CLAUDE_CODE_OAUTH_TOKEN=op://[[Sivart]] Secrets/Claude OAuth/token
   OPENAI_API_KEY=op://[[Sivart]] Secrets/OpenAI/api key
   CLAWDBOT_GATEWAY_TOKEN=op://[[Sivart]] Secrets/Gateway/token
   ```

8. **Modify the service to use `op run`**:

   ```bash
   systemctl --user edit clawdbot-gateway.service
   # Change ExecStart to:
   # ExecStart=/usr/bin/op run --env-file=%h/.clawdbot/secrets.env -- \
   #   /usr/bin/node %h/.npm-global/lib/node_modules/clawdbot/dist/entry.js gateway --port 18789
   ```

### What This Achieves

- Only `OP_SERVICE_ACCOUNT_TOKEN` lives in the systemd environment.
- All other secrets are resolved at runtime from 1Password.
- Secrets never touch disk in plaintext (the `.env` file contains references, not values).
- Rotating a secret means updating it in 1Password; the next service restart picks it up automatically.
- Revoking the service account immediately cuts off all agent access to secrets.

### Tradeoffs

- **Startup dependency**: The service now requires 1Password servers to be reachable at startup. If 1Password is down, the service fails to start. For a personal agent, this is acceptable.
- **One remaining env var**: The service account token itself must still be an environment variable. This is a smaller attack surface (one token vs. many), and it can be rotated independently.
- **Requires `sudo`**: Installing `op` requires root. [[Ξ2T]] handles this during initial setup.

## Alternative: `op inject` for Config Files

If secrets live in the Clawdbot config file rather than environment variables:

```bash
# ~/.clawdbot/clawdbot.json.tpl
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "op://[[Sivart]] Secrets/Telegram Bot/token",
    },
  },
}

# Resolve at startup:
op inject -i ~/.clawdbot/clawdbot.json.tpl -o ~/.clawdbot/clawdbot.json
```

This approach writes the resolved config to disk, which is less ideal than `op run` (secrets exist on disk briefly). Use only if `op run` does not work for a specific integration.

## Alternative: systemd `LoadCredential`

For a zero-dependency approach:

```ini
[Service]
LoadCredential=telegram-token:/path/to/encrypted/telegram-token
LoadCredential=openai-key:/path/to/encrypted/openai-key
```

systemd makes these available at `$CREDENTIALS_DIRECTORY/telegram-token`. The application must be modified to read from this path. This is more complex and less portable than 1Password, but it works without external services.

## Key Decisions for [[Ξ2T]]

1. **Create the [[Sivart]] Secrets vault.** Only [[Ξ2T]] can do this (requires 1Password admin).
2. **Create the service account.** Requires 1Password web interface.
3. **Install `op` on the server.** Requires `sudo`.
4. **Migrate secrets.** One-time process: move each secret into 1Password, update the service config, restart, verify, then remove old env vars.

## Secret Inventory

Current secrets that should be managed:

| Secret             | Current Location     | Recommended 1Password Item         |
| ------------------ | -------------------- | ---------------------------------- |
| Telegram bot token | clawdbot.json or env | [[Sivart]] Secrets / Telegram Bot  |
| Claude OAuth token | systemd env          | [[Sivart]] Secrets / Claude OAuth  |
| OpenAI API key     | systemd env          | [[Sivart]] Secrets / OpenAI        |
| Gateway token      | systemd env          | [[Sivart]] Secrets / Gateway Token |
| GitHub PAT         | gh CLI config        | [[Sivart]] Secrets / GitHub PAT    |
