---
title: Loom Service Specification
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
source: research/raw/loom-service-spec.md
---

# Loom Service Specification

Status: Draft v1 (language agnostic)

Purpose: Define a service that orchestrates coding agents to get project work done, using GitHub as the issue tracker, Claude Code as the coding agent, and Synthweave as the intelligence layer.

## 1. Problem Statement

Loom is a long running automation service that continuously reads work from GitHub Issues, creates an isolated workspace for each issue, and runs a Claude Code session for that issue inside the workspace.

The service solves five operational problems:

- It turns issue execution into a repeatable daemon workflow instead of manual scripts.
- It isolates agent execution in per issue workspaces so agent commands run only inside per issue workspace directories.
- It keeps the workflow policy in repo (`WORKFLOW.md`) so teams version the agent prompt and runtime settings with their code.
- It provides enough observability to operate and debug multiple concurrent agent runs.
- It connects agents to shared team context through Synthweave, so each agent benefits from institutional knowledge and every agent run enriches the knowledge base.

Implementations are expected to document their trust and safety posture explicitly. This specification does not require a single approval, sandbox, or operator confirmation policy; some implementations may target trusted environments with a high trust configuration, while others may require stricter approvals or sandboxing.

Important boundary:

- Loom is a scheduler/runner and tracker reader.
- Ticket writes (state transitions, comments, PR links) are performed by the coding agent using tools available in the workflow/runtime environment.
- A successful run may end at a workflow defined handoff state (for example a PR ready for human review), not necessarily a closed issue.

### 1.1 Three Layer Architecture

Loom separates concerns into three layers. Each does one thing.

**The orchestrator stays a scheduler.** Poll GitHub Issues, dispatch work, manage concurrency, retry, reconcile. Pure scheduling logic. No opinions about what the agent knows or how it reasons.

**Synthweave becomes the intelligence layer.** Provides agents with shared context, decision propagation, institutional memory, and progress reporting. Fills the gap that ephemeral agents have: they know nothing beyond the rendered prompt. Synthweave gives them team knowledge, and every agent run makes that knowledge deeper.

**Claude Code is the execution engine.** Does the actual work in isolated workspaces. Connects to Synthweave via MCP to read context and report decisions back. Swappable: the orchestrator and intelligence layer do not depend on which coding agent executes.

## 2. Goals and Non Goals

### 2.1 Goals

- Poll GitHub Issues on a fixed cadence and dispatch work with bounded concurrency.
- Maintain a single authoritative orchestrator state for dispatch, retries, and reconciliation.
- Create deterministic per issue workspaces and preserve them across runs.
- Stop active runs when issue state changes make them ineligible.
- Recover from transient failures with exponential backoff.
- Load runtime behavior from a repository owned `WORKFLOW.md` contract.
- Provision agent tool environments declaratively, including MCP server connections.
- Expose operator visible observability (at minimum structured logs).
- Support restart recovery without requiring a persistent database.

### 2.2 Non Goals

- Rich web UI or multi tenant control plane.
- Prescribing a specific dashboard or terminal UI implementation.
- General purpose workflow engine or distributed job scheduler.
- Built in business logic for how to edit tickets, PRs, or comments. (That logic lives in the workflow prompt and agent tooling.)
- Mandating strong sandbox controls beyond what the coding agent and host OS provide.
- Mandating a single default approval, sandbox, or operator confirmation posture for all implementations.

## 3. System Overview

### 3.1 Main Components

1. `Workflow Loader`
   - Reads `WORKFLOW.md`.
   - Parses YAML front matter and prompt body.
   - Returns `{config, prompt_template}`.

2. `Config Layer`
   - Exposes typed getters for workflow config values.
   - Applies defaults and environment variable indirection.
   - Performs validation used by the orchestrator before dispatch.

3. `Issue Tracker Client`
   - Fetches candidate issues in active states from GitHub.
   - Fetches current states for specific issue numbers (reconciliation).
   - Fetches closed issues during startup cleanup.
   - Normalizes GitHub payloads into a stable issue model.

4. `Orchestrator`
   - Owns the poll tick.
   - Owns the in memory runtime state.
   - Decides which issues to dispatch, retry, stop, or release.
   - Tracks session metrics and retry queue state.

5. `Workspace Manager`
   - Maps issue identifiers to workspace paths.
   - Ensures per issue workspace directories exist.
   - Runs workspace lifecycle hooks.
   - Cleans workspaces for terminal issues.

6. `Tool Provisioner`
   - Resolves tool declarations from WORKFLOW.md.
   - Validates CLI tool availability and versions.
   - Generates `.mcp.json` for MCP server connections.
   - Injects file resources into workspaces.
   - Validates connectivity to required MCP servers.

7. `Agent Runner`
   - Creates workspace.
   - Builds prompt from issue + workflow template.
   - Launches Claude Code CLI in the workspace.
   - Monitors agent liveness via Synthweave progress reports.

8. `Status Surface` (optional)
   - Presents human readable runtime status (terminal output, dashboard, or other operator facing view).

9. `Logging`
   - Emits structured runtime logs to one or more configured sinks.

### 3.2 Abstraction Levels

Loom is easiest to port when kept in these layers:

1. `Policy Layer` (repo defined)
   - `WORKFLOW.md` prompt body.
   - Team specific rules for ticket handling, validation, and handoff.

2. `Configuration Layer` (typed getters)
   - Parses front matter into typed runtime settings.
   - Handles defaults, environment tokens, and path normalization.

3. `Coordination Layer` (orchestrator)
   - Polling loop, issue eligibility, concurrency, retries, reconciliation.

4. `Execution Layer` (workspace + agent CLI)
   - Filesystem lifecycle, workspace preparation, tool provisioning, agent invocation.

5. `Integration Layer` (GitHub adapter)
   - API calls and normalization for tracker data.

6. `Intelligence Layer` (Synthweave)
   - Context retrieval, decision propagation, progress reporting, institutional memory.

7. `Observability Layer` (logs + optional status surface)
   - Operator visibility into orchestrator and agent behavior.

### 3.3 External Dependencies

