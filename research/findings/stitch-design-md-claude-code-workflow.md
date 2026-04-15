---
title: "Using Google Stitch design.md with Claude Code: Practical Workflow"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/stitch-design-md-claude-code-workflow.md
---

# Using Google Stitch design.md with Claude Code: Practical Workflow

_Source: https://www.youtube.com/watch?v=sZQ7lqaOGMg_
_Date: March 23, 2026_
_Creator: Chris (app designer, 15 years experience)_
_Transcribed and formatted: 2026-03-22_

---

## Context

This is a hands-on walkthrough of the complete Stitch to Claude Code pipeline. The creator takes an existing "vibe coded" app (a copywriting agency tool) that looks like AI slop, redesigns it in Stitch, generates a design.md, and applies it to the real codebase using Claude Code with the Stitch MCP.

## The Problem Being Solved

"How do I design apps that actually look good and not like AI slop? And how do I maintain those styles throughout the rest of my app as I continue to build it with AI?"

design.md solves this by creating a persistent, agent-readable design system that coding agents reference throughout the build.

## New Features Breakdown

1. **AI Native Canvas**: spatial canvas that accepts images, code, and PRDs as creative seeds
2. **Smarter Design Agent**: improved at creating designs
3. **Voice Interaction**: talk to the app, it transcribes into prompts
4. **Instant Prototype**: clickable preview, more like Figma than Lovable/Bolt for prototyping
5. **Design Systems (design.md)**: the big one. Created automatically as you design. Exportable. Usable in any coding agent.
6. **Stitch MCP + Skills**: connect Claude Code or any coding agent directly to Stitch designs

## The Workflow (Step by Step)

### Phase 1: Create Designs in Stitch

**Input:** Screenshots of existing app (two pages: dashboard and library)

**Prompt used:**
> I want to redesign these two screens for this web app. The purpose of this web app is to help a copywriting agency to write content for their clients using AI. The app shows a dashboard and a library screen. I'd like to redesign this in a more professional, minimal and dark mode user interface style. Can you recommend some more professional looking serif fonts for the headings and sans serif font that is readable for the body copy.

**What happened:**
- Stitch imported screenshots onto the canvas
- Generated redesigned versions that looked significantly better
- Initially created mobile designs (had to prompt for desktop versions separately)

### Phase 2: Design System Generation

Stitch automatically created a design system called "Obsidian Script" containing:

- Primary, secondary, and tertiary colors (with full scale)
- Typography (display, headline, label, title, body fonts)
- Component styling (buttons, icons, elevation)
- **Do's and don'ts**: rules for styling, which is notable

**Key observation:** Stitch picked complementary colors that a designer would choose but a non-designer wouldn't. The secondary color was a less saturated version of primary. The tertiary color was complementary. This is genuine design intelligence, not random generation.

### Phase 3: Iterate the Design

**Follow-up prompt:**
> Let's change the primary colors from purple to something that's a bit more neutral and warm and friendlier and feels a bit more like editorial. Can you also pick a complementary tertiary color? Make sure you update the design system and the desktop designs.

Stitch created an updated design system ("Obsidian Script Editorial") and regenerated all designs with the new palette.

### Phase 4: Apply to Code (Two Methods)

#### Method A: Copy design.md Manually

1. Go to design system in Stitch
2. Click design.md tab
3. Copy to clipboard
4. Create `design.md` file in project root
5. Paste and save
6. Tell Claude Code: "Redesign the app following the styles as documented in design.md"

**Result:** Claude Code created a 6-phase plan and executed it. The result was "a lot better" but didn't match the Stitch design exactly. Got the right fonts but not in the exact right way. Colors not matching 100%.

**Assessment:** design.md alone gives a good foundation but not pixel-perfect replication.

#### Method B: Use the Stitch MCP

