---
title: "AutoResearchClaw: Experiment-Driven Development Analysis"
tags: [autoresearchclaw, agents, research, experiment, pipeline, science]
related: [[hermes-agent]], [[harness-engineering]], [[lean-software-delivery]], [[dark-factory]]
source: research/raw/autoresearchclaw-analysis.md
---

# AutoResearchClaw: Experiment-Driven Development Analysis

## Summary

AutoResearchClaw is a fully autonomous research pipeline producing conference-ready papers via 23 stages across 8 phases. While it automates paper production with strong quality controls, it conflates output generation with genuine scientific inquiry.

## Key Claims

1. **23 Stage Pipeline:** Linear pipeline with typed stage contracts, status transitions, rollback rules, and three human-in-the-loop gates (Stages 5, 9, 20). Covers research scoping, literature discovery, synthesis, experiment design, execution, analysis, paper writing, and finalization.
2. **Real Literature:** Queries OpenAlex, Semantic Scholar, arXiv with deduplication and circuit breakers. 4-layer citation verification (arXiv ID, CrossRef DOI, Semantic Scholar title match, LLM relevance). Anti-fabrication guards.
3. **Sandbox Execution:** Subprocess with timeout (300s default), memory limits (4096MB), AST validation, forbidden pattern detection (subprocess, eval, exec), NaN/Inf fast-fail, self-healing repair loops (up to 10 iterations).
4. **PIVOT/REFINE/PROCEED Loop:** Stage 15 decides whether to continue, re-run experiments, or generate new hypotheses. Maximum 2 pivots before forced PROCEED.

## The Scientific Validity Problem

The pipeline optimizes for paper quality (length, formatting, citation integrity) rather than scientific validity. Hypotheses are formally correct but epistemically empty: the LLM generates claims it knows how to confirm. The REFINE loop optimizes metrics rather than testing falsification. Negative results trigger pivots, not findings. Peer review is methodology consistency checking, not independent expert evaluation.

## What It Actually Is

An automated academic paper mill with unusually good quality controls. Excellent at producing well-structured, properly cited, internally consistent papers. Not doing science, but doing science cosplay.

## Patterns to Extract

- **Sandbox execution pattern** (subprocess, timeout, metric parsing, NaN detection)
- **Self-healing repair loop** (error → LLM fix → re-run)
- **Stage contracts** (typed input/output per stage)
- **Evolution store** (JSONL lesson extraction with time decay)
- **Checkpoint/resume** (pipeline checkpoint after each stage)
- **Sentinel watchdog** (process monitoring for crash recovery)

## Related

- [[hermes-agent]] — Agent platform with self-evolution
- [[harness-engineering]] — Agent-first development
- [[lean-software-delivery]] — Quality gates and metrics
- [[dark-factory]] — Lights-out autonomous operation
- [[karl-popper]] — Philosophy of falsification
