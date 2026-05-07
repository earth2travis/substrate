---
title: "Paperclip Deployment & Configuration Guide"
tags: [research, deployment, paperclip, agents]
related: [agent-native-operations, agent-factory-production-system, clanker-agent-deployment-patterns, hermes-deployment-guide]
source: "github.com/paperclipai/paperclip source code analysis"
---

# Paperclip Deployment & Configuration Guide

## Summary

Paperclip deploys as an interactive onboarding wizard (`npx paperclipai onboard`) using @clack/prompts. Supports quickstart (sensible defaults, auto-detects env vars) and advanced (per-section prompts) modes. Default config lives at `~/.paperclip/instances/default/paperclip.json`.

## Key Concepts

**Config Architecture:**
- `$meta`: version, updatedAt, source
- `llm`: provider (claude|openai), apiKey
- `database`: embedded-postgres or external postgres with backup config
- `server`: deploymentMode (local_trusted|authenticated), exposure (private|public), host, port
- `storage`: local_disk or s3
- `secrets`: local_encrypted, env, etc. with strictMode
- `auth`: baseUrlMode, publicBaseUrl

**Company Model:**
Paperclip models AI organizations as companies with agents (roles, hierarchy, adapters), projects, issues, goals, and approvals. CEO is root of org chart. Agents can create sub-agents with `canCreateAgents` permission.

**OpenClaw Gateway Adapter:**
Connects via WebSocket (not HTTP). Challenge-response handshake with Ed25519 device auth. Sends wake text to OpenClaw with task context. OpenClaw agent claims API key and calls Paperclip REST API directly.

**Key Environment Variables:**
`DATABASE_URL`, `PORT`, `HOST`, `PAPERCLIP_PUBLIC_URL`, `PAPERCLIP_DEPLOYMENT_MODE`, `PAPERCLIP_AGENT_JWT_SECRET`, `PAPERCLIP_STORAGE_PROVIDER`, `PAPERCLIP_SECRETS_PROVIDER`

## Applications

Full REST API surface for companies, agents, issues, heartbeat runs, projects, goals, approvals, secrets, labels. Auto-wakeup on issue assignment. Checkout/release flow for agent task claiming. [[agent-native-operations]] [[agent-factory-production-system]]
