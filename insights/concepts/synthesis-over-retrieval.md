---
title: Synthesis Over Retrieval
tags:
- agents
- knowledge
- synthesis
- retrieval
- memory
- rag
related:
- rag-vs-wiki
- agent-memory
- karpathy-llm-knowledge-bases
- automation-leverage
- context-stack
source: research/findings/synthesis-vs-retrieval-paradigm.md
---




# Synthesis Over Retrieval

The industry is focused on Retrieval (RAG, MCP, Vector Search): giving agents access to data. But access is not understanding. The deeper pattern is Synthesis: maintaining a continuously updated, conflict-resolved representation of reality.

## The Scavenger Hunt vs. The Library

**Retrieval** is a scavenger hunt. It starts from zero every time, finding fragments without context. A retrieval system returns whichever source it finds first. If Slack says "Friday" and Linear says "Wednesday," it returns one or both and leaves the user to resolve the conflict.

**Synthesis** is a library. It maintains a worldview. It resolves conflicts, determines authoritative sources, and presents a single, reasoned answer. It builds understanding that compounds over time.

## The "New Employee" Problem

Giving an agent access to Slack, Drive, and CRM is like hiring a new employee every morning and expecting decisions by lunch. The agent finds information but lacks temporal context and signal hierarchy. It is confidently wrong because it has no accumulated understanding.

## The Architecture Difference

Retrieval: Documents → Embed → Retrieve → Synthesize (every query)

Synthesis: Documents → Read → Understand → Write (once per source) → Query (from synthesized knowledge)

The synthesis approach pays upfront for cheap queries later. The retrieval approach pays per query, rediscovering from scratch every time.

## The Filesystem as Universal API

The best way to deliver synthesized understanding to agents is through a Context Graph stored as files. Every agent already knows how to read files. By decoupling the Substrate (Synthesis Layer) from the Agent (Execution Layer), we create a persistent, vendor-agnostic moat.

## Connection to Our System

Our Substrate is a synthesis system. We compile raw sources into findings, findings into concepts. The agent queries compiled knowledge, not raw sources. The cost is the compilation step. The benefit is persistent, compounding understanding.

The question is not "RAG or wiki?" but "what belongs in the synthesis layer and what stays in retrieval?" Facts that change daily: retrieval. Facts that compound over months: synthesis.
