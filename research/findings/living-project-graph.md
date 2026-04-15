---
title: "Living Project Graph: Research Foundation"
tags:
  - research
related:
  - [[2026-02-10-ai-career-convergence]]
  - [[actual-occasions]]
  - [[alfred-north-whitehead]]
  - [[api-first-interfaces]]
source: research/raw/living-project-graph.md
---

# Living Project Graph: Research Foundation

_Research for [[Synthweave]] planning tool exploration_
_Started: February 14, 2026_

---

## The Core Concept

A living project graph treats project structure as a dynamic, interconnected graph that evolves in real time as work happens. Every entity (tasks, decisions, people, code changes, conversations, blockers) is a node. Relationships between them are edges. The graph updates itself by observing actual work.

**The key shift:** From maintained state to observed state. The difference between a map someone drew last week and a GPS that updates as you drive.

---

## Why Now?

Three converging forces make this possible:

1. **LLMs can parse unstructured context.** Before 2023, extracting meaning from a Slack thread or meeting transcript required humans. Now an agent can read a conversation and understand "this is a blocker for issue #47."

2. **Graph databases are mature.** Neo4j, Dgraph, and others can handle complex traversals at scale. The infrastructure exists.

3. **Integration density.** Modern teams generate enormous trails: commits, PRs, deploys, Slack messages, calendar events, docs, meeting recordings. The raw material for automatic graph construction exists.

---

## Intellectual Lineage

### Knowledge Graphs (Google, 2012)

Google's Knowledge Graph introduced the idea of entities and relationships as a queryable structure. "Things, not strings." Search became about understanding what you meant, not matching keywords.

**Relevance:** Project entities (tasks, people, decisions) should be first-class objects with typed relationships, not rows in a table.

### Event Sourcing (Greg Young, ~2006)

State as accumulated events rather than snapshots. Instead of "the task is blocked," you have "task created → assigned to Alice → blocked by infra issue → unblocked → completed." The full history is preserved.

**Relevance:** A living graph should capture how it arrived at its current state, not just what the state is. This enables replay, debugging, and understanding causality.

### Distributed Tracing (Zipkin, Jaeger, OpenTelemetry)

Following a request through a distributed system. Each service adds a span. The trace shows causality: what called what, where time was spent, where failures occurred.

**Relevance:** Projects are distributed systems. A decision leads to a task leads to a PR leads to a deploy. Tracing this flow is the same problem.

### Digital Twins (Grieves, 2002)

A virtual representation of a physical object or system that updates in real time based on sensor data. Used in manufacturing, aerospace, infrastructure.

**Relevance:** The living project graph is a digital twin of the project itself. The "sensors" are integrations: GitHub, Slack, Meet, etc.

### Zettelkasten / Tools for Thought (Luhmann; Roam/Obsidian, 2020s)

Atomic notes with bidirectional links. Structure emerges from connections rather than hierarchy. The "second brain" movement.

**Relevance:** Decisions, context, and rationale should be nodes that link to the work they spawned. Backlinks reveal impact.

### Wardley Mapping (Simon Wardley, 2005)

Visualizing the value chain of a system and the evolution of components. Strategic planning through spatial reasoning.

**Relevance:** Not all nodes are equal. Some represent commodities, others represent bets. The graph should surface strategic position.

### OODA Loop (Boyd, 1976)

Observe, Orient, Decide, Act. Decision-making as a continuous loop. Faster loops win.

**Relevance:** The living graph accelerates the Observe phase. You see the actual state, not a report about the state.

---

## Partial Implementations Today

### Linear

- Strong GitHub/Slack integration
- Cycles and projects provide structure
- Automatic status updates from PR activity
- **Gap:** Context lives outside the system. The "why" is scattered.

### Notion

- Flexible relations between databases
- Rich documents for context
- **Gap:** Relations are manual. State is maintained, not observed.

### GitHub Projects

- Native to where code lives
- Automation rules for status changes
- **Gap:** Siloed from conversations. No meeting context. No decision trail.

### Backstage (Spotify)

- Service catalog with ownership, dependencies, docs
- **Gap:** Designed for services, not projects. Operational, not planning.

### Roam / Obsidian

- Graph view of notes
- Bidirectional links
- **Gap:** Personal tools. Not multi-player. Not integrated with work systems.

### Notion AI / Linear AI / GitHub Copilot

- AI features bolted onto existing tools
- **Gap:** Assistants, not agents. They answer questions but don't observe and update state.

---

