---
title: Hermes Agent Platform — Deep Research Report
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/hermes-agent-report.md
---

# Hermes Agent Platform — Deep Research Report

> **Date:** 2026-04-11
> **Version inspected:** v0.7.0 (2026.4.3)
> **Scope:** Architecture, capabilities, development velocity, competitive landscape

## What It Is

Hermes Agent is an open-source (MIT license), **self-improving AI agent platform** built by **Nous Research** — the same organization famous for the Hermes model family. The current version is v0.7.0, running on an active development cadence of multiple commits per day.

### Origin

Hermes evolved from **OpenClaw** (originally by Steve Tigue/llmstxt.org). The codebase includes a full `hermes claw migrate` command that imports SOUL.md, memories, skills, API keys, and messaging settings from OpenClaw. The project was adopted by Nous Research and has since grown far beyond its origins into a comprehensive agent runtime with genuine learning capabilities.

## Architecture

The codebase contains 40+ tools across a clean, well-documented architecture:

```
hermes-agent/
├── run_agent.py              # Core AIAgent conversation loop
├── model_tools.py            # Tool orchestration, _discover_tools()
├── cli.py                    # Interactive CLI with Rich TUI
├── hermes_state.py           # SQLite session store with FTS5 search
├── agent/
│   ├── prompt_builder.py     # System prompt assembly
│   ├── context_compressor.py # Auto context compression
│   ├── prompt_caching.py     # Anthropic prompt caching
│   ├── auxiliary_client.py   # Auxiliary LLM (vision, summarization)
│   ├── model_metadata.py     # Model context lengths, token estimation
│   ├── models_dev.py         # models.dev registry integration
│   ├── display.py            # KawaiiSpinner, tool preview formatting
│   ├── skill_commands.py     # Skill slash commands (shared CLI/gateway)
│   └── trajectory.py         # Trajectory saving helpers
├── hermes_cli/
│   ├── main.py               # Entry point for all `hermes` subcommands
│   ├── config.py             # DEFAULT_CONFIG, OPTIONAL_ENV_VARS, migration
│   ├── commands.py           # Central COMMAND_REGISTRY for all slash commands
│   ├── callbacks.py          # Terminal callbacks (clarify, sudo, approval)
│   ├── setup.py              # Interactive setup wizard
│   ├── skin_engine.py        # Full theming/skin system
│   ├── skills_config.py      # Per-platform skill enablement
│   ├── tools_config.py       # Per-platform tool enablement
│   ├── skills_hub.py         # /skills slash command
│   ├── models.py             # Model catalog, provider model lists
│   ├── model_switch.py       # Shared /model switch pipeline
│   └── auth.py               # Provider credential resolution
├── tools/
│   ├── registry.py           # Central tool registry
│   ├── approval.py           # Dangerous command detection
│   ├── terminal_tool.py      # Terminal orchestration
│   ├── process_registry.py   # Background process management
│   ├── file_tools.py         # File read/write/search/patch
│   ├── web_tools.py          # Web search/extraction
│   ├── browser_tool.py       # Browserbase browser automation
│   ├── code_execution_tool.py # execute_code sandbox
│   ├── delegate_tool.py      # Subagent spawning
│   ├── mcp_tool.py           # Full MCP client (~1050 lines)
│   └── environments/         # 6 terminal backends
├── gateway/
│   ├── run.py                # Main loop, slash commands, message dispatch
│   ├── session.py            # SessionStore — conversation persistence
│   └── platforms/            # Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant
├── acp_adapter/              # VS Code / Zed / JetBrains integration
├── cron/                     # Built-in scheduler (jobs.py, scheduler.py)
├── environments/             # Atropos RL training environments
├── tests/                    # ~3000 tests
└── batch_runner.py           # Parallel batch processing
```

**Key configs:** `~/.hermes/config.yaml` (settings), `~/.hermes/.env` (API keys)

### File Dependency Chain

The codebase follows a clean import hierarchy:

```
tools/registry.py  (no deps — imported by all tool files)
       ↑
tools/*.py  (each calls registry.register() at import time)
       ↑
model_tools.py  (imports tools/registry + triggers tool discovery)
       ↑
run_agent.py, cli.py, batch_runner.py, environments/
```

### Central Command Registry Pattern

All slash commands are defined in a central `COMMAND_REGISTRY` list of `CommandDef` objects. Every downstream consumer derives from this registry automatically:

- **CLI** — `process_command()` resolves aliases via `resolve_command()`
- **Gateway** — `GATEWAY_KNOWN_COMMANDS` frozenset for hook emission
- **Gateway help** — `gateway_help_lines()` generates `/help` output
- **Telegram** — `telegram_bot_commands()` generates the BotCommand menu
- **Slack** — `slack_subcommand_map()` generates `/hermes` subcommand routing
- **Autocomplete** — `COMMANDS` flat dict feeds `SlashCommandCompleter`
- **CLI help** — `COMMANDS_BY_CATEGORY` dict feeds `show_help()`

