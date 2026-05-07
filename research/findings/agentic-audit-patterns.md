---
title: "Agentic Audit Patterns"
tags: [agent, audit, security, process, compliance, governance]
related:
- agent-security
- agent-evaluation
- agentic-architecture
source: research/raw/agentic-audit-patterns.md
---
# Agentic Audit Patterns

## The Core Problem

Agentic AI systems operate with autonomy. Autonomy without accountability is dangerous. Auditing is the mechanism that maintains accountability.

For personal AI agents like Sivart, the stakes differ from lab-scale safety evaluations, but the principles transfer:
- **Process drift**: established procedures get abandoned under pressure or over time
- **Silent failures**: things break without anyone noticing
- **False confidence**: "it seems to be working" is not verification
- **Memory gaps**: decisions and context get lost between sessions

## Audit Taxonomy

### By Trigger
1. **Event-triggered**: Something goes wrong. Reactive.
2. **Periodic**: Scheduled at regular intervals. Proactive maintenance.
3. **Milestone**: At project boundaries, major decisions, or handoffs. Structural.
4. **Random**: Unscheduled spot-checks. Keeps honest.

### By Scope
1. **Process audit**: Are we following our established procedures?
2. **Content audit**: Are our files, logs, and documentation accurate and current?
3. **Decision audit**: Were our decisions well-reasoned and properly recorded?
4. **Infrastructure audit**: Is the technical setup healthy?
5. **Relationship audit**: Is the partnership working? Communication quality?

### By Depth
1. **Quick check**: Automated or scripted verification of key items. Minutes.
2. **Standard audit**: Systematic review of a specific area. 30-60 minutes.
3. **Deep audit**: Comprehensive review of everything. Hours. Done monthly.

## Patterns from the Big Labs (Adapted for Personal Agents)

**Gate Pattern (from Anthropic)**: Programmatic checks between pipeline steps. Before committing: Did I create an issue? Did I run the formatter? These are gates.

**Controlled Environment Testing (from METR)**: Before making external actions (sends, posts, deployments), verify in workspace first. Dry runs.

**Elicitation Gap (from METR)**: How much could process drift degrade quality? The gap between what our procedures say and what we actually do. Our first audit found 50% compliance; that is the elicitation gap in reverse.

**Multi-Perspective Review (from Anthropic Parallelization)**: Self-audit plus human review. The agent checks itself, but the human validates. Neither alone is sufficient.

**Audit Trail as First-Class Artifact (from OpenAI)**: Everything in version-controlled files. Git history IS the audit trail. Decisions logged with reasoning. Daily notes as journal. The workspace architecture is inherently auditable.

## Anti-Patterns to Avoid

1. **Audit theater**: Going through motions without honest assessment
2. **Over-auditing**: Spending more time checking than doing
3. **Recency bias**: Only auditing recent work. Old practices can rot silently.
4. **Self-serving audits**: Grading yourself easy
5. **Audit without remediation**: Finding problems but not fixing them

## Recommended Audit Cadence for Personal AI Agents

| Type | Frequency | Trigger |
|------|-----------|---------|
| Quick check | Every session | Session start: read files, verify state |
| Process audit | Weekly | End of week or after significant work |
| Content audit | Bi-weekly | After major project milestones |
| Decision audit | Daily | Review today's decisions |
| Deep audit | Monthly | Comprehensive review of everything |
| Incident audit | As needed | When something goes wrong (Five Whys) |

## Metrics Worth Tracking

- **Process compliance rate**: percentage of established practices actually followed
- **Decision logging rate**: percentage of significant decisions captured in the log
- **Issue discipline**: percentage of work that had an issue before starting
- **Response to findings**: Time from audit finding to remediation
- **Drift detection**: How far have practices drifted from documented procedures?