## What Would Be Different

### 1. Observation Layer

The system watches:

- **Google Meet:** Transcripts become nodes. Decisions mentioned become decision nodes linked to the conversation.
- **Slack:** Threads about specific issues link to those issues. Blockers raised become blocker nodes.
- **GitHub:** PRs, commits, reviews, deploys all create/update nodes and edges.
- **Calendar:** Meetings, deadlines, milestones.

No human updates a status board. The graph reflects reality.

### 2. Context Propagation

Every node carries its provenance:

- This task exists because of this decision
- This decision was made in this meeting
- This meeting happened because of this blocker
- This blocker was raised in this Slack thread

You never ask "why did we do this?" The graph knows.

### 3. Impact Analysis

Traversals answer questions:

- "If we delay X, what moves?" (downstream dependencies)
- "What's blocking Y?" (upstream blockers)
- "Who knows about Z?" (people connected to related nodes)
- "What decisions led to this state?" (provenance chain)

### 4. AI-Native Planning

An agent can:

- Traverse the graph to understand project state
- Suggest priorities based on dependencies and deadlines
- Identify risks (orphaned tasks, overloaded people, stale blockers)
- Prepare meeting agendas by surfacing what needs discussion
- Summarize progress without anyone writing an update

### 5. Meeting as Input, Not Output

Traditional: Meeting happens → someone writes notes → notes rot in a doc.

Living graph: Meeting happens → transcript parsed → decisions/actions/blockers extracted → graph updated → participants notified of their new nodes.

The meeting is an event that feeds the system, not a ceremony that produces artifacts.

### 6. Slack as Nervous System

Messages aren't chat. They're signals:

- Mentions of issues update those issue nodes
- Questions create "needs clarification" edges
- Blockers raised create blocker nodes
- Decisions stated create decision nodes

Slack becomes a sensor array, not a separate context to manage.

---

## Open Questions

### Identity and Deduplication

How does the system know that "the auth thing" in a Slack message refers to issue #127? Entity resolution across unstructured text is hard. LLMs help but aren't perfect.

### Signal vs Noise

Not every message matters. How do you filter? Too aggressive and you miss context. Too permissive and the graph becomes noise.

### Privacy and Boundaries

Some conversations shouldn't feed the graph. How do you handle:

- Private DMs?
- Sensitive personnel discussions?
- Off-the-record brainstorming?

### Ownership and Trust

If the system infers state, who's responsible when it's wrong? Do humans review inferences? How do you correct errors?

### Cold Start

A new project has no history. How do you bootstrap the graph? Manual entry defeats the purpose.

### Graph Visualization

Graphs are powerful but hard to visualize at scale. What's the right interface? Is it even visual, or is it conversational ("ask the graph")?

---

## The [[Synthweave]] Opportunity

### Integrations to Leverage

- **Google Meet:** Import transcripts → extract decisions, actions, blockers
- **Slack:** Observe threads → link to entities, surface signals
- **GitHub Projects:** Native integration → sync issues, PRs, milestones

### The Weekly Planning Meeting

The tool should:

- **Before:** Generate agenda from graph state (open blockers, stale items, approaching deadlines)
- **During:** Capture decisions and actions in real time (or from transcript)
- **After:** Update graph automatically, notify owners, surface impacts

The meeting becomes a checkpoint, not a status ceremony.

### What's Possible vs What's Ideal

Current tools can:

- Sync GitHub ↔ project boards
- Import meeting transcripts
- Post Slack notifications

The ideal tool:

- Infers structure from conversation
- Maintains itself
- Answers questions about project state
- Surfaces risks before they're raised
- Makes planning feel like navigation, not data entry

---

## Next Steps

1. **[[Ξ2T]] to share [[Synthweave]] investor deck** for context on the company and problem space
2. **Map existing workflow** (Meet → Slack → GitHub → Planning) to identify friction points
3. **Prototype concepts** for meeting-to-graph extraction
4. **Explore technical architecture** for observation layer

---

## References

- Singhal, A. (2012). "Introducing the Knowledge Graph." Google Blog.
- Young, G. (2010). "CQRS and Event Sourcing." DDD/CQRS Google Group.
- Wardley, S. (2016). "Wardley Maps." Creative Commons.
- Grieves, M. (2014). "Digital Twin: Manufacturing Excellence through Virtual Factory Replication."
- Boyd, J. (1976). "Destruction and Creation." US Army Command and General Staff College.

---

_This document is a living research foundation. Update as exploration continues._
