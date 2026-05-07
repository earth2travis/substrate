---
title: "28 Painful Mistakes Building Agent Systems"
tags: [agents, failure-modes, operations, lessons-learned]
related:
- agent-skills-as-onboarding
- five-whys
source: research/raw/28-openclaw-mistakes-kloss.md
---
# 28 Painful Mistakes Building Agent Systems

## Summary

Practitioner report from three weeks of intensive OpenClaw development. Core failure mode: gaps between what was planned and what was enforced at runtime. Fix is a closed loop: load context before responding, back claims with evidence, enforce rules via scripts not docs.

## Key Metrics

- Rules as documentation: ~48% compliance
- Rules as scripts: ~100% compliance

## Critical Patterns

**Hierarchy prevents chaos.** Agents without chain of command produce context thrashing and conflicting changes. Main session orchestrates, domain agents dispatch, subagents execute bounded tasks. Mixing agent identity with temporary compute burns tokens.

**Ownership before parallelization.** Four agents spawned on same files without ownership definitions produced conflicting changes. Define ownership explicitly before parallel dispatch.

**Atomic scope.** Handing five problems at once yields half-assed work on each. One problem per agent. Called the "single biggest recent improvement to execution quality."

**Evidence gates before "done."** Before marking complete: repo + branch, commit hash, files changed, verification that changes work, artifact for UI. "If you take one thing from this entire article, take this."

**Write first, speak second.** Agent says complete but state never written; next session treats it as not done. Persist to disk before reporting completion.

**Cron hygiene.** Half of cron jobs produce no value but consume resources. Standard format: what happened, why it matters, what's next, confidence 0-100, evidence. No output and nothing to report are different signals.