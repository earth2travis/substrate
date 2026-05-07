---
title: "Synthweave Harness Engineering Evaluation"
tags: [synthweave, harness-engineering, evaluation, agent, assessment, quality]
related:
- harness-engineering
- codex
- lean-software-delivery
- dark-factory
source: research/raw/synthweave-harness-readiness.md
---
# Synthweave Harness Engineering Evaluation

## Summary

An evaluation of Synthweave against OpenAI's harness engineering methodology across eight categories. Overall score: 3.1/5. Strong in MCP tooling and DDD structure; weak in agent-facing navigation and dependency boundary enforcement.

## Key Claims

1. **AGENTS.md as ToC (2/5):** No top-level AGENTS.md entry point. 22 context.md files exist but lack a navigation document.
2. **Repo as System of Record (3.5/5):** Good DDD structure with bounded contexts, but external context (roadmap, user research) lives outside the repo.
3. **Mechanical Enforcement (3/5):** ESLint + Prettier + pre-commit hooks present, but no dependency boundary enforcement, import cycle detection, or commit message linting.
4. **Application Legibility (4/5):** Excellent MCP tooling (22 tools), headless boot script, Docker Compose with health checks, multi-tier observability.
5. **Testing and Verification (3/5):** 153 test files but minimal E2E coverage, no visual regression, no proof-of-work capability.
6. **CI/CD Pipeline (3/5):** Build + typecheck + unit tests block PRs, but no release automation or deployment pipeline.
7. **Entropy and Quality (2.5/5):** No tech debt tracking, no quality grades, no stale documentation detection.
8. **Progressive Disclosure (3.5/5):** Good README and CLAUDE.md entry points, but no recommended reading order or dependency graph visualization.

## Top 5 Investments

1. Create AGENTS.md navigation system
2. Add dependency boundary enforcement (eslint-plugin-boundaries)
3. Implement proof-of-work capability (screenshots + test execution)
4. Create TECHNICAL_DEBT.md registry
5. Add agent-queryable CI/merge status MCP tool

## Related

- [[harness-engineering]] -- The methodology being evaluated
- [[codex]] -- Primary agent tool
- [[lean-software-delivery]] -- Quality and flow discipline
- [[dark-factory]] -- Target operational model