1. Set up the Stitch MCP in Claude Code (terminal command from Stitch docs)
2. Create API key in Stitch settings
3. Start new Claude Code session (required after adding MCP)
4. Prompt: "Update the client dashboard screen to match the layout of the editorial dashboard desktop screen in Google Stitch using the Stitch MCP"

**What Claude Code does with MCP:**
- Lists all projects on Stitch
- Finds the right project
- Fetches screen details (HTML code + screenshot)
- Reads the source code Stitch generated (HTML/CSS)
- Understands layout and builds it

**Result:** "Actually pretty good." Better than design.md alone because Claude Code can see the actual HTML/CSS and screenshot, not just the design tokens. Still not 100% perfect (some fonts not pulling through correctly) but a strong foundation.

**Important caveat:** Stitch designs may include features your app doesn't have (or vice versa). Be explicit about what to include/exclude, or update Stitch designs to match your app's actual features.

### Phase 5: Ongoing Maintenance

- Claude Code can update design.md as you go
- New rules or components get added to the file
- Consistency maintained throughout the project lifecycle

## Stitch MCP Setup

```bash
# From Stitch docs, search "google stitch mcp setup"
# Available for: Cursor, VS Code, Claude Code, others
# Requires: API key from Stitch Settings > API section
# After adding: must start new Claude Code session
```

Supports: Cursor, Antigravity, VS Code, Claude Code

## Honest Assessment

### What Works Well
- Going from AI slop to professional design in one prompt
- Automatic design system generation with intelligent color selection
- design.md as persistent reference for coding agents
- MCP connection giving Claude Code direct access to Stitch designs and source code
- Instant prototyping (better than Lovable/Bolt for this purpose)
- Free to use

### What Doesn't Work Yet
- design.md alone doesn't produce pixel-perfect results
- Even with MCP, fonts and colors don't match 100%
- Stitch sometimes creates mobile designs when you want desktop
- Need to be careful about feature parity between Stitch designs and actual app

### The Creator's Take
"Is design.md perfect? Absolutely not. It's not 100% there yet. But this is based on a pattern that a lot of people were already doing by documenting their design systems in markdown files."

"I previously didn't really rate Google Stitch, but I actually really like the direction they're taking with design.md and design systems with AI agents."

## Design Tips from the Walkthrough

1. **Start with screenshots of your existing app** as input, not blank canvas
2. **Give design direction** in your prompt: "professional, minimal, dark mode"
3. **Request specific typography**: serif for headings, sans-serif for body
4. **Iterate the color palette** with natural language: "more neutral and warm and friendlier"
5. **Use design references** from Dribbble or Mobbin for even better results
6. **Generate desktop versions explicitly** (Stitch may default to mobile)
7. **Review the design system do's and don'ts** before applying to code

---

## Key Takeaways for Synthweave

1. **The two-method approach reveals a gap.** design.md alone (tokens + rules) gets you 70% there. design.md + MCP (tokens + rules + source code + screenshots) gets you 85%. The remaining 15% is still manual refinement. Loom should aim to close that gap.

2. **Stitch generates HTML/CSS, not Figma files.** The designs are code-native from the start. This is why the MCP works: Claude Code reads real HTML/CSS, not design tool artifacts. Our skills should work the same way: outputs that agents can directly consume.

3. **The "AI slop to professional" transformation is the killer use case.** Not designing from scratch. Taking something that exists and elevating it. Consider how Loom could offer the same: "take this basic agent and make it production-grade."

4. **Design system do's and don'ts are rules for agents.** Stitch generates behavioral constraints alongside visual tokens. This maps directly to how AGENTS.md works: not just what to do, but what not to do.

5. **The workflow assumes Claude Code as the coding agent.** Stitch MCP setup docs list Claude Code first. Google is building for the Claude ecosystem. This validates our toolchain choices.

6. **Feature parity between design and implementation is a real problem.** The creator explicitly warns about this. For Loom: agent capabilities in the design phase must match what's actually deployable. Don't design agents with skills that don't exist yet.