- GitHub API (REST and/or GraphQL) for issue tracking.
- Synthweave MCP server for context, decisions, and progress reporting.
- Local filesystem for workspaces and logs.
- Git CLI for workspace population.
- Claude Code CLI (`claude`) that supports `--print` mode for non interactive execution.
- Host environment authentication for GitHub, Synthweave, and any additional MCP servers.

## 4. Core Domain Model

### 4.1 Entities

#### 4.1.1 Issue

Normalized issue record used by orchestration, prompt rendering, and observability output.

Fields:

- `id` (integer)
  - GitHub issue number.
- `identifier` (string)
  - Human readable key: `owner/repo#123` or `#123` when repo is implicit.
- `title` (string)
- `description` (string or null)
  - Issue body in markdown.
- `priority` (integer or null)
  - Derived from labels (e.g., `priority:1`, `priority:2`). Lower numbers are higher priority.
- `state` (string)
  - `open` or `closed`.
- `state_reason` (string or null)
  - `completed`, `not_planned`, or null.
- `labels` (list of strings)
  - All issue labels, normalized to lowercase.
- `assignees` (list of strings)
  - GitHub usernames.
- `milestone` (string or null)
- `project_status` (string or null)
  - GitHub Projects v2 status field value (e.g., "Todo", "In Progress", "Done").
- `branch_name` (string or null)
  - Derived from linked PR or generated from issue identifier.
- `url` (string)
- `blocked_by` (list of blocker refs)
  - Derived from issue body or linked issues with "blocked" relationship.
  - Each blocker ref contains:
    - `number` (integer)
    - `state` (string)
    - `identifier` (string or null)
- `created_at` (timestamp)
- `updated_at` (timestamp)

#### 4.1.2 Workflow Definition

Parsed `WORKFLOW.md` payload:

- `config` (map)
  - YAML front matter root object.
- `prompt_template` (string)
  - Markdown body after front matter, trimmed.

#### 4.1.3 Service Config (Typed View)

Typed runtime values derived from `WorkflowDefinition.config` plus environment resolution.

Examples:

- poll interval
- workspace root
- active and terminal issue states/labels
- concurrency limits
- agent executable/args/timeouts
- tool declarations
- workspace hooks

#### 4.1.4 Workspace

Filesystem workspace assigned to one issue identifier.

Fields (logical):

- `path` (absolute workspace path)
- `workspace_key` (sanitized issue identifier)
- `created_now` (boolean, used to gate `after_create` hook)

#### 4.1.5 Run Attempt

One execution attempt for one issue.

Fields (logical):

- `issue_id`
- `issue_identifier`
- `attempt` (integer or null, `null` for first run, `>=1` for retries/continuation)
- `workspace_path`
- `started_at`
- `status`
- `error` (optional)

#### 4.1.6 Live Session (Agent Session Metadata)

State tracked while a Claude Code process is running.

Fields:

- `session_id` (string, Claude Code session identifier)
- `claude_pid` (integer or null, process ID)
- `last_progress_timestamp` (timestamp or null, from Synthweave progress reports)
- `last_progress_status` (string or null)
- `last_progress_summary` (string or null)
- `input_tokens` (integer)
- `output_tokens` (integer)
- `total_tokens` (integer)
- `turn_count` (integer)
  - Number of Claude Code invocations within the current worker lifetime.

#### 4.1.7 Retry Entry

Scheduled retry state for an issue.

Fields:

- `issue_id`
- `identifier` (best effort human ID for status surfaces/logs)
- `attempt` (integer, 1 based for retry queue)
- `due_at_ms` (monotonic clock timestamp)
- `timer_handle` (runtime specific timer reference)
- `error` (string or null)

#### 4.1.8 Orchestrator Runtime State

Single authoritative in memory state owned by the orchestrator.

Fields:

- `poll_interval_ms` (current effective poll interval)
- `max_concurrent_agents` (current effective global concurrency limit)
- `running` (map `issue_id -> running entry`)
- `claimed` (set of issue IDs reserved/running/retrying)
- `retry_attempts` (map `issue_id -> RetryEntry`)
- `completed` (set of issue IDs; bookkeeping only, not dispatch gating)
- `token_totals` (aggregate tokens + runtime seconds)

### 4.2 Stable Identifiers and Normalization Rules

- `Issue ID`
  - GitHub issue number. Use for API lookups and internal map keys.
- `Issue Identifier`
  - Human readable: `#123` or `owner/repo#123`. Use for logs and workspace naming.
- `Workspace Key`
  - Derive from `issue.identifier` by replacing any character not in `[A-Za-z0-9._-]` with `_`.
  - Example: `#123` becomes `_123`, `owner/repo#123` becomes `owner_repo_123`.
- `Normalized Issue State`
  - Compare states and labels after `trim` + `lowercase`.
- `Session ID`
  - Claude Code session identifier, used for `--resume`.

## 5. Workflow Specification (Repository Contract)

### 5.1 File Discovery and Path Resolution

Workflow file path precedence:

1. Explicit application/runtime setting (set by CLI startup path).
2. Default: `WORKFLOW.md` in the current process working directory.

Loader behavior:

- If the file cannot be read, return `missing_workflow_file` error.
- The workflow file is expected to be repository owned and version controlled.

### 5.2 File Format

`WORKFLOW.md` is a Markdown file with optional YAML front matter.

Parsing rules:

- If file starts with `---`, parse lines until the next `---` as YAML front matter.
- Remaining lines become the prompt body.
- If front matter is absent, treat the entire file as prompt body and use an empty config map.
- YAML front matter must decode to a map/object; non map YAML is an error.
- Prompt body is trimmed before use.

Returned workflow object:

- `config`: front matter root object (not nested under a `config` key).
- `prompt_template`: trimmed Markdown body.

### 5.3 Front Matter Schema

Top level keys:

- `tracker`
- `polling`
- `workspace`
- `hooks`
- `agent`
- `claude`
- `tools`

Unknown keys should be ignored for forward compatibility.

#### 5.3.1 `tracker` (object)

Fields:

- `kind` (string)
  - Required for dispatch.
  - Supported value: `github`
