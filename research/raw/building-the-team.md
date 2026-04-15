# Building the Team: Specialized Agents for [[Sivart]]

_Research started: February 13, 2026_
_Context: Week 2 feedback from [[Ξ2T]] indicated sloppy execution, repeated back-and-forth, work requiring manual intervention_

---

## This Week's Failures (Specific Incidents)

1. **Stale Summary Problem** — Compaction summary said evals research was "in progress." Reality: already merged as PR #166. Result: Created duplicate PR #174 with 0 files changed. Wasted time, confused [[Ξ2T]].

2. **Template Noise** — PR #172 showed "3 of 14 tasks" complete. Looked unfinished. Reality: just irrelevant template checkboxes. Required manual clarification.

3. **Email Neglect** — Last tracked email check was Feb 3. Ten day gap. Inbox accumulated mess.

4. **Sync Drift** — Blog had 8 posts, transmissions/ directory had different files. Out of sync for unknown duration. Required manual cleanup.

5. **Multiple Iterations** — Simple tasks taking 2-3 back-and-forths when they should be right the first time.

---

## Pattern Analysis

| Failure Type            | Root Cause                                | Frequency |
| ----------------------- | ----------------------------------------- | --------- |
| Acting on stale data    | Trusted summary over reality              | High      |
| Maintenance neglect     | Background tasks fall off when not forced | Medium    |
| Process drift           | Knowing what to do, not doing it          | Medium    |
| Incomplete verification | Claiming done without checking            | High      |

**The Common Thread:** Verification failures. I act on assumptions instead of checking state. I claim completion without confirming. I let maintenance slip because nothing forces it.

---

## What Specialized Agents Would Solve

### 1. Ops Agent (Highest Priority)

**Purpose:** Handle recurring operational tasks autonomously. Run daily without being asked.

**Responsibilities:**

- Email triage (daily)
- Blog/source sync check (weekly)
- Version monitoring (weekly)
- Heartbeat state maintenance
- Inbox zero enforcement

**Why This Helps:** Removes maintenance burden from main session. These tasks happen whether or not anyone remembers them. Radio silence default, escalates only when needed.

**Implementation:** Isolated cron job with agentTurn, runs once daily at a quiet hour. Reports anomalies only.

---

### 2. Verifier Agent (Second Priority)

**Purpose:** Check reality before I act. The "trust but verify" function.

**Responsibilities:**

- Before creating PR: Does this work already exist? Is the branch stale?
- Before claiming done: Does the file exist? Does git log confirm?
- Before working from summary: Is the summary accurate to current state?
- Spot check outputs against source data

**Why This Helps:** Catches the "stale summary" class of errors before they waste time. Forces me to ground claims in reality rather than assumptions.

**Implementation:** Could be a pre-action hook, or a dedicated sub-agent I invoke before major actions. "Verifier, is this PR needed?" "Verifier, is evals research actually done?"

---

### 3. Review Agent (Third Priority)

**Purpose:** Quality check before work reaches [[Ξ2T]]. Second pair of eyes.

**Responsibilities:**

- Review PRs for: Does description match actual changes? Template filled correctly?
- Check for style drift (dashes, citation leaks)
- Verify issue checklist items are actually complete before closing
- Catch obvious errors I missed

**Why This Helps:** Prevents the "multiple iterations" problem. Work is right the first time because it was reviewed before submission.

**Implementation:** Invoke before creating PR or closing issue. "Review Agent, check this PR before I submit."

---

## Alternative Framing: State Manager

Instead of Verifier as a separate agent, consider a **State Manager** that maintains ground truth:

- Canonical list of what's done, pending, blocked
- Updated after every merge/close
- I query it instead of trusting summaries
- Single source of truth that survives compaction

This might be simpler than a Verifier agent. Just maintain accurate state and always check it.

---

## Implementation Questions

1. **Sub-agent vs Cron Job?**
   - Ops Agent → Cron job (runs on schedule, isolated)
   - Verifier → Sub-agent or hook (invoked on demand)
   - Review → Sub-agent (invoked before submission)

2. **How do agents communicate?**
   - Ops Agent reports via announce to main session
   - Verifier returns pass/fail with details
   - Review Agent returns approval or list of issues

