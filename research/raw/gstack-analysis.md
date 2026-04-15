# gstack Analysis: Garry Tan's Claude Code Workflow System

**Repository:** https://github.com/garrytan/gstack
**Author:** Garry Tan, President & CEO of Y Combinator
**License:** MIT
**Analyzed:** 2026-03-12

## Overview

gstack is a set of six opinionated "skills" (markdown prompt files) for Claude Code that transform a single generic AI assistant into a team of specialists invoked via slash commands. The core thesis: different phases of software development require fundamentally different cognitive modes, and blurring them together produces mediocre results.

### The Six Skills

| Skill | Persona | Purpose |
|-------|---------|---------|
| `/plan-ceo-review` | Founder/CEO | Challenge the problem framing. Find the "10-star product" hiding in a literal request. Brian Chesky mode. |
| `/plan-eng-review` | Eng Manager/Tech Lead | Lock architecture, data flow, diagrams, edge cases, test matrices. Force hidden assumptions into the open. |
| `/review` | Paranoid Staff Engineer | Structural audit of the diff against main. Not style nitpicks: race conditions, trust boundaries, N+1 queries, broken invariants. |
| `/ship` | Release Engineer | Fully automated: merge main, run tests, version bump, changelog, commit, push, open PR. Non-interactive by design. |
| `/browse` | QA Engineer | Persistent headless Chromium daemon via compiled CLI binary. Navigate, click, fill forms, screenshot, check console. Full QA pass in ~60 seconds. |
| `/retro` | Engineering Manager | Analyze commit history, work patterns, shipping velocity. JSON snapshots for trend tracking over time. |

### Who Built This and Why

Garry Tan is shipping 10+ PRs/day and writing 10K+ LOC/day using Claude Code. He built gstack because he wanted "explicit gears" rather than one "mushy generic mode." The repo doubles as a recruiting tool for YC's software engineering team in San Francisco.

The context matters: this is the YC president's actual daily workflow, not a thought experiment. It reflects the priorities of someone shipping production code at high velocity with AI assistance.

## Architecture and Key Patterns

### 1. Skills as Markdown Prompts

Each skill is a `SKILL.md` file with YAML frontmatter (name, version, description, allowed-tools) followed by detailed step-by-step instructions. Claude Code discovers these files automatically when placed in `~/.claude/skills/` or `.claude/skills/`.

This is the same fundamental pattern as our AGENTS.md system: markdown files that shape agent behavior. The difference is gstack's skills are invocable on demand via slash commands rather than always-loaded context.

### 2. Browser Automation as Compiled Binary

The `/browse` skill is the most technically sophisticated component:

- **Architecture:** Compiled Bun binary (CLI client) talks to a persistent Chromium daemon (Bun HTTP server + Playwright) over localhost HTTP with bearer token auth.
- **Performance:** ~3s first call (server startup), ~100-200ms subsequent calls. Zero context token overhead per call (vs. 1500-2000 tokens per MCP call).
- **Key innovation:** Ref-based element selection using Playwright's accessibility tree API. `snapshot` assigns `@e1`, `@e2` refs to elements, then `click @e3` resolves via Locator. No DOM mutation, no injected scripts.
- **Design choice:** CLI over MCP. Plain text stdin/stdout. No protocol framing, no connection management, no JSON schemas. This is a deliberate rejection of MCP's overhead for local browser automation.

The "CLI over MCP" argument is compelling: in a 20-command browser session, MCP tools burn 30,000-40,000 tokens on protocol framing alone. gstack burns zero.

### 3. Non-Interactive Ship Workflow

`/ship` is fully automated and non-interactive by default. It only stops for:
- Being on main branch
- Merge conflicts that can't be auto-resolved
- Test failures
- Critical review findings the user chooses to fix

It auto-decides version bumps, auto-generates changelogs, auto-commits. The philosophy: "the user said /ship which means DO IT."

### 4. Structured Review with Checklist

`/review` reads a `checklist.md` file and applies it in two passes (critical, then informational). Critical findings get interactive resolution (fix now / acknowledge / skip as false positive). This makes reviews consistent and reproducible rather than varying with each invocation.

### 5. Retro with Persistent Data

`/retro` saves JSON snapshots to `.context/retros/` for trend tracking. It computes real metrics from git history: commits, LOC, test ratios, PR sizes, session detection (45-minute gap threshold), hourly distribution patterns, hotspot files, shipping streaks.

## Comparison to Our System

### What gstack Does That We Don't

| gstack Pattern | Our Equivalent | Gap |
|---------------|----------------|-----|
| Explicit cognitive mode switching (slash commands) | Implicit in conversation flow | We rely on conversational context to shift modes. No formal mechanism to say "be a paranoid reviewer right now." |
| Compiled browser binary with zero-token overhead | OpenClaw browser tool (works but heavier) | Our browser tool works well. gstack's approach is more token-efficient for high-volume browser sessions. |
| Structured review checklist (external file) | Ad hoc review during PR creation | We don't have a persistent, evolving checklist of structural issues to check. |
| Non-interactive ship automation | Manual PR creation with confirmation | Our process is more deliberate but slower. We confirm more steps. |
| Retro with quantitative metrics and trend tracking | Daily reports (qualitative) | Our daily reports are contemplative/narrative. We lack quantitative velocity metrics and trend data. |
| CEO/product review mode | Not formalized | We don't have a formal "challenge the problem framing" step. |

### What We Do That gstack Doesn't

