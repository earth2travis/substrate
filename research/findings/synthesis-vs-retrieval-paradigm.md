---
title: "Synthesis vs. Retrieval: The Scavenger Hunt vs. The Library"
tags: [agents, knowledge, rag, synthesis, context, memory]
related:
  - [[rag-vs-wiki]]
  - [[agent-memory]]
  - [[karpathy-llm-knowledge-bases]]
  - [[automation-leverage]]
  - [[synthesis-over-retrieval]]
source: research/raw/synthesis-vs-retrieval-paradigm.md
---

# Synthesis vs. Retrieval: The Scavenger Hunt vs. The Library

**Source:** https://x.com/contextconor/status/2045957951278739520, April 20, 2026

## The Claim

The current AI industry is focused on **Retrieval** (RAG, MCP, Vector Search) — giving agents "access" to data. However, access is not understanding. A retrieval system is like a scavenger hunt: it starts from zero every time, finding fragments without context. A **Synthesis System** is like a library or a "Company Brain": it maintains a continuously updated, conflict-resolved representation of reality.

## The "New Employee" Problem

Giving an agent access to Slack, Drive, and CRM is like hiring a new employee every morning and expecting them to make decisions by lunch. They will find information, but they will be "confidently wrong" because they lack **temporal context** and **signal hierarchy**.

## Retrieval is Fragmented; Synthesis is Unified

**Retrieval:** Returns whichever source it finds first. If Slack says "Friday" and Linear says "Wednesday," it might return both or just one, leaving the user to resolve the conflict.

**Synthesis:** Resolves the conflict, determines the authoritative source, and presents a single, reasoned answer. It builds a **Worldview** rather than just a list of facts.

## The Filesystem as the Universal API

The best way to deliver this "Synthesized Understanding" to agents is through a **Context Graph** stored as files. Every agent (Claude Code, Cursor, OpenClaw) already knows how to read files. By decoupling the "Brain" (Synthesis Layer) from the "Agent" (Execution Layer), we create a persistent, vendor-agnostic moat.

## The Architecture

Retrieval: Documents → Embed → Retrieve → Synthesize (every query)

Synthesis: Documents → Read → Understand → Write (once per source) → Query (from synthesized knowledge)

The synthesis approach pays upfront (compile sources into structured knowledge) for cheap queries later. The retrieval approach pays per query (rediscover from scratch every time).

## Connection to Our System

Our Substrate is a synthesis system. We compile raw sources into findings, findings into concepts. The agent queries the compiled knowledge, not the raw sources. The cost is the compilation step. The benefit is persistent, compounding understanding.

The question is not "RAG or wiki?" but "what belongs in the synthesis layer and what stays in retrieval?" Facts that change daily: retrieval. Facts that compound over months: synthesis.
