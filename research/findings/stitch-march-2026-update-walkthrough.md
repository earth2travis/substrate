---
title: "Google Stitch March 2026 Update: Full Walkthrough"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/stitch-march-2026-update-walkthrough.md
---

# Google Stitch March 2026 Update: Full Walkthrough

_Source: https://www.youtube.com/watch?v=J7XpscQqCYw_
_Date: March 23, 2026_
_Transcribed and formatted: 2026-03-22_

---

## Overview

Google Labs dropped a major update to Stitch. What started as a simple screenshot/mockup generator has evolved over the past year into a full AI Figma competitor. This update introduces an agentic system incorporating recent Gemini text and image models.

## New Features

### 1. Native Design Canvas

Similar concept to AI Studio, but for design instead of code. You prompt it, it builds the design with you. Uses a new **design agent** under the hood.

Key details:
- Can spin up multiple agents at a time
- Choose between Gemini 3 Flash or Pro models
- Flash is faster, Pro sometimes produces more thoughtful layouts
- Results vary between runs (experiment early)

### 2. design.md File

Just as coding tools have agents.md, Stitch now creates a **design.md** file that wraps your entire design system.

Two ways to edit:
- **Graphically**: edit the theme through the UI
- **As a file**: get the raw design.md and use it in your coding editor, another tool, or as an organizational brand standard applied across multiple designs

This is the bridge between design and code. A portable, agent-readable design system.

### 3. URL-Based Design Extraction

Pass in a URL and Stitch pulls out the design standard from that site: colors, fonts, styling on icons and buttons.

Use case: if you have an existing site you're happy with, feed it in as context for building the design system and design.md.

Note: color combinations and general styling aren't copyrightable, so this is a legitimate way to capture a vibe from a reference site.

### 4. Export Options

Multiple export paths:
- **AI Studio**: takes the design and codes it up as a Next.js app (can add authentication, database, etc.)
- **Figma**: still supported
- **React app**: direct export
- **Instant prototype**: clickable mockup
- **Project brief**: generates a product requirements document including design system and palette

The AI Studio export passes both HTML and image versions, giving the coding agent full context.

### 5. MCP and Skills Integration

Stitch now supports MCP (Model Context Protocol) and skills as ways to work with coding agents. This connects the design tool directly into the agentic coding workflow.

### 6. Voice Design (Gemini Live)

Uses the Gemini Live bidirectional model for "vibe design" with voice. Talk to the interface, it makes changes in real time.

Assessment: still early days, but the direction is clear. Conversational design iteration.

### 7. Image Generation

Uses Imagen (likely Imagen 3) in the background for placeholder images. Generates contextually appropriate images (e.g., chefs for a cuisine page, resort imagery for a hospitality site).

## Walkthrough: Building a Resort Website

### Step 1: Setup
- Choose web app (vs mobile app)
- Paste a reference URL (in this case, a famous Thai resort)
- Stitch recognizes the URL as a source automatically

### Step 2: Design System Generation
- Stitch analyzes the reference site
- Extracts primary and secondary colors (browns, earth tones from the resort)
- Identifies fonts
- Picks up styling for icons, buttons, and other elements
- Builds the theme automatically

### Step 3: Initial Design
- Flash model generates the first design
- Gets the "vibe" right from the reference
- Pro model produces similar design specs but sometimes more thoughtful layouts
- Can request specific pages (programs, cuisine, residences) from the nav bar

### Step 4: Preview
- Preview as desktop, iPad, or phone
- Responsive layouts generated automatically

### Step 5: Instant Prototype
- Wires pages together into a clickable prototype
- Navigate page to page
- Select any element to modify
- Connect screens to each other

### Step 6: Iterate
- Prompt for variations: "go for a more holistic natural food look"
- Generates multiple variations per page
- Compare side by side
- Can upload custom images to replace generated ones

### Step 7: Export
- AI Studio: adds prompt for what to build ("make this real and add a user dashboard with dynamic data")
- Figma: for teams still in that workflow
- React: direct code export
- Project brief: PRD with design system included

## Design System Editing

- Edit theme visually (colors, fonts, borders)
- Import design system from any website URL
- Save and apply across projects
- Export as design.md for use in any coding project

## Assessment

Stitch has become a real competitor to Figma for non-professional designers who know what they want. Particularly strong for:

- People with reference sites they want to emulate
- Quick prototyping with real design systems
- Bridging design to code without manual handoff

### Current Strengths
- Free (no cost for service or tokens)
- URL-based design extraction is powerful
- design.md as portable design system
- Direct export to AI Studio for full app development
- Instant prototyping with page linking

### Current Limitations
- Limited to apps and websites (no thumbnails, general design yet)
- Still in beta
- Model choice (Flash vs Pro) produces variable results

### What to Watch For
- Expansion beyond apps/websites (thumbnails, general design)
- Tighter integration with coding agents via MCP
- Model improvements as Gemini 3.1 Flash releases

---

## Key Takeaways for Synthweave

1. **The agentic design pattern is real.** Stitch now runs multiple design agents simultaneously, same pattern as our research agents. Design is becoming an orchestration problem.

2. **URL as input is a killer feature.** "Capture the vibe of this site" as a design primitive. Consider how Loom could offer similar: "build an agent that works like this reference."

3. **design.md + agents.md + SKILL.md = the pattern.** Markdown files in repos as contracts between humans and agents. Stitch validates this from the design side. We validate it from the agent side.

4. **Export paths matter.** Stitch to AI Studio to Next.js app is a real pipeline. Our equivalent: Loom to skills to deployed agent. The fewer handoffs, the better.

5. **Free tier as adoption strategy.** Stitch is free. Tokens are free. This is Google Labs building market share by removing friction. Consider implications for Synthweave pricing.

6. **MCP integration signals convergence.** Stitch supporting MCP means design tools and coding agents are connecting through the same protocol. Loom should be ready for this.
