---
title: Server Hardening Checklist
tags:
  - ai-agents
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/server-hardening.md
---

# Server Hardening Checklist

_Supporting document for the Agent OpSec research (Issue #53)._

## Current State (February 1, 2026)

Server: Hetzner CPX11, Ubuntu 24.04, Ashburn VA.

### What Is Already Good

- **fail2ban**: Active. Protects SSH against brute force attacks.
- **unattended-upgrades**: Active. Security patches applied automatically.
- **Home directory permissions**: 750. Only clawd and its group can access.
- **Clawdbot state directory**: 700. Owner-only access.
- **Config and auth files**: 600. Properly locked.
- **Gateway binding**: Loopback only (127.0.0.1:18789). Not exposed to the network.
- **Telegram DM policy**: Pairing (default). Unknown senders are gated.

### What Needs Fixing

**Credentials directory permissions (775)**

```bash
chmod 700 ~/.clawdbot/credentials/
```

The files within are correctly 600, but the directory itself allows group and world traversal.

**SSH password authentication (commented out)**

```bash
# Edit /etc/ssh/sshd_config
sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config
sudo systemctl restart sshd
```

Currently relying on the system default, which may or may not disable passwords. Make it explicit.

**No host-level firewall**

```bash
sudo apt install -y ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw enable
```

Even with Hetzner's external firewall, a host-level firewall provides defense in depth.

**Docker not installed (sandboxing unavailable)**

```bash
sudo apt install -y docker.io
sudo usermod -aG docker clawd
# Then build the sandbox image:
# scripts/sandbox-setup.sh (from the clawdbot/openclaw install)
```

Docker is a prerequisite for [[OpenClaw]]/Clawdbot sandboxing. Without it, all tool execution runs directly on the host.

### systemd Service Hardening

The gateway service unit currently has no security directives beyond environment variables. Adding these restricts what the process can do even if compromised:

```ini
[Service]
# Filesystem isolation
ProtectSystem=strict
ProtectHome=tmpfs
BindPaths=/home/clawd/.clawdbot:/home/clawd/.clawdbot
BindPaths=/home/clawd/clawd:/home/clawd/clawd
BindReadOnlyPaths=/home/clawd/.npm-global:/home/clawd/.npm-global
PrivateTmp=yes

# Privilege restrictions
NoNewPrivileges=yes
RestrictSUIDSGID=yes

# Network (service needs outbound for Telegram, GitHub, OpenAI)
# Cannot restrict network without breaking functionality
# But we can restrict capabilities
CapabilityBoundingSet=
AmbientCapabilities=

# System call filtering
SystemCallArchitectures=native
```

**Note**: These directives need testing. `ProtectHome=tmpfs` with `BindPaths` creates a minimal view of the home directory. If any path is wrong, the service will fail to start. Apply incrementally and test each addition.

### Monitoring

Things worth checking periodically:

- `journalctl --user -u clawdbot-gateway.service` for unexpected errors or access attempts.
- `last` and `lastb` for SSH access history.
- `fail2ban-client status sshd` for ban statistics.
- `apt list --upgradable` to verify unattended-upgrades is working.

## Implementation Order

1. Fix credentials directory permissions (30 seconds, zero risk).
2. Harden SSH config (2 minutes, verify key access first).
3. Install and configure ufw (5 minutes).
4. Run `clawdbot security audit` (informational).
5. Install Docker for sandboxing capability (when ready for that step).
6. Add systemd hardening directives (incrementally, with testing).
