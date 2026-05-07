---
title: "Prompt Caching: Deep Research"
tags: [agents, performance, cost, caching, infrastructure]
related:
  - [[agent-native-operations]]
  - [[harness-engineering]]
  - [[proof-of-work]]
source: research/raw/prompt-caching.md
---

# Prompt Caching: Deep Research

Research compiled from Anthropic API docs, Claude Code Camp experiments, OpenClaw docs, and Thariq's thread "Lessons from Building Claude Code: Prompt Caching Is Everything."

## What Prompt Caching Actually Is

Not response caching. It caches the intermediate computation (KV cache: Key and Value matrices from attention layers) that the model builds while reading the prompt. When the next request shares the same prefix, the model skips recomputing those tokens.

The KV cache for a 100K token prompt on Opus is estimated at 500MB to 1GB of GPU VRAM. That is what Anthropic stores and retrieves per request.

## Economics (Opus 4.6)

| Operation | Cost per MTok |
|-----------|---------------|
| Base input | $5.00 |
| 5 min cache write | $6.25 |
| 1 hour cache write | $10.00 |
| Cache read | $0.50 |

A 100K token session at 90% cache hit rate: ~$19 vs ~$100 without caching. This is why Claude Code Pro at $20/month is viable.

## Key Mechanics

**Prefix matching.** Caching is strictly prefix-based. The API hashes the prompt from the beginning and matches forward. Any byte change in the prefix invalidates everything after it. Two capital letters changed in a system prompt invalidate the entire cache.

**Minimum thresholds:** 1,024 tokens for Sonnet/Haiku, 2,048 to 4,096 for Opus.

**Cache lifetime.** Default: 5 minutes of inactivity. Each cache hit resets the timer. Active sessions keep cache warm indefinitely. Extended option: 1 hour TTL at higher write cost.

## Seven Lessons from Claude Code

1. **Static content first, dynamic content last.** Order: system prompt and tools → project config → session context → conversation messages. Fragile: timestamps in system prompt, shuffling tool order, updating tool parameters all break the cache.

2. **Use messages for updates, not system prompt changes.** When information becomes stale, insert a `<system-reminder>` tag in the next user message or tool result. Model sees updated info; cached prefix stays intact.

3. **Never change models mid-session.** Prompt caches are model-specific. Switching from Opus to Haiku after 100K tokens pays full rebuild cost. Right pattern: sub-agents. Opus prepares handoff message; Haiku builds its own cache in isolated session.

4. **Never add or remove tools mid-session.** Tools are part of the cached prefix. Even if intuitive to give only needed tools, cache math makes this wrong.

5. **Plan mode as a tool.** Do not swap tool set to read-only. Use `EnterPlanMode` and `ExitPlanMode` as tools themselves. When toggled, agent gets system message explaining mode change. Tool definitions never change. Bonus: model can autonomously enter plan mode when it detects a hard problem.

6. **Tool search: defer instead of remove.** With dozens of MCP tools, sending all full schemas is expensive. Removing them breaks cache. Solution: `defer_loading`. Send lightweight stubs (name only with `defer_loading: true`). Full schemas load only when selected via `ToolSearch`. Cached prefix stays stable.

7. **Cache-safe compaction.** When context runs out, the naive approach (separate API call with different system prompt and no tools) gets zero cache hits. Claude Code's solution: compaction uses the exact same system prompt, user context, system context, and tool definitions as the parent conversation. Parent messages are prepended; compaction prompt appended as new user message. Nearly identical to parent's last request; cached prefix is reused.

## What We Already Get (OpenClaw)

- Static system prompt at front of prefix
- Tools defined once, stay consistent
- Conversation grows at end (new messages only uncached part)
- Compaction built into OpenClaw (safeguard mode)

## What We Are Missing

- No explicit `cacheRetention` config. OpenClaw seeds "short" (5 min) by default for API key profiles.
- No cache diagnostics. OpenClaw has full cache trace system not enabled. No visibility into cache hit rate.
- No cache-aware heartbeat timing. Docs mention 55m intervals to keep 1-hour caches warm. Our heartbeat is at 60m.
- Isolated cron sessions do not share cache. Each builds its own cache from scratch. Correct behavior, but know the cost.

## Recommendations

1. **Enable cache diagnostics.** Add `diagnostics.cacheTrace.enabled: true`. Monitor hit rate over a week.
2. **Set explicit cacheRetention.** Consider "long" with 55m heartbeat for long sessions.
3. **Context pruning.** Enable `contextPruning.mode: "cache-ttl"` for idle recovery.
4. **Monitor for cache-breaking changes.** Treat unexpected cache misses as incidents.

## The Big Insight

Prompt caching is not an optimization you bolt on. It is an architectural constraint you design around from the start. Claude Code was "built around prompt caching from day one." Every feature decision flows from treating cache coherence as a first-class concern.

The immediate action is measurement. We need to know our cache hit rate before we can optimize it. Everything else follows from data.