- `owner` (string)
  - GitHub repository owner (user or organization).
  - Required when `tracker.kind == "github"`.
- `repo` (string)
  - GitHub repository name.
  - Required when `tracker.kind == "github"`.
- `api_token` (string)
  - May be a literal token or `$VAR_NAME`.
  - Canonical environment variable: `GITHUB_TOKEN` or `GH_TOKEN`.
  - If `$VAR_NAME` resolves to an empty string, treat the key as missing.
- `project_number` (integer, optional)
  - GitHub Projects v2 project number.
  - When set, issue dispatch state is read from the project board status field in addition to labels.
- `active_labels` (list of strings or comma separated string)
  - Default: `agent:ready`
  - Issues with any of these labels are candidates for dispatch.
- `active_states` (list of strings or comma separated string)
  - Default: `open`
  - GitHub issue state filter.
- `terminal_states` (list of strings or comma separated string)
  - Default: `closed`
  - Issues in these states are considered done.
- `exclude_labels` (list of strings or comma separated string)
  - Default: `agent:blocked`, `agent:skip`
  - Issues with any of these labels are excluded from dispatch.
- `in_progress_label` (string)
  - Default: `agent:in-progress`
  - Applied when an issue is claimed. Removed when released.

#### 5.3.2 `polling` (object)

Fields:

- `interval_ms` (integer or string integer)
  - Default: `30000`
  - Changes should be re applied at runtime and affect future tick scheduling without restart.

#### 5.3.3 `workspace` (object)

Fields:

- `root` (path string or `$VAR`)
  - Default: `<system-temp>/symphony_workspaces`
  - `~` and strings containing path separators are expanded.
- `repo_url` (string or `$VAR`, optional)
  - Git remote URL for workspace population.
  - Default: `https://github.com/<tracker.owner>/<tracker.repo>.git`
- `default_branch` (string)
  - Default: `main`

#### 5.3.4 `hooks` (object)

Fields:

- `after_create` (multiline shell script string, optional)
  - Runs only when a workspace directory is newly created.
  - Typical use: `git clone`, dependency installation.
  - Failure aborts workspace creation.
- `before_run` (multiline shell script string, optional)
  - Runs before each agent attempt after workspace preparation and before launching the agent.
  - Typical use: `git checkout`, `git pull`, branch creation.
  - Failure aborts the current attempt.
- `after_run` (multiline shell script string, optional)
  - Runs after each agent attempt (success, failure, timeout, or cancellation) once the workspace exists.
  - Typical use: cleanup, metrics collection.
  - Failure is logged but ignored.
- `before_remove` (multiline shell script string, optional)
  - Runs before workspace deletion if the directory exists.
  - Failure is logged but ignored; cleanup still proceeds.
- `timeout_ms` (integer, optional)
  - Default: `60000`
  - Applies to all workspace hooks.

#### 5.3.5 `agent` (object)

Fields:

- `max_concurrent_agents` (integer or string integer)
  - Default: `3`
  - Changes should be re applied at runtime and affect subsequent dispatch decisions.
  - Note: default is lower than the original spec's 10, reflecting that Claude Code sessions are heavier weight than Codex sessions.
- `max_turns` (integer)
  - Default: `10`
  - Maximum number of Claude Code invocations per issue per worker session.
- `max_retry_backoff_ms` (integer or string integer)
  - Default: `300000` (5 minutes)
  - Changes should be re applied at runtime and affect future retry scheduling.
- `max_concurrent_agents_by_label` (map `label_name -> positive integer`)
  - Default: empty map.
  - Label keys are normalized (`trim` + `lowercase`) for lookup.
  - Limits how many agents can work on issues sharing a specific label.

#### 5.3.6 `claude` (object)

Fields:

- `command` (string)
  - Default: `claude`
  - The Claude Code CLI executable.
- `model` (string, optional)
  - Model to use. Passed as `--model` flag.
  - Default: whatever Claude Code's default is.
- `max_turns` (integer, optional)
  - Passed as `--max-turns` to Claude Code.
  - Default: `50`
- `permission_mode` (string)
  - How Claude Code handles tool permissions.
  - Values: `default`, `accept-all`, `bypassPermissions`
  - Default: `default`
  - `accept-all` passes `--dangerously-skip-permissions`. Use only in trusted, sandboxed environments.
- `output_format` (string)
  - Default: `json`
  - Passed as `--output-format`.
- `session_timeout_ms` (integer)
  - Default: `3600000` (1 hour)
  - Maximum wall clock time for a single Claude Code invocation.
- `stall_timeout_ms` (integer)
  - Default: `300000` (5 minutes)
  - If no progress report is received from Synthweave within this period, the agent is considered stalled.
  - If `<= 0`, stall detection is disabled.
  - Note: because Claude Code is CLI based (no streaming events), stall detection relies on Synthweave progress reports. If Synthweave is not configured, stall detection falls back to process liveness checks.

#### 5.3.7 `tools` (object)

Declarative tool provisioning. The orchestrator resolves these before agent launch.

Fields:

- `mcp` (list of MCP server declarations)
  Each entry:
  - `name` (string, required): identifier for logging and status
  - `url` (string): remote MCP server URL (StreamableHTTP or SSE). Mutually exclusive with `command`.
  - `command` (string): local MCP server command (stdio transport). Mutually exclusive with `url`.
  - `args` (list of strings): arguments for command based servers
  - `env` (map string to string): environment variables. Supports `$VAR` indirection.
  - `auth` (string): authentication token or `$VAR` reference
  - `required` (boolean, default true): failure to connect fails the run
  - `context` (map string to string): template rendered values passed as connection metadata

- `cli` (list of CLI tool declarations)
  Each entry:
  - `name` (string, required): executable name
  - `required` (boolean, default true)
  - `version` (string): semver constraint
  - `install` (string): shell command to install if missing (runs during `after_create` only)

- `files` (list of file injection rules)
  Each entry:
  - `source` (string, required): source path, supports `$VAR` and `~`
  - `target` (string, required): destination relative to workspace root
  - `required` (boolean, default true)

