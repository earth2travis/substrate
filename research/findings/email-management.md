---
title: "Email Management: AI-First Inbox Strategy"
tags: [email, agent, automation, triage, gmail, operations]
related:
- telegram-group-setup
- custom-tooling-opportunities
- github-as-memory
- lean-software-delivery
- harness-engineering
- agent-native-operations
source: research/raw/email-management.md
---
# Email Management: AI-First Inbox Strategy

## Summary

Research on AI-first email management for a shared AI-human inbox. The agent (Sivart) is the primary reader; the human (Ξ2T) only touches what truly requires human attention. Combines Inbox Zero, GTD, and OHIO frameworks into an Agent-First Email Processing (AFEP) system with tiered priority classification and downstream routing.

## Key Claims

**Email is an intake, not a workspace.** Process into downstream systems (GitHub Issues, memory files, Telegram alerts, archive). The agent is the gatekeeper. Ξ2T only sees what truly needs human eyes.

**Classification is a decision, not a delay.** Every email gets one pass, one classification. Silence is golden: if the agent can handle it, Ξ2T never hears about it. Audit trail over memory: label and log everything. The agent forgets between sessions; labels don't.

**Four priority tiers:**
- P0 (Urgent): Security alerts, time-sensitive business. Immediate Telegram notification.
- P1 (Action Required): Needs Ξ2T input or approval. Next heartbeat summary or GitHub issue.
- P2 (Informational): Agent handles silently. Logs to memory. Payment confirmations, status updates.
- P3 (Noise): Auto-archived, never surfaced. Marketing, social notifications.

**Traditional frameworks adapted:**
- Inbox Zero's five actions (delete, delegate, respond, defer, do) map directly to agent triage
- GTD's two-minute rule: agent handles instantly what it can, escalates what it can't
- OHIO (Only Handle It Once): agent reads each email once per heartbeat and decides
- Tiago Forte's downstream systems: GitHub Issues, memory files, Telegram alerts, archive

**Gmail API constraints.** Current readonly access (service account blocked by org policy). Cannot apply labels, archive, delete, or send replies. Manual workaround: Ξ2T creates label taxonomy and filters via web UI; agent reads labels that Gmail applies.

**Recommended label taxonomy:** Sivart/Urgent, Sivart/Action, Sivart/Processed, Sivart/Verification, Sivart/Receipts, Sivart/Notifications, Sivart/Newsletters, Sivart/Security, Sivart/Business, Sivart/Ignore.

**Implementation roadmap:** Phase 1 (foundation: resolve GCP policy, create labels, build processing module), Phase 2 (smart classification: sender reputation, content pattern matching), Phase 3 (active management: agent applies labels, archives, creates GitHub issues), Phase 4 (correspondence: agent drafts replies, handles routine responses).

## Processing Flow

New email arrives → Gmail filters (server-side) → Agent picks up on heartbeat → Classification: Noise/Handled (label + archive), Informational (label + log), Actionable agent (label + create issue), Actionable human (label + alert via Telegram), Urgent (label + immediate alert).

## Daily Digest

Once daily: processed count, urgent count, action needed count, handled count, archived count. Example: "Processed: 12 emails. Urgent: 0. Action needed: 1 (domain renewal reminder). Handled: 8. Archived: 3."

## Connection to Agent Operations

Email is one of multiple ingestion surfaces for the Agent Factory. The AFEP system demonstrates how any external signal (email, social, webhook) can be classified and routed to appropriate downstream systems. The pattern is generalizable: intake → classify → route → act.

## Related

- [[telegram-group-setup]] — Primary alert channel for escalations
- [[custom-tooling-opportunities]] — Process audit and capacity reporting
- [[github-as-memory]] — Downstream system for actionable items
- [[lean-software-delivery]] — Continuous improvement and waste elimination
- [[harness-engineering]] — Agent-first development methodology
