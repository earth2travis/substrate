---
title: "Context Evaluation Engine Specification"
date: 2026-04-22
status: "review"
version: "1.1"
---

# Context Evaluation Engine Specification (`_eval.py`)

## Purpose

The Context Evaluation Engine is the **system health test**. It verifies that the Substrate actually works as a knowledge system -- not whether content exists, but whether agents can derive correct, synthesized answers from it.

## Evals vs. Queries

| | Evals | Queries |
|---|---|---|
| **Audience** | System maintainers testing the Substrate | Agents and humans using the Substrate |
| **Purpose** | Verify the Substrate is working correctly | Retrieve knowledge for current work |
| **Ground truth** | Yes -- pre-written authoritative answers | No -- answers come from the Substrate |
| **Output** | Scored report saved to `evals/` | Answer returned to caller in real-time |
| **Frequency** | Scheduled (weekly cron) | Ad-hoc, on-demand |
| **Scoring** | Scored 0-100 via SAS metric | Not scored |

Evals are how you **test** the Substrate. Queries are how you **use** it.

## Architecture

### A. The Input: Ground Truth Questions

Ground truth questions and answers live in `research/queries/` alongside query definitions, distinguished by the `eval: true` frontmatter flag.

Each eval question has:

```markdown
---
title: "Question description"
category: identity|state|conflict|synthesis
created: YYYY-MM-DD
eval: true
last_run: YYYY-MM-DD
score: null
---

# Eval: Title

## Question
The question being asked.

## Ground Truth
The authoritative answer, written by a human. This is the standard the Substrate
is tested against. Must be specific enough to verify correctness.

## Expected Citations
Which files or sources a correct answer should reference:
- research/raw/authentic-source.md
- insights/concepts/key-concept.md
```

Categories:

- **identity** — Who does what? What is X? Tests entity and concept knowledge.
- **state** — What are we working on now? What decisions exist? Tests temporal awareness of current organizational state.
- **conflict** — Which source wins when data disagrees? Tests provenance handling.
- **synthesis** — How do X and Y connect? Tests cross-domain reasoning.

### B. The Engine: `_eval.py`

A Python script located in `scripts/_eval.py`. Execution steps:

1. **Load:** Find all eval questions (`eval: true`) in `research/queries/`.
2. **Expand:** Load `insights/entities/entity-map.json` and expand entity aliases in the eval questions.
3. **Query:** For each question, construct a prompt that forces the engine to answer using only Substrate files, expanded across all known aliases.
4. **Synthesize:** Generate an answer via the Substrate's knowledge retrieval.
   - Phase 1 (local): Read files directly from the repo. Use a local LLM call.
   - Phase 2 (cloud): Integrate with the AI Gateway + Workers ("the Brain") for consistent model usage and context window management.
5. **Cite:** Force the engine to list every source file used in its answer.
6. **Compare:** Score the generated answer against the human-written ground truth.
7. **Report:** Write the full eval report to `evals/YYYY-MM-DD-eval.md`.

### C. The Output: Evaluation Reports

Reports are stored in `evals/YYYY-MM-DD-eval.md` (no subdirectory). Each report includes:

- **Synthesis Accuracy Score (SAS):** 0-100% aggregate score
- **Per-question breakdown:** Score, pass/fail, citations used vs. expected
- **Provenance Check:** Did the engine cite the correct source of truth?
- **Gap Analysis:** Specific areas where the Substrate failed to provide context

## The Metric: Synthesis Accuracy Score (SAS)

The SAS is calculated based on four pillars:

| Pillar | Weight | Tests |
|---|---|---|
| **Factual Correctness** | 40% | Is the answer right compared to ground truth? |
| **Conflict Resolution** | 30% | When sources disagree, did it pick the authoritative one? |
| **Entity Unification** | 20% | Did it recognize equivalent entities? (e.g., "Ansible" = "Substrate") |
| **Provenance** | 10% | Did it cite the correct source files? |

## Implementation Plan

### Phase 1: Local Baseline

- Write local `_eval.py` using direct filesystem reads and local LLM calls
- Define ground truth questions with human answers in `research/queries/`
- Test manually to validate the SAS scoring logic

### Phase 2: Automation

- Wire `_eval.py` into the cron schedule (weekly Sunday 04:00 UTC)
- Generate timestamped reports to `evals/`
- Feed gap analysis into weekly retrospectives

### Phase 3: Cloud Integration

- Deploy the "Brain" (AI Gateway + Cloudflare Workers inference layer)
- Integrate `_eval.py` with the Gateway for consistent model usage
- Add context window management and multi-model comparison

## Usage

```bash
python3 scripts/_eval.py                          # Run all evals
python3 scripts/_eval.py --category identity      # Run specific category
python3 scripts/_eval.py --single filename.md     # Run one eval question
python3 scripts/_eval.py --dry-run               # Preview without saving
python3 scripts/_eval.py --format json            # Machine-readable output
```

## Integration

Eval runs:

1. Weekly via cron (Sunday 04:00 UTC)
2. On demand by Travis or agents after major system changes
3. Results feed into the weekly retrospective gap analysis

## Skill Contract Testing

Eval tests skill stability when the SEPL Loop proposes improvements. For skills with `contract.md`, the eval engine:

1. Loads the skill's `contract.md` (inputs, outputs, failure modes)
2. Runs the skill through its test cases from `skills/<name>/tests/` if they exist
3. Compares pre-improvement and post-improvement behavior
4. Validates that the improvement didn't break the contract

Only skills with `evolvable: true` are auto-tested. All improvements require a PR regardless.
