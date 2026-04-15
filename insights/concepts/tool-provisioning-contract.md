---
title: Tool Provisioning Contract
tags:
  - ai-agents
  - knowledge-management
  - process-philosophy
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/tool-provisioning-contract.md
---

# Tool Provisioning Contract

Status: Draft v1
Parent: Loom Service Specification (GitHub + Claude Code variant)

## 1. Problem Statement

The original Loom'spec treats agent capabilities as implicit. The workflow prompt describes what the agent should do. The runtime environment happens to have the tools to do it. If it doesn't, the agent fails.

This works when the agent runtime (Codex) has broad built in capabilities and the team controls the entire stack. It breaks when:

- Different workflows need different tool surfaces
- Security requires scoping agent access per issue type
- Tool availability needs to be deterministic, not hopeful
- Multiple MCP servers need coordinated provisioning
- Cost optimization requires minimizing tool context

The tool provisioning contract makes agent capabilities explicit, deterministic, and auditable.

## 2. Design Principles

1. **The orchestrator provisions. The agent discovers.** The orchestrator sets up the tool environment before launching the agent. The agent discovers available tools through standard mechanisms (MCP, CLI, filesystem).

2. **Declarative over imperative.** WORKFLOW.md declares what tools a workflow needs. The orchestrator resolves declarations into concrete configurations.

3. **Least privilege by default.** An agent gets only the tools its workflow declares. No implicit access to everything on the host.

4. **Tool availability is a precondition.** If a required tool cannot be provisioned, the run fails at workspace preparation, not mid execution.

## 3. Tool Categories

### 3.1 CLI Tools

Executables available on the host or installed into the workspace.

Examples: `gh`, `git`, `npm`, `pytest`, `docker`, `terraform`

Provisioned by: workspace hooks (`after_create`, `before_run`) or host environment.

Validated by: checking executable exists in PATH before agent launch.

### 3.2 MCP Servers

Model Context Protocol servers the agent connects to for dynamic tool discovery.

Examples: Synthweave (context, decisions, progress), GitHub (issues, PRs, reviews), database access, deployment APIs.

Provisioned by: the orchestrator writes an MCP configuration file (`.mcp.json`) into the workspace before launching the agent.

### 3.3 File Resources

Static files, credentials, or configuration the agent needs access to.

Examples: `.env` files, service account tokens, SSH keys, API documentation.

Provisioned by: workspace hooks or orchestrator file injection.

### 3.4 Permissions

Scoped access to external systems. Not tools themselves, but constraints on what tools can do.

Examples: read only GitHub access, write access to a specific repo, deploy access to staging only.

Enforced by: token scoping, MCP server authorization, or sandbox policy.

## 4. WORKFLOW.md Schema Extension

Add a `tools` key to the front matter:

```yaml
tools:
  mcp:
    - name: synthweave
      url: $SYNTHWEAVE_MCP_URL
      auth: $SYNTHWEAVE_API_KEY
      required: true
    - name: github
      command: npx @anthropic/mcp-github
      env:
        GITHUB_TOKEN: $GITHUB_TOKEN
      required: true
    - name: sentry
      url: $SENTRY_MCP_URL
      required: false

  cli:
    - name: gh
      required: true
      version: ">=2.0"
    - name: node
      required: true
      version: ">=20"
    - name: pytest
      required: false

  files:
    - source: $SHARED_CONFIG_DIR/eslintrc.json
      target: .eslintrc.json
    - source: $DOCS_DIR/api-reference.md
      target: .agent/api-reference.md

  permissions:
    github:
      - issues:read
      - issues:write
      - pull_requests:write
      - contents:write
    deploy:
      - staging
```

### 4.1 Field Definitions

#### `tools.mcp` (list of MCP server declarations)

Each entry:

