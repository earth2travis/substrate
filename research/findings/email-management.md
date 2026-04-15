---
title: "Email Management Research: AI-First Inbox Strategy"
tags:
  - ai-agents
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/email-management.md
---

# Email Management Research: AI-First Inbox Strategy

_Research compiled February 2, 2026. For the <email> shared inbox._

## Context

[[Sivart]] (AI agent) and [[Ξ2T]] (human) share an inbox via Google Workspace. The dynamic is unusual: an AI agent is the primary inbox reader, checking on heartbeat intervals via the Gmail API. The human dislikes email, uses it only for admin tasks. This means traditional email management frameworks need to be adapted for a workflow where the agent triages and the human only touches what truly requires human attention.

Current constraints:

- Gmail API access is **readonly** (service account blocked on org policy for key creation)
- Inbox is low volume: service signups, verification codes, admin notifications
- Business correspondence may come later
- The agent cannot currently modify labels, archive, or send replies via API

## 1. Traditional Email Management Frameworks

### Inbox Zero (Merlin Mann, 43 Folders)

The "zero" refers to the amount of time your brain spends in the inbox, not the literal count of messages. Core actions for every email:

1. **Delete** (or archive): Does it need a response? No? Gone.
2. **Delegate**: Are you the right person? Forward it to whoever is.
3. **Respond**: Can you answer in under 2 minutes? Do it now.
4. **Defer**: Needs more thought? Capture it in a task system, archive the email.
5. **Do**: For the remaining action items, do the work.

**Relevance to us:** The five actions map directly to agent triage. The agent can classify every email into one of these buckets automatically. "Delete" becomes "archive/ignore." "Delegate" means routing to [[Ξ2T]]. "Respond" could eventually be agent-drafted replies. "Defer" maps to creating GitHub issues or tasks. "Do" is the agent handling things itself (like noting verification codes).

### GTD Email Processing (David Allen)

Getting Things Done treats email as just one of many "inboxes" feeding a unified task system. The process:

1. **Capture**: Collect everything in inboxes (email is one of many).
2. **Clarify**: For each item, ask: Is it actionable? If yes, what's the next action? If no, trash it, file it as reference, or add to a "someday/maybe" list.
3. **Organize**: Put clarified items where they belong (calendar, project list, reference files, waiting-for list).
4. **Review**: Weekly review of all lists and inboxes.
5. **Engage**: Work from your organized lists, not from your inbox.

**The two-minute rule**: If the next action takes less than two minutes, do it immediately. Otherwise, delegate or defer.

**Relevance to us:** GTD's core insight is that email is an intake point, not a workspace. The agent should process email into other systems (GitHub issues, memory files, alerts to [[Ξ2T]]) rather than treating the inbox as a to-do list. The two-minute rule maps to the agent's per-heartbeat processing: if it can handle something instantly (log a verification code, note a notification), do it. Otherwise, escalate.

### OHIO (Only Handle It Once)

A simplification of the above: every time you open an email, take a final action on it. No re-reading the same email three times trying to decide what to do. Touch it once, process it, move on.

**Relevance to us:** This maps perfectly to agent processing. The agent reads each email once per heartbeat check and makes a classification decision. No "come back to this later" loop. The agent either handles it, escalates it, or archives it.

### Tiago Forte's One-Touch Inbox Zero

Forte's approach builds on Mann's Inbox Zero with emphasis on downstream systems. His core argument: inboxes overflow because there are no effective downstream systems to receive the processed items. He advocates:

- Stripping email down to its core function: collecting new inputs.
- Routing every email to one of four downstream systems: a task manager, a calendar, a reference system, or an archive.
- Turning off all Gmail "smart" features (stars, categories, importance markers, filters) in favor of external systems.

**Relevance to us:** The "downstream systems" principle is powerful for us. Our downstream systems are:

- **GitHub Issues**: Actionable items that need tracking
- **Memory files**: Context and reference information
- **Telegram alerts**: Urgent items requiring [[Ξ2T]]'s attention
- **Archive**: Everything else

## 2. AI-Assisted Email Management Trends

### Commercial AI Email Tools

Products like SaneBox, Superhuman, and Shortwave have established patterns for AI email triage:

- **Priority classification**: AI determines importance based on sender, content, and patterns.
- **Auto-categorization**: Sorting into folders/labels like SaneBox's SaneLater, SaneNews, SaneBlackHole.
- **Digest summaries**: Rolling up less important emails into a single daily summary.
- **Follow-up detection**: Flagging sent emails that haven't received responses.
- **Smart snoozing**: Resurface emails at relevant times.

### Patterns Worth Adopting

1. **Tiered importance**: Not all emails deserve equal attention. A three-tier system (urgent, routine, noise) is the minimum.
2. **Digest model**: Low-priority items collected and presented as a batch summary, not individual alerts.
3. **Sender reputation**: Build a list of known senders and their typical importance level.
4. **Content pattern matching**: Verification codes, receipts, shipping notifications, and security alerts all have recognizable patterns.
5. **Blackhole concept**: Some senders should be permanently ignored without unsubscribing (preserves the signup but kills the noise).

