---
title: "gstack Analysis: Garry Tan's Claude Code Workflow System"
tags: [skills, claude-code, workflow, browser, patterns, efficiency]
related:
- skills-landscape
- tools-landscape
- workflows-landscape
- browser-efficiency-from-gstack
source: research/raw/gstack-analysis.md
---
# gstack Analysis: Garry Tan's Claude Code Workflow System

## Summary

gstack is a set of six opinionated skills for Claude Code that transform a generic AI assistant into a team of specialists invoked via slash commands. The core thesis: different phases of software development require fundamentally different cognitive modes, and blurring them together produces mediocre results.

The six skills are: plan-ceo-review (challenge problem framing), plan-eng-review (lock architecture), review (paranoid structural audit), ship (fully automated release), browse (persistent headless Chromium daemon), and retro (quantitative velocity metrics). Garry Tan (YC President) ships 10+ PRs/day and 10K+ LOC/day using this system.

Key architectural insight: explicit cognitive mode switching is underrated. "Be a paranoid reviewer" produces better output than "review this PR" because it sets expectations about depth, tone, and what matters. gstack's compiled browser binary achieves ~100-200ms per command vs. 1500-2000 tokens per MCP call, a significant efficiency win for high-volume browser sessions.

gstack has no memory between sessions, no identity, no proactive behavior. It is a tool multiplier for a single developer, not an autonomous agent. Our system has the opposite strengths: persistent memory, identity, multi-channel presence, sub-agent orchestration. These are complementary, not competing, approaches.