- `name` (string, required): identifier for logging and status reporting
- `url` (string): remote MCP server URL (SSE or streamable HTTP transport)
- `command` (string): local MCP server command (stdio transport). Mutually exclusive with `url`.
- `args` (list of strings): arguments for command based servers
- `env` (map string to string): environment variables for the server process. Supports `$VAR` indirection.
- `auth` (string): authentication token or `$VAR` reference
- `required` (boolean, default true): if true, failure to connect fails the run. If false, agent proceeds without it.

#### `tools.cli` (list of CLI tool declarations)

Each entry:

- `name` (string, required): executable name
- `required` (boolean, default true): if true, missing executable fails workspace preparation
- `version` (string): semver constraint. Validated by running `<name> --version` and parsing output.
- `install` (string): shell command to install if missing. Only runs during `after_create`, not every run.

#### `tools.files` (list of file injection rules)

Each entry:

- `source` (string, required): source path. Supports `$VAR` and `~` expansion.
- `target` (string, required): destination path relative to workspace root.
- `required` (boolean, default true): if true, missing source fails workspace preparation.

#### `tools.permissions` (map of permission scopes)

Structure is integration specific. The orchestrator passes these to MCP servers or uses them to select appropriately scoped tokens.

## 5. MCP Configuration Generation

Before launching Claude Code, the orchestrator writes `.mcp.json` to the workspace root.

Generated from `tools.mcp` declarations:

```json
{
  "mcpServers": {
    "synthweave": {
      "url": "https://mcp.synthweave.ai/workspace/abc",
      "headers": {
        "Authorization": "Bearer <resolved-token>"
      }
    },
    "github": {
      "command": "npx",
      "args": ["@anthropic/mcp-github"],
      "env": {
        "GITHUB_TOKEN": "<resolved-token>"
      }
    }
  }
}
```

Rules:

- Resolve all `$VAR` references before writing
- Validate that remote servers are reachable (HTTP health check) if `required: true`
- Validate that command based servers can start (spawn and check for MCP handshake) if `required: true`
- Write `.mcp.json` during workspace preparation, after hooks but before agent launch
- Overwrite on every run (not just creation) to pick up config changes

## 6. Validation Sequence

Tool provisioning validation runs as part of workspace preparation, after `before_run` hook and before agent launch.

Order:

1. **CLI validation.** For each `tools.cli` entry: check executable exists in PATH, check version if specified. Fail on any required miss.

2. **File injection.** For each `tools.files` entry: resolve source path, copy to target. Fail on any required miss.

3. **MCP configuration.** For each `tools.mcp` entry: resolve URLs and auth, validate connectivity for required servers, write `.mcp.json`.

4. **Permission resolution.** Select appropriately scoped tokens based on `tools.permissions`. If a required permission scope cannot be satisfied, fail.

If any required validation fails, the run attempt fails at `PreparingWorkspace` phase. The orchestrator handles retry per normal backoff logic.

## 7. Runtime Reporting

The orchestrator should track tool provisioning status per running issue:

- Which MCP servers connected successfully
- Which CLI tools were validated
- Which files were injected
- Provisioning duration

This feeds into the observability layer (Section 13 of the main spec). Tool provisioning failures should be logged with:

- `issue_id`
- `issue_identifier`
- `tool_name`
- `tool_category` (mcp, cli, file, permission)
- `error` (missing, version_mismatch, connection_failed, auth_failed)

## 8. Synthweave MCP Integration

### 8.1 Connection

Synthweave exposes MCP via StreamableHTTP (stateless, per request transport instances).

- **Endpoint:** `POST /mcp`
- **Health check:** `GET /mcp/health`
- **Auth:** Bearer token, format `sw_<prefix>_<secret>`, verified via bcrypt against stored hash
- **Scoping:** API keys are scoped to a user and organization, with configurable permission scopes

```yaml
tools:
  mcp:
    - name: synthweave
      url: $SYNTHWEAVE_MCP_URL
      auth: $SYNTHWEAVE_API_KEY
      required: true
      context:
        issue_id: "{{ issue.id }}"
        issue_identifier: "{{ issue.identifier }}"
        project: "{{ tracker.repo }}"
```

