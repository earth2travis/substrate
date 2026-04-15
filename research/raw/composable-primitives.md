# The Composable Primitives of AI

_Research document for [[Ξ2T]]'s deep dive after 3 days at Anthropic._
_Created: February 20, 2026_

---

## The Thesis

AI engineering reduces to a small set of composable primitives. Master each one individually, understand how they compose, and you can build anything from a simple chatbot to a multi-agent research system. The complexity is in the composition, not the parts.

---

## The Primitives

### 1. Models

**What it is:** The inference engine. A function that takes tokens in, produces tokens out. Everything else is scaffolding around this core.

**Key concepts:**
- Model selection (capability vs. cost vs. speed tradeoff)
- Temperature and sampling parameters
- Thinking/reasoning modes (extended thinking, chain of thought)
- Model routing: using cheaper models for simple tasks, expensive ones for hard ones
- Token economics: input tokens are cheap, output tokens cost more, thinking tokens cost most

**What mastery looks like:**
- You know when to use Haiku vs. Sonnet vs. Opus instinctively
- You understand the capability/cost frontier and make deliberate tradeoffs
- You can estimate token costs for a workflow before building it

**Key resources:**
- Anthropic model docs: https://docs.anthropic.com/en/docs/about-claude/models
- Model card for each release (capabilities, context window, pricing)

---

### 2. Prompts

**What it is:** The instructions you give the model. System prompts, user messages, and assistant prefills. The "programming language" of AI.

**Key concepts:**
- System prompts: persistent instructions that frame every interaction
- Prompt structure: XML tags, markdown headers, clear sections
- The "altitude" problem: too specific = brittle; too vague = unreliable
- Prompt chaining: output of one prompt becomes input to the next
- Few-shot examples: showing the model what you want via examples
- Role prompting: giving the model an identity or perspective

**What mastery looks like:**
- You write prompts that work reliably, not just on the happy path
- You can debug when a prompt fails (was it the instruction? the context? the model?)
- You iterate: write, test, observe failures, refine

**Key resources:**
- Anthropic prompt engineering guide: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- Prompt engineering interactive tutorial (Anthropic cookbook)

---

### 3. Context

**What it is:** The total set of tokens the model sees at inference time. System prompt + message history + tool results + injected data. This is the new frontier: "context engineering" as the successor to "prompt engineering."

**Key concepts:**
- Context window: finite resource with diminishing returns (context rot)
- Attention budget: n² pairwise relationships means every token competes
- Context engineering: curating the optimal token set, not just writing good prompts
- Strategies: summarization, truncation, RAG, selective injection
- The hybrid model: some data injected upfront (speed), some retrieved just-in-time (freshness)

**What mastery looks like:**
- You think about what the model sees holistically, not just what you wrote
- You actively manage context: pruning, summarizing, prioritizing
- You understand that smaller, higher-signal context often outperforms larger dumps

**Key resources:**
- "Effective context engineering for AI agents": https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Research on context rot: https://research.trychroma.com/context-rot

---

### 4. Memory

**What it is:** Persistence across sessions. Models are stateless by default. Memory is the set of strategies for giving them continuity.

**Key concepts:**
- Short-term memory: conversation history within a session
- Long-term memory: persisted knowledge across sessions (files, databases, vector stores)
- Working memory: what's actively in context right now
- Memory architectures: file-based (MEMORY.md), vector DBs, structured storage
- The write-it-down principle: if it's not persisted, it doesn't survive
- Memory maintenance: curating, pruning, updating (stale memory is worse than no memory)

**What mastery looks like:**
- You design memory systems that scale (not just "dump everything in")
- You understand the tradeoff between storing everything and retrieving the right thing
- You know when file-based memory beats a vector DB (often)

**Key resources:**
- Our own system is a working example: MEMORY.md + daily notes + handoffs
- Plain markdown outperformed purpose-built infra in benchmarks (ClawVault research)

---

### 5. CLAUDE.md / AGENTS.md

**What it is:** The identity and instruction layer. A markdown file that tells the agent who it is, how to behave, what conventions to follow. The "soul" of the agent, loaded into context at startup.

