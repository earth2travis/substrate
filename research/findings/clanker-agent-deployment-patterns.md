---
title: "Clanker Agent Deployment Patterns: Lessons for Agent Factories"
tags: [agent, deployment, patterns, farcaster, cost-optimization, production]
related: [[clanker-event-driven-architecture]], [[farcaster-protocol]], [[neynar-platform]], [[harness-engineering]], [[dark-factory]]
source: research/raw/clanker-agent-deployment-patterns.md
---

# Clanker Agent Deployment Patterns: Lessons for Agent Factories

## Summary

Jack Dishman's Clanker deployment patterns distilled into six actionable insights for building agent factories. The core theme: treat the social platform as ingestion layer, not runtime. Separate decision from execution. Classify cheap, escalate expensive. These patterns are proven at scale (tens of millions of requests) and directly portable to agent deployment.

## Key Claims

**Insight 1: Rules First, LLMs Second.** Routing everything through an LLM is the most expensive mistake in agent architecture. Deterministic rules should handle everything they can. LLMs fill the gaps where natural language parsing is truly necessary. Application: group chat filtering (who's talking, is it a mention, is it a known command) should be cheap checks before the model sees it.

**Insight 2: Classify Cheap, Escalate Expensive.** Use the cheapest model that can handle classification. Only requests requiring genuine reasoning reach capable models. We run Opus for everything. Sonnet or Haiku could handle classification, simple queries, and routine operations. Reserve Opus for main session and complex reasoning.

**Insight 3: Separate Decision from Execution.** Never execute actions inline. Agent decides what to do. Separate worker does it. Retry without re-deciding. Our sub-agent model already does this partially (main session decides, sub-agents execute) but we lack queuing or retry logic.

**Insight 4: Triple-Layer Idempotency.** Deduplicate at queue, execution, and database layers. We've had duplicate processing issues (heartbeat overlap, cron jobs running while main session is active). No deduplication layer exists. Any agent deployment platform needs this from day one.

**Insight 5: Social Platform as Ingestion Layer.** Clanker uses Farcaster as its ingestion surface. Users tag @clanker in a cast, the system processes and executes. The social platform is not where the agent lives. It's where events enter the system. This validates our direction for Sivart on Telegram and Farcaster integration.

**Insight 6: Dead Letter Queues as Early Warning.** DLQ patterns are the earliest signal of dependency degradation. Monitor them actively. We have no equivalent. Failed cron jobs, errored sub-agents, and broken API calls disappear into logs. No aggregation, no pattern detection.

## The Big Picture

Clanker is essentially a vending machine that reads social posts and executes financial transactions. Replace "financial transactions" with "agent deployments" and you have the Agent Factory's social interface. Same event-driven architecture, same social ingestion layer, same handler chain, same queue-based execution. Different payload.

## Connection to Agent Factories

For building agent factories:
- Agent-controlled infrastructure is a high-value target
- Skill vetting is not optional
- The human role shifts from operator to guardian
- Security transparency builds trust

## Related

- [[clanker-event-driven-architecture]] — Detailed five-layer architecture
- [[farcaster-protocol]] — Decentralized social protocol
- [[neynar-platform]] — Infrastructure provider
- [[harness-engineering]] — Methodology for agent-first development
- [[dark-factory]] — Lights-out operation
- [[the-openclaw-lesson]] — Security foundations
