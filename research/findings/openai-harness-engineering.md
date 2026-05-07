---
title: "Harness Engineering: Leveraging Codex in an Agent-First World"
tags: [finding, harness-engineering, codex, agent-first, openai, ralph-wiggum-loop]
related: [[harness-engineering]], [[dark-factory]], [[agent-native-operations]], [[agent-factory-production-system]], [[centaur-principle]]
source: research/raw/openai-harness-engineering.md
ingested: 2026-05-07
---

# Harness Engineering: Leveraging Codex in an Agent-First World

Ryan Lopopolo's account of building an internal beta with 0 lines of manually-written code, processing 1B+ tokens/day, and achieving 3.5 PRs/engineer/day throughput.

## Key Points

**The experiment.** Starting from an empty git repository in August 2025, the Frontier team built a product used by hundreds of internal users and external alpha testers. Every line of code (application logic, tests, CI, docs, observability, tooling) was written by Codex. Estimated time: 1/10th of manual development.

**Redefining the engineer's role.** The primary job is no longer writing code but designing environments, specifying intent, and building feedback loops that allow agents to do reliable work. Humans interact through prompts: describe a task, run the agent, let it open a PR. Codex reviews its own changes locally, requests additional agent reviews in the cloud, responds to feedback, and iterates in a loop until all agent reviewers are satisfied (the Ralph Wiggum Loop).

**Repository knowledge as system of record.** The "one big AGENTS.md" approach failed: context is scarce, too much guidance becomes non-guidance, monolithic manuals rot instantly, hard to verify. Instead, AGENTS.md is a table of contents. The knowledge base lives in a structured `docs/` directory. Progressive disclosure: agents start with a small entry point and are taught where to look next. Dedicated linters and CI jobs validate that the knowledge base is up to date, cross-linked, and structured correctly.

**Agent legibility as the goal.** Anything the agent can't access in-context effectively doesn't exist. Knowledge in Google Docs, chat threads, or people's heads is illegible to the system. Repository-local, versioned artifacts are all it can see. We favored dependencies that could be fully internalized. "Boring" technologies tend to be easier for agents to model due to composability, API stability, and representation in the training set.

**Enforcing architecture and taste.** Documentation alone doesn't keep an agent-generated codebase coherent. Invariants are enforced mechanically via custom linters and structural tests. Each business domain is divided into fixed layers with strictly validated dependency directions. Agents are most effective in environments with strict boundaries and predictable structure.

**Application legibility.** Codex drives the app with Chrome DevTools MCP: snapshots state before and after triggering UI paths, observes runtime events, applies fixes, restarts, and loops until clean. Observability tooling (logs, metrics, traces) is exposed via a local ephemeral stack per worktree. Agents query logs with LogQL and metrics with PromQL. Single Codex runs work on a single task for upwards of six hours (often while humans sleep).

## Relevance

This is the canonical account of harness engineering. Every principle (AGENTS.md as TOC, repository as system of record, agent legibility, mechanical enforcement, application legibility) is directly applicable to the Agent Factory.

## Related

- [[harness-engineering]] -- Core research area
- [[dark-factory]] -- Lights-out manufacturing as metaphor
- [[agent-native-operations]] -- Tools for the AI-human partnership
- [[agent-factory-production-system]] -- Factory as product
- [[centaur-principle]] -- Process as differentiator
