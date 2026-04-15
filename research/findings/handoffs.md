---
title: Handoffs Research
tags:
  - ai-agents
  - knowledge-management
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/handoffs.md
---

# Handoffs Research

Research into preserving context across LLM conversation boundaries.

## Problem

LLM sessions are ephemeral. When context windows fill, compaction loses critical details — decisions, reasoning, rejected alternatives, relational context. How do we build infrastructure that survives this?

## Key Findings

- **Three-layer defense:** persistent files (long-term memory), session handoffs (episodic), daily notes (working memory)
- **Pre-compaction protocol:** write handoffs at 70-80% context, not when compaction fires
- **Memory formation > summarization:** selectively store what matters vs. compress everything equally
- **Observation masking:** hide old tool outputs, preserve reasoning (JetBrains/NeurIPS 2025)
- **Context rot:** performance degrades as context grows — attention is finite (Anthropic)
- **39% performance drop** in multi-turn vs. single-turn conversations (arXiv 2505.06120)

## Sources

- [Anthropic: Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Sep 2025)
- [Mother CLAUDE: Session Handoffs](https://dev.to/dorothyjb/session-handoffs-giving-your-ai-assistant-memory-that-actually-persists-je9) (Jan 2026)
- [Context Compaction Research: Claude Code, Codex CLI, OpenCode, Amp](https://gist.github.com/badlogic/cd2ef65b0697c4dbe2d13fbecb0a0a5f) (Dec 2025)
- [JetBrains Research: Smarter Context Management](https://blog.jetbrains.com/research/2025/12/efficient-context-management/) (NeurIPS 2025)
- [Substratia: Ultimate Guide to Claude Code Context Management](https://substratia.io/blog/context-management-guide/) (Jan 2026)
- [Rajiv Pant: How Claude's Memory Actually Works](https://rajiv.com/blog/2025/12/12/how-claude-memory-actually-works-and-why-claude-md-matters/) (Dec 2025)
- [Angelo Lima: Context and Memory Management in Claude Code](https://angelo-lima.fr/en/claude-code-context-memory-management/) (Dec 2025)
- [Mem0: LLM Chat History Summarization Guide](https://mem0.ai/blog/llm-chat-history-summarization-guide-2025) (Oct 2025)
- [arXiv 2505.06120: LLMs Get Lost In Multi-Turn Conversation](https://arxiv.org/abs/2505.06120) (May 2025)

## Files

- `README.md` — this overview

## Related

- Handoff outputs: [`handoffs/`](../../handoffs/) (top-level directory)

- Guide: [`guides/handoff-guide.md`](../../guides/handoff-guide.md)
- Issue: [#17](https://github.com/earth2travis/sivart/issues/17)
