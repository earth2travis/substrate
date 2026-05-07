---
title: Proof of Work
tags:
- agents
- verification
- quality
- automation
- harness
related:
- agent-native-operations
- harness-engineering
- browser-verification
- agent-orchestrator-pattern
- reference-free-evaluation
---



# Proof of Work

When an agent opens a PR without human review, it must prove its own work is correct through automated means. The proof of work concept structures this verification into a protocol the agent follows before landing changes.

## The Verification Stack

Proof of work is not one check. It is a layered verification protocol:

1. **Static checks**: Lint, type check, format. Fast, deterministic, zero false positives.
2. **Unit tests**: Run the test suite. Verify nothing is broken.
3. **Integration tests**: Verify the change works in context with the rest of the system.
4. **Regression checks**: Verify the change does not break anything that was working before.
5. **Complexity analysis**: Did the agent add unnecessary complexity? Measure cyclomatic complexity, duplication, coupling.
6. **Evidence capture**: Screenshots, test output, walkthrough videos. Artifacts a human can review asynchronously.

## Why It Matters

Without proof of work, autonomous agents generate work that humans must review mechanically. This defeats the purpose of autonomy. The goal is not to eliminate human review. It is to shift human review from "did you run the tests?" to "is this the right approach?"

Proof of work makes the agent trustworthy for mechanical correctness. Human review then focuses on architectural judgment, not syntax.

## Harness Engineering Connection

The harness engineering blog post makes this explicit: "Humans steer. Agents execute." Three engineers driving 1500 PRs in five months. The human role is designing feedback loops, encoding taste into linters, building the scaffolding that enables agent autonomy.

The harness is the proof of work. It is the infrastructure that makes autonomous agents reliable.
