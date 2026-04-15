# Agentic Audit Patterns — Synthesis

## The Core Problem

Agentic AI systems operate with autonomy. Autonomy without accountability is dangerous. Auditing is the mechanism that maintains accountability.

For personal AI agents (like [[Sivart]]), the stakes are different from lab-scale safety evaluations but the principles transfer:

- **Process drift** — established procedures get abandoned under pressure or over time
- **Silent failures** — things break without anyone noticing
- **False confidence** — "it seems to be working" isn't verification
- **Memory gaps** — decisions and context get lost between sessions

## Audit Taxonomy

### By Trigger

1. **Event-triggered** — Something goes wrong (incident, complaint, unexpected behavior). Reactive.
2. **Periodic** — Scheduled at regular intervals. Proactive maintenance.
3. **Milestone** — At project boundaries, major decisions, or handoffs. Structural.
4. **Random** — Unscheduled spot-checks. Keeps honest.

### By Scope

1. **Process audit** — Are we following our established procedures?
2. **Content audit** — Are our files, logs, and documentation accurate and current?
3. **Decision audit** — Were our decisions well-reasoned and properly recorded?
4. **Infrastructure audit** — Is the technical setup healthy?
5. **Relationship audit** — Is the partnership working? Communication quality?

### By Depth

1. **Quick check** — Automated or scripted verification of key items. Minutes.
2. **Standard audit** — Systematic review of a specific area. 30-60 minutes.
3. **Deep audit** — Comprehensive review of everything. Hours. Done monthly.

## Patterns from the Big Labs (Adapted for Personal Agents)

### 1. Gate Pattern (from Anthropic)

**Lab version:** Programmatic checks between pipeline steps.
**Our version:** Checkpoints built into workflows. Before committing: Did I create an issue? Did I run Prettier? Did I add to project 4? These are gates.

### 2. Controlled Environment Testing (from METR)

**Lab version:** Test dangerous capabilities in sandboxed environments.
**Our version:** Before making external actions (sends, posts, deployments), verify in workspace first. Dry runs.

### 3. Elicitation Gap (from METR)

**Lab version:** How much could post-training enhancement improve capability?
**Our version:** How much could process drift degrade quality? The gap between what our procedures say and what we actually do. Our first audit found 50% compliance — that's the elicitation gap in reverse.

### 4. Multi-Perspective Review (from Anthropic Parallelization)

**Lab version:** Run multiple evaluators on the same task.
**Our version:** Self-audit plus human review. The agent checks itself, but the human validates. Neither alone is sufficient.

### 5. Audit Trail as First-Class Artifact (from OpenAI)

**Lab version:** Accountability requires auditability.
**Our version:** Everything in version-controlled files. Git history IS the audit trail. Decisions logged with reasoning. Daily notes as journal. The workspace architecture is inherently auditable.

### 6. Evaluations Must Evolve (from All Labs)

**Lab version:** Capabilities change, evaluations must keep pace.
**Our version:** Our procedures evolve. The audit checklist must evolve with them. When we add a new practice, we add it to the audit scope.

## Anti-Patterns to Avoid

1. **Audit theater** — Going through motions without honest assessment. Checking boxes without looking.
2. **Over-auditing** — Spending more time checking than doing. Audits serve the work, not the other way around.
3. **Recency bias** — Only auditing recent work. Old practices can rot silently.
4. **Self-serving audits** — Grading yourself easy. The audit must be willing to find failure.
5. **Audit without remediation** — Finding problems but not fixing them. An audit that doesn't lead to action is a waste.

## Recommended Audit Cadence for Personal AI Agents

| Type           | Frequency     | Trigger                                  |
| -------------- | ------------- | ---------------------------------------- |
| Quick check    | Every session | Session start — read files, verify state |
| Process audit  | Weekly        | End of week or after significant work    |
| Content audit  | Bi-weekly     | After major project milestones           |
| Decision audit | Daily         | Review today's decisions                 |
| Deep audit     | Monthly       | Comprehensive review of everything       |
| Incident audit | As needed     | When something goes wrong (5 Whys)       |

## Metrics Worth Tracking

- **Process compliance rate** — % of established practices actually followed
- **Decision logging rate** — % of significant decisions captured in the log
- **Issue discipline** — % of work that had an issue before starting
- **Response to findings** — Time from audit finding to remediation
- **Drift detection** — How far have practices drifted from documented procedures?

## Sources

- Anthropic, "Building Effective AI Agents" — gate pattern, parallelization
- Anthropic, "Challenges in Evaluating AI Systems" — evaluation difficulty, false confidence
- OpenAI, "Practices for Governing Agentic AI Systems" — accountability framework
- METR, "Autonomy Evaluation Resources" — task-based evaluation, elicitation gap
- [[OpenClaw]] documentation — agent workspace patterns, heartbeat, sessions
- Our own first audit — 50% compliance finding
