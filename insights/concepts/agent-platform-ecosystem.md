---
title: "Agent Platform Ecosystem"
tags: [concept, agents, platforms, openclaw, hermes, claude-code, gateway, specialist]
related: [[openclaw]], [[coding-vs-research-platforms]], [[claude-code-capabilities]], [[browser-automation]], [[skills-as-portable-knowledge]], [[agent-native-operations]], [[the-openclaw-lesson]]
source: insights/concepts/agent-platform-ecosystem.md
---

# Agent Platform Ecosystem

## Thesis

No single agent platform serves all needs. The optimal architecture is a **gateway/specialist split**: a persistent orchestrator (OpenClaw) managing channels, communications, and project state; paired with specialized runtimes (Hermes, Claude Code) handling deep coding, research, and verification tasks. The two systems don't compete; they compose around a shared source of truth.

## The Platform Landscape

### OpenClaw: The Persistent Partner

**Role:** Executive/Gateway. Always running, proactive, maintains personality and relationships.

**Strengths:**
- Multi-channel presence (Telegram, Slack, Discord)
- Heartbeat system for proactive behavior (email, calendar, mentions)
- Persistent identity across sessions (SOUL.md, personality, relationships)
- Multi-agent orchestration (HighClaw, ClawHub with 5,700+ skills)
- Canvas for UI rendering, TTS for voice output
- Always-on daemon (systemd service)

**Weaknesses:**
- Static "Workspace" — requires manual skill writing and updating
- Slower execution than Python-native runtimes
- Single-agent loop for deep work

### Hermes: The Technical Specialist

**Role:** Deep worker. Self-improving, fast, autonomy-focused.

**Strengths:**
- **The Learning Loop:** Extracts reusable patterns after every 10-15 tasks. Remembers the "best way" to structure repeated work.
- **Procedural Memory:** Converts successful workflows into "skills" automatically. Reduces tool calls from ~15 to ~3 for repeated tasks.
- **Fast Execution:** Python-native runtime, tighter tool integration. Community benchmarks report 40% faster coding.
- **Automatic Skill Extraction:** Research tasks produce reusable skills without manual curation.

**Weaknesses:**
- Primarily single-agent — limited multi-agent orchestration
- Autonomy can be a "double-edged sword" for compliance requirements
- Smaller ecosystem than OpenClaw's ClawHub

### Claude Code: The Power Tool

**Role:** Craftsmanship layer. Deep IDE/terminal/git integration for implementation.

**Strengths:**
- Native IDE integration (VS Code, JetBrains)
- Checkpointing and rewind (Esc+Esc to any previous prompt)
- Plan mode for safe exploration (Shift+Tab)
- Skills system with frontmatter configuration
- Hooks for lifecycle automation
- MCP for external service integration
- Sandboxing for security isolation
- GitHub Actions integration for CI/CD

**Weaknesses:**
- No persistent identity across sessions
- No proactive behavior (heartbeats, email monitoring)
- Limited multi-channel presence
- Interactive sessions only (no always-on daemon)

## The "Workspace" vs. "Skills" Philosophy

- **OpenClaw (Workspace):** You are the **Architect**. You build the room, place the tools, and the agent lives there. Predictable and safe, but requires labor to evolve.
- **Hermes (Skills):** You are the **Mentor**. You give the agent a task, and it builds its own tools as it goes. Adaptive and fast, but you must trust its judgment.
- **Claude Code (Power Tool):** You are the **Craftsperson**. You pick up the tool when you need deep work, then put it down. No persistence, no overhead, pure execution.

## The Optimal Split

The current setup — **Sivart on OpenClaw** and **Koda on Hermes** — maps to the optimal architecture:

- **Sivart (OpenClaw):** Executive/Gateway. Manages channels, handles the human interface, uses ClawHub ecosystem for broad research, maintains continuity through heartbeats and memory files.
- **Koda (Hermes):** Technical Specialist. Uses the self-improving loop to master coding and harness engineering tasks requiring deep, repetitive learning.
- **Claude Code (ad hoc):** Power tool for Ξ2T's direct coding sessions. Bridges via repo conventions (CLAUDE.md, skills, rules) that both systems respect.

## The Centaur Stack

This is the centaur chess principle in action:

1. **Ξ2T (human):** Intention, direction, taste, final judgment
2. **Sivart/OpenClaw (persistent agent):** Continuity, communications, research, project management, proactive support
3. **Koda/Hermes (specialist):** Deep coding, research, skill extraction, autonomous learning
4. **Claude Code (power tool):** Implementation, debugging, code review, testing

Better process beats everything. The process: define conventions once (CLAUDE.md, skills, rules), maintain them in version control, let both agent systems read from the same source of truth.

## Connection to Agent Factory

The Agent Factory doesn't need to choose one platform. It needs to:
1. **Define the interface between gateway and specialist** (what gets delegated, how results are returned)
2. **Maintain shared conventions** in version control (repo is the source of truth)
3. **Measure each platform's contribution** (coding speed, research depth, channel coverage)
4. **Evolve the split as capabilities change** (what Hermes learns, OpenClaw should eventually adopt)

## Related

- [[openclaw]] — Our persistent agent platform
- [[coding-vs-research-platforms]] — Detailed comparison of OpenClaw vs Hermes
- [[claude-code-capabilities]] — Claude Code's feature inventory
- [[browser-automation]] — Browser tools for interactive web tasks
- [[skills-as-portable-knowledge]] — Agent behavior as versioned, composable instructions
- [[agent-native-operations]] — Tools designed for AI-human partnership
- [[the-openclaw-lesson]] — Lessons from OpenClaw adoption