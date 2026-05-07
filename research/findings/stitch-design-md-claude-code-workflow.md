---
title: "Stitch design.md with Claude Code: Practical Workflow"
tags: [research, stitch, design-systems, claude-code, mcp]
related: [skills-as-portable-knowledge, agent-native-operations, design-md-transcript, codex]
source: "YouTube walkthrough by Chris, 2026-03-22"
---

# Stitch design.md with Claude Code: Practical Workflow

## Summary

Hands-on walkthrough of the Stitch to Claude Code pipeline. Takes a "vibe coded" app that looks like AI slop, redesigns it in Stitch, generates a design.md, and applies it to the real codebase via Claude Code with the Stitch MCP.

## Key Concepts

**The Problem:**
"How do I design apps that actually look good and not like AI slop? And how do I maintain those styles throughout the rest of my app as I continue to build it with AI?"

**Two Application Methods:**

*Method A: design.md manually:*
Copy design.md from Stitch, paste into project root, tell Claude Code "Redesign following styles in design.md." Result: good foundation but not pixel-perfect (~70% match).

*Method B: Stitch MCP:*
Connect Claude Code to Stitch via MCP. Agent lists projects, fetches screen details (HTML + screenshot), reads source code, understands layout, builds it. Result: better than design.md alone (~85% match) because agent sees actual HTML/CSS and screenshots.

**Design System Generation:**
Stitch automatically creates design systems with primary/secondary/tertiary colors, typography, component styling, and do's/don'ts rules. Color selection demonstrates genuine design intelligence (complementary palettes, saturation control).

**Iteration Workflow:**
Natural language prompts change the design system ("more neutral and warm and friendlier"), Stitch updates all designs with new palette. Claude Code can update design.md as project evolves.

**Honest Limitations:**
- design.md alone doesn't produce pixel-perfect results
- Even with MCP, fonts and colors don't match 100%
- Stitch sometimes creates mobile when desktop requested
- Feature parity between design and implementation requires explicit management

## Applications

The two-method approach reveals a gap: tokens + rules gets 70%, tokens + rules + source + screenshots gets 85%. The remaining 15% is manual refinement. For agent factories: design system do's/don'ts are behavioral constraints for agents, same pattern as AGENTS.md. [[skills-as-portable-knowledge]] [[agent-native-operations]] [[design-md-transcript]] [[codex]]
