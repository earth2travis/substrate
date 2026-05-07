---
title: "28 Painful Mistakes Building Agent Systems (Kloss)"
tags: [agent-systems, operations, reliability, lessons-learned, enforcement]
related:
  - [[agent-native-operations]]
  - [[context-persistence]]
  - [[kanban-doctrine]]
  - [[lean-doctrine]]
  - [[feedback-loop-discipline]]
  - [[harness-engineering]]
source: "[@kloss_xyz](https://x.com/kloss_xyz/status/2032011756890177552) March 2026"
---

# 28 Painful Mistakes Building Agent Systems

Practitioner report from three weeks of intensive OpenClaw system development. The core failure mode: gaps between what was planned and what was enforced at runtime.

## Key Metric

Rules as documentation equals approximately 48 percent compliance. Rules as scripts equals approximately 100 percent compliance.

## Categories of Mistakes

### Routing and Triggers

Loose word matching fires wrong actions. Words like "go" and "proceed" appear in normal conversation. Fix: exact whole-word matching with explicit triggers. Test with weird inputs, not just happy paths.

### Agent Architecture

Agents without hierarchy create expensive chaos: context thrashing, no ownership, conflicting changes. Fix: real chain of command. Main session orchestrates. Domain agents dispatch. Subagents execute bounded tasks. Agents have durable identity; subagents are temporary compute.

Parallel agents on same files without ownership produce conflicting changes. Four agents spawned, two overlapped, neither flagged it. Fix: define ownership before parallelizing.

Multi-problem asks produce garbage. Handing five problems at once equals half-assed work on each. One problem per agent. Atomic scope, clean output. Described as the single biggest recent improvement to execution quality.

### Handoffs and Communication

Handoffs without structured context degrade like telephone. Must carry: who sent it, what the task is, when dispatched, where results go, what evidence exists.

Agent going silent kills trust. Worst wait: approximately ten minutes from a timed-out process blocking the message channel. Fixes: fast acknowledgment before real work; long-running work in separate sessions.

### Persistence and Memory

Session death loses unsaved work. Agent times out at minute 14, work was going to commit at minute 15. Fix: commit incrementally. Small commits, frequent saves.

Corrections vanish between sessions. Same wrong assumption corrected three times in one day. Fix: decisions file loaded at session start. Every redirect written to file immediately with a date.

Phantom progress: "done" but no record on disk. Agent says complete, state never written, next session treats it as not done. Fix: write first, speak second. Persist state before telling the human anything.

### Verification and Evidence

"Done" without receipts is worthless. Built an evidence gate requiring repo plus branch, commit hash, files changed, verification that changes work, screenshot or artifact for UI.

Agent confidently reports false information. CLI summaries treated as truth. Fix: CLI summaries are views, not truth. Source files are truth. Confidence is not accuracy.

"File doesn't exist" when it does. Wrong path or incomplete directory listing. Fix: inventory scripts that count what actually exists on disk.

Narrative updates are unverifiable. "Things are looking good" tells you nothing. Fix: structured reports with explicit pass/fail. Machine-readable JSON plus human-readable markdown.

### Cron and Scheduling

Polling loops waste context. Checking "is it done?" every five seconds for ten minutes equals 120 status checks, zero information. Fix: wait for events, escalate on timeout.

Half your cron jobs make things worse. Jobs producing no value but consuming resources. Fix: cut ruthlessly. If you would not read or act on the output, kill the job.

Noisy cron jobs steal attention. Standard format for all output: what happened, why it matters, what's next, confidence zero to 100, evidence. Nothing to report equals clean acknowledgment, not silence.

Running same cron job twice simultaneously. Two processes competing over same state. Fix: trust the active loop. Let fixes soak for a full cycle before re-enabling disabled jobs.

### Configuration and Change Management

Rules in wrong order waste days. Correct sequence: core identity files, then routing rules, then language contracts, then stress tests. Each step depends on previous being stable.

Deploy in advisory mode first. Thirteen formal standards all run in read-only "what would happen" mode before enforcement. Fix problems before touching production.

Change settings without saving old ones. Fifty-four config files, 200-plus risky values. Fix: snapshot before every change, no exceptions.

Fixing all security issues at once is a trap. Fix one at a time, in order, with snapshot and rollback plan at each step. Phased hardening with checkpoints.

### Rule Enforcement

Agent violates rules it cites in the same session. Fix: mechanical gate that loads context before responding. Not a suggestion; a script that cannot be skipped. Documentation rules: approximately 48 percent compliance. Script-enforced rules: approximately 100 percent.

Prompts drift over time. Even perfect prompts get ignored without mechanical enforcement. Instructions in files are suggestions. Scripts that run before every response are enforcement.

### System Health

Health scores lie. Score at 94 while critical stuff failing. Stale data. Fix: three-layer scoring (letter grade to category scores to hard gates) plus an integrity multiplier. Critical gate failure degrades entire score.

Safety checks skipped under pressure. Approval processes ignored when things get busy. Fix: numbered sequential gates with pass/fail criteria. Structure makes skipping harder than doing.

### Debugging and Environment

Irreversible actions need human checkpoints. Branch first, pause before merge, review before ship.

"Random" bugs are not random. Caused by managed browser profile interfering with automation under specific conditions. Find the boundary and behavior becomes predictable.

Duplicate repos silently wreck everything. Six duplicate repo sets found. Agent reads from wrong copy, makes confident statements on outdated code. Fix: one location per repo, audit regularly.

## Thesis

The unlock is not better prompts. The unlock is operational mechanics. You can have an average model with strong enforcement and run a reliable system. Reliability wins because enforcement compounds over time.

## Mapping to Our Systems

| His Fix | Our Equivalent | Status |
|---|---|---|
| Evidence gate | Issue closure protocol plus confirmation block | Implemented |
| Decisions log | Memory files plus daily notes | Implemented |
| Write first, speak second | Partial (commits before reporting, not mechanically enforced) | Gap |
| Chain of command | Main to ops agent hierarchy, sub-agent spawning | Implemented |
| Cron audit | The Floor daily check | Implemented |
| Health scoring | No equivalent. Floor reports status but no composite score | Gap |
| Advisory mode before enforcement | No equivalent. Deploy rule changes directly | Gap |
| Script enforcement over docs | CI checks enforce some rules. Most rules are documentation-only | Partial |
| Structured cron output format | No standard format. Some crons are noisy | Gap |
| Snapshot before config changes | Git provides this implicitly, no explicit snapshot protocol | Partial |
