---
title: "Prompt Caching: Deep Research"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/prompt-caching.md
---

# Prompt Caching: Deep Research

**Date:** 2026-03-01
**Trigger:** Thariq (@trq212) thread "Lessons from Building Claude Code: Prompt Caching Is Everything"
**Sources:** Anthropic API docs, Claude Code Camp experiments, OpenClaw docs, community discussion

## What Prompt Caching Actually Is

Not what most people think. It does not cache responses. It caches the intermediate computation (KV cache: Key and Value matrices from the attention layers) that the model builds while reading your prompt. When the next request shares the same prefix, the model skips recomputing those tokens and picks up where it left off.

The KV cache for a 100K token prompt on Opus is estimated at 500MB to 1GB of GPU VRAM. That's what Anthropic stores and retrieves per request.

### Economics

Cache reads cost 10% of base input price. Cache writes cost 125% (5 min TTL) or 200% (1 hour TTL). For Opus 4.6:

| Operation | Cost per MTok |
|---|---|
| Base input | $5.00 |
| 5 min cache write | $6.25 |
| 1 hour cache write | $10.00 |
| Cache read | $0.50 |

A 100K token session at 90% cache hit rate: ~$19 vs ~$100 without caching. This is why Claude Code Pro at $20/month is viable.

### Prefix Matching

Caching is strictly prefix-based. The API hashes your prompt from the beginning and matches forward. If any byte changes anywhere in the prefix, everything after it is invalidated. Two capital letters changed in a system prompt will invalidate the entire cache.

Minimum token thresholds: 1,024 for Sonnet/Haiku, 2,048 to 4,096 for Opus.

### Cache Lifetime (TTL)

Default: 5 minutes of inactivity. Each cache hit resets the timer. An active session keeps cache warm indefinitely. Stop typing for 5 minutes and the cache evaporates.

Extended option: 1 hour TTL at higher write cost.

## Seven Lessons from Claude Code (Thariq's Thread)

### 1. Static Content First, Dynamic Content Last

The prompt ordering that maximizes cache hits:

1. **Static system prompt and tools** (globally cached across all sessions)
2. **CLAUDE.md / project config** (cached within a project)
3. **Session context** (cached within a session)
4. **Conversation messages** (grows each turn, only new messages are uncached)

This is surprisingly fragile. Things that have broken the ordering at Anthropic:
- Putting a detailed timestamp in the static system prompt
- Shuffling tool definition order non-deterministically
- Updating tool parameters (e.g., which sub-agents the AgentTool can call)

### 2. Use Messages for Updates, Not System Prompt Changes

When information becomes stale (time of day, file changes), do not update the system prompt. That invalidates the cache.

Instead, insert a `<system-reminder>` tag in the next user message or tool result. The model sees the updated info, but the cached system prompt prefix stays intact.

### 3. Never Change Models Mid-Session

Prompt caches are model-specific. If you're 100K tokens into an Opus conversation and want Haiku to answer a simple question, you pay the full 100K input cost to rebuild Haiku's cache. It's cheaper to let Opus answer.

The right pattern for model switching: **sub-agents**. Opus prepares a handoff message with the relevant context, sends it to Haiku in an isolated session. Haiku builds its own smaller cache. This is how Claude Code's Explore agents work.

**OpenClaw implication:** Our isolated cron jobs (which we just set up) naturally follow this pattern. Each isolated session builds its own minimal cache instead of contaminating the main session's prefix.

### 4. Never Add or Remove Tools Mid-Session

Tools are part of the cached prefix. Adding or removing a tool invalidates the entire cache. Even if it seems intuitive to only give the model tools it needs right now, the cache math makes this wrong.

### 5. Plan Mode: Design Around the Cache

The naive approach to plan mode: swap tool set to read-only tools. This breaks the cache.

Claude Code's approach: keep ALL tools in every request. Use `EnterPlanMode` and `ExitPlanMode` as tools themselves. When plan mode is toggled, the agent gets a system message explaining the mode change. Tool definitions never change.

Bonus: because `EnterPlanMode` is a tool the model can call, it can autonomously enter plan mode when it detects a hard problem.

### 6. Tool Search: Defer Instead of Remove

