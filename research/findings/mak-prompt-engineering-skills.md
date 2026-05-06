---
title: "Mak's Prompt Engineering Skills: Composable Skill Pipeline"
tags: [skills, prompt-engineering, composability, testing, cost-optimization]
related: [[skills-landscape]], [[our-skills-audit]], [[tools-landscape]], [[agent-native-operations]]
source: research/raw/mak-prompt-engineering-skills.md
---

# Mak's Prompt Engineering Skills: Composable Skill Pipeline

## Summary

Mak (Synthweave team) created three composable Claude Code skills: prompt-creator (builds and optimizes system prompts), prompt-tester (tests for weaknesses, edge cases, adversarial inputs), and model-benchmarker (compares models on cost, quality, capability). The individual skills are less important than the pipeline they form.

The composable pipeline: Create → Test → Fix → Re-test → Benchmark → Ship. This is a self-improving loop where each skill's output feeds the next skill's input. prompt-creator builds a prompt; prompt-tester finds weaknesses; prompt-creator fixes based on test results; prompt-tester re-tests and compares before/after; model-benchmarker finds the cheapest model that passes quality threshold.

Seven best practices extracted: skills should be composable not monolithic (explicit input/output contracts); improvement mode is first-class (handle both creation and iteration); testing before shipping is non-negotiable; cost-aware model selection (cheapest that meets threshold); leaderboard-driven decisions (external data informs workflow); structured output awareness (skip format instructions when API enforces schema); user input templates (guide humans to give good input, not just process AI output).
