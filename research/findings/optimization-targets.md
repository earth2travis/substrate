---
title: Optimization Targets for Agent Self-Evolution
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/optimization-targets.md
---

# Optimization Targets for Agent Self-Evolution

**Issue:** #443
**Filed:** 2026-03-25
**Purpose:** Identify which artifacts in our agent stack are most amenable to evolutionary improvement, ranked by measurability, frequency, and impact.

---

## 1. Artifact Inventory

### 1a. Skill Files (16 skills)

| Skill | Lines | Usage Frequency | Testable? |
|-------|-------|----------------|-----------|
| web-search | 560 | High (daily) | Yes, query quality measurable |
| stitch-prompt | 318 | Medium (sub-agent spawns) | Yes, output quality assessable |
| github-issues | 191 | High (daily) | Yes, issue quality checkable |
| skill-optimizer | 174 | Low (meta) | Partially |
| github-projects | 172 | High (daily) | Yes, project operations verifiable |
| adr | 155 | Low | Yes, decision doc quality |
| conventional-commit | 130 | High (every commit) | Yes, commit message format |
| memory-merger | 118 | Medium (cron) | Yes, merge quality assessable |
| evm-wallet | 117 | Low | Yes, transaction success |
| content-ingestion | 112 | Medium | Yes, extraction quality |
| agent-soul-design | 105 | Low (design time) | No (creative) |
| openclaw-stability | 97 | Medium (troubleshooting) | Partially |
| calendar | 80 | Medium (daily cron) | Yes, accuracy of operations |
| cognitive-modes | 77 | Low | No (behavioral) |
| lesson-extraction | 68 | Medium (daily cron) | Yes, lesson quality |
| product-verification | ? | Low | Yes |

### 1b. Core Configuration Files

| File | Lines | Impact | Testable? |
|------|-------|--------|-----------|
| AGENTS.md | 511 | Critical (governs all behavior) | Partially, via process compliance |
| SOUL.md | 119 | Critical (identity, voice) | No (subjective) |
| TOOLS.md | 380 | High (infrastructure reference) | No (reference data) |
| MEMORY.md | 83 | High (continuity) | Partially, via recall accuracy |
| GOALS.md | ~120 | High (direction) | No (strategic) |

### 1c. Cron Job Configurations (22 jobs)

| Category | Count | Testable? |
|----------|-------|-----------|
| Monitoring (email, calendar, ops) | 6 | Yes, false positive/negative rates |
| Audits (project, incident, tool) | 5 | Yes, finding accuracy |
| Reporting (daily, velocity) | 2 | Partially, completeness |
| Memory/reflection (growth, patterns, lessons) | 4 | Partially, quality subjective |
| Maintenance (export, planning) | 3 | Yes, task completion |
| Work execution (this job) | 1 | Yes, PR quality |
| One-shot reminders | 1 | N/A |

### 1d. Scripts (14 scripts)

| Script | Usage | Testable? |
|--------|-------|-----------|
| gmail-processor.js | 2x daily | Yes, triage accuracy |
| calendar-intelligence.js | 2x daily | Yes, event detection |
| calendar-manager.js | On demand | Yes, CRUD success |
| session-gap-analyzer.js | Daily | Yes, gap detection quality |
| lesson-extractor.js | Daily | Yes, extraction quality |
| check-pr-ci.js | On demand | Yes, CI status accuracy |
| check-orphan-issues.js | On demand | Yes, orphan detection |
| git-preflight.sh | Every commit | Yes, preflight accuracy |
| Others (6) | Low/sporadic | Varies |

---

## 2. Ranking: Optimization Priority

Scored on three dimensions (1-5 each):
- **Measurability:** Can we define a metric and evaluate before/after?
- **Frequency:** How often is this artifact used?
- **Impact:** How much does improvement here affect overall agent quality?

### Tier 1: High Priority (Score 12-15)

| Artifact | Measurability | Frequency | Impact | Total | Why |
|----------|-------------|-----------|--------|-------|-----|
| **conventional-commit skill** | 5 | 5 | 3 | 13 | Every commit. Format is binary pass/fail. Perfect GEPA target. |
| **github-issues skill** | 4 | 5 | 4 | 13 | Daily use. Can measure: label accuracy, project assignment, description quality. |
| **cron job prompts** | 4 | 5 | 4 | 13 | Run 20+ times daily. Output quality directly measurable. Token cost trackable. |
| **web-search skill** | 4 | 4 | 4 | 12 | Frequent use. Search result relevance and source quality measurable. |
| **gmail-processor.js** | 5 | 4 | 3 | 12 | Triage accuracy directly testable against labeled examples. |

### Tier 2: Medium Priority (Score 9-11)

