---
title: "GitHub usage, knowledge graphs, and second brain"
tags: [github, knowledge-graph, memory, institutional-memory, second-brain]
related: [github-as-memory, agent-native-operations, memory-systems, project-board-configuration]
source: research/raw/github-knowledge-graph-second-brain.md
---

# GitHub usage, knowledge graphs, and second brain

## Summary

Synthesis of repository documents mapping how GitHub is used as an operating system for work, how it connects to knowledge graphs and institutional memory, and adjacent second brain framing. Acts as a map to primary sources.

## Key Insights

### GitHub as Operating System

**Issues are memory:** every task documented; comments are the log; read the issue before work; create an issue if none exists. Labels, projects, and assignments should happen automatically.

**Comments are the heartbeat:** work start, decisions, and changes get commented; the issue is the single source of truth.

**Success criterion:** when someone asks for status of X, the answer is always in GitHub, not in someone's head.

### GitHub as Institutional Knowledge Graph

Thesis: GitHub Issues are nodes in an institutional knowledge graph. Issues hold decisions and context; the commit log is a timeline; PRs narrate change; comments preserve reasoning.

**GitHub Memory Protocol conventions:**
- Rich issue bodies with context
- Mandatory cross-references in "Related" section
- Closure protocol: outcome, artifacts, lessons, PR link
- Label hygiene
- Knowledge issues for decisions, learnings, patterns
- Search-oriented titles

### Living Project Graph

A living project graph treats entities (tasks, decisions, people, code, conversations) as nodes and relationships as edges. The graph updates by observing work, not only by manual status updates.

Intellectual lineage includes: knowledge graphs (Google), event sourcing (history and causality), distributed tracing (causality chains), digital twins (real-time mirror), and Zettelkasten (atomic notes, backlinks).

Partial implementations: Linear, Notion, GitHub Projects. Gaps: siloed from conversations and full decision trail.

### Obsidian and Wiki-Links

Adoption of frontmatter and `[[wiki-links]]` makes the workspace Obsidian-friendly. Wiki-links yield an emergent knowledge graph when entities are linked consistently, enabling visual graph views and backlinks.

### Agent Orchestration

The Symphony-style service (SPEC-github-claude) adapts OpenAI's Symphony spec with GitHub Issues as the tracker and Claude Code as the worker. Treats the tracker as the authoritative work queue.

### Source Index

Primary sources in repo: GOALS.md, AGENTS.md, CLAUDE.md, patterns/our-flow-map.md, research/project-management/github-as-memory.md, decisions/2026-02-04-github-best-practices.md, research/symphony/SPEC-github-claude.md, and memory architecture files.

## Synthesis

GitHub is both the operating system and the memory substrate. The gap is not in the tool but in the discipline: writing issues for the reader six months later, closing with context, and cross-referencing relentlessly. Agents that consume this graph downstream depend on the data quality we create today.
