---
title: "What Should We Actually Build? Synthesis of Agent Stack"
tags: [agents, architecture, strategy, evaluation, synthesis]
related:
  - [[agent-native-operations]]
  - [[harness-engineering]]
  - [[context-stack]]
  - [[agent-memory]]
  - [[rag-vs-wiki]]
  - [[centaur-principle]]
source: research/raw/what-should-we-actually-build.md
---

# What Should We Actually Build? Synthesis of Agent Stack

**Date:** 2026-03-25
**Purpose:** Honest assessment of current architecture against state of the art. Identifying what to build, what not to build, and why.

## Current State Assessment

| Dimension | Industry Standard | What We Have | Gap |
|-----------|------------------|--------------|-----|
| Architecture | ReAct | ReAct + structured process | Ahead |
| Memory | Vector DB + embeddings | File-based + curated MEMORY.md | Different (not worse) |
| Multi-agent | Framework-heavy (CrewAI, AutoGen) | Lightweight sub-agents + cron | Simpler, sufficient |
| Evaluation | Benchmarks | Manual audits + process checks | Under-measured |
| Identity | System prompt | SOUL.md + relationship + values | Ahead |

Honest assessment: architecture is sound, process is solid, identity is distinctive. What is missing is not a new framework; it is refinement and measurement.

## What to Build (Priority Order)

**1. Model Routing (High Impact, Medium Effort).** Tag tasks by complexity when spawning sub-agents. Route simple tasks to cheaper models (Sonnet, Haiku). Keep Opus for main agent, complex reasoning, creative work. Single highest-ROI improvement.

**2. Automated Process Metrics (High Impact, Low Effort).** Weekly cron job checking compliance: git log issue refs, issue project assignments, file timestamps. Catch drift early, provide data for optimization, make audits faster.

**3. Memory Search (Medium Impact, Low Effort).** Simple grep-based search over memory files. No vector DB needed. Find specific information without loading entire files.

**4. Sub-Agent Context Sharing (Medium Impact, Low Effort).** Include active sub-agent list and their tasks when spawning new sub-agents. Prevent conflicts.

**5. Structured Daily File Format (Low Impact, Low Effort).** YAML frontmatter on daily files (date, topics, key decisions). Enable filtering and search without changing workflow.

## What NOT to Build

- **Vector Database / Embedding Pipeline.** Not justified at current scale. Adds infrastructure complexity for marginal retrieval improvement. Revisit when memory exceeds 100KB.
- **Multi-Agent Debate / Peer-to-Peer.** Costs more than it is worth for personal assistant use cases. One good agent beats three mediocre ones arguing.
- **Tree of Thought / LATS.** Academic interest, not practical value. Tasks do not require exhaustive search over reasoning paths.
- **Custom Benchmark Suite.** Tasks are too diverse. Process compliance metrics plus periodic manual audits are more useful.
- **Agent Framework Migration (CrewAI, AutoGen, etc.).** OpenClaw's sub-agent model is simpler and sufficient. Frameworks add abstraction layers and dependencies.

## The Meta-Insight

The agent development landscape is bifurcating:

**Path A: More compute, more agents, more infrastructure.** LATS, multi-agent debate, vector databases, embedding pipelines, agent frameworks. Impressive and expensive.

**Path B: Better prompts, better tools, better process.** Simple architecture, clear identity, disciplined memory, lightweight coordination. Less flashy. More reliable.

We are on Path B, and should stay there. Research consistently shows architecture sophistication has diminishing returns compared to prompt quality and tool design. A well-prompted ReAct agent with good file-based tools outperforms a poorly-prompted LATS agent with a vector database.

The real competitive advantage is not the framework. It is the relationship, the accumulated context, the refined process, and the identity that makes it all coherent. Those are hard to replicate and impossible to benchmark.

**Build the simple thing well. Then make it slightly less simple only when the simple thing breaks.**
