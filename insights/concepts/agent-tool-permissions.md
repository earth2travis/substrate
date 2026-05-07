---
title: "Agent Tool Permissions"
tags: [concept, security, permissions, mcp, agent-tools, least-privilege]
related:
- tools-landscape
- just-bash-analysis
- composio-analysis
- tool-provisioning-contract
- the-openclaw-lesson
- agent-native-operations
- harness-engineering
- dark-factory
- cloudflare-first-agent-factory
- constitutional-governance
- agent-payment-infrastructure
- agent-orchestrator-pattern
- workspace-isolation
source: insights/concepts/agent-tool-permissions.md
---
# Agent Tool Permissions

## Thesis

Permission models are the weakest area across the entire agent tooling landscape. Current frameworks provide assignment-level permissions but no enforcement. An agent assigned to use a tool can typically do anything that tool can do, with no rate limits, no cost caps, and no audit trail. This is a production catastrophe waiting to happen.

## The Current State

MCP says "Hosts MUST obtain explicit user consent before invoking any tool." This is a guideline, not enforcement. OpenAI provides tool-level permissions in Assistants but uses blanket approval in practice. LangGraph has human-in-the-loop interrupt nodes (most granular control available). CrewAI assigns tools to agents but has no finer-grained permissions. AutoGen separates call authorization from execution (closest to a real model) but lacks enforcement.

## What Is Needed

1. **Per-tool policies**: Read vs write vs execute. Rate limits. Cost caps. An agent with a GitHub tool should not automatically have write access to every repository.
2. **Scope-based access**: Agent A can use tools X and Y but not Z. Current frameworks do assignment but not enforcement.
3. **Audit trails**: What was called, with what arguments, by which agent, with what result. LangSmith provides this for LangGraph. Others are ad hoc.
4. **Budget enforcement**: This agent can spend at most $5 in tool calls. Nobody implements this well.

## The just-bash Model

just-bash demonstrates a practical security approach for agent execution: per-instance command registry (agents only get registered commands), virtual filesystem with configurable access (read-only, copy-on-write, full), network disabled by default with URL prefix allow-lists, execution limits on loops/calls/expansion, and header transforms for credential injection (secrets never enter the sandbox).

The principle: provision capabilities at workspace preparation time, not at runtime. If a required tool cannot be provisioned, fail before the agent launches, not mid-execution.

## The Composio Alternative

Composio provides per-user credential isolation and automatic OAuth token refresh for supported toolkits. But it stores credentials on third-party servers, does not rotate API keys, has no expiry alerting, and is designed for multi-tenant SaaS rather than infrastructure teams. Its architectural patterns are worth stealing (meta tools for runtime discovery, auth config abstraction), but its security model introduces new trust boundaries.

## Recommendation for Synthweave

Build permission enforcement from scratch. The Loom tool provisioning contract already provides the declarative framework: WORKFLOW.md declares what tools an agent needs, and the orchestrator resolves declarations into scoped configurations. Extend this with:

- Token budget caps per agent per task
- Tool-level permission policies enforced at the MCP client layer
- Audit logging of every tool invocation with full context
- Circuit breakers that kill runs exceeding failure or cost thresholds

The principle is simple: least privilege by default, explicit capability grants, deterministic enforcement, immutable audit trails.
