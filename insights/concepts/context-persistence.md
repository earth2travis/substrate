---
title: "Context Persistence"
tags: [concept, context, memory, handoffs, llm, session, persistence, compaction]
related:
- context-stack
- context-compression
- agent-memory
- handoffs
updated: 2026-05-07
---
# Context Persistence

LLM sessions are ephemeral. When context windows fill, compaction loses critical details: decisions, reasoning, rejected alternatives, relational context. Building infrastructure that survives this requires a systematic approach.

## The Three-Layer Defense

**Persistent files (long-term memory):** knowledge graph, decision journal, skills. Survive across sessions, compacted or not.

**Session handoffs (episodic memory):** pre-compaction writeups capturing the state of work, open questions, and next steps. Written at 70-80% context capacity, not when compaction fires.

**Daily notes (working memory):** lightweight running record of what happened today. Quick to write, quick to scan. The first thing read in a new session.

## Key Findings from Research

- **Pre-compaction protocol matters:** write handoffs before compaction triggers, not after. Once compaction fires, details are already lost.
- **Memory formation over summarization:** selectively store what matters. Don't compress everything equally. Decisions and reasoning are more valuable than tool outputs.
- **Observation masking:** hide old tool outputs, preserve reasoning. Tool outputs are recoverable. Reasoning is not.
- **Context rot is real:** performance degrades as context grows. Attention is finite. Anthropic's research confirms this.
- **39% performance drop** in multi-turn vs. single-turn conversations (arXiv 2505.06120). The longer the session, the more the model degrades.

## Implementation Principles

1. **Write before you need to.** Handoffs at 70% context, not 100%.
2. **Separate recoverable from irreplaceable.** Tool outputs can be rerun. Decisions and reasoning cannot.
3. **Make reading frictionless.** The handoff must be scannable in seconds. Dense walls of text defeat the purpose.
4. **Link, don't duplicate.** Reference files by path. Don't paste content that lives elsewhere.
5. **Signal vs. noise.** Every handoff should answer: what changed, what's open, what's next.

## The Anti-Pattern

The most common failure: waiting until compaction fires, then writing a hurried summary of what was lost. By then, the details that mattered are gone. The summary is a performance of memory, not memory itself.
