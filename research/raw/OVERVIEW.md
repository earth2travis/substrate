# Loom: Autonomous Coding Agent Orchestration

## What Is Loom?

Loom is a system that turns a backlog of GitHub issues into completed, verified code without humans writing any of it.

It works like this: you label an issue `agent:ready`. Loom picks it up, creates an isolated workspace, launches a Claude Code agent, and that agent reads the issue, searches for relevant context in Synthweave, writes the code, runs the tests, opens a PR, and reports back. If it fails, Loom retries with exponential backoff. If the issue gets closed while the agent is working, Loom kills the agent and cleans up.

Humans steer. Agents execute.

## The Three Layers

Loom separates concerns cleanly. Each layer does one thing.

```
┌─────────────────────────────────────────────┐
│           Loom Orchestrator             │
│                                             │
│  Poll GitHub → Dispatch → Reconcile         │
│  Concurrency control, retry, stall detect   │
│                                             │
│  "What needs to be done? Who's doing it?"   │
└──────────────────┬──────────────────────────┘
                   │ spawns per issue
                   ▼
┌─────────────────────────────────────────────┐
│            Claude Code CLI                  │
│                                             │
│  Isolated workspace per issue               │
│  Reads code, writes code, runs tests        │
│  Opens PRs, responds to review              │
│                                             │
│  "Do the work."                             │
└──────────┬──────────────────┬───────────────┘
           │ reads/writes     │ reads/writes
           ▼                  ▼
┌──────────────────┐  ┌──────────────────────┐
│   GitHub         │  │   Synthweave MCP     │
│                  │  │                      │
│  Issues, PRs     │  │  Shared context      │
│  Code, CI        │  │  Team decisions      │
│                  │  │  Institutional memory │
│                  │  │  Progress reporting   │
│  "Where the      │  │                      │
│   code lives."   │  │  "What the team      │
│                  │  │   knows."            │
└──────────────────┘  └──────────────────────┘
```

**The orchestrator is a scheduler.** It polls GitHub Issues every 30 seconds, filters for issues labeled `agent:ready`, sorts by priority, and dispatches agents up to a concurrency limit. It manages retries, detects stalled agents, and reconciles running work against issue state changes. It has no opinions about what the agent knows or how it reasons.

**Claude Code is the execution engine.** Each issue gets a fresh Claude Code invocation in an isolated workspace. The agent reads the issue, writes code, runs tests, and opens a PR. It connects to MCP servers for additional capabilities. It is swappable: the orchestrator does not depend on which coding agent executes.

**Synthweave is the intelligence layer.** It gives agents access to shared team context, prior decisions, and institutional memory. Every agent run enriches this knowledge base. The 50th agent working on a codebase has access to context from all 49 previous runs. Synthweave also serves as the observability bridge: agents report progress through it, and the orchestrator uses those reports for stall detection.

## How It Works

### The Loop

Every 30 seconds, Loom runs this cycle:

1. **Reconcile.** Check all running agents. Is the issue still open? Did it get closed while the agent was working? Is the agent stalled? Kill anything that should not be running.

2. **Validate.** Re read WORKFLOW.md. Is the config still valid? Did someone change the polling interval or concurrency limit?

3. **Fetch.** Query GitHub for open issues with the `agent:ready` label. Exclude anything labeled `agent:blocked` or `agent:skip`.

4. **Sort.** Priority labels first (lower number = higher priority), then oldest issues first.

5. **Dispatch.** For each eligible issue, if concurrency slots are available: claim it (add `agent:in-progress` label), create or reuse its workspace, provision tools, render the prompt, launch Claude Code.

### Workspace Lifecycle

Each issue gets its own directory under the workspace root:

```
~/symphony_workspaces/
├── _123/          # Issue #123
├── _124/          # Issue #124
└── _125/          # Issue #125
```

When a workspace is first created, the `after_create` hook runs (typically: git clone, npm install). Before each agent run, the `before_run` hook runs (typically: git fetch, rebase on main, create a branch). After each run, the `after_run` hook runs (cleanup). When an issue is closed, the workspace is removed.

Workspaces persist across retries. If an agent fails and retries, it picks up the same workspace with its previous work intact.