- `permissions` (map of permission scopes)
  Structure is integration specific. Used to select appropriately scoped tokens.

### 5.4 Prompt Template Contract

The Markdown body of `WORKFLOW.md` is the per issue prompt template.

Rendering requirements:

- Use a strict template engine (Liquid compatible semantics are sufficient).
- Unknown variables must fail rendering.
- Unknown filters must fail rendering.

Template input variables:

- `issue` (object)
  - Includes all normalized issue fields, including labels and blockers.
- `attempt` (integer or null)
  - `null`/absent on first attempt.
  - Integer on retry or continuation run.

Fallback prompt behavior:

- If the workflow prompt body is empty, the runtime may use a minimal default prompt (`You are working on a GitHub issue.`).
- Workflow file read/parse failures are configuration/validation errors and should not silently fall back to a prompt.

### 5.5 Workflow Validation and Error Surface

Error classes:

- `missing_workflow_file`
- `workflow_parse_error`
- `workflow_front_matter_not_a_map`
- `template_parse_error`
- `template_render_error`

Dispatch gating behavior:

- Workflow file read/YAML errors block new dispatches until fixed.
- Template errors fail only the affected run attempt.

## 6. Configuration Specification

### 6.1 Source Precedence and Resolution Semantics

Configuration precedence:

1. Workflow file path selection (runtime setting -> cwd default).
2. YAML front matter values.
3. Environment indirection via `$VAR_NAME` inside selected YAML values.
4. Built in defaults.

Value coercion semantics:

- Path/command fields support `~` home expansion and `$VAR` expansion.
- Apply expansion only to values intended to be local filesystem paths; do not rewrite URIs.

### 6.2 Dynamic Reload Semantics

Dynamic reload is required:

- Watch `WORKFLOW.md` for changes.
- On change, re read and re apply workflow config and prompt template without restart.
- Reloaded config applies to future dispatch, retry scheduling, reconciliation, hook execution, tool provisioning, and agent launches.
- Invalid reloads should not crash the service; keep operating with the last known good configuration and emit an operator visible error.

### 6.3 Dispatch Preflight Validation

Startup validation:

- Validate configuration before starting the scheduling loop.
- If startup validation fails, fail startup with operator visible error.

Per tick dispatch validation:

- Re validate before each dispatch cycle.
- If validation fails, skip dispatch for that tick, keep reconciliation active.

Validation checks:

- Workflow file can be loaded and parsed.
- `tracker.kind` is present and supported.
- `tracker.api_token` is present after `$` resolution.
- `tracker.owner` and `tracker.repo` are present.
- `claude.command` is present and non empty.

### 6.4 Config Fields Summary

- `tracker.kind`: string, required, `github`
- `tracker.owner`: string, required
- `tracker.repo`: string, required
- `tracker.api_token`: string or `$VAR`, canonical env `GITHUB_TOKEN`
- `tracker.project_number`: integer, optional
- `tracker.active_labels`: list/string, default `agent:ready`
- `tracker.active_states`: list/string, default `open`
- `tracker.terminal_states`: list/string, default `closed`
- `tracker.exclude_labels`: list/string, default `agent:blocked, agent:skip`
- `tracker.in_progress_label`: string, default `agent:in-progress`
- `polling.interval_ms`: integer, default `30000`
- `workspace.root`: path, default `<system-temp>/symphony_workspaces`
- `workspace.repo_url`: string, default derived from tracker owner/repo
- `workspace.default_branch`: string, default `main`
- `hooks.after_create`: shell script or null
- `hooks.before_run`: shell script or null
- `hooks.after_run`: shell script or null
- `hooks.before_remove`: shell script or null
- `hooks.timeout_ms`: integer, default `60000`
- `agent.max_concurrent_agents`: integer, default `3`
- `agent.max_turns`: integer, default `10`
- `agent.max_retry_backoff_ms`: integer, default `300000`
- `agent.max_concurrent_agents_by_label`: map, default `{}`
- `claude.command`: string, default `claude`
- `claude.model`: string, optional
- `claude.max_turns`: integer, default `50`
- `claude.permission_mode`: string, default `default`
- `claude.output_format`: string, default `json`
- `claude.session_timeout_ms`: integer, default `3600000`
- `claude.stall_timeout_ms`: integer, default `300000`
- `tools.mcp`: list of MCP server declarations
- `tools.cli`: list of CLI tool declarations
- `tools.files`: list of file injection rules
- `tools.permissions`: map of permission scopes

## 7. Orchestration State Machine

The orchestrator is the only component that mutates scheduling state.

### 7.1 Issue Orchestration States

Internal claim states (not the same as GitHub issue states):

1. `Unclaimed`
   - Issue is not running and has no retry scheduled.

2. `Claimed`
   - Orchestrator has reserved the issue. The `in_progress_label` is applied to the GitHub issue.
   - In practice, claimed issues are either `Running` or `RetryQueued`.

3. `Running`
   - Worker task exists and the issue is tracked in `running` map.

4. `RetryQueued`
   - Worker is not running, but a retry timer exists in `retry_attempts`.

5. `Released`
   - Claim removed. The `in_progress_label` is removed from the GitHub issue.

### 7.2 Run Attempt Lifecycle

A run attempt transitions through these phases:

1. `PreparingWorkspace`
2. `ProvisioningTools`
3. `BuildingPrompt`
4. `LaunchingAgent`
5. `AgentRunning`
6. `Finishing`
7. `Succeeded`
8. `Failed`
9. `TimedOut`
10. `Stalled`
11. `CanceledByReconciliation`

### 7.3 Transition Triggers

- `Poll Tick`
  - Reconcile active runs.
  - Validate config.
  - Fetch candidate issues.
  - Dispatch until slots are exhausted.

- `Worker Exit (normal)`
  - Remove running entry.
  - Update aggregate runtime totals.
  - Schedule continuation retry (attempt `1`).

- `Worker Exit (abnormal)`
  - Remove running entry.
  - Update aggregate runtime totals.
  - Schedule exponential backoff retry.

- `Progress Report` (from Synthweave)
  - Update live session fields and stall detection timer.

