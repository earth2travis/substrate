---
title: "Factory Architecture: Cloudflare-First Specification"
tags: [cloudflare, architecture, agents, factory, infrastructure, specification]
related: [[harness-engineering]], [[dark-factory]], [[lean-software-delivery]]
source: research/raw/factory-architecture-cloudflare.md
---

# Factory Architecture: Cloudflare-First Specification

## Summary

A draft specification for The Agent Factory: a distributed, asynchronous, versioned intelligence system using Cloudflare's developer platform as the substrate for agent operations.

## Key Claims

1. **GitHub is the UI:** Human operator interacts exclusively through GitHub (Issues, PRs, Projects). Issues are intent; PRs are deliverables; Projects provide roadmap context.
2. **Email is the Bus:** Agents use Cloudflare Email Service for robust, authenticated, asynchronous handoffs with guaranteed delivery.
3. **Artifacts are the Memory:** Git-compatible versioned storage (Cloudflare Artifacts) stores shared knowledge with forkable state and full audit trails.
4. **Workers are the Alchemists:** Logic and transformation run in Cloudflare Workers, orchestrated by the Agents SDK.
5. **Zero-Secrets Architecture:** Workers Bindings eliminate exposed API keys. Unified billing tracks all AI spend in one place.

## Pipeline Architecture

- **Ingest Pipeline:** GitHub Issue -> Worker webhook -> Durable Object Task -> Email to agent
- **Execution Pipeline:** Agent receives email -> forks Substrate in Artifacts -> performs work -> emails for help if needed -> commits and opens PR
- **Review Pipeline:** Automated linting -> Human review -> Merge -> Worker updates Substrate -> Telegram summary

## Implications

This specification articulates the Cloudflare-native vision for agent factories. It unifies GitHub (control plane), Email (transport), Artifacts (memory), and Workers (compute) into a coherent operational architecture.

## Related

- [[harness-engineering]] -- Methodology for agent-first development
- [[dark-factory]] -- Lights-out autonomous operation
- [[lean-software-delivery]] -- Cost and flow discipline
- [[cloudflare-ai-platform-inference-layer]] -- Unified inference layer
- [[cloudflare-email-service-for-agents]] -- Email transport layer
