---
title: "Symphony Service Specification (GitHub + Claude Code Variant)"
tags: [symphony, orchestration, github, claude-code, agent-runner, spec]
related: [symphony-orchestrator, codex, hermes-agent, agent-native-operations]
source: research/raw/symphony-service-spec-github-claude.md
---

# Symphony Service Specification (GitHub + Claude Code Variant)

## Summary

Draft specification for a service that orchestrates coding agents using GitHub Issues/Projects as the tracker and Claude Code as the worker. Adapted from OpenAI Symphony SPEC.md. Defines system components, domain model, workflow contract, and runtime behavior.

## Key Insights

### Problem Statement

Symphony turns issue execution into a repeatable daemon workflow. It creates isolated per-issue workspaces and runs coding agent sessions inside them. Solves four problems: repeatability, isolation, versioned policy (WORKFLOW.md), and observability.

### System Components

1. **Workflow Loader:** Reads WORKFLOW.md, parses YAML front matter and prompt body
2. **Config Layer:** Typed getters for workflow config values with defaults and validation
3. **Issue Tracker Client:** Fetches candidate issues, normalizes payloads, handles reconciliation
4. **Orchestrator:** Owns poll tick, in-memory runtime state, dispatch decisions
5. **Workspace Manager:** Maps issue IDs to workspace paths, runs lifecycle hooks
6. **Agent Runner:** Creates workspace, builds prompt, launches Claude Code CLI
7. **Status Surface:** Operator-visible runtime status
8. **Logging:** Structured runtime logs

### Domain Model

**Issue:** Normalized record with id, identifier, title, description, priority, state, branch_name, url, labels, blocked_by, timestamps.

**Workflow Definition:** Parsed WORKFLOW.md with config map and prompt_template.

**Workspace:** Filesystem directory per issue with path, workspace_key, created_now flag.

**Run Attempt:** One execution attempt with issue_id, attempt number, workspace_path, started_at, status, error.

**Live Session:** Agent session metadata with session_id, claude_pid, token counts, cost, turn_count, claude_session_id for resume.

### Workflow Contract (WORKFLOW.md)

Markdown file with optional YAML front matter. Front matter schema covers tracker (kind, owner, repo, project_number, api_key, active_states, terminal_states, filter_labels, exclude_labels, blocked_label), polling (interval_ms), workspace (root), hooks (after_create, before_run, after_run, before_remove, timeout_ms), agent (max_concurrent_agents, max_retry_backoff_ms, max_concurrent_agents_by_state), and claude (command, model, permission_mode, max_turns, turn_timeout_ms, stall_timeout_ms, output_format, system_prompt, allowedTools, disallowedTools).

### Key Behaviors

- **Polling:** Fixed cadence with bounded concurrency
- **Reconciliation:** Stops active runs when issue state changes make them ineligible
- **Retries:** Exponential backoff for transient failures
- **Restart recovery:** No persistent database required
- **Trust and safety:** Implementation-defined; spec does not mandate approval/sandbox policy

### Important Boundary

- Symphony is a scheduler/runner and tracker reader
- Ticket writes (state transitions, comments, PR links) are performed by the coding agent via gh CLI or GitHub API
- A successful run may end at a workflow-defined handoff state (e.g., "needs-review"), not necessarily a closed issue

## Synthesis

This specification defines the architecture for an autonomous coding agent harness that treats GitHub Issues as the work queue and Claude Code as the executor. The WORKFLOW.md contract allows teams to version agent behavior with their code. The key design decision is separation of concerns: orchestrator reads and dispatches; agent writes and executes.

## Related

- [[workflow-as-contract]] — The promoted insight on versioning agent behavior in-repo
- [[symphony-orchestrator]] — OpenAI Frontier's internal Elixir/BEAM implementation
- [[codex]] — The coding agent that Symphony dispatches
