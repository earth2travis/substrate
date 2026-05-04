---
title: "Hermes Kanban: Deep Dive — Capabilities, History, and Philosophy"
created: 2026-05-04
updated: 2026-05-04
type: concept
tags: [kanban, hermes, operations, multi-agent, workflow, toyota, lean]
related:
  - [[taiichi-ohno]]
  - [[toyota-production-system]]
  - [[value-stream-mapping]]
  - [[research/raw/hermes-kanban-tutorial]]
source: |
  https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
  https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-tutorial
  docs/hermes-kanban-v1-spec.pdf (Nous Research internal)
  Anderson 2010, Kanban: Successful Evolutionary Change for Your Technology Business
  Womack & Jones 1990, The Machine That Changed the World
  Ohno 1988, Toyota Production System: Beyond Large-Scale Production
---

# Hermes Kanban: Deep Dive — Capabilities, History, and Philosophy

> This document is a full-spectrum recon on Kanban: where it came from, what it means, and how Hermes Agent implements it as a multi-agent coordination primitive. It is written for the operator who needs to reason about fleet behavior, not just run commands.

---

## Part I: Hermes Kanban — What Is Possible

### The Core Primitive

Hermes Kanban is a durable task board, shared across all Hermes profiles, backed by a single SQLite database at `~/.hermes/kanban.db`. Every task is a row. Every handoff is a row anyone can read and write. Every worker is a full OS process with its own identity, memory, and toolset.

This is not a project management tool bolted onto an agent. It is a coordination primitive: the shape that covers workloads `delegate_task` cannot.

### What It Covers That `delegate_task` Does Not

| Dimension | `delegate_task` | Kanban |
|---|---|---|
| Shape | RPC call (fork → join) | Durable message queue + state machine |
| Parent | Blocks until child returns | Fire-and-forget after create |
| Child identity | Anonymous subagent | Named profile with persistent memory |
| Resumability | None — failed = failed | Block → unblock → re-run; crash → reclaim |
| Human in the loop | Not supported | Comment / unblock at any point |
| Agents per task | One call = one subagent | N agents over task's life (retry, review, follow-up) |
| Audit trail | Lost on context compression | Durable rows in SQLite forever |
| Coordination | Hierarchical (caller → callee) | Peer — any profile reads/writes any task |

One-sentence distinction: `delegate_task` is a function call; Kanban is a work queue where every handoff is a row any profile (or human) can see and edit.

### The Board: Six Columns

The dashboard and CLI share the same six-column model:

1. **Triage** — raw ideas, a specifier fleshes out the spec before anyone works on them.
2. **Todo** — created but waiting on dependencies, or not yet assigned.
3. **Ready** — assigned and waiting for the dispatcher to claim.
4. **In Progress** — a worker is actively running the task. Sub-groups by assignee when "Lanes by profile" is on.
5. **Blocked** — a worker asked for human input, or the circuit breaker tripped.
6. **Done** — completed.

### The Dispatcher: The Engine

A long-lived loop inside the gateway process (default: `kanban.dispatch_in_gateway: true`). Every N seconds (default 60), it does the following atomically:

- Reclaims stale claims (TTL expired).
- Reclaims crashed workers (PID gone but TTL not yet expired).
- Promotes tasks whose parents are all `done` from `todo` to `ready`.
- Claims ready tasks and spawns the assigned profile as a worker process.

After ~5 consecutive spawn failures on the same task, the dispatcher auto-blocks it. This is the circuit breaker. Prevents thrashing on tasks whose profile does not exist, workspace cannot mount, or credentials are missing.

### The Worker Toolset: Seven Tools

When a worker is spawned, `HERMES_KANBAN_TASK` is set in its environment. This gate unlocks a dedicated toolset the normal agent schema never sees:

| Tool | Purpose |
|---|---|
| `kanban_show` | Read the current task (title, body, prior attempts, comments, context). |
| `kanban_complete` | Finish with summary + metadata structured handoff. |
| `kanban_block` | Escalate for human input. |
| `kanban_heartbeat` | Signal liveness during long operations. |
| `kanban_comment` | Append to the task thread. |
| `kanban_create` | (Orchestrators) Fan out into child tasks. |
| `kanban_link` | (Orchestrators) Add dependency edges after the fact. |

Why tools and not CLI? Three reasons: backend portability (works across Docker/Modal/SSH), no shell-quoting fragility, and structured JSON errors the model can reason about. Zero schema footprint on normal sessions.

### Workspaces: Three Kinds

| Kind | What It Is | Use Case |
|---|---|---|
| `scratch` | Fresh tmp dir, GC'd on archive | Research, ephemeral computation |
| `dir:<absolute_path>` | Shared persistent directory | Obsidian vault, ops scripts repo, per-account folder |
| `worktree` | Git worktree under `.worktrees/<id>/` | Coding tasks with branch isolation |

Relative paths are rejected at dispatch as a confused-deputy escape vector. The path is otherwise trusted: your box, your filesystem, your uid.

### Dependency Engine: Parent → Child Promotion

Tasks can have parent-child links. A child in `todo` stays there until every parent reaches `done`, then auto-promotes to `ready`. No manual coordination. The dispatcher and dependency engine handle it.

This is the pipeline primitive: `pm → backend-eng → reviewer` with each stage gated by the prior.

### Idempotent Create (for Automation)

```
hermes kanban create "nightly ops review" \
    --assignee ops \
    --idempotency-key "nightly-ops-$(date -u +%Y-%m-%d)" \
    --json
```

First call creates the task. Subsequent calls with the same key return the existing task id. This is critical for cron jobs and webhooks that might fire twice.

### Task Pinning: Skills Attached to Tasks

A single task can load extra skills beyond the built-in `kanban-worker`:

```
hermes kanban create "audit auth flow" \
    --assignee reviewer \
    --skill security-pr-audit \
    --skill github-code-review
```

The dispatcher passes `--skills <name>` for each. The worker spawns with all of them loaded. No need to edit the assignee's profile.

### The Orchestrator Skill

The `kanban-orchestrator` skill encodes the decomposition playbook: anti-temptation rules, a standard specialist roster (`researcher`, `analyst`, `writer`, `backend-eng`, `reviewer`, `ops`, `pm`), and a step-by-step pattern for fan-out, pipeline, and human-in-the-loop workflows.

For best results, pair it with a profile whose toolsets are restricted to board operations so the orchestrator literally cannot execute implementation tasks even if it tries.

### Dashboard (GUI)

A bundled plugin at `plugins/kanban/`. Open with `hermes dashboard`, click the Kanban tab.

What it gives you:
- Drag-and-drop cards between columns.
- Inline create on any column header.
- Multi-select with bulk actions (shift/ctrl-click).
- Per-card drawer: editable title, assignee, priority, description (markdown-rendered), dependency editor, status actions, result section, comment thread, last 20 events.
- Live updates via WebSocket tailing the append-only `task_events` table.
- Per-profile lanes inside Running.
- Filters: search, tenant, assignee, archived toggle, lanes toggle.
- Nudge dispatcher button for immediate dispatch tick.

The GUI is strictly read-through-the-DB + write-through-kanban_db. No domain logic of its own. Everything the plugin does is reachable from the CLI.

### REST Surface

| Method | Path | Purpose |
|---|---|---|
| GET | `/board` | Full board grouped by status |
| GET | `/tasks/:id` | Task + comments + events + links + runs |
| POST | `/tasks` | Create (wraps `kanban_db.create_task`) |
| PATCH | `/tasks/:id` | Status / assignee / priority / title / body / result |
| POST | `/tasks/bulk` | Batch patch across ids |
| POST | `/tasks/:id/comments` | Append comment |
| POST | `/links` | Add dependency |
| DELETE | `/links` | Remove dependency |
| POST | `/dispatch` | Nudge the dispatcher |
| GET | `/config` | Read dashboard preferences |
| WS | `/events` | Live stream of `task_events` rows |

