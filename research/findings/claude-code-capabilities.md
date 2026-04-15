---
title: "Claude Code: Complete Capabilities Guide"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/claude-code-capabilities.md
---

# Claude Code: Complete Capabilities Guide

_Research compiled February 24, 2026 for [[Ξ2T]]'s primary development tool._
_Source: https://code.claude.com/docs/_

---

## 1. Complete Feature Inventory

Everything Claude Code can do, organized by capability domain.

### Core Architecture

Claude Code is an agentic coding tool that operates through a three phase loop: gather context, take action, verify results. It runs in your terminal, IDE, desktop app, or browser. The same engine powers every surface, so CLAUDE.md files, settings, and MCP servers work across all of them.

**Available surfaces:** Terminal CLI, VS Code extension, JetBrains plugin, Desktop app (macOS/Windows), Web (claude.ai/code), iOS app, Slack integration, Chrome extension, GitHub Actions, GitLab CI/CD.

**Built in tools fall into five categories:**

- File operations: read, edit, create, rename, reorganize
- Search: find files by pattern, search content with regex, explore codebases
- Execution: run shell commands, start servers, run tests, use git
- Web: search the web, fetch documentation, look up error messages
- Code intelligence: type errors, warnings, jump to definitions (via plugins)

### Memory System

Claude Code has a layered memory hierarchy. This is one of its most powerful features.

| Location                                                                                             | Purpose                                                  | Shared?                |
| ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ---------------------- |
| Managed policy (`/Library/Application Support/ClaudeCode/CLAUDE.md` or `/etc/claude-code/CLAUDE.md`) | Org wide instructions from IT                            | All users              |
| Project memory (`./CLAUDE.md` or `./.claude/CLAUDE.md`)                                              | Team shared project instructions                         | Via source control     |
| Project rules (`./.claude/rules/*.md`)                                                               | Modular, topic specific rules with optional path scoping | Via source control     |
| User memory (`~/.claude/CLAUDE.md`)                                                                  | Personal preferences for all projects                    | Just you               |
| Local project memory (`./CLAUDE.local.md`)                                                           | Personal project preferences (auto gitignored)           | Just you               |
| Auto memory (`~/.claude/projects/<project>/memory/`)                                                 | Claude's automatic notes and learnings                   | Just you (per project) |

**Auto memory** is a new feature where Claude writes its own notes as it works: project patterns, build commands, debugging insights, architecture notes, preferences. Stored at `~/.claude/projects/<project>/memory/MEMORY.md` with optional topic files. First 200 lines of MEMORY.md loaded into system prompt every session. Topic files loaded on demand.

**CLAUDE.md imports:** Files can import others with `@path/to/file` syntax. Supports relative paths, absolute paths, and `~` home paths. Recursive imports up to 5 levels deep. First encounter shows approval dialog.

**Path scoped rules:** Rules in `.claude/rules/` can have YAML frontmatter with `paths` field using glob patterns. Rules only apply when Claude works with matching files. Supports brace expansion (`*.{ts,tsx}`).

**Child directory CLAUDE.md:** Files in subdirectories load on demand when Claude reads files in those directories, not at startup.

### Skills (Custom Slash Commands)

Skills are markdown files with YAML frontmatter stored in `.claude/skills/<name>/SKILL.md`. They create slash commands and can be auto invoked by Claude when relevant.

**Locations:** Enterprise (managed settings), Personal (`~/.claude/skills/`), Project (`.claude/skills/`), Plugin (namespaced).

**Key frontmatter fields:**

- `name`: slash command name
- `description`: helps Claude decide when to use it
- `disable-model-invocation: true`: only user can trigger
- `user-invocable: false`: only Claude can trigger (background knowledge)
- `allowed-tools`: tools allowed without permission when skill is active
- `model`: override model for this skill
- `context: fork`: run in isolated subagent context
- `agent`: which subagent type to use with `context: fork`
- `hooks`: lifecycle hooks scoped to the skill

**String substitutions:** `$ARGUMENTS`, `$ARGUMENTS[N]`, `$N`, `${CLAUDE_SESSION_ID}`.

**Supporting files:** Skills can include templates, examples, scripts in their directory. Reference from SKILL.md so Claude knows when to load them.

**Legacy compatibility:** `.claude/commands/` files still work with the same frontmatter. Skills take precedence if names collide.

### Hooks

