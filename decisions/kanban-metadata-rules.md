---
title: "Kanban Metadata Rules for Squad Handoffs"
tags: [decision, kanban, metadata, operations, multi-agent, standard]
related: [[kanban-doctrine]], [[kanban-vs-delegate-task]], [[a3-thinking]]
source: "internal-doctrine"
---

# Kanban Metadata Rules for Squad Handoffs

## Status: Accepted

Every `kanban_complete` call must include structured metadata. The shape of that metadata depends on the type of work performed. This decision record defines the schema for each work type.

## The Principle: A3 Structure

Every handoff follows the A3 format: what was the problem, what did we observe, what was the root cause, what did we do, and how do we know it worked?

## Metadata Schemas by Work Type

### Coding Task

```json
{
  "changed_files": ["path/to/file.py"],
  "tests_run": 14,
  "tests_passed": 14,
  "decisions": ["user_id primary, IP fallback for unauthenticated requests"],
  "migration_needed": false,
  "breaking_change": false
}
```

### Research Task

```json
{
  "sources_read": 12,
  "recommendation": "vLLM",
  "confidence": "high",
  "next_action": "spike: benchmark vLLM vs SGLang on our dataset"
}
```

### Review Task

```json
{
  "pr_number": 123,
  "findings": [
    {"severity": "critical", "file": "api/search.py", "line": 42, "issue": "raw SQL concat"}
  ],
  "approved": false,
  "blockers": ["SQL injection risk in /search"]
}
```

### Infrastructure / Ops Task

```json
{
  "services_affected": ["gateway", "dispatcher"],
  "rollback_plan": "revert commit abc123",
  "monitoring_added": true,
  "alert_thresholds": {"cpu": 80, "memory": 85}
}
```

### Documentation Task

```json
{
  "pages_created": ["guides/kanban-doctrine.md"],
  "pages_updated": ["INDEX.md"],
  "lint_passed": true,
  "cross_references_added": 4
}
```

## Universal Fields

Every metadata object should include:

- `work_type`: One of `[coding, research, review, infra, docs, analysis, other]`
- `estimated_effort`: `[trivial, small, medium, large, epic]` — updated if original estimate was wrong
- `risks`: Array of strings describing anything the next worker should know

## Anti-Patterns

**Do not** put secrets or tokens in metadata. It is persisted in SQLite forever.

**Do not** write narrative prose in metadata. Use the `summary` field of `kanban_complete` for prose. Metadata is for parsers.

**Do not** omit metadata because the task was "small." Small tasks compound into large systems. The cost of a missing handoff is paid by the next agent who has to rediscover what you already knew.

## Remember

The Substrate is only as trustworthy as its citations. The Kanban board is only as useful as its handoffs.
