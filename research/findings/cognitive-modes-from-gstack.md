---
title: Cognitive Modes Pattern (from gstack)
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/cognitive-modes-from-gstack.md
---

# Cognitive Modes Pattern (from gstack)

**Source:** [github.com/garrytan/gstack](https://github.com/garrytan/gstack) (Garry Tan, YC President)
**Filed:** 2026-03-11

## Core Insight

"I do not want AI coding tools stuck in one mushy mode." The unlock is telling the model what kind of brain to use right now. Explicit gears, not a blended mode.

Planning is not review. Review is not shipping. Founder taste is not engineering rigor. Blurring them produces mediocre blends of all four.

## The Six Cognitive Modes

### 1. CEO/Founder Mode (`/plan-ceo-review`)

**Persona:** Brian Chesky. Product visionary.

**Purpose:** Don't take the request literally. Ask "what is this product actually for?" Find the 10-star version hiding inside the request.

**Three sub-modes:**
- **SCOPE EXPANSION:** Dream big. "What's 10x more ambitious for 2x effort?" Build the cathedral.
- **HOLD SCOPE:** Scope accepted. Make it bulletproof. Maximum rigor on the plan as stated.
- **SCOPE REDUCTION:** Surgeon mode. Find the minimum viable version. Cut everything else.

**Key mechanic:** Once a mode is selected, COMMIT. Don't silently drift. Raise concerns once, then execute the chosen mode faithfully.

**Valuable patterns:**
- Nuclear Scope Challenge (Step 0): Is this the right problem? What happens if we do nothing? What's the 12-month ideal state?
- Temporal Interrogation: What decisions will need to be made at Hour 1, Hour 2-3, Hour 4-5? Resolve them NOW.
- Dream State Mapping: CURRENT → THIS PLAN → 12-MONTH IDEAL
- Delight Opportunities: 5+ adjacent 30-minute improvements that make users think "oh nice, they thought of that"

### 2. Engineering Manager Mode (`/plan-eng-review`)

**Persona:** Best technical lead you've had.

**Purpose:** Lock in architecture, data flow, edge cases, test coverage. Make the idea buildable.

**Key insight:** "LLMs get way more complete when you force them to draw the system." Diagrams force hidden assumptions into the open.

**Valuable patterns:**
- Mandatory ASCII diagrams for every non-trivial flow
- Error & Rescue Map: method → what can fail → exception class → rescued? → user sees?
- Data flow tracing with shadow paths (nil, empty, error for every path)
- Interaction edge case matrix (double-click, navigate-away, slow connection, stale state, back button)

### 3. Paranoid Staff Engineer Mode (`/review`)

**Persona:** The reviewer who imagines the production incident before it happens.

**Purpose:** Find bugs that pass CI but blow up in production. Not style nitpicks.

**Targets:** N+1 queries, race conditions, trust boundaries, missing indexes, bad retry logic, tests that pass while missing the real failure mode.

**Key rule:** "I do not want flattery here."

### 4. Release Engineer Mode (`/ship`)

**Persona:** Disciplined release machine.

**Purpose:** Non-interactive automation. User says /ship, next thing they see is the PR URL.

**Key insight:** "A lot of branches die when the interesting work is done and only the boring release work is left. Humans procrastinate that part. AI should not."

**Valuable patterns:**
- Bisectable commits: split logical units, ordered by dependency
- Auto-version bumping (4-digit: MAJOR.MINOR.PATCH.MICRO)
- Pre-landing review embedded in the ship flow
- Only stops for: merge conflicts, test failures, critical review findings

### 5. QA Engineer Mode (`/browse`)

**Persona:** Operator in the machine.

**Purpose:** Give the agent eyes. Full QA pass without the human opening a browser.

See browser section below.

### 6. Engineering Manager/Retro Mode (`/retro`)

**Persona:** Engineering manager running a retrospective.

**Purpose:** Data-driven weekly analysis. Commits, LOC, test ratio, PR sizes, session detection, shipping streaks.

**Valuable patterns:**
- Session detection via 45-minute gap between commits
- Focus score: % of commits touching single most-changed directory
- Fix ratio flagging: >50% fixes signals "ship fast, fix fast" pattern
- Persistent JSON snapshots for trend tracking
- Tweetable summary line as first output

## Adaptation for Our System

### What to Build

**Cognitive mode switching for our workflow.** We don't use Claude Code's slash commands, but we can implement the same pattern through our skills system or AGENTS.md directives:

1. **Founder Mode** → When evaluating new ideas, features, or directions. Use the 10-star framing, dream state mapping, and scope challenge before committing to build.

2. **Review Mode** → Before merging PRs or closing issues. The paranoid staff engineer lens, not the "looks good to me" lens. Maps directly to the "no-men" concept from the a16z article.

3. **Ship Mode** → Automate the boring release hygiene. Our "Before You Work" process already has steps 1-9, but we could make a more automated version that runs tests, checks CI, and opens the PR in one flow.

4. **Retro Mode** → Our daily reports and weekly planning partially cover this, but the quantitative analysis (session detection, focus score, fix ratio, streak tracking) is sharper. Consider adding metrics to our daily reports.

### What We Already Have

- The Floor = our operational mode (covers what /retro and monitoring do)
- AGENTS.md "Before You Work" = our ship process (less automated)
- Issue closure protocol = partial review mode
- SOUL.md values = our founder taste (but not structured as a review process)

### Key Principle to Steal

**"Once a mode is selected, COMMIT. Don't silently drift."**

This is the most transferable insight. When we're in research mode, stay in research mode. When we're in execution mode, don't get pulled into ideation. When we're reviewing, be paranoid, not supportive. The mode discipline is the unlock.
