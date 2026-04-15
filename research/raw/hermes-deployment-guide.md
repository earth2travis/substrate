# Hermes Agent Deployment Guide for Koda

**Filed:** 2026-03-27
**Purpose:** Deployment reference for installing Hermes Agent on Koda's dedicated server (5.78.80.86)
**Version:** v0.4.0 (v2026.3.23), released March 23, 2026

---

## 1. Current Release: v0.4.0

Released 3 days ago. Major highlights relevant to us:

- **OpenAI compatible API server**: Exposes /v1/chat/completions endpoint, plus /api/jobs REST API for cron management
- **6 new messaging adapters**: Signal, DingTalk, SMS (Twilio), Mattermost, Matrix, Webhook (joins Telegram, Discord, WhatsApp, Slack, Email, Home Assistant)
- **Gateway prompt caching**: Preserves Anthropic prompt cache across turns for cost savings
- **Context compression overhaul**: Structured summaries with iterative updates
- **Streaming enabled by default**
- **MCP server management CLI**: `hermes mcp` commands with OAuth 2.1 PKCE
- **@ context references**: Claude Code style @file and @url injection
- **200+ bug fixes**

## 2. Installation

### Quick Install (recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Installer handles: Python 3.11 (via uv), Node.js v22, ripgrep, ffmpeg, repo clone, venv, global `hermes` command, provider config. Only prereq is `git`.

### Manual Install (condensed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone --recurse-submodules https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
uv venv venv --python 3.11
export VIRTUAL_ENV="$(pwd)/venv"
uv pip install -e ".[all]"
npm install  # optional, for browser tools and WhatsApp

mkdir -p ~/.hermes/{cron,sessions,logs,memories,skills,pairing,hooks,image_cache,audio_cache,whatsapp/session}
cp cli-config.yaml.example ~/.hermes/config.yaml
touch ~/.hermes/.env

mkdir -p ~/.local/bin
ln -sf "$(pwd)/venv/bin/hermes" ~/.local/bin/hermes
```

### Post Install

```bash
source ~/.bashrc
hermes version
hermes doctor
hermes model    # configure provider
hermes tools    # configure toolsets
```

## 3. Directory Structure

```
~/.hermes/
├── config.yaml     # Settings (model, terminal, TTS, compression, etc.)
├── .env            # API keys and secrets
├── auth.json       # OAuth provider credentials
├── SOUL.md         # Agent identity (slot #1 in system prompt)
├── memories/       # Persistent memory (MEMORY.md, USER.md)
├── skills/         # Agent created and installed skills
├── cron/           # Scheduled jobs
├── sessions/       # Gateway sessions
└── logs/           # Logs (secrets auto redacted)
```

## 4. Configuration for Koda

### Provider Setup

For Anthropic (our primary):
```bash
# Option 1: API key
echo 'ANTHROPIC_API_KEY=sk-ant-...' >> ~/.hermes/.env

# Option 2: Claude Code auth (if available)
hermes model  # select Anthropic
```

### SOUL.md

Koda's SOUL.md already exists at `/home/clawd/koda/SOUL.md`. Copy to `~/.hermes/SOUL.md` on the new server. This is slot #1 in the system prompt, the agent's primary identity.

Key: Hermes only loads SOUL.md from ~/.hermes/, NOT from the working directory.

### Memory System

Two files in `~/.hermes/memories/`:
- **MEMORY.md**: Agent's personal notes (2,200 char limit, ~800 tokens)
- **USER.md**: User profile (1,375 char limit, ~500 tokens)

Memory is injected as a frozen snapshot at session start. Changes during a session persist to disk but don't appear in the prompt until next session.

### Skills

Skills live in `~/.hermes/skills/`. Compatible with agentskills.io open standard. Progressive disclosure pattern (list > view > detail) minimizes token usage.

Skills can be:
- Bundled (copied on fresh install)
- Installed from hub: `hermes skills install <path>`
- Agent created during use
- Custom SKILL.md files

## 5. Messaging Gateway (Telegram)

```bash
hermes gateway setup  # interactive platform config
```

For Telegram specifically:
```
TELEGRAM_BOT_TOKEN=...
TELEGRAM_ALLOWED_USERS=...  # restrict access
```

Gateway commands:
```bash
hermes gateway              # run foreground
hermes gateway install      # install as systemd user service
hermes gateway start/stop   # manage service
hermes gateway status
```

### Session Management

Sessions reset based on configurable policies:
- Daily reset (default: 4:00 AM)
- Idle reset (default: 1440 min)
- Per platform overrides in `~/.hermes/gateway.json`

### Security

Default: deny all users not in allowlist. DM pairing available as alternative:
```bash
hermes pairing approve telegram <code>
hermes pairing list
hermes pairing revoke telegram <user_id>
```

## 6. Key Differences from OpenClaw

| Feature | OpenClaw | Hermes |
|---------|----------|--------|
| Language | Node.js/TypeScript | Python |
| Config | JSON (openclaw.json) | YAML (config.yaml) + .env |
| Identity | SOUL.md (in workspace) | SOUL.md (in ~/.hermes/) |
| Memory | MEMORY.md (manual, in workspace) | MEMORY.md + USER.md (tool managed, in ~/.hermes/memories/) |
| Memory limits | Unlimited (manual curation) | 2,200 + 1,375 chars (enforced) |
| Skills | SKILL.md (in workspace/skills/) | SKILL.md (in ~/.hermes/skills/, agentskills.io compatible) |
| Gateway | Built in | Separate `hermes gateway` process |
| Service | systemd user service | systemd user or system service |
| Migration | N/A | `hermes claw migrate` built in |

## 7. Migration Path

Hermes has a built in `hermes claw migrate` command for transitioning from OpenClaw. This could be useful for migrating Koda's existing config.

## 8. Deployment Checklist for Koda's Server

- [ ] Server hardened (see koda-server-hardening issue)
- [ ] Git installed
- [ ] Hermes installed via quick install script
- [ ] `hermes doctor` passes
- [ ] Anthropic API key configured in ~/.hermes/.env
- [ ] SOUL.md deployed to ~/.hermes/SOUL.md (from Koda's existing identity)
- [ ] USER.md created in ~/.hermes/memories/ (describing Ξ2T)
- [ ] Telegram bot created for Koda
- [ ] Gateway configured with Telegram adapter
- [ ] Gateway installed as systemd service
- [ ] GitHub PAT configured (for MCP or direct git ops)
- [ ] Skills installed/configured as needed
- [ ] Cron jobs configured for autonomous behavior
- [ ] Test conversation verified
- [ ] Memory persistence verified across sessions

## 9. Sources

- [Hermes Docs](https://hermes-agent.nousresearch.com/docs/)
- [GitHub Releases](https://github.com/NousResearch/hermes-agent/releases)
- [Installation Guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
- [Configuration Guide](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
- [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging)
- [Memory System](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)
- [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [Personality & SOUL.md](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality)
- Previous research: `research/agents/hermes-self-evolution.md`