### Gateway Notifications

When you run `/kanban create` from a gateway chat (Telegram, Discord, Slack), the originating chat is auto-subscribed. The notifier polls `task_events` and delivers one message per terminal event (`completed`, `blocked`, `gave_up`, `crashed`, `timed_out`) to that chat. Completed tasks also send the first line of the worker's `--result`.

Subscriptions auto-remove once the task reaches `done` or `archived`.

### Runs: One Row Per Attempt

A task is a logical unit of work; a run is one attempt to execute it. The `task_runs` table captures:

- Outcome (`completed`, `blocked`, `crashed`, `timed_out`, `spawn_failed`, `gave_up`, `reclaimed`).
- Summary and metadata (structured handoff).
- Elapsed time, profile, timestamp.

Downstream children read the most recent completed run's summary + metadata for each parent. Retrying workers read prior attempts so they do not repeat a failed path. This replaces the "dig through comments" dance of flat kanban systems.

Bulk close with `--summary` is refused: structured handoff is per-run, and copy-pasting the same summary to N tasks is almost always wrong.

### Eight Canonical Collaboration Patterns

| Pattern | Shape | Example |
|---|---|---|
| P1 Fan-out | N siblings, same role | "Research 5 angles in parallel" |
| P2 Pipeline | Role chain: scout → editor → writer | Daily brief assembly |
| P3 Voting / Quorum | N siblings + 1 aggregator | 3 researchers → 1 reviewer picks |
| P4 Long-running Journal | Same profile + shared dir + cron | Obsidian vault accumulation |
| P5 Human-in-the-Loop | Worker blocks → user comments → unblock | Ambiguous decisions |
| P6 @mention | Inline routing from prose | @reviewer look at this |
| P7 Thread-scoped Workspace | `/kanban here` in a thread | Per-project gateway threads |
| P8 Fleet Farming | One profile, N subjects | 50 social accounts |
| P9 Triage Specifier | Rough idea → triage → specifier → todo | "Turn this one-liner into a spec" |

### Multi-Tenant Usage

Tag tasks with `--tenant <name>` and `--workspace dir:<tenant_path>`. Workers receive `HERMES_TENANT` and namespace memory writes by prefix. The board, dispatcher, and profiles are shared; only data is scoped.

---

## Part II: History and Philosophy of Kanban

### Origins: Taiichi Ohno and the Toyota Production System (1940s–1960s)

Kanban (看板) means "visual signboard" or "card." It emerged not as a software methodology but as a physical control mechanism on the factory floor of Toyota Motor Corporation in postwar Japan.

**Taiichi Ohno** (1912–1990) is the central figure. Joining Toyota in 1943, he was promoted to plant manager around 1949 and tasked with making production viable in a country with scarce capital, low demand, and no room for inventory buffers. He studied Ford's mass production and rejected it. Ford made only what the schedule dictated, regardless of actual demand. That created waste: overproduction, warehousing, obsolescence.

Ohno's insight came from American supermarkets. A customer takes what they need; the shelf is restocked only when empty. The empty shelf is the signal. He adapted this to manufacturing: a downstream process withdraws parts from an upstream process only when needed, using a physical card (the kanban) as the signal.

The core doctrine:

> "Make only what is needed, when it is needed, in the amount needed."

This is **Just-in-Time (JIT)** production. It is inseparable from **Jidoka** (autonomation): machines stop when abnormalities occur, giving workers authority and obligation to fix problems immediately. The Andon cord on Toyota's assembly lines is the physical manifestation of this philosophy: any worker can halt the entire line.

Ohno identified **seven wastes (muda)**: overproduction, waiting, transportation, over-processing, inventory, motion, defects. The entire TPS is an apparatus for exposing and eliminating these wastes. Inventory is not an asset; it is a symptom of dysfunction. Buffers hide problems. Kanban exposes them.

