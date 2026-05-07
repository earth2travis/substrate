---
title: "Skills Landscape for Agentic Systems"
tags: [skills, agent-tools, mcp, anthropic, orchestration, patterns]
related:
- tools-landscape
- workflows-landscape
- our-skills-audit
- codex
- hermes-agent
- skills-as-portable-knowledge
source: research/raw/skills-landscape.md
---
# Skills Landscape for Agentic Systems

## Summary

Skills are reusable packages of procedural knowledge for AI agents. They tell an agent how to accomplish tasks, as opposed to tools which give agents capabilities to act. Anthropic formalized the concept in October 2025. By December, OpenAI adopted the same format for Codex. The Agent AI Foundation now lists Skills alongside MCP and agents.md as founding sibling projects.

Anthropic's reference implementation uses three levels of progressive disclosure: YAML frontmatter (always in context, under 1024 chars), SKILL.md body (loaded when relevant), and linked files (discovered as needed). This respects context window limits. Most skills are invisible most of the time.

Three categories exist: Document and Asset Creation, Workflow Automation, and MCP Enhancement. Category 3 is where Skills and MCP intersect: a skill wraps MCP tools with procedural knowledge, orchestrating multi-step tool calls with domain expertise and error handling.

The ecosystem is young: no formal registry, no runtime verification, manual discovery. But the format is simple (markdown + YAML + optional scripts), portable, and versionable. The three-layer architecture (MCP servers provide capabilities, Skills orchestrate them, Workflow orchestration manages activation) cleanly separates concerns.