- `Retry Timer Fired`
  - Re fetch active candidates and attempt re dispatch, or release claim.

- `Reconciliation State Refresh`
  - Stop runs whose issues are closed or no longer labeled for dispatch.

- `Stall Timeout`
  - Kill worker and schedule retry.

### 7.4 Idempotency and Recovery Rules

- The orchestrator serializes state mutations through one authority.
- `claimed` and `running` checks are required before launching any worker.
- Reconciliation runs before dispatch on every tick.
- Restart recovery is GitHub driven and filesystem driven (no durable database required).
- On startup, remove `in_progress_label` from any issues that are not actively running.

## 8. Polling, Scheduling, and Reconciliation

### 8.1 Poll Loop

At startup: validate config, perform startup cleanup, schedule immediate tick, then repeat every `polling.interval_ms`.

Tick sequence:

1. Reconcile running issues.
2. Run dispatch preflight validation.
3. Fetch candidate issues from GitHub.
4. Sort issues by dispatch priority.
5. Dispatch eligible issues while slots remain.
6. Notify observability/status consumers.

### 8.2 Candidate Selection Rules

An issue is dispatch eligible only if all are true:

- It has a number, title, and state.
- Its state is in `active_states` (default: open).
- It has at least one label from `active_labels` (default: `agent:ready`).
- It has none of the `exclude_labels`.
- It is not already in `running` or `claimed`.
- Global concurrency slots are available.
- Per label concurrency slots are available.
- Blocker rule passes: if the issue has blockers (from `blocked_by`), all blockers must be in terminal states.

Sorting order:

1. `priority` ascending (derived from priority labels; null sorts last)
2. `created_at` oldest first
3. `number` ascending tiebreaker

### 8.3 Concurrency Control

Global limit:

- `available_slots = max(max_concurrent_agents - running_count, 0)`

Per label limit:

- `max_concurrent_agents_by_label[label]` if present (label key normalized)
- otherwise fallback to global limit

### 8.4 Retry and Backoff

Backoff formula:

- Normal continuation retries after a clean exit: fixed delay of `1000` ms.
- Failure driven retries: `delay = min(10000 * 2^(attempt - 1), agent.max_retry_backoff_ms)`.

Retry handling:

1. Fetch active candidate issues.
2. Find the specific issue by `issue_id`.
3. If not found or no longer eligible, release claim (remove `in_progress_label`).
4. If eligible and slots available, dispatch.
5. If eligible but no slots, requeue.

### 8.5 Active Run Reconciliation

Runs every tick. Two parts.

Part A: Stall detection

- For each running issue, compute `elapsed_ms` since `last_progress_timestamp` (or `started_at` if no progress seen).
- If `elapsed_ms > claude.stall_timeout_ms`, terminate the worker and queue a retry.
- If Synthweave is not configured, fall back to process liveness: check if the Claude Code process is still running and consuming CPU.
- If `stall_timeout_ms <= 0`, skip stall detection.

Part B: GitHub state refresh

- Fetch current state and labels for all running issue numbers.
- For each running issue:
  - If issue is closed: terminate worker and clean workspace.
  - If `active_labels` removed: terminate worker.
  - If `exclude_labels` added: terminate worker.
  - If still active: update the in memory issue snapshot.
- If state refresh fails, keep workers running and retry next tick.

### 8.6 Startup Cleanup

When the service starts:

1. Query GitHub for closed issues that may have stale workspaces.
2. Remove `in_progress_label` from any issue not actively being worked.
3. Clean corresponding workspace directories.
4. If cleanup fetch fails, log warning and continue startup.

## 9. Workspace Management and Safety

### 9.1 Workspace Layout

Workspace root: `workspace.root`

Per issue workspace path: `<workspace.root>/<sanitized_issue_identifier>`

Workspaces are reused across runs for the same issue. Successful runs do not auto delete workspaces.

### 9.2 Workspace Creation and Reuse

1. Sanitize identifier to `workspace_key`.
2. Compute workspace path under workspace root.
3. Ensure the workspace path exists as a directory.
4. Mark `created_now=true` if newly created.
5. If `created_now=true`, run `after_create` hook (typically: git clone, npm install).

### 9.3 Workspace Population

The spec recommends but does not require Git based workspace population.

Recommended `after_create` hook:

```bash
git clone $REPO_URL .
git checkout -b agent/$ISSUE_IDENTIFIER $DEFAULT_BRANCH
```

Recommended `before_run` hook:

```bash
git fetch origin
git rebase origin/$DEFAULT_BRANCH
```

Failure handling:

- Population failures fail the current attempt.
- New workspaces with failed population may be removed.
- Reused workspaces should not be destructively reset on failure.

### 9.4 Workspace Hooks

Supported hooks: `after_create`, `before_run`, `after_run`, `before_remove`.

Execution: `bash -lc <script>` with workspace directory as cwd. Timeout: `hooks.timeout_ms`.

Failure semantics:

- `after_create` failure is fatal to workspace creation.
- `before_run` failure is fatal to the current run attempt.
- `after_run` and `before_remove` failures are logged and ignored.

### 9.5 Safety Invariants

Invariant 1: Run the coding agent only in the per issue workspace path.

Invariant 2: Workspace path must stay inside workspace root. Normalize both to absolute paths and verify prefix.

Invariant 3: Workspace key is sanitized. Only `[A-Za-z0-9._-]` allowed. Replace all other characters with `_`.

## 10. Tool Provisioning

### 10.1 Design Principles

1. The orchestrator provisions. The agent discovers.
2. Declarative over imperative. WORKFLOW.md declares what tools a workflow needs.
3. Least privilege by default. An agent gets only what its workflow declares.
4. Tool availability is a precondition. Missing required tools fail the run at preparation, not mid execution.

### 10.2 Provisioning Sequence

Runs after `before_run` hook and before agent launch:

1. **CLI validation.** For each `tools.cli` entry: check executable in PATH, check version if specified. Fail on any required miss.
2. **File injection.** For each `tools.files` entry: resolve source, copy to target. Fail on any required miss.
3. **MCP configuration.** For each `tools.mcp` entry: resolve URLs and auth, validate connectivity for required servers, write `.mcp.json` to workspace root.
4. **Permission resolution.** Select scoped tokens based on `tools.permissions`.