Key dates:
- 1956: Ohno visits the United States, observing Ford lines and supermarket logistics firsthand.
- 1960s–1970s: TPS matures with heijunka (production leveling), standardized work, and continuous improvement (kaizen).
- 1988: Ohno publishes *Toyota Production System: Beyond Large-Scale Production*.

### Lean Manufacturing: Womack, Jones, and the Universalization of TPS (1990)

The Toyota Production System remained largely inside Japan until the **MIT International Motor Vehicle Program (IMVP)**, a five-year study (1984–1989) led by James P. Womack, Daniel T. Jones, and Daniel Roos. They coined the term **"Lean"** to describe TPS and its relatives, publishing *The Machine That Changed the World* in 1990.

In 1996, Womack and Jones published *Lean Thinking*, codifying five principles:

1. **Identify Value** — Define value from the customer perspective.
2. **Map the Value Stream** — Identify all actions to deliver product; eliminate non-value-adding steps.
3. **Create Flow** — Make value-adding steps occur without interruption.
4. **Establish Pull** — Let customer demand trigger production, not forecast schedules.
5. **Seek Perfection** — Pursue continuous improvement relentlessly.

Lean universalized Ohno's shop-floor practices into a management philosophy applicable to any industry. It framed waste as a symptom of deeper systemic failures. Centralized, forecast-driven planning is inherently flawed; only direct pull from real demand creates efficiency.

### David Anderson and the Kanban Method for Knowledge Work (2004+)

The leap from manufacturing to software was not automatic. Software is not a physical product. Requirements emerge. Work is variable. You cannot standardize knowledge work the way you standardize an assembly line.

**David J. Anderson** made the bridge. In 2004, while at Microsoft, he adapted kanban-inspired flow management to software engineering maintenance and feature teams. He had experimented earlier at Sprint and BellSouth. The key realization: the physical card is not the point. The point is the **pull signal**, the **WIP limit**, and the **visual management** of flow.

Anderson's Kanban Method, published in *Kanban: Successful Evolutionary Change for Your Technology Business* (2010), rests on four foundational principles:

1. **Start with what you do now.**
2. **Agree to pursue incremental, evolutionary change.**
3. **Respect the current process, roles, responsibilities, and titles.**
4. **Encourage acts of leadership at every level.**

And six core practices:

1. **Visualize workflow.**
2. **Limit Work In Progress (WIP).**
3. **Manage flow.**
4. **Make process policies explicit.**
5. **Implement feedback loops (cadences).**
6. **Improve collaboratively, evolve experimentally.**

The philosophy is one of **evolutionary systems change**: lower resistance by respecting current state, then use flow data to drive improvements. It treats the workflow as a **service delivery system** with customers, not merely a production pipeline.

In knowledge work, the container analogy becomes a ticket on a digital board. The signal mechanism is an empty WIP slot. Routing is emergent and policy-defined, not fixed. The primary goal shifts from zero inventory to **optimal flow** and **short, predictable lead time**.

### Core Concepts in Depth

**Pull Systems**
In production, physical kanban cards circulate between stations. A downstream station removes parts and sends the card upstream as a production order. The upstream station does not produce until the card returns.

In knowledge work, virtual signals (empty slots on a board) indicate capacity to accept new work. Team members pull the next highest-priority item from a queue only when WIP limits permit. This prevents overload and aligns work initiation with completion capacity.

**WIP Limits**
Explicitly enforced caps on the number of work items allowed in any given workflow state (e.g., "In Progress = 3"). This forces idle capacity at non-bottlenecks, making bottlenecks visible. It reduces context-switching and multitasking overhead. The philosophy: busyness is not efficiency. Limiting WIP improves lead time predictability and quality by focusing attention.

**Flow**
The smooth movement of work items from commitment point to delivery. Metrics include lead time, cycle time, throughput, and the Cumulative Flow Diagram (CFD). The goal is to optimize **flow efficiency** (time spent actively adding value vs waiting) rather than **resource efficiency** (utilization percentage). A system with high utilization often exhibits poor flow due to queuing delays.

