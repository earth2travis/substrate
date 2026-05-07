---
title: "Spec-Driven Development"
tags: [spec-driven, development, agent, contract, harness-engineering, dark-factory]
related:
- harness-engineering
- lean-software-delivery
- dark-factory
- github-as-knowledge-graph
source: research/raw/spec-driven-development.md
---
# Spec-Driven Development

Distribution and assembly of software via specifications that coding agents can interpret and reassemble. The spec becomes the contract, and agents iteratively close the gap between spec and implementation.

## Core Loop

Spec → agent generates code → test validates → feedback refines → loop until spec matches code.

This is different from traditional requirements documents because the spec IS the executable specification — not a description but a testable contract.

## Connection to Dark Factory

In the dark factory pipeline, spec-driven development allows autonomous agents to assemble and reassemble code from specifications without human intervention. The spec is the environment design part of harness engineering.

## Key Distinctions

- Traditional: requirements describe what the software should do
- Spec-driven: the spec is a contract that can be validated automatically
- The agent doesn't just read the spec — it generates code from it, tests against it, and refines until the implementation satisfies the contract

## Related Concepts

- Harness engineering: the broader framework for environment design and autonomous code generation
- Lean software delivery: spec-driven dev eliminates handoff waste by making specs executable
- Multi-agent orchestration: agents can execute specs and coordinate around them
