---
title: "Project Board Configuration: Concrete Recommendations"
tags:
  - research
  - project-management
  - github
related:
  - [[2026-02-10-ai-career-convergence]]
  - [[actual-occasions]]
  - [[alfred-north-whitehead]]
  - [[api-first-interfaces]]
source: research/raw/project-board-configuration.md
---

# Project Board Configuration: Concrete Recommendations

_Research completed 2026-02-28. Related: issue #302._

## Current State

### What We Have

**Three projects:**

- Foundation (#4): Status, Priority (single select), Size (single select), Parent issue, Sub-issues progress. This is the most mature configuration. Closing out with issue #302.
- Framing (#6): Status only. No custom fields. Default configuration.
- Operations (#7): Status only. No custom fields. Default configuration.

**Labels (28):** Well organized across categories: type (bug, task, research, decision, idea, creative), domain (infra, agent, blockchain, security), status (blocked, in-progress, needs-info, needs-triage, ready-for-review), lifecycle (stale, duplicate, wontfix).

**What we are not using:** Iteration fields, roadmap views, date fields, automations, auto-add filters, auto-archive, charts/insights.

### The Gap

Foundation had Priority and Size fields. Framing and Operations have none. We are using GitHub Projects as a flat kanban board when it can function as a lightweight but powerful planning tool. The board view alone leaves planning, prioritization, and progress tracking as cognitive overhead instead of making them visible.

## What High-Performing Small Teams Do

Research across GitHub's docs, community discussions, and practitioner reports reveals consistent patterns among teams that get real value from Projects V2:

1. **Multiple purpose-built views, not one do-everything board.** A board for daily work. A table for triage. A roadmap for planning conversations. Each view answers a different question.

2. **Two to four custom fields maximum.** Enough to slice the data meaningfully, few enough that updating them is not a chore. Priority and effort/size are near universal. A third field for category or area is common. Beyond four fields, maintenance cost exceeds information value.

3. **Automations for status transitions.** Humans should not manually move cards to Done when closing an issue. The machine handles ceremony; humans handle judgment.

4. **Iteration fields for rhythm.** Even teams that do not run formal sprints benefit from a cycle field that groups work into time periods. It creates natural retrospection points and prevents the endless treadmill feeling.

5. **Auto-add rules per repository.** New issues automatically appear in the right project. No manual step means no missed issues.

6. **Auto-archive completed work.** Done items disappear from active views after a configurable delay. This keeps the board focused on live work.

## Recommended Custom Fields

### For Both Framing (#6) and Operations (#7)

Add these four fields to each project:

| Field        | Type          | Options                               | Why                                                                                                                                                                           |
| ------------ | ------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Priority** | Single select | 🔴 Urgent, 🟠 High, 🟡 Medium, 🟢 Low | Every issue needs a priority. Without it, everything is implicitly equal, which means nothing is prioritized. Foundation already had this.                                    |
| **Size**     | Single select | XS, S, M, L, XL                       | Rough effort estimate. Not hours. T-shirt sizes keep it fast and honest. Prevents taking on too many L/XL items simultaneously. Foundation already had this.                  |
| **Cycle**    | Iteration     | 2-week iterations                     | Creates rhythm. Group work by cycle to plan what fits. Roadmap view uses this for timeline. Two weeks matches our natural cadence (not Scrum sprints, just planning buckets). |
| **Area**     | Single select | (project-specific, see below)         | Groups work by domain so we can see if one area is starving or bloated.                                                                                                       |

**Area options for Framing (#6):**

- 🏗️ Infrastructure
- 📝 Content/Creative
- 🔬 Research
- 🤖 Agent
- 🌐 Web3/Farcaster
- 📊 Process

**Area options for Operations (#7):**

- 🖥️ Server/Hosting
- 🔐 Security
- 💰 Finance/Accounting
- 📧 Email/Calendar
- 🔧 Tooling
- 📋 Admin

## Recommended Views

### Framing (#6): Five Views

**1. "Board" (Board layout, default)**

- Column field: Status
- Group by: none
- Filter: `status:Todo,In Progress,In Review`
- Sort: Priority (descending)
- Purpose: Daily work view. What am I doing right now?

**2. "Backlog" (Table layout)**

- Visible columns: Title, Priority, Size, Area, Labels, Status
- Filter: `status:Todo,Backlog`
- Sort: Priority descending, then Size ascending
- Group by: Area
- Purpose: Triage and planning. What should we work on next?

**3. "Roadmap" (Roadmap layout)**

- Date field: Cycle (iteration)
- Group by: Area
- Filter: `status:Todo,In Progress,In Review`
- Purpose: Planning conversations with [[Ξ2T]]. What does the next month look like?

**4. "Active" (Table layout)**

- Visible columns: Title, Status, Linked PRs, Assignees
- Filter: `status:In Progress,In Review`
- Sort: updated date descending
- Purpose: Quick status check. What is live right now?

**5. "Done" (Table layout)**

- Visible columns: Title, Area, Size, closed date
- Filter: `status:Done`
- Sort: closed date descending
- Limit: last 30 items (auto-archive older)
- Purpose: Retrospective. What did we accomplish recently?

### Operations (#7): Four Views

**1. "Board" (Board layout, default)**

- Column field: Status
- Filter: `status:Todo,In Progress,In Review`
- Sort: Priority descending
- Purpose: Active ops work.

**2. "By Area" (Table layout)**

- Visible columns: Title, Priority, Status, Area
- Group by: Area
- Filter: `-status:Done`
- Purpose: Are we neglecting any operational domain?

**3. "Urgent" (Table layout)**

- Visible columns: Title, Status, Area, Labels
- Filter: `priority:🔴 Urgent,🟠 High`
- Sort: Priority descending
- Purpose: What needs attention now? Quick scan.

**4. "Log" (Table layout)**

- Visible columns: Title, Area, Status, closed date
- Filter: `status:Done`
- Sort: closed date descending
- Purpose: Operational record. What maintenance was done?

## Automations

### Built-in Workflows to Enable (Both Projects)

GitHub Projects V2 has built-in workflows under Settings > Workflows:

| Workflow      | Trigger                          | Action                 | Enable?                    |
| ------------- | -------------------------------- | ---------------------- | -------------------------- |
| Item added    | Issue/PR added to project        | Set status to **Todo** | ✅ Yes                     |
| Item closed   | Issue closed                     | Set status to **Done** | ✅ Yes (likely already on) |
| Item reopened | Issue reopened                   | Set status to **Todo** | ✅ Yes                     |
| PR merged     | Pull request merged              | Set status to **Done** | ✅ Yes                     |
| Auto-archive  | Status = Done for 14 days        | Archive item           | ✅ Yes                     |
| Auto-add      | New issue in earth2travis/sivart | Add to project         | See below                  |

### Auto-Add Rules

Configure auto-add on each project so issues arrive automatically:

**Framing (#6):** Auto-add issues with labels: `research`, `task`, `enhancement`, `idea`, `creative`, `agent`, `blockchain`
**Operations (#7):** Auto-add issues with labels: `infra`, `security`, `config`, `incident`

This eliminates the manual step of adding issues to projects. The label applied at creation routes the issue. Issues with ambiguous labels (like `bug`) get manually triaged.

### GitHub Actions Automation (Future)

For automations beyond built-in workflows, a GitHub Action can:

1. **Auto-set Priority based on labels.** Issues labeled `incident` or `security` get Priority = Urgent automatically.
2. **Stale issue detection.** Issues in "In Progress" for more than 14 days with no activity get labeled `stale` and a comment requesting status update.
3. **Cycle rollover.** At the end of each iteration, unfinished items flag for review rather than silently rolling into the next cycle.
4. **Weekly digest.** Generate a summary of issues opened, closed, and still in progress, posted to a file or notification.

These are worth implementing after the basic field and view setup is stable. Do not build all automations at once.

## Implementation Plan

### Phase 1: Fields (30 minutes)

```bash
# Add Priority to Framing
gh project field-create 6 --owner earth2travis --name "Priority" --data-type "SINGLE_SELECT" --single-select-options "🔴 Urgent,🟠 High,🟡 Medium,🟢 Low"

# Add Size to Framing
gh project field-create 6 --owner earth2travis --name "Size" --data-type "SINGLE_SELECT" --single-select-options "XS,S,M,L,XL"

# Add Area to Framing
gh project field-create 6 --owner earth2travis --name "Area" --data-type "SINGLE_SELECT" --single-select-options "🏗️ Infrastructure,📝 Content/Creative,🔬 Research,🤖 Agent,🌐 Web3/Farcaster,📊 Process"

# Add Cycle (iteration) to Framing
gh project field-create 6 --owner earth2travis --name "Cycle" --data-type "ITERATION"

# Repeat for Operations with its own Area options
gh project field-create 7 --owner earth2travis --name "Priority" --data-type "SINGLE_SELECT" --single-select-options "🔴 Urgent,🟠 High,🟡 Medium,🟢 Low"
gh project field-create 7 --owner earth2travis --name "Size" --data-type "SINGLE_SELECT" --single-select-options "XS,S,M,L,XL"
gh project field-create 7 --owner earth2travis --name "Area" --data-type "SINGLE_SELECT" --single-select-options "🖥️ Server/Hosting,🔐 Security,💰 Finance/Accounting,📧 Email/Calendar,🔧 Tooling,📋 Admin"
gh project field-create 7 --owner earth2travis --name "Cycle" --data-type "ITERATION"
```

Note: `gh project field-create` may require specific syntax; verify with `gh project field-create --help`. Views must be created through the web UI as there is no CLI command for view creation yet.

### Phase 2: Views (30 minutes, web UI)

Create the views listed above through the GitHub web interface:

1. Navigate to each project at github.com
2. Click "+ New view" for each view
3. Set layout, filters, grouping, sorting as specified
4. Save each view

### Phase 3: Automations (15 minutes, web UI)

1. Go to project Settings > Workflows
2. Enable the built-in workflows listed above
3. Configure auto-add rules per project
4. Set auto-archive to 14 days after Done

### Phase 4: Backfill Existing Issues (1 hour)

Set Priority and Area on existing open issues in Framing and Operations. This is the tedious but necessary step. Do it in one session rather than letting it drag.

### Phase 5: GitHub Actions (future, separate issue)

Build custom automations after the manual workflow is validated. Do not automate what you have not done manually first. This is a lean principle: standardize before you automate.

## What Not to Do

1. **Do not add more than four custom fields.** The temptation to track everything leads to fields nobody updates. If we find we need a fifth field, one of the existing four should be removed or merged.

2. **Do not create more than five views per project.** Views are only valuable if they are used. Too many views means none of them are the default habit.

3. **Do not use iteration fields as deadlines.** The Cycle field groups work for planning conversations. It is not a commitment mechanism. If something slips a cycle, it is information, not failure.

4. **Do not build GitHub Actions automations before validating the manual workflow.** Automate what works. Do not automate what is aspirational.

5. **Do not duplicate information across labels and custom fields.** Priority exists as a project field. Do not also create priority labels. One source of truth per dimension.

## Connection to Our Principles

**Making the invisible visible** (from origins research): every custom field and view exists to surface information that is otherwise trapped in people's heads. Priority that is not written down is not priority.

**Pull over push** (kanban principle): the board view with WIP awareness lets us pull work when we have capacity rather than pushing new issues into an already overloaded queue.

**Lightweight enough to maintain, structured enough to be useful** (from our GitHub PM guide): four fields, five views, basic automations. This is the minimum configuration that gives us meaningful visibility without creating maintenance burden.

**PDCA applied to the board itself:** Review the board configuration every quarter. Are we using all the views? Are the fields getting updated? If not, simplify. The board is a tool, not a monument.