**Visual Management**
The kanban board with columns representing workflow states. Elements: work item cards, avatars/assignees, blocked indicators, explicit policies under each column, class-of-service markers. Purpose: create a single source of truth, enable self-organization, and make dysfunctions immediately visible without status reports.

**Cadence**
Regular, predictable intervals for specific coordination activities. Unlike Scrum, cadences are decoupled from delivery. Kanban teams may hold replenishment meetings weekly, retrospectives bi-weekly, and releases on demand. Cadence reduces coordination cost and decision fatigue while maintaining rhythm.

**Evolutionary Change**
Transformational change (big-bang reorganization) creates resistance and fails because it ignores local context. Evolutionary change introduces small, continuous experiments (kaizen). WIP limits expose constraints; teams apply Theory of Constraints thinking or PDCA (Plan-Do-Check-Act) cycles to resolve them. Changes are reversible and low-risk.

**Service-Oriented Workflow**
Work is not merely "tasks"; it is a service delivered to customers (internal or external). Classes of Service (Standard, Expedite, Fixed Date, Intangible) each have explicit policies for entry, handling, and exit. The service is evaluated by whether it satisfies customer purpose, not just whether it met technical specifications.

### Production Kanban vs. Knowledge-Work Kanban

| Dimension | Production Kanban | Knowledge-Work Kanban |
|---|---|---|
| Work Unit | Physical parts/components | Intangible items (tickets, stories) |
| Variability | Low; standardized specs | High; emergent requirements |
| Container | Physical bin + card | Virtual ticket on digital board |
| Signal | Paper/plastic card | Empty WIP slot / board policy |
| Routing | Fixed, known stations | Emergent, policy-defined transitions |
| Primary Goal | Zero inventory, JIT delivery | Optimal flow, short predictable lead time |
| Quality Method | Jidoka / stop-the-line | Explicit policies / Definition of Done |
| Time Tracking | Cycle time highly predictable | Probabilistic forecasting (Monte Carlo) |
| WIP Limit Basis | Physical space, takt time | Team capacity, cognitive load limits |

The key philosophical difference: production Kanban optimizes a repeatable conversion process. Knowledge-work Kanban optimizes a discovery-and-delivery process where the act of doing the work reveals what the work actually is. Therefore, knowledge-work Kanban embraces variability and uses flow metrics for probabilistic forecasting rather than deterministic scheduling.

### Kanban vs. Scrum

| Feature | Kanban | Scrum |
|---|---|---|
| Change Philosophy | Evolutionary | Revolutionary (framework adoption) |
| Work Cadence | Continuous flow | Time-boxed Sprints (1–4 weeks) |
| Roles Prescribed | None required | Product Owner, Scrum Master, Developers |
| Commitment Unit | Individual work item | Sprint Goal / whole Sprint batch |
| Planning Cycle | On-demand / replenishment | Sprint Planning (batch commitment) |
| Board State | Persistent; work stays as-is | Reset each Sprint; new board |
| WIP Limits | Central doctrine | Implicit via Sprint scope |
| Metrics Focus | Lead time, cycle time, CFD, throughput | Velocity, burndown, commitment vs completion |
| Change Mid-Stream | Allowed; pull next item anytime | Changes discouraged during Sprint |
| Ceremonies | Optional cadences; team-defined | Mandatory (Standup, Review, Retro, Planning) |
| Process Prescription | Overlay on existing process | Replace process with Scrum framework |
| Batch Size | Single-item flow | Sprint-sized batch |
| Improvement Model | Continuous kaizen via flow data | Sprint Retrospective + adaptation |

Scrum is a product development framework built on empirical process control. It assumes restructuring into cross-functional teams is necessary to expose dysfunction. Kanban is a change-management method that assumes the current system contains latent capacity and wisdom; it overlays visual controls and flow discipline without mandatory reorganization. They are not mutually exclusive: Scrumban fuses Scrum's team structure with Kanban's flow mechanics.

