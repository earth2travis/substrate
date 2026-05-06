---
title: "Project Board Configuration: GitHub Projects V2 Recommendations"
tags: [github, project-management, kanban, configuration, automation, process]
related: [[github-as-memory]], [[kanban-doctrine]], [[lean-software-delivery]], [[harness-engineering]], [[custom-tooling-opportunities]]
source: research/raw/project-board-configuration.md
---

# Project Board Configuration: GitHub Projects V2 Recommendations

## Summary

Research on GitHub Projects V2 configuration for three projects (Foundation, Framing, Operations). Foundation has Priority and Size fields. Framing and Operations have only Status. The gap: using GitHub Projects as flat kanban boards when they can function as lightweight but powerful planning tools. Recommendations: four custom fields, multiple purpose-built views, built-in automations, and auto-add rules.

## Current State

**Three projects:** Foundation (#4) has Status, Priority, Size, Parent issue, Sub-issues progress. Framing (#6) and Operations (#7) have Status only.

**Labels (28):** Well organized across type, domain, status, and lifecycle categories.

**Not using:** Iteration fields, roadmap views, date fields, automations, auto-add filters, auto-archive, charts/insights.

## What High-Performing Small Teams Do

1. **Multiple purpose-built views**, not one do-everything board
2. **Two to four custom fields maximum** — enough to slice data, few enough to maintain
3. **Automations for status transitions** — humans handle judgment, machines handle ceremony
4. **Iteration fields for rhythm** — natural retrospection points
5. **Auto-add rules per repository** — new issues appear automatically
6. **Auto-archive completed work** — keeps board focused on live work

## Recommended Custom Fields

Four fields for Framing and Operations:
- **Priority** (Single select): Urgent, High, Medium, Low
- **Size** (Single select): XS, S, M, L, XL — rough effort estimate
- **Cycle** (Iteration): 2-week iterations for planning buckets
- **Area** (Single select): project-specific domain grouping

## Recommended Views

**Framing (#6):** Board (daily work), Backlog (triage and planning), Roadmap (planning conversations), Active (quick status check), Done (retrospective).

**Operations (#7):** Board (active ops), By Area (domain check), Urgent (attention now), Log (operational record).

## Automations

**Built-in workflows:** Item added → Set status to Todo. Item closed → Set status to Done. Item reopened → Set status to Todo. PR merged → Set status to Done. Auto-archive after 14 days in Done.

**Auto-add rules:** Framing adds issues with labels research, task, enhancement, idea, creative, agent, blockchain. Operations adds issues with labels infra, security, config, incident.

**Future GitHub Actions:** Auto-set Priority based on labels, stale issue detection, cycle rollover, weekly digest.

## Implementation Order

1. Fields (30 minutes via CLI)
2. Views (30 minutes via web UI)
3. Automations (15 minutes via web UI)
4. Backfill existing issues (1 hour)
5. GitHub Actions (future, separate issue)

## Connection to Our Principles

**Making the invisible visible:** Every custom field and view exists to surface information otherwise trapped in people's heads. Priority that is not written down is not priority.

**Pull over push:** Board view with WIP awareness lets us pull work when we have capacity rather than pushing new issues into an overloaded queue.

**PDCA applied to the board itself:** Review configuration quarterly. Are we using all views? Are fields getting updated? If not, simplify.

## Related

- [[github-as-memory]] — Issues as institutional knowledge graph
- [[kanban-doctrine]] — Auftragstaktik as agent operating system
- [[lean-software-delivery]] — Continuous improvement
- [[harness-engineering]] — Agent-first development
- [[custom-tooling-opportunities]] — Agent-native tooling for process compliance