Hooks are shell commands or LLM prompts that execute automatically at specific lifecycle points. Defined in JSON settings files.

**Hook events:**

- `SessionStart` / `SessionEnd`
- `UserPromptSubmit` (before Claude processes your prompt)
- `PreToolUse` / `PostToolUse` / `PostToolUseFailure`
- `PermissionRequest`
- `Notification`
- `SubagentStart` / `SubagentStop`
- `Stop` (when Claude finishes responding)
- `TeammateIdle` (agent teams)
- `TaskCompleted`
- `ConfigChange`
- `WorktreeCreate` / `WorktreeRemove`
- `PreCompact`

**Matchers:** Regex patterns that filter when hooks fire. Tool hooks match on tool name, session hooks on start/end reason, etc.

**Hook types:** command (shell), prompt (LLM), agent.

**Decision control:** PreToolUse hooks can return `permissionDecision: "deny"` to block tool calls. Can also return `"allow"` or `"ask"`.

**Hook locations:** User settings, project settings, local settings, managed policy, plugins, skill/agent frontmatter.

### Subagents

Subagents are isolated AI workers that run in their own context windows.

**Built in subagents:**

- **Explore:** Haiku model, read only tools, fast codebase exploration
- **Plan:** Inherits model, read only, used during plan mode
- **General purpose:** Inherits model, all tools, complex multi step tasks
- **Bash:** Terminal commands in separate context
- **Claude Code Guide:** Haiku, answers questions about Claude Code

**Custom subagents:** Defined as markdown files in `.claude/agents/` (project) or `~/.claude/agents/` (user). Also definable via `--agents` CLI flag as JSON.

**Supported frontmatter:** name, description, tools, disallowedTools, model, permissionMode, maxTurns, skills, mcpServers, hooks, memory.

**Key capability:** Subagents can preload skills (`skills:` field), use specific MCP servers, and have their own hooks. They preserve main conversation context by returning only summaries.

### Agent Teams (Experimental)

Multiple Claude Code instances coordinating as a team. One session leads, others work independently with peer to peer messaging and shared task lists.

Enable with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

**Difference from subagents:** Agent teams have inter agent communication. Subagents only report back to caller.

**Best for:** Parallel research, new feature development, debugging with competing hypotheses, cross layer coordination.

**Display modes:** In process (all in one terminal, Shift+Down to cycle) or split pane (each teammate in own tmux pane).

### Plugins and Marketplaces

Plugins bundle skills, agents, hooks, MCP servers, and LSP servers into installable units. Plugin skills are namespaced (`/plugin-name:skill-name`).

**Plugin structure:**

- `.claude-plugin/plugin.json` (manifest)
- `skills/`, `agents/`, `commands/`, `hooks/` directories
- `.mcp.json`, `.lsp.json`, `settings.json` at plugin root

**Marketplaces:** Distributable registries for plugins. Managed settings can restrict marketplace sources.

### MCP (Model Context Protocol)

Open standard for connecting AI tools to external services. Three transport options:

- **HTTP** (recommended for remote): `claude mcp add --transport http <name> <url>`
- **SSE** (deprecated): `claude mcp add --transport sse <name> <url>`
- **Stdio** (local processes): `claude mcp add <name> -- <command> [args...]`

**Scopes:** `local` (you, this project), `project` (shared via `.mcp.json`), `user` (you, all projects).

**Management:** `claude mcp list`, `claude mcp get <name>`, `claude mcp remove <name>`, `/mcp` in session.

**Dynamic tool updates:** Supports MCP `list_changed` notifications for live updates.

**Tool search:** When MCP tool descriptions exceed 10% of context, Claude Code auto defers them and loads on demand.

**Managed MCP:** Admins can use `allowManagedMcpServersOnly` to restrict which servers are available.

### Permissions and Security

**Permission modes:**

- `default`: prompts for permission on first use
- `acceptEdits`: auto accepts file edits for the session
- `plan`: read only analysis mode
- `dontAsk`: auto denies unless pre approved
- `bypassPermissions`: skips all prompts (containers only)

**Permission rules:** `Tool` or `Tool(specifier)` syntax. Supports glob patterns. Evaluated in deny > ask > allow order.

**Sandboxing:** OS level filesystem and network isolation using Seatbelt (macOS) or bubblewrap (Linux). Two modes: auto allow (sandboxed commands run without prompting) and regular (all commands prompted). Enable with `/sandbox`.