### The Agent-First Difference

Traditional AI email tools assist a human who reads email. Our setup inverts this: the agent is the primary reader, and the human is a secondary escalation target. This changes the design:

- **The agent doesn't need to "summarize" for itself.** It reads the full content and makes decisions.
- **Escalation is the expensive operation.** Every alert to [[Ξ2T]] has a cost (attention, context switching). Minimize false positives.
- **The agent can maintain state between checks.** Track what's been seen, what's pending, what's been escalated.
- **Response latency is different.** The agent checks on intervals, not in real-time. This is fine for admin email but needs consideration if business correspondence arrives.

## 3. Gmail-Specific Implementation

### Labels vs. Categories vs. Filters

Gmail offers three organizational tools:

**Categories** (system-level, limited):

- Primary, Social, Promotions, Updates, Forums
- Cannot create custom categories
- Useful as a first-pass pre-sort; Gmail's own ML handles this
- Available via API as system labels (CATEGORY_PERSONAL, CATEGORY_SOCIAL, etc.)

**Labels** (user-level, flexible):

- Up to 5,000 custom labels
- Support nesting (hierarchical: `Parent/Child`)
- Can be applied via API using `users.messages.modify`
- Can have colors for visual distinction in the web UI
- Many-to-many: one email can have multiple labels

**Filters** (automation rules):

- Created in Gmail settings or via API
- Match on From, To, Subject, has words, doesn't have, size, attachments
- Actions: skip inbox, apply label, star, forward, delete, mark as read, categorize
- Only affect new messages (not retroactive unless specified at creation)

### Gmail API Capabilities

For agent-managed email, the relevant API endpoints:

| Operation     | Endpoint                | Required Scope   |
| ------------- | ----------------------- | ---------------- |
| List messages | `users.messages.list`   | `gmail.readonly` |
| Get message   | `users.messages.get`    | `gmail.readonly` |
| Modify labels | `users.messages.modify` | `gmail.modify`   |
| Create labels | `users.labels.create`   | `gmail.labels`   |
| List labels   | `users.labels.list`     | `gmail.readonly` |
| Send message  | `users.messages.send`   | `gmail.send`     |

**Current blocker**: We only have `gmail.readonly`. To implement the full system, we need at minimum `gmail.modify` (for labeling/archiving) and `gmail.labels` (for creating our label taxonomy). This requires resolving the GCP org policy blocking service account key creation.

### Recommended Label Taxonomy

Based on our use case, a flat-with-prefixes approach works best. Nesting is useful for visual organization but the API works with label IDs regardless.

```
[[Sivart]]/Urgent          — Needs [[Ξ2T]]'s attention now
[[Sivart]]/Action          — Agent is tracking; may need human action
[[Sivart]]/Processed       — Agent handled it; archived for reference
[[Sivart]]/Verification    — Verification codes, 2FA, confirmations
[[Sivart]]/Receipts        — Purchase confirmations, billing
[[Sivart]]/Notifications   — Service notifications, system alerts
[[Sivart]]/Newsletters     — Subscribed content, digests
[[Sivart]]/Security        — Security alerts, login attempts, password changes
[[Sivart]]/Business        — Correspondence requiring human judgment (future)
[[Sivart]]/Ignore          — Known noise; agent skips these
```

The `[[Sivart]]/` prefix keeps our labels namespaced and distinct from any labels [[Ξ2T]] might create manually.

### Recommended Gmail Filters

Set up server-side filters for the most predictable categories. These run before the agent even sees the email:

1. **Verification codes**: From common senders (google, github, etc.) with subjects containing "verification", "confirm", "code" → Apply `[[Sivart]]/Verification`, skip inbox
2. **Receipts**: From known billing senders, subjects with "receipt", "invoice", "payment" → Apply `[[Sivart]]/Receipts`, skip inbox
3. **Security alerts**: Subjects containing "security alert", "new sign-in", "password changed" → Apply `[[Sivart]]/Security`, keep in inbox (agent should review)
4. **Social/promo noise**: Gmail categories Social and Promotions → Apply `[[Sivart]]/Ignore`, skip inbox

## 4. Recommended System: Agent-First Email Processing (AFEP)

Combining the best of the frameworks above into a system designed for our specific setup.

### Design Principles

1. **Email is an intake, not a workspace.** Process into downstream systems.
2. **The agent is the gatekeeper.** [[Ξ2T]] only sees what truly needs human eyes.
3. **Classification is a decision, not a delay.** Every email gets one pass, one classification.
4. **Silence is golden.** If the agent can handle it, [[Ξ2T]] never hears about it.
5. **Audit trail over memory.** Label and log everything. The agent forgets between sessions; the labels don't.

