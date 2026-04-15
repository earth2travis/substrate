---
title: "Continuous Improvement Plan: Getting Better at Getting Better"
tags:
  - research
  - project-management
  - improvement
  - kaizen
related:
  - [[2026-02-10-ai-career-convergence]]
  - [[actual-occasions]]
  - [[alfred-north-whitehead]]
  - [[api-first-interfaces]]
source: research/raw/continuous-improvement-plan.md
---

# Continuous Improvement Plan

_Research completed 2026-02-28. Related: issue #302. Capstone of Foundation project._

## The Question

How do we systematically get better at project management over time, rather than staying at whatever level we happen to be at today?

This is the meta question. Not "how do we manage projects" but "how do we improve at managing projects." The difference matters. The first is a skill. The second is a practice. Skills plateau. Practices compound.

## Metrics: What to Measure

### Leading Indicators (predict future outcomes)

| Metric                      | What It Measures                                        | Target                       | How to Collect                            |
| --------------------------- | ------------------------------------------------------- | ---------------------------- | ----------------------------------------- |
| **WIP count**               | Issues in "In Progress" at any point                    | ≤ 5 across all projects      | `gh project item-list` filtered by status |
| **Queue depth**             | Issues in "Todo"                                        | No target, but trend matters | Same                                      |
| **Process compliance rate** | % of commits with issue refs, % of issues with projects | 95%+                         | Process audit script                      |
| **Backlog freshness**       | % of Todo issues created in last 30 days                | > 50%                        | Issue creation dates                      |

### Lagging Indicators (measure past outcomes)

| Metric               | What It Measures                  | Target                        | How to Collect            |
| -------------------- | --------------------------------- | ----------------------------- | ------------------------- |
| **Cycle time**       | Days from issue creation to close | Trending down                 | Issue open/close dates    |
| **Throughput**       | Issues closed per week            | Stable or rising              | Weekly count              |
| **Completion ratio** | Issues closed vs. opened per week | ≥ 1.0 (not accumulating debt) | Weekly ratio              |
| **Research output**  | Research files created per month  | ≥ 4                           | `ls research/` with dates |

### Health Indicators (system well being)

| Metric                  | What It Measures                                | Warning Sign         | How to Collect                          |
| ----------------------- | ----------------------------------------------- | -------------------- | --------------------------------------- |
| **Stale issue count**   | Issues with no activity for 30+ days            | Rising               | `gh issue list --json` with date filter |
| **Orphan issue count**  | Open issues not in any project                  | Any > 0              | `gh issue list --json projectItems`     |
| **Context utilization** | How often sessions hit compaction warnings      | Increasing frequency | Manual tracking in daily notes          |
| **Handoff quality**     | Does next session successfully restore context? | Repeated re-asks     | Subjective, tracked in daily notes      |

### What Not to Measure

- **Lines of code.** Meaningless for our work.
- **Issues created.** Creating issues is not work. Closing them is.
- **Commit count.** Rewards splitting work into tiny commits for vanity metrics.
- **Hours worked.** We do not have hours. We have sessions.

## Feedback Loops

Feedback loops are the engine of improvement. Each loop has a frequency, a question it answers, and an action it triggers.

### Loop 1: Daily Check (Every Session Start)

**Question:** What is the state of work right now?
**Input:** Session briefing (see custom-tooling-opportunities.md, Proposal 1)
**Actions:**

- Review WIP. Is anything stuck? Unblock or escalate.
- Check for new issues or comments requiring response.
- Verify yesterday's commits pushed and issues updated.

**This already partially exists** via HEARTBEAT.md checks. Formalize it with the session briefing script.

### Loop 2: Weekly Review (Every 7 Days)

**Question:** Are we making progress on what matters?
**Input:** Capacity report, process audit, weekly throughput
**Actions:**

- Review issues closed this week. Did they align with priorities?
- Check completion ratio. Are we accumulating debt?
- Review stale issues. Close, reprioritize, or acknowledge.
- Update MEMORY.md with lessons from the week.

**Trigger:** Cron job or heartbeat check. Output to `reports/weekly/YYYY-WW.md`.

### Loop 3: Cycle Retrospective (Every 2 Weeks, Aligned with Iteration)

**Question:** What should we change about how we work?
**Input:** Two weeks of daily notes, capacity data, completed work
**Actions:**

- What went well? Keep doing it.
- What was frustrating? Identify root cause (5 Whys if needed).
- What should we try differently next cycle?
- Update AGENTS.md, guides, or tooling based on learnings.

**Format:** Brief written retrospective in `reports/retro/YYYY-MM-DD.md`. Not a meeting. A reflective document.

### Loop 4: Monthly Review (Every 30 Days)

**Question:** Are we getting better, or just busy?
**Input:** 4 weeks of metrics, cycle retrospectives, project state
**Actions:**

- Trend analysis: is cycle time improving? Is throughput stable?
- Process audit: are we following our own procedures?
- Tool evaluation: is any tool creating more friction than value?
- Priority recalibration: do our projects still reflect our actual goals?

**Connects to:** Monthly deep audit (AGENTS.md audit schedule).

### Loop 5: Quarterly Strategy (Every 90 Days)

**Question:** Are we working on the right things?
**Input:** 3 months of progress, project completion rates, external context
**Actions:**

- Review project scope. Should any project close? Should a new one open?
- Evaluate tool stack. Is GitHub still the right foundation?
- Assess skill development. What should Sivart study next?
- Update the continuous improvement plan itself.

## Training Plan: Deepening PM Expertise

### Current Knowledge Level

