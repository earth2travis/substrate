---
title: Feedback Loop Discipline
tags:
- process
- improvement
- kaizen
- metrics
- feedback
related:
- kanban-doctrine
- lean-doctrine
- kaizen
- toyota-production-system
- proof-of-work
- reference-free-evaluation
- agent-native-operations
- per-run-learning
source: research/findings/continuous-improvement-plan.md
---




# Feedback Loop Discipline

A system of nested feedback loops at different frequencies, each answering a different question about organizational health. Not a dashboard. A practice.

## The Five Loops

### Loop 1: Daily Check
**Question:** What is the state of work right now?
**Actions:** Review WIP. Check for stuck items. Verify yesterday's commits pushed and issues updated.
**Frequency:** Every session start.

### Loop 2: Weekly Review
**Question:** Are we making progress on what matters?
**Actions:** Review issues closed. Check completion ratio. Review stale issues. Update MEMORY.md with lessons.
**Frequency:** Every 7 days.
**Output:** `reports/weekly/YYYY-WW.md`

### Loop 3: Cycle Retrospective
**Question:** What should we change about how we work?
**Actions:** What went well? What was frustrating? What should we try differently?
**Frequency:** Every 2 weeks.
**Output:** `reports/retro/YYYY-MM-DD.md`

### Loop 4: Monthly Review
**Question:** Are we getting better, or just busy?
**Actions:** Trend analysis. Process audit. Tool evaluation. Priority recalibration.
**Frequency:** Every 30 days.

### Loop 5: Quarterly Strategy
**Question:** Are we working on the right things?
**Actions:** Review project scope. Evaluate tool stack. Assess skill development. Update the plan itself.
**Frequency:** Every 90 days.

## Metrics by Layer

**Leading indicators** predict future outcomes: WIP count, queue depth, process compliance rate, backlog freshness.

**Lagging indicators** measure past outcomes: cycle time, throughput, completion ratio, research output.

**Health indicators** signal system wellbeing: stale issue count, orphan issue count, context utilization, handoff quality.

### What Not to Measure
Lines of code. Issues created. Commit count. Hours worked. These are vanity metrics that reward the wrong behavior.

## The PDCA Engine

Each loop is a PDCA cycle: Plan, Do, Check, Act. The quarterly loop plans strategy. The daily loop plans the next few hours. The same structure at different time scales.

The critical insight: the plan itself must be subject to PDCA. Review and update the continuous improvement plan quarterly. Dead processes are processes that do not change.

## Implementation Discipline

**This week:** Enable automations, add custom fields, start collecting WIP and throughput manually.

**This month:** Build session briefing script, build process audit script, write first cycle retrospective, establish weekly review habit.

**This quarter:** Build capacity report script, collect one full quarter of metrics, run first PDCA experiment on workflow.

**Ongoing:** Cycle retrospective every two weeks. Weekly review every week. Monthly review and AGENTS.md update. Quarterly strategy review.

## Connection to Lean Principles

This is kanban applied to a human-agent partnership. Set WIP limits and pull rules, then let the system self-organize within those constraints. The constraints create the conditions for order without dictating the order.

**Spontaneous order:** Good behavior emerges from good defaults. Auto-add rules route issues. Built-in workflows handle transitions. Process audits catch drift. The human provides direction and judgment. The system provides structure and consistency.

**Cyberpunk pragmatism:** Every recommendation passes the test: can we implement it this week? Does it solve a problem we actually have? Will we maintain it after the novelty wears off?
