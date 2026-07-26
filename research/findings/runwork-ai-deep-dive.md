---
title: "Runwork.ai: The Shared Capability Layer Under Every Team Agent"
tags: [finding, runwork, adoption, onboarding, skills, mcp, team-ai, agent-native, synthweave, competitive-landscape]
related:
- agent-native-operations
- skills-as-portable-knowledge
- institutional-ai-redesign
- context-stack
- integration-day-onboarding-frame
- centaur-principle
source: research/raw/runwork-ai-deep-dive.md
ingested: 2026-07-26
---
# Runwork.ai: The Shared Capability Layer Under Every Team Agent

## Summary

Runwork is a shared AI workspace for teams, built on a diagnosis most AI-adoption vendors skip: companies bought AI tools (ChatGPT seats, Claude Code, Cursor) but none of it connects, nothing compounds, and nobody can see who is actually getting better at AI. Runwork sells the missing layer: shared capability. Setup, company context, skills, workflows, and adoption analytics live in one cloud workspace and sync into every AI tool every teammate uses. Taglines: "Teach your AI once. Everyone's AI knows it." Full support for Claude Code/Desktop, Cursor, Codex, Windsurf, Cline, Gemini CLI, and Antigravity; MCP-only for ChatGPT; claims 60+ tools. Founded by Oytun Tez (previously MotaWord co-founder); launched Dec 2025, 32 releases and 125 features by June 2026. Captured from the full marketing site (two passes, including 22 JS-rendered pages) on 2026-07-24. It is the closest existing product to Synthweave's concierge onboarding motion, and the changelog shows it racing directly toward that overlap.

## The Capability Map

- **Onboarding as a guided journey.** A Tauri desktop app runs a resumable 14-scene flow: scan the machine, detect installed AI tools, install what is missing, configure each with team skills/MCP/settings without clobbering personal config. Ends at a hub dashboard with live activity feed and sync-status tray icon. CLI equivalent (`runwork setup --agent claude-code`, `runwork doctor`) for engineers. Admin side tracks the funnel: Invited / Desktop Installed / Setup Complete / Active, with recommended actions per stuck member.
- **Adoption measurement as product.** "My Journey" scores each member 0-100 across Setup, Usage, Building, Knowledge against the team average. A capability map (grounded in learning science: retention curves, zone of proximal development, explicitly not gamification) marks skills mastered / ready-next / upcoming. Skill decay fades unexercised capabilities and triggers nudges. Next-best-step guidance is persona-aware: everyday, curious, and engineer personas each have their own definition of "fully adopted"; an ops person can hit 100% without ever building an app. Weekly personalized training emails, team-champion surfacing, and `runwork reflect`: a privacy-safe weekly digest (user messages and tool taxonomy only, assistant output dropped) that spots repeated manual work and suggests saving it as a skill.
- **Skills as the compounding asset.** Every app auto-generates a SKILL.md from its registered capabilities at runtime; users layer editable domain knowledge on top. Skills sync to every teammate's agent, load via slash commands (multiple simultaneously for cross-app orchestration), export portably, and import from external registries (skills.sh, MCP Registry) with domain-allowlisted HTTP tools.
- **MCP as universal adapter, both directions.** Every workspace exposes one aggregate MCP server; every app gets its own per-app MCP server with full read/write. The MCP client imports external servers with auto-discovery and rate limiting. Everything built for a client is MCP-exposed by default.
- **Share and Resume.** Native byte-for-byte session transplant between same-family agents (Claude Code to Cowork, Codex CLI to Desktop), with a universal Markdown-transcript fallback for any MCP-speaking agent. Conversation inbox with auto-titles, intent metadata, suggested next steps. Handoff as the mechanism by which good patterns spread.
- **The workspace substrate.** Natural-language full-stack apps, multi-day workflows with human-in-the-loop approvals, durable cron schedules, webhook automations, a shared entity graph as one data model across all apps, 3,200+ integrations, presigned-URL storage, public REST APIs, n8n import (8,000+ community recipes converted into full apps), git versioning with rollback, immutable audit logs, RBAC. SOC 2 and SSO both "soon."
- **Economics.** $79/$379/$979 per month tiers plus Enterprise; additional seats $29. AI is BYOK by default and does not draw credits; usage credits meter only integration calls and agent runtime. Warnings at 75%/90%, then pause, no surprise bills. Post-trial workspaces pause read-only rather than deleting.

## Why It Matters for Substrate's Thesis

Runwork is a commercial proof point for several concepts already in the graph:

1. **Client context as managed, versioned, synced objects.** Team instructions and per-agent instruction overrides in markdown, pushed to every configured agent and editable centrally, is exactly how [[context-stack]] files (CLAUDE.md, AGENTS.md, SOUL.md) should be treated: not one-time bootstrap artifacts but living synced state.
2. **Skills as the owned deliverable.** Auto-generated capability docs plus human-authored domain knowledge, portable via SKILL.md, synced fleet-wide: a concierge engagement should leave the client owning a skill library, not just a configured agent. Direct support for [[skills-as-portable-knowledge]].
3. **Onboarding never ends; it decays and renews.** Skill-decay nudges and weekly next-best-step coaching reframe onboarding as a continuous capability practice, extending the five-beat arc of [[integration-day-onboarding-frame]] into a subscription motion. A scheduled agent that reviews usage, finds the frontier skill, and coaches one step per week is the post-onboarding engagement model.
4. **Adoption analytics as retention engine.** The funnel telemetry (who is stuck where, with a named next action) is both the internal operator dashboard and the client-facing proof of value. This is the demand-side instrumentation that [[institutional-ai-redesign]] argues organizations lack.
5. **Reflection-driven capture.** An agent that notices repeated manual patterns and offers "save as skill" converts onboarding into a growing asset library: the compounding-value story, and a concrete [[centaur-principle]] mechanism (process improvement captured from actual use, not imposed from above).

## Competitive Reading

Runwork's /compare/ page frames it as "the 2026 way to vibe-code business software" against DIY stacks, general chat tools, internal-tool builders, AI app generators, automation platforms, and workspace suites, and notably compares against [[openclaw]] directly. Its unique angle is the shared team layer under every agent: shared skills, one-time integration connections, cross-agent conversation handoff, adoption dashboards, MCP-native architecture. Gaps and risks from our side: vendor self-description only (no independent reviews captured), SOC 2/SSO pending, and the June 2026 shipping sequence (adoption, spend, BYOK) signals active convergence on the concierge overlap zone.

## Connections

- [[agent-native-operations]] — the shared capability layer is what agent-native tooling looks like at team scale.
- [[skills-as-portable-knowledge]] — skills as the compounding, portable, client-owned asset.
- [[institutional-ai-redesign]] — adoption analytics as the missing organizational instrumentation.
- [[context-stack]] — instruction files as managed, synced, versioned objects rather than bootstrap artifacts.
- [[integration-day-onboarding-frame]] — the five-beat concierge arc extended into continuous onboarding.
- [[centaur-principle]] — reflection-driven skill capture as process improvement from actual use.
