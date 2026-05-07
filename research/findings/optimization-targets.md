---
title: "Optimization Targets for Agent Self-Evolution"
tags: [agents, optimization, evaluation, self-improvement, metrics]
related:
  - [[harness-engineering]]
  - [[proof-of-work]]
  - [[reference-free-evaluation]]
  - [[agent-native-operations]]
  - [[skills-as-portable-knowledge]]
source: research/raw/optimization-targets.md
---

# Optimization Targets for Agent Self-Evolution

**Issue:** #443
**Filed:** 2026-03-25
**Purpose:** Identify which artifacts in the agent stack are most amenable to evolutionary improvement, ranked by measurability, frequency, and impact.

## Artifact Inventory

**Skills (16 total):** web-search, stitch-prompt, github-issues, skill-optimizer, github-projects, adr, conventional-commit, memory-merger, evm-wallet, content-ingestion, agent-soul-design, openclaw-stability, calendar, cognitive-modes, lesson-extraction, product-verification.

**Core Config Files:** AGENTS.md (511 lines, critical), SOUL.md (119 lines, critical), TOOLS.md (380 lines, high), MEMORY.md (83 lines, high), GOALS.md (~120 lines, high).

**Cron Jobs (22 total):** Monitoring (6), Audits (5), Reporting (2), Memory/reflection (4), Maintenance (3), Work execution (1), One-shot reminders (1).

**Scripts (14 total):** gmail-processor.js, calendar-intelligence.js, calendar-manager.js, session-gap-analyzer.js, lesson-extractor.js, check-pr-ci.js, check-orphan-issues.js, git-preflight.sh, and 6 others.

## Ranking: Optimization Priority

Scored on measurability, frequency, and impact (1-5 each):

### Tier 1: High Priority (Score 12-15)

| Artifact | Measurability | Frequency | Impact | Total | Why |
|----------|-------------|-----------|--------|-------|-----|
| conventional-commit skill | 5 | 5 | 3 | 13 | Every commit. Format is binary pass/fail. |
| github-issues skill | 4 | 5 | 4 | 13 | Daily use. Label accuracy, project assignment measurable. |
| cron job prompts | 4 | 5 | 4 | 13 | Run 20+ times daily. Output quality directly measurable. |
| web-search skill | 4 | 4 | 4 | 12 | Search result relevance and source quality measurable. |
| gmail-processor.js | 5 | 4 | 3 | 12 | Triage accuracy directly testable. |

### Tier 2: Medium Priority (Score 9-11)

stitch-prompt skill (11), github-projects skill (11), AGENTS.md process rules (11), lesson-extraction skill (10), content-ingestion skill (10), calendar-intelligence.js (10), memory-merger skill (10).

### Tier 3: Lower Priority (Score ≤8)

SOUL.md (11* but unmeasurable), cognitive-modes skill (7), agent-soul-design skill (4), evm-wallet skill (7), adr skill (6).

## Recommended Optimization Phases

**Phase 1: Skill Optimization (weeks 1-4).** Target: conventional-commit skill and github-issues skill. Highest testability, highest frequency, clear metrics.

**Phase 2: Cron Prompt Optimization (weeks 5-8).** Target: monitoring cron prompts. Measure output format compliance, token usage, false positive rate, actionable finding rate.

**Phase 3: Script Optimization (weeks 9-12).** Target: gmail-processor.js triage logic. Classification task with clear ground truth.

## Prerequisites

Before any optimization:
1. Evaluation dataset: 50+ examples per artifact
2. Scoring function: defined metric per artifact
3. Baseline measurement: run current artifact on eval set
4. Safety gate: optimized version passes all existing tests
5. Human review: all optimized artifacts go through PR review

## Relationship to Other Work

- Issue #444 (Evaluation infrastructure): Builds the eval harness needed
- Issue #445 (Execution traces): Provides data for reflective optimization
- Issue #447 (Agent Factory hooks): Template integration for optimization pipeline
- Hermes research on self-evolution: Framework and theory basis
