---
title: "Agent Operational Security: Server Hardening and Credential Management"
tags: [agent, security, opsec, credentials, server, hardening]
related: [[agentic-architecture]], [[agent-identity]], [[agent-evaluation]]
source: research/raw/agent-opsec-overview.md
---

# Agent Operational Security: Server Hardening and Credential Management

## Summary

Security posture of Sivart, an AI agent running on a Hetzner cloud server (Ubuntu 24.04), connected via Telegram and GitHub, with plans to expand into email, blog hosting, and additional API integrations.

## Platform Security (OpenClaw)

**DM Pairing (Default: On)**: Unknown senders receive a pairing code; messages ignored until owner approves. Codes expire after one hour. Pending requests capped at three per channel.

**Loopback Binding**: Gateway WebSocket defaults to `127.0.0.1:18789`. Nothing listens on public interfaces unless explicitly configured.

**Security Audit Tool**: `openclaw security audit` checks inbound access policies, tool blast radius, network exposure, browser control, disk permissions, and plugin safety.

**Formal Verification**: TLA+ models for security properties: pairing store correctness, DM gating, session isolation, ingress gating, gateway exposure.

**Docker Sandboxing**: Tools can run inside Docker containers to limit blast radius. Workspace access: none, read-only, or read-write.

**Per-Agent Isolation**: Each agent has its own workspace, session store, auth profiles, and tool policies. Tools can be allowed or denied per agent.

## Credential Management

**Current State**: Credentials stored in three places: systemd environment variables (visible to any process running as `clawd`), Clawdbot config file (`~/.clawdbot/clawdbot.json`, permissions 600), and GitHub CLI auth (`~/.config/gh/hosts.yml`).

**The Problem with Environment Variables**: Visible in `/proc/<pid>/environ`, logged by systemd journal, inherited by child processes. For a personal agent with a single user, this is acceptable but not ideal.

**1Password CLI (`op`)**: Three relevant approaches:
- **`op run`**: Wraps a command, injects secrets from 1Password into process environment for that command only.
- **`op read`**: Reads a single secret reference.
- **`op inject`**: Takes a template with secret references, outputs resolved file.
- **Service Accounts**: Authenticate with a single token (`OP_SERVICE_ACCOUNT_TOKEN`), scoped to specific vaults.

**Recommendation**: Install 1Password CLI. Create a service account scoped to a "Sivart Secrets" vault. Use `op run` to inject secrets into the gateway service at startup.

## Account Isolation

**GitHub**: Currently using [[Ξ2T]]'s account (`earth2travis`) with a broad-scope token. Better approach: create a machine user or use fine-grained PAT scoped to the `sivart` repo.

**Email**: When Sivart gets email, it should be a separate address (e.g., `email@sivart.wtf`). Sharing the human's inbox creates privacy risk in both directions.

**Telegram**: Already separate. Sivart has its own bot token and identity. Correct.

**1Password**: A separate vault (not the human's personal vault) with a dedicated service account.

## Server Security Audit Results

| Check | Status | Notes |
|-------|--------|-------|
| fail2ban | Active | Protects SSH against brute force |
| unattended-upgrades | Active | Automatic security patches |
| SSH key auth | Default config | PasswordAuthentication commented out |
| Firewall (ufw) | Not installed | No firewall rules in place |
| Home directory | 750 | Correct: group-readable, not world-readable |
| .clawdbot directory | 700 | Correct: owner-only |
| Config file | 600 | Correct |
| Credentials directory | 775 | **Problem**: group and world-executable |
| Docker | Not installed | Sandboxing unavailable |
| Gateway binding | Loopback only | Correct |
| SSH listening | 0.0.0.0:22 | Standard, but open to all interfaces |

## Immediate Recommendations

1. **Fix credentials directory permissions**: `chmod 700 ~/.clawdbot/credentials/`
2. **Explicitly disable SSH password auth**: Set `PasswordAuthentication no` in sshd_config
3. **Install ufw**: `apt install ufw && ufw allow 22 && ufw enable`
4. **Run the security audit**: `clawdbot security audit --deep`
5. **Install 1Password CLI** and create a service account for Sivart
6. **Move secrets to 1Password**: Telegram bot token, API keys, OAuth tokens
7. **Scope GitHub token**: Create fine-grained PAT for the sivart repo only

## Blast Radius If Server Compromised

Current blast radius if attacker gains access as `clawd`:
- Read all agent memory, session history, workspace files
- Read all API keys from process environment
- Send messages as Sivart on Telegram
- Push code to any of [[Ξ2T]]'s GitHub repositories
- Use the OpenAI API key for any purpose
- Use the Claude OAuth token for any purpose

This is the most important reason to scope credentials: a compromised server should not grant access to everything the human owns.
