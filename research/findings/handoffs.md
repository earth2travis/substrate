---
title: "Handoffs Research"
tags: [handoffs, context, memory, llm, compaction, session, persistence]
related:
- context-compression
- context-stack
- agent-memory
- context-persistence
source: research/raw/handoffs.md
---
# Handoffs Research

Research into preserving context across LLM conversation boundaries.

## The Problem

LLM sessions are ephemeral. When context windows fill, compaction loses critical details: decisions, reasoning, rejected alternatives, relational context. How do we build infrastructure that survives this?

## Key Findings

- **Three-layer defense:** persistent files (long-term memory), session handoffs (episodic), daily notes (working memory)
- **Pre-compaction protocol:** write handoffs at 70-80% context, not when compaction fires
- **Memory formation over summarization:** selectively store what matters vs. compress everything equally
- **Observation masking:** hide old tool outputs, preserve reasoning (JetBrains/NeurIPS 2025)
- **Context rot:** performance degrades as context grows — attention is finite (Anthropic)
- **39% performance drop** in multi-turn vs. single-turn conversations (arXiv 2505.06120)

## Sources

- Anthropic: "Effective Context Engineering for AI Agents" (Sep 2025)
- Mother CLAUDE: "Session Handoffs" (Jan 2026)
- Context Compaction Research: Claude Code, Codex CLI, OpenCode, Amp (Dec 2025)
- JetBrains Research: "Smarter Context Management" (NeurIPS 2025)
- Substratia: "Ultimate Guide to Claude Code Context Management" (Jan 2026)
- Rajiv Pant: "How Claude's Memory Actually Works" (Dec 2025)
- Angelo Lima: "Context and Memory Management in Claude Code" (Dec 2025)
- Mem0: "LLM Chat History Summarization Guide" (Oct 2025)
- arXiv 2505.06120: "LLMs Get Lost In Multi-Turn Conversation" (May 2025)
