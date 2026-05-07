---
title: Design System as Code
tags:
- concept
- design-systems
- markdown
- infrastructure
- agents
related:
- skills-as-portable-knowledge
- agent-native-operations
- roundtrip-workflow
- workflow-as-contract
- progressive-autonomy
- figma-dev-mode-presentation
- figma-github-projects-plugin
- figma-x-claude-code-livestream
- stitch-design-md-claude-code-workflow
- stitch-march-2026-update-walkthrough
- premium-results-strategy
source: 'Synthesized from Batch 19: design-md-transcript, figma-dev-mode-presentation,
  stitch-workflow, skill-design-foundations'
---



# Design System as Code

## Definition

A design system expressed as a markdown file in the code repository, making it version-controlled, agent-readable, and portable across tools and teams. The design system is infrastructure, not a feature locked inside a proprietary design tool.

## Core Idea

The traditional design pipeline has three lossy handoffs: PM writes document, designer creates mockup in separate tool, developer interprets and codes. Each translation is where things go wrong. design.md collapses this into one continuous loop by making the design system a file that both humans and agents can read and write.

**The Pattern:**
- claude.md: prompting instructions
- agents.md: agent configurations
- design.md: design systems
- SKILL.md: agent skills
- WORKFLOW.md: executable process definitions

Different teams, independently, arriving at the same conclusion: a markdown file in the repo is the perfect contract between humans and AI agents.

## Why It Works

- Simple enough for a human to open and edit
- Structured enough for an AI agent to parse reliably
- Trackable with git (full version history, diffable)
- No special SDK or API key required
- It's just a file

## Key Implementations

**Google Stitch:** Automatically generates design.md from canvas designs. Exports to AI Studio, Figma, React. URL-based extraction from reference sites.

**Figma Code Connect:** Template files in the codebase map Figma component properties to code output. Renders recursively for nested components. Links to GitHub source.

**Figma MCP:** Five tools give LLMs direct access to design metadata, screenshots, Code Connect snippets, variable definitions, and React/Tailwind code generation.

**Anthropic Skills:** SKILL.md with YAML frontmatter and Markdown instructions. Progressive disclosure minimizes token usage.

## Limitations and Gaps

- design.md alone doesn't describe complex user flows or animations
- Pixel-perfect replication requires source code + screenshots, not just tokens
- Feature parity between design and implementation must be explicitly managed
- Fonts and colors don't always translate 100% across tools

## Applications

**For Agent Factories:**
Agent-readable design systems mean agents can maintain visual consistency across implementations. Design rules become executable constraints. Do's and don'ts are behavioral specifications, not style guide suggestions.

**For Cross-Functional Teams:**
Designers and engineers collaborate on the same file. Changes are reviewable via PR. The design system evolves with the code, not beside it.

**For Tool Builders:**
The unopinionated platform access + opinionated community skills on top maps directly to how design tools should integrate with agent ecosystems. MCP as the translation layer.

## Related

- [[skills-as-portable-knowledge]]: the same pattern applied to agent behavior
- [[agent-native-operations]]: tools designed for AI-human partnership
- [[codex]]: the coding agent that consumes these design systems
- [[workflow-as-contract]]: executable process definitions in markdown
- [[progressive-autonomy]]: graduated trust for agent design capabilities