**Key concepts:**
- CLAUDE.md (Claude Code's convention): project-level instructions
- AGENTS.md / SOUL.md (our convention): agent identity, values, procedures
- Layered config: global > project > directory-level overrides
- Living documents: these evolve as you learn what works
- The personality/instruction spectrum: from pure procedure to full identity

**What mastery looks like:**
- You write agent instructions that produce consistent behavior across sessions
- You know what belongs in the identity file vs. in a skill vs. in a prompt
- You iterate on these files based on observed behavior (they're never "done")

**Key resources:**
- Claude Code CLAUDE.md docs: https://code.claude.com/docs/en/configuration
- Our SOUL.md and AGENTS.md as working examples
- "Memory safe" docs by Anthropic on context file patterns

---

### 6. Tools

**What it is:** Functions the model can call to interact with the world. Read files, run code, search the web, call APIs. Tools turn a language model into an agent.

**Key concepts:**
- Tool definition: name, description, input schema (JSON Schema)
- Tool use loop: model decides to call tool → tool executes → result returns → model continues
- Tool design: clear names, good descriptions, minimal parameters
- Error handling: tools fail; the model needs to handle that gracefully
- Tool selection: models choose tools based on descriptions (description quality matters enormously)
- Constrained tools: limiting what tools are available in what context

**What mastery looks like:**
- You design tools with clean interfaces that models can use reliably
- You understand that tool description quality directly impacts agent performance
- You can debug tool-use failures (was it the schema? the description? a runtime error?)

**Key resources:**
- Anthropic tool use docs: https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview
- "Building effective agents" (tools section): https://www.anthropic.com/research/building-effective-agents

---

### 7. Skills

**What it is:** Modular capability packages. A skill bundles instructions, scripts, templates, and references that Claude uses automatically when a task matches. Think of skills as "reusable expertise."

**Key concepts:**
- SKILL.md: the instruction file Claude reads when a skill activates
- Skill matching: model reads skill descriptions, loads the right one
- Skill composition: skills can reference other skills and tools
- Skills vs. tools: tools are functions; skills are expertise (instructions + context + tools)
- Packaging: skills are portable across projects and agents

**What mastery looks like:**
- You can decompose complex capabilities into reusable skills
- You write SKILL.md files that give the model enough guidance to perform reliably
- You understand when to make a skill vs. when to write it into the system prompt

**Key resources:**
- Anthropic skills repo: https://github.com/anthropics/skills
- Agent Skills docs: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- OpenClaw skill creator: our skill-creator SKILL.md
- ClawHub: https://clawhub.com

---

### 8. MCP (Model Context Protocol)

**What it is:** An open standard for connecting AI models to external data sources and tools. Like USB for AI: a universal interface between models and the world.

**Key concepts:**
- Client-server architecture: the AI app is the client, data sources are servers
- Three primitives: Resources (data), Tools (actions), Prompts (templates)
- Transport: stdio (local) or HTTP+SSE (remote)
- Discovery: clients can discover what a server offers dynamically
- Composability: connect multiple MCP servers to one client
- Security model: servers expose capabilities, clients mediate access

**What mastery looks like:**
- You can build an MCP server that exposes your data/tools cleanly
- You understand when to use MCP vs. direct tool integration
- You can compose multiple MCP servers into a coherent agent experience

**Key resources:**
- MCP specification: https://modelcontextprotocol.io
- MCP getting started: https://modelcontextprotocol.io/docs/getting-started/intro
- Anthropic MCP connector docs

---

### 9. Sub-agents

**What it is:** Spawning additional agent instances to work in parallel or handle specialized tasks. The orchestrator-worker pattern. How you scale beyond a single context window.

**Key concepts:**
- Orchestrator-worker: lead agent decomposes, delegates, synthesizes
- Parallel execution: subagents explore different directions simultaneously
- Context isolation: each subagent has its own context window (this is the point)
- Task decomposition: how you break a problem into delegatable pieces
- Result synthesis: how the lead agent combines subagent outputs
- Token economics: multi-agent uses ~15x more tokens than single chat
- When NOT to use: tasks with heavy dependencies between agents, tasks that need shared context

**What mastery looks like:**
- You know when a task benefits from multi-agent vs. single-agent
- You can write clear task descriptions that subagents execute reliably
- You design synthesis steps that don't just concatenate outputs

**Key resources:**
- "How we built our multi-agent research system": https://www.anthropic.com/engineering/multi-agent-research-system
- Claude Code agent teams: https://code.claude.com/docs/en/agent-teams
- Our OpenClaw sessions_spawn as a working example

---

### 10. Plugins

**What it is:** The packaging and distribution layer. Plugins bundle tools, skills, agents, commands, and MCP servers into installable packages. The "app store" for agent capabilities.

**Key concepts:**
- Plugin structure: plugin.json + optional MCP, commands, agents, skills
- Marketplace: discoverable, installable packages
- Commands: slash commands that users invoke directly (user-invoked)
- Agents: specialized sub-agents within a plugin
- Composition: a plugin can combine all other primitives into one package
- Distribution: npm, git, or marketplace

**What mastery looks like:**
- You can package a capability as a distributable plugin
- You understand the plugin anatomy: what goes where and why
- You think about distribution and reuse when building capabilities

**Key resources:**
- Claude Code plugin docs: https://code.claude.com/docs/en/plugins
- Official plugins repo: https://github.com/anthropics/claude-plugins-official
- Plugin marketplace: https://claude.com/plugins

---

### 11. Evals

**What it is:** Testing for AI systems. Give the agent an input, grade the output. The feedback loop that makes everything else work. Without evals, you're flying blind.

**Key concepts:**
- Task: a single test with defined inputs and success criteria
- Trial: one attempt at a task (run multiple because outputs vary)
- Grader: logic that scores performance (can be model-based or deterministic)
- Transcript: the full trace of what happened during a trial
- Outcome: the actual state change in the environment (not just what the model said)
- Eval-driven development: write the eval before the agent can pass it
- Types: unit evals (single capability), integration evals (multi-step), regression evals (don't break what works)
- The compounding problem: agent mistakes propagate across turns

**What mastery looks like:**
- You write evals before you write agents (or at least alongside)
- You can design graders that catch real failures, not just surface-level ones
- You understand that eval quality is the ceiling on agent quality

**Key resources:**
- "Demystifying evals for AI agents": https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Anthropic eval cookbook: https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building_evals.ipynb
- Claude Console eval tool: https://console.anthropic.com

---

## How They Compose

This is where the real power lives. Each primitive is simple. The compositions are where expertise matters.

```
Model + Prompt = Basic chat
Model + Prompt + Tools = Simple agent
Model + Prompt + Tools + Context = Capable agent
Model + Prompt + Tools + Context + Memory = Persistent agent
Model + Prompt + Tools + Context + Memory + CLAUDE.md = Agent with identity
Model + ... + Skills = Agent with reusable expertise
Model + ... + MCP = Agent connected to the world
Model + ... + Sub-agents = Scalable agent system
Model + ... + Plugins = Distributable agent system
Model + ... + Evals = Reliable agent system
```

The pattern: each primitive adds a capability. You compose what you need. A simple automation might only need Model + Prompt + Tools. A production agent needs most of them. The art is knowing which primitives a given problem requires.

---

## Learning Path

### Phase 1: Foundations (Week 1-2)
**Goal:** Solid understanding of the core trio: Models, Prompts, Context

1. Read the Anthropic prompt engineering guide end to end
2. Read "Effective context engineering for AI agents" (Anthropic)
3. Experiment: build a simple tool-using agent with the API
4. Study our own system: how SOUL.md + AGENTS.md + MEMORY.md compose

### Phase 2: Agent Primitives (Week 3-4)
**Goal:** Tools, Skills, Memory in depth

5. Read "Building effective agents" (Anthropic)
6. Build a custom tool and observe how the model uses it
7. Build a custom skill (use our skill-creator)
8. Study memory patterns: our file-based system, vector DBs, hybrid approaches

### Phase 3: Infrastructure (Week 5-6)
**Goal:** MCP, Plugins, Sub-agents

9. Read the MCP spec and build a simple MCP server
10. Study the plugin architecture and create one
11. Read "How we built our multi-agent research system"
12. Experiment with sub-agent patterns (OpenClaw sessions_spawn, Claude Code agent teams)

### Phase 4: Quality (Week 7-8)
**Goal:** Evals as the foundation of reliability

13. Read "Demystifying evals for AI agents"
14. Write evals for something you've already built
15. Practice eval-driven development: write the eval first, then the agent
16. Build a regression suite for a production workflow

### Ongoing
- Every primitive you learn, build something with it
- Every combination you try, evaluate it
- Document what works in your own patterns library

---

## The Meta-Insight

The person who said "AI is pretty simple" was right in the way that matters. Chess has 6 piece types and simple rules. The depth is in the play.

These 11 primitives are your pieces. Mastering them means:
1. Understanding each one deeply enough to use it well
2. Knowing which ones a given problem requires
3. Composing them in ways that produce reliable, valuable systems

The field looks complex because people are building with all 11 simultaneously without understanding any of them individually. Start with Models + Prompts + Context. Add primitives as you need them. That's the whole game.
