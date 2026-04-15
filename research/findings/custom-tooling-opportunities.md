---
title: "Custom Tooling Opportunities: Agent-Native Project Management"
tags:
  - research
  - project-management
  - tooling
  - agent
related:
  - [[actual-occasions]]
  - [[ai-career-convergence]]
  - [[ai-sdk-research]]
  - [[alfred-north-whitehead]]
source: research/raw/custom-tooling-opportunities.md
---

# Custom Tooling Opportunities

_Research completed 2026-02-28. Related: issue #302._

## Where Existing Tools Fall Short

Our workflow is unusual: the project manager is an AI agent ([[Sivart]]) working with a human ([[Ξ2T]]). This creates specific friction points that no off-the-shelf tool was designed to address.

### Friction Point 1: Context Loss Between Sessions

**The problem:** Sivart wakes up fresh each session. The first minutes of every session are spent reading SOUL.md, MEMORY.md, recent daily notes, and HEARTBEAT.md to reconstruct context. This is wasteful and imperfect. Information from previous sessions that was not explicitly written down is gone.

**Where tools fall short:** GitHub Issues, Projects, and the gh CLI provide no concept of "session context." They track work items, not working context. A human PM remembers that yesterday's standup revealed tension about a feature's direction. Sivart does not, unless someone wrote it down.

**Tooling opportunity:**

- **Session context generator.** A script that runs at session start and produces a structured briefing: open issues by priority, recently closed issues, issues with new comments, PRs awaiting review, upcoming calendar events, last 3 daily notes summarized. Output: a single markdown file optimized for fast ingestion.
- **Implementation:** `scripts/session-briefing.js` that calls `gh` CLI, reads recent memory files, and compiles a briefing. Could run as part of HEARTBEAT.md check or be triggered manually.
- **Effort:** Medium (1-2 days). **Impact:** High. Reduces session startup from minutes to seconds.

### Friction Point 2: Issue Lifecycle Gaps

**The problem:** Our process (AGENTS.md) requires: issue first, add to project, do work, commit with reference, close with summary. But nothing enforces this. Sivart can (and occasionally does) do work without an issue, commit without referencing an issue, or close an issue without documenting what was done.

**Where tools fall short:** GitHub has no concept of "process compliance for an AI agent." Commitlint checks commit format but not issue references. Project automations move cards but do not verify that the process was followed end-to-end.

**Tooling opportunity:**

- **Process compliance checker.** A script or GitHub Action that audits:
  - Commits without issue references (`#NNN`)
  - Open issues with no recent activity (assigned but stale)
  - Closed issues with no linked commits or PRs
  - Issues not assigned to any project
  - PRs without linked issues
- **Implementation:** `scripts/process-audit.js` using `gh` CLI to query issues, PRs, and commits. Run weekly or on-demand.
- **Effort:** Medium (1 day). **Impact:** High. Catches process drift before it accumulates.

### Friction Point 3: Work Capacity Blindness

**The problem:** Neither [[Ξ2T]] nor Sivart has a clear picture of how much work is in progress, how much is queued, or whether the current pace is sustainable. We have no WIP limits, no velocity tracking, no way to answer "are we taking on too much?"

**Where tools fall short:** GitHub Projects V2 has charts (burn-up, distribution) but they are basic and require manual interpretation. There is no concept of WIP limits or capacity planning.

**Tooling opportunity:**

- **Capacity dashboard.** A script that calculates and reports:
  - Current WIP: count of issues in "In Progress" across all projects
  - Queue depth: count of issues in "Todo" by priority
  - Velocity: issues closed per week (rolling 4-week average)
  - Size distribution: are we doing mostly XS/S (good flow) or mostly L/XL (risk of stall)?
  - Cycle time: average days from Todo to Done
- **Implementation:** `scripts/capacity-report.js` using `gh project item-list` with JSON output and jq processing. Output to `reports/capacity/` or as a project issue comment.
- **Effort:** Medium (1-2 days). **Impact:** High. Makes invisible capacity constraints visible.

### Friction Point 4: Research Discoverability

**The problem:** We have a rich research directory (40+ files and folders) but no index, no search, no way to quickly find relevant prior research when starting new work. Sivart must `ls` and `cat` files to check what exists.

**Where tools fall short:** GitHub's repository search works but is clunky. The research directory has no metadata structure that enables programmatic discovery.

**Tooling opportunity:**

- **Research index generator.** A script that scans `research/` and generates an index file with: title, date, tags, related files, and a one-line summary extracted from frontmatter or first paragraph.
- **Implementation:** `scripts/research-index.js` that parses YAML frontmatter and generates `research/INDEX.md`. Run after each research commit (via pre-push hook or GitHub Action).
- **Effort:** Low (half day). **Impact:** Medium. Prevents duplicate research and speeds up context gathering.

### Friction Point 5: Decision Tracking Fragmentation

**The problem:** Decisions are scattered across issue comments, commit messages, daily notes, and the decisions/ directory. Finding "why did we choose X?" requires searching multiple locations.

**Where tools fall short:** GitHub has no decision tracking primitive. Issues are for tasks, not for recording architectural or strategic decisions. ADR (Architecture Decision Record) patterns exist but are not integrated with GitHub's workflow.

**Tooling opportunity:**

- **Decision log with backlinks.** Ensure every decision in `decisions/` references the issue that prompted it and is cross-referenced from the issue. A script could audit for orphaned decisions (no issue link) or issues with decisions that are not documented.
- **Implementation:** Convention + audit script. Less about new tooling, more about process consistency.
- **Effort:** Low. **Impact:** Medium.

## Agent-Native Project Management: What Changes When the PM is an AI

