# Insights: Clanker Agent Deployment Patterns

**Source:** `research/agents/clanker-event-driven-architecture.md`
**Origin:** Jack Dishman (Clanker founder), April 2026
**Relevance:** Direct inspiration for how we deploy agents via social platforms

---

## Insight 1: Rules First, LLMs Second

The most expensive mistake in agent architecture is routing everything through an LLM. Deterministic rules should handle everything they can. LLMs fill the gaps where natural language parsing is truly necessary.

**Application to us:** Our agents (Sivart, Koda, Ops) process every message through the full model. We have no handler chain, no deterministic pre-filtering. OpenClaw's heartbeat and cron systems handle some routing, but incoming messages all hit the primary model. As volume grows, this becomes a cost and latency problem.

**Action:** Evaluate where deterministic routing could replace model calls. Group chat filtering (who's talking, is it a mention, is it a known command) should be cheap checks before the model sees it.

---

## Insight 2: Classify Cheap, Escalate Expensive

Use the cheapest model that can handle classification. Only requests requiring genuine reasoning reach capable models.

**Application to us:** We run Opus for everything. Sonnet or Haiku could handle classification, simple queries, and routine operations. The tiered model approach Dishman describes maps to what OpenClaw already supports (model routing per agent/context), but we haven't configured it.

**Action:** Consider Sonnet for Ops Agent, Haiku-class for heartbeat checks and simple cron jobs. Reserve Opus for main session and complex reasoning.

---

## Insight 3: Separate Decision from Execution

Never execute actions inline. Agent decides what to do. Separate worker does it. Retry without re-deciding.

**Application to us:** Our sub-agent model already does this partially. Main session (Sivart) decides, sub-agents execute. But we don't have queuing or retry logic. If a sub-agent fails, we re-run the whole thing.

**Action:** This becomes critical when we build Loom. The orchestrator should enqueue work, not execute it. Workers retry independently.

---

## Insight 4: Triple-Layer Idempotency

Deduplicate at queue, execution, and database layers. If two workers race on the same event, the second returns the first's result.

**Application to us:** We've had duplicate processing issues (heartbeat overlap, cron jobs running while main session is active on the same task). No deduplication layer exists.

**Action:** Relevant for Agent Factory production system. Any agent deployment platform needs this from day one.

---

## Insight 5: The Social Platform as Ingestion Layer

Clanker uses Farcaster as its ingestion surface. Users tag @clanker in a cast, the system processes and executes. The social platform is not where the agent lives. It's where events enter the system.

**Application to us:** This is exactly how Sivart operates on Telegram and how we envision Farcaster integration. The social post is an event. The agent is the processing pipeline behind it. Dishman's architecture validates our direction: social platforms as ingestion adapters, not as the agent runtime.

**Action:** When building Farcaster integration (#474), model the Neynar webhook as an ingestion adapter in Dishman's five-layer pattern. Platform-specific behavior in the handler, not the LLM.

---

## Insight 6: Dead Letter Queues as Early Warning

DLQ patterns are the earliest signal of dependency degradation. Monitor them actively.

**Application to us:** We have no equivalent. Failed cron jobs, errored sub-agents, and broken API calls disappear into logs. No aggregation, no pattern detection.

**Action:** Build a failure aggregation pattern into Ops Agent. Surface recurring failures as signals, not just incidents.

---

## The Big Picture

Dishman built what is essentially a vending machine that reads social posts and executes financial transactions. Replace "financial transactions" with "agent deployments" and you have the Agent Factory's social interface. The architecture is proven at scale (tens of millions of requests). The patterns are directly portable.

The key translation: **Clanker deploys tokens. We deploy agents.** Same event-driven architecture, same social ingestion layer, same handler chain, same queue-based execution. Different payload.
