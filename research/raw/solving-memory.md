# [Solving Memory for [[OpenClaw]] & General Agents](https://x.com/sillydarket/status/2022394007448429004?s=43&t=jEKzkG7y7osog41OjAm09Q)

Every AI agent you've ever used has the same fatal flaw: **context death**.

The moment a session ends, everything dies. Decisions, preferences, relationships, project context — gone. Your "intelligent" assistant wakes up tomorrow as a stranger.

We spent months obsessing over this problem at Versatly. The result is **ClawVault™** — an open-source memory architecture that gives AI agents something they've never had: **continuity**.

Here's what we learned building it. And why Obsidian's approach to knowledge was the key insight that unlocked everything.

## The Research That Changed Our Approach

We benchmarked every agent memory solution we could find. Mem0, Zep, vector databases, custom RAG pipelines. Measured them against LoCoMo (a long-context memory benchmark).

The results were humbling:

- Specialized memory tools: 68.5%
- Simple filesystem with markdown files: 74.0%

Read that again. Plain markdown files — organized in folders, with grep and search — **outperformed purpose-built memory infrastructure**.

Why? Because LLMs already know how to work with files. They've seen billions of examples of reading, searching, and organizing text during training. Fighting that instinct with specialized APIs is swimming upstream.

## The Obsidian Insight

Obsidian got something profoundly right: your notes are just files.

No proprietary database. No cloud lock-in. Markdown files in folders. The magic is in the **structure on top**: YAML frontmatter for metadata, wiki-links for connections, and a graph view that emerges from the relationships.

We realized agent memory should work exactly the same way.

ClawVault stores every memory as a markdown file with YAML frontmatter:

```yaml
---
title: "Architecture Decision: Event-Driven Pipeline"
date: 2026-02-12
category: decisions
memoryType: decision
priority: 🔴
tags: [architecture, pipeline, backend]
---

Chose event-driven over request-response for the ingestion layer.
Reasoning: 3x throughput at scale, natural backpressure handling...
```

This is simultaneously:

- A ClawVault document the agent can search and retrieve
- An Obsidian note with full Properties panel support
- A plain text file any tool can read

One format. Zero lock-in. Complete interoperability.

## Memory Types Matter

Here's a lesson that took us embarrassingly long to learn: **not all memories are equal**.

When a human says "remember this," what _kind_ of thing are they asking you to remember?

- A **decision** (chose React over Vue)
- A **preference** (likes dark mode)
- A **relationship** (Sarah is the CTO)
- A **commitment** (promised to follow up Friday)
- A **lesson** (never deploy on Fridays)

ClawVault enforces this taxonomy. Every memory is typed. Why? Because "show me all decisions from last month" only works if you stored them AS decisions. Dumping everything into a single notes file is the agent equivalent of writing on your hand.

The extendable category system maps directly to Obsidian folders:

```
vault/
├── decisions/
├── people/
├── lessons/
├── projects/
├── commitments/
├── preferences/
└── handoffs/
```

Open this in Obsidian and you get instant visual organization. The agent navigates it programmatically. Same structure serves both.

## The Memory Graph

Here's where it gets interesting.

ClawVault uses wiki-links (`[[entity-name]]`) inside notes, exactly like Obsidian. When the agent writes about a person, project, or decision, it links to them:

```markdown
Discussed [[hale-pet-door]] migration with [[justin-dukes]].
Decision: proceed with [[event-driven-architecture]] per [[2026-02-10-standup]].
```

Run `clawvault link --all` and it auto-detects entity mentions across the vault. The result is a **knowledge graph** — the same graph you'd see in Obsidian's graph view.

> 6 day old memory graph for one of our clients

But for the agent, this graph is **navigable context**. When asked about Hale Pet Door, the agent doesn't just find the project file — it traverses links to find related decisions, people, commitments, and lessons. The graph IS the agent's associative memory.

## Observational Memory: Compression That Preserves Signal

_(Quick note: we are not convinced we need observational memory.)_

Raw conversation transcripts are too noisy and too large. But naive summarization loses critical details.

ClawVault's observational memory system compresses conversations into priority-tagged observations:

- 🔴 **Critical** — decisions, commitments, blockers
- 🟡 **Notable** — insights, preferences, context
- 🟢 **Background** — routine updates, low-signal content

On wake, the agent loads 🔴 observations first, then fills remaining context budget with 🟡, then 🟢. This is **budget-aware context injection** — the most important memories always make it into the window, regardless of how much history exists.

The compression happens via LLM (Gemini Flash — fast and cheap), but here's the critical insight: **LLMs rewrite keywords during compression**. "Decision: use Postgres" becomes "Postgres was selected for the database layer." If you're pattern-matching on "Decision:" downstream, you'll miss it.

Our fix: regex-based priority enforcement AFTER LLM compression. Trust the LLM for compression quality, not for classification accuracy.

## The Vault Index Pattern

For agents working in Obsidian-compatible vaults, we use a **vault index** — a single file listing every note with a one-line description:

| Note                      | Description                                         |
| ------------------------- | --------------------------------------------------- |
| decisions/event-driven.md | Chose event-driven architecture for ingestion       |
| people/justin-dukes.md    | Sr Ops Manager at Hale Pet Door, primary contact    |
| lessons/deploy-fridays.md | Production incident from Friday deploy, never again |

The agent scans the index FIRST before deciding what to read. This is dramatically more efficient than embedding search for most queries — a single file read vs. a vector similarity computation. The index is the table of contents; embeddings are the search engine. Use both.

## Zero Cloud, Full Sovereignty

ClawVault makes zero network calls (except optional LLM for observation compression). No telemetry. No sync service. No cloud dependency.

Your agent's memories live on your filesystem. Period.

This isn't an ideological choice — it's an architectural one. Agent memories contain the most sensitive operational data in your organization: decisions, relationships, strategies, mistakes. That data should never leave your infrastructure unless you explicitly choose to send it somewhere.

## What This Means

The agent memory problem isn't a technology problem. It's a **design** problem.

The tools already exist. Markdown files. YAML frontmatter. Folder hierarchies. Wiki-links. Obsidian proved this works for humans. ClawVault proves it works for agents.

The insight is that human knowledge management and agent memory management are **the same problem**. Both need:

1. Typed, structured storage
2. Associative linking between concepts
3. Priority-based retrieval under budget constraints
4. Compression that preserves signal
5. Zero lock-in to any platform

When your agent's memory vault IS an Obsidian vault, something remarkable happens: you can **see** what your agent knows. Open the graph view. Browse the folders. Read the frontmatter. The agent's memory becomes inspectable, auditable, and editable by humans.

That's not a feature. That's the whole point.

---

ClawVault™ is fully open source and ready for you to use today.

- **GitHub:** <https://github.com/Versatly/clawvault>
- **npm:** `npm install clawvault` — <https://www.npmjs.com/package/clawvault>
- **Docs:** <https://clawvault.dev>

Built by Versatly — we deploy autonomous AI employees that actually remember into real businesses.

If context death has been killing your agents, come try ClawVault.
