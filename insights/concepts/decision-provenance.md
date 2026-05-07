---
title: "Decision Provenance"
tags: [concept, provenance, decision-tracking, observability, accountability]
related: [[agent-memory]], [[context-stack]], [[agent-native-operations]], [[subagent-architecture]]
---

# Decision Provenance

The discipline and infrastructure for tracing every agent decision back to its inputs, reasoning, and alternatives considered.

## What It Is

Not logging. Not observability. Provenance: the full causal chain from input to decision to outcome, preserved in a way that survives time and can answer questions about itself.

The two questions at the heart of everything: Why did the agent decide X? What did it know at the time?

## What Must Be Captured

A decision record answers five questions:

1. **What was decided?** Identity: unique decision ID, timestamp, session context, agent identity.
2. **Why?** Reasoning: chain of thought, key factors, assumptions, confidence level.
3. **What else was considered?** Alternatives: other options, why rejected, conditions for preference.
4. **How confident was the agent?** Metadata: model version, temperature, context utilization, token counts.
5. **What happened as a result?** Outcome: action taken, observable result, human response, downstream effects.

## What Counts as a "Decision"

A decision is worth tracking when it closes off alternatives. The test: reversibility and consequence. If the action is hard to undo or has effects beyond the current turn, it's a decision.

For the Agent Factory, decisions worth tracking include: external actions (emails, commits, messages), architectural choices, information synthesis, recommendations to the human, process deviations, memory updates.

## Storage Architecture: Hybrid (Logs + Index)

Append-only markdown files in `decisions/` as source of truth. Standardized YAML frontmatter with machine-parseable fields. Generated index for fast lookup. Git history provides immutability. When outgrown, structured frontmatter makes migration to a graph database mechanical.

This is the best fit for systems that start simple and need to scale. Which is exactly our trajectory.

## Query Patterns That Matter

- **Temporal:** What decisions were made on a specific date?
- **Topical:** What decisions have we made about email handling?
- **Causal:** What led to the decision to use 1Password?
- **Counterfactual:** What would have changed if we'd known X earlier?
- **Audit:** Show me all decisions where confidence was low.
- **Pattern:** Are we making the same type of mistake repeatedly?

## Multi-Agent Provenance

Each sub-agent produces its own decision records with agent identity in metadata. The orchestrator's synthesis decision references sub-agent outputs explicitly. Delegation is an explicit relationship in the provenance graph.

## The Discipline

Decision provenance is not a feature you add. It's a discipline you practice. The infrastructure supports the discipline, but the discipline comes first. We already make decisions worth tracking. Now we make the tracking worth the decisions.

## Connection to Other Concepts

- [[agent-memory]] -- Memory architecture for epistemic state
- [[context-stack]] -- Where reasoning and identity are encoded
- [[agent-native-operations]] -- Executive layer and process discipline
- [[subagent-architecture]] -- Multi-agent attribution and delegation