### Tool Provisioning

Before launching Claude Code, the orchestrator provisions the agent's tool environment:

1. **CLI tools.** Verify that `gh`, `git`, `node`, etc. are available and at the right versions.
2. **MCP servers.** Write a `.mcp.json` file to the workspace with connection details for Synthweave, GitHub MCP, and any other declared servers.
3. **File resources.** Inject configuration files, documentation, or credentials into the workspace.

This is declarative. WORKFLOW.md says what tools the workflow needs. The orchestrator makes them available. If a required tool is missing, the run fails before the agent ever starts.

### Agent Execution

Claude Code runs in `--print` mode with JSON output:

```bash
claude --print --output-format json -p "<prompt>" --cwd /workspace
```

The prompt is rendered from WORKFLOW.md's template body, with issue data injected. It tells the agent what to do and how to use its tools.

During execution, the agent:

- Searches Synthweave for related context and prior decisions
- Reads and modifies code in its isolated workspace
- Runs tests and fixes failures
- Reports progress to Synthweave every 5 to 10 minutes
- Opens a PR when the work is complete
- Captures any architectural decisions in Synthweave for future agents

If the agent needs multiple turns (e.g., addressing PR review feedback), Loom continues the session using `claude --resume <session_id>`.

### Stall Detection

Because Claude Code is a CLI tool (not a persistent process with streaming events), the orchestrator cannot observe the agent directly during execution. Instead:

1. The workflow prompt instructs the agent to call `report_progress` in Synthweave periodically.
2. The orchestrator polls Synthweave each tick for the latest progress timestamp.
3. If no progress report arrives within `stall_timeout_ms` (default: 5 minutes), the agent is considered stalled, killed, and retried.

If Synthweave is not configured, stall detection falls back to process monitoring (is the Claude Code process still alive and consuming CPU?).

### Retry and Recovery

When an agent fails:

- **Clean exit, issue still active:** Retry after 1 second. The agent picks up where it left off.
- **Error exit:** Retry with exponential backoff (10s, 20s, 40s... up to 5 minutes).
- **Stall:** Kill the process, retry with backoff.
- **Issue closed during execution:** Kill the process, clean up, no retry.

On restart, Loom has no persistent database. It recovers by querying GitHub for issue states and checking the filesystem for existing workspaces. Stale `agent:in-progress` labels are cleaned up.

## Why Synthweave?

Synthweave is optional but transformative.

Without it, Loom is a job scheduler. Each agent starts from scratch with only the issue description and whatever is in the repo. This is how the original Symphony spec works. It is functional but limited.

With Synthweave, agents have institutional memory:

**Before starting work**, the agent searches Synthweave for related context. "Has anyone worked on something similar? What patterns does this team use? What was tried before and didn't work?" This comes from prior agent runs, human documentation, and team discussions that have been captured as snips.

**During work**, the agent reports progress. The orchestrator stays informed. The team can see what agents are doing in real time.

**After completing work**, the agent captures its decisions. "I chose approach A over approach B because of X." This becomes searchable context for every future agent.

The knowledge compounds. Early agents are nearly as blind as they would be without Synthweave. After weeks or months of agent runs, the accumulated context makes agents dramatically more effective. They make fewer mistakes because they can see what mistakes were made before. They follow team conventions because those conventions are discoverable, not tribal.

This is the gap between a job scheduler and an intelligent system.

### Synthweave's Current Tool Surface

Synthweave already exposes 22 MCP tools:

| Category | Tools | What They Do |
|----------|-------|-------------|
| Search | `snip_search` | Hybrid semantic + full text search across all knowledge |
| Read | `snip_reader`, `ls`, `get-comments` | Navigate and read context, discussions, decisions |
| Write | `create-snip`, `snip_commenter`, `snip_rewrite` | Capture decisions, annotate context, update knowledge |
| Version | `checkpoint` | Version history for snips, audit trail |
| Link | `manage_reference_links` | Connect related decisions, build knowledge graph |
| Tasks | `task_creator`, `task_updater` | Track work within Synthweave |
| Users | `user_search` | Find people for escalation |

Six additional tools are needed for full Loom integration:

| Tool | Priority | Purpose |
|------|----------|---------|
| `report_progress` | Required | Agent liveness signal for stall detection |
| `report_blocker` | Required | Structured escalation when agent is stuck |
| `sync_github_issue` | Recommended | Bidirectional state sync with GitHub |
| `check_ci_status` | Recommended | Agent queries CI results |
| `capture_evidence` | Recommended | Proof of work artifacts (test output, screenshots) |
| `get_team_patterns` | Recommended | Targeted coding conventions for specific files |

## WORKFLOW.md

Everything about how Loom behaves is defined in one file, checked into the repo alongside the code.

The front matter (YAML) configures the system: which repo to watch, how many concurrent agents, what tools to provision, how long before an agent is considered stalled.

The body (Markdown) is the prompt template. It tells the agent what to do, rendered with issue data at dispatch time.

```yaml
---
tracker:
  kind: github
  owner: myorg
  repo: myapp
  active_labels: agent:ready

agent:
  max_concurrent_agents: 3

claude:
  model: claude-sonnet-4-20250514
  stall_timeout_ms: 300000

tools:
  mcp:
    - name: synthweave
      url: $SYNTHWEAVE_MCP_URL
      auth: $SYNTHWEAVE_API_KEY
      required: true
    - name: github
      command: npx
      args: ["-y", "@anthropic/mcp-github"]
      env:
        GITHUB_TOKEN: $GITHUB_TOKEN
      required: true
  cli:
    - name: gh
      required: true
    - name: git
      required: true
---

You are working on {{ issue.identifier }}: {{ issue.title }}

{{ issue.description }}

Search Synthweave for context. Write code. Run tests. Open a PR.
Report progress every 5-10 minutes.
```

Changes to WORKFLOW.md are picked up automatically. No restart required. Update the concurrency limit, change the model, add a new MCP server, modify the prompt: all live reloaded.

## Differences from OpenAI's Symphony

Symphony was released by OpenAI in March 2026 as an open source spec for orchestrating Codex agents against Linear issues. This version adapts the architecture for a different stack.

| Aspect | Original | This Version |
|--------|----------|-------------|
| Issue tracker | Linear (GraphQL) | GitHub Issues + Projects |
| Coding agent | Codex app server (persistent JSON RPC) | Claude Code CLI (invocation based) |
| Intelligence layer | None | Synthweave MCP |
| Tool provisioning | Implicit | Explicit, declarative |
| Agent communication | Bidirectional stdio pipe | MCP + CLI output |
| Stall detection | Event stream monitoring | Synthweave progress reports |
| Claim visibility | Internal only | GitHub label (`agent:in-progress`) |
| Default concurrency | 10 | 3 |

The orchestration core (poll, dispatch, reconcile, retry) is preserved unchanged. The differences are in the integration layer (GitHub vs Linear), the execution layer (CLI vs persistent process), and the addition of an intelligence layer that did not exist in the original.

## Who Is This For?

Teams that want to turn their issue backlog into completed code with minimal human intervention.

The prerequisites:

1. **A well structured codebase.** Agents need tests, types, linters, CI. If a human can't onboard quickly from the repo alone, an agent won't either. (See: harness engineering.)

2. **Well specified issues.** "Fix the bug" is not enough. "The /api/users endpoint returns 500 when the email field is null; add validation and return 400" gives the agent something to work with.

3. **Willingness to invest in the harness.** The agent is only as good as its environment. Documentation, conventions, automated checks: these are not overhead, they are the infrastructure that makes autonomous agents reliable.

Loom does not replace engineering judgment. It replaces the mechanical translation of well understood requirements into working code. Humans decide what to build and why. Agents figure out how and do it.

## Getting Started

1. Write a `WORKFLOW.md` in your repo with tracker config, tool declarations, and a prompt template.
2. Run the Loom orchestrator, pointed at your repo.
3. Label an issue `agent:ready`.
4. Watch.

The orchestrator picks up the issue, provisions a workspace, launches Claude Code, and the agent goes to work. When it opens a PR, you review it. When it captures a decision in Synthweave, every future agent benefits.

Start small. One issue. One agent. See what happens. Then scale.
