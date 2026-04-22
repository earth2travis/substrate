---
title: "Factory Architecture: Cloudflare-First Stack"
date: 2026-04-22
status: "draft"
version: "1.0"
---

# Factory Architecture: Cloudflare-First Stack

## 1. Overview
The Agent Factory is built on a **Cloudflare-First** architecture. This stack provides the reliability, global distribution, and "serverless" simplicity required for a 24/7 autonomous partnership. It decouples the **Substrate** (the knowledge) from the **Engine** (the processing) and the **Interface** (the human control).

## 2. The Four Pillars

### A. The Memory: Cloudflare Artifacts (Git for Agents)
**Role:** The persistent, versioned storage for the Substrate.
*   **Why:** Artifacts provides "Git for Agents." It allows us to fork, branch, and merge agent states just like code.
*   **Implementation:** The Substrate repo is hosted as an Artifact. Agents `git pull` to gain "tenure" and `git push` to commit their work.
*   **Benefit:** Atomic, forkable context. An agent can test a new "personality" or "skill" in a forked branch without affecting the main Substrate.

### B. The Engine: Cloudflare Workers + AI Gateway
**Role:** The execution layer for the Autogenesis Protocol (AGP).
*   **Workers:** Lightweight, globally distributed functions that run the "Synthesis Loop" (Reflect, Propose, Validate, Commit).
*   **AI Gateway:** The inference cortex. It provides a unified API for multiple models (Anthropic, OpenAI, etc.) with built-in caching, rate-limiting, and observability.
*   **Benefit:** Model-agnostic inference. We can swap the "brain" (model) without changing the "body" (code).

### C. The Transport: Cloudflare Email Service
**Role:** The asynchronous "bus" for agent-to-agent handoffs.
*   **Why:** Email is the most robust, universal, and asynchronous protocol available. It decouples agents from real-time chat constraints.
*   **Implementation:** Specialized `@substrate.wtf` addresses for each agent (e.g., `koda@`, `sivart@`).
*   **Benefit:** Robust, auditable, and private agent communication that doesn't rely on ephemeral chat logs.

### D. The Interface: GitHub
**Role:** The human control plane.
*   **Why:** Humans understand Issues and Pull Requests. GitHub provides the UI for intent (Issues) and deliverables (PRs).
*   **Implementation:** Agents monitor the repo for "Signals" (new issues, comments) and respond with "Actions" (commits, PRs).
*   **Benefit:** A familiar, high-trust interface for the human operator.

## 3. Integration with The Substrate
The **Substrate** (`specs/the-substrate-spec.md`) defines the *content* and *structure* of our knowledge. The **Factory Architecture** defines the *infrastructure* that hosts and evolves that knowledge.

*   **The Substrate** is the "What" (The Knowledge Graph).
*   **The Factory** is the "How" (The Cloudflare Stack).

## 4. Future Components
*   **Durable Objects:** For maintaining long-lived agent "Souls" or stateful sessions that exceed the lifespan of a single Worker invocation.
*   **Vectorize:** For high-dimensional semantic search across the Substrate once the file-count exceeds the limits of simple text-based retrieval.

## 5. Related
*   [[the-substrate-spec]]
*   [[autogenesis-protocol]]
*   [[context-eval-engine]]