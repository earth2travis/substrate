---
title: "design.md: Portable Agent-Readable Design Systems"
tags: [research, design-systems, stitch, agents, markdown]
related: [skills-as-portable-knowledge, agent-native-operations, stitch-design-md-claude-code-workflow, llm-wiki-pattern]
source: "YouTube transcript, 2026-03-22"
---

# design.md: Portable Agent-Readable Design Systems

## Summary

Google Stitch's design.md is a single markdown file that lays out an entire design system (colors, fonts, spacing, rules) in plain natural language. The critical shift: it lives inside the code repository, making it readable by any coding agent without proprietary tooling.

## Key Concepts

**From Feature to Infrastructure:**
Traditional design systems in Figma are locked down. design.md in the repo is open: any agent, any environment, any workflow can read it. This collapses three handoffs (PM → Designer → Developer) into one continuous loop.

**Markdown as Universal Agent Interface:**
Multiple teams independently arrived at the same pattern:
- claude.md: prompting instructions
- agents.md: agent configurations
- design.md: design systems
- SKILL.md: agent skills

A markdown file in the repo is becoming the standard contract between humans and AI agents.

**Why It Works:**
- Simple enough for humans to edit
- Structured enough for agents to parse
- Trackable with git (full version history)
- No special SDK or API key required

**Limitations:**
- Doesn't describe complex user flows or animations yet
- Stitch is still in beta
- Currently only exports basic HTML and CSS
- Not pixel-perfect replication (gets ~70% there alone, ~85% with MCP)

## Applications

design.md creates a single, shared, live source of truth for the entire product pipeline. Update the markdown, the agent sees the change instantly. The value shifts from manual execution to strategic judgment: deciding what to build, not how to build it. [[skills-as-portable-knowledge]] [[agent-native-operations]]