This is the frontier question. Most project management tools assume a human PM who:

- Has persistent memory across days and weeks
- Reads social cues and body language
- Attends meetings and hallway conversations
- Has intuitive sense of team morale and capacity
- Makes judgment calls based on experience and gut feeling

An AI PM has different strengths and weaknesses:

### What an AI PM Does Better

1. **Perfect process compliance** (when configured correctly). Never forgets to update an issue, reference a commit, or follow the workflow. The failure mode is not forgetting but misconfiguring.

2. **Exhaustive search.** Can scan every open issue, every commit, every file in seconds. A human PM skims. An AI PM can be thorough.

3. **Consistent triage.** Applies the same criteria to every issue without fatigue, recency bias, or favoritism.

4. **Documentation as natural output.** Writing is not overhead for an AI. Every decision, every research finding, every status update gets documented because documentation is how the AI thinks.

5. **24/7 availability** (within session constraints). Can check for urgent issues, process email, review PRs at any hour.

6. **Multi-source synthesis.** Can simultaneously consider issue state, git history, calendar, email, and memory files when making decisions.

### What an AI PM Does Worse

1. **No persistent state.** The human PM wakes up remembering yesterday. The AI PM wakes up reading files about yesterday. The delta is significant for nuanced context.

2. **No social sensing.** Cannot read frustration in a PR review comment, detect burnout in shorter commit messages, or sense that [[Ξ2T]] is excited about a direction from tone of voice.

3. **Difficulty with "when to break the rules."** Process deviations require judgment that is hard to codify. The AI PM may follow the process into a wall.

4. **No independent motivation.** An AI PM does not think about the project in the shower. It does not have background processing between sessions. Ideas and insights that emerge from subconscious rumination do not happen.

5. **Context window as WIP limit.** The AI PM cannot hold infinite context. Long sessions degrade quality. This is actually a useful constraint (it forces handoffs and documentation) but it is different from human cognitive limits.

### Design Principles for Agent-Native PM

Based on these differences, agent-native project management should be designed around:

1. **Write everything down.** Not as a nice-to-have but as a survival mechanism. If it is not in a file, it does not exist for the next session. This is already our philosophy (AGENTS.md), but it should be elevated to the primary design constraint.

2. **Automate the ceremony, preserve the judgment.** Moving cards on a board is ceremony. Deciding what to work on next is judgment. Automate the former ruthlessly. Protect the latter from automation.

3. **Build session affordances.** Every tool interaction should assume a fresh context. The session briefing (Friction Point 1) is the prototype. Other affordances: issue templates that include relevant context links, commit hooks that validate process compliance, dashboard scripts that summarize state.

4. **Externalize memory to structured data.** Instead of relying on narrative memory files (which require reading and interpretation), move key state into structured formats: JSON for metrics, YAML frontmatter for metadata, project fields for issue state. Structured data is faster to parse and harder to misinterpret.

5. **Short feedback loops by default.** The AI PM should check process compliance after every commit, not once a week. Review capacity daily, not monthly. The cost of frequent checking is low for an AI (a few API calls). The cost of delayed feedback is high (drift accumulates silently).

6. **Human-in-the-loop for irreversible actions.** Sending emails, posting publicly, closing milestones, archiving projects. The AI PM proposes; the human approves. For reversible actions (creating issues, updating fields, drafting documents), act autonomously.

## Concrete Proposals

### Proposal 1: Session Briefing Script

**File:** `scripts/session-briefing.js`
**Trigger:** Manual or heartbeat
**Output:** `reports/session-briefing.md`
**Content:** Open issues by project/priority, recent closures, PRs pending, calendar next 48h, unread email count, last daily note date
**Effort:** 1 day | **Priority:** High

### Proposal 2: Process Audit Script

**File:** `scripts/process-audit.js`
**Trigger:** Weekly (cron) or manual
**Output:** `reports/process-audit.md`
**Content:** Commits without issue refs, issues without projects, closed issues without commits, stale in-progress issues
**Effort:** 1 day | **Priority:** High

### Proposal 3: Capacity Report Script

**File:** `scripts/capacity-report.js`
**Trigger:** Weekly or on-demand
**Output:** `reports/capacity/YYYY-MM-DD.md`
**Content:** WIP count, queue depth, velocity, cycle time, size distribution
**Effort:** 1.5 days | **Priority:** Medium

### Proposal 4: Research Index Generator

**File:** `scripts/research-index.js`
**Trigger:** Post-commit hook or manual
**Output:** `research/INDEX.md`
**Content:** Catalog of all research files with frontmatter metadata
**Effort:** 0.5 day | **Priority:** Medium

### Proposal 5: Issue Form Templates

**Files:** `.github/ISSUE_TEMPLATE/task.yml`, `research.yml`, `decision.yml`
**Content:** Structured YAML forms replacing free-text templates
**Effort:** 0.5 day | **Priority:** Medium

### Proposal 6: GitHub Actions Pipeline

**Files:** `.github/workflows/pr-checks.yml`, `weekly-digest.yml`
**Content:** Prettier check, commitlint, stale issue detection, weekly summary
**Effort:** 1 day | **Priority:** Medium

### Implementation Order

1. Session briefing (immediate value, unblocks everything else)
2. Process audit (catches drift early)
3. Issue form templates (low effort, immediate quality improvement)
4. GitHub Actions pipeline (automates mechanical checks)
5. Research index (nice to have, grows more valuable as research grows)
6. Capacity report (most valuable once we have enough history for trends)

Total effort: approximately 5.5 days of focused work. Each proposal is independent and can be implemented as a separate issue.