### 10.3 MCP Configuration Generation

The orchestrator writes `.mcp.json` to the workspace root before launching Claude Code:

```json
{
  "mcpServers": {
    "synthweave": {
      "url": "https://app.synthweave.ai/mcp",
      "headers": {
        "Authorization": "Bearer sw_xxx_yyy"
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-github"],
      "env": {
        "GITHUB_TOKEN": "<resolved>"
      }
    }
  }
}
```

Rules:

- Resolve all `$VAR` references before writing.
- Validate reachability for required remote servers (HTTP health check to `/mcp/health`).
- Overwrite `.mcp.json` on every run to pick up config changes.
- Add `.mcp.json` to `.gitignore` in the workspace (contains resolved credentials).

### 10.4 Runtime Reporting

Track tool provisioning status per running issue:

- Which MCP servers connected
- Which CLI tools validated
- Provisioning duration

Log failures with: `issue_id`, `issue_identifier`, `tool_name`, `tool_category`, `error`.

## 11. Agent Runner Protocol (Claude Code Integration)

### 11.1 Launch Contract

Claude Code is a CLI tool invoked per task, not a persistent process.

Invocation:

```bash
claude --print \
  --output-format json \
  --model <claude.model> \
  --max-turns <claude.max_turns> \
  -p "<rendered_prompt>" \
  --cwd <workspace_path>
```

If `claude.permission_mode` is `accept-all`:

```bash
claude --print \
  --output-format json \
  --dangerously-skip-permissions \
  --model <claude.model> \
  --max-turns <claude.max_turns> \
  -p "<rendered_prompt>" \
  --cwd <workspace_path>
```

The orchestrator captures the Claude Code process ID for lifecycle management.

### 11.2 Session Continuation

Claude Code supports session continuation via `--resume <session_id>`.

After a successful first invocation:

1. Parse the JSON output for the session ID.
2. If the issue is still active, invoke again with `--resume <session_id>` and continuation guidance.
3. Repeat up to `agent.max_turns`.

The first invocation uses the full rendered prompt. Continuation invocations send only new context (e.g., "The PR received review feedback. Please address it.").

### 11.3 Output Parsing

Claude Code with `--output-format json` returns structured output including:

- Session ID
- Token usage (input, output, total)
- Cost estimate
- Result content

The agent runner parses this output to:

- Extract session ID for continuation
- Update token counters in orchestrator state
- Determine success/failure
- Capture the agent's final output for logging

### 11.4 Observability Without Streaming Events

Unlike Codex's persistent JSON RPC channel, Claude Code does not stream events during execution. Observability comes from two sources:

**Synthweave progress reports.** The agent calls `report_progress` through the MCP server during execution. The orchestrator polls Synthweave or subscribes to real time updates.

**Process monitoring.** The orchestrator checks that the Claude Code process is still alive and consuming resources. A process that is running but idle (no CPU, no Synthweave activity) may be stalled.

The workflow prompt should instruct the agent to call `report_progress` periodically:

```markdown
Every 5-10 minutes during your work, call the `report_progress` tool in Synthweave
with your current status. This is how the orchestrator knows you are alive.
```

### 11.5 Timeout and Error Handling

Timeouts:

- `claude.session_timeout_ms`: maximum wall clock time per invocation. Kill the process on expiry.
- `claude.stall_timeout_ms`: maximum time between Synthweave progress reports.

Error categories:

- `claude_not_found`: CLI executable not in PATH
- `invalid_workspace_cwd`: workspace path invalid
- `session_timeout`: wall clock exceeded
- `stall_timeout`: no progress within threshold
- `process_exit_error`: non zero exit code
- `output_parse_error`: JSON output malformed
- `permission_denied`: Claude Code permission prompt triggered in non interactive mode

### 11.6 Agent Runner Contract

1. Create/reuse workspace for issue.
2. Provision tools (Section 10).
3. Build prompt from workflow template.
4. Launch Claude Code CLI.
5. Monitor liveness via process checks and Synthweave progress.
6. On completion, parse output and report to orchestrator.
7. On error, fail the attempt (orchestrator handles retry).

## 12. Issue Tracker Integration Contract (GitHub)

### 12.1 Required Operations

1. `fetch_candidate_issues()`
   - Return open issues with `active_labels` in the configured repository.
   - Exclude issues with `exclude_labels`.
   - Include issue body, labels, assignees, milestone, creation date.

2. `fetch_issue_states_by_numbers(issue_numbers)`
   - Return current state, state_reason, and labels for specific issues.
   - Used for reconciliation.

3. `fetch_closed_issues()`
   - Return recently closed issues for startup cleanup.

4. `add_label(issue_number, label)`
   - Add `in_progress_label` when claiming.

5. `remove_label(issue_number, label)`
   - Remove `in_progress_label` when releasing.

### 12.2 Query Semantics (GitHub)

GitHub REST API:

- Endpoint: `https://api.github.com`
- Auth: `Authorization: Bearer <token>` header
- Candidate issues: `GET /repos/{owner}/{repo}/issues?state=open&labels={active_labels}`
- Issue state refresh: `GET /repos/{owner}/{repo}/issues/{number}`
- Label management: `POST /repos/{owner}/{repo}/issues/{number}/labels` and `DELETE /repos/{owner}/{repo}/issues/{number}/labels/{label}`

GitHub GraphQL API (for Projects v2):

- Endpoint: `https://api.github.com/graphql`
- Used when `tracker.project_number` is set, to read project board status.

Pagination:

- REST: follow `Link` header for `rel="next"`.
- GraphQL: cursor based pagination.
- Page size: 100 (GitHub maximum for REST).
- Network timeout: `30000 ms`.

### 12.3 Normalization Rules

- `id`: issue number (integer)
- `identifier`: `#<number>`
- `title`: issue title
- `description`: issue body (markdown)
- `priority`: derived from labels matching `priority:<n>` pattern, parsed to integer
- `state`: `open` or `closed`
- `labels`: all label names, lowercase
- `blocked_by`: parsed from issue body (e.g., "Blocked by #45") or from GitHub sub issue relationships
- `created_at`, `updated_at`: ISO 8601 timestamps

### 12.4 Error Handling

Error categories:

- `unsupported_tracker_kind`
- `missing_github_token`
- `missing_github_owner_or_repo`
- `github_api_request` (network/transport)
- `github_api_status` (non 2xx HTTP)
- `github_rate_limit` (403 with rate limit headers)
- `github_not_found` (404)

Orchestrator behavior on errors:

- Candidate fetch failure: log and skip dispatch for this tick.
- State refresh failure: keep workers running, retry next tick.
- Startup cleanup failure: log warning, continue startup.
- Rate limit: respect `Retry-After` header, pause polling.

### 12.5 Tracker Writes (Important Boundary)

Loom manages only one label (`in_progress_label`) on GitHub issues.

All other ticket mutations (state transitions, comments, PR creation, linking) are performed by the coding agent using `gh` CLI or the GitHub MCP server. The service remains a scheduler/runner and tracker reader.

## 13. Synthweave Intelligence Layer

### 13.1 Role

Synthweave serves three functions in the Loom architecture:

1. **Context provider.** Agents search and read shared knowledge during execution.
2. **Decision sink.** Agents write decisions, findings, and context back for future agents.
3. **Observability bridge.** Agents report progress through Synthweave, replacing the streaming event channel that existed in the Codex model.

### 13.2 Connection

Synthweave MCP server uses StreamableHTTP transport (stateless, per request).

- Endpoint: `POST /mcp`
- Health check: `GET /mcp/health`
- Auth: Bearer token, format `sw_<prefix>_<secret>`
- API keys are scoped to user and organization with configurable permissions

### 13.3 Available Tools (Current: 22)

Grouped by Loom function:

**Intelligence (context retrieval):**

| Tool | Purpose |
|------|---------|
| `snip_search` | Hybrid semantic + full text search with filters (content type, tags, project IDs) |
| `snip_reader` | Read snip with full content, links, and comments |
| `ls` | Navigate workspace structure: bases, projects, folders, snips |
| `get-comments` | Retrieve discussion history on a snip |
| `user_search` | Find users by email/username for escalation |

**Decision propagation (writing back):**

| Tool | Purpose |
|------|---------|
| `create-snip` | Create snip with title, content, tags, project associations |
| `snip_commenter` | Add comments to existing snips |
| `snip_rewrite` | Replace entire snip content |
| `checkpoint` | Create/list/read version history |
| `manage_reference_links` | CRUD for snip to snip links |

**Task management:**

| Tool | Purpose |
|------|---------|
| `create_project` | Create new project in a base |
| `task_creator` | Create task (new snip or link existing) |
| `task_updater` | Update task status (todo/doing/done), assignee, due date |
| `manage_snip` | Create, move, or update snip metadata |
| `manage_folder` | Create, rename, move, delete folders |
| `manage_project` | Create, update, delete projects |

### 13.4 Required New Tools for Loom Integration

Six additional tools are needed:

**Priority 1 (orchestrator observability):**

`report_progress`: Agent signals liveness and status.

```
Input: issue_id, status (working|testing|reviewing|blocked|completing),
       summary, percent_complete (optional)
Storage: New record type, queryable by orchestrator.
```

`report_blocker`: Structured escalation.

```
Input: issue_id, blocker_type (clarification_needed|access_denied|
       test_failure|design_decision|dependency), description,
       suggested_action (optional)
Effect: Creates tagged snip, optionally triggers Slack notification.
```

**Priority 2 (cross system bridge):**

`sync_github_issue`: Bidirectional state sync between GitHub Issues and Synthweave tasks.

```
Input: action (import|export|sync_status), github_issue (owner, repo,
       number), synthweave_project_id (optional)
```

**Priority 3 (verification):**

`check_ci_status`: Query CI results for a branch or PR.

```
Input: owner, repo, branch (optional), pr_number (optional)
Output: Structured check results with pass/fail status.
```

`capture_evidence`: Store proof of work artifacts as versioned snips.

```
Input: issue_id, evidence_type (test_results|screenshot|log_output|
       before_after), title, content, attachments (optional)
```

`get_team_patterns`: Targeted coding conventions for specific files/domains.

```
Input: file_paths, domain (optional), pattern_types (optional)
Output: Relevant context.md content, ADRs, and applicable rules.
```

### 13.5 Orchestrator Integration Patterns

**Polling (recommended starting point):**

Orchestrator calls Synthweave API each tick to check progress for running issues. One HTTP call per running issue per tick.

**Real time subscriptions (future optimization):**

Synthweave supports Hasura GraphQL subscriptions. Orchestrator subscribes to progress updates for all running issues. Stall detection becomes event driven.

### 13.6 Context Compounding

The defining advantage of the Synthweave layer: knowledge accumulates.

Agent run 1 on a codebase captures decisions and context. Agent run 50 has access to all prior context. This is the gap that ephemeral agents (Loom original, Codex standalone) can never close. Each agent run enriches the knowledge base through `create-snip`, `snip_commenter`, and `checkpoint`. Future agents search this accumulated knowledge via `snip_search`.

The orchestrator does not manage this accumulation. It happens organically through agent tool use guided by the workflow prompt.

## 14. Prompt Construction and Context Assembly

### 14.1 Inputs

- `workflow.prompt_template`
- normalized `issue` object
- optional `attempt` integer

### 14.2 Rendering Rules

- Render with strict variable checking.
- Render with strict filter checking.
- Convert issue object keys to strings for template compatibility.
- Preserve nested arrays/maps (labels, blockers) so templates can iterate.

### 14.3 Retry/Continuation Semantics

`attempt` should be passed to the template because the workflow prompt may provide different instructions for first runs versus continuations versus retries.

### 14.4 Recommended Prompt Structure

