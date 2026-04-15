---
title: "GitHub as Institutional Memory and Knowledge Graph"
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [infrastructure, memory, development]
sources:
  - raw/github-knowledge-graph-second-brain.md
---

# GitHub as Institutional Memory and Knowledge Graph

## Definition

The thesis that GitHub Issues, commits, and PRs are not merely a task tracker but **nodes in an institutional knowledge graph** — where decisions, context, and reasoning are preserved for future readers, not just current workers.

## Core Principles

### Issues as Memory
- Every task documented; comments are the log
- Issues written for "the reader six months later," not the person working today
- The issue is the single source of truth — success criterion: when someone asks for status, the answer is always in GitHub

### Flow Model
`Signal → Capture (GitHub issue) → Backlog → In Progress → Done → Integrated (PR merged)`

Capture friction is the primary failure point: "Issue First" is sometimes skipped in the moment, losing the memory link.

### GitHub Memory Protocol
Conventions for preserving knowledge quality:
- **Rich issue bodies** with context
- **Mandatory cross-references** ("Related" section)
- **Closure protocol** (outcome, artifacts, lessons, PR link)
- **Label hygiene**
- **Knowledge issues** for decisions, learnings, patterns (separate from task issues)
- **Monthly health checks** on issue memory quality

## Living Project Graph

Related concept: a **living project graph** where entities (tasks, decisions, people, code, conversations) are nodes; relationships are edges; the graph updates by observing work, not only by manual status updates.

**Intellectual lineage:**
- **Knowledge graphs** (Google, 2012): entities and typed relationships, "things not strings"
- **Event sourcing**: history and causality, not only current state
- **Distributed tracing**: causality chains across distributed project work
- **Digital twins**: real-time mirror; sensors include GitHub (PRs, commits, reviews, deploys)
- **Zettelkasten / tools for thought** (Roam, Obsidian): atomic notes, backlinks, second brain emergence

## Knowledge Graph Technology Landscape

| Topic | Description |
|---|---|
| **Rowboat** | Markdown + folders + LLM extraction + `backlinks`; existing knowledge management pattern |
| **MemPalace** | SQLite triple store for memory architecture |
| **Graphiti / Zep** | Temporal / bi-temporal graphs for knowledge tracking |
| **Hyperstack** | "Cards" as typed graph |
| **Loom** | `manage_reference_links`, knowledge graph language |
| **ClawVault / Obsidian** | Obsidian-style memory and graph layer with semantic search via MCP |

## Agent-Native PM Gaps

GitHub doesn't model well: **session context**, **process compliance for AI agents**, **capacity/WIP**, **research discoverability**, or a unified **decision primitive**. Proposed mitigations: session briefing scripts, process audits, capacity reports, research index generation, and decision logs with backlinks to issues.

## Symphony Orchestration

The Symphony-style service adapted from OpenAI's spec treats GitHub Issues and Projects v2 as the authoritative work queue, with Claude Code as the worker, `WORKFLOW.md` as versioned policy, and agent-side writes via `gh` / API.

## Connection to Zookooree

This concept maps to the [[llm-wiki-pattern]] as a parallel knowledge system: the wiki compounds knowledge from raw research sources; the knowledge graph compounds operational memory from work artifacts. Together they form a complete organizational memory: the *what we know* (wiki) and the *what we've decided/done* (graph).

## See Also

- [[llm-wiki-pattern]] -- parallel: wiki compounds research knowledge, graph compounds operational memory
- [[hermes-agent]] -- agent orchestration via Symphony uses GitHub as work queue
- [[dark-factory]] -- agents as autonomous workers whose output feeds the knowledge graph