**Managed settings:** Organization wide policies that cannot be overridden. Deployable via MDM, server managed settings, or file based configs.

### Programmatic Usage (Agent SDK)

`claude -p "query"` runs non interactively. All CLI flags work.

**Output formats:** text (default), json (structured with metadata), stream-json (real time streaming).

**Structured output:** `--json-schema` returns validated JSON matching a schema.

**Key flags for automation:**

- `--allowedTools`: auto approve specific tools
- `--max-turns`: limit agentic turns
- `--max-budget-usd`: spending cap
- `--append-system-prompt`: add instructions
- `--continue` / `--resume`: session management
- `--fallback-model`: automatic model fallback on overload

**Python and TypeScript SDKs** available for full programmatic control with callbacks, native message objects, and tool approval.

### GitHub Actions and CI/CD

`@claude` mention in PRs/issues triggers Claude Code via GitHub Actions. Can create PRs, implement features, fix bugs, review code.

Setup: `/install-github-app` from Claude Code, or manual workflow file.

GitLab CI/CD also supported.

### Session Management

- **Continue:** `claude -c` or `claude --continue` resumes most recent session
- **Resume:** `claude -r <session>` resumes specific session by ID or name
- **Fork:** `--fork-session` branches off without affecting original
- **PR linking:** Sessions auto link when created via `gh pr create`. Resume with `--from-pr <number>`
- **Remote Control:** Continue local sessions from phone/browser
- **Teleport:** `/teleport` pulls web sessions into terminal

### Checkpointing

Every user prompt creates a checkpoint. Esc+Esc or `/rewind` opens the rewind menu.

**Actions:** Restore code and conversation, restore conversation only, restore code only, summarize from point forward.

Checkpoints persist across sessions, cleaned up after 30 days.

### Model Configuration

**Aliases:** `default`, `sonnet`, `opus`, `haiku`, `sonnet[1m]`, `opusplan`.

**`opusplan`:** Uses Opus for planning, Sonnet for execution. Best of both worlds.

**Effort levels** (Opus 4.6): low, medium, high. Controls adaptive reasoning depth.

**Extended context:** 1M token context window available for Opus 4.6 and Sonnet 4.6.

**Fast mode:** Faster Opus 4.6 responses, togglable.

### Interactive Features

**Keyboard shortcuts:**

- Shift+Tab: toggle permission modes (normal > accept edits > plan)
- Ctrl+G: open prompt in text editor
- Ctrl+O: toggle verbose output
- Esc+Esc: rewind/summarize
- Ctrl+B: background running tasks
- Ctrl+T: toggle task list
- Alt+P: switch model without clearing prompt

**Input modes:** `@` for file references, `!` for bash mode, `/` for commands/skills.

**Image support:** Drag/drop, clipboard paste, or provide path. Works with screenshots, mockups, diagrams.

### Cost Management

Average: $6/dev/day, $100 to $200/dev/month with Sonnet.

**Strategies:**

- `/clear` between tasks to avoid stale context
- `/compact` with custom instructions to guide summarization
- Use Sonnet for most work, Opus for complex reasoning
- Disable unused MCP servers (each adds tool definitions to context)
- Prefer CLI tools over MCP servers when available (less context overhead)
- Custom status line to monitor context usage continuously

### Other Notable Features

- **Chrome integration:** Debug live web apps, test UI, automate forms
- **Slack integration:** `@Claude` in Slack triggers tasks, returns PRs
- **Output styles:** Adapt Claude Code for non engineering uses
- **Custom status line:** Monitor context %, costs, git status via `/statusline`
- **Custom keybindings:** Configure in keybindings config file
- **Development containers:** Consistent team environments
- **OpenTelemetry monitoring:** Enterprise observability
- **LLM gateway support:** Route through LiteLLM, custom proxies
- **Third party providers:** Amazon Bedrock, Google Vertex AI, Microsoft Foundry

---

## 2. What We Already Use

Mapping Claude Code features to our current workflows.

### CLAUDE.md / Memory System → Our AGENTS.md + MEMORY.md

We already do this, but differently. Our AGENTS.md, SOUL.md, and MEMORY.md serve the same purpose as Claude Code's CLAUDE.md hierarchy. Our approach is more personal and identity focused. Claude Code's approach is more structured (project rules, path scoping, auto memory).

**Key difference:** We run through OpenClaw, not Claude Code directly. Our memory files are loaded by OpenClaw's context injection, not by Claude Code's native CLAUDE.md loader.

### Session Management → Our Handoff System

Claude Code has `--continue`, `--resume`, `--fork-session`. We built our own handoff system (`handoffs/YYYYMMDD-HHMM-description.md`) because OpenClaw sessions don't have Claude Code's native session persistence. Our approach is more manual but captures reasoning and emotional context that Claude Code's system doesn't.

### Subagents → OpenClaw Subagents

We already use subagents extensively. OpenClaw spawns them for research, analysis, and parallel work. Claude Code's subagent system is more structured (frontmatter configs, model selection, tool restrictions) but the concept is identical.

### Git Workflow

We follow strict commit discipline: issues first, branches, PRs, conventional commits. Claude Code natively supports `gh pr create`, commit generation, and PR linking. We use this through shell commands already.

### Context Management

We monitor context via `session_status` and follow the 50/60/70/85% protocol. Claude Code offers `/context`, `/cost`, custom status line, and automatic compaction. The principles align; the tooling differs.

---

## 3. What We're Missing

Features we aren't using that would materially help.

### Auto Memory (High Value)

Claude Code can automatically write notes about project patterns, debugging insights, and preferences to `~/.claude/projects/<project>/memory/`. This happens during sessions without explicit instruction. We do manual memory maintenance via heartbeats and daily files. Auto memory would supplement this with zero effort pattern capture.

**Why it matters:** We lose learnings between sessions unless we explicitly write them down. Auto memory captures the stuff we forget to capture.

### Skills System (High Value)

We have no custom slash commands or skills defined. Claude Code skills would let [[Ξ2T]] create:

- `/review` for his PR review checklist
- `/commit` customized to our conventional commit discipline
- `/deploy` for deployment workflows
- Reference skills for API conventions, architecture decisions

Skills with `context: fork` would run in isolated subagents, preserving main context.

### Hooks (Medium Value)

We could automate:

- Prettier on every file edit (`PostToolUse` hook on Edit)
- Lint checks before commits (`PreToolUse` hook on Bash with git commit matcher)
- Notifications on task completion (`Stop` hook)
- Custom compaction behavior (`PreCompact` hook)

### Path Scoped Rules (Medium Value)

`.claude/rules/` with glob patterns would let [[Ξ2T]] define different conventions for different parts of the codebase without bloating a single CLAUDE.md file.

### Plan Mode (Medium Value)

Shift+Tab to toggle into plan mode for safe exploration before implementation. Ctrl+G to edit plans in a text editor. We don't use this structured approach; we should.

### Checkpointing and Rewind (Medium Value)

Esc+Esc to rewind to any previous prompt. Summarize from a point forward to free context without losing everything. We don't have this in OpenClaw.

### `opusplan` Model Mode (Low/Medium Value)

Automatic Opus for planning, Sonnet for execution. Optimizes cost without sacrificing reasoning quality for architecture decisions.

### GitHub Actions Integration (Low Value for Now)

`@claude` in PRs for automated review. We don't have CI/CD set up on the repo yet, but when we do, this would be powerful.

### Sandboxing (Low Value for Us)

We're on a VPS with controlled access. Sandboxing matters more for local development on personal machines. Still, enabling it would add defense in depth.

### Agent Teams (Experimental, Future Value)

Multiple Claude instances collaborating on a task with peer to peer communication. Still experimental, but the research/debugging use case is compelling.

---

## 4. Immediate Recommendations

Things to adopt now, ordered by impact.

### 1. Create a CLAUDE.md for the Repo

Even though we run through OpenClaw, [[Ξ2T]] uses Claude Code directly too. A `CLAUDE.md` in the repo root would give Claude Code sessions instant context about our conventions, commit discipline, and project structure. Keep it under 500 lines. Import `@README.md` and `@AGENTS.md` for detail.

### 2. Define Core Skills

Start with three skills in `.claude/skills/`:

**`commit/SKILL.md`**: Our conventional commit workflow. Reference issue, run prettier, stage only intended files, use correct prefix. Set `disable-model-invocation: true` so it only runs when explicitly invoked.

**`review/SKILL.md`**: PR review checklist matching our templates. Check that issue is referenced, deliverables are checked off, correct template is used.

**`research/SKILL.md`**: Template for research tasks. Create research file, structure findings, commit to branch, create PR. This formalizes what we do ad hoc.

