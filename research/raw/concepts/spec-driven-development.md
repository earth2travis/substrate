---
title: "Spec-Driven Development"
created: 2026-04-09
updated: 2026-04-09
type: concept
tags: [development, tools]
sources: [raw/transcripts/symphony-harness-engineering-transcript-2026-04-07.md]
---

# Spec-Driven Development

Distribution and assembly of software via specifications that coding agents can interpret and reassemble. The spec becomes the contract, and agents iteratively close the gap between spec and implementation.

## Core Loop

The fundamental pattern: spec -> agent generates code -> test validates -> feedback refines -> loop until spec matches code. This is different from traditional requirements docs because the spec IS the executable specification -- not a description but a testable contract.

## Connection to Dark Factory

In Ryan Lopopolo's dark factory pipeline, spec-driven development allows autonomous agents to assemble and reassemble code from specifications without human intervention. The spec is the environment design part of harness engineering.

## Related

- [[harness-engineering]] -- Spec-driven dev is a key technique within this
- [[lean-software-development]] -- Spec-driven dev eliminates handoff waste by making specs executable
- [[symphony-orchestrator]] -- Multi-agent system that executes specs
