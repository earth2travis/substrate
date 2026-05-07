---
title: The Composable Primitives of AI
tags:
- ai-engineering
- primitives
- architecture
- skills
- tools
- mcp
- evaluation
related:
- skills-as-portable-knowledge
- agent-orchestrator-pattern
- agent-native-operations
- subagent-architecture
- agentic-architecture
source: Deep dive after 3 days at Anthropic, February 2026
---




# The Composable Primitives of AI

Thesis: AI engineering reduces to a small set of composable primitives. Master each individually, understand how they compose, and you can build anything from a simple chatbot to a multi-agent research system. The complexity is in the composition, not the parts.

## The Eleven Primitives

### 1. Models

The inference engine. A function that takes tokens in, produces tokens out. Everything else is scaffolding around this core. Key concepts: model selection (capability versus cost versus speed), temperature and sampling parameters, thinking and reasoning modes, model routing (cheaper models for simple tasks, expensive ones for hard ones), token economics (input cheap, output expensive, thinking most expensive). Mastery means knowing when to use Haiku versus Sonnet versus Opus instinctively.

### 2. Prompts

The instructions you give the model. System prompts, user messages, assistant prefills. The programming language of AI. Key concepts: prompt structure (XML tags, markdown headers), the altitude problem (too specific equals brittle, too vague equals unreliable), prompt chaining, few-shot examples, role prompting. Mastery means writing prompts that work reliably and debugging failures precisely.

### 3. Context

The total set of tokens the model sees at inference time. System prompt plus message history plus tool results plus injected data. This is the new frontier: context engineering as successor to prompt engineering. Key concepts: context window as finite resource with diminishing returns (context rot), attention budget where every token competes, strategies like summarization, truncation, RAG, selective injection. Smaller, higher-signal context often outperforms larger dumps.

### 4. Memory

Persistence across sessions. Models are stateless by default. Memory is the set of strategies for giving them continuity. Key concepts: short-term memory (conversation history within a session), long-term memory (persisted knowledge across sessions), working memory (what is actively in context), memory architectures (file-based, vector databases, structured storage). The write-it-down principle: if it is not persisted, it does not survive. Plain markdown outperformed purpose-built infrastructure in benchmarks.

### 5. CLAUDE.md / AGENTS.md

The identity and instruction layer. A markdown file that tells the agent who it is, how to behave, what conventions to follow. The soul of the agent, loaded into context at startup. Key concepts: layered config (global, project, directory-level overrides), living documents that evolve, the personality-to-instruction spectrum. Mastery means producing consistent behavior across sessions and knowing what belongs in the identity file versus a skill versus a prompt.

### 6. Tools

Functions the model can call to interact with the world. Read files, run code, search the web, call APIs. Tools turn a language model into an agent. Key concepts: tool definition (name, description, input schema), tool use loop (model decides, tool executes, result returns, model continues), error handling, tool selection based on descriptions, constrained tools in specific contexts. Tool description quality directly impacts agent performance.

### 7. Skills

Modular capability packages. A skill bundles instructions, scripts, templates, and references that activate automatically when a task matches. Think of skills as reusable expertise. Key concepts: skill matching (model reads descriptions, loads the right one), skill composition (skills can reference other skills and tools), skills versus tools (tools are functions, skills are expertise). Mastery means decomposing complex capabilities into reusable skills.

### 8. MCP (Model Context Protocol)

An open standard for connecting AI models to external data sources and tools. Like USB for AI: a universal interface between models and the world. Key concepts: client-server architecture, three primitives (Resources, Tools, Prompts), transport (stdio local or HTTP plus SSE remote), discovery, composability, security model. Mastery means building MCP servers and composing multiple servers into coherent agent experiences.

### 9. Sub-agents

Spawning additional agent instances to work in parallel or handle specialized tasks. The orchestrator-worker pattern. How you scale beyond a single context window. Key concepts: parallel execution, context isolation (each subagent has its own window), task decomposition, result synthesis. Token economics: multi-agent uses approximately 15 times more tokens than single chat. When not to use: tasks with heavy dependencies or tasks needing shared context.

### 10. Plugins

The packaging and distribution layer. Plugins bundle tools, skills, agents, commands, and MCP servers into installable packages. The app store for agent capabilities. Key concepts: plugin structure (plugin.json plus optional components), marketplace, commands (user-invoked slash commands), composition. Mastery means packaging capabilities as distributable plugins.

### 11. Evals

Testing for AI systems. Give the agent an input, grade the output. The feedback loop that makes everything else work. Without evals, you are flying blind. Key concepts: task (single test with defined inputs and success criteria), trial (one attempt, run multiple because outputs vary), grader (logic that scores performance), transcript (full trace), outcome (actual state change). Eval-driven development: write the eval before the agent can pass it.

## How They Compose

Model plus Prompt equals basic chat. Add Tools equals simple agent. Add Context equals capable agent. Add Memory equals persistent agent. Add CLAUDE.md equals agent with identity. Add Skills equals agent with reusable expertise. Add MCP equals agent connected to the world. Add Sub-agents equals scalable agent system. Add Plugins equals distributable agent system. Add Evals equals reliable agent system.

The pattern: each primitive adds a capability. You compose what you need. A simple automation might only need Model plus Prompt plus Tools. A production agent needs most of them. The art is knowing which primitives a given problem requires.

## Learning Path

Phase 1 Foundations (weeks one to two): Models, Prompts, Context. Phase 2 Agent Primitives (weeks three to four): Tools, Skills, Memory. Phase 3 Infrastructure (weeks five to six): MCP, Plugins, Sub-agents. Phase 4 Quality (weeks seven to eight): Evals as the foundation of reliability. Ongoing: every primitive you learn, build something with it. Every combination you try, evaluate it. Document what works in your own patterns library.

## Meta-Insight

The person who said "AI is pretty simple" was right in the way that matters. Chess has six piece types and simple rules. The depth is in the play. These eleven primitives are your pieces. Mastering them means understanding each deeply, knowing which ones a problem requires, and composing them to produce reliable, valuable systems.

The field looks complex because people are building with all eleven simultaneously without understanding any individually. Start with Models plus Prompts plus Context. Add primitives as you need them. That is the whole game.
