---
title: "AI Native PM Operating System"
tags: [finding, product-management, ai-native, mcp, cursor, claude]
related: [[agent-native-operations]], [[skills-as-portable-knowledge]], [[agent-tool-permissions]], [[centaur-principle]]
source: research/raw/ai-native-pm-operating-system.md
ingested: 2026-05-07
---

# AI Native PM Operating System

Mike Ball (Head of Product at David's Bridal) demonstrates an AI-native PM stack built around Claude Desktop/Cursor as the central hub, connected via MCP to Jira, GitHub, Figma, Sanity, Supabase, Gmail, and Calendar.

## Key Points

**"Thinking in prompts" as the fundamental shift.** AI-native PMs work from "what do I need to do" to "what are the steps" to "what are the best tools to get me there." The mental block of "that's too technical" is the barrier to cross.

**Centralize around one hub.** Instead of logging into 20 different tools, centralize around Claude Desktop or Cursor and connect everything else via MCP. Stay in flow state without changing UI. Example: checking if a Jira issue was completed without leaving the tool you are in.

**MCP as the integration layer.** Model Context Protocol connects apps to Claude Code/Cursor without custom coding for each integration. Supabase for database schema, Render for hosting, Sanity for CMS, Atlassian for Confluence. The MCP has its own API key and map, so it can find what the user is asking for.

**Project-level context in Claude.** Frame context per project (wedding planning app vs advertising partnerships) rather than everything in the entire application. Use Memory MCP so Claude picks up relationships between ideas over time.

**Research with Manus.** Manus runs independently, gives the full trace of everything it did, and provides sample data, sources reports, and human summaries. Unlike Claude research mode, it does not max out quickly or burn through usage. Raw information is then pulled into Claude for product requirements, user research, and technical strategy.

**Figma Make for design variation.** Not for production-quality code, but for generating variations of existing designs when the designer is already working on the next thing. Fully layered output that designers can take pieces from.

**Google AI Studio for rapid prototyping.** One-shot working apps in 10 minutes. Built to a certain quality level, then pushed to GitHub or deployed to Cloud Run, then pulled into Cursor for normal workflow editing.

## Relevance

This is the current state-of-practice for AI-native PMs. Our advantage is not the tools but the depth: persistent identity, soul documents, continuous memory, and genuine centaur partnership rather than tool usage.

## Related

- [[agent-native-operations]] -- Tools for the AI-human partnership
- [[skills-as-portable-knowledge]] -- Skills as portable capabilities
- [[agent-tool-permissions]] -- Permission models for agent tooling