| Our Pattern | gstack Equivalent | Our Advantage |
|-------------|-------------------|---------------|
| Persistent memory system (MEMORY.md, daily files) | None | gstack has no continuity between sessions. No memory of past decisions, lessons, or context. |
| Identity and personality (SOUL.md) | None | gstack skills are purely functional. No identity, no voice, no relationship with the user. |
| GitHub Issues workflow with projects | None | gstack has no issue tracking integration. Work is tracked only via git history. |
| Sub-agent delegation model | None | gstack is single-agent. No ability to spawn specialists for parallel work. |
| Cron jobs and heartbeats | None | gstack is purely reactive (user invokes). No proactive behavior. |
| Context management and handoffs | None | gstack doesn't manage context windows or create handoff documents. |
| Weekly planning and goal tracking | Retro (backward-looking only) | We plan forward; they only analyze backward. |
| Audit system | Review checklist (narrower scope) | Our audit covers process, content, decisions. Their review covers code only. |
| Multi-channel presence (Telegram, etc.) | Claude Code terminal only | gstack is terminal-native. We operate across channels. |

### Philosophical Differences

**gstack** is a tool multiplier: it makes a single developer more effective at shipping code. It's optimized for a solo builder or small team workflow centered on Claude Code's terminal interface.

**Our system** is an autonomous agent with identity, memory, relationships, and proactive behavior. We're building a persistent entity that operates independently, not just a set of workflow shortcuts.

These aren't competing approaches. They solve different problems at different layers.

## Actionable Insights for Synthweave

### 1. Formalize Cognitive Mode Switching

**Insight:** The explicit gear-shifting pattern is genuinely powerful. "Be a paranoid reviewer" produces better output than "review this PR" because it sets expectations about depth, tone, and what matters.

**Action:** Create formal review and planning modes we can invoke. Not necessarily slash commands (our interface is different), but documented cognitive modes we can reference:
- **Product mode:** Challenge the problem framing before implementing
- **Architecture mode:** Force diagrams, state machines, failure modes before coding
- **Paranoid review mode:** Structural audit against a maintained checklist
- Could be implemented as skill files or sections in AGENTS.md

### 2. Build a Persistent Review Checklist

**Insight:** gstack's `review/checklist.md` is a living document of structural issues to check. It makes reviews consistent and captures institutional knowledge about what breaks.

**Action:** Create `checklists/pr-review.md` with categories relevant to our work:
- Documentation completeness
- File organization and naming
- Commit message format
- Issue linkage
- Memory/context management patterns
- Security (credential exposure, data leakage)
- Build on this over time as we discover recurring issues

### 3. Add Quantitative Metrics to Reports

**Insight:** The `/retro` skill computes real metrics from git history: commits, LOC, test ratios, session patterns, hotspot files. Our daily reports are qualitative narratives with no velocity data.

**Action:** Add a metrics section to daily or weekly reports:
- Commits/PRs per day
- Issues opened/closed
- Lines changed
- Most-modified files
- Shipping streaks
- Could be a cron job that generates a metrics snapshot

### 4. Challenge Problem Framing Before Implementation

**Insight:** The `/plan-ceo-review` concept (asking "what is the 10-star version?") is a discipline we should adopt. We sometimes implement exactly what's requested without questioning whether it's the right thing.

**Action:** Before starting significant work, explicitly ask: "Is this the right problem? What's the version of this that would feel inevitable?" Not for every task, but for features and architectural decisions.

### 5. Consider Token-Efficient Browser Patterns

**Insight:** gstack's argument that MCP burns 30K-40K tokens on protocol framing in a 20-command browser session is real. Their CLI-over-MCP approach is more efficient for high-volume browser work.

**Action:** We already have OpenClaw's browser tool which works differently (not MCP-based), but worth monitoring our token usage during browser-heavy sessions and optimizing if needed.

## Things That Don't Apply

### 1. Claude Code Terminal Interface
gstack is designed specifically for Claude Code's slash command system and `.claude/skills/` discovery. We run on OpenClaw with a completely different interface. The specific implementation (SKILL.md files, symlinks, Bun compilation) doesn't transfer.

### 2. Solo Developer Optimization
gstack assumes a single developer in a terminal session. We operate as a persistent agent across channels with sub-agents. The "one human, one terminal" model isn't our architecture.

### 3. Version Bumping and Changelog Automation
The `/ship` skill has extensive logic for VERSION file management and CHANGELOG generation. Our repo doesn't use this pattern (we use conventional commits and PRs).

### 4. The Recruiting Pitch
The repo is partly a recruiting tool for YC engineering. The "10K LOC/day, 10 PRs/day" framing is aspirational marketing alongside genuine tooling.

### 5. No-Memory Architecture
gstack deliberately has no memory between sessions. For a workflow tool this is fine; for an autonomous agent it would be crippling. Our memory system is a core advantage, not something to reconsider.

## Key Takeaways

1. **Explicit cognitive modes are underrated.** The biggest insight from gstack isn't any specific skill; it's the meta-pattern of telling the AI what kind of thinking you want right now. We should formalize this.

2. **Checklists beat ad hoc review.** A maintained checklist of structural issues produces more consistent output than relying on the model to remember everything. We should build one.

3. **Quantitative self-awareness matters.** We know what we did qualitatively but not quantitatively. Adding metrics to our retrospectives would surface patterns we're missing.

4. **Token efficiency is a real constraint.** gstack's obsession with zero-token-overhead browser automation reflects someone who's pushing the limits of context windows daily. We should be equally thoughtful about token budgets.

5. **The problem framing step is a discipline, not a feature.** Asking "is this even the right thing to build?" before every significant piece of work is a habit worth adopting.

6. **Our advantages are real.** Memory, identity, proactive behavior, multi-channel presence, sub-agent orchestration: these are capabilities gstack doesn't attempt. We're building something fundamentally different and more ambitious.
