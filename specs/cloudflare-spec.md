---
title: "Cloud Architecture"
date: 2026-04-22
status: "draft"
version: "1.0"
---

# Cloudflare-First Stack

## 1. Overview

The Agent Factory is built on a **Cloudflare-First** architecture. This stack provides the reliability, global distribution, and "serverless" simplicity required for a 24/7 autonomous partnership. It decouples the **Substrate** (the knowledge) from the **Engine** (the processing) and the **Interface** (the human control).

## 2. The Four Pillars

### A. The Memory: Cloudflare Artifacts (Git for Agents)

**Role:** The persistent, versioned storage for the Substrate.

* **Why:** Artifacts provides "Git for Agents." It allows us to fork, branch, and merge agent states just like code.
* **Implementation:** The Substrate repo is hosted as an Artifact. Agents `git pull` to gain "tenure" and `git push` to commit their work.
* **Benefit:** Atomic, forkable context. An agent can test a new "personality" or "skill" in a forked branch without affecting the main Substrate.

### B. The Engine: Cloudflare Workers + AI Gateway

**Role:** The execution layer for the Autogenesis Protocol (AGP).

* **Workers:** Lightweight, globally distributed functions that run the "Synthesis Loop" (Reflect, Propose, Validate, Commit).
* **AI Gateway:** The inference cortex. It provides a unified API for multiple models (Anthropic, OpenAI, etc.) with built-in caching, rate-limiting, and observability.
* **Benefit:** Model-agnostic inference. We can swap the "brain" (model) without changing the "body" (code).

### C. The Transport: Cloudflare Email Service

**Role:** The asynchronous "bus" for agent-to-agent handoffs.

* **Why:** Email is the most robust, universal, and asynchronous protocol available. It decouples agents from real-time chat constraints.
* **Implementation:** Specialized `@substrate.wtf` addresses for each agent (e.g., `koda@`, `sivart@`).
* **Benefit:** Robust, auditable, and private agent communication that doesn't rely on ephemeral chat logs.

### D. The Interface: GitHub

**Role:** The human control plane.

* **Why:** Humans understand Issues and Pull Requests. GitHub provides the UI for intent (Issues) and deliverables (PRs).
* **Implementation:** Agents monitor the repo for "Signals" (new issues, comments) and respond with "Actions" (commits, PRs).
* **Benefit:** A familiar, high-trust interface for the human operator.

### E. The Scheduler: Cloudflare Cron Triggers

**Role:** The heartbeat of the Continuous Improvement Loop.

* **Why:** The Substrate requires reliable, automated execution of `_ingest.py`, `_lint.py`, `_eval.py`, and `_retro.sh` (Section 3.7 of `substrate-spec.md`).
* **Implementation:** Cloudflare Cron Triggers invoke specific Workers on a schedule (Daily 02:00-03:00 UTC, Sunday 04:00-05:00 UTC).
* **Benefit:** Serverless, reliable automation that ensures the "Company Brain" is always processing new signals.

### F. The Entity Resolution Service

**Role:** The "Identity Unification" layer.

* **Why:** To support Section 5.4 of `substrate-spec.md`, the system must resolve aliases (e.g., "Ξ2T" = "earth2travis") across all tools.
* **Implementation:** Cloudflare Workers load `insights/entities/entity-map.json` at runtime to perform "Alias Expansion" during Ingest and Query phases.
* **Benefit:** Comprehensive retrieval. Agents find all relevant information regardless of which alias was used in the source.

## 3. Integration with The Substrate

The **Substrate** (`specs/the-substrate-spec.md`) defines the *content* and *structure* of our knowledge. The **Factory Architecture** defines the *infrastructure* that hosts and evolves that knowledge.

* **The Substrate** is the "What" (The Knowledge Graph).
* **The Factory** is the "How" (The Cloudflare Stack).

## 4. Implementation Phases

* **Phase 1:** GitHub-only (Current state). Manual commits and PRs.
* **Phase 2:** Cloudflare Workers for Ingest/Lint. Automating the daily pipeline.
* **Phase 3:** Cloudflare Email Service for the Agent Bus. Enabling asynchronous, robust agent-to-agent handoffs.
* **Phase 4:** Cloudflare Artifacts for "Git for Agents" memory. Moving from standard GitHub to forkable, versioned agent states.

## 5. Future Components

* **Durable Objects:** For maintaining long-lived agent "Souls" or stateful sessions that exceed the lifespan of a single Worker invocation.
* **Vectorize:** For high-dimensional semantic search across the Substrate once the file-count exceeds the limits of simple text-based retrieval.

## 5. Related

* [[substrate-spec]]
* [[ingest-spec]]
* [[eval-spec]]
