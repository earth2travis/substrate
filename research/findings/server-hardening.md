---
title: "Server Hardening Checklist"
tags: [security, server, hardening, ssh, firewall, docker, systemd, ops]
related:
- agent-security
- open-source-governance
- github-as-knowledge-graph
- lean-doctrine
source: research/raw/server-hardening.md
---
# Server Hardening Checklist

Server: Hetzner CPX11, Ubuntu 24.04, Ashburn VA.

## Current State (Good)

- **fail2ban:** active. Protects SSH against brute force attacks
- **unattended-upgrades:** active. Security patches applied automatically
- **Home directory permissions:** 750 (owner and group only)
- **Clawdbot state directory:** 700 (owner-only)
- **Config and auth files:** 600 (properly locked)
- **Gateway binding:** loopback only (127.0.0.1:18789). Not exposed to network
- **Telegram DM policy:** pairing (default). Unknown senders gated

## What Needs Fixing

**1. Credentials directory permissions (775 → 700)**
```bash
chmod 700 ~/.clawdbot/credentials/
```
Files within are 600, but the directory allows group and world traversal.

**2. SSH password authentication (make explicit)**
```bash
sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config
sudo systemctl restart sshd
```
Currently relying on system defaults.

**3. No host-level firewall**
```bash
sudo apt install -y ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw enable
```
Defense in depth even with Hetzner's external firewall.

**4. Docker not installed (sandboxing unavailable)**
```bash
sudo apt install -y docker.io
sudo usermod -aG docker clawd
```
Docker is prerequisite for OpenClaw/Clawdbot sandboxing.

## systemd Service Hardening

Recommended directives for the gateway service unit:
```ini
[Service]
ProtectSystem=strict
ProtectHome=tmpfs
BindPaths=/home/clawd/.clawdbot:/home/clawd/.clawdbot
BindPaths=/home/clawd/clawd:/home/clawd/clawd
BindReadOnlyPaths=/home/clawd/.npm-global:/home/clawd/.npm-global
PrivateTmp=yes
NoNewPrivileges=yes
RestrictSUIDSGID=yes
CapabilityBoundingSet=
AmbientCapabilities=
SystemCallArchitectures=native
```
Apply incrementally and test each addition.

## Monitoring

- `journalctl --user -u clawdbot-gateway.service` for errors and access attempts
- `last` and `lastb` for SSH access history
- `fail2ban-client status sshd` for ban statistics
- `apt list --upgradable` to verify unattended-upgrades

## Implementation Order

1. Fix credentials directory permissions (30 seconds, zero risk)
2. Harden SSH config (2 minutes, verify key access first)
3. Install and configure ufw (5 minutes)
4. Run security audit
5. Install Docker for sandboxing
6. Add systemd hardening directives (incrementally, with testing)
