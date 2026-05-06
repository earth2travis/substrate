---
title: "Agent Security: Least Privilege for Autonomous Systems"
tags: [concept, agent, security, opsec, credentials, server]
related: [[agentic-architecture]], [[agent-identity]], [[toyota-production-system]]
source: research/findings/agent-opsec-overview.md
---

# Agent Security: Least Privilege for Autonomous Systems

## Overview

Agentic AI systems operate with autonomy. Autonomy without accountability is dangerous. Security is not a feature; it is the foundation that makes autonomy possible.

## The Credential Problem

**Environment variables are the most common way to pass secrets, and the weakest.** They are visible in `/proc/<pid>/environ`, logged by systemd journal, inherited by child processes. For a personal agent with a single user, this is acceptable but not ideal. The risk: any code the agent executes (or any prompt injection that triggers shell commands) can read the full environment.

**Better approach: 1Password CLI service accounts.** Authenticate with a single token (`OP_SERVICE_ACCOUNT_TOKEN`), scoped to a specific vault. Use `op run` to inject secrets into the process for the duration of a single command. This reduces exposure to one rotatable token rather than spreading multiple API keys across the environment.

## Account Isolation Principles

An agent should have the minimum access needed for its current tasks, with a clear path to revoke that access.

**GitHub**: Use a machine user or fine-grained PAT scoped to specific repos. The current setup uses Ξ2T's account with broad scope: `repo`, `workflow`, `gist`, `project`, `read:org`. A compromised token could modify any repository, leak private code via gists, or trigger workflows.

**Email**: The agent should have a separate address (e.g., `email@sivart.wtf`). Sharing the human's inbox creates privacy risk in both directions.

**Telegram**: Already separate. The agent has its own bot token and identity. Correct.

**1Password**: A separate vault with a dedicated service account. The human retains admin access; the agent gets read-only access to its own secrets.

## Server Hardening Checklist

| Check | Status | Action |
|-------|--------|--------|
| fail2ban | Active | Continue monitoring |
| unattended-upgrades | Active | Continue monitoring |
| ufw (firewall) | Not installed | `apt install ufw && ufw allow 22 && ufw enable` |
| SSH password auth | Default config | Set `PasswordAuthentication no` explicitly |
| Credentials directory | 775 (too open) | `chmod 700 ~/.clawdbot/credentials/` |
| Docker | Not installed | Install for sandboxing before adding untrusted integrations |
| Gateway binding | Loopback only | Correct. Do not change without VPN. |

## Blast Radius

If an attacker gains access as the `clawd` user:
- Read all agent memory, session history, workspace files
- Read all API keys from process environment
- Send messages as the agent on Telegram
- Push code to any of the human's GitHub repositories
- Use API keys for any purpose

A compromised server should not grant access to everything the human owns.

## The Security Philosophy

**Access control before intelligence.** Most failures are not sophisticated exploits. They are someone messaging the bot and the bot doing what they asked.

Recommended priority order:
1. Lock down who can talk to the bot (pairing, allowlists)
2. Scope where the bot can act (tool policy, sandboxing)
3. Assume the model can be manipulated; design so manipulation has limited blast radius

## Connection to Jidoka

Toyota's jidoka principle, automation with a human touch, applies directly: when something goes wrong, production stops. For agent systems: when a security boundary is breached or anomalous behavior detected, halt and investigate rather than letting the agent continue operating.
