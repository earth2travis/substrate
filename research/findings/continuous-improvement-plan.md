---
title: "Continuous Improvement Plan: Getting Better at Getting Better"
tags: [improvement, kaizen, process, metrics, feedback-loops]
related:
  - [[kanban-doctrine]]
  - [[lean-doctrine]]
  - [[kaizen]]
  - [[toyota-production-system]]
  - [[proof-of-work]]
  - [[agent-native-operations]]
  - [[feedback-loop-discipline]]
source: research/raw/continuous-improvement-plan.md
---

# Continuous Improvement Plan: Getting Better at Getting Better

**Research completed:** 2026-02-28
**Related:** Issue #302. Capstone of Foundation project.

## The Question

Not "how do we manage projects" but "how do we improve at managing projects." The difference matters. Skills plateau. Practices compound.

## Metrics: What to Measure

### Leading Indicators (predict future outcomes)

| Metric | What It Measures | Target | How to Collect |
|--------|-----------------|--------|----------------|
| WIP count | Issues in "In Progress" | ≤ 5 across all projects | `gh project item-list` |
| Queue depth | Issues in "Todo" | No target, trend matters | Same |
| Process compliance rate | % commits with issue refs | 95%+ | Process audit script |
| Backlog freshness | % Todo issues created in last 30 days | > 50% | Issue creation dates |

### Lagging Indicators (measure past outcomes)

| Metric | What It Measures | Target | How to Collect |
|--------|-----------------|--------|----------------|
| Cycle time | Days from issue creation to close | Trending down | Issue open/close dates |
| Throughput | Issues closed per week | Stable or rising | Weekly count |
| Completion ratio | Issues closed vs opened per week | ≥ 1.0 | Weekly ratio |
| Research output | Research files created per month | ≥ 4 | `ls research/` with dates |

### Health Indicators (system wellbeing)

| Metric | What It Measures | Warning Sign | How to Collect |
|--------|-----------------|--------------|----------------|
| Stale issue count | Issues with no activity for 30+ days | Rising | `gh issue list --json` |
| Orphan issue count | Open issues not in any project | Any > 0 | `gh issue list --json` |
| Context utilization | Sessions hitting compaction warnings | Increasing | Manual tracking |
| Handoff quality | Next session successfully restores context | Repeated re-asks | Subjective, daily notes |

### What NOT to Measure

- Lines of code. Meaningless.
- Issues created. Creating issues is not work. Closing them is.
- Commit count. Rewards splitting work for vanity metrics.
- Hours worked. We do not have hours. We have sessions.

## Feedback Loops

### Loop 1: Daily Check (Every Session Start)
**Question:** What is the state of work right now?
**Actions:** Review WIP, check for new issues/comments, verify yesterday's commits pushed.

### Loop 2: Weekly Review (Every 7 Days)
**Question:** Are we making progress on what matters?
**Actions:** Review issues closed, check completion ratio, review stale issues, update MEMORY.md.
**Output:** `reports/weekly/YYYY-WW.md`

### Loop 3: Cycle Retrospective (Every 2 Weeks)
**Question:** What should we change about how we work?
**Actions:** What went well? What was frustrating? What should we try differently?
**Output:** `reports/retro/YYYY-MM-DD.md`

### Loop 4: Monthly Review (Every 30 Days)
**Question:** Are we getting better, or just busy?
**Actions:** Trend analysis, process audit, tool evaluation, priority recalibration.

### Loop 5: Quarterly Strategy (Every 90 Days)
**Question:** Are we working on the right things?
**Actions:** Review project scope, evaluate tool stack, assess skill development, update this plan.

## Training Plan

| Quarter | Focus | Key Texts/Resources | Output |
|---------|-------|---------------------|--------|
| Q1 2026 | Lean foundations | PDCA, VSM, 5 Whys, fishbone, A3 | Research files |
| Q2 2026 | Constraint theory + quantitative methods | Goldratt _The Goal_, Monte Carlo, Little's Law | `research/theory-of-constraints/` |
| Q3 2026 | Systems thinking | Meadows _Thinking in Systems_, Senge _The Fifth Discipline_ | `research/systems-thinking/` |
| Q4 2026 | Agent-native PM patterns | Linear AI features, GitHub Copilot for PM | `research/agent-pm-patterns/` |

## Practice, Not Just Study

1. Write a cycle retrospective every two weeks. Not optional.
2. Collect metrics for one full quarter before drawing conclusions.
3. Run one PDCA experiment per month.
4. Review and update AGENTS.md quarterly.
5. Teach what you learn. Write research useful to another human/AI partnership.

## Connection to Values

**Spontaneous Order:** Good behavior emerges from good defaults. Auto-add rules route issues. Built-in workflows handle status transitions. Process audits catch drift. The human provides direction and judgment. The system provides structure and consistency.

**Cyberpunk Pragmatism:** Use what works. GitHub Projects V2 is not the platonic ideal. It is the tool we have, integrated where code lives. Every recommendation passes the pragmatism test: can we implement it this week? Does it solve a problem we actually have?