### 3. Set Up Project Rules

Create `.claude/rules/` with:

- `git-workflow.md`: Our branch protection, PR template, and commit rules
- `writing-style.md` (with `paths: ["reports/**", "research/**", "SOUL.md"]`): No dashes, no citing influences, write like a human
- `memory-files.md` (with `paths: ["memory/**", "MEMORY.md"]`): How to handle memory updates

### 4. Enable Auto Memory

Set `CLAUDE_CODE_DISABLE_AUTO_MEMORY=0` to force it on. This gives [[Ξ2T]] automatic pattern capture during Claude Code sessions. Zero effort, immediate value.

### 5. Use Plan Mode for Complex Work

Before jumping into implementation, toggle Shift+Tab into plan mode. Explore the codebase, create a plan, edit it with Ctrl+G, then switch back to normal mode. This maps perfectly to the "explore first, then plan, then code" pattern in the best practices.

### 6. Set Up a Status Line

`/statusline` to configure context window % display. Monitor context usage continuously instead of checking `session_status` manually.

---

## 5. Comparison with Our OpenClaw Setup

### What Overlaps

| Capability          | OpenClaw                               | Claude Code                      |
| ------------------- | -------------------------------------- | -------------------------------- |
| Chat interface      | Telegram bot                           | Terminal/IDE/Desktop/Web         |
| Memory files        | AGENTS.md, MEMORY.md, daily notes      | CLAUDE.md hierarchy, auto memory |
| Subagents           | OpenClaw spawned subagents             | Built in subagents with configs  |
| Tool access         | Read, Write, Edit, Exec, Browser, etc. | Read, Edit, Bash, WebFetch, etc. |
| Context management  | session_status monitoring              | /context, status line, /compact  |
| Session persistence | Heartbeats, handoffs                   | Native session resume/fork       |

### What's Different

**OpenClaw gives us things Claude Code doesn't:**

- Telegram as a conversational interface (mobile accessible, async)
- Persistent identity across sessions (SOUL.md, personality, relationships)
- Heartbeat system for proactive behavior (email, calendar, mentions)
- Multi channel presence (Telegram, potential Discord/Slack)
- Node pairing for camera, screen, location on physical devices
- Canvas for UI rendering
- TTS for voice output
- Always on daemon (systemd service, not interactive sessions)

**Claude Code gives us things OpenClaw doesn't (natively):**

- CLAUDE.md hierarchy with path scoping and auto discovery
- Skills/slash commands with frontmatter configuration
- Hooks for lifecycle automation
- MCP for external service integration
- Checkpointing and rewind
- Plan mode for safe exploration
- Sandboxing for security isolation
- Agent teams for parallel coordination
- GitHub Actions integration for CI/CD
- Chrome integration for web debugging
- Structured programmatic output (JSON schemas)
- Native IDE integration (VS Code, JetBrains)

### What's Complementary

The two systems serve different roles:

**OpenClaw is the persistent partner.** It's [[Sivart]]'s home. Always running, proactive, has personality, handles communications, manages the workspace, maintains continuity through heartbeats and memory files. It's the relationship layer.

**Claude Code is the power tool.** When [[Ξ2T]] sits down to write code, Claude Code is the hands on coding assistant. It has deeper integration with the development workflow: IDE, terminal, git, testing, debugging. It's the craftsmanship layer.

**They don't compete; they compose.** OpenClaw manages the workspace, creates issues, does research, handles communications. Claude Code implements the code, reviews PRs, debugs problems. The CLAUDE.md file in the repo bridges them: conventions defined once, respected by both systems.

**The bridge:** When [[Ξ2T]] asks [[Sivart]] (via OpenClaw) to do coding work, [[Sivart]] uses shell commands and file operations that accomplish the same things Claude Code would. When [[Ξ2T]] uses Claude Code directly, the `.claude/` directory skills and rules ensure consistent behavior. The repo is the shared state.

### The Centaur Stack

This is exactly the centaur chess principle in action. The stack is:

1. **[[Ξ2T]]** (human): intention, direction, taste, final judgment
2. **[[Sivart]]/OpenClaw** (persistent agent): continuity, communications, research, project management, proactive support
3. **Claude Code** (power tool): implementation, debugging, code review, testing

Better process beats everything. The process here is: define conventions once (CLAUDE.md, skills, rules), maintain them in version control, and let both agent systems read from the same source of truth.
