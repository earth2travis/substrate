---
title: "Context Evaluation Engine Specification"
date: 2026-04-22
status: "draft"
version: "1.0"
---

# Context Evaluation Engine Specification

## 1. Overview
The Context Evaluation Engine is a systematic testing framework designed to measure the **Synthesized Understanding** of The Agent Factory. Unlike traditional RAG benchmarks that test simple retrieval, this engine tests the system's ability to resolve conflicts, unify entities, and maintain temporal awareness.

## 2. Architecture

### A. The Input: Ground Truth Questions
The engine uses a curated list of questions (`evals/ground-truth-questions.md`) that represent core organizational knowledge. These are categorized into:
*   **Identity & Roles:** Who does what?
*   **Current State:** What are we doing right now?
*   **Conflict Resolution:** Which source wins when data disagrees?
*   **Temporal Awareness:** What changed recently?

### B. The Engine: `_eval.py`
A Python script located in `scripts/_eval.py` that performs the following steps:
1.  **Query:** Takes a question from the Ground Truth list.
2.  **Synthesize:** Uses the Substrate's current "Brain" (AI Gateway + Workers) to generate an answer based *only* on the files in the repo.
3.  **Cite:** Requires the engine to list every file used to reach its conclusion.
4.  **Compare:** (Manual or Automated) Compares the generated answer against the "Human Baseline."

### C. The Output: Evaluation Reports
Results are stored in `evals/reports/YYYY-MM-DD-context-eval.md`. Each report includes:
*   **Synthesis Accuracy Score (SAS):** A 0-100% rating based on correctness and depth.
*   **Provenance Check:** Did the agent cite the correct "Source of Truth"?
*   **Gap Analysis:** Specific areas where the Substrate failed to provide context.

## 3. The Metric: Synthesis Accuracy Score (SAS)
The SAS is calculated based on four pillars:
1.  **Factual Correctness (40%):** Is the answer right?
2.  **Conflict Resolution (30%):** Did it pick the authoritative source?
3.  **Entity Unification (20%):** Did it recognize that "Ansible" and "Substrate" are the same thing?
4.  **Provenance (10%):** Did it show its work?

## 4. Implementation Plan

### Phase 1: The Baseline
*   Draft `evals/ground-truth-questions.md`.
*   Manually answer them to create the "Human Baseline."

### Phase 2: The Script
*   Write `scripts/_eval.py` to automate the querying of the Substrate.
*   Integrate with AI Gateway for consistent model usage.

### Phase 3: The Loop
*   Run the eval weekly.
*   Use the "Gap Analysis" to drive the **SEPL Loop** (Autogenesis Protocol) for system improvements.

## 5. Related
*   [[factory-architecture-cloudflare]]
*   [[autogenesis-protocol]]
*   [[the-substrate-spec]]