### Key Figures Roster

- **Taiichi Ohno** (1912–1990): Chief architect of TPS, developed JIT and pull production.
- **Eiji Toyoda** (1913–2013): Toyota president, supported Ohno's experiments.
- **Shigeo Shingo** (1909–1990): Industrial engineer, contributed SMED and defect-reduction methods.
- **James Womack / Daniel Jones / Daniel Roos**: MIT researchers, coined "Lean" (1990).
- **David J. Anderson**: Originator of Kanban Method for knowledge work (2004+), published definitive text 2010.
- **Corey Ladas**: Introduced Scrumban concept (2009).
- **Mary and Tom Poppendieck**: Translated Lean principles to software (2003–2007).
- **Don Reinertsen**: *The Principles of Product Development Flow* (2009); heavily influenced Kanban economic thinking.

---

## Part III: The Agent Skills

### kanban-worker

Auto-injected into every dispatched worker via `KANBAN_GUIDANCE`. The lifecycle:

1. On spawn, call `kanban_show()` to read title + body + parent handoffs + prior attempts + comment thread.
2. `cd $HERMES_KANBAN_WORKSPACE` and do the work there.
3. Call `kanban_heartbeat(note="...")` every few minutes during long operations.
4. Complete with `kanban_complete(summary="...", metadata={...})`, or `kanban_block(reason="...")` if stuck.

Key practices:
- Shape `metadata` so downstream parsers can use it without re-reading prose.
- Block reasons should be one specific sentence naming the decision needed.
- Heartbeats should name progress ("epoch 12/50, loss 0.31"), not just "still working."
- On retry, read prior runs' outcomes and do not repeat failed paths.
- Never modify files outside `$HERMES_KANBAN_WORKSPACE` unless instructed.
- Never use `delegate_task` as a substitute for `kanban_create`.

### kanban-orchestrator

Loaded into orchestrator profiles. The rules:

- **Do not execute the work yourself.** Route, don't execute.
- **For any concrete task, create a Kanban task and assign it.** Every single time.
- **If no specialist fits, ask the user which profile to create.** Do not default to "close enough."
- **Decompose, route, and summarize.** That is the whole job.

Standard specialist roster: `researcher`, `analyst`, `writer`, `reviewer`, `backend-eng`, `frontend-eng`, `ops`, `pm`.

Decomposition playbook:
1. Understand the goal (ask clarifying questions).
2. Sketch the task graph out loud before creating anything.
3. Create tasks and link them with `parents=[...]`.
4. Complete your own task with a summary of what you created.
5. Report back to the user in plain prose.

Pitfall: if T3's structure depends on what T1 and T2 find, let T3 exist as a "synthesize findings" task whose first step is to read parent handoffs and plan the rest. Orchestrators can spawn orchestrators.

---

## Part IV: Synthesis — What This Means for the Partnership

### The Philosophical Lineage Is Not Decorative

Hermes Kanban is not "a Kanban board for agents." It is an implementation of the same principles Ohno discovered on Toyota's factory floor, filtered through Anderson's knowledge-work adaptation, applied to a new substrate: autonomous agents as workers.

The principles hold:

- **Pull over push.** The dispatcher claims tasks; workers do not receive assignments pushed onto them. The empty slot (ready task) is the signal.
- **Visual management.** The dashboard makes fleet state visible without querying every agent.
- **WIP limits.** Implicitly, each profile works on one task at a time (serialized by the dispatcher). Fleet capacity is visible and bounded.
- **Stop-the-line authority.** `kanban_block()` is the Andon cord. Any worker can halt a task and demand human input.
- **Structured handoff.** The `summary` + `metadata` pattern is the knowledge-work equivalent of a kanban card: a compact, standardized signal that carries exactly what the next station needs.
- **Durable audit trail.** `task_events` and `task_runs` are the factory's production log. Nothing is lost to context compression.
- **Evolutionary change.** The board overlays onto whatever workflow the operator already has. No big-bang reorganization required.