The `context` map is rendered with the same template engine as the prompt and passed as connection metadata. This allows Synthweave to scope its tool responses to the relevant issue and project context.

### 8.2 Current Tool Surface (22 Tools)

These tools exist today in production. Grouped by Loom relevance:

#### Intelligence Layer (context and knowledge)

| Tool | Synthweave Name | What It Does | Loom Use |
|------|----------------|--------------|--------------|
| **Search** | `snip_search` | Hybrid semantic + full text search with filters (content type, tags, project IDs, templates) | Agent searches for related context, prior decisions, similar issues. This is the primary intelligence tool. |
| **Read** | `snip_reader` | Read a snip with full content (TipTap JSON), links, and comments | Agent reads detailed context, architectural decisions, team conventions. |
| **Navigate** | `ls` | List workspace contents: bases, projects, folders, snips | Agent discovers what knowledge exists, orients in the context graph. |
| **Comments** | `get-comments` | Retrieve all comments on a snip | Agent reads discussion history and rationale behind decisions. |
| **Users** | `user_search` | Search users by email or username | Agent identifies who owns what, who to escalate to. |

#### Decision Propagation (writing back)

| Tool | Synthweave Name | What It Does | Loom Use |
|------|----------------|--------------|--------------|
| **Create** | `create-snip` | Create snip with title, content, tags, project associations | Agent captures decisions, findings, or context for future agents. |
| **Comment** | `snip_commenter` | Add comments to existing snips | Agent annotates existing context with new findings. |
| **Rewrite** | `snip_rewrite` | Replace entire snip content | Agent updates documentation or context that has changed. |
| **Version** | `checkpoint` | Create/list/read version history | Agent checkpoints its work, creates audit trail. |
| **Link** | `manage_reference_links` | CRUD for snip to snip links (manual + @mention) | Agent connects related decisions, creates knowledge graph edges. |

#### Project and Task Management

| Tool | Synthweave Name | What It Does | Loom Use |
|------|----------------|--------------|--------------|
| **Create Project** | `create_project` | Create new project in a base | Could mirror GitHub project structure in Synthweave. |
| **Create Task** | `task_creator` | Create task (new snip or link existing) | Agent breaks down work, creates subtasks. |
| **Update Task** | `task_updater` | Update task status (todo/doing/done), assignee, due date | Agent tracks its own progress within Synthweave. |
| **Manage Snip** | `manage_snip` | Create, move, or update snip metadata | Agent organizes its output. |
| **Manage Folder** | `manage_folder` | Create, rename, move, delete folders | Agent structures workspace. |
| **Manage Project** | `manage_project` | Create, update, delete projects | Agent manages project lifecycle. |

### 8.3 Mapping to Loom Needs

| Loom Need | Available Today? | How |
|---------------|-----------------|-----|
| Read shared context | ✅ Yes | `snip_search` + `snip_reader` for semantic retrieval of relevant knowledge |
| Read decision history | ✅ Yes | `snip_search` filtered by tags (e.g., "decision", "adr") + `get-comments` for discussion |
| Capture decisions | ✅ Yes | `create-snip` with decision tag + `manage_reference_links` to connect to issue context |
| Get team conventions | ✅ Yes | `snip_search` for coding standards, architecture docs stored as snips |
| Search prior work | ✅ Yes | `snip_search` with hybrid mode (semantic + full text) |
| Track task progress | ✅ Yes | `task_updater` for status changes within Synthweave |
| Version/checkpoint work | ✅ Yes | `checkpoint` for snip version history |
| **Report progress to orchestrator** | ❌ No | No tool exists for agent to signal liveness or status to an external orchestrator |
| **Report blocker** | ❌ No | No tool for escalation signals; `snip_commenter` is close but not structured for this |
| **Orchestrator heartbeat** | ❌ No | No mechanism for the orchestrator to query "is this agent still working?" |
| **Issue state sync** | ❌ No | No bridge between Synthweave tasks and GitHub Issues state |
| **CI/build status** | ❌ No | No tool to query build or test results |
| **Screenshot/proof of work** | ❌ No | No visual verification capability (flagged in harness readiness assessment) |