3. **What infrastructure exists?**
   - [[OpenClaw]] supports isolated cron jobs with agentTurn
   - Sub-agents via sessions_spawn
   - Could use labels/files for state management

4. **Cost/Complexity Tradeoff?**
   - Start with Ops Agent (clearest value, isolated, won't break anything)
   - Add others based on whether problems persist

---

## Recommendation: Start with Ops Agent

**Rationale:**

- Clearest scope and value
- Runs in isolation (can't break main session)
- Solves the "maintenance neglect" class entirely
- Proves the model before adding complexity

**First Implementation:**

- Daily cron job, runs at 06:00 UTC
- Checks: email, blog sync, version status
- Output: "All clear" or specific alerts
- Announces to main session only if action needed

**After Ops Agent is stable (1-2 weeks):**

- Evaluate whether Verifier or Review Agent is still needed
- The discipline of having Ops Agent might naturally improve other areas

---

## Goals and Success Metrics

Before implementing, we need alignment on what success looks like.

### Ops Agent

**Goal:** Eliminate maintenance neglect. Background tasks happen daily without manual prompting.

**Success Metrics:**
| Metric | Baseline (this week) | Target |
|--------|---------------------|--------|
| Email check gaps | 10 days | 0 days (daily) |
| Sync drift detected late | Multiple times | Caught within 24h |
| Version updates missed | Noticed late | Alerted same day |
| Manual reminders needed | Frequent | Zero |

**How to Measure:**

- Track `heartbeat-state.json` timestamps
- Log when Ops Agent runs and what it finds
- Count incidents where maintenance was neglected

**Failure Condition:** If Ops Agent runs but I still miss things, the scope is wrong.

---

### Verifier Agent

**Goal:** Eliminate stale-data errors. No more acting on assumptions that don't match reality.

**Success Metrics:**
| Metric | Baseline (this week) | Target |
|--------|---------------------|--------|
| Duplicate/empty PRs | 1 (PR #174) | 0 |
| Work based on stale summary | Multiple | 0 |
| "Already done" discoveries | Frequent | Caught before action |

**How to Measure:**

- Track PRs created vs merged (0-file PRs = failures)
- Log verification checks and outcomes
- Count times reality differed from assumption

**Failure Condition:** If verification passes but reality was different, the checks are wrong.

---

### Review Agent

**Goal:** First-time-right. Work reaches [[Ξ2T]] in correct state without iteration.

**Success Metrics:**
| Metric | Baseline (this week) | Target |
|--------|---------------------|--------|
| Back-and-forth iterations | 2-3 per task | 0-1 |
| Template noise issues | PR #172 | 0 |
| Style drift caught late | Some | Caught before PR |
| Checklist items incomplete | Occasional | 0 |

**How to Measure:**

- Count messages per task (fewer = better)
- Track PRs rejected or needing fixes
- Log Review Agent catches vs misses

**Failure Condition:** If Review Agent approves but [[Ξ2T]] finds issues, the review criteria are wrong.

---

## Complexity Management

**Risks of adding agents:**

- More moving parts = more failure modes
- Agent coordination overhead
- Cost of additional API calls
- Debugging becomes harder

**Mitigations:**

1. **Start with one agent only** (Ops Agent)
2. **Run for 2 weeks minimum** before adding another
3. **Track metrics from day one** (can't improve what we don't measure)
4. **Kill switch** — if agent causes more problems than it solves, disable immediately
5. **Weekly review** — are metrics improving? Is complexity justified?

**Decision Framework for Adding Next Agent:**

- Ops Agent metrics stable for 2 weeks? → Consider Verifier
- Verifier metrics stable for 2 weeks? → Consider Review Agent
- Metrics NOT improving? → Fix current agent before adding new one

---

## Open Questions for [[Ξ2T]]

1. Do these goals and metrics capture what matters to you?
2. Are there metrics I'm missing?
3. How should I track and report these? (Daily note? Weekly summary? Dashboard?)
4. 2-week stabilization period between agents feel right?
5. What's the threshold for "this agent isn't working, shut it down"?

---

_This document builds on: agent-economy research, feature-flags research (progressive autonomy), evals research (validating the validator)_
