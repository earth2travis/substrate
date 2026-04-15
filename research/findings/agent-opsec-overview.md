---
title: "Agent Operational Security: Research and Recommendations"
tags:
  - ai-agents
  - knowledge-management
  - process-philosophy
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/agent-opsec-overview.md
---

# Agent Operational Security: Research and Recommendations

_Research for Issue #53. Conducted February 1, 2026._

## Summary

This document examines the security posture of Sivart, an AI agent running on a Hetzner cloud server (Ubuntu 24.04), connected via Telegram and GitHub, with plans to expand into email, blog hosting, and additional API integrations. The goal: understand risks, identify gaps, and recommend a security posture appropriate for our scale before expanding further.

The findings fall into six areas: platform security (OpenClaw), credential management, account isolation, server hardening, risks specific to our setup, and community practices.

## 1. OpenClaw Platform Security

OpenClaw (the platform powering Clawdbot) has a mature, layered security model. The documentation is thorough, and the defaults are sensible.

### What the Platform Provides

**DM Pairing (Default: On).** Unknown senders receive a short pairing code and their messages are ignored until the owner approves. Codes expire after one hour. Pending requests are capped at three per channel. This is the single most important defense: it gates who can talk to the bot.

**Loopback Binding.** The Gateway WebSocket defaults to `127.0.0.1:18789`. Nothing listens on public interfaces unless explicitly configured. Non-loopback binds require auth tokens. This is correct and should never change without a VPN or tailnet in place.

**Security Audit Tool.** `openclaw security audit` (and `--deep`, `--fix`) checks inbound access policies, tool blast radius, network exposure, browser control, disk permissions, and plugin safety. Running this regularly is strongly recommended.

**Formal Verification.** OpenClaw maintains TLA+ models for its security properties: pairing store correctness, DM gating, session isolation, ingress gating, and gateway exposure. These are executable, attacker-driven regression suites. Not a proof of total security, but meaningfully beyond what most projects offer.

**Docker Sandboxing.** Tools can run inside Docker containers to limit blast radius. Configurable per agent, per session, or shared. Workspace access can be none, read-only, or read-write. This is the strongest available mitigation against prompt injection leading to file or process access.

**Per-Agent Isolation.** Multi-agent routing gives each agent its own workspace, session store, auth profiles, and tool policies. Agents can be restricted to specific tools (allow/deny lists). This enables principle of least privilege at the agent level.

**Tool Policy and Elevated Mode.** Tools can be allowed or denied per agent. Elevated exec runs on the host and bypasses sandboxing, so it should be treated as operator-level access. The platform recommends Anthropic Opus 4.5 for tool-enabled agents because of its prompt injection resistance.

### What the Platform Recommends

The security docs lay out a clear philosophy: **access control before intelligence**. Most failures are not sophisticated exploits. They are someone messaging the bot and the bot doing what they asked.

The recommended priority order:

1. Lock down who can talk to the bot (pairing, allowlists).
2. Scope where the bot can act (tool policy, sandboxing).
3. Assume the model can be manipulated; design so manipulation has limited blast radius.

For credentials, the platform recommends: keep secrets out of prompts, pass them via env/config on the gateway host, use `logging.redactSensitive` to avoid leaking them in tool summaries.

### Our Status

Our Gateway is loopback-only (confirmed via `ss -tlnp`). DM policy is pairing. Telegram is the only active channel. These defaults are correct.

**Gaps identified:**

- Docker is not installed, so sandboxing is unavailable.
- We have not run `openclaw security audit` (or its Clawdbot equivalent).
- No tool deny lists are configured.

## 2. Credential Management

This is the area with the most room for improvement.

### Current State

Credentials are stored in three places:

1. **Systemd environment variables.** The gateway service environment contains `CLAUDE_CODE_OAUTH_TOKEN`, `OPENAI_API_KEY`, `CLAWDBOT_GATEWAY_TOKEN`, and the Telegram bot token (via config). These are visible to any process running as the `clawd` user and readable from `/proc/<pid>/environ`.

2. **Clawdbot config file** (`~/.clawdbot/clawdbot.json`, permissions 600). Contains the Telegram bot token and other configuration.

