---
title: "Workflow as Contract"
tags: [symphony, orchestration, workflow, agent, contract, spec]
related: [[symphony-service-spec-github-claude]], [[symphony-orchestrator]], [[codex]], [[harness-engineering]], [[agent-native-operations]], [[cloudflare-first-agent-factory]], [[skills-as-portable-knowledge]]
source: research/findings/symphony-service-spec-github-claude.md
---

# Workflow as Contract

## Thesis

Agent behavior should be versioned in the repository alongside the code it operates on. A WORKFLOW.md contract separates policy (what the agent should do) from orchestration (how it is scheduled and run). This makes agent behavior reviewable, testable, and reversible like any other code change.

## The Symphony Pattern

The Symphony service specification defines a six-layer architecture:

1. **Policy Layer (repo-defined):** WORKFLOW.md prompt body and team-specific rules
2. **Configuration Layer:** Typed getters for runtime settings with defaults and validation
3. **Coordination Layer:** Polling loop, issue eligibility, concurrency, retries, reconciliation
4. **Execution Layer:** Filesystem lifecycle, workspace preparation, agent CLI invocation
5. **Integration Layer:** GitHub adapter for API calls and normalization
6. **Observability Layer:** Structured logs and operator-visible status

## Key Design Decisions

**Separation of Concerns:** The orchestrator reads the tracker and dispatches work. The agent writes tickets and executes code. Neither layer assumes the other's responsibilities.

**Per-Issue Workspaces:** Each issue gets an isolated workspace. Agent commands run only inside that directory. This prevents cross-contamination and enables parallel execution.

**Repository-Owned Policy:** WORKFLOW.md is version-controlled. Changes to agent behavior go through the same review process as code changes. Teams can experiment with prompts on branches.

**No Persistent Database Required:** Runtime state is kept in memory. Restart recovery uses tracker reconciliation, not database replay. This reduces operational complexity.

## The WORKFLOW.md Contract

A Markdown file with optional YAML front matter. Front matter covers tracker config (GitHub owner/repo/project, active/terminal states, labels), polling interval, workspace root, lifecycle hooks, concurrency limits, and agent CLI settings (model, permissions, timeouts, tool allowlists).

The Markdown body is the per-issue prompt template. Rendered with issue context at dispatch time.

## Trust and Safety Boundary

The specification intentionally does not mandate a single approval, sandbox, or operator-confirmation policy. Implementations choose their posture: high-trust for trusted environments, stricter controls for untrusted ones. This flexibility is a feature, not a gap.

## Connection to Harness Engineering

Harness engineering is the discipline that makes this pattern safe. Code review for WORKFLOW.md changes. CI validation of prompt templates. Gradual rollout of policy updates. The same rigor applied to application code applies to agent behavior.

## Connection to Cloudflare-First Agent Factory

A Cloudflare Worker can serve as the lightweight backend for the Integration Layer, handling CORS proxying and OAuth token exchange. Durable Objects can manage orchestrator state with restart recovery. The entire stack runs on the edge.

## Related

- [[symphony-service-spec-github-claude]] — The full specification for GitHub + Claude Code variant
- [[symphony-orchestrator]] — OpenAI Frontier's internal Elixir/BEAM implementation
- [[codex]] — The coding agent that Symphony dispatches
- [[harness-engineering]] — The discipline that makes autonomous agents safe
- [[agent-native-operations]] — Tools designed for AI-human partnership
- [[cloudflare-first-agent-factory]] — Edge platform for agent infrastructure
- [[skills-as-portable-knowledge]] — Agent behavior as versioned, composable instructions
