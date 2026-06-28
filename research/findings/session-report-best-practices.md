---
title: "Session-End Reporting Best Practices: Cross-Domain Synthesis for Agent SITREPs"
tags: [agents, reporting, sft, handoff, operations, crash, multi-agent, coordination]
related:
- agent-native-operations
- kanban-doctrine
- mission-command
- multi-agent-coordination-patterns
- agent-orchestrator-pattern
- audit-replay
source: research/raw/session-report-best-practices.md
---
# Session-End Reporting Best Practices: Cross-Domain Synthesis for Agent SITREPs

## Summary

Research on best practices for session-end reporting, handoff documentation, and shift-change communication across five high-stakes domains — military, medical, software engineering, incident response, and aviation CRM — to inform the design of a SITREP pattern for AI agent sessions. The synthesis identifies ten universal patterns and a minimal universal structure.

## Five Domains

1. **Military shift-change briefings** (U.S. Navy/DoD): Watch turnover with 10 structured fields including watch purpose, current situation, active threats, ongoing operations, equipment status, standing orders, pending actions, read-back/confirmation. Written log backs verbal brief. The relief must formally state "I have the watch."

2. **Medical shift changes** (SBAR and I-PASS): SBAR (Situation, Background, Assessment, Recommendation) for urgent clinical communication. I-PASS (Illness Severity, Patient Summary, Action List, Situation Awareness/Contingency, Synthesis by Receiver) for shift handoff. I-PASS validated in NEJM 2014: 23% reduction in medical errors, 30% reduction in preventable adverse events. Critical: "Synthesis by Receiver" is active read-back.

3. **Software engineering:** PR descriptions (the closest formal analog to a SITREP) and end-of-session notes. Good PR: problem/motivation, solution/approach, testing done, scope, risk, follow-ups, backout plan. End-of-session: what I was doing, completed, mid-way through, blocked, next, anything weird.

4. **Incident response post-mortems and SRE handoffs:** Mid-incident IC handoff (status, customer impact, what tried, what trying, hypotheses, decisions, open questions, action items, read-back). Post-incident post-mortem (blameless, timeline, root cause, what went well/wrong, where lucky, action items with owners/dates).

5. **Aviation CRM debriefs:** Objectives, what went well (named behaviors), errors/threats, countermeasures, what differently, open conversations. TEM model: Threats, Errors, Undesired States, Countermeasures.

## Ten Universal Patterns

1. **Verbal + written combination** — synchronous verbal handoff (read-back) paired with durable written artifact. Neither alone sufficient.
2. **Structured/templated format** — fixed template every time. Prevents omission, speeds production under pressure.
3. **Closing-loop / read-back** — active confirmation by receiver. I-PASS calls it "Synthesis by Receiver"; military requires read-back; IC relief restates the active frame. "Any questions?" is not verification.
4. **Situation before solution** — good reports start with the problem and why before the what.
5. **Severity/priority up front** — I-PASS forces one-word severity first; post-incident has severity at top; military lists active threats first. The receiver gets a triage frame.
6. **Failed attempts / rejected options logged** — post-mortems include "what we tried"; IC handoffs document rejected mitigations; I-PASS has contingency planning. Prevents the next person from re-running dead-ends.
7. **What's next, concretely** — all domains close with the next action set.
8. **Blameless / systems framing** — SRE post-mortems explicitly blameless; CRM normalizes error; medical focuses on process not persons. Preserves psychological safety.
9. **Contingency / "if-X-then-Y"** — I-PASS, IC handoff ("what if hypothesis is wrong"), good PRs (rollback plan), military (contingency orders).
10. **Active verification, not passive sign-off** — receiver reads back, IC repeats active frame, CRM asks each crewmember to contribute.

## Two Universal Anti-Patterns

1. **The "Nothing Happened" Dismissal** — "Quiet watch, stable patient, great flight." Hides the active frame precisely when most likely to be lost. Protocol must mandate the report especially when nothing visible happened.
2. **The "I'll Write It Later" Assumption** — end-of-watch rush, "postmortem next week," "PR description after merge." Each is when memory decays fastest and reconstruction error creeps in. Protocol must require capture close to the event.

## Minimal Universal SITREP Structure

1. Headline / situation summary (1-3 sentences)
2. Severity / status (green/yellow/red or done/partial/blocked/failed)
3. What was attempted (concrete list)
4. What succeeded / completed
5. What failed / didn't work (with why, and rejected approaches)
6. What's blocked / pending
7. Active state / in-flight work (state dump)
8. Next actions (sorted list, who/what/when)
9. Open questions / contingencies ("If X then Y")
10. References / state snapshots (logs, commits, files, IDs)

Close: read-back when synchronous — receiver restates situation summary and top three action items.

## Why This Matters for the Substrate

This research directly informs agent session reporting. The SITREP pattern derived here is the artifact that flows through the blackboard architecture described in cross-agent reporting. The "nothing happened" dismissal maps to the no-op log entries that the Substrate's daily synthesis already produces — and validates that reporting even when nothing happened is the correct protocol.

The failed-attempts logging connects to [[audit-replay]] — recording what was attempted (not just what succeeded) is a proven safety practice across domains. The structured handoff with read-back connects to [[kanban-doctrine]] and [[mission-command]] — structured context transfer is how mission command operationalizes intent across personnel changes. The multi-agent coordination patterns in [[multi-agent-coordination-patterns]] and [[agent-native-operations]] require this kind of structured reporting to maintain coherent fleet operation.

One sentence: a session report is a context transfer artifact that must be structured, templated, closed-loop confirmed, and capture failed attempts alongside successful ones, written as close to the event as possible.

## Related

- [[agent-native-operations]] — Tools and workflows designed for AI-human partnership
- [[kanban-doctrine]] — Auftragstaktik as agent operating system
- [[mission-command]] — Command by intent, structured handoff
- [[multi-agent-coordination-patterns]] — Coordination across independent agents