```markdown
You are working on GitHub issue {{ issue.identifier }}: {{ issue.title }}

## Issue Description
{{ issue.description }}

## Your Environment
- Workspace: your current working directory is the project root
- Tools: you have access to `gh` CLI, `git`, and Synthweave MCP tools
- Branch: work on `agent/{{ issue.identifier }}`

## Instructions
1. Search Synthweave for related context and prior decisions
2. Understand the issue fully before writing code
3. Report progress via Synthweave every 5-10 minutes
4. Write tests for your changes
5. Open a PR with a clear description linking to {{ issue.url }}
6. Capture any architectural decisions in Synthweave

{% if attempt %}
## Retry Context
This is attempt {{ attempt }}. A previous attempt failed or was interrupted.
Check the current state of the branch and continue where it left off.
{% endif %}
```

### 14.5 Failure Semantics

Prompt rendering failure fails the run attempt immediately.

## 15. Logging, Status, and Observability

### 15.1 Logging Conventions

Required context fields:

- `issue_id` and `issue_identifier` for issue related logs
- `session_id` for agent session logs

### 15.2 Runtime Snapshot

If exposed, the snapshot should return:

- `running`: list of running sessions with turn count and last progress
- `retrying`: list of retry queue entries
- `token_totals`: input, output, total tokens and aggregate runtime seconds
- `tool_status`: MCP server connectivity status

### 15.3 Token Accounting

- Parse Claude Code JSON output for token usage.
- Track per session and aggregate totals.
- Include cost estimates when available from Claude Code output.

## 16. Example WORKFLOW.md

```yaml
---
tracker:
  kind: github
  owner: synthweave
  repo: app
  api_token: $GITHUB_TOKEN
  active_labels: agent:ready
  exclude_labels: agent:blocked, agent:skip
  in_progress_label: agent:in-progress

polling:
  interval_ms: 30000

workspace:
  root: ~/symphony_workspaces
  default_branch: main

hooks:
  after_create: |
    git clone https://github.com/synthweave/app.git .
    npm install
  before_run: |
    git fetch origin
    git checkout -B agent/$ISSUE_IDENTIFIER origin/main
  after_run: |
    git stash

agent:
  max_concurrent_agents: 3
  max_turns: 10

claude:
  model: claude-sonnet-4-20250514
  max_turns: 50
  permission_mode: default
  session_timeout_ms: 3600000
  stall_timeout_ms: 300000

tools:
  mcp:
    - name: synthweave
      url: $SYNTHWEAVE_MCP_URL
      auth: $SYNTHWEAVE_API_KEY
      required: true
      context:
        issue_id: "{{ issue.id }}"
        issue_identifier: "{{ issue.identifier }}"
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
    - name: node
      required: true
      version: ">=20"
---

You are an autonomous coding agent working on {{ issue.identifier }}: {{ issue.title }}

## Issue
{{ issue.description }}

## Workflow

1. **Understand.** Search Synthweave for related context, prior decisions, and team conventions using `snip_search`. Read any linked snips with `snip_reader`.

2. **Plan.** Think through your approach. If this is a significant architectural decision, check `snip_search` for existing ADRs in this area.

3. **Implement.** Write code, tests, and documentation. Follow the project's conventions.

4. **Verify.** Run tests. Check types. Lint. Fix what fails.

5. **Document.** Capture any decisions you made in Synthweave using `create-snip` with appropriate tags. Future agents will thank you.

6. **Ship.** Open a PR with `gh pr create`, linking to {{ issue.url }}. Include a clear description of what changed and why.

7. **Report.** Call `report_progress` in Synthweave every 5-10 minutes so the orchestrator knows you are alive.

{% if attempt %}
## Continuation
This is attempt {{ attempt }}. Check the current branch state and pick up where the previous attempt left off. Do not redo completed work.
{% endif %}
```

## 17. Implementation Notes

### 17.1 Language Choice

This spec is language agnostic. The reference implementation choice (Elixir, Node.js, Python, Go, etc.) is independent of this specification.

Considerations:

- The orchestrator is a straightforward poll/dispatch/reconcile loop. Any language with timers, process management, and HTTP client support is sufficient.
- Node.js/TypeScript aligns with existing Synthweave infrastructure (Express, BullMQ).
- Elixir/BEAM provides superior fault tolerance at scale (supervision trees, hot code reload, lightweight processes) but introduces a separate runtime ecosystem.
- For teams already using the BEAM, Elixir is a natural fit. For everyone else, the operational overhead of a new runtime likely outweighs the concurrency benefits at typical Loom scale (3 to 30 concurrent agents).

### 17.2 Minimum Viable Implementation

A conforming implementation requires:

1. WORKFLOW.md loader with YAML front matter parsing
2. GitHub Issues REST client (candidate fetch, state refresh, label management)
3. Orchestrator with poll loop, concurrency control, retry queue
4. Workspace manager with hooks and safety invariants
5. Tool provisioner with `.mcp.json` generation
6. Claude Code CLI launcher with output parsing
7. Structured logging

The intelligence layer (Synthweave) is strongly recommended but not required for basic operation. Without it, stall detection falls back to process monitoring and agents lose access to shared context.

### 17.3 Differences from Original Symphony Spec

| Aspect | Original (Linear + Codex) | This Spec (GitHub + Claude + Synthweave) |
|--------|--------------------------|------------------------------------------|
| Tracker | Linear GraphQL | GitHub REST + GraphQL |
| Agent | Codex app server (JSON RPC over stdio) | Claude Code CLI (invocation based) |
| Agent communication | Persistent bidirectional stdio channel | CLI invocation + MCP for context |
| Stall detection | Event stream inactivity | Synthweave progress reports + process monitoring |
| Session continuity | Same thread, same process | `--resume` with session ID, new process |
| Tool provisioning | Implicit (prompt + runtime) | Explicit (WORKFLOW.md `tools` section) |
| Intelligence layer | None | Synthweave MCP (context, decisions, memory) |
| Claim signaling | None (orchestrator internal only) | GitHub label (`agent:in-progress`) |
| Default concurrency | 10 | 3 |
| Client side tools | `linear_graphql` (optional) | GitHub MCP + Synthweave MCP (recommended) |