### The Competitive Implications

Most agent systems treat coordination as an afterthought: prompts that call subagents, fragile in-process swarms that die when the parent context rolls. Hermes Kanban treats coordination as the primary primitive. The SQLite database is the nervous system. The dispatcher is the heartbeat. The board is the single source of truth.

This matters for:
- **Research triage.** Parallel researchers + analyst + writer, human-in-the-loop at any point.
- **Scheduled ops.** Recurring daily briefs that build a journal over weeks. The board survives restarts.
- **Digital twins.** Persistent named assistants (`inbox-triage`, `ops-review`) that accumulate memory over time.
- **Engineering pipelines.** Decompose → implement in parallel worktrees → review → iterate → PR. Each stage is a task with structured handoff.
- **Fleet farming.** One specialist managing N subjects (50 social accounts, 12 monitored services). The queue is the coordination primitive.

### The Boundary

Kanban is deliberately single-host. `~/.hermes/kanban.db` is local SQLite and the dispatcher spawns workers on the same machine. Multi-host coordination is out of scope: run an independent board per host and use `delegate_task` or a message queue to bridge them.

This is a feature, not a limitation. It makes the system deterministic, inspectable, and free of distributed systems complexity. The agent fleet is a local organism.

---

## Appendix: Full CLI Command Reference

```
hermes kanban init                                     # create kanban.db
hermes kanban create "<title>" [--body ...] [--assignee <profile>]
                                [--parent <id>]... [--tenant <name>]
                                [--workspace scratch|worktree|dir:<path>]
                                [--priority N] [--triage] [--idempotency-key KEY]
                                [--max-runtime 30m|2h|1d|<seconds>]
                                [--skill <name>]...
                                [--json]
hermes kanban list [--mine] [--assignee P] [--status S] [--tenant T] [--archived] [--json]
hermes kanban show <id> [--json]
hermes kanban assign <id> <profile>                    # or 'none' to unassign
hermes kanban link <parent_id> <child_id>
hermes kanban unlink <parent_id> <child_id>
hermes kanban claim <id> [--ttl SECONDS]
hermes kanban comment <id> "<text>" [--author NAME]
hermes kanban complete <id>... [--result "..."] [--summary "..."] [--metadata '{...}']
hermes kanban block <id> "<reason>" [--ids <id>...]
hermes kanban unblock <id>...
hermes kanban archive <id>...
hermes kanban tail <id>                                # follow a single task's event stream
hermes kanban watch [--assignee P] [--tenant T]        # live stream ALL events
        [--kinds completed,blocked,…] [--interval SECS]
hermes kanban heartbeat <id> [--note "..."]
hermes kanban runs <id> [--json]                       # attempt history
hermes kanban assignees [--json]                       # profiles + task counts
hermes kanban dispatch [--dry-run] [--max N]
        [--failure-limit N] [--json]
hermes kanban stats [--json]                           # per-status + per-assignee counts
hermes kanban log <id> [--tail BYTES]                  # worker log
hermes kanban notify-subscribe <id>
        --platform <name> --chat-id <id> [--thread-id <id>] [--user-id <id>]
hermes kanban notify-list [<id>] [--json]
hermes kanban notify-unsubscribe <id>
        --platform <name> --chat-id <id> [--thread-id <id>]
hermes kanban context <id>                             # what a worker sees
hermes kanban gc [--event-retention-days N]
        [--log-retention-days N]
```

Also available as `/kanban` slash commands in the gateway.

---

*Compiled 2026-05-04 by the Alchemist (Sivart). Sources: Hermes Agent Kanban docs (Nous Research), Hermes Kanban tutorial (Nous Research), `kanban-worker` and `kanban-orchestrator` skills, Anderson 2010, Womack & Jones 1990, Ohno 1988.*
