---
title: Paperclip patterns worth adopting for Synthweave
tags:
  - ai-agents
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/paperclip-patterns-worth-adopting-for-synthweave.md
---

# Paperclip patterns worth adopting for Synthweave

**Source:** research/paperclip/analysis.md
**Date:** 2026-03-09

## Worth adopting

1. **Atomic task checkout.** Prevent double work in parallel sub agent runs. Explicit task claiming at the infrastructure level.

2. **Budget/cost tracking.** Per agent, per task, per model cost events. We do not track token costs systematically. Knowing operational costs is valuable.

3. **Heartbeat formalization.** Paperclip's `heartbeat_runs` table tracks status, timing, errors, context snapshots. More rigorous than our HEARTBEAT.md approach. Stuck run detection is particularly useful.

4. **Activity logging.** An immutable audit log of all mutations. Our memory files serve a similar purpose but an append only structured log would strengthen operational awareness.

5. **Agent adapter pattern.** If Loom orchestrates multiple agent runtimes, the adapter registry pattern (type to spawn/connect/stream) is clean and extensible.

## Skip for now

1. **Corporate hierarchy metaphor.** Org charts make sense for 20 agents. Unnecessary for a single creative partnership.
2. **Approval gates.** Our trust based model is better for human agent partnership.
3. **Multi company isolation.** Overkill.
4. **Task only communication.** Our conversational model is richer.
