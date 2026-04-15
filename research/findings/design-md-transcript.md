---
title: "design.md: The Real Story Behind Google Stitch's Update"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/design-md-transcript.md
---

# design.md: The Real Story Behind Google Stitch's Update

_Source: https://www.youtube.com/watch?v=FWuJZaVWhxk_
_Transcribed and formatted: 2026-03-22_

---

## The Headline Everyone Missed

Google dropped a huge update to Stitch. The tech world focused on the canvas, voice controls, and "vibe design." Those features are neat, but that is not the real story.

The actual game-changing announcement is something quieter, more fundamental: a single, unassuming file called **design.md**.

## What is design.md?

The official term: a **portable, agent-readable design system**.

It's a single markdown file that lays out your entire design system (colors, fonts, spacing) in plain, natural language. The magic: a coding agent can read it and use it directly.

This is a massive jump from a static PDF style guide or design tokens buried inside a proprietary tool.

**The most important part:** it lives inside your code repository.

That phrase, "in your repo," is the entire point.

## The Critical Shift: Feature to Infrastructure

Think about a normal design system in Figma. It's locked down. Only Figma really gets it.

Now look at design.md. It's in your repo, totally open. Any agent, any development environment, any workflow can read it.

That is the shift from being a feature to becoming actual infrastructure.

## Collapsing the Pipeline

design.md isn't really about the file itself. It's about what it does to our broken development process. It collapses three painful handoffs into one continuous loop.

### The Old Workflow (a game of telephone)

1. PM writes a document
2. Designer creates a mockup in a separate tool
3. Developer interprets all of that and turns it into code
4. Every handoff is where things go wrong

### The New Loop

1. PM describes the business goal
2. An AI tool like Stitch generates the initial UI
3. The coding agent reads design.md and builds the final product directly against it

No Figma export. No spec document. No painful meetings about how the developer interpreted the design wrong.

## The Handoff Was Always the Bug

It wasn't the tools that were the problem. It was the broken, lossy translation of ideas between them.

Going one level deeper: it wasn't just a process problem. It was a **context problem**. Every team (product, design, engineering) was working from their own separate static snapshot of truth.

design.md creates a single, shared, live source of truth for the entire pipeline.

## Markdown as the Universal Agent Interface

This connects to a bigger trend happening almost under the radar. Markdown is quietly becoming the universal interface for AI agents:

| File | Purpose |
|------|---------|
| claude.md | Prompting instructions |
| agents.md | Agent configurations |
| design.md | Design systems |

Different teams, completely independently, all arriving at the same idea: **a markdown file in the code repo is the perfect contract between humans and AI agents.**

### Why It Works

- Simple enough for a human to open and edit
- Structured enough for an AI agent to parse reliably
- Trackable with git (full version history)
- No special SDK or API key required
- It's just a file

That simplicity is what makes it powerful and open.

## Current Limitations

This doesn't magically solve everything. As one bottleneck is fixed, a new one appears.

- design.md doesn't describe complex user flows or animations yet
- It's the foundation, not the whole skyscraper
- Stitch is still in beta, with bugs
- Currently only exports basic HTML and CSS

But the trajectory is clear. The old fragmented pipeline from design to code is collapsing into a single unified step.

## The Living File vs. the Static Artifact

design.md is a living file, not a static artifact you hand off and forget.

Update the markdown, the agent sees the change instantly. No more Slack messages asking "hey, did you see the latest Figma update?"

## What This Means for Work

The bottleneck doesn't vanish. It moves. It shifts from pure execution to **judgment**.

The value is no longer the manual act of writing code or pushing pixels. It's the strategic decisions made before any of that happens.

When you can go from idea to fully functional, on-brand prototype in an hour or less, the hard part isn't building. **The hard part is deciding what to build.**

That is the question we all need to get much better at answering.

---

## Key Takeaways for Synthweave

1. **design.md is infrastructure, not a feature.** It's the pattern we should follow: portable, agent-readable specs as markdown files in repos.
2. **The handoff is the bug.** Any place where context translates between humans or tools is a failure point. Collapse those handoffs.
3. **Markdown is becoming the universal agent interface.** claude.md, agents.md, design.md, SKILL.md. We're already building this way.
4. **The value shifts to judgment.** When execution is cheap, deciding what to execute is the bottleneck. This is the strategic layer Loom should optimize for.
5. **Living files over static artifacts.** Agents read from the repo. The repo is the truth. Everything else is a lossy copy.
