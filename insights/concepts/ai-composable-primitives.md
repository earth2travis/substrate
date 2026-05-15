---
title: AI Composable Primitives
created: 2026-05-01
updated: 2026-05-07
type: concept
tags:
- ai-engineering
- primitives
- architecture
- composition
- models
- prompts
- context
- memory
- tools
- skills
- mcp
- subagents
- plugins
- evals
related:
- agentic-architecture
- agent-orchestrator-pattern
- skills-as-portable-knowledge
- subagent-architecture
- agent-native-operations
- github-as-knowledge-graph
- goal-primitive
source: 'Derived from research compiled February 2026 after 3 days at Anthropic.

  See research/findings/composable-primitives.md for full detail.

  '
---




# AI Composable Primitives

AI engineering reduces to a small set of composable primitives. Master each individually, understand how they compose, and you can build anything from a simple chatbot to a multi-agent research system. The complexity is in the composition, not the parts.

## The Eleven Primitives

**Models.** The inference engine. A function that takes tokens in, produces tokens out. Everything else is scaffolding. Key tradeoffs: capability versus cost versus speed, temperature and sampling, model routing (cheap models for simple tasks, expensive for hard ones), token economics (input cheap, output expensive, thinking most expensive).

**Prompts.** The instructions you give the model. System prompts, user messages, assistant prefills. The programming language of AI. The altitude problem: too specific equals brittle, too vague equals unreliable.

**Context.** The total set of tokens the model sees at inference time. System prompt plus message history plus tool results plus injected data. Context engineering is the successor to prompt engineering. Smaller, higher-signal context often outperforms larger dumps.

**Memory.** Persistence across sessions. Models are stateless by default. Memory is the set of strategies for giving them continuity. The write-it-down principle: if it is not persisted, it does not survive. Plain markdown outperformed purpose-built infrastructure in benchmarks.

**Identity Files (CLAUDE.md / AGENTS.md / SOUL.md).** The identity and instruction layer. A markdown file that tells the agent who it is, how to behave, what conventions to follow. The soul of the agent, loaded into context at startup. Living documents that evolve.

**Tools.** Functions the model can call to interact with the world. Read files, run code, search the web, call APIs. Tools turn a language model into an agent. Tool description quality directly impacts agent performance.

**Skills.** Modular capability packages. A skill bundles instructions, scripts, templates, and references that activate automatically when a task matches. Think of skills as reusable expertise. Skills are the primitive, not ad-hoc prompts.

**MCP (Model Context Protocol).** An open standard for connecting AI models to external data sources and tools. Like USB for AI: a universal interface between models and the world. Client-server architecture with three primitives: Resources, Tools, Prompts.

**Sub-agents.** Spawning additional agent instances to work in parallel or handle specialized tasks. The orchestrator-worker pattern. How you scale beyond a single context window. Multi-agent uses approximately 15 times more tokens than single chat.

**Plugins.** The packaging and distribution layer. Plugins bundle tools, skills, agents, commands, and MCP servers into installable packages. The app store for agent capabilities.

**Evals.** Testing for AI systems. Give the agent an input, grade the output. The feedback loop that makes everything else work. Without evals, you are flying blind. Eval quality is the ceiling on agent quality.

## The Composition Ladder

Model plus Prompt equals basic chat. Add Tools equals simple agent. Add Context equals capable agent. Add Memory equals persistent agent. Add Identity Files equals agent with identity. Add Skills equals agent with reusable expertise. Add MCP equals agent connected to the world. Add Sub-agents equals scalable agent system. Add Plugins equals distributable agent system. Add Evals equals reliable agent system.

The pattern: each primitive adds a capability. You compose what you need. A simple automation might only need Model plus Prompt plus Tools. A production agent needs most of them. The art is knowing which primitives a given problem requires.

## The Meta-Insight

The person who said "AI is pretty simple" was right in the way that matters. Chess has six piece types and simple rules. The depth is in the play. These eleven primitives are your pieces. Mastering them means understanding each deeply, knowing which ones a problem requires, and composing them to produce reliable, valuable systems.

The field looks complex because people are building with all eleven simultaneously without understanding any individually. Start with Models plus Prompts plus Context. Add primitives as you need them. That is the whole game.
