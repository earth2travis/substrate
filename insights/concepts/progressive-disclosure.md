---
title: "Progressive Disclosure: Context as Architecture"
tags: [concept, agent, context, skills, design, cognition]
related: [[agentic-architecture]], [[skills-as-onboarding]], [[agent-identity]]
source: research/findings/agent-tool-design-lessons.md
---

# Progressive Disclosure: Context as Architecture

## Overview

Progressive disclosure means the agent discovers context incrementally through exploration, rather than having everything front-loaded. This is the most important design principle for agent systems that scale.

## The Evolution

**RAG / vector database**: Context given to the model. Fast but fragile. Requires indexing. The model does not learn to find context itself.

**Grep tool**: Model searches for its own context. Slower but more robust. The model builds skill at finding what it needs.

**Skills with recursive file references**: Nested discovery. A skill file references other files, which reference other files. The model navigates a knowledge graph.

Over time, agents went from "not really being able to build their own context" to "nested search across several layers of files to find exactly what is needed."

## Why This Matters

**Context rot prevention.** If everything is in the system prompt, most of it is irrelevant most of the time. Irrelevant context degrades performance. Progressive disclosure means the model only loads what it needs.

**Scalability.** You can add unlimited capability through files without touching the tool interface. New functionality equals a new file, not a new tool.

**Composability.** Users extend the system by writing files, not code. Skills are user-authored. The SKILL.md file is the extension mechanism.

**Learning to learn.** A model that builds its own context develops research skills. It learns what to search for, how to navigate file structures, when to go deeper. This is qualitatively different from being handed context.

## Design Heuristics

1. **One tool, one semantic purpose.** Do not overload tools with multiple functions.
2. **Match the interface to the model's reasoning.** If the model struggles with a tool, the tool is wrong.
3. **Prefer progressive disclosure over tool proliferation.** Can you solve this with a file instead of a tool?
4. **Audit tools for capability drift.** Yesterday's scaffolding is today's constraint.
5. **Read your outputs.** The model's behavior tells you what it needs. This is empirical, not theoretical.

## The 20 Tool Ceiling

Claude Code maintains approximately 20 tools, and the bar to add new ones is high. More options means more cognitive load, more potential for confusion. The escape hatch: extend capability without extending the tool set by using progressive disclosure. A subagent with specialized instructions is functionally a tool, but it does not increase the tool count in the parent agent's action space.

## Connection to Substrate

Our entire architecture is already a progressive disclosure system:
- `AGENTS.md` points to `SOUL.md`, `USER.md`, `MEMORY.md`
- `MEMORY.md` references daily files in `memory/`
- Skills are `SKILL.md` files referencing scripts, configs, other files
- Research directories are navigated on demand

The question is whether we are doing it well. Are there places where we front-load too much? Are there places where a layer of indirection would improve performance?
