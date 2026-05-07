---
title: "Roundtrip Workflow"
tags: [concept, design, code, roundtrip, mcp, agents]
related: [skills-as-portable-knowledge, agent-native-operations, workflow-as-contract, design-system-as-code]
source: "Synthesized from Batch 19: figma-livestream, stitch-workflow, design-md-transcript"
---

# Roundtrip Workflow

## Definition

A workflow where agents can translate bidirectionally between design and code surfaces: reading a design to write code, reading code to generate or update a design, and keeping context intact across both directions. Not a one-way handoff but a continuous loop.

## Core Idea

Pre-MCP workflows had clear handoffs: designer hands off to developer, developer hands off to deployer. Each handoff was lossy. Post-MCP workflows let agents traverse surfaces while keeping context intact. Code and UI are both materials. MCP provides lossless translation between them.

**The Old Pipeline (telephone game):**
1. PM writes document
2. Designer creates mockup
3. Developer interprets and codes
4. QA finds discrepancies
5. Back to designer for fixes
6. Back to developer for updates

**The New Loop:**
1. Designer marks section "Ready for Dev"
2. Agent reads design metadata, screenshot, component mappings, variables, code representation
3. Agent implements using production components
4. Designer tweaks in Figma
5. Agent reads changes and updates code
6. Agent compares implementation to design and annotates discrepancies

## Key Capabilities

**Code to Design:**
- Agent analyzes code logic and generates all UI states
- Creates components in Figma with proper variant structure
- Self-annotates fidelity notes, linked components, manual rebuilds, known issues

**Design to Code:**
- Agent reads design metadata to understand structure
- Gets screenshot for visual reference
- Pulls Code Connect snippets for production components
- Retrieves variable definitions in code syntax
- Generates React/Tailwind implementation

**Design QA:**
- Agent compares Figma frame to actual implementation
- Annotates discrepancies with severity (high/medium/low)
- Flags component overrides
- Drops comments on Figma frame via API

## Applications

**For Designers:**
Delegate tooling work (syncing, organizing, auditing, linting) to agents. Focus on deep creative work. The canvas becomes cheap exploration without token cost.

**For Engineers:**
Bar for visual output rises. Marketing assets, prototypes, simple design versions that previously needed a designer are now agent-generated. But the hard part remains: deciding what to build, not how to build it.

**For Agent Factories:**
The "single idea, multiple surfaces" framing validates the architecture Loom should enable. MCP as the translation layer. Skills as the domain-specific intelligence layer.

## Limitations

- Image generation/upload via MCP not yet available
- Comment APIs require different auth methods than MCP tools
- Agents balance initiative vs asking for approval: sometimes too cautious, sometimes not cautious enough
- Each model generation behaves differently

## Related

- [[skills-as-portable-knowledge]]: portable, composable skill architecture
- [[agent-native-operations]]: tools designed for AI-human partnership
- [[codex]]: the coding agent in the roundtrip loop
- [[workflow-as-contract]]: version-controlled agent behavior definitions
- [[design-system-as-code]]: design systems as agent-readable markdown files