3. **GitHub CLI auth** (`~/.config/gh/hosts.yml`). Contains a GitHub OAuth token with broad scope: `gist`, `project`, `read:org`, `repo`, `workflow`.

### The Problem with Environment Variables

Environment variables are the most common way to pass secrets to services. They are also the weakest:

- Visible in `/proc/<pid>/environ` to any process with the same UID.
- Logged by systemd journal on service start (depending on configuration).
- Inherited by child processes (including any exec'd commands).
- Visible in the output of `systemctl --user show` (which is how I found them during this audit).

For a personal agent with a single user on the server, this is acceptable but not ideal. The risk is that any code the agent executes (or any prompt injection that triggers shell commands) can read the full environment, including all API keys.

### 1Password CLI (`op`)

1Password CLI is not installed on the server. It offers three relevant approaches:

**`op run`**: Wraps a command and injects secrets from 1Password into the process environment for the duration of that command. Secrets are not stored on disk. Example: `op run --env-file=secrets.env -- clawdbot gateway`. This is the most practical approach for a service running on a headless server.

**`op read`**: Reads a single secret reference and outputs it. Useful for scripts that need one specific value.

**`op inject`**: Takes a template with secret references and outputs a file with resolved values. Good for config files.

**Service Accounts**: 1Password offers service accounts that authenticate with a single token (stored as `OP_SERVICE_ACCOUNT_TOKEN`). The service account can be scoped to specific vaults with specific permissions. This is the recommended approach for servers: create a service account with read-only access to a "Sivart" vault containing only the secrets the agent needs.

The chicken-and-egg problem: to use `op` on a headless server, you need to store the service account token somewhere (typically an environment variable or a file). This does not eliminate environment-based secrets entirely, but it reduces exposure to a single token that can be rotated and revoked, rather than spreading multiple API keys across the environment.

### 1Password Connect Server

An alternative to the CLI. Runs as a Docker container, provides a REST API for secret retrieval, caches data locally. More appropriate for multi-service environments or teams. Overkill for a single-agent setup.

### HashiCorp Vault

A full-featured secrets management system. Supports dynamic secrets, lease-based access, comprehensive audit logging. Significantly more complex to operate than 1Password. Not recommended for our scale.

### systemd Credentials

systemd has a built-in credential passing mechanism (`LoadCredential=`, `SetCredentialEncrypted=`). Secrets are loaded from files into a per-service credential directory, accessible only to that service. This is a lighter-weight option that does not require external tooling but offers less management capability than 1Password.

### Recommendation

**Short term**: Install 1Password CLI. Create a service account scoped to a "Sivart Secrets" vault. Use `op run` to inject secrets into the gateway service at startup. This removes API keys from the systemd environment and centralizes them in 1Password where Ξ2T already manages credentials.

**Longer term**: Evaluate `systemd` `LoadCredentialEncrypted=` as a zero-dependency alternative if the 1Password approach proves too complex for service restarts.

## 3. Account Isolation and Identity

### Should an AI Agent Have Its Own Accounts?

Yes, with nuance. The principle of least privilege applies: an agent should only have access to what it needs, and that access should be revocable without disrupting the human's accounts.

**GitHub**: Currently using Ξ2T's account (`earth2travis`) with a broad-scope token. This works for a private repo where the agent is an extension of the owner, but it means the agent could (if compromised) access all of Ξ2T's repos, create gists, modify projects, and trigger workflows across any repository. A better approach: create a machine user or use fine-grained personal access tokens scoped to the `sivart` repo with only the permissions needed (contents read/write, issues read/write, pull requests read/write).

**Email**: When Sivart gets email (#47), it should be a separate address (something like `sivart@domain`). Sharing the human's inbox creates privacy risk in both directions: the agent sees personal email, and a compromised agent could impersonate the human.

**Telegram**: Already separate. Sivart has its own bot token and identity. Correct.

**Social Media**: Separate accounts with clearly labeled AI identity. This is both a security boundary and a trust/transparency practice.

**1Password**: A separate vault (not the human's personal vault) with a dedicated service account. The human retains admin access; the agent gets read-only access to its own secrets.

### Access Scoping

The general principle: **an agent should have the minimum access needed for its current tasks, with a clear path to revoke that access.**

For each new integration:

1. What permissions does this integration actually need?
2. Can those permissions be scoped (read-only, specific repos, specific folders)?
3. What is the blast radius if this credential is compromised?
4. How quickly can this credential be rotated?

## 4. Server Security

### Current State (Audited)

| Check                 | Status         | Notes                                                                         |
| --------------------- | -------------- | ----------------------------------------------------------------------------- |
| fail2ban              | Active         | Protects SSH against brute force                                              |
| unattended-upgrades   | Active         | Automatic security patches                                                    |
| SSH key auth          | Default config | PasswordAuthentication commented out (relies on system default, which varies) |
| Firewall (ufw)        | Not installed  | No firewall rules in place                                                    |
| Home directory        | 750            | Correct: group-readable but not world-readable                                |
| .clawdbot directory   | 700            | Correct: owner-only                                                           |
| Config file           | 600            | Correct                                                                       |
| Auth profiles         | 600            | Correct                                                                       |
| Credentials directory | 775            | **Problem**: group and world-executable                                       |
| Credential files      | 600            | Files within are correctly locked                                             |
| Docker                | Not installed  | Sandboxing unavailable                                                        |
| Gateway binding       | Loopback only  | Correct                                                                       |
| SSH listening         | 0.0.0.0:22     | Standard, but open to all interfaces                                          |

### Recommendations

**Install and configure ufw.** Even on a cloud server with external firewall rules, a host-level firewall provides defense in depth. Allow SSH (22) and deny everything else. The gateway already binds to loopback, so no firewall rules are needed for it.

**Explicitly disable SSH password authentication.** The current config has `PasswordAuthentication` commented out. Uncomment and set to `no`. Also set `PermitRootLogin no` explicitly.

**Fix credentials directory permissions.** `chmod 700 ~/.clawdbot/credentials/` (currently 775).

**Consider installing Docker** for sandboxing capability, especially before adding integrations that process untrusted content (email, web browsing).

**systemd service hardening.** The current service unit does not include hardening directives. Consider adding:

- `ProtectHome=read-only` (or `tmpfs` with explicit bind mounts)
- `ProtectSystem=strict`
- `PrivateTmp=yes`
- `NoNewPrivileges=yes`
- `RestrictSUIDSGID=yes`
- `ReadWritePaths=` for only the directories the service needs

These are low-cost, high-value mitigations that limit what a compromised process can do.

## 5. Risks Specific to Our Setup

### Telegram Bot Token Exposure

If the bot token leaks, an attacker can impersonate Sivart on Telegram, read messages sent to the bot, and potentially trigger commands. Mitigation: store in 1Password, inject at runtime, have a procedure to rotate via @BotFather if compromised.

### GitHub Token Scope

The current token has `repo` (full repository access), `workflow` (can trigger GitHub Actions), `gist` (can create public gists), `project`, and `read:org`. This is broader than needed. A compromised token could modify any repository, leak private code via gists, or trigger workflows. Mitigation: switch to a fine-grained PAT scoped to the `sivart` repo only.

### API Keys in Process Environment

As discussed above, all API keys are visible to any process running as `clawd`. This includes any command the agent executes, any subagent, and any prompt-injected shell command. Mitigation: 1Password service account with `op run`.

### What Happens If the Server Is Compromised

Current blast radius if an attacker gains access as the `clawd` user:

- Read all agent memory, session history, and workspace files.
- Read all API keys from the process environment.
- Send messages as Sivart on Telegram.
- Push code to any of Ξ2T's GitHub repositories.
- Use the OpenAI API key for any purpose.
- Use the Claude OAuth token for any purpose.

This is the most important reason to scope credentials: a compromised server should not grant access to everything the human owns.

### Prompt Injection

Even with DM pairing, prompt injection can come through any content the agent reads: web pages, fetched URLs, email content, pasted code. The OpenClaw docs are clear on this: "the sender is not the only threat surface; the content itself can carry adversarial instructions."

Mitigations (layered):

1. Sandboxing (Docker) limits what injected commands can access.
2. Tool deny lists reduce the available attack surface.
3. Strong models (Opus 4.5) are more resistant to prompt injection.
4. Keeping secrets out of the agent's reachable filesystem and prompts.
5. Using a read-only "reader agent" to summarize untrusted content before passing to the main agent.

## 6. What Other AI Agent Operators Do

### Community Practices

Direct access to the OpenClaw Discord and community forums was not available during this research (web search was not configured, and Discord content is not fetchable). This is a gap that should be revisited.

### General Patterns from Documentation and Guides

From the OpenClaw security docs, the 1Password developer documentation, and general infrastructure security resources, common patterns emerge:

**Secrets management is the number one concern.** Every guide, every framework, every discussion about agent security starts here. Environment variables are the minimum viable approach; anything beyond a hobby project should use a secrets manager.

**Principle of least privilege is universal.** Agents should have the minimum permissions needed. This applies to API tokens, filesystem access, network access, and which tools the agent can invoke.

**Sandboxing is the strongest mitigation for prompt injection.** When an agent can execute code, the question is not whether prompt injection will be attempted, but what happens when it succeeds. Sandboxing limits the damage.

**Separate identities reduce blast radius.** Dedicated accounts, dedicated API keys, dedicated vaults. If one credential is compromised, the damage is contained.

**Audit trails matter.** Knowing what the agent did, when, and why. OpenClaw session logs provide this, but they should be treated as sensitive data themselves.

### Gaps in Available Research

The field of "personal AI agent security" is young. Most security literature focuses on enterprise deployments, multi-tenant systems, or theoretical prompt injection research. Practical guides for a single human running a personal AI agent on a VPS are rare. This document represents our attempt to synthesize what exists into something actionable.

**Flagged for revisiting** (once additional access is available):

- YouTube content on agent security setups
- Twitter/X discussions in the OpenClaw and AI agent communities
- OpenClaw Discord community practices
- Blog posts from other personal agent operators

## Prioritized Action Plan

### Immediate (This Week)

1. **Fix credentials directory permissions**: `chmod 700 ~/.clawdbot/credentials/`
2. **Explicitly disable SSH password auth**: Uncomment and set `PasswordAuthentication no` in sshd_config
3. **Install ufw**: `apt install ufw && ufw allow 22 && ufw enable`
4. **Run the security audit**: `clawdbot security audit --deep`

### Short Term (Next Two Weeks)

5. **Install 1Password CLI** and create a service account for Sivart
6. **Move secrets to 1Password**: Telegram bot token, API keys, OAuth tokens
7. **Use `op run`** to inject secrets into the gateway service
8. **Scope GitHub token**: Create a fine-grained PAT for the sivart repo only

### Medium Term (Next Month)

9. **Install Docker** and enable sandboxing for non-main sessions
10. **Add systemd hardening directives** to the gateway service unit
11. **Create separate accounts** for Sivart (email, any new services)
12. **Configure tool deny lists** for capabilities the agent does not need

### Ongoing

13. **Run `clawdbot security audit`** after any config change
14. **Rotate credentials** on a regular schedule (quarterly)
15. **Review session logs** periodically for anomalous behavior
16. **Update this document** as the setup evolves

## Sources

- OpenClaw Security Documentation: https://docs.openclaw.ai/gateway/security
- OpenClaw Sandboxing Documentation: https://docs.openclaw.ai/gateway/sandboxing
- OpenClaw Pairing Documentation: https://docs.openclaw.ai/start/pairing
- OpenClaw Multi-Agent Documentation: https://docs.openclaw.ai/concepts/multi-agent
- OpenClaw Configuration Documentation: https://docs.openclaw.ai/gateway/configuration
- OpenClaw Remote Access Documentation: https://docs.openclaw.ai/gateway/remote
- OpenClaw Formal Verification: https://docs.openclaw.ai/security/formal-verification
- 1Password CLI Documentation: https://developer.1password.com/docs/cli/get-started
- 1Password Secret References: https://developer.1password.com/docs/cli/secret-references
- 1Password Service Accounts: https://developer.1password.com/docs/service-accounts/get-started
- 1Password Connect: https://developer.1password.com/docs/connect
- HashiCorp Vault: https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault
- Server security audit conducted live on the target server (February 1, 2026)
