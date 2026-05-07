---
title: "Building the Team: Specialized Agents for Sivart"
tags: [research, agents, ops, verification, review, team-building]
related: [agent-native-operations, symphony-orchestrator, workflow-as-contract, progressive-autonomy, kanban-doctrine, creative-partnership, chief-of-staff-model]
source: "Research notes from February 13, 2026"
---

# Building the Team: Specialized Agents for Sivart

## Summary

Week 2 feedback from Ξ2T indicated sloppy execution: stale summaries, template noise, email neglect, sync drift, multiple iterations. Root cause pattern: verification failures — acting on assumptions instead of checking state. Proposed specialized agents to solve each failure class.

## Failure Pattern Analysis

| Failure Type | Root Cause | Frequency |
|-------------|------------|-----------|
| Acting on stale data | Trusted summary over reality | High |
| Maintenance neglect | Background tasks fall off when not forced | Medium |
| Process drift | Knowing what to do, not doing it | Medium |
| Incomplete verification | Claiming done without checking | High |

## Proposed Agent Specializations

### 1. Ops Agent (Highest Priority)

**Purpose:** Handle recurring operational tasks autonomously. Run daily without being asked.

**Responsibilities:** Email triage, blog/source sync check, version monitoring, heartbeat state maintenance, inbox zero enforcement.

**Implementation:** Isolated cron job, runs at 06:00 UTC. Reports anomalies only. Radio silence default.

**Success Metrics:** Email check gaps from 10 days → 0 days. Sync drift caught within 24h. Zero manual reminders needed.

### 2. Verifier Agent (Second Priority)

**Purpose:** Check reality before acting. "Trust but verify" function.

**Responsibilities:** Before creating PR: does this work already exist? Is the branch stale? Before claiming done: does the file exist? Does git log confirm? Before working from summary: is the summary accurate?

**Implementation:** Pre-action hook or dedicated sub-agent invoked before major actions.

**Success Metrics:** Duplicate/empty PRs → 0. Work based on stale summary → 0.

### 3. Review Agent (Third Priority)

**Purpose:** Quality check before work reaches Ξ2T.

**Responsibilities:** Review PRs for description/change alignment, template correctness, style drift, checklist completeness.

**Success Metrics:** Back-and-forth iterations from 2-3 per task → 0-1. Template noise issues → 0.

## Alternative: State Manager

Instead of Verifier as separate agent, maintain canonical ground truth:
- Updated after every merge/close
- Query instead of trusting summaries
- Single source of truth that survives compaction

## Implementation Recommendations

1. **Start with Ops Agent only** (clearest scope, isolated, won't break anything)
2. **Run for 2 weeks minimum** before adding another
3. **Track metrics from day one**
4. **Kill switch** — disable immediately if causing more problems than solving
5. **Weekly review** — are metrics improving? Is complexity justified?

## Complexity Risks

- More moving parts = more failure modes
- Agent coordination overhead
- Cost of additional API calls
- Debugging becomes harder

Mitigation: one agent at a time, minimum 2-week stabilization periods, metrics-driven decisions.

## Connection to Agent Factory

This document operationalizes the [[progressive-autonomy]] principle: start with the lowest-risk automation (background maintenance), validate with metrics, then expand. The [[symphony-orchestrator]] pattern provides the coordination framework. [[workflow-as-contract]] defines the agent behavior contracts.

## Related

- [[agent-native-operations]] — Tools designed for AI-human partnership
- [[symphony-orchestrator]] — Coordination framework for agent teams
- [[workflow-as-contract]] — Versioned agent behavior contracts
- [[progressive-autonomy]] — Gradual trust increase with validation gates
- [[kanban-doctrine]] — Auftragstaktik alignment for agent dispatch