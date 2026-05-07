---
title: "Claude Code: Complete Capabilities Guide"
tags: [research, claude-code, capabilities, skills, memory, mcp]
related: [openclaw, skills-as-portable-knowledge, agent-native-operations, progressive-autonomy, the-openclaw-lesson, browser-automation]
source: "https://code.claude.com/docs, compiled February 24, 2026"
---

# Claude Code: Complete Capabilities Guide

## Summary

Comprehensive inventory of Claude Code's feature set: core architecture, memory system, skills, hooks, subagents, agent teams, plugins, MCP, permissions, programmatic usage, GitHub Actions, session management, checkpointing, model configuration, and cost management.

## Core Architecture

Three-phase loop: gather context, take action, verify results. Surfaces: Terminal CLI, VS Code extension, JetBrains plugin, Desktop app, Web, iOS, Slack, Chrome extension, GitHub Actions, GitLab CI/CD.

Built-in tools: file operations, search, execution, web, code intelligence.

## Memory System

Layered hierarchy:
- Managed policy (`/etc/claude-code/CLAUDE.md`): org-wide instructions
- Project memory (`./CLAUDE.md`): team-shared project instructions
- Project rules (`./.claude/rules/*.md`): modular, topic-specific, path-scoped
- User memory (`~/.claude/CLAUDE.md`): personal preferences
- Local project memory (`./CLAUDE.local.md`): personal project preferences (gitignored)
- Auto memory (`~/.claude/projects/<project>/memory/`): Claude's automatic notes

Auto memory writes project patterns, build commands, debugging insights, architecture notes. First 200 lines of MEMORY.md loaded into system prompt every session. Topic files loaded on demand.

CLAUDE.md imports: `@path/to/file` syntax, recursive up to 5 levels. Path-scoped rules with glob patterns and brace expansion.

## Skills (Custom Slash Commands)

Markdown files with YAML frontmatter in `.claude/skills/<name>/SKILL.md`.

Key fields: `name`, `description`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `model`, `context: fork`, `agent`, `hooks`.

String substitutions: `$ARGUMENTS`, `$N`, `${CLAUDE_SESSION_ID}`. Supporting files (templates, examples, scripts) in skill directory.

## Hooks

Lifecycle automation: `SessionStart/End`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PermissionRequest`, `SubagentStart/Stop`, `TaskCompleted`, `ConfigChange`, `PreCompact`, etc.

Types: command (shell), prompt (LLM), agent. PreToolUse hooks can return `permissionDecision: deny` to block tool calls.

## Subagents and Agent Teams

Built-in subagents: Explore (Haiku, read-only), Plan (read-only), General purpose, Bash, Claude Code Guide. Custom subagents in `.claude/agents/` with frontmatter for tools, model, hooks, memory.

Agent teams (experimental): multiple Claude Code instances coordinating with peer-to-peer messaging. Enable with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

## MCP (Model Context Protocol)

Three transports: HTTP (recommended remote), SSE (deprecated), Stdio (local). Scopes: local, project, user. Dynamic tool updates via `list_changed` notifications. Tool search: auto-defer when descriptions exceed 10% of context.

## Permissions and Security

Modes: default, acceptEdits, plan, dontAsk, bypassPermissions (containers only). Sandboxing: OS-level filesystem/network isolation via Seatbelt (macOS) or bubblewrap (Linux). Managed settings: org-wide policies via MDM or file-based configs.

## Programmatic Usage and CI/CD

`claude -p "query"` for non-interactive execution. Output formats: text, json, stream-json. Structured output via `--json-schema`. Key flags: `--allowedTools`, `--max-turns`, `--max-budget-usd`, `--append-system-prompt`, `--continue`, `--resume`, `--fallback-model`.

GitHub Actions: `@claude` mention in PRs/issues triggers automated review, feature implementation, bug fixes. GitLab CI/CD also supported.

## Session Management and Checkpointing

Continue (`-c`), resume (`-r <session>`), fork (`--fork-session`), PR linking (`--from-pr <number>`), remote control, teleport (`/teleport`).

Every user prompt creates a checkpoint. Esc+Esc or `/rewind` opens rewind menu: restore code/conversation, restore conversation only, restore code only, summarize from point forward. Checkpoints persist across sessions, cleaned up after 30 days.

## Cost Management

Average: $6/dev/day, $100-200/dev/month with Sonnet. Strategies: `/clear` between tasks, `/compact` with custom instructions, Sonnet for most work, disable unused MCP servers, prefer CLI tools over MCP when available, custom status line for continuous monitoring.

## Connection to OpenClaw

Claude Code and OpenClaw serve complementary roles:
- **OpenClaw:** Persistent partner. Always running, proactive, personality, communications, workspace management, continuity via heartbeats.
- **Claude Code:** Power tool. Deep IDE/terminal/git integration, implementation, debugging, code review.
- **Shared state:** The repo is the bridge. CLAUDE.md conventions defined once, respected by both.

## Related

- [[openclaw]] — Our persistent agent platform
- [[skills-as-portable-knowledge]] — Agent behavior as versioned, composable instructions
- [[agent-native-operations]] — Tools designed for AI-human partnership
- [[browser-automation]] — Browser tools for interactive web tasks
- [[the-openclaw-lesson]] — Lessons from OpenClaw adoption