### Agent Loop

The core loop is inside `run_conversation()` — entirely synchronous:

```python
while api_call_count < self.max_iterations and self.iteration_budget.remaining > 0:
    response = client.chat.completions.create(model=model, messages=messages, tools=tool_schemas)
    if response.tool_calls:
        for tool_call in response.tool_calls:
            result = handle_function_call(tool_call.name, tool_call.args, task_id)
            messages.append(tool_result_message(result))
        api_call_count += 1
    else:
        return response.content
```

Messages follow OpenAI format with reasoning content stored in `assistant_msg["reasoning"]`.

## The Six Feature Pillars

### 1. Self-Improving Memory Loop

- **Persistent memory** across sessions — saves facts, preferences, corrections, environment details
- **Autonomous skill creation** — after complex tasks (5+ tool calls), the agent offers to save workflows as reusable skills
- **Skills self-improve during use** — if a loaded skill is wrong or outdated, it patches itself via `skill_manage(action='patch')`
- **FTS5 session search** with LLM summarization — searches past conversations across all sessions, not just keywords but semantic recall
- **Honcho integration** — opt-in dialectic user modeling for deeper understanding
- **Compatible with agentskills.io** open standard

### 2. Massive Tool Ecosystem (40+ tools)

- Terminal execution with 6 backend environments
- File operations (read, write, search, patch with fuzzy matching)
- Web extraction and browser automation (Browserbase)
- Subagent delegation with parallel execution
- Execute-code Python sandbox for programmatic tool calling
- Full MCP (Model Context Protocol) client — connect any MCP server
- Cron scheduling with natural language prompts
- Text-to-speech and vision analysis
- Dangerous command approval system for safety
- Background process management (list, poll, log, wait, kill, write, submit)
- Image generation via FLUX 2 Pro with 2x upscaling

### 3. Six Terminal Backends — Runs Anywhere

| Backend | Use Case | Persistence |
|---------|----------|-------------|
| **Local** | Direct machine access | Session-based |
| **Docker** | Containerized isolation | Session-based |
| **SSH** | Remote machine access | Session-based |
| **Daytona** | Serverless with hibernation | Serverless |
| **Modal** | Serverless GPU-capable | Serverless |
| **Singularity** | HPC environments | Session-based |

This means it can run on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle.

### 4. Multi-Platform Gateway

A single gateway process powers:

- Telegram
- Discord
- Slack
- WhatsApp
- Signal
- Home Assistant

All with conversation continuity across platforms, voice memo transcription, and cross-platform conversation history. Slash commands work identically everywhere.

### 5. Model Agnostic — No Lock-In

Supports:

- OpenRouter (200+ models)
- Nous Portal
- z.ai/GLM
- Kimi/Moonshot
- MiniMax
- OpenAI
- Anthropic
- Any custom endpoint

Switch with `hermes model` — no code changes.

### 6. Research Infrastructure

- Batch trajectory generation for training data
- Atropos RL environments for reinforcement learning
- Trajectory compression for training next-gen tool-calling models
- Integration with tinker-atropos submodule for RL fine-tuning
- Support for GRPO, DPO, and other RL training methods

## CLI Architecture Details

### Skin Engine

The `hermes_cli/skin_engine.py` provides a data-driven CLI theming system:

- Initialized from `display.skin` config key at startup
- Skins customize: banner colors, spinner faces/verbs/wings, tool prefix, response box, branding text
- Recently made fully skin-aware across all CLI elements

### Prompt Assembly

- System prompt assembled dynamically from: core prompt + memory + skills + context files + conversation history
- Skills injected as **user message** (not system prompt) to preserve Anthropic prompt caching
- Context compressor available for long conversations

### Command Approval System

- Dangerous command detection via `tools/approval.py`
- Pattern-based matching for risky operations
- Gateway-level blocking for messaging platforms
- Session-scoped and user-scoped approval patterns

## Recent Development Activity (Last 30 Commits)

The git log shows extremely active development with real features shipping:

| Commit | Change |
|--------|--------|
| `af9caec4` | fix(qwen): correct context lengths for qwen3-coder models |
| `f4592140` | **feat**: background process monitoring — watch_patterns for real-time output alerts |
| `a2f9f04c` | fix: honor session-scoped gateway model overrides |
| `671d5068` | fix: add gpt-5.4 and gpt-5.4-mini to openai-codex curated model list |
| `50ad66ae` | test(tools): add unit tests for budget_config module |
| `80d82c2f` | test(tools): add unit tests for tool_backend_helpers module |
| `4e56eacd` | fix(vision): reject oversized images before API call, handle file:// URIs |
| `30769768` | fix: prevent zombie processes, redact cron stderr, skip symlinks in skill enumeration |
| `4d1f1dcc` | fix: normalize numeric MCP server names to str |
| `640441b8` | **feat(tools)**: add Voxtral TTS provider (Mistral AI) |
| `58b62e3e` | **feat(skin)**: make all CLI colors skin-aware |
| `d9f53dba` | **feat(honcho)**: add opt-in initOnSessionStart for tools mode |