| Artifact | Measurability | Frequency | Impact | Total | Why |
|----------|-------------|-----------|--------|-------|-----|
| **stitch-prompt skill** | 3 | 3 | 5 | 11 | Sub-agent quality depends on prompt quality. Hard to measure but high leverage. |
| **github-projects skill** | 4 | 4 | 3 | 11 | Project operations verifiable. |
| **lesson-extraction skill** | 4 | 3 | 3 | 10 | Daily cron. Lesson quality assessable by human review. |
| **content-ingestion skill** | 4 | 3 | 3 | 10 | Extraction quality measurable against source. |
| **AGENTS.md process rules** | 2 | 5 | 4 | 11 | Governs everything, but hard to A/B test sections. |
| **calendar-intelligence.js** | 4 | 4 | 2 | 10 | Event detection accuracy testable. Lower impact. |
| **memory-merger skill** | 3 | 3 | 4 | 10 | Memory quality is high impact but subjective to measure. |

### Tier 3: Lower Priority (Score ≤8)

| Artifact | Measurability | Frequency | Impact | Total | Why |
|----------|-------------|-----------|--------|-------|-----|
| SOUL.md | 1 | 5 | 5 | 11* | *High frequency and impact but essentially unmeasurable. Voice is subjective. |
| cognitive-modes skill | 2 | 2 | 3 | 7 | Behavioral, hard to measure. |
| agent-soul-design skill | 1 | 1 | 2 | 4 | Rarely used, creative output. |
| evm-wallet skill | 5 | 1 | 1 | 7 | Perfectly testable but rarely used. |
| adr skill | 3 | 1 | 2 | 6 | Low frequency. |

---

## 3. Independently Testable Artifacts

These artifacts can be evaluated without modifying the live agent, making them safe candidates for automated optimization:

### Fully Testable (can run evaluation offline)

1. **conventional-commit skill**: Feed commit diffs, compare generated messages against format rules. Binary pass/fail.
2. **gmail-processor.js**: Feed sample emails, check triage accuracy against labeled dataset.
3. **cron job prompts**: Run same prompt twice with variations, compare output quality and token usage.
4. **github-issues skill**: Feed task descriptions, evaluate generated issue quality (labels, project, description completeness).
5. **check-pr-ci.js / check-orphan-issues.js**: Known inputs, verifiable outputs.

### Partially Testable (requires judgment or proxy metrics)

6. **web-search skill**: Can measure source diversity, result relevance (with human labels), query reformulation quality.
7. **content-ingestion skill**: Compare extracted content against source, measure information retention.
8. **lesson-extraction skill**: Can measure lesson count, taxonomy compliance, deduplication quality.
9. **stitch-prompt skill**: Sub-agent success rate as proxy metric.

### Not Independently Testable

10. **SOUL.md**: Voice is subjective. Would need human preference ratings.
11. **AGENTS.md**: Process compliance can be measured, but isolating which section caused improvement is hard.
12. **cognitive-modes**: Behavioral shifts are hard to attribute.

---

## 4. Recommended First Optimization Targets

Based on the Hermes phased approach (start with skills, then tool descriptions, then system prompts):

### Phase 1: Skill Optimization (weeks 1-4)

**Target:** `conventional-commit` skill
**Why:** Highest testability, highest frequency, clear metrics (format compliance, message quality). Perfect first candidate for GEPA-style optimization because the evaluation function is nearly deterministic.

**Evaluation approach:**
- Collect 50 recent commit diffs from our repo
- Current skill generates messages for each
- Optimized skill generates messages for each
- Score: format compliance (binary), message clarity (1-5 human rating), information density (does it capture what changed?)

**Target:** `github-issues` skill
**Why:** High frequency, good measurability. Can evaluate label accuracy, project assignment correctness, description completeness.

### Phase 2: Cron Prompt Optimization (weeks 5-8)

**Target:** Monitoring cron prompts (email triage, calendar check, ops check)
**Why:** Run multiple times daily. Can measure: output format compliance, token usage, false positive rate, actionable finding rate.

**Evaluation approach:**
- Run same cron prompt with variations
- Compare token usage (lower is better, holding quality constant)
- Compare output compliance with standardized format
- Track false positive/negative rates over time

### Phase 3: Script Optimization (weeks 9-12)

**Target:** `gmail-processor.js` triage logic
**Why:** Classification task with clear ground truth. Can build labeled dataset from past triage results.

---

## 5. Prerequisites

Before running any optimization:

1. **Evaluation dataset**: Need 50+ examples per artifact (commit diffs, emails, task descriptions)
2. **Scoring function**: Each artifact needs a defined metric (format compliance, accuracy, token cost)
3. **Baseline measurement**: Run current artifact on eval set, record scores
4. **Safety gate**: Optimized version must pass all existing tests plus maintain semantic equivalence
5. **Human review**: All optimized artifacts go through PR review before deployment

---

## 6. Relationship to Other Issues

- **#444 (Evaluation infrastructure)**: Builds the eval harness needed for phases 1-3
- **#445 (Execution traces)**: Provides the data GEPA needs for reflective optimization
- **#447 (Agent Factory hooks)**: Template integration for optimization pipeline
- **#446 (Lesson extraction)**: Already running, could be an early optimization target
- **Hermes research** (`research/agents/hermes-self-evolution.md`): Framework and theory basis
