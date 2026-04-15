---
title: "Clanker: Event-Driven Agent Architecture"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/clanker-event-driven-architecture.md
---

# Clanker: Event-Driven Agent Architecture

**Source:** https://x.com/JackDishman/status/2039452216730222969
**Author:** Jack Dishman (founder, Clanker)
**Context:** Farcon presentation prep. Clanker is a Farcaster deployment agent that listens to social posts and executes financial transactions (token deployments) on demand.
**Scale:** Tens of millions of API requests, hundreds of thousands of in-feed social conversations.
**Extracted:** 2026-04-02

## What Clanker Is

A deployment agent on Farcaster. Users post plain English requests on the social platform. Within three seconds, Clanker reads the post, classifies intent, validates the user, dispatches an action to a third-party API (blockchain token deployment), logs the result, and replies. Zero human involvement.

Dishman's definition of a "true agent": a program that monitors an environment, makes decisions, and takes action based on what it perceives. Not a chatbot with a personality. It watches a stream of events and continuously reacts.

## The Five-Layer Architecture

Every production agent is five decoupled layers, each with clear input/output contracts, operating independently.

### Layer 1: Ingestion

Two modes: push (webhooks) and pull (polling). Use both in practice.

**Webhooks (Push):** External service sends HTTP POST in real time. Handler should do as little as possible: validate signature, enqueue job, return 200. All real processing is asynchronous.

**Polling (Pull):** Cron job queries API periodically. Filter by timestamp, check `processed_ids` to skip duplicates. Adds latency but dead simple. Fallback when webhooks unavailable.

**Critical rule:** Always validate and enqueue in the ingestion layer. Never execute business logic there. A webhook handler that takes 500ms to respond will eventually be retried by the sender, producing duplicates.

### Layer 2: Decision (Handler Chain)

**The most important principle in the entire post: deterministic rules handle everything they can. LLMs fill the gaps where natural language parsing is truly necessary.**

Rules are fast, cheap, predictable, testable. LLMs are slow, expensive, stochastic, hard to unit-test. "Using an LLM where a regex would do is like hiring a consultant to check whether a number is greater than zero."

Every message runs through a handler chain: sequence of checks, first match wins. Known commands, spam patterns, rate limits all handled deterministically before any LLM call.

### Layer 3: Classification (Model Cost Optimization)

**Classify first, escalate only when necessary.**

Cheapest classifier model handles routing. A Haiku-class call (fraction of a cent) decides which tier the task belongs to. Deterministic rules eliminate obvious cases first. Lightweight model handles intent classification. Only genuine natural language reasoning reaches capable models.

**Trap to avoid:** Using a powerful model as your entry point "just to be safe." The entry point should be the cheapest thing that can handle classification. Escalate explicitly, never by default.

### Layer 4: Structured Output (Intent to Action)

When you use an LLM, bridge free-form text to structured actions via a typed tool system. Named functions with defined parameter schemas. Model picks which tool to call and returns structured params. API enforces valid JSON.

**Key subtlety:** Platform-specific behavior belongs in the handler, not the LLM. The model parses intent and returns structured action. Whether to execute, how to reply, which platform behavior applies: all deterministic if-statements in the handler. Mixing behavioral policy into prompts makes it invisible, untestable, fragile.

### Layer 5: Queue + Workers (Execution)

**Never execute actions inline. Always enqueue them.**

Agent decides what to do. Separate worker does it.

Benefits:
- **Parallelism without interference:** Separate queues per platform and per service. Slow external process in one queue doesn't block others.
- **Retry without re-deciding:** If action fails, retry just the action, not the perception-decision loop. LLM call already happened. Don't pay for it again.
- **Cost:** Synchronous functions in a queue on dedicated workers significantly cheaper than serverless per-millisecond billing.
- **Visibility:** Queue is a dashboard. Pending depth shows if falling behind. Retry counts show dependency degradation. Dead letter queues show permanently broken event classes.

## Memory: Two Distinct Problems

Conflating these causes bugs.

### Task State (Short-Term)

Database row with status field. Every multi-step task gets a lifecycle record: pending, processing, completed, failed. Every status transition is a log entry. Every failure is debuggable. When agent crashes at 3am, you know exactly where it was.

### Knowledge (Long-Term)

Track every processed event by unique message ID (deduplication). Track per-user request counts, block lists, trusted accounts, behavioral state persisting across sessions.

**Triple-layer idempotency:**
1. Queue (deduplication IDs)
2. Execution layer (check processed_ids before acting)
3. Database (unique constraints on result records)

If two workers race on the same event, the second returns the first's result. No duplicates, no errors.

## Production Hardening

- **Idempotency everywhere:** Events will be delivered more than once. Workers will race. Deduplicate at every layer. Build this assumption from the start; retrofitting onto a live system is painful.
- **Timeouts and staged execution:** After triggering external action, don't immediately read result. Enqueue follow-up with delay. Retry with exponential backoff. Have fallback query strategy.
- **Input sanitization:** Strip HTML/scripts from all incoming content. Null checks on every field. Common attack: sending literal string "null" to trigger unhandled edge cases. Sanitize at ingestion AND before any LLM call.
- **Dead letter queue monitoring:** DLQ only useful if watched. Alert on new entries. Daily cron to categorize failure reasons. DLQ patterns are earliest signal of dependency degradation.
- **Deployment:** Start serverless. Offload expensive/long-running compute to dedicated microservices only as needed. Core logic (ingestion, classification, decision, dispatch) scales fine serverless. Heavy workers get their own infrastructure.

## Connection to Farcaster

Clanker operates natively on Farcaster. Users tag @clanker in a cast, the agent processes the request and deploys tokens. This is the model Ξ2T flagged as inspiration for deploying agents through social platforms. The architecture handles the Farcaster-specific ingestion (Neynar webhooks for cast mentions) and translates to a platform-agnostic handler chain.