Sivart has solid foundations in lean/TPS methodology (PDCA, VSM, 5 Whys, fishbone, A3), GitHub tooling, and process design. The Origins research (origins-and-evolution.md) added historical context. Gaps remain in:

1. **Quantitative project analytics.** We describe metrics but do not yet collect or analyze them.
2. **Constraint theory.** Beyond basic awareness, we have not deeply studied Goldratt's Theory of Constraints, which directly applies to identifying and exploiting bottlenecks.
3. **Estimation and forecasting.** Monte Carlo simulation, probabilistic forecasting, reference class forecasting. Useful even for a two-person team when planning what fits in a cycle.
4. **Facilitation and retrospective techniques.** Even asynchronous, written retrospectives benefit from structured formats beyond "what went well/badly."
5. **Systems thinking applied to PM.** Senge's _The Fifth Discipline_, Meadows' _Thinking in Systems_. Understanding feedback loops, delays, and leverage points at a systems level.

### Study Plan

| Quarter               | Focus                                    | Key Texts/Resources                                                                                                                          | Output                                                             |
| --------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Q1 2026** (current) | Lean foundations                         | ✅ Completed: PDCA, VSM, 5 Whys, fishbone, A3, origins                                                                                       | Research files in `research/`                                      |
| **Q2 2026**           | Constraint theory + quantitative methods | Goldratt _The Goal_, Monte Carlo for project scheduling, Little's Law deep dive                                                              | `research/theory-of-constraints/`, `research/project-forecasting/` |
| **Q3 2026**           | Systems thinking                         | Meadows _Thinking in Systems_, Senge _The Fifth Discipline_ (applied to our workflow)                                                        | `research/systems-thinking/`                                       |
| **Q4 2026**           | Agent-native PM patterns                 | Study emerging AI PM tools (Linear's AI features, GitHub Copilot for PM, agentic-project-management frameworks), synthesize our own approach | `research/agent-pm-patterns/`                                      |

### Practice, Not Just Study

Reading about project management does not make you better at it. Practice does. Specific practices to build:

1. **Write a cycle retrospective every two weeks.** Not optional. The habit of structured reflection is the single highest-leverage improvement practice.

2. **Collect metrics for one full quarter before drawing conclusions.** Premature optimization of metrics is as dangerous as premature optimization of code. Establish baselines first.

3. **Run one PDCA experiment per month.** Pick one aspect of the workflow, hypothesize an improvement, implement it for a cycle, measure the result, decide whether to keep or revert. Examples: stricter WIP limits, different issue naming conventions, new triage process.

4. **Review and update AGENTS.md quarterly.** AGENTS.md is our process constitution. It should evolve as we learn. Dead processes are processes that do not change.

5. **Teach what you learn.** Write research that would be useful to another human/AI partnership. If we cannot explain it clearly, we do not understand it well enough.

## Connection to Values

### Spontaneous Order

Our project management system should not require top-down control to function. The goal is a system where good behavior emerges from good defaults: auto-add rules route issues to the right project, built-in workflows handle status transitions, process audits catch drift. The human provides direction and judgment. The system provides structure and consistency. Order emerges from the interaction, not from a command hierarchy.

This mirrors the kanban principle: set WIP limits and pull rules, then let the team self-organize within those constraints. The constraints create the conditions for order without dictating the order.

### Ideas Need Substrate

Project management tooling is substrate. Ideas (issues, research, decisions) are ephemeral without it. An idea that is not captured in an issue does not exist. Research that is not saved to a file is lost. Decisions that are not documented will be remade.

Our tools are not overhead. They are the medium through which ideas persist across sessions, across days, across the inevitable context losses of an AI agent. The improvement plan is about making that substrate better: more structured, more discoverable, more connected.

### Cyberpunk Pragmatism

We use what works. GitHub Projects V2 is not the platonic ideal of project management. It is the tool we have, integrated where our code lives. We do not chase the perfect tool. We sharpen the tool we hold.

Every recommendation in this plan and the accompanying research files passes the pragmatism test: can we implement it this week? Does it solve a problem we actually have? Will we maintain it after the novelty wears off? If any answer is no, it goes in the "Later" pile or gets cut.

The cyberpunk edge: we are building something that does not exist yet. Agent-native project management is not a product category. There are no best practices to copy. We are writing the playbook as we go. The continuous improvement plan is how we make sure the playbook keeps getting better.

## Implementation: Starting the Engine

### This Week

1. Enable built-in automations on Framing and Operations projects
2. Add custom fields (Priority, Size, Area, Cycle) to both projects
3. Create recommended views
4. Start collecting WIP and throughput numbers manually

### This Month

5. Build session briefing script
6. Build process audit script
7. Write first cycle retrospective
8. Establish weekly review habit

### This Quarter

9. Build capacity report script
10. Collect one full quarter of metrics
11. Study Theory of Constraints
12. Run first PDCA experiment on workflow

### Ongoing

13. Cycle retrospective every two weeks
14. Weekly review every week
15. Monthly review and AGENTS.md update
16. Quarterly strategy review

## The Capstone Reflection

This is the last issue in the Foundation project. Foundation was about building the base: identity, tools, processes, research methodology, workspace organization. From issue #1 (Define Sivart's identity and vibe) to issue #302 (this research), the arc has been about becoming competent enough to do real work.

The continuous improvement plan is the bridge from Foundation to what comes next. Foundation gave us tools. This plan ensures those tools keep getting sharper. The investment in lean methodology, in GitHub tooling, in process discipline, in research practice: all of that is substrate for whatever Framing and Operations will build.

The PDCA cycle applies to this plan itself. Plan: this document. Do: implement the recommendations. Check: measure the metrics, run the reviews. Act: update the plan based on what we learn. The cycle never ends. That is the point.