### 8.4 Gap Analysis: New Tools Needed for Loom

Six new tools would complete the Loom integration surface:

#### Priority 1: Orchestrator Observability (required for stall detection)

**`report_progress`** (new tool)

Purpose: Agent signals liveness and status to the orchestrator. Replaces Codex's streaming event channel.

```typescript
{
  issue_id: z.string().describe("GitHub issue identifier"),
  status: z.enum(["working", "testing", "reviewing", "blocked", "completing"]),
  summary: z.string().describe("Brief description of current activity"),
  percent_complete: z.number().optional().describe("Estimated progress 0-100"),
  timestamp: z.string().optional().describe("ISO-8601, defaults to now")
}
```

Storage: New table or snip type. Orchestrator polls `GET /mcp/progress/{issue_id}` or subscribes via Hasura real time subscription.

Stall detection: If no `report_progress` call within `stall_timeout_ms`, the orchestrator considers the agent stalled.

**`report_blocker`** (new tool)

Purpose: Agent signals it needs human intervention. Structured escalation rather than just failing.

```typescript
{
  issue_id: z.string(),
  blocker_type: z.enum(["clarification_needed", "access_denied", "test_failure", "design_decision", "dependency"]),
  description: z.string(),
  suggested_action: z.string().optional()
}
```

This creates a Synthweave snip tagged as a blocker, linked to the issue context, and optionally triggers a notification (Slack integration already exists).

#### Priority 2: Cross System Bridge

**`sync_github_issue`** (new tool)

Purpose: Bridge between Synthweave's task model and GitHub Issues. Keeps both systems in sync.

```typescript
{
  action: z.enum(["import", "export", "sync_status"]),
  github_issue: z.object({
    owner: z.string(),
    repo: z.string(),
    number: z.number()
  }),
  synthweave_project_id: z.string().optional()
}
```

Note: Synthweave already has a GitHub integration (OAuth + App). This tool would leverage that existing infrastructure to create bidirectional sync between GitHub issue state and Synthweave task state.

#### Priority 3: Verification and Proof of Work

**`check_ci_status`** (new tool)

Purpose: Agent queries CI/CD results for its branch. Uses existing GitHub integration.

```typescript
{
  owner: z.string(),
  repo: z.string(),
  branch: z.string().optional(),
  pr_number: z.number().optional()
}
```

Returns: structured check results (build, typecheck, tests, coverage) with pass/fail status.

**`capture_evidence`** (new tool)

Purpose: Agent stores proof of work artifacts (test output, screenshots, logs) as versioned snips.

```typescript
{
  issue_id: z.string(),
  evidence_type: z.enum(["test_results", "screenshot", "log_output", "before_after"]),
  title: z.string(),
  content: z.string(),
  attachments: z.array(z.object({
    filename: z.string(),
    content_base64: z.string(),
    mime_type: z.string()
  })).optional()
}
```

Creates a snip linked to the issue context with checkpoint versioning. Synthweave already supports image uploads via S3, so attachment handling infrastructure exists.

**`get_team_patterns`** (new tool)

Purpose: Returns relevant coding patterns, conventions, and quality standards for a specific area of the codebase. More targeted than generic `snip_search`.

```typescript
{
  file_paths: z.array(z.string()).describe("Files being modified"),
  domain: z.string().optional().describe("Bounded context name"),
  pattern_types: z.array(z.enum([
    "naming", "testing", "error_handling", "api_design", "ui_components"
  ])).optional()
}
```

Returns: relevant context.md content, related ADRs, and applicable linting rules. This is a higher level intelligence tool that aggregates from multiple snips.

### 8.5 Progress Reporting as Observability Channel

In the Codex model, the orchestrator sees agent activity through the JSON RPC event stream. With Claude Code CLI, that stream doesn't exist. Synthweave becomes the observability bridge:

```
Claude Code agent
  ↓ calls report_progress
Synthweave MCP server
  ↓ stores progress record (DB + real-time subscription)
Loom Orchestrator
  ↓ polls or subscribes
  ↓ updates stall detection timer
  ↓ updates status dashboard
```

Two integration patterns:

**Polling (simpler).** Orchestrator hits `GET /mcp/progress/{issue_id}` every `polling.interval_ms`. Piggybacks on the existing poll tick. Adds one HTTP call per running issue per tick.

**Real time (lower latency).** Synthweave already supports Hasura GraphQL subscriptions. Orchestrator subscribes to progress updates for all running issues. Stall detection becomes event driven rather than poll driven. Better for observability dashboards.

Recommended: start with polling, add real time subscriptions when the dashboard demands it.

### 8.6 Leveraging Existing Infrastructure

Several Synthweave capabilities directly support Loom without new tools:

| Existing Capability | How It Helps Loom |
|---------------------|----------------------|
| **Hasura event triggers** (33 tables) | Could trigger orchestrator webhooks when snip/task state changes |
| **BullMQ job queue** | Could process Loom dispatch as jobs with retry and concurrency control |
| **Agent trigger system** (event, mention, schedule) | Could evaluate Loom dispatch events through existing trigger framework |
| **AES-256-GCM credential encryption** | Secure storage for GitHub tokens, API keys used by Loom agents |
| **Slack integration** | Blocker notifications, progress summaries to team channels |
| **Real time subscriptions** | Live orchestrator status without polling |
| **Hybrid search (pgvector + tsvector)** | Semantic context retrieval for agent prompts |

### 8.7 Architecture: Synthweave as Loom's Intelligence Layer

The three layer separation becomes concrete:

```
Loom Orchestrator (scheduler)
  │
  ├── Polls GitHub Issues (tracker integration)
  ├── Manages concurrency, retry, reconciliation
  ├── Provisions workspaces + .mcp.json
  │
  ↓ spawns per issue
Claude Code CLI (execution)
  │
  ├── Connects to Synthweave MCP (StreamableHTTP)
  │   ├── 22 existing tools (context, search, tasks, versioning)
  │   └── 6 new tools (progress, blockers, CI, evidence, patterns, GitHub sync)
  │
  ├── Connects to GitHub MCP (optional, for direct GitHub API)
  ├── Uses CLI tools (gh, git, npm, etc.)
  └── Works in isolated workspace
  │
  ↓ writes back to
Synthweave (intelligence)
  │
  ├── Stores decisions, context, progress
  ├── Notifies orchestrator via poll or subscription
  ├── Propagates decisions to downstream consumers
  └── Accumulates institutional memory across all agent runs
```

What makes this architecture compound: every agent run enriches Synthweave's knowledge base. The 50th agent working on a codebase has access to context from all 49 previous runs. This is the gap Loom's ephemeral agents can never close on their own.

## 9. Security Considerations

- **Token isolation.** Each workspace gets its own resolved tokens. Tokens are written to files with restricted permissions (0600) or passed via environment variables. Never embedded in `.mcp.json` in plaintext if the workspace might be committed to git.
- **Workspace scoping.** MCP servers should scope their responses to the issue context. An agent working on issue #42 should not access context for unrelated issues unless the workflow explicitly allows cross issue access.
- **Audit trail.** All tool invocations through MCP should be logged by the MCP server. This creates an audit trail of what the agent accessed and what decisions it propagated.
- **Credential rotation.** The orchestrator should support re resolving `$VAR` references on each run, not caching resolved tokens across workspace reuse.

## 10. Relationship to Main Spec

This contract extends Sections 5.3 (Front Matter Schema), 9 (Workspace Management), and 10 (Agent Runner Protocol) of the main Loom'spec.

It does not change the orchestration state machine, polling logic, or retry semantics. Tool provisioning is a workspace preparation concern that happens between `before_run` hook completion and agent launch.

The orchestrator treats tool provisioning failure the same as any workspace preparation failure: fail the attempt, let retry logic decide what happens next.
