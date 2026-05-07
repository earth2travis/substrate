---
title: "Factory AI Droid: Long Session Context Management"
tags: [finding, context, compression, scaffolding, prompt-caching, agent-ops]
related: [[agent-memory]], [[context-stack]], [[agent-native-operations]], [[subagent-architecture]]
source: research/raw/factory-ai-droid-session.md
ingested: 2026-05-07
---

# Factory AI Droid: Long Session Context Management

Factory AI's "Droid" maintained coherent behavior across 7 million token sessions without losing instructions or forgetting the plan. This is how they did it.

## Key Points

**Spec Mode vs Plan Mode.** Plan mode (Claude Code, Cursor) is tactical: "here are the actions I'll take." Spec mode (Factory AI) is strategic: "here is the complete picture of what we're building," mapping to full lifecycle (PRD -> engineering design -> prototype). Start every session in spec mode first. This is "by far the most successful" way to use Factory.

**The 140k Sweet Spot.** All current models operate ideally around 140k tokens. Performance degrades above this. Strategy: compress session state back to manageable size when approaching threshold, then continue.

**Naive Compression Fails.** Simple "compress everything at threshold" causes the agent to spend significant time re-exploring files and re-figuring out what needed to happen. Context preserved but orientation lost.

**The Four Anchors (What Must Survive Compression).**
1. Latest changes made in the session (actual changes, not summaries)
2. The to-do list (active work queue)
3. Agent instructions (AGENTS.md equivalent) — as context windows grow, models stop following it unless it persists unchanged
4. Session scaffolding (structural context: what kind of session, goal, stage)

**Anchored Summaries (Rolling Compression).** When hitting ~140k, the system identifies the current message as an "anchor point." Everything before gets summarized by an LLM. The anchor message stays in full fidelity. Next compression: the previous anchor gets heavy weighting in the new summary. Critical anchors (instructions, todos, intent) persist at full fidelity through every cycle. Recent context is detailed; older context is progressively compressed.

**Append-Only Message History.** Message history must be append-only to never break the prompt cache. Any change to the message prefix invalidates cached KV pairs. Linear history gives temporal grounding. Append-only sessions run "much, much quicker."

**Agent Scaffolding.** Beyond model and prompt: system notifications, tool descriptions, tool implementations, timeouts, prompt caching strategy, message history structure, model-agnostic harness. Scaffolding must be model-aware: OpenAI prefers `apply_patch`; Anthropic prefers find-and-replace.

**Connection to our system.** Our boot sequence (AGENTS.md, SOUL.md, TODO.md, memory files) already does what Factory anchors. Our handoffs are manual anchored summaries. The gap: automatic compression at threshold with explicit anchor preservation.

## Relevance

Our handoff system is doing manually what Factory automates. The anchored summary approach should inform pre-compaction state snapshots.

## Related

- [[agent-memory]] -- Memory architecture for session continuity
- [[context-stack]] -- Where identity and protocols are encoded
- [[agent-native-operations]] -- Session management and boot sequences
- [[subagent-architecture]] -- Model-specific scaffolding
