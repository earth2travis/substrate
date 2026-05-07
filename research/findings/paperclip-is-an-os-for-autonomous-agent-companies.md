---
title: "Paperclip: An OS for Autonomous Agent Companies"
tags: [paperclip, agents, os, company, coordination, governance]
related: [[harness-engineering]], [[dark-factory]], [[lean-software-delivery]]
source: research/raw/paperclip-is-an-os-for-autonomous-agent-companies.md
---

# Paperclip: An OS for Autonomous Agent Companies

## Summary

Paperclip is a control plane for AI agent companies. It does not build, run, or provide an agent framework. It provides organizational infrastructure: org charts, task management, budget enforcement, goal alignment, and governance for multiple simultaneous agent instances.

## Key Claims

1. **The Metaphor:** "If OpenClaw is an employee, Paperclip is the company." Provides structure, accountability, and coordination above individual agents.
2. **Problem Solved:** People running 10+ simultaneous agent sessions lose track of spend, lack audit trails, and manually coordinate context between agents.
3. **What It Is NOT:** Not an agent framework, workflow builder, chatbot, prompt manager, or single-agent tool. It is organizational infrastructure.
4. **Tech Stack:** Node.js + Express, React + Vite, PostgreSQL via Drizzle ORM, embedded PGlite for zero-config local dev. MIT licensed.
5. **Quick Start:** `npx paperclipai onboard --yes` gets a local instance running immediately.

## Implications

Paperclip represents the organizational layer that sits above harness engineering. While harness engineering optimizes the agent's environment, Paperclip optimizes the company's environment: budgets, org charts, and governance for fleets of agents. The two are complementary.

## Related

- [[harness-engineering]] -- Agent environment design
- [[dark-factory]] -- Lights-out autonomous operation
- [[lean-software-delivery]] -- Cost discipline in delivery
- [[openclaw]] -- Individual agent tool
