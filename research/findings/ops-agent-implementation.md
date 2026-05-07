---
title: "Operations Agent: Implementation Plan"
tags: [finding, ops-agent, implementation, multi-agent, cron, monitoring]
related: [[agent-native-operations]], [[agent-memory]], [[context-stack]], [[subagent-architecture]]
source: research/raw/ops-agent-implementation.md
ingested: 2026-05-07
---

# Operations Agent: Implementation Plan

The decision to create the first specialist agent (Ops), based on six weeks of operational data showing a pattern: Sivart is strong at vision and weak at operational follow-through.

## Key Points

**Why Ops first.** Five consecutive days of "nothing proactive" in daily growth reflections. Steve's email unread for 5 days. Cron delivery errors compounding silently. Commits on stale branches. The pattern is operational drift, not capability gaps. An Ops agent addresses the root cause.

**Lessons from training Sivart to apply.**
- AGENTS.md + SOUL.md + memory pattern works. Use the same architecture.
- Start lean: ~100 lines, not 500+. Let complexity emerge from need.
- Radio silence default: not every message needs a response.
- Verify before acting: check actual state, not summaries.
- Daily notes are essential: memory files survive session boundaries.
- Process documentation prevents drift: write it down or it doesn't exist.

**Lessons to avoid.**
- Don't over-prescribe personality: SOUL.md evolves through experience.
- Don't give too much scope: the Ops agent owns operations. Period.
- Don't make it chatty: report findings, not feelings.
- Don't skip evals: metrics from day one.
- Don't trust "it's working" without checking.

**Architecture.** OpenClaw multi-agent config: Agent ID `ops`, workspace `/home/clawd/ops-agent`, model Opus (upgraded from Sonnet per Ξ2T: "giving her access to the best brain possible"), heartbeat disabled, tools restricted (read, exec, cron, memory_search, memory_get, session_status), no direct channel access. Reports via announce to Sivart's session. Sivart is the interface to Ξ2T.

**Four-phase rollout.** Phase 1 (Foundation): create workspace, add to config, create initial cron job, verify boots. Phase 2 (Core Checks): email monitoring, cron health, infrastructure health, git hygiene, TODO.md staleness. Phase 3 (Refinement): tune check frequency, add runbooks, establish baselines. Phase 4 (Autonomy): agent updates its own SOUL.md, safe auto-remediation, pattern detection.

**Metrics from day one.** Missed issues (things Sivart/Ξ2T catch that ops should have): target 0/week. False alarms: target <2/week. Detection latency: target <24h. Report quality (actionable without follow-up): target >90%. Cost: track, no target yet.

## Relevance

The Ops agent is the first specialist in the crew. This document is the blueprint for adding future agents: auditor, builder, researcher. The pattern (separate workspace, restricted tools, cron-driven, Sivart-mediated) is replicable.

## Related

- [[agent-native-operations]] -- Executive layer and agent communication model
- [[agent-memory]] -- Memory architecture for cross-session continuity
- [[context-stack]] -- Where identity and protocols are encoded
- [[subagent-architecture]] -- Technical capabilities and parameters
