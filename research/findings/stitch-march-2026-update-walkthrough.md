---
title: "Google Stitch March 2026 Update: Full Walkthrough"
tags: [research, stitch, design-systems, agents, gemini]
related: [skills-as-portable-knowledge, agent-native-operations, design-system-as-code, roundtrip-workflow]
source: "YouTube walkthrough, 2026-03-22"
---

# Google Stitch March 2026 Update: Full Walkthrough

## Summary

Major update to Google Stitch evolving it from screenshot generator to full AI Figma competitor. Introduces native design canvas, design.md portable design systems, URL-based design extraction, multiple export paths, MCP/skills integration, voice design via Gemini Live, and image generation via Imagen.

## Key Concepts

**Native Design Canvas:**
Spatial canvas accepting images, code, and PRDs as creative seeds. Multiple agents can run simultaneously. Model choice: Gemini 3 Flash (faster) or Pro (more thoughtful layouts).

**design.md File:**
Portable, agent-readable design system wrapping the entire theme. Editable graphically or as raw markdown. Bridge between design and code.

**URL-Based Design Extraction:**
Pass a URL, Stitch extracts design standard: colors, fonts, icon/button styling. Legitimate way to capture vibe from reference sites (color combinations aren't copyrightable).

**Export Paths:**
- AI Studio: codes as Next.js app with auth/database
- Figma: still supported
- React app: direct export
- Instant prototype: clickable mockup
- Project brief: PRD with design system

**MCP and Skills Integration:**
Stitch supports MCP and skills for coding agent workflows. Connects design tool directly into agentic coding pipeline.

**Voice Design (Gemini Live):**
Bidirectional voice model for conversational design iteration. Early days but directionally significant.

**Walkthrough: Resort Website:**
Reference URL → design system generation → initial design (Flash or Pro) → preview (desktop/iPad/phone) → instant prototype with page linking → iteration via prompts → export to AI Studio/Figma/React/brief.

## Applications

Stitch validates the markdown-as-contract pattern from the design side: design.md + agents.md + SKILL.md = the emerging standard. Export paths matter: fewer handoffs between design and code means less context loss. Free tier removes friction and builds market share. MCP integration signals convergence between design tools and coding agents. [[skills-as-portable-knowledge]] [[agent-native-operations]] [[design-md-transcript]]
