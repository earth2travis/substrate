---
title: Symphony Service Specification (GitHub + Claude Code Variant)
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
source: research/raw/symphony-service-spec-github-claude.md
---

# Symphony Service Specification (GitHub + Claude Code Variant)

Status: Draft v1 (language-agnostic)

Purpose: Define a service that orchestrates coding agents to get project work done.

Based on: [OpenAI Symphony SPEC.md](https://github.com/openai/symphony/blob/main/SPEC.md), adapted
for GitHub Issues/Projects as the tracker and Claude Code as the coding agent.

## 1. Problem Statement

Symphony is a long-running automation service that continuously reads work from an issue tracker
(GitHub Issues with optional GitHub Projects v2 in this specification version), creates an isolated
workspace for each issue, and runs a coding agent session for that issue inside the workspace.

The service solves four operational problems:

- It turns issue execution into a repeatable daemon workflow instead of manual scripts.
- It isolates agent execution in per-issue workspaces so agent commands run only inside per-issue
  workspace directories.
- It keeps the workflow policy in-repo (`WORKFLOW.md`) so teams version the agent prompt and runtime
  settings with their code.
- It provides enough observability to operate and debug multiple concurrent agent runs.

Implementations are expected to document their trust and safety posture explicitly. This
specification does not require a single approval, sandbox, or operator-confirmation policy; some
implementations may target trusted environments with a high-trust configuration, while others may
require stricter approvals or sandboxing.

Important boundary:

- Symphony is a scheduler/runner and tracker reader.
- Ticket writes (state transitions, comments, PR links) are typically performed by the coding agent
  using tools available in the workflow/runtime environment (for example `gh` CLI or the GitHub API).
- A successful run may end at a workflow-defined handoff state (for example a "needs-review" label),
  not necessarily a closed issue.

## 2. Goals and Non-Goals

### 2.1 Goals

- Poll the issue tracker on a fixed cadence and dispatch work with bounded concurrency.
- Maintain a single authoritative orchestrator state for dispatch, retries, and reconciliation.
- Create deterministic per-issue workspaces and preserve them across runs.
- Stop active runs when issue state changes make them ineligible.
- Recover from transient failures with exponential backoff.
- Load runtime behavior from a repository-owned `WORKFLOW.md` contract.
- Expose operator-visible observability (at minimum structured logs).
- Support restart recovery without requiring a persistent database.

### 2.2 Non-Goals

- Rich web UI or multi-tenant control plane.
- Prescribing a specific dashboard or terminal UI implementation.
- General-purpose workflow engine or distributed job scheduler.
- Built-in business logic for how to edit tickets, PRs, or comments. (That logic lives in the
  workflow prompt and agent tooling.)
- Mandating strong sandbox controls beyond what the coding agent and host OS provide.
- Mandating a single default approval, sandbox, or operator-confirmation posture for all
  implementations.

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
   - Fetches candidate issues in active states.
   - Fetches current states for specific issue IDs (reconciliation).
   - Fetches terminal-state issues during startup cleanup.
   - Normalizes tracker payloads into a stable issue model.

4. `Orchestrator`
   - Owns the poll tick.
   - Owns the in-memory runtime state.
   - Decides which issues to dispatch, retry, stop, or release.
   - Tracks session metrics and retry queue state.

5. `Workspace Manager`
   - Maps issue identifiers to workspace paths.
   - Ensures per-issue workspace directories exist.
   - Runs workspace lifecycle hooks.
   - Cleans workspaces for terminal issues.

6. `Agent Runner`
   - Creates workspace.
   - Builds prompt from issue + workflow template.
   - Launches the Claude Code CLI process.
   - Captures agent output and reports results back to the orchestrator.

7. `Status Surface` (optional)
   - Presents human-readable runtime status (for example terminal output, dashboard, or other
     operator-facing view).

8. `Logging`
   - Emits structured runtime logs to one or more configured sinks.

### 3.2 Abstraction Levels

Symphony is easiest to port when kept in these layers:

1. `Policy Layer` (repo-defined)
   - `WORKFLOW.md` prompt body.
   - Team-specific rules for ticket handling, validation, and handoff.

2. `Configuration Layer` (typed getters)
   - Parses front matter into typed runtime settings.
   - Handles defaults, environment tokens, and path normalization.

3. `Coordination Layer` (orchestrator)
   - Polling loop, issue eligibility, concurrency, retries, reconciliation.

4. `Execution Layer` (workspace + agent subprocess)
   - Filesystem lifecycle, workspace preparation, Claude Code CLI invocation.

5. `Integration Layer` (GitHub adapter)
   - API calls and normalization for tracker data.

6. `Observability Layer` (logs + optional status surface)
   - Operator visibility into orchestrator and agent behavior.

### 3.3 External Dependencies

- Issue tracker API (GitHub REST API and/or GraphQL API for `tracker.kind: github`).
- Local filesystem for workspaces and logs.
- Optional workspace population tooling (for example Git CLI, if used).
- Claude Code CLI (`claude`) installed and available on the host.
- Host environment authentication for the issue tracker (`GITHUB_TOKEN` or `GH_TOKEN`) and coding
  agent (Anthropic API key or Claude Max session).

## 4. Core Domain Model

### 4.1 Entities

#### 4.1.1 Issue

Normalized issue record used by orchestration, prompt rendering, and observability output.

Fields:

- `id` (string)
  - Stable tracker-internal ID. For GitHub, this is the numeric issue ID (not the issue number).
- `identifier` (string)
  - Human-readable ticket key. Format: `owner/repo#123` when the orchestrator manages multiple
    repos, or `#123` when operating on a single repo (derived from `tracker.owner` and
    `tracker.repo`).
- `title` (string)
- `description` (string or null)
  - The issue body.
- `priority` (integer or null)
  - Derived from labels (for example `priority:1` through `priority:4`) or from a GitHub Projects
    v2 custom field. Lower numbers are higher priority in dispatch sorting. Null if no priority is
    assigned.
- `state` (string)
  - Current tracker state name. For GitHub: derived from open/closed status combined with labels or
    GitHub Projects v2 column/status. See Section 11 for details.
- `branch_name` (string or null)
  - Extracted from the issue body, a linked branch, or a development field if available.
- `url` (string or null)
  - The HTML URL of the issue.
- `labels` (list of strings)
  - Normalized to lowercase.
- `blocked_by` (list of blocker refs)
  - Each blocker ref contains:
    - `id` (string or null)
    - `identifier` (string or null)
    - `state` (string or null)
  - Derived from issues referenced in a "blocked by" task list, issues with a "blocked" label
    linking to other issues, or a custom blocker field convention.
- `created_at` (timestamp or null)
- `updated_at` (timestamp or null)

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
- active and terminal issue states
- concurrency limits
- coding-agent executable/args/timeouts
- workspace hooks

#### 4.1.4 Workspace

Filesystem workspace assigned to one issue identifier.

Fields (logical):

- `path` (workspace path; current runtime typically uses absolute paths, but relative roots are
  possible if configured without path separators)
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

State tracked while a Claude Code subprocess is running.

Fields:

- `session_id` (string)
  - A unique identifier for this agent invocation. Generated by the orchestrator (for example a
    UUID or `<issue_id>-<attempt>-<timestamp>`).
- `claude_pid` (integer or null)
  - OS process ID of the running `claude` process.
- `last_activity_timestamp` (timestamp or null)
  - Last time output was observed from the process (for stall detection).
- `claude_input_tokens` (integer)
- `claude_output_tokens` (integer)
- `claude_total_tokens` (integer)
- `claude_cost_usd` (float or null)
  - Cost reported by Claude Code in its JSON output, if available.
- `turn_count` (integer)
  - Number of coding-agent invocations started within the current worker lifetime.
- `claude_session_id` (string or null)
  - The Claude Code session ID, used for `--resume` on continuation turns.

#### 4.1.7 Retry Entry

Scheduled retry state for an issue.

Fields:

- `issue_id`
- `identifier` (best-effort human ID for status surfaces/logs)
- `attempt` (integer, 1-based for retry queue)
- `due_at_ms` (monotonic clock timestamp)
- `timer_handle` (runtime-specific timer reference)
- `error` (string or null)

#### 4.1.8 Orchestrator Runtime State

Single authoritative in-memory state owned by the orchestrator.

Fields:

- `poll_interval_ms` (current effective poll interval)
- `max_concurrent_agents` (current effective global concurrency limit)
- `running` (map `issue_id -> running entry`)
- `claimed` (set of issue IDs reserved/running/retrying)
- `retry_attempts` (map `issue_id -> RetryEntry`)
- `completed` (set of issue IDs; bookkeeping only, not dispatch gating)
- `claude_totals` (aggregate tokens + runtime seconds + cost)
- `claude_rate_limits` (latest rate-limit snapshot from agent output, if available)

### 4.2 Stable Identifiers and Normalization Rules

- `Issue ID`
  - Use for tracker lookups and internal map keys. For GitHub, this is the numeric issue ID
    (available from the API as `id` on the issue object).
- `Issue Identifier`
  - Use for human-readable logs and workspace naming. Format: `owner/repo#123` or `#123`.
- `Workspace Key`
  - Derive from `issue.identifier` by replacing any character not in `[A-Za-z0-9._-]` with `_`.
  - Use the sanitized value for the workspace directory name.
  - Example: `owner/repo#123` becomes `owner_repo_123`.
- `Normalized Issue State`
  - Compare states after `trim` + `lowercase`.
- `Session ID`
  - Generated by the orchestrator for each agent invocation. Format is implementation-defined
    (for example UUID or composite key).

## 5. Workflow Specification (Repository Contract)

### 5.1 File Discovery and Path Resolution

Workflow file path precedence:

1. Explicit application/runtime setting (set by CLI startup path).
2. Default: `WORKFLOW.md` in the current process working directory.

Loader behavior:

- If the file cannot be read, return `missing_workflow_file` error.
- The workflow file is expected to be repository-owned and version-controlled.

### 5.2 File Format

`WORKFLOW.md` is a Markdown file with optional YAML front matter.

Design note:

- `WORKFLOW.md` should be self-contained enough to describe and run different workflows (prompt,
  runtime settings, hooks, and tracker selection/config) without requiring out-of-band
  service-specific configuration.

Parsing rules:

- If file starts with `---`, parse lines until the next `---` as YAML front matter.
- Remaining lines become the prompt body.
- If front matter is absent, treat the entire file as prompt body and use an empty config map.
- YAML front matter must decode to a map/object; non-map YAML is an error.
- Prompt body is trimmed before use.

Returned workflow object:

- `config`: front matter root object (not nested under a `config` key).
- `prompt_template`: trimmed Markdown body.

### 5.3 Front Matter Schema

Top-level keys:

- `tracker`
- `polling`
- `workspace`
- `hooks`
- `agent`
- `claude`

Unknown keys should be ignored for forward compatibility.

Note:

- The workflow front matter is extensible. Optional extensions may define additional top-level keys
  (for example `server`) without changing the core schema above.
- Extensions should document their field schema, defaults, validation rules, and whether changes
  apply dynamically or require restart.
- Common extension: `server.port` (integer) enables the optional HTTP server described in Section
  13.7.

#### 5.3.1 `tracker` (object)

Fields:

- `kind` (string)
  - Required for dispatch.
  - Supported value: `github`
- `owner` (string)
  - Required. The GitHub repository owner (user or organization).
- `repo` (string)
  - Required. The GitHub repository name.
- `project_number` (integer, optional)
  - GitHub Projects v2 project number. When set, issue states are derived from the project board
    status field instead of labels. The project must be accessible with the configured auth token.
- `api_key` (string)
  - May be a literal token or `$VAR_NAME`.
  - Canonical environment variables: `GITHUB_TOKEN`, `GH_TOKEN`.
  - If `$VAR_NAME` resolves to an empty string, treat the key as missing.
  - The token must have `repo` scope (and `project` scope if `project_number` is used).
- `active_states` (list of strings or comma-separated string)
  - Default: `open`, `in progress`
  - These are matched against the normalized issue state. See Section 11 for state derivation.
- `terminal_states` (list of strings or comma-separated string)
  - Default: `closed`, `done`
- `filter_labels` (list of strings, optional)
  - When set, only issues bearing at least one of these labels are considered candidates. Useful
    for scoping Symphony to a subset of issues (for example `symphony`, `agent-ready`).
- `exclude_labels` (list of strings, optional)
  - Default: empty. Issues bearing any of these labels are excluded from dispatch.
- `blocked_label` (string, optional)
  - Default: `blocked`. Issues with this label are treated as blocked regardless of other state.

#### 5.3.2 `polling` (object)

Fields:

- `interval_ms` (integer or string integer)
  - Default: `30000`
  - Changes should be re-applied at runtime and affect future tick scheduling without restart.

#### 5.3.3 `workspace` (object)

Fields:

- `root` (path string or `$VAR`)
  - Default: `<system-temp>/symphony_workspaces`
  - `~` and strings containing path separators are expanded.
  - Bare strings without path separators are preserved as-is (relative roots are allowed but
    discouraged).

#### 5.3.4 `hooks` (object)

Fields:

- `after_create` (multiline shell script string, optional)
  - Runs only when a workspace directory is newly created.
  - Failure aborts workspace creation.
- `before_run` (multiline shell script string, optional)
  - Runs before each agent attempt after workspace preparation and before launching the coding
    agent.
  - Failure aborts the current attempt.
- `after_run` (multiline shell script string, optional)
  - Runs after each agent attempt (success, failure, timeout, or cancellation) once the workspace
    exists.
  - Failure is logged but ignored.
- `before_remove` (multiline shell script string, optional)
  - Runs before workspace deletion if the directory exists.
  - Failure is logged but ignored; cleanup still proceeds.
- `timeout_ms` (integer, optional)
  - Default: `60000`
  - Applies to all workspace hooks.
  - Non-positive values should be treated as invalid and fall back to the default.
  - Changes should be re-applied at runtime for future hook executions.

#### 5.3.5 `agent` (object)

Fields:

- `max_concurrent_agents` (integer or string integer)
  - Default: `10`
  - Changes should be re-applied at runtime and affect subsequent dispatch decisions.
- `max_retry_backoff_ms` (integer or string integer)
  - Default: `300000` (5 minutes)
  - Changes should be re-applied at runtime and affect future retry scheduling.
- `max_concurrent_agents_by_state` (map `state_name -> positive integer`)
  - Default: empty map.
  - State keys are normalized (`trim` + `lowercase`) for lookup.
  - Invalid entries (non-positive or non-numeric) are ignored.

#### 5.3.6 `claude` (object)

Fields:

- `command` (string shell command)
  - Default: `claude`
  - The runtime invokes this command as a CLI process in the workspace directory.
- `model` (string, optional)
  - Claude model to use (for example `claude-sonnet-4-20250514`). Passed via `--model` flag.
  - Default: whatever the installed Claude Code CLI defaults to.
- `permission_mode` (string)
  - Controls how Claude Code handles tool permissions.
  - Values:
    - `dangerously_skip` — pass `--dangerously-skip-permissions` flag. No permission prompts.
      Suitable for trusted/sandboxed environments.
    - `default` — use Claude Code's default permission behavior with any configured
      `.claude/settings.json` or `CLAUDE.md` in the workspace.
  - Default: `default`
- `permission_prompt_tool` (string, optional)
  - Path to a custom MCP tool or script that auto-responds to permission prompts. When set, this
    is passed via `--permission-prompt-tool`. Enables fine-grained permission control without
    fully skipping permissions.
- `max_turns` (integer, optional)
  - Maximum number of agentic turns per invocation. Passed via `--max-turns`.
  - Default: `20` (handled by the orchestrator, not necessarily by the CLI flag).
- `turn_timeout_ms` (integer)
  - Default: `3600000` (1 hour)
  - Maximum wall-clock time for a single Claude Code invocation before the process is killed.
- `stall_timeout_ms` (integer)
  - Default: `300000` (5 minutes)
  - If `<= 0`, stall detection is disabled.
  - Stall is detected when no stdout/stderr output has been observed for this duration.
- `output_format` (string)
  - Default: `json`
  - Passed via `--output-format`. Use `json` to get structured output including token usage.
- `system_prompt` (string, optional)
  - Additional system prompt text passed via `--system-prompt`. Appended to the rendered workflow
    prompt context.
- `append_system_prompt` (string, optional)
  - Text appended to the system prompt via `--append-system-prompt`.
- `allowedTools` (list of strings, optional)
  - Restrict Claude Code to specific tools via `--allowedTools`.
- `disallowedTools` (list of strings, optional)
  - Block specific tools via `--disallowedTools`.

### 5.4 Prompt Template Contract

The Markdown body of `WORKFLOW.md` is the per-issue prompt template.

Rendering requirements:

- Use a strict template engine (Liquid-compatible semantics are sufficient).
- Unknown variables must fail rendering.
- Unknown filters must fail rendering.

Template input variables:

- `issue` (object)
  - Includes all normalized issue fields, including labels and blockers.
- `attempt` (integer or null)
  - `null`/absent on first attempt.
  - Integer on retry or continuation run.

Fallback prompt behavior:

- If the workflow prompt body is empty, the runtime may use a minimal default prompt
  (`You are working on a GitHub issue.`).
- Workflow file read/parse failures are configuration/validation errors and should not silently fall
  back to a prompt.

### 5.5 Workflow Validation and Error Surface

Error classes:

- `missing_workflow_file`
- `workflow_parse_error`
- `workflow_front_matter_not_a_map`
- `template_parse_error` (during prompt rendering)
- `template_render_error` (unknown variable/filter, invalid interpolation)

Dispatch gating behavior:

- Workflow file read/YAML errors block new dispatches until fixed.
- Template errors fail only the affected run attempt.

## 6. Configuration Specification

### 6.1 Source Precedence and Resolution Semantics

Configuration precedence:

1. Workflow file path selection (runtime setting -> cwd default).
2. YAML front matter values.
3. Environment indirection via `$VAR_NAME` inside selected YAML values.
4. Built-in defaults.

Value coercion semantics:

- Path/command fields support:
  - `~` home expansion
  - `$VAR` expansion for env-backed path values
  - Apply expansion only to values intended to be local filesystem paths; do not rewrite URIs or
    arbitrary shell command strings.

### 6.2 Dynamic Reload Semantics

Dynamic reload is required:

- The software should watch `WORKFLOW.md` for changes.
- On change, it should re-read and re-apply workflow config and prompt template without restart.
- The software should attempt to adjust live behavior to the new config (for example polling
  cadence, concurrency limits, active/terminal states, claude settings, workspace paths/hooks, and
  prompt content for future runs).
- Reloaded config applies to future dispatch, retry scheduling, reconciliation decisions, hook
  execution, and agent launches.
- Implementations are not required to restart in-flight agent sessions automatically when config
  changes.
- Extensions that manage their own listeners/resources (for example an HTTP server port change) may
  require restart unless the implementation explicitly supports live rebind.
- Implementations should also re-validate/reload defensively during runtime operations (for example
  before dispatch) in case filesystem watch events are missed.
- Invalid reloads should not crash the service; keep operating with the last known good effective
  configuration and emit an operator-visible error.

### 6.3 Dispatch Preflight Validation

This validation is a scheduler preflight run before attempting to dispatch new work. It validates
the workflow/config needed to poll and launch workers, not a full audit of all possible workflow
behavior.

Startup validation:

- Validate configuration before starting the scheduling loop.
- If startup validation fails, fail startup and emit an operator-visible error.

Per-tick dispatch validation:

- Re-validate before each dispatch cycle.
- If validation fails, skip dispatch for that tick, keep reconciliation active, and emit an
  operator-visible error.

Validation checks:

- Workflow file can be loaded and parsed.
- `tracker.kind` is present and supported.
- `tracker.api_key` is present after `$` resolution.
- `tracker.owner` and `tracker.repo` are present and non-empty.
- `claude.command` is present and non-empty.

### 6.4 Config Fields Summary (Cheat Sheet)

This section is intentionally redundant so a coding agent can implement the config layer quickly.

- `tracker.kind`: string, required, currently `github`
- `tracker.owner`: string, required
- `tracker.repo`: string, required
- `tracker.project_number`: integer, optional (GitHub Projects v2)
- `tracker.api_key`: string or `$VAR`, canonical env `GITHUB_TOKEN` or `GH_TOKEN`
- `tracker.active_states`: list/string, default `open, in progress`
- `tracker.terminal_states`: list/string, default `closed, done`
- `tracker.filter_labels`: list of strings, optional
- `tracker.exclude_labels`: list of strings, optional
- `tracker.blocked_label`: string, default `blocked`
- `polling.interval_ms`: integer, default `30000`
- `workspace.root`: path, default `<system-temp>/symphony_workspaces`
- `hooks.after_create`: shell script or null
- `hooks.before_run`: shell script or null
- `hooks.after_run`: shell script or null
- `hooks.before_remove`: shell script or null
- `hooks.timeout_ms`: integer, default `60000`
- `agent.max_concurrent_agents`: integer, default `10`
- `agent.max_turns`: integer, default `20`
- `agent.max_retry_backoff_ms`: integer, default `300000` (5m)
- `agent.max_concurrent_agents_by_state`: map of positive integers, default `{}`
- `claude.command`: shell command string, default `claude`
- `claude.model`: string, optional
- `claude.permission_mode`: string, default `default`
- `claude.permission_prompt_tool`: string, optional
- `claude.max_turns`: integer, default `20`
- `claude.turn_timeout_ms`: integer, default `3600000`
- `claude.stall_timeout_ms`: integer, default `300000`
- `claude.output_format`: string, default `json`
- `claude.system_prompt`: string, optional
- `claude.append_system_prompt`: string, optional
- `claude.allowedTools`: list of strings, optional
- `claude.disallowedTools`: list of strings, optional
- `server.port` (extension): integer, optional; enables the optional HTTP server, `0` may be used
  for ephemeral local bind, and CLI `--port` overrides it

## 7. Orchestration State Machine

The orchestrator is the only component that mutates scheduling state. All worker outcomes are
reported back to it and converted into explicit state transitions.

### 7.1 Issue Orchestration States

This is not the same as tracker states (`open`, `in progress`, etc.). This is the service's internal
claim state.

1. `Unclaimed`
   - Issue is not running and has no retry scheduled.

2. `Claimed`
   - Orchestrator has reserved the issue to prevent duplicate dispatch.
   - In practice, claimed issues are either `Running` or `RetryQueued`.

3. `Running`
   - Worker task exists and the issue is tracked in `running` map.

4. `RetryQueued`
   - Worker is not running, but a retry timer exists in `retry_attempts`.

5. `Released`
   - Claim removed because issue is terminal, non-active, missing, or retry path completed without
     re-dispatch.

Important nuance:

- A successful worker exit does not mean the issue is done forever.
- The worker may continue through multiple back-to-back coding-agent invocations before it exits.
- After each normal invocation completion, the worker re-checks the tracker issue state.
- If the issue is still in an active state, the worker should start another invocation in the same
  workspace, up to `agent.max_turns`.
- The first invocation should use the full rendered task prompt.
- Continuation invocations should use `--resume` with the previous session ID and send only
  continuation guidance, not resend the original task prompt.
- Once the worker exits normally, the orchestrator still schedules a short continuation retry
  (about 1 second) so it can re-check whether the issue remains active and needs another worker
  session.

### 7.2 Run Attempt Lifecycle

A run attempt transitions through these phases:

1. `PreparingWorkspace`
2. `BuildingPrompt`
3. `LaunchingAgentProcess`
4. `RunningAgent`
5. `Finishing`
6. `Succeeded`
7. `Failed`
8. `TimedOut`
9. `Stalled`
10. `CanceledByReconciliation`

Distinct terminal reasons are important because retry logic and logs differ.

### 7.3 Transition Triggers

- `Poll Tick`
  - Reconcile active runs.
  - Validate config.
  - Fetch candidate issues.
  - Dispatch until slots are exhausted.

- `Worker Exit (normal)`
  - Remove running entry.
  - Update aggregate runtime totals.
  - Schedule continuation retry (attempt `1`) after the worker exhausts or finishes its in-process
    turn loop.

- `Worker Exit (abnormal)`
  - Remove running entry.
  - Update aggregate runtime totals.
  - Schedule exponential-backoff retry.

- `Agent Output Event`
  - Update live session fields, token counters, and activity timestamp.

- `Retry Timer Fired`
  - Re-fetch active candidates and attempt re-dispatch, or release claim if no longer eligible.

- `Reconciliation State Refresh`
  - Stop runs whose issue states are terminal or no longer active.

- `Stall Timeout`
  - Kill worker and schedule retry.

### 7.4 Idempotency and Recovery Rules

- The orchestrator serializes state mutations through one authority to avoid duplicate dispatch.
- `claimed` and `running` checks are required before launching any worker.
- Reconciliation runs before dispatch on every tick.
- Restart recovery is tracker-driven and filesystem-driven (no durable orchestrator DB required).
- Startup terminal cleanup removes stale workspaces for issues already in terminal states.

## 8. Polling, Scheduling, and Reconciliation

### 8.1 Poll Loop

At startup, the service validates config, performs startup cleanup, schedules an immediate tick, and
then repeats every `polling.interval_ms`.

The effective poll interval should be updated when workflow config changes are re-applied.

Tick sequence:

1. Reconcile running issues.
2. Run dispatch preflight validation.
3. Fetch candidate issues from tracker using active states.
4. Sort issues by dispatch priority.
5. Dispatch eligible issues while slots remain.
6. Notify observability/status consumers of state changes.

If per-tick validation fails, dispatch is skipped for that tick, but reconciliation still happens
first.

### 8.2 Candidate Selection Rules

An issue is dispatch-eligible only if all are true:

- It has `id`, `identifier`, `title`, and `state`.
- Its state is in `active_states` and not in `terminal_states`.
- It is not already in `running`.
- It is not already in `claimed`.
- Global concurrency slots are available.
- Per-state concurrency slots are available.
- It does not have the `blocked_label` (default: `blocked`).
- Blocker rule passes:
  - If the issue has blockers listed in `blocked_by`, do not dispatch when any blocker is
    non-terminal.

Sorting order (stable intent):

1. `priority` ascending (1..4 are preferred; null/unknown sorts last)
2. `created_at` oldest first
3. `identifier` lexicographic tie-breaker

### 8.3 Concurrency Control

Global limit:

- `available_slots = max(max_concurrent_agents - running_count, 0)`

Per-state limit:

- `max_concurrent_agents_by_state[state]` if present (state key normalized)
- otherwise fallback to global limit

The runtime counts issues by their current tracked state in the `running` map.

### 8.4 Retry and Backoff

Retry entry creation:

- Cancel any existing retry timer for the same issue.
- Store `attempt`, `identifier`, `error`, `due_at_ms`, and new timer handle.

Backoff formula:

- Normal continuation retries after a clean worker exit use a short fixed delay of `1000` ms.
- Failure-driven retries use `delay = min(10000 * 2^(attempt - 1), agent.max_retry_backoff_ms)`.
- Power is capped by the configured max retry backoff (default `300000` / 5m).

Retry handling behavior:

1. Fetch active candidate issues (not all issues).
2. Find the specific issue by `issue_id`.
3. If not found, release claim.
4. If found and still candidate-eligible:
   - Dispatch if slots are available.
   - Otherwise requeue with error `no available orchestrator slots`.
5. If found but no longer active, release claim.

Note:

- Terminal-state workspace cleanup is handled by startup cleanup and active-run reconciliation
  (including terminal transitions for currently running issues).
- Retry handling mainly operates on active candidates and releases claims when the issue is absent,
  rather than performing terminal cleanup itself.

### 8.5 Active Run Reconciliation

Reconciliation runs every tick and has two parts.

Part A: Stall detection

- For each running issue, compute `elapsed_ms` since:
  - `last_activity_timestamp` if any output has been seen, else
  - `started_at`
- If `elapsed_ms > claude.stall_timeout_ms`, terminate the worker and queue a retry.
- If `stall_timeout_ms <= 0`, skip stall detection entirely.

Part B: Tracker state refresh

- Fetch current issue states for all running issue IDs.
- For each running issue:
  - If tracker state is terminal: terminate worker and clean workspace.
  - If tracker state is still active: update the in-memory issue snapshot.
  - If tracker state is neither active nor terminal: terminate worker without workspace cleanup.
- If state refresh fails, keep workers running and try again on the next tick.

### 8.6 Startup Terminal Workspace Cleanup

When the service starts:

1. Query tracker for issues in terminal states (closed issues in the configured repo).
2. For each returned issue identifier, remove the corresponding workspace directory.
3. If the terminal-issues fetch fails, log a warning and continue startup.

This prevents stale terminal workspaces from accumulating after restarts.

## 9. Workspace Management and Safety

### 9.1 Workspace Layout

Workspace root:

- `workspace.root` (normalized path; the current config layer expands path-like values and preserves
  bare relative names)

Per-issue workspace path:

- `<workspace.root>/<sanitized_issue_identifier>`

Workspace persistence:

- Workspaces are reused across runs for the same issue.
- Successful runs do not auto-delete workspaces.

### 9.2 Workspace Creation and Reuse

Input: `issue.identifier`

Algorithm summary:

1. Sanitize identifier to `workspace_key`.
2. Compute workspace path under workspace root.
3. Ensure the workspace path exists as a directory.
4. Mark `created_now=true` only if the directory was created during this call; otherwise
   `created_now=false`.
5. If `created_now=true`, run `after_create` hook if configured.

Notes:

- This section does not assume any specific repository/VCS workflow.
- Workspace preparation beyond directory creation (for example dependency bootstrap, checkout/sync,
  code generation) is implementation-defined and is typically handled via hooks.

### 9.3 Optional Workspace Population (Implementation-Defined)

The spec does not require any built-in VCS or repository bootstrap behavior.

Implementations may populate or synchronize the workspace using implementation-defined logic and/or
hooks (for example `after_create` and/or `before_run`).

Failure handling:

- Workspace population/synchronization failures return an error for the current attempt.
- If failure happens while creating a brand-new workspace, implementations may remove the partially
  prepared directory.
- Reused workspaces should not be destructively reset on population failure unless that policy is
  explicitly chosen and documented.

### 9.4 Workspace Hooks

Supported hooks:

- `hooks.after_create`
- `hooks.before_run`
- `hooks.after_run`
- `hooks.before_remove`

Execution contract:

- Execute in a local shell context appropriate to the host OS, with the workspace directory as
  `cwd`.
- On POSIX systems, `sh -lc <script>` (or a stricter equivalent such as `bash -lc <script>`) is a
  conforming default.
- Hook timeout uses `hooks.timeout_ms`; default: `60000 ms`.
- Log hook start, failures, and timeouts.

Failure semantics:

- `after_create` failure or timeout is fatal to workspace creation.
- `before_run` failure or timeout is fatal to the current run attempt.
- `after_run` failure or timeout is logged and ignored.
- `before_remove` failure or timeout is logged and ignored.

### 9.5 Safety Invariants

This is the most important portability constraint.

Invariant 1: Run the coding agent only in the per-issue workspace path.

- Before launching the coding-agent subprocess, validate:
  - `cwd == workspace_path`

Invariant 2: Workspace path must stay inside workspace root.

- Normalize both paths to absolute.
- Require `workspace_path` to have `workspace_root` as a prefix directory.
- Reject any path outside the workspace root.

Invariant 3: Workspace key is sanitized.

- Only `[A-Za-z0-9._-]` allowed in workspace directory names.
- Replace all other characters with `_`.

## 10. Agent Runner Protocol (Claude Code CLI Integration)

This section defines the language-neutral contract for integrating Claude Code as the coding agent.

Claude Code is a CLI tool, not a JSON-RPC app-server. The integration model is fundamentally
different from a persistent app-server protocol: the orchestrator invokes the `claude` CLI as a
subprocess for each turn, passing the prompt as input and capturing structured output.

### 10.1 Launch Contract

Subprocess launch parameters:

- Command: `claude.command` (default: `claude`)
- Invocation: the orchestrator builds a command-line invocation with appropriate flags and executes
  it as a subprocess.
- Working directory: workspace path
- Stdout/stderr: captured separately
- Output format: `--output-format json` produces a JSON object on stdout upon completion

The Claude Code CLI is invoked in `--print` mode (non-interactive) for automation. The full
invocation pattern for a first turn:

```bash
claude --print \
  --output-format json \
  --max-turns <claude.max_turns> \
  [--model <claude.model>] \
  [--dangerously-skip-permissions] \
  [--permission-prompt-tool <path>] \
  [--system-prompt <text>] \
  [--append-system-prompt <text>] \
  [--allowedTools <tools>] \
  [--disallowedTools <tools>] \
  --prompt "<rendered prompt>"
```

For continuation turns on the same issue (resuming a previous session):

```bash
claude --print \
  --output-format json \
  --resume <session_id> \
  --max-turns <claude.max_turns> \
  [--model <claude.model>] \
  [--dangerously-skip-permissions] \
  --prompt "<continuation guidance>"
```

Notes:

- `--print` enables non-interactive mode. Claude Code reads the prompt, executes, and exits.
- `--output-format json` produces structured JSON output including token usage.
- `--resume <session_id>` continues a previous Claude Code session, preserving conversation history.
- The `--prompt` flag (or stdin pipe) provides the task text.
- Permission mode is controlled via `--dangerously-skip-permissions` or
  `--permission-prompt-tool`, not via a protocol handshake.

Recommended additional process settings:

- Max output capture: 50 MB (for safe buffering of stdout)
- The process should be spawned with `GITHUB_TOKEN` (or `GH_TOKEN`) in its environment so the
  agent can use `gh` CLI or GitHub API tools within the session.

### 10.2 Session and Turn Model

Unlike the Codex app-server which maintains a persistent process with a thread/turn protocol,
Claude Code uses a CLI-per-invocation model:

First turn:

1. Build the full rendered prompt from the workflow template + issue context.
2. Invoke `claude --print` with the prompt.
3. Wait for the process to exit.
4. Parse the JSON output from stdout.
5. Extract the `session_id` from the output for potential continuation.

Continuation turns:

1. Invoke `claude --print --resume <previous_session_id>` with continuation guidance as the prompt.
2. Wait for the process to exit.
3. Parse the JSON output.

Session identifiers:

- Claude Code outputs a `session_id` in its JSON output.
- Store this for `--resume` on continuation turns.
- The orchestrator's own `session_id` (for tracking) is distinct from Claude Code's session ID.

### 10.3 Output Processing

Claude Code with `--output-format json` produces a JSON object on stdout upon completion.

The output includes:

- `result` (string): the text response from Claude
- `is_error` (boolean): whether the session ended in error
- `total_cost_usd` (float): total cost of the session
- `usage` (object): token usage breakdown
  - `input_tokens` (integer)
  - `output_tokens` (integer)
  - `cache_read_input_tokens` (integer)
  - `cache_creation_input_tokens` (integer)
- `session_id` (string): Claude Code session identifier for `--resume`
- `num_turns` (integer): number of agent turns executed

Completion conditions:

- Process exit code 0 with `is_error: false` -> success
- Process exit code 0 with `is_error: true` -> failure (agent-level error)
- Process exit code non-zero -> failure (process-level error)
- Turn timeout (`turn_timeout_ms`) -> failure (process killed)
- Stall timeout (no output activity) -> failure (process killed)

Line handling during execution:

- While the process is running, monitor stdout/stderr for activity to detect stalls.
- Stderr output is diagnostic (Claude Code emits progress information to stderr).
- Update `last_activity_timestamp` whenever any output is observed on either stream.
- The final JSON output on stdout is parsed only after process exit.

### 10.4 Emitted Runtime Events (Upstream to Orchestrator)

The agent runner emits structured events to the orchestrator. Each event should include:

- `event` (enum/string)
- `timestamp` (UTC timestamp)
- `claude_pid` (if available)
- optional `usage` map (token counts)
- payload fields as needed

Events emitted by the runner:

- `session_started` — Claude Code process launched
- `activity_detected` — output observed (for stall detection updates)
- `session_completed` — process exited successfully with `is_error: false`
- `session_failed` — process exited with error
- `session_timed_out` — turn timeout exceeded, process killed
- `session_stalled` — stall timeout exceeded, process killed
- `session_canceled` — process killed due to reconciliation

### 10.5 Permission and Safety Policy

Permission and sandbox behavior is controlled via Claude Code CLI flags rather than a protocol
handshake.

Policy requirements:

- Each implementation should document its chosen permission posture.
- The recommended approach for fully automated environments is one of:
  - `--dangerously-skip-permissions` for trusted/sandboxed environments where all tool use is
    pre-approved.
  - `--permission-prompt-tool <path>` with a custom auto-approval tool for fine-grained control.
  - Default mode with a pre-configured `.claude/settings.json` in the workspace that allows
    the necessary tools.
- Implementations must ensure the agent process does not hang waiting for interactive input. In
  `--print` mode, Claude Code does not prompt for user input, but permission prompts can still
  block if not handled.

Example high-trust behavior:

- Use `--dangerously-skip-permissions` to bypass all permission checks.
- Set `GITHUB_TOKEN` in the environment for `gh` CLI access.
- Rely on workspace isolation and OS-level controls for safety.

Optional client-side tool extension:

- An implementation may pre-configure tools available to Claude Code via `CLAUDE.md` or
  `.claude/settings.json` in the workspace.
- Current optional standardized tool: `github_api` (see below).

`github_api` extension contract:

- Purpose: execute GitHub REST or GraphQL API calls using Symphony's configured tracker auth for
  the current session.
- Availability: only meaningful when `tracker.kind == "github"` and valid GitHub auth is configured.
- Implementation approach: rather than a client-side tool protocol (as with Codex app-server),
  this is typically provided by:
  1. Ensuring `gh` CLI is available in the workspace environment with `GITHUB_TOKEN` set, or
  2. Providing a custom MCP server tool that wraps GitHub API calls, or
  3. Including instructions in the workflow prompt for the agent to use `gh` CLI directly.
- The simplest conforming implementation is option (1): set `GITHUB_TOKEN` in the subprocess
  environment and instruct the agent to use `gh api` or `gh` subcommands in the workflow prompt.
- For GraphQL queries, the agent can use `gh api graphql -f query='...'`.
- Pagination: GitHub REST uses `Link` headers; `gh` CLI handles pagination with `--paginate`.
  GitHub GraphQL uses cursor-based pagination with `pageInfo { hasNextPage endCursor }`.

### 10.6 Timeouts and Error Mapping

Timeouts:

- `claude.turn_timeout_ms`: total wall-clock time for one `claude` invocation
- `claude.stall_timeout_ms`: enforced by orchestrator based on output inactivity

Error mapping (recommended normalized categories):

- `claude_not_found` — `claude` CLI not on PATH or not executable
- `invalid_workspace_cwd` — workspace path validation failed
- `turn_timeout` — process killed after `turn_timeout_ms`
- `stall_timeout` — process killed after no output for `stall_timeout_ms`
- `process_exit_error` — non-zero exit code
- `agent_error` — `is_error: true` in JSON output
- `output_parse_error` — stdout was not valid JSON
- `session_canceled` — process killed due to reconciliation

### 10.7 Agent Runner Contract

The `Agent Runner` wraps workspace + prompt + Claude Code CLI invocation.

Behavior:

1. Create/reuse workspace for issue.
2. Build prompt from workflow template.
3. Invoke Claude Code CLI with appropriate flags.
4. Monitor process for activity (stall detection).
5. On process exit, parse output and report result to orchestrator.
6. On any error, fail the worker attempt (the orchestrator will retry).

Note:

- Workspaces are intentionally preserved after successful runs.

## 11. Issue Tracker Integration Contract (GitHub)

### 11.1 Required Operations

An implementation must support these tracker adapter operations:

1. `fetch_candidate_issues()`
   - Return open issues in configured active states for the configured repository.

2. `fetch_issues_by_states(state_names)`
   - Used for startup terminal cleanup (fetch closed issues).

3. `fetch_issue_states_by_ids(issue_ids)`
   - Used for active-run reconciliation. For GitHub, this fetches issue state by issue number.

### 11.2 Query Semantics (GitHub)

GitHub-specific requirements for `tracker.kind == "github"`:

- REST API endpoint: `https://api.github.com` (or GitHub Enterprise endpoint if configured)
- Auth token sent in `Authorization: Bearer <token>` header
- `tracker.owner` and `tracker.repo` identify the repository

Candidate issue query:

- `GET /repos/{owner}/{repo}/issues?state=open&per_page=100&sort=created&direction=asc`
- If `tracker.filter_labels` is set, add `labels=<comma-separated>` query parameter.
- If `tracker.exclude_labels` is set, filter out matching issues client-side (GitHub REST API does
  not support label exclusion natively).
- Pagination: follow `Link` header `rel="next"` URLs until exhausted.
- Page size default: `100` (GitHub maximum).
- Network timeout: `30000 ms`.

State derivation:

- When `tracker.project_number` is not set:
  - Issue state is derived from its open/closed status and labels.
  - Open issues default to state `open`.
  - If an issue has a label matching an `active_states` entry (for example `in progress`), use that
    as the state.
  - Closed issues have state `closed`.
- When `tracker.project_number` is set:
  - Use the GitHub Projects v2 GraphQL API to fetch the project item's `Status` field value.
  - The status field value becomes the issue state (for example `Todo`, `In Progress`, `Done`).
  - Query:
    ```graphql
    query($owner: String!, $number: Int!, $cursor: String) {
      user(login: $owner) {  # or organization(login: $owner)
        projectV2(number: $number) {
          items(first: 50, after: $cursor) {
            pageInfo { hasNextPage endCursor }
            nodes {
              content {
                ... on Issue {
                  id
                  number
                  title
                  body
                  url
                  createdAt
                  updatedAt
                  state
                  labels(first: 20) { nodes { name } }
                  repository { nameWithOwner }
                }
              }
              fieldValueByName(name: "Status") {
                ... on ProjectV2ItemFieldSingleSelectValue { name }
              }
            }
          }
        }
      }
    }
    ```
  - GraphQL endpoint: `https://api.github.com/graphql`
  - Pagination: cursor-based via `pageInfo`.

Issue state refresh by IDs:

- For small sets of issue numbers, use individual REST calls:
  `GET /repos/{owner}/{repo}/issues/{number}`
- For larger sets, use GraphQL:
  ```graphql
  query($owner: String!, $repo: String!, $numbers: [Int!]!) {
    repository(owner: $owner, name: $repo) {
      issues(filterBy: {}) {
        # Note: GitHub GraphQL does not support filtering by number list directly.
        # Use individual node lookups instead.
      }
    }
  }
  ```
- Practical approach for reconciliation: fetch each running issue individually via REST, or batch
  via GraphQL `node` lookups using global node IDs.

Blocker detection:

- Check for the `blocked_label` (default: `blocked`) on the issue.
- Optionally parse the issue body for task list references like `- [ ] blocked by #123` and resolve
  those issue numbers to check their state.
- The simplest conforming implementation: treat any issue with the `blocked` label as blocked.

Important:

- GitHub API rate limits apply. The implementation should respect `X-RateLimit-Remaining` headers
  and back off when approaching limits. Use conditional requests (`If-None-Match` / ETags) where
  possible.

### 11.3 Normalization Rules

Candidate issue normalization should produce fields listed in Section 4.1.1.

Additional normalization details:

- `id` -> GitHub issue numeric ID (from API `id` field), converted to string
- `identifier` -> `owner/repo#number` or `#number` depending on config
- `labels` -> lowercase strings
- `blocked_by` -> derived from `blocked` label presence, or parsed from issue body references
- `priority` -> derived from `priority:N` labels (extract integer), or from project custom field.
  Non-integers become null.
- `branch_name` -> extracted from linked branches (if available via development API) or null
- `created_at` and `updated_at` -> parse ISO-8601 timestamps

### 11.4 Error Handling Contract

Recommended error categories:

- `unsupported_tracker_kind`
- `missing_tracker_api_key`
- `missing_tracker_owner_repo`
- `github_api_request` (transport failures)
- `github_api_status` (non-2xx HTTP)
- `github_api_rate_limited` (403 with rate limit headers)
- `github_graphql_errors`
- `github_unknown_payload`
- `github_missing_pagination` (pagination integrity error)

Orchestrator behavior on tracker errors:

- Candidate fetch failure: log and skip dispatch for this tick.
- Running-state refresh failure: log and keep active workers running.
- Startup terminal cleanup failure: log warning and continue startup.
- Rate limit hit: log warning, skip dispatch, and respect `Retry-After` or `X-RateLimit-Reset`
  headers before next attempt.

### 11.5 Tracker Writes (Important Boundary)

Symphony does not require first-class tracker write APIs in the orchestrator.

- Ticket mutations (state transitions, comments, PR metadata) are typically handled by the coding
  agent using `gh` CLI or GitHub API tools available in the workflow environment.
- The service remains a scheduler/runner and tracker reader.
- Workflow-specific success often means "reached the next handoff state" (for example adding a
  "needs-review" label) rather than tracker terminal state (closed).
- The `gh` CLI, pre-authenticated via `GITHUB_TOKEN` in the subprocess environment, is the
  recommended tool for agent-side tracker writes.

## 12. Prompt Construction and Context Assembly

### 12.1 Inputs

Inputs to prompt rendering:

- `workflow.prompt_template`
- normalized `issue` object
- optional `attempt` integer (retry/continuation metadata)

### 12.2 Rendering Rules

- Render with strict variable checking.
- Render with strict filter checking.
- Convert issue object keys to strings for template compatibility.
- Preserve nested arrays/maps (labels, blockers) so templates can iterate.

### 12.3 Retry/Continuation Semantics

`attempt` should be passed to the template because the workflow prompt may provide different
instructions for:

- first run (`attempt` null or absent)
- continuation run after a successful prior session
- retry after error/timeout/stall

### 12.4 Failure Semantics

If prompt rendering fails:

- Fail the run attempt immediately.
- Let the orchestrator treat it like any other worker failure and decide retry behavior.

## 13. Logging, Status, and Observability

### 13.1 Logging Conventions

Required context fields for issue-related logs:

- `issue_id`
- `issue_identifier`

Required context for coding-agent session lifecycle logs:

- `session_id`

Message formatting requirements:

- Use stable `key=value` phrasing.
- Include action outcome (`completed`, `failed`, `retrying`, etc.).
- Include concise failure reason when present.
- Avoid logging large raw payloads unless necessary.

### 13.2 Logging Outputs and Sinks

The spec does not prescribe where logs must go (stderr, file, remote sink, etc.).

Requirements:

- Operators must be able to see startup/validation/dispatch failures without attaching a debugger.
- Implementations may write to one or more sinks.
- If a configured log sink fails, the service should continue running when possible and emit an
  operator-visible warning through any remaining sink.

### 13.3 Runtime Snapshot / Monitoring Interface (Optional but Recommended)

If the implementation exposes a synchronous runtime snapshot (for dashboards or monitoring), it
should return:

- `running` (list of running session rows)
- each running row should include `turn_count`
- `retrying` (list of retry queue rows)
- `claude_totals`
  - `input_tokens`
  - `output_tokens`
  - `total_tokens`
  - `total_cost_usd`
  - `seconds_running` (aggregate runtime seconds as of snapshot time, including active sessions)
- `rate_limits` (latest GitHub API rate limit state, if tracked)

Recommended snapshot error modes:

- `timeout`
- `unavailable`

### 13.4 Optional Human-Readable Status Surface

A human-readable status surface (terminal output, dashboard, etc.) is optional and
implementation-defined.

If present, it should draw from orchestrator state/metrics only and must not be required for
correctness.

### 13.5 Session Metrics and Token Accounting

Token accounting rules:

- Claude Code with `--output-format json` reports token usage in the output JSON.
- Extract `usage.input_tokens`, `usage.output_tokens`, and compute total.
- Extract `total_cost_usd` for cost tracking.
- Each invocation's usage is additive (not cumulative across invocations).
- Accumulate aggregate totals in orchestrator state.

Runtime accounting:

- Runtime should be reported as a live aggregate at snapshot/render time.
- Implementations may maintain a cumulative counter for ended sessions and add active-session
  elapsed time derived from `running` entries (for example `started_at`) when producing a
  snapshot/status view.
- Add run duration seconds to the cumulative ended-session runtime when a session ends (normal exit
  or cancellation/termination).
- Continuous background ticking of runtime totals is not required.

Rate-limit tracking:

- Track GitHub API rate limit state from response headers (`X-RateLimit-Remaining`,
  `X-RateLimit-Reset`).
- Any human-readable presentation of rate-limit data is implementation-defined.

### 13.6 Humanized Agent Event Summaries (Optional)

Humanized summaries of agent process events are optional.

If implemented:

- Treat them as observability-only output.
- Do not make orchestrator logic depend on humanized strings.

### 13.7 Optional HTTP Server Extension

This section defines an optional HTTP interface for observability and operational control.

If implemented:

- The HTTP server is an extension and is not required for conformance.
- The implementation may serve server-rendered HTML or a client-side application for the dashboard.
- The dashboard/API must be observability/control surfaces only and must not become required for
  orchestrator correctness.

Enablement (extension):

- Start the HTTP server when a CLI `--port` argument is provided.
- Start the HTTP server when `server.port` is present in `WORKFLOW.md` front matter.
- `server.port` is extension configuration and is intentionally not part of the core front-matter
  schema in Section 5.3.
- Precedence: CLI `--port` overrides `server.port` when both are present.
- `server.port` must be an integer. Positive values bind that port. `0` may be used to request an
  ephemeral port for local development and tests.
- Implementations should bind loopback by default (`127.0.0.1` or host equivalent) unless explicitly
  configured otherwise.
- Changes to HTTP listener settings (for example `server.port`) do not need to hot-rebind;
  restart-required behavior is conformant.

#### 13.7.1 Human-Readable Dashboard (`/`)

- Host a human-readable dashboard at `/`.
- The returned document should depict the current state of the system (for example active sessions,
  retry delays, token consumption, cost, runtime totals, recent events, and health/error
  indicators).
- It is up to the implementation whether this is server-generated HTML or a client-side app that
  consumes the JSON API below.

#### 13.7.2 JSON REST API (`/api/v1/*`)

Provide a JSON REST API under `/api/v1/*` for current runtime state and operational debugging.

Minimum endpoints:

- `GET /api/v1/state`
  - Returns a summary view of the current system state (running sessions, retry queue/delays,
    aggregate token/runtime/cost totals, latest rate limits, and any additional tracked summary
    fields).
  - Suggested response shape:

    ```json
    {
      "generated_at": "2026-02-24T20:15:30Z",
      "counts": {
        "running": 2,
        "retrying": 1
      },
      "running": [
        {
          "issue_id": "123456",
          "issue_identifier": "owner/repo#42",
          "state": "in progress",
          "session_id": "a1b2c3d4",
          "turn_count": 3,
          "started_at": "2026-02-24T20:10:12Z",
          "last_activity_at": "2026-02-24T20:14:59Z",
          "tokens": {
            "input_tokens": 1200,
            "output_tokens": 800,
            "total_tokens": 2000
          },
          "cost_usd": 0.042
        }
      ],
      "retrying": [
        {
          "issue_id": "789012",
          "issue_identifier": "owner/repo#43",
          "attempt": 3,
          "due_at": "2026-02-24T20:16:00Z",
          "error": "no available orchestrator slots"
        }
      ],
      "claude_totals": {
        "input_tokens": 5000,
        "output_tokens": 2400,
        "total_tokens": 7400,
        "total_cost_usd": 0.156,
        "seconds_running": 1834.2
      },
      "github_rate_limits": {
        "remaining": 4832,
        "limit": 5000,
        "reset_at": "2026-02-24T21:00:00Z"
      }
    }
    ```

- `GET /api/v1/<issue_identifier>`
  - Returns issue-specific runtime/debug details for the identified issue.
  - Suggested response shape:

    ```json
    {
      "issue_identifier": "owner/repo#42",
      "issue_id": "123456",
      "status": "running",
      "workspace": {
        "path": "/tmp/symphony_workspaces/owner_repo_42"
      },
      "attempts": {
        "restart_count": 1,
        "current_retry_attempt": 2
      },
      "running": {
        "session_id": "a1b2c3d4",
        "claude_session_id": "sess_abc123",
        "turn_count": 3,
        "state": "in progress",
        "started_at": "2026-02-24T20:10:12Z",
        "last_activity_at": "2026-02-24T20:14:59Z",
        "tokens": {
          "input_tokens": 1200,
          "output_tokens": 800,
          "total_tokens": 2000
        },
        "cost_usd": 0.042
      },
      "retry": null,
      "recent_events": [
        {
          "at": "2026-02-24T20:14:59Z",
          "event": "activity_detected",
          "message": "output observed on stderr"
        }
      ],
      "last_error": null
    }
    ```

  - If the issue is unknown to the current in-memory state, return `404` with an error response (for
    example `{"error":{"code":"issue_not_found","message":"..."}}`).

- `POST /api/v1/refresh`
  - Queues an immediate tracker poll + reconciliation cycle (best-effort trigger; implementations
    may coalesce repeated requests).
  - Suggested request body: empty body or `{}`.
  - Suggested response (`202 Accepted`) shape:

    ```json
    {
      "queued": true,
      "coalesced": false,
      "requested_at": "2026-02-24T20:15:30Z",
      "operations": ["poll", "reconcile"]
    }
    ```

API design notes:

- The JSON shapes above are the recommended baseline for interoperability and debugging ergonomics.
- Implementations may add fields, but should avoid breaking existing fields within a version.
- Endpoints should be read-only except for operational triggers like `/refresh`.
- Unsupported methods on defined routes should return `405 Method Not Allowed`.
- API errors should use a JSON envelope such as `{"error":{"code":"...","message":"..."}}`.
- If the dashboard is a client-side app, it should consume this API rather than duplicating state
  logic.

## 14. Failure Model and Recovery Strategy

### 14.1 Failure Classes

1. `Workflow/Config Failures`
   - Missing `WORKFLOW.md`
   - Invalid YAML front matter
   - Unsupported tracker kind or missing tracker credentials/owner/repo
   - Missing coding-agent executable (`claude` not on PATH)

2. `Workspace Failures`
   - Workspace directory creation failure
   - Workspace population/synchronization failure (implementation-defined; may come from hooks)
   - Invalid workspace path configuration
   - Hook timeout/failure

3. `Agent Session Failures`
   - Claude Code process launch failure
   - Process exit with error (`is_error: true` or non-zero exit code)
   - Turn timeout (process killed)
   - Stall timeout (no output activity)
   - Output parse error (stdout not valid JSON)

4. `Tracker Failures`
   - API transport errors
   - Non-2xx status
   - GraphQL errors (when using Projects v2)
   - Rate limiting (403 with rate limit headers)
   - Malformed payloads

5. `Observability Failures`
   - Snapshot timeout
   - Dashboard render errors
   - Log sink configuration failure

### 14.2 Recovery Behavior

- Dispatch validation failures:
  - Skip new dispatches.
  - Keep service alive.
  - Continue reconciliation where possible.

- Worker failures:
  - Convert to retries with exponential backoff.

- Tracker candidate-fetch failures:
  - Skip this tick.
  - Try again on next tick.

- Reconciliation state-refresh failures:
  - Keep current workers.
  - Retry on next tick.

- Dashboard/log failures:
  - Do not crash the orchestrator.

- Rate limit failures:
  - Respect `Retry-After` or `X-RateLimit-Reset` headers.
  - Skip dispatch until rate limit resets.

### 14.3 Partial State Recovery (Restart)

Current design is intentionally in-memory for scheduler state.

After restart:

- No retry timers are restored from prior process memory.
- No running sessions are assumed recoverable.
- Service recovers by:
  - startup terminal workspace cleanup
  - fresh polling of active issues
  - re-dispatching eligible work

### 14.4 Operator Intervention Points

Operators can control behavior by:

- Editing `WORKFLOW.md` (prompt and most runtime settings).
- `WORKFLOW.md` changes should be detected and re-applied automatically without restart.
- Changing issue states in the tracker:
  - closing an issue -> running session is stopped and workspace cleaned when reconciled
  - removing active labels -> running session is stopped without cleanup
- Adding/removing labels (for example `blocked`, filter labels, exclude labels).
- Restarting the service for process recovery or deployment (not as the normal path for applying
  workflow config changes).

## 15. Security and Operational Safety

### 15.1 Trust Boundary Assumption

Each implementation defines its own trust boundary.

Operational safety requirements:

- Implementations should state clearly whether they are intended for trusted environments, more
  restrictive environments, or both.
- Implementations should state clearly whether they rely on `--dangerously-skip-permissions`,
  custom permission tools, pre-configured permission profiles, or some combination of those
  controls.
- Workspace isolation and path validation are important baseline controls, but they are not a
  substitute for whatever permission and sandbox policy an implementation chooses.

### 15.2 Filesystem Safety Requirements

Mandatory:

- Workspace path must remain under configured workspace root.
- Coding-agent cwd must be the per-issue workspace path for the current run.
- Workspace directory names must use sanitized identifiers.

Recommended additional hardening for ports:

- Run under a dedicated OS user.
- Restrict workspace root permissions.
- Mount workspace root on a dedicated volume if possible.

### 15.3 Secret Handling

- Support `$VAR` indirection in workflow config.
- Do not log API tokens or secret env values.
- Validate presence of secrets without printing them.
- `GITHUB_TOKEN` should be passed to Claude Code subprocess environment but never included in
  prompts or logs.

### 15.4 Hook Script Safety

Workspace hooks are arbitrary shell scripts from `WORKFLOW.md`.

Implications:

- Hooks are fully trusted configuration.
- Hooks run inside the workspace directory.
- Hook output should be truncated in logs.
- Hook timeouts are required to avoid hanging the orchestrator.

### 15.5 Harness Hardening Guidance

Running Claude Code agents against repositories, issue trackers, and other inputs that may contain
sensitive data or externally-controlled content can be dangerous. A permissive deployment can lead
to data leaks, destructive mutations, or full machine compromise if the agent is induced to execute
harmful commands or use overly-powerful integrations.

Implementations should explicitly evaluate their own risk profile and harden the execution harness
where appropriate. This specification intentionally does not mandate a single hardening posture, but
ports should not assume that tracker data, repository contents, prompt inputs, or tool arguments are
fully trustworthy just because they originate inside a normal workflow.

Possible hardening measures include:

- Using Claude Code's permission system (`--permission-prompt-tool` or `.claude/settings.json`)
  instead of `--dangerously-skip-permissions` to allow only necessary tools.
- Adding external isolation layers such as OS/container/VM sandboxing, network restrictions, or
  separate credentials beyond Claude Code's built-in permission controls.
- Filtering which GitHub issues, labels, or repositories are eligible for dispatch so untrusted or
  out-of-scope tasks do not automatically reach the agent.
- Scoping the `GITHUB_TOKEN` to minimal required permissions (for example using fine-grained
  personal access tokens with only the necessary repository and project scopes).
- Reducing the set of tools, credentials, filesystem paths, and network destinations available to
  the agent to the minimum needed for the workflow.

The correct controls are deployment-specific, but implementations should document them clearly and
treat harness hardening as part of the core safety model rather than an optional afterthought.

## 16. Reference Algorithms (Language-Agnostic)

### 16.1 Service Startup

```text
function start_service():
  configure_logging()
  start_observability_outputs()
  start_workflow_watch(on_change=reload_and_reapply_workflow)

  state = {
    poll_interval_ms: get_config_poll_interval_ms(),
    max_concurrent_agents: get_config_max_concurrent_agents(),
    running: {},
    claimed: set(),
    retry_attempts: {},
    completed: set(),
    claude_totals: {input_tokens: 0, output_tokens: 0, total_tokens: 0, total_cost_usd: 0, seconds_running: 0},
    github_rate_limits: null
  }

  validation = validate_dispatch_config()
  if validation is not ok:
    log_validation_error(validation)
    fail_startup(validation)

  startup_terminal_workspace_cleanup()
  schedule_tick(delay_ms=0)

  event_loop(state)
```

### 16.2 Poll-and-Dispatch Tick

```text
on_tick(state):
  state = reconcile_running_issues(state)

  validation = validate_dispatch_config()
  if validation is not ok:
    log_validation_error(validation)
    notify_observers()
    schedule_tick(state.poll_interval_ms)
    return state

  issues = tracker.fetch_candidate_issues()
  if issues failed:
    log_tracker_error()
    notify_observers()
    schedule_tick(state.poll_interval_ms)
    return state

  for issue in sort_for_dispatch(issues):
    if no_available_slots(state):
      break

    if should_dispatch(issue, state):
      state = dispatch_issue(issue, state, attempt=null)

  notify_observers()
  schedule_tick(state.poll_interval_ms)
  return state
```

### 16.3 Reconcile Active Runs

```text
function reconcile_running_issues(state):
  state = reconcile_stalled_runs(state)

  running_ids = keys(state.running)
  if running_ids is empty:
    return state

  refreshed = tracker.fetch_issue_states_by_ids(running_ids)
  if refreshed failed:
    log_debug("keep workers running")
    return state

  for issue in refreshed:
    if issue.state in terminal_states:
      state = terminate_running_issue(state, issue.id, cleanup_workspace=true)
    else if issue.state in active_states:
      state.running[issue.id].issue = issue
    else:
      state = terminate_running_issue(state, issue.id, cleanup_workspace=false)

  return state
```

### 16.4 Dispatch One Issue

```text
function dispatch_issue(issue, state, attempt):
  worker = spawn_worker(
    fn -> run_agent_attempt(issue, attempt, parent_orchestrator_pid) end
  )

  if worker spawn failed:
    return schedule_retry(state, issue.id, next_attempt(attempt), {
      identifier: issue.identifier,
      error: "failed to spawn agent"
    })

  state.running[issue.id] = {
    worker_handle,
    monitor_handle,
    identifier: issue.identifier,
    issue,
    session_id: generate_session_id(),
    claude_pid: null,
    claude_session_id: null,
    last_activity_timestamp: null,
    claude_input_tokens: 0,
    claude_output_tokens: 0,
    claude_total_tokens: 0,
    claude_cost_usd: 0,
    retry_attempt: normalize_attempt(attempt),
    started_at: now_utc(),
    turn_count: 0
  }

  state.claimed.add(issue.id)
  state.retry_attempts.remove(issue.id)
  return state
```

### 16.5 Worker Attempt (Workspace + Prompt + Claude Code)

```text
function run_agent_attempt(issue, attempt, orchestrator_channel):
  workspace = workspace_manager.create_for_issue(issue.identifier)
  if workspace failed:
    fail_worker("workspace error")

  if run_hook("before_run", workspace.path) failed:
    fail_worker("before_run hook error")

  max_turns = config.agent.max_turns
  turn_number = 1
  claude_session_id = null

  while true:
    if turn_number == 1:
      prompt = build_prompt(workflow_template, issue, attempt)
    else:
      prompt = build_continuation_prompt(issue, turn_number, max_turns)

    if prompt failed:
      run_hook_best_effort("after_run", workspace.path)
      fail_worker("prompt error")

    cmd = build_claude_command(prompt, claude_session_id)

    process = spawn_process(cmd, cwd=workspace.path, env={GITHUB_TOKEN: config.tracker.api_key})
    send(orchestrator_channel, {session_started, issue.id, process.pid})

    monitor_output_for_activity(process, orchestrator_channel, issue.id)

    result = wait_for_exit(process, timeout=config.claude.turn_timeout_ms)

    if result is timeout:
      kill(process)
      run_hook_best_effort("after_run", workspace.path)
      fail_worker("turn timeout")

    output = parse_json(result.stdout)
    if output failed:
      run_hook_best_effort("after_run", workspace.path)
      fail_worker("output parse error")

    send(orchestrator_channel, {usage_update, issue.id, output.usage, output.total_cost_usd})

    if output.is_error:
      run_hook_best_effort("after_run", workspace.path)
      fail_worker("agent error: " + output.result)

    claude_session_id = output.session_id

    refreshed_issue = tracker.fetch_issue_states_by_ids([issue.id])
    if refreshed_issue failed:
      run_hook_best_effort("after_run", workspace.path)
      fail_worker("issue state refresh error")

    issue = refreshed_issue[0] or issue

    if issue.state is not active:
      break

    if turn_number >= max_turns:
      break

    turn_number = turn_number + 1

  run_hook_best_effort("after_run", workspace.path)
  exit_normal()
```

### 16.6 Worker Exit and Retry Handling

```text
on_worker_exit(issue_id, reason, state):
  running_entry = state.running.remove(issue_id)
  state = add_runtime_seconds_to_totals(state, running_entry)

  if reason == normal:
    state.completed.add(issue_id)  # bookkeeping only
    state = schedule_retry(state, issue_id, 1, {
      identifier: running_entry.identifier,
      delay_type: continuation
    })
  else:
    state = schedule_retry(state, issue_id, next_attempt_from(running_entry), {
      identifier: running_entry.identifier,
      error: format("worker exited: %reason")
    })

  notify_observers()
  return state
```

```text
on_retry_timer(issue_id, state):
  retry_entry = state.retry_attempts.pop(issue_id)
  if missing:
    return state

  candidates = tracker.fetch_candidate_issues()
  if fetch failed:
    return schedule_retry(state, issue_id, retry_entry.attempt + 1, {
      identifier: retry_entry.identifier,
      error: "retry poll failed"
    })

  issue = find_by_id(candidates, issue_id)
  if issue is null:
    state.claimed.remove(issue_id)
    return state

  if available_slots(state) == 0:
    return schedule_retry(state, issue_id, retry_entry.attempt + 1, {
      identifier: issue.identifier,
      error: "no available orchestrator slots"
    })

  return dispatch_issue(issue, state, attempt=retry_entry.attempt)
```

## 17. Test and Validation Matrix

A conforming implementation should include tests that cover the behaviors defined in this
specification.

Validation profiles:

- `Core Conformance`: deterministic tests required for all conforming implementations.
- `Extension Conformance`: required only for optional features that an implementation chooses to
  ship.
- `Real Integration Profile`: environment-dependent smoke/integration checks recommended before
  production use.

Unless otherwise noted, Sections 17.1 through 17.7 are `Core Conformance`. Bullets that begin with
`If ... is implemented` are `Extension Conformance`.

### 17.1 Workflow and Config Parsing

- Workflow file path precedence:
  - explicit runtime path is used when provided
  - cwd default is `WORKFLOW.md` when no explicit runtime path is provided
- Workflow file changes are detected and trigger re-read/re-apply without restart
- Invalid workflow reload keeps last known good effective configuration and emits an
  operator-visible error
- Missing `WORKFLOW.md` returns typed error
- Invalid YAML front matter returns typed error
- Front matter non-map returns typed error
- Config defaults apply when optional values are missing
- `tracker.kind` validation enforces currently supported kind (`github`)
- `tracker.api_key` works (including `$VAR` indirection with `GITHUB_TOKEN` and `GH_TOKEN`)
- `tracker.owner` and `tracker.repo` are validated as present and non-empty
- `$VAR` resolution works for tracker API key and path values
- `~` path expansion works
- `claude.command` is preserved as a shell command string
- Per-state concurrency override map normalizes state names and ignores invalid values
- Prompt template renders `issue` and `attempt`
- Prompt rendering fails on unknown variables (strict mode)

### 17.2 Workspace Manager and Safety

- Deterministic workspace path per issue identifier
- Missing workspace directory is created
- Existing workspace directory is reused
- Existing non-directory path at workspace location is handled safely (replace or fail per
  implementation policy)
- Optional workspace population/synchronization errors are surfaced
- `after_create` hook runs only on new workspace creation
- `before_run` hook runs before each attempt and failure/timeouts abort the current attempt
- `after_run` hook runs after each attempt and failure/timeouts are logged and ignored
- `before_remove` hook runs on cleanup and failures/timeouts are ignored
- Workspace path sanitization and root containment invariants are enforced before agent launch
- Agent launch uses the per-issue workspace path as cwd and rejects out-of-root paths

### 17.3 Issue Tracker Client

- Candidate issue fetch uses active states and owner/repo
- GitHub REST query uses the correct repository endpoint
- Pagination follows `Link` header `rel="next"` URLs (REST) or cursor-based pagination (GraphQL)
- If `filter_labels` is configured, only matching issues are returned
- If `exclude_labels` is configured, matching issues are filtered out client-side
- Labels are normalized to lowercase
- Issue state refresh by number returns minimal normalized issues
- Blocker detection respects `blocked_label` configuration
- If `project_number` is configured, state is derived from Projects v2 status field
- Error mapping for request errors, non-2xx status, rate limits, GraphQL errors, malformed payloads

### 17.4 Orchestrator Dispatch, Reconciliation, and Retry

- Dispatch sort order is priority then oldest creation time
- Issue with `blocked` label (or configured `blocked_label`) is not eligible
- Issue with non-terminal blockers (if blocker parsing is implemented) is not eligible
- Issue with terminal blockers is eligible
- Active-state issue refresh updates running entry state
- Non-active state stops running agent without workspace cleanup
- Terminal state stops running agent and cleans workspace
- Reconciliation with no running issues is a no-op
- Normal worker exit schedules a short continuation retry (attempt 1)
- Abnormal worker exit increments retries with 10s-based exponential backoff
- Retry backoff cap uses configured `agent.max_retry_backoff_ms`
- Retry queue entries include attempt, due time, identifier, and error
- Stall detection kills stalled sessions and schedules retry
- Slot exhaustion requeues retries with explicit error reason
- If a snapshot API is implemented, it returns running rows, retry rows, token totals, cost, and
  rate limits
- If a snapshot API is implemented, timeout/unavailable cases are surfaced

### 17.5 Claude Code Agent Integration

- Launch command uses workspace cwd and invokes `claude --print` with appropriate flags
- `--output-format json` is passed to get structured output
- JSON output is parsed after process exit to extract usage, session_id, is_error, and result
- Turn timeout is enforced (process killed after `turn_timeout_ms`)
- Stall detection monitors stdout/stderr for activity and kills after `stall_timeout_ms`
- Continuation turns use `--resume <session_id>` with continuation prompt
- Permission mode is applied correctly:
  - `dangerously_skip` passes `--dangerously-skip-permissions`
  - `default` uses default Claude Code permission behavior
  - `permission_prompt_tool` passes `--permission-prompt-tool <path>` when configured
- `GITHUB_TOKEN` is passed in subprocess environment
- Non-zero exit code is treated as failure
- `is_error: true` in output is treated as failure
- Invalid JSON output is treated as failure

### 17.6 Observability

- Validation failures are operator-visible
- Structured logging includes issue/session context fields
- Logging sink failures do not crash orchestration
- Token and cost aggregation remains correct across repeated agent invocations
- If a human-readable status surface is implemented, it is driven from orchestrator state and does
  not affect correctness
- If humanized event summaries are implemented, they cover key event classes without changing
  orchestrator behavior

### 17.7 CLI and Host Lifecycle

- CLI accepts an optional positional workflow path argument (`path-to-WORKFLOW.md`)
- CLI uses `./WORKFLOW.md` when no workflow path argument is provided
- CLI errors on nonexistent explicit workflow path or missing default `./WORKFLOW.md`
- CLI surfaces startup failure cleanly
- CLI exits with success when application starts and shuts down normally
- CLI exits nonzero when startup fails or the host process exits abnormally

### 17.8 Real Integration Profile (Recommended)

These checks are recommended for production readiness and may be skipped in CI when credentials,
network access, or external service permissions are unavailable.

- A real tracker smoke test can be run with valid credentials supplied by `GITHUB_TOKEN` or
  `GH_TOKEN`.
- Real integration tests should use isolated test repositories/issues and clean up artifacts when
  practical.
- A skipped real-integration test should be reported as skipped, not silently treated as passed.
- If a real-integration profile is explicitly enabled in CI or release validation, failures should
  fail that job.

## 18. Implementation Checklist (Definition of Done)

Use the same validation profiles as Section 17:

- Section 18.1 = `Core Conformance`
- Section 18.2 = `Extension Conformance`
- Section 18.3 = `Real Integration Profile`

### 18.1 Required for Conformance

- Workflow path selection supports explicit runtime path and cwd default
- `WORKFLOW.md` loader with YAML front matter + prompt body split
- Typed config layer with defaults and `$` resolution
- Dynamic `WORKFLOW.md` watch/reload/re-apply for config and prompt
- Polling orchestrator with single-authority mutable state
- Issue tracker client with candidate fetch + state refresh + terminal fetch (GitHub REST/GraphQL)
- Workspace manager with sanitized per-issue workspaces
- Workspace lifecycle hooks (`after_create`, `before_run`, `after_run`, `before_remove`)
- Hook timeout config (`hooks.timeout_ms`, default `60000`)
- Claude Code CLI subprocess integration with `--print --output-format json`
- Claude Code launch command config (`claude.command`, default `claude`)
- Strict prompt rendering with `issue` and `attempt` variables
- Exponential retry queue with continuation retries after normal exit
- Configurable retry backoff cap (`agent.max_retry_backoff_ms`, default 5m)
- Reconciliation that stops runs on terminal/non-active tracker states
- Workspace cleanup for terminal issues (startup sweep + active transition)
- Structured logs with `issue_id`, `issue_identifier`, and `session_id`
- Operator-visible observability (structured logs; optional snapshot/status surface)

### 18.2 Recommended Extensions (Not Required for Conformance)

- Optional HTTP server honors CLI `--port` over `server.port`, uses a safe default bind host, and
  exposes the baseline endpoints/error semantics in Section 13.7 if shipped.
- Optional GitHub Projects v2 integration for richer state derivation from project board columns.
- Optional blocker parsing from issue body task list references.
- Persist retry queue and session metadata across process restarts.
- Make observability settings configurable in workflow front matter without prescribing UI
  implementation details.
- Add first-class tracker write APIs (comments/state transitions) in the orchestrator instead of
  only via agent tools.
- Add pluggable issue tracker adapters beyond GitHub.

### 18.3 Operational Validation Before Production (Recommended)

- Run the `Real Integration Profile` from Section 17.8 with valid credentials and network access.
- Verify hook execution and workflow path resolution on the target host OS/shell environment.
- If the optional HTTP server is shipped, verify the configured port behavior and loopback/default
  bind expectations on the target environment.
- Verify `claude` CLI is installed and accessible on the target host.
- Verify `gh` CLI is installed if the workflow prompt instructs the agent to use it for tracker
  writes.
