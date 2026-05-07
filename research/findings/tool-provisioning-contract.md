---
title: "Tool Provisioning Contract for Agent Workspaces"
tags: [tools, provisioning, mcp, agent-workspaces, contracts, loom]
related:
- tools-landscape
- workflows-landscape
- just-bash-analysis
- agent-native-operations
source: research/raw/tool-provisioning-contract.md
---
# Tool Provisioning Contract for Agent Workspaces

## Summary

A specification for making agent capabilities explicit, deterministic, and auditable. The original Loom spec treated capabilities as implicit: the workflow prompt describes what the agent should do, and the runtime environment hopefully has the tools. This breaks when different workflows need different tool surfaces, security requires scoping per issue type, or multiple MCP servers need coordinated provisioning.

The contract extends WORKFLOW.md frontmatter with a `tools` key declaring MCP servers, CLI tools, file injections, and permission scopes. The orchestrator provisions everything during workspace preparation before agent launch. If a required tool cannot be provisioned, the run fails at preparation, not mid-execution.

Key principles: the orchestrator provisions, the agent discovers; declarative over imperative; least privilege by default; tool availability is a precondition. Validation runs in four phases: CLI executable check, file injection, MCP configuration generation with health checks, and permission resolution.

Synthweave exposes 22 MCP tools today across intelligence (search, read, navigate), decision propagation (create, comment, rewrite, version, link), and project management. Six new tools would complete Loom integration: report_progress, report_blocker, sync_github_issue, check_ci_status, capture_evidence, and get_team_patterns.
