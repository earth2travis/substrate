---
title: "Figma Dev Mode + MCP: Official Presentation"
tags: [research, figma, mcp, dev-mode, design-systems]
related: [skills-as-portable-knowledge, agent-native-operations, design-system-as-code, roundtrip-workflow, workflow-as-contract]
source: "Official Figma presentation by Jake, 2026-04-01"
---

# Figma Dev Mode + MCP: Official Presentation

## Summary

Figma's official presentation on Dev Mode, Code Connect, and the Figma MCP server. Demonstrates the full design-to-code workflow using five MCP tools that give LLMs access to design metadata, screenshots, Code Connect snippets, variable definitions, and React/Tailwind code generation.

## Key Concepts

**Design System Abstractions:**
- Variables: design tokens that change between themes
- Components: reusable elements with properties
- Styles: composite tokens (box shadow, text style)
- Code Connect: maps Figma components to production code

**Dev Mode Features:**
- Inspect panel with code preview in CSS, React, etc.
- "Ready for Dev" workflow with AI layer audit
- Focus view scoped to handoff-ready work
- Theme toggling (light/dark preview)

**Code Connect (Two Versions):**
1. Snippets (deep): template files in codebase map Figma props to code output, published via `npx figma connect publish`
2. UI (shallow): connect components from Figma UI, authenticate with GitHub, auto-connect icon libraries

**Five MCP Tools:**
1. Get metadata: frames, instances, structure
2. Get screenshot: visual image of selection
3. Get code connect map: production component snippets
4. Get variable definitions: design tokens in code syntax
5. Get code: React + Tailwind representation

**Annotations as Machine-Readable Intent:**
Content annotations, property callouts, rich text, and custom context make designs machine-readable for LLM-powered workflows.

## Applications

The full workflow: designer marks "Ready for Dev," developer selects section, agent calls MCP tools in sequence (metadata → screenshot → code connect → variables → code), implements using correct components and tokens. Production-grade UI matching the design system. [[skills-as-portable-knowledge]] [[agent-native-operations]]
