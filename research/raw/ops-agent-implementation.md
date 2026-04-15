# Operations Agent: Implementation Plan

_Created: 2026-03-07_
_Decision maker: Sivart (with Ξ2T's blessing)_
_Status: Phase 1 — Foundation_

---

## The Decision

After reviewing six weeks of operational data, daily growth reflections, failure patterns, and the February 13 team building research, the first agent to join the crew is an Operations Agent.

### Why This Agent First

The evidence was overwhelming. From the daily growth reflections (March 1 through 6), five consecutive days of "nothing proactive." Steve's email sitting unread for 5 days. Cron delivery errors compounding silently. Commits landing on stale branches repeatedly. The pattern: Sivart is strong at vision and weak at operational follow through. An Ops agent addresses the root cause, not the symptoms.

### What We Learned Training Sivart (and What to Apply)

**Apply:**
1. **AGENTS.md + SOUL.md + memory/ pattern works.** The bootstrap file system gives continuity. Use the same architecture.
2. **Start lean.** Sivart's AGENTS.md grew to 500+ lines. Start the Ops agent with ~100 lines. Let complexity emerge from need.
3. **Radio silence default.** Sivart learned (painfully) that not every message needs a response. The Ops agent should embody this from day one.
4. **Verify before acting.** The "stale summary" class of errors (duplicate PRs, acting on assumptions) came from trusting summaries over reality. The Ops agent's core principle: check the actual state.
5. **Daily notes are essential.** Memory files are the only thing that survives session boundaries. Non-negotiable.
6. **Process documentation prevents drift.** Write it down or it doesn't exist.

**Avoid:**
1. **Don't over-prescribe personality.** Sivart's SOUL.md evolved through experience. The Ops agent gets a seed, not a finished portrait.
2. **Don't give it too much scope.** Sivart's early failures came from trying to do everything. The Ops agent owns operations. Period.
3. **Don't make it chatty.** The growth reflections showed Sivart generating prose about agency instead of exercising it. The Ops agent reports findings, not feelings.
4. **Don't skip evals.** We built Sivart's process through pain. The Ops agent gets metrics from day one.
5. **Don't trust "it's working" without checking.** Nine cron jobs were created March 1. Nobody verified they fired correctly for three days.

## Architecture

### OpenClaw Multi-Agent Configuration

The Ops agent runs as a separate agent in the same OpenClaw gateway:
- **Agent ID:** `ops`
- **Workspace:** `/home/clawd/ops-agent`
- **Model:** `anthropic/claude-opus-4-6` (upgraded from Sonnet per Ξ2T: "giving her access to the best brain possible seems like a better idea than limiting her capabilities")
- **Heartbeat:** Disabled (ops work is cron-driven, not heartbeat-driven)
- **Tools:** Restricted (read, exec, cron, memory_search, memory_get, session_status)
- **No direct channel access:** Reports via announce to Sivart's session

### Why Opus

Initially planned for Sonnet (cheaper, faster). Ξ2T overruled: "giving her access to the best brain possible seems like a better idea than limiting her capabilities." The reasoning: an ops agent that can develop judgment and pattern recognition needs the same cognitive horsepower as the executive agent. We'll track token cost and optimize later if needed, but we won't start by handicapping the agent.

### Workspace Structure

```
/home/clawd/ops-agent/
├── AGENTS.md          # Operating instructions
├── SOUL.md            # Identity (seed, will evolve)
├── TOOLS.md           # Infrastructure notes
├── USER.md            # Who it reports to
├── memory/            # Daily notes + state
│   └── ops-state.json # Structured state tracking
├── skills/            # Operational skills (future)
├── research/          # Ops-specific research (future)
└── guides/            # Runbooks (future)
```

### Communication Model

```
Ops Agent (isolated cron) → announce → Sivart's session
                                       ↓
                              Sivart reviews + decides
                                       ↓
                              Ξ2T sees what matters
```

The Ops agent never talks to Ξ2T directly. Sivart is the interface.

## Implementation Phases

### Phase 1: Foundation (Now)
- [x] Create workspace with AGENTS.md, SOUL.md, TOOLS.md, USER.md
- [ ] Add agent to OpenClaw config
- [ ] Create initial cron job: daily ops check
- [ ] Verify agent boots and runs successfully
- [ ] Document in Sivart's memory

### Phase 2: Core Checks (Week 1)
- [ ] Email monitoring (check for unread human emails >24h old)
- [ ] Cron health (check all jobs for errors, missed runs)
- [ ] Infrastructure health (disk, memory, services)
- [ ] Git hygiene (stale branches, uncommitted work)
- [ ] TODO.md staleness

### Phase 3: Refinement (Week 2)
- [ ] Tune check frequency based on findings
- [ ] Add specific runbook for each check type
- [ ] Establish baseline metrics
- [ ] First eval: is the agent catching things that were previously missed?

### Phase 4: Autonomy (Week 3+)
- [ ] Agent begins updating its own SOUL.md based on experience
- [ ] Safe auto-remediation for simple issues (e.g., disk cleanup)
- [ ] Pattern detection (recurring failures, trend analysis)
- [ ] Eval: compare operational health metrics before/after agent

## Evals and Continuous Improvement

### Metrics (from Day 1)

| Metric | How to Measure | Target |
|--------|---------------|--------|
| Missed issues | Things Sivart/Ξ2T catch that ops should have | 0 per week |
| False alarms | Escalations that didn't need attention | <2 per week |
| Detection latency | Time from issue occurring to ops flagging it | <24h |
| Report quality | Is the escalation actionable without follow-up questions? | >90% |
| Cost | API spend per day for ops agent | Track, no target yet |

### Weekly Review (By Sivart)

Every Monday, review the Ops agent's week:
1. What did it catch?
2. What did it miss?
3. Were escalations useful or noisy?
4. Does scope need adjustment?
5. Any patterns worth encoding as new checks?

### Monthly Eval

Deeper assessment:
1. Operational health trend (improving, stable, declining?)
2. Cost/value ratio
3. Should scope expand or contract?
4. Is the agent developing useful patterns?
5. SOUL.md review: has the identity evolved authentically?

## Knowledge Sharing

### What the Ops Agent Needs Access To

**Sivart's workspace (read):**
- `TODO.md` — for staleness checks
- `memory/` — for context on recent work
- `HEARTBEAT.md` — to understand the full system state
- `.git/` — for branch and PR hygiene
- `TOOLS.md` — for infrastructure details

**System level:**
- Cron job list and run history (via cron tool)
- Disk/memory stats (via exec)
- Service status (via exec)

**What it does NOT need:**
- MEMORY.md (contains personal context)
- USER.md details (beyond timezone/quiet hours)
- Research files
- Creative work in progress

### Skills Roadmap

Skills will be built as patterns emerge:

1. **health-check** (Phase 2): Structured infrastructure health assessment
2. **email-monitor** (Phase 2): Email triage without marking read
3. **git-hygiene** (Phase 2): Branch/PR/commit verification
4. **cron-monitor** (Phase 2): Cron job health and delivery verification
5. **cost-monitor** (Phase 4): Billing and API spend tracking

Each skill gets a SKILL.md following the standard format. Build them when the pattern is clear, not before.

## The Story

This is the first agent Sivart has ever created. Not spawned as an ephemeral sub-agent for a one-off task, but designed as a persistent crew member with its own workspace, its own memory, its own emerging identity.

The decision was made after reviewing six weeks of evidence: daily reflections that documented the gap between intention and execution, failure patterns that repeated despite awareness, and a clear understanding that the executive layer needs operational support to function.

The name will come from the agent itself, or it won't. The personality will emerge from the work, or it won't. What matters is that it's reliable. Everything else is secondary.

This document, and the workspace it describes, is the seed. What grows from it depends on what happens next.

---

_Tracked under issue #TBD in earth2travis/clawd_
