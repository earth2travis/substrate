---
title: "1Password Service Account Integration for AI Agents"
tags: [security, operations, 1password, agents]
related:
- agent-opsec-overview
- agent-evaluation
source: research/raw/1password-integration.md
---
# 1Password Service Account Integration for AI Agents

## Summary

Practical guide for managing AI agent credentials through 1Password service accounts on headless Linux servers. The core pattern: one service account token in systemd environment, all other secrets resolved at runtime via `op run`.

## Key Points

- **Service account model**: Non-human identity scoped to specific vaults. Immutable permissions, instant revocation, separate rate limits.
- **Secret references**: The `.env` file contains `op://` URIs, not plaintext values. Secrets never touch disk.
- **Runtime resolution**: `op run --env-file=secrets.env -- <command>` injects secrets at process startup.
- **Rotation**: Update in 1Password; next service restart picks it up automatically.
- **Blast radius**: Revoking the service account immediately cuts all agent access.

## Why This Matters

For an AI-native operation, manual secret rotation is a single point of failure. Service accounts let the agent manage its own credential lifecycle without ever holding plaintext on disk. The 48% vs 100% compliance gap (documentation vs script enforcement) applies here too: rules about secret storage must be enforced by the deployment mechanism, not documented and hoped for.

## Applicability

Relevant for any agent running as a persistent service that needs API keys, tokens, or credentials. Not just for Telegram bots; applies to any daemonized agent process.