---
title: "Synthweave MCP Server and Data Model Analysis"
tags: [synthweave, mcp, agents, data-model, architecture, api]
related: [[harness-engineering]], [[lean-software-delivery]], [[codex]]
source: research/raw/synthweave-mcp-analysis.md
---

# Synthweave MCP Server and Data Model Analysis

## Summary

Synthweave exposes 22 MCP tools via StreamableHTTP (stateless), with API key auth using bcrypt verification. The data model uses PostgreSQL + Hasura GraphQL with 18 bounded contexts in a Turbo monorepo.

## Key Claims

1. **MCP Protocol:** Stateless StreamableHTTP transport at `POST /mcp`. Per-request transport instances. Health check at `GET /mcp/health`.
2. **Auth Model:** API Key format `sw_<prefix>_<secret>`, verified via bcrypt hash lookup against PostgreSQL.
3. **22 Tools:** Navigation (`ls`), Search (`snip_search`), Snip CRUD, Project Management, User Management. Hybrid semantic + full-text search.
4. **Data Model:** Organization -> Bases -> Projects -> Tasks/Snips. Vector search via pgvector. TipTap JSON content. Webhook event triggers on 33 tables.
5. **Workflow Engine:** Event-driven triggers (not DAG). BullMQ queues with exponential backoff. State machine: queued -> running -> completed/failed/waiting_for_user/cancelled.
6. **Integrations:** Auth0, OpenAI, Anthropic, Google AI, GitHub, Slack, AWS S3/SES, Serper, LlamaCloud. AES-256-GCM encryption for credentials.

## Implications

Synthweave's MCP tooling (22 tools) and DDD structure are strengths, but the lack of dependency boundary enforcement and minimal E2E coverage indicate harness engineering gaps. The event-driven trigger system is suitable for agent workflows but lacks full DAG orchestration.

## Related

- [[harness-engineering]] -- Agent-first development methodology
- [[synthweave-harness-readiness]] -- Overall harness evaluation
- [[lean-software-delivery]] -- Quality and testing discipline
- [[codex]] -- Primary agent coding tool
