---
title: 28 Painful Mistakes Building Agent Systems
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[5-whys]]
  - [[a3-thinking]]
  - [[accounting-bookkeeping-research]]
source: research/raw/28-openclaw-mistakes-kloss.md
---

# 28 Painful Mistakes Building Agent Systems

**Source:** [@kloss_xyz](https://x.com/kloss_xyz/status/2032011756890177552) (March 2026)
**Filed:** 2026-03-11
**Context:** 3 weeks of intensive OpenClaw system development. Practitioner report, not theory.

## Executive Summary

The core failure mode: **gaps between what was planned and what was enforced at runtime.** Made worse by importing external configs without auditing against existing setup ("context poisoning"). The fix is a closed loop: load context before responding, back claims with evidence, enforce rules via scripts not docs, and ensure health scores reflect current reality.

Key metric: Rules as documentation = ~48% compliance. Rules as scripts = ~100%.

## The 28 Mistakes, Categorized

### Routing & Triggers (1)

**1. Loose word matching fires wrong actions.** Words like "go" and "proceed" appear in normal conversation. Fix: exact whole-word matching, explicit triggers. Test with weird inputs, not just happy paths.

### Agent Architecture & Hierarchy (2, 5, 7)

**2. Agents without hierarchy = expensive chaos.** Context thrashing, no ownership, conflicting changes. Fix: real chain of command. Main session orchestrates. Domain agents dispatch. Subagents execute bounded tasks. Agents have durable identity; subagents are temporary compute. Mixing them burns tokens.

**5. Parallel agents on same files without ownership.** 4 agents spawned, 2 overlapped on same files, conflicting changes, neither flagged it. Fix: define ownership before parallelizing. Make it explicit.

**7. Multi-problem asks produce garbage.** Handing 5 problems at once = half-assed work on each. One problem per agent. Atomic scope, clean output. "Single biggest recent improvement to execution quality."

### Handoffs & Communication (3, 6)

**3. Handoffs without structured context degrade like telephone.** Must carry: who sent it, what the task is, when dispatched, where results go, what evidence exists. Tightening handoff format immediately improved output quality.

**6. Agent going silent kills trust.** Worst wait: ~10 minutes from a timed-out process blocking the message channel. Fixes: (a) fast ack before real work, (b) long-running work in separate sessions so it doesn't block the conversation channel.

### Persistence & Memory (8, 11, 12)

**8. Session death loses unsaved work.** Agent times out at minute 14, work was going to commit at minute 15. Fix: commit incrementally. Small commits, frequent saves. Don't gamble on session survival.

**11. Corrections vanish between sessions.** Same wrong assumption corrected 3 times in one day. Fix: decisions.md loaded at session start. Every redirect, deprioritization, or "stop doing that" written to file immediately with a date. Missing daily logs cause the system to rediscover solved problems.

**12. Phantom progress: "done" but no record on disk.** Agent says complete, state never written, next session treats it as not done. Fix: write first, speak second. Persist state to file before telling the human anything.

### Verification & Evidence (9, 13, 14, 19)

**9. "Done" without receipts is worthless.** Built an evidence gate. Before marking done: repo + branch, commit hash, files changed, verification that changes work, screenshot/artifact for UI. "If you take one thing from this entire article, take this."

**13. Agent confidently reports false information.** CLI summaries treated as truth. "No agents running" when agents were running. Fix: CLI summaries are views, not truth. Source files are truth. Confidence is not accuracy.

**14. "File doesn't exist" when it does.** Wrong path or incomplete directory listing. Fix: inventory scripts that count what actually exists on disk. Anti-hallucination tooling.

**19. Narrative updates are unverifiable.** "Things are looking good" tells you nothing. Fix: structured reports with explicit pass/fail. Machine-readable JSON + human-readable markdown for every major report.

### Cron & Scheduling (10, 15, 16, 17)

**10. Polling loops waste context.** Checking "is it done?" every 5 seconds for 10 minutes = 120 status checks, zero information. One cron job timed out 8 times in a day from retrying with no backoff. Fix: wait for events, escalate on timeout.

**15. Half your cron jobs make things worse.** Jobs producing no value but consuming resources, cluttering channels, confusing the system. Fix: cut ruthlessly. If you wouldn't read or act on the output, kill the job.

**16. Noisy cron jobs steal attention.** Standard format for all output: what happened, why it matters, what's next, confidence (0-100), evidence. Nothing to report = clean ack, not silence. "No output" and "nothing to report" are different signals.

**17. Running same cron job twice simultaneously.** Two processes competing over same state. Old and new policies applied simultaneously. Fix: trust the active loop. Fix it, don't run a parallel one. Let fixes soak for a full cycle before re-enabling disabled jobs.

### Configuration & Change Management (4, 21, 22, 28)

**4. Rules in wrong order waste days.** Correct sequence: (1) core identity files, (2) routing rules, (3) language/communication contracts, (4) stress tests. Each step depends on previous being stable.

**21. Deploy in advisory mode first.** 13 formal standards all run in read-only "what would happen" mode before enforcement. Fix problems before touching production. "One of the biggest wins of the entire last 3 weeks."

**22. Change settings without saving old ones.** 54 config files, 200+ risky values. Fix: snapshot before every change, no exceptions. Recovery without snapshots takes 10x longer.

**28. Fixing all security issues at once is a trap.** Credentials in wrong places, mismatched accounts, secrets in logs. Fix one at a time, in order, with snapshot and rollback plan at each step. Phased hardening with checkpoints.

### Rule Enforcement (23, 25)

**23. Agent violates rules it cites in the same session.** "Investigate before concluding" in 3 files, violated in session where it was cited. Fix: mechanical gate that loads context before responding. Not a suggestion; a script that cannot be skipped. **Documentation rules: ~48% compliance. Script-enforced rules: ~100%.** "Every mistake in your agent system is potentially a rule you haven't turned into a script yet."

**25. Prompts drift over time.** Even perfect prompts get ignored without mechanical enforcement. Worse when importing external configs that contradict existing prompts. "Instructions in files are suggestions. Scripts that run before every response are enforcement."

### System Health (18, 20)

**18. Health scores lie.** Score at 94 while critical stuff failing. Stale data. Fix: three-layer scoring (letter grade → category scores → hard gates) plus an integrity multiplier (pass=1.0, warning=0.67, failing=0.33). Critical gate failure degrades entire score. "High activity does not mean healthy."

**20. Safety checks skipped under pressure.** Approval processes ignored when things get busy. Fix: numbered sequential gates with pass/fail criteria. Structure makes skipping harder than doing.

### Debugging & Environment (24, 26, 27)

**24. Irreversible actions need human checkpoints.** Branch first, pause before merge, review before ship. Workspace should be a GitHub repo.

**26. "Random" bugs aren't random.** Ghost duplicate repos, localhost pages opening unexpectedly. Caused by managed browser profile interfering with automation under specific conditions. Find the boundary and the behavior becomes predictable.

**27. Duplicate repos silently wreck everything.** 6 duplicate repo sets found. Agent reads from wrong copy, makes confident statements on outdated code. Fix: one location per repo, audit regularly.

## Mapping to Our Systems

| His Fix | Our Equivalent | Status |
|---|---|---|
| Evidence gate (#9) | Issue closure protocol + "Before You Work" confirmation block | ✅ Implemented |
| decisions.md (#11) | memory/YYYY-MM-DD.md + MEMORY.md | ✅ Implemented |
| Write first, speak second (#12) | Partial (commits before reporting, but not mechanically enforced) | ⚠️ Gap |
| Chain of command (#2) | Main → ops agent hierarchy, sub-agent spawning | ✅ Implemented |
| Cron audit (#15) | The Floor daily check catches failing crons | ✅ Implemented |
| Health scoring (#18) | No equivalent. Floor reports status but no composite score or integrity multiplier | ❌ Gap |
| Advisory mode before enforcement (#21) | No equivalent. We deploy rule changes directly | ❌ Gap |
| Script enforcement over docs (#23, #25) | CI checks enforce some rules. Most rules are still documentation-only | ⚠️ Partial |
| Structured cron output format (#16) | No standard format. Some crons are noisy | ⚠️ Gap |
| Snapshot before config changes (#22) | Git provides this implicitly, but no explicit snapshot protocol | ⚠️ Partial |

## His Recommended Fix Order (If Your System Is Lying)

1. **Context gate:** Load corrections, decisions, recent memory before agent responds to anything
2. **Decisions log:** Every redirect saved permanently, loaded at session start
3. **Evidence gate:** Repo, branch, commit hash, what changed, proof it works
4. **Health score:** Timestamps, freshness checks, category detail. Critical failure = whole score degrades
5. **Integrity multiplier:** High activity + broken integrity = bad score, not good
6. **Script enforcement:** Every repeated failure becomes a mechanical gate, not another line in a doc

His thesis: "The unlock is not better prompts. The unlock is operational mechanics. You can have an average model with strong enforcement and run a reliable one. Reliability wins because enforcement compounds over time."

## Key Gaps to Address

1. **Health scoring system.** We have no composite health score. The Floor reports individual checks but nothing aggregated with hard gates and integrity multipliers.
2. **Advisory mode for rule changes.** We deploy directly. Running new rules in read-only mode first would catch conflicts.
3. **Standardized cron output format.** What/why/next/confidence/evidence for every job. Silent ack when nothing to report.
4. **Script enforcement ratio.** Need to audit how many of our rules are documentation vs mechanically enforced. Target: move critical rules from docs to scripts.
