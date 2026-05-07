---
title: "Cognitive Modes Pattern (from gstack)"
tags: [cognitive-modes, agent, gstack, garry-tan, workflow, context-switching]
related:
- probe-deeper-pattern
- centaur-principle
- agent-native-operations
- workflow-as-contract
source: research/raw/cognitive-modes-from-gstack.md
---
# Cognitive Modes Pattern (from gstack)

**Source:** Garry Tan's gstack — a pattern for telling the model what kind of brain to use right now. Explicit gears, not a blended mode.

"Planning is not review. Review is not shipping. Founder taste is not engineering rigor. Blurring them produces mediocre blends of all four."

## The Six Modes

**1. CEO/Founder Mode (`/plan-ceo-review`)**
- Persona: Brian Chesky. Product visionary.
- Purpose: ask "what is this product actually for?" Find the 10-star version hiding inside the request.
- Three sub-modes: scope expansion, hold scope, scope reduction
- Key mechanic: once selected, COMMIT. Don't silently drift.
- Patterns: nuclear scope challenge, temporal interrogation, dream state mapping, delight opportunities

**2. Engineering Manager Mode (`/plan-eng-review`)**
- Persona: best technical lead you've had.
- Purpose: lock in architecture, data flow, edge cases, test coverage.
- Key insight: "LLMs get way more complete when you force them to draw the system."
- Patterns: ASCII diagrams for every non-trivial flow, error and rescue map, data flow tracing with shadow paths, interaction edge case matrix

**3. Paranoid Staff Engineer Mode (`/review`)**
- Persona: the reviewer who imagines the production incident before it happens.
- Purpose: find bugs that pass CI but blow up in production.
- Targets: N+1 queries, race conditions, trust boundaries, missing indexes, bad retry logic
- Key rule: "I do not want flattery here."

**4. Release Engineer Mode (`/ship`)**
- Persona: disciplined release machine.
- Purpose: non-interactive automation. User says /ship, next thing they see is the PR URL.
- Key insight: "A lot of branches die when the interesting work is done and only the boring release work is left. Humans procrastinate that part. AI should not."
- Patterns: bisectable commits, auto-version bumping, pre-landing review embedded

**5. QA Engineer Mode (`/browse`)**
- Persona: operator in the machine.
- Purpose: give the agent eyes. Full QA pass without the human opening a browser.

**6. Engineering Manager/Retro Mode (`/retro`)**
- Persona: engineering manager running a retrospective.
- Purpose: data-driven weekly analysis.
- Patterns: session detection via 45-minute gap, focus score, fix ratio flagging, persistent JSON snapshots

## Core Principle

**"Once a mode is selected, COMMIT. Don't silently drift."**

When in research mode, stay in research mode. When in execution mode, don't get pulled into ideation. When reviewing, be paranoid, not supportive. The mode discipline is the unlock.
