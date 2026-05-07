---
title: "Hermes Agent Deployment Guide"
tags: [hermes-agent, deployment, infrastructure, configuration, migration]
related:
- hermes-agent
- openclaw
- nous-research
- cloudflare-first-agent-factory
source: research/raw/hermes-deployment-guide.md
---
# Hermes Agent Deployment Guide

## Summary

Deployment reference for Hermes Agent v0.4.0 (v2026.3.23): quick install via curl script, manual install with uv, directory structure, provider configuration, SOUL.md identity, memory system, skills, Telegram gateway, and migration path from OpenClaw.

## Key Claims

1. **Quick Install:** `curl -fsSL install.sh | bash` handles Python 3.11 (uv), Node.js v22, ripgrep, ffmpeg, repo clone, venv, global `hermes` command.
2. **Directory Structure:** `~/.hermes/` contains config.yaml, .env, SOUL.md, memories/, skills/, cron/, sessions/, logs/. Identity and memory live in ~/.hermes/, not workspace.
3. **Memory System:** MEMORY.md (agent notes, 2,200 char limit) + USER.md (user profile, 1,375 char limit). Injected as frozen snapshot at session start. Changes persist to disk but don't appear until next session.
4. **Skills:** Compatible with agentskills.io open standard. Bundled, hub-installed, agent-created, or custom SKILL.md files. Progressive disclosure pattern (list > view > detail).
5. **Gateway:** `hermes gateway` runs foreground or as systemd service. Sessions reset daily at 4:00 AM or on idle timeout. Security: deny all users not in allowlist.

## Migration from OpenClaw

`hermes claw migrate` imports SOUL.md, memories, skills, API keys, sessions, cron, and configuration with dry-run preview.

## Related

- [[hermes-agent]] — Platform overview
- [[openclaw]] — Migration source
- [[nous-research]] — Organization behind Hermes
- [[cloudflare-first-agent-factory]] — Alternative deployment architecture
