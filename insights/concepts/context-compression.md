---
title: "Context Compression"
tags: [concept, context, compression, memory, agent-ops, prompt-caching]
related: [[agent-memory]], [[context-stack]], [[agent-native-operations]], [[subagent-architecture]]
---

# Context Compression

The techniques for preserving agent coherence when context windows exceed optimal thresholds.

## The Problem

Current models operate ideally around 140k tokens. Performance degrades above this. Naive compression (summarize everything at threshold) causes the agent to lose orientation: it preserves facts but forgets what it was doing, why it was doing it, and what comes next.

## Anchored Compression

Factory AI's solution: identify four things that must survive any compression in their original form:

1. **Latest changes made in the session.** The agent needs to know what it just did. Not a summary. The actual changes.
2. **The to-do list.** The active work queue. Without it, the agent loses its place.
3. **Agent instructions.** The behavioral contract (AGENTS.md equivalent). As context windows grow, models stop following instructions unless they persist unchanged.
4. **Session scaffolding.** Structural context: what kind of session, what's the goal, what stage are we in.

## The Rolling Anchor Mechanism

When the session hits ~140k, the system identifies the current message as an "anchor point." Everything before gets summarized by an LLM. The anchor message stays in full fidelity. Next compression: the previous anchor gets heavy weighting in the new summary. Critical anchors persist at full fidelity through every cycle.

This creates a telescoping history: recent context is detailed, older context is progressively compressed, but instructions, todos, and intent never disappear.

## Append-Only Constraint

All compression must feel append-only to the model for prompt caching to work. Any change to the message prefix invalidates cached KV pairs, making every subsequent response slower. The compression must preserve the cacheable prefix and compress only the tail.

This is a significant engineering constraint. You cannot restructure the whole context. You must preserve the prefix and append the compressed summary at the end.

## Connection to Handoffs

Our handoff system is manual anchored compression. We write a summary when we notice context getting high. Factory AI automates it at threshold. The principle is the same: ensure the next session knows where the previous one left off, what the current goal is, and what remains to be done.

## Connection to Other Concepts

- [[agent-memory]] -- Memory architecture for session continuity
- [[context-stack]] -- Where identity and protocols are encoded
- [[agent-native-operations]] -- Session management and boot sequences
- [[subagent-architecture]] -- Model-specific scaffolding and caching
