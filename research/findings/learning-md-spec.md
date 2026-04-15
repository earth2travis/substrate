---
title: "LEARNING.md: Per-Run Feedback for Self-Improving Agentic Systems"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/learning-md-spec.md
---

# LEARNING.md: Per-Run Feedback for Self-Improving Agentic Systems

Research Date: 2026-02-27
Status: Early concept

## The Problem

Agentic systems run workflows repeatedly but don't systematically capture what they learn from each execution. Existing conventions (CLAUDE.md, AGENTS.md, .cursorrules) handle project context and identity. Memory files (daily logs, MEMORY.md) handle episodic and semantic recall. Nothing occupies the space of **structured feedback from a specific workflow run** that feeds back into the next run.

The "reflect" pattern is emerging across multiple implementations (Claude Diary, claude-mem, fsck.com episodic memory, Softcery's session logs) but everyone names the output differently and most conflate reflection with journaling. The feedback signal gets lost in narrative.

## The Idea

One learning file per workflow run. The workflow produces its output AND its reflection as a pair. The file captures what happened, what went wrong, and what to do differently. Atomic, scoped, diffable.

## Structure

```
learning/
  <workflow-name>/
    <ISO-timestamp>.md
    <ISO-timestamp>.md
  <workflow-name>/
    <ISO-timestamp>.md
```

Each file is a snapshot of one execution. The directory for a workflow becomes its improvement history, readable chronologically.

## Pre-Run Behavior

Before executing a workflow, the agent reads the last N learning files for that workflow. Recent feedback informs the current run. Recency handles pruning naturally: you only look back a window.

## Graduation

When the same lesson appears across multiple run files, that's the signal to bake it into the workflow itself (update the script, the prompt, the skill). The learning files become evidence for the change. After graduation, old files can be archived or deleted.

## Diffing as Audit

If run 5 learned "always check for rate limits" and run 12 still hit a rate limit, the learning files make that visible. They become an audit trail for whether the system is actually improving or just logging the same mistakes.

## Where It Fits

| File | Purpose | Nature |
|---|---|---|
| CLAUDE.md / AGENTS.md | Who I am, how to work here | Static context |
| memory/ | What happened each day | Episodic log |
| MEMORY.md | Curated long-term knowledge | Semantic, maintained |
| learning/ | What I learned from doing the work | Dynamic feedback buffer |
| Workflows / Skills | The actual behavior | Updated by graduating learnings |

## The Self-Improving Loop

Run → Observe → Record in learning/<workflow>/<timestamp>.md → Next run reads recent learning files → Performs better → Validated fix merges into the workflow → Old entries cleared.

## Ecosystem Context

No standard exists for this yet. A December 2025 survey ("Memory in the Age of AI Agents," arXiv:2512.13564) catalogues the fragmentation. Key finding: a plain filesystem scores 74% on memory benchmarks, beating specialized vector store libraries. Markdown files work. The gap is in naming the pattern and giving it structure.

Everyone is doing per-run reflection ad hoc. Nobody has named it.

## Open Questions

- What goes in each file? Minimal viable schema TBD.
- How many recent files should the agent read before a run? Fixed window vs. adaptive?
- Should learning files be human-written, agent-written, or both?
- How to handle workflows that call sub-workflows? Nested learning?
- Should there be a rollup mechanism (periodic distillation into a summary file per workflow)?
- Is this a convention to propose publicly (like AGENTS.md) or just internal tooling?
