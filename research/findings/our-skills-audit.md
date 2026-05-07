---
title: "Skills Audit: Anthropic Skill System Assessment"
tags: [skills, anthropic, agent-tools, audit, quality]
related: [[skills-landscape]], [[tools-landscape]], [[workflows-landscape]], [[hermes-agent]], [[codex]]
source: research/raw/our-skills-audit.md
---

# Skills Audit: Anthropic Skill System Assessment

## Summary

A systematic audit of existing skills against Anthropic's published skill system guide, using a scoring rubric across frontmatter completeness, trigger precision, structural organization, and progressive disclosure depth. The audit revealed that most skills scored 6-8/10, with calendar missing YAML frontmatter entirely and web-search using passive description language. No skill had testing coverage. No Category 3 MCP Enhancement skills existed.

The core insight: skills are instructions, not contracts. The model may not follow them perfectly, and without testing there is no verification that a skill triggers correctly or produces quality output. The gap between "has a skill file" and "skill works reliably" is where most agent teams fail.

Key actions taken: fixed calendar frontmatter, identified web-search description weakness, established testing as the next priority, and set Category 3 skill development as the strategic direction for Synthweave.