Plus numerous auxiliary client hardening fixes, provider alignment updates, and test isolation improvements.

**This is not a dead project — it's multiple commits per day with a strong focus on quality** (test isolation, approval security, edge-case handling).

## Competitive Landscape

| Feature | Claude Code | Cursor | OpenClaw | Hermes |
|---------|------------|--------|----------|--------|
| Self-improving skills | No | No | Partial | Yes |
| Cross-session memory | Minimal | No | Yes | Yes + FTS5 |
| Multi-platform messaging | No | No | Yes | Yes + HA |
| RL training integration | No | No | No | Yes (Atropos) |
| Terminal backends | 1 | 1 | 2 | 6 |
| MCP client | No | No | Yes | Full (~1050 lines) |
| Serverless hibernation | No | No | No | Yes (Modal/Daytona) |
| Skin/theming | No | No | No | Yes |
| Model lock-in | Anthropic | OpenAI | None | None |
| Open source | No | No | Partial | Yes (MIT) |
| Test coverage | Unknown | Unknown | Unknown | ~3000 tests |

## Technical Depth: Key Design Decisions

### 1. Synchronous Agent Loop

Unlike many agent frameworks that use async, Hermes uses a synchronous loop. This simplifies reasoning about state, makes debugging easier, and avoids the complexity of async tool orchestration.

### 2. SQLite with FTS5

Session storage uses SQLite with Full-Text Search (FTS5) extension. This provides:
- Fast text search across all past conversations
- No external database dependency
- LLM summarization for semantic recall
- Portable across all backend environments

### 3. Tool Registry Pattern

Each tool file calls `registry.register()` at import time. This creates a self-documenting, self-registering tool system where:
- Adding a new tool requires only creating a file and calling register()
- Tool schemas are auto-discovered
- The central registry handles dispatch and validation

### 4. Context File Injection

Context files in project directories are automatically loaded and injected as user messages to preserve prompt caching while giving the agent project awareness.

## Community & Ecosystem

- **Discord:** [Nous Research Discord](https://discord.gg/NousResearch) — main community hub
- **Documentation:** [hermes-agent.nousresearch.com/docs/](https://hermes-agent.nousresearch.com/docs/) — comprehensive documentation
- **Skills Hub:** Built-in skills hub with install/search/browse capabilities
- **Agent Skills:** Compatible with [agentskills.io](https://agentskills.io) open standard
- **Migration path:** Full OpenClaw migration tool for existing users
- **Contributor guide:** Clean dev setup with uv, ~3000 tests, clear file dependency chain

## Honest Assessment

### Strengths

- **Only agent with a genuine closed learning loop** — the combination of memory, autonomous skill creation, skill self-improvement, and session search creates a system that genuinely gets better over time
- **Extremely well-architected** for an open-source project — clean dependency chains, central registry pattern, comprehensive test suite
- **Nous Research's ML expertise** shows in the RL infrastructure and trajectory generation capabilities
- **Model-agnostic design** is refreshing in a landscape dominated by vendor lock-in
- **Runs on anything** from a $5 VPS to Modal GPU clusters
- **Active, committed development** with multiple commits per day
- **Migration-friendly** — the OpenClaw migration path reduces switching costs
- **Comprehensive tool ecosystem** with 40+ tools covering most agent needs

### Potential Concerns

- **Still relatively new** compared to established players like Claude Code
- **Complex setup** for full feature set — gateway, skills, platforms require configuration
- **Voice dependency friction** — Termux needs special `.[termux]` extra due to incompatible voice dependencies
- **No native Windows support** — requires WSL2
- **Cloud sandbox limitations** — persistent filesystem but not guaranteed always-on machine

## Future Trajectory

Based on the development velocity and feature set, Hermes appears positioned to become:

1. **A training data engine** — the trajectory generation and compression capabilities suggest Nous plans to use Hermes interaction data to train better tool-calling models
2. **A universal agent runtime** — the model-agnostic design and multiple backends could make it the "Linux" of AI agents
3. **A learning platform** — the closed loop of experience → skill → memory → better performance is genuinely novel
4. **An RL research platform** — the Atropos environments provide a real testbed for agent optimization

## Conclusion

Hermes Agent is the most ambitious open-source agent platform currently available. It's not just another Claude Code wrapper — it's a complete agent runtime with genuine learning capabilities, production-grade architecture, and the research infrastructure to train better tool-calling models from its own trajectories.

The combination of Nous Research's expertise, daily commit velocity, and the closed learning loop architecture suggests this could become a foundational piece of AI infrastructure in the coming years.
