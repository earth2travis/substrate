---
title: "Figma x Claude Code Live: Roundtrip Workflows with Figma MCP"
tags: [research, figma, mcp, claude-code, roundtrip]
related: [skills-as-portable-knowledge, agent-native-operations, roundtrip-workflow, workflow-as-contract]
source: "YouTube livestream, Brett (Figma) and Tarek (Anthropic), 2026-04-02"
---


# Figma x Claude Code Live: Roundtrip Workflows with Figma MCP

## Summary

Live demonstration of Figma-Claude Code roundtrip workflows. Pre-MCP: clear handoffs, manual screenshots. Post-MCP: agents traverse code and canvas while keeping context intact. A single idea, manipulated on multiple surfaces.

## Key Concepts

**Source of Truth Shift:**
Not shifting to code. Shifting to the system: design, research, content, all inputs together. MCP delivers design context to agents as lossless translation between surfaces.

**Figma MCP Capabilities:**
- Read: extract design context, component structures, properties, variants
- Write: `generate_figma_design` (initial), `use_figma` (Plugin API direct manipulation, beta), image generation/upload (in development)

**Skills Architecture:**
- Foundational skill `figma-use`: unopinionated Plugin API access
- Community skills build on top (e.g., `cc-figma-tokens` for variable generation)
- Skills are composable, shareable, extensible
- Explicit invocation more reliable than inference

**Live Demos:**
1. Component round-trip: Claude creates component in Figma from code, manual tweaks, Claude updates code to match
2. Marketing poster: Claude creates graphic design asset in Figma
3. State explosion: Claude generates all login flow frames from code logic
4. Design QA: Claude compares Figma frame to actual login screen, annotates discrepancies with severity
5. Variable generation: JSON to Figma variables, skill-enabled vs unskilled comparison

**Key Insight:**
Figma canvas is cheap exploration (option-drag, duplicate) without spending tokens. Knowing when to use agentic workflows vs traditional workflows is a critical skill.

## Applications

Designers delegate tooling work (syncing, organizing, auditing) to agents. Engineers raise the bar for visual output. Cross-functional partners collaborate on skill creation. The "single idea, multiple surfaces" framing validates the architecture Loom should enable. [[skills-as-portable-knowledge]] [[agent-native-operations]] [[codex]]