### Processing Flow

```
New Email Arrives
       │
       ▼
Gmail Filters (server-side)
       │
       ├── Known pattern? → Auto-label, skip inbox
       │
       └── Unknown/Inbox → Agent picks up on heartbeat
                │
                ▼
        Agent Classification
                │
                ├── Noise/Handled → Label + Archive
                │       (verification codes logged, receipts noted)
                │
                ├── Informational → Label + Log to memory
                │       (service notifications, status updates)
                │
                ├── Actionable (agent) → Label + Create issue/task
                │       (things the agent can handle independently)
                │
                ├── Actionable (human) → Label + Alert [[Ξ2T]] via Telegram
                │       (requires human judgment or credentials)
                │
                └── Urgent → Label + Immediate Telegram alert
                        (security breaches, time-sensitive business)
```

### Priority Tiers

**P0 (Urgent)**: Security alerts for active threats, time-sensitive business emails, anything that could cause harm if delayed. Agent sends immediate Telegram notification with summary.

**P1 (Action Required)**: Emails needing [[Ξ2T]]'s input or approval. Agent includes in the next heartbeat summary or creates a GitHub issue. Examples: renewal decisions, legal correspondence, account issues requiring human auth.

**P2 (Informational)**: Agent handles silently. Logs relevant data to memory files. Examples: successful payment confirmations, service status updates, shipping notifications.

**P3 (Noise)**: Auto-archived, never surfaced. Examples: marketing emails, social notifications, promotional offers.

### Heartbeat Integration

The agent already checks email on heartbeat intervals. The email processing should:

1. Fetch unread messages since last check (track in `memory/heartbeat-state.json`)
2. For each message, classify using the flow above
3. Apply labels (once we have write access)
4. Generate a summary only if P0 or P1 items exist
5. Update heartbeat state with timestamp and counts

### Daily Digest

Once daily (or on request), the agent can provide [[Ξ2T]] with a digest:

```
📧 Daily Email Digest (Feb 2, 2026)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Processed: 12 emails
  🔴 Urgent: 0
  🟡 Action needed: 1 (domain renewal reminder from Hover)
  🟢 Handled: 8 (3 receipts, 2 verifications, 3 notifications)
  ⚫ Archived: 3 (promotional)
```

## 5. Implementation Roadmap

### Phase 1: Foundation (Current Sprint)

**Prerequisite**: Resolve GCP org policy to enable service account key creation.

1. Enable `gmail.modify` and `gmail.labels` scopes on the service account
2. Create the label taxonomy via API
3. Set up Gmail filters for known patterns
4. Build the agent's email processing module:
   - Fetch unread since last check
   - Classify by sender + subject + content patterns
   - Log results to memory
   - Alert via Telegram for P0/P1

### Phase 2: Smart Classification

1. Build sender reputation database (JSON file mapping sender → typical priority)
2. Implement content pattern matching for common email types
3. Add regex patterns for verification codes, tracking numbers, etc.
4. Integrate with heartbeat cycle (batch processing, state tracking)

### Phase 3: Active Management

1. Agent applies labels based on classification
2. Agent archives processed emails
3. Agent maintains daily digest
4. Agent creates GitHub issues for actionable items

### Phase 4: Correspondence (Future)

1. Agent drafts replies for [[Ξ2T]]'s approval
2. Agent handles routine responses independently (with guardrails)
3. Business email templates and workflows
4. Contact management

## 6. Technical Notes

### Gmail API Readonly Workarounds

While we're stuck on readonly, the agent can still:

- Read and classify all emails
- Track state in local files (what's been seen, what needs action)
- Alert via Telegram for anything important
- Log verification codes and important data to memory

What we cannot do without write access:

- Apply labels programmatically
- Archive or delete emails
- Move emails between categories
- Send replies

The manual workaround: [[Ξ2T]] creates the label taxonomy and filters through the Gmail web UI. The agent reads the labels that Gmail filters apply and uses those in its classification logic.

### State Tracking Schema

```json
{
  "lastCheck": "2026-02-02T23:00:00Z",
  "lastMessageId": "msg_abc123",
  "processedCount": {
    "total": 47,
    "urgent": 0,
    "action": 3,
    "info": 28,
    "noise": 16
  },
  "senderReputation": {
    "noreply@github.com": { "tier": "P2", "type": "notifications" },
    "<sender>": { "tier": "P1", "type": "billing" },
    "<sender>": { "tier": "P2", "type": "security" }
  }
}
```

## Sources

- Merlin Mann, "Inbox Zero" (43folders.com)
- David Allen, "Getting Things Done" methodology
- Tiago Forte, "One-Touch to Inbox Zero" (fortelabs.com)
- Google Gmail API Documentation (developers.google.com/workspace/gmail)
- Google Gmail Support: Labels, Filters, Categories
- SaneBox product model and AI triage patterns

---

_This document is a living reference. Update as we implement and learn._
