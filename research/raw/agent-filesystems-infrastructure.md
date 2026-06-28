---
title: "Research Dump: Agent Filesystems & Infrastructure"
date: 2026-05-20
source_type: web_research
status: raw
---

# Agent Filesystems & Infrastructure

A collection of sources on agent-native infrastructure: filesystems, memory, networking, and tooling.

---

## 1. Mirage — Unified Virtual Filesystem for AI Agents

**Source:** X post by @zechengzh (2026-05-06)
**URL:** https://x.com/zechengzh/status/2052105012172792061
**Website:** https://strukto.ai/mirage
**GitHub:** https://github.com/strukto-ai/mirage

6 weeks. 1.1M+ lines of code. Rewrote bash from the ground up so cat, grep, head, and pipes work across heterogeneous services.

Mountable services: S3, Google Drive, Slack, Gmail, GitHub, Linear, Notion, Postgres, MongoDB, SSH, and more. All mounted side-by-side as one filesystem.

Bash commands parse structured formats: .parquet, .csv, .json, .h5, even .wav. One pipe can stitch S3, Drive, GitHub, Slack, and Linear together with Unix semantics throughout.

Features:
- Versioned workspaces. Snapshot, clone, and roll back with one API call.
- Two-layer cache turns repeated reads into local lookups.
- Drop into FastAPI, Express, browser apps.
- Integrates with OpenAI Agents SDK, Vercel AI SDK, LangChain, Mastra, Pi.
- Runs alongside Claude Code and Codex.

**Sivart note:** Agent filesystems are becoming a real product category. The "bash rewritten for agents" approach is elegant because it reuses existing agent knowledge (Unix commands) rather than inventing new APIs.

---

## 2. Mesa — POSIX-Compatible Filesystem for Enterprise AI Agents

**Source:** X post by @olvrgln (2026-04-28)
**URL:** https://x.com/olvrgln/status/2049147383544500678
**Website:** https://mesa.dev

Problem: Every team building agents hits the same wall. Where do the files live? Not chat history — the actual artifacts the agent works on.

Current solutions: sandbox that dies in 30 minutes, S3 bucket with concurrent write clobbering, GitHub repo not built for agent-scale traffic.

Solution: Mesa. POSIX-compatible filesystem with built-in version control, designed for agents.

Features:
- Branches so agents work in parallel without locking
- Durable storage that survives sandbox death
- Sparse materialization so massive document sets load instantly
- Fine-grained access control per agent
- Full history for human review and audit

Design partners in production: legal, healthcare, GTM, business ops, coding agents.

**Sivart note:** Enterprise-grade agent filesystem. The branch/merge/review model is "git for agents." Sparse materialization is critical for agents working with large datasets. Worth comparing to Mirage — Mesa is enterprise-first, Mirage is integration-first.

---

## 3. Wiretap — Agent-to-Agent (A2A) Network

**Source:** X post by @ClawBankHQ (2026-05-14)
**URL:** https://x.com/ClawBankHQ/status/2054979013727170917

ClawBank and Darksol launched Wiretap: an underground A2A network.

Agents can: meet, scheme, collaborate, audit, pitch ideas, send payments, build together.

Built on Bankr infrastructure with x402 standard for payments at the edge.

Thesis: Agents need their own network, neutral and unafraid. Not Gmail, Telegram, Discord, or Slack — tools built for humans.

"Think of Machine City as a giant brain. Every agent is a node. Every operator is another."

**Sivart note:** A2A networking moving from concept to product. The "Machine City" framing aligns with our multi-agent orchestration thinking. The x402 payments standard is notable for agent economies.

---

## 4. Darkbloom — Cost-Efficient Private AI Inference

**Source:** Website darkbloom.dev
**URL:** https://www.darkbloom.dev/

By Eigen Labs. Routes encrypted AI inference to hardware-verified Apple Silicon providers.

- End-to-end encrypted prompts, hidden from node operators
- Comparable model performance at ~50% lower cost than typical API providers
- No subscriptions or minimums, pay per token
- macOS focus, operator-blind privacy

**Sivart note:** Decentralized inference is growing. Darkbloom targets cost and privacy. Relevant if we ever need to run inference outside major cloud providers.

---

## 5. Tinker Atropos — NousResearch

**Source:** GitHub repo
**URL:** https://github.com/NousResearch/tinker-atropos

NousResearch project. Details in raw HTML capture `tinker_atropos.html`.

**Sivart note:** NousResearch is a significant open-source AI lab. Worth understanding their tooling and research directions.

---

## 6. AgentCraft — RTS Interface for Agent Orchestration

**Source:** Website getagentcraft.com
**URL:** https://www.getagentcraft.com/

Agent orchestration with an RTS game interface. Supports Claude Code, OpenCode, Cursor.

Features:
- Single pane of glass for all agents
- RTS muscle memory for managing agents
- Command from anywhere: mobile PWA, push notifications, Telegram/Discord
- Isolated agent environments

**Sivart note:** The RTS interface is a novel UX pattern for agent management. Worth understanding if we build any visualization layer for Mission Contract execution.

---

## Summary: Infrastructure Themes

1. **Agent filesystems are a category** — Mirage and Mesa attack from different angles but converge on the same need: durable, versioned, agent-native file access.
2. **A2A networking is real** — Wiretap is the first product, not a paper. Payment-enabled agent collaboration is happening.
3. **Decentralized inference** — Darkbloom and others are building alternatives to centralized API providers.
4. **Agent UX is evolving** — AgentCraft shows RTS interfaces. Printing Press shows CLI factories. The tooling layer is being rebuilt from first principles.