With dozens of MCP tools, including all full schemas in every request is expensive. But removing them breaks the cache.

Solution: `defer_loading`. Send lightweight stubs (just tool name with `defer_loading: true`) that the model can discover via a `ToolSearch` tool. Full schemas load only when selected. The cached prefix stays stable because the same stubs are always present in the same order.

### 7. Cache-Safe Compaction (Forking)

When context runs out, you need to summarize and continue. The naive approach: separate API call with different system prompt and no tools. This gets zero cache hits on the parent conversation. You pay full input price for 100K+ tokens.

Claude Code's solution: compaction uses the **exact same** system prompt, user context, system context, and tool definitions as the parent conversation. The parent's messages are prepended, and the compaction prompt is appended as a new user message. From the API's perspective, the request is nearly identical to the parent's last request, so the cached prefix is reused.

This requires maintaining a "compaction buffer" (room in the context window for the compact message and output). Anthropic has since built compaction directly into the API based on these learnings.

## Relevance to Our Setup (OpenClaw + Sivart)

### What We Already Get

OpenClaw handles the basic caching architecture:
- System prompt is static and at the front of the prefix
- Tools are defined once and stay consistent
- Conversation grows at the end (new messages are the only uncached part)
- Compaction is built into OpenClaw (safeguard mode)

### What We're Missing

**No explicit cacheRetention config.** Our `openclaw.json` has no cache settings. OpenClaw seeds `cacheRetention: "short"` for Anthropic API key profiles by default, so we're probably getting 5-min caching. But we're not configuring it explicitly.

**No cache diagnostics.** OpenClaw has a full cache trace system (`diagnostics.cacheTrace`) that we haven't enabled. We have no visibility into our cache hit rate. Thariq says Claude Code "runs alerts on prompt cache hit rate and declares SEVs if they're too low." We don't even measure ours.

**No cache-aware heartbeat timing.** OpenClaw docs mention using heartbeat at 55m intervals to keep 1-hour caches warm. Our heartbeat is at 60m. If we switched to `cacheRetention: "long"`, a 55m heartbeat would keep the cache alive between turns.

**Isolated cron sessions don't share cache.** Each isolated cron job builds its own cache from scratch. This is correct behavior (they're separate sessions), but worth noting that our new cron architecture trades cache efficiency for context isolation. The right tradeoff, but know the cost.

### Potential Optimizations

1. **Enable cache diagnostics.** Add `diagnostics.cacheTrace.enabled: true` to config. Monitor cache hit rate over a week. This is the first step, you can't optimize what you don't measure.

2. **Set explicit cacheRetention.** If we're on API key auth (which we are), consider `cacheRetention: "long"` with heartbeat at 55m to keep cache warm. The 1-hour TTL costs more per write but pays off in long sessions.

3. **Context pruning.** Enable `contextPruning.mode: "cache-ttl"` to prevent post-idle requests from re-caching oversized history.

4. **Monitor for cache-breaking changes.** Treat unexpected cache misses as incidents. Any change to system prompt, tools, or workspace files that OpenClaw injects can invalidate the cache.

### What We Don't Need to Worry About

- **Model switching mid-session:** We don't do this. Main session is Opus, cron jobs are isolated.
- **Tool changes mid-session:** OpenClaw handles tool definitions stably.
- **System prompt volatility:** Our SOUL.md, AGENTS.md, etc. are injected once and rarely change mid-session.

## The Big Insight

Prompt caching isn't an optimization you bolt on. It's an architectural constraint you design around from the start. Claude Code was "built around prompt caching from day one." Every feature decision (plan mode as a tool, deferred loading, cache-safe compaction) flows from treating cache coherence as a first-class concern.

For us, the immediate action is measurement. We need to know our cache hit rate before we can optimize it. Everything else follows from data.

## Action Items

- [ ] Enable cache diagnostics in OpenClaw config
- [ ] Set explicit `cacheRetention` policy
- [ ] Monitor cache hit rate for one week
- [ ] Evaluate `cacheRetention: "long"` + 55m heartbeat pattern
- [ ] Add cache hit rate to our monitoring/incident detection
- [ ] Consider `contextPruning.mode: "cache-ttl"` for idle recovery
