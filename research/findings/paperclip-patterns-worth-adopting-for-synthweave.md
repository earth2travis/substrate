---
title: "Paperclip Patterns Worth Adopting for Synthweave"
tags: [patterns, agent-ops, paperclip, synthweave, orchestration]
related: [[workflows-landscape]], [[agent-native-operations]], [[dark-factory]], [[harness-engineering]]
source: research/raw/paperclip-patterns-worth-adopting-for-synthweave.md
---

# Paperclip Patterns Worth Adopting for Synthweave

## Summary

Paperclip is an operating system for autonomous agent companies. From analysis of its architecture, five patterns are worth adopting for Synthweave and three should be skipped.

Worth adopting: (1) Atomic task checkout prevents double work in parallel sub-agent runs through explicit task claiming at the infrastructure level. (2) Budget/cost tracking per agent, per task, per model, surfacing operational costs that are currently invisible. (3) Heartbeat formalization with status, timing, errors, and context snapshots enables stuck-run detection. (4) Activity logging as an immutable audit log of all mutations, stronger than our memory files. (5) Agent adapter pattern for Loom orchestrating multiple agent runtimes via a type-to-spawn registry.

Skip: corporate hierarchy metaphor (unnecessary for a single creative partnership), approval gates (trust-based model is better for human-agent partnership), multi-company isolation (overkill), and task-only communication (conversational model is richer).
