---
title: "Anthropic Skills Guide: Building Skills for Claude"
tags: [research, skills, claude, mcp]
related: [skills-as-portable-knowledge, agent-native-operations, synthweave-mcp-analysis, codex]
source: "resources.anthropic.com, extracted 2025-07-17"
---

# Anthropic Skills Guide: Building Skills for Claude

## Summary

Anthropic's official guide for building Claude skills defines a skill as a folder containing SKILL.md (required), scripts/, references/, and assets/. Skills use progressive disclosure (YAML frontmatter always loaded, body loaded when relevant, linked files discovered as needed), composability across skills, and portability across Claude.ai, Claude Code, and API.

## Key Concepts

**Three Use Case Categories:**
1. Document & Asset Creation: embedded style guides, templates, quality checklists
2. Workflow Automation: multi-step processes with validation gates and iterative refinement
3. MCP Enhancement: coordinates multiple MCP calls, embeds domain expertise, handles errors

**Critical Technical Rules:**
- SKILL.md must be exactly `SKILL.md` (case-sensitive)
- Folder naming: kebab-case only
- No README.md inside skill folder
- No XML angle brackets in frontmatter
- No "claude" or "anthropic" in skill name

**Frontmatter Requirements:**
- name (required): kebab-case, matches folder
- description (required): under 1024 chars, must include what it does AND when to use it
- Optional: license, compatibility, metadata

**Three Testing Areas:**
1. Triggering tests: loads at right times, doesn't trigger on unrelated topics
2. Functional tests: correct outputs, API success, error handling, edge cases
3. Performance comparison: token usage, message count, error rate with/without skill

**Distribution:** Download folder → zip → upload to Claude.ai Settings, or place in Claude Code skills directory. API `/v1/skills` endpoint available.

## Applications

Skills-as-portable-knowledge pattern validated by platform vendor. Progressive disclosure minimizes token usage. Testing framework provides measurable quality gates. [[skills-as-portable-knowledge]] [[agent-native-operations]]
