---
title: "Clanker: Five-Layer Event-Driven Agent Architecture"
tags: [agent, architecture, event-driven, farcaster, deployment, production]
related:
- farcaster-protocol
- neynar-platform
- harness-engineering
- dark-factory
- the-openclaw-lesson
- decentralized-social
source: research/raw/clanker-event-driven-architecture.md
---
# Clanker: Five-Layer Event-Driven Agent Architecture

## Summary

Jack Dishman's Clanker is a Farcaster-based deployment agent that processes tens of millions of API requests. Its architecture is five decoupled layers, each with clear input/output contracts: Ingestion, Decision (handler chain), Classification, Structured Output, and Queue + Workers. The core principle: deterministic rules handle everything they can; LLMs fill only the gaps where natural language parsing is truly necessary.

## Key Claims

**Rules first, LLMs second.** Using an LLM where a regex would do is like hiring a consultant to check whether a number is greater than zero. Every message runs through a handler chain: sequence of checks, first match wins. Known commands, spam patterns, rate limits all handled deterministically before any LLM call.

**Classify cheap, escalate expensive.** The cheapest classifier model handles routing. A Haiku-class call decides which tier the task belongs to. Only genuine natural language reasoning reaches capable models. Escalate explicitly, never by default.

**Separate decision from execution.** The agent decides what to do. A separate worker does it. Retry without re-deciding. Benefits: parallelism without interference, retry without re-deciding, lower cost than serverless per-millisecond billing, and visibility via queue depth dashboards.

**Triple-layer idempotency.** Deduplicate at queue, execution, and database layers. If two workers race on the same event, the second returns the first's result. Build this assumption from the start; retrofitting onto a live system is painful.

**Memory: two distinct problems.** Task state (short-term) via database rows with status fields. Knowledge (long-term) via tracking every processed event by unique message ID, per-user request counts, block lists, and behavioral state persisting across sessions.

**Platform-specific behavior in the handler, not the LLM.** The model parses intent and returns structured action. Whether to execute, how to reply, which platform behavior applies: all deterministic if-statements in the handler. Mixing behavioral policy into prompts makes it invisible, untestable, fragile.

## Five Layers

1. **Ingestion:** Push (webhooks) and pull (polling). Handler validates signature, enqueues job, returns 200. All real processing is asynchronous.
2. **Decision (Handler Chain):** Deterministic rules handle everything they can. LLMs fill the gaps.
3. **Classification:** Cheapest model handles routing. Escalate only when necessary.
4. **Structured Output:** Named functions with defined parameter schemas. Model picks which tool to call.
5. **Queue + Workers:** Never execute actions inline. Always enqueue them.

## Connection to Our Work

Clanker deploys tokens via Farcaster. We deploy agents. Same event-driven architecture, same social ingestion layer, same handler chain, same queue-based execution. Different payload. This validates our direction: social platforms as ingestion adapters, not as the agent runtime.

The architecture maps directly to Hermes Agent's cron/heartbeat model: ingestion via webhooks/heartbeat, classification via model routing, execution via sub-agents. The key gap we have: no queuing or retry layer. If a sub-agent fails, we re-run the whole thing.

## Related

- [[farcaster-protocol]] — Decentralized social protocol
- [[neynar-platform]] — Infrastructure provider for Farcaster
- [[harness-engineering]] — Agent-first development methodology
- [[dark-factory]] — Lights-out operation requiring queue-based execution
- [[the-openclaw-lesson]] — Security foundations for agent platforms
- [[telegram-group-setup]] — Telegram forum as agent ingestion layer
