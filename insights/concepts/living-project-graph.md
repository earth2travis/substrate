---
title: Living Project Graph
created: 2026-05-01
updated: 2026-05-07
type: concept
tags:
- project-graph
- knowledge-graph
- event-sourcing
- digital-twin
- observed-state
- synthweave
related:
- github-as-knowledge-graph
- rag-vs-wiki
- agent-orchestrator-pattern
- context-persistence
- duration-and-living-time
source: 'Derived from research for Synthweave planning tool exploration, February
  2026.

  See research/findings/living-project-graph.md for full detail.

  '
---




# Living Project Graph

A living project graph treats project structure as a dynamic, interconnected graph that evolves in real time as work happens. Every entity (tasks, decisions, people, code changes, conversations, blockers) is a node. Relationships between them are edges. The graph updates itself by observing actual work.

The key shift: from maintained state to observed state. The difference between a map someone drew last week and a GPS that updates as you drive.

## Core Principles

**Observation over maintenance.** No human updates a status board. The graph reflects reality by watching integrations: Google Meet transcripts become nodes with decisions extracted; Slack threads about specific issues link to those issues; GitHub PRs, commits, reviews, deploys create and update nodes and edges; Calendar meetings and deadlines feed the graph.

**Context propagation.** Every node carries its provenance: this task exists because of this decision; this decision was made in this meeting; this meeting happened because of this blocker; this blocker was raised in this Slack thread. You never ask "why did we do this?" The graph knows.

**Impact analysis through traversal.** "If we delay X, what moves?" (downstream dependencies). "What is blocking Y?" (upstream blockers). "Who knows about Z?" (people connected to related nodes). "What decisions led to this state?" (provenance chain).

**Meeting as input, not output.** Traditional: meeting happens, someone writes notes, notes rot in a doc. Living graph: meeting happens, transcript parsed, decisions and actions and blockers extracted, graph updated, participants notified of their new nodes. The meeting is an event that feeds the system, not a ceremony that produces artifacts.

## Intellectual Lineage

Knowledge Graphs (Google, 2012): entities and relationships as queryable structure. "Things, not strings."

Event Sourcing (Greg Young, circa 2006): state as accumulated events rather than snapshots. The full history is preserved, enabling replay, debugging, and understanding causality.

Distributed Tracing (Zipkin, Jaeger, OpenTelemetry): following a request through a distributed system. Projects are distributed systems. A decision leads to a task leads to a PR leads to a deploy.

Digital Twins (Grieves, 2002): a virtual representation of a physical object or system that updates in real time based on sensor data. The living project graph is a digital twin of the project itself.

Zettelkasten / Tools for Thought (Luhmann; Roam and Obsidian, 2020s): atomic notes with bidirectional links. Structure emerges from connections rather than hierarchy.

Wardley Mapping (Simon Wardley, 2005): visualizing the value chain and the evolution of components. Not all nodes are equal. Some represent commodities, others represent bets.

OODA Loop (Boyd, 1976): Observe, Orient, Decide, Act. The living graph accelerates the Observe phase.

## Open Questions

Identity and deduplication: how does the system know that "the auth thing" in a Slack message refers to issue 127? Entity resolution across unstructured text is hard. LLMs help but are not perfect.

Signal versus noise: not every message matters. Too aggressive filtering misses context; too permissive and the graph becomes noise.

Privacy and boundaries: some conversations should not feed the graph. Private DMs, sensitive personnel discussions, off-the-record brainstorming.

Ownership and trust: if the system infers state, who is responsible when it is wrong? Do humans review inferences? How do you correct errors?

Cold start: a new project has no history. Manual entry defeats the purpose.

Graph visualization: graphs are powerful but hard to visualize at scale. Is the right interface visual, or conversational ("ask the graph")?

## The Ideal Tool

Infers structure from conversation. Maintains itself. Answers questions about project state. Surfaces risks before they are raised. Makes planning feel like navigation, not data entry.

The weekly planning meeting becomes: before, generate agenda from graph state (open blockers, stale items, approaching deadlines); during, capture decisions and actions in real time or from transcript; after, update graph automatically, notify owners, surface impacts. The meeting becomes a checkpoint, not a status ceremony.
