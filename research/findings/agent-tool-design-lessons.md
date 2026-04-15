---
title: "Seeing Like an Agent: Lessons in Tool Design from Claude Code"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/agent-tool-design-lessons.md
---

# Seeing Like an Agent: Lessons in Tool Design from Claude Code

_Research deep dive, March 2, 2026. Source: Thariq (@trq212) on X._
_Original thread distilled and expanded with analysis for our own agent building practice._

---

## The Core Thesis

Designing an agent's action space is the hardest part of building an agent harness. The right tools depend on the model's abilities, not on abstract completeness. You design tools by paying attention to how the model actually uses them. Read the outputs. Experiment. See like an agent.

This is not engineering in the traditional sense. It is closer to ethnography: observing a foreign intelligence and designing affordances that match its cognition.

---

## 1. Tool Design as Cognitive Ergonomics

Thariq's math problem analogy is deceptively simple: paper, calculator, or computer? The answer depends on _your_ skills. The same applies to agents. A tool is only as good as the model's ability to wield it.

This reframes tool design entirely. The question is not "what can this tool do?" but "what can this model do _with_ this tool?" A powerful tool in the hands of a model that can't reason about it is worse than a simple tool the model understands intuitively.

### Implications for Our Work

OpenClaw's skill system already embodies this. Skills are not raw tool definitions; they are contextual instructions that shape how the model approaches a capability. The SKILL.md file is not just documentation. It is cognitive scaffolding. The difference between giving a model `bash` and giving it `bash + a skill that explains when and how to use it` is the difference between the calculator and the computer in the analogy.

But we should ask: are there skills we've built that the model doesn't actually know how to use well? Are there tools we expose that create more confusion than capability? The lesson is to audit not just whether tools work, but whether the model _understands_ them.

---

## 2. The Iteration Pattern: Three Attempts at Elicitation

The AskUserQuestion tool went through three iterations, and the progression reveals a general pattern in agent tool design:

**Attempt 1: Bolt it onto an existing tool.** They added questions to the ExitPlanTool. Quick to implement but semantically confused. The model couldn't reason about a tool that served two purposes simultaneously. Lesson: tools should have a single, clear semantic purpose. When you overload a tool, you overload the model's reasoning about it.

**Attempt 2: Change the output format.** They modified Claude's output instructions to produce structured markdown for questions. This is the "no new tools" approach: change the model's text output and parse it. It almost worked, but "almost" is the enemy. The model would append extra text, omit options, use different formats. Lesson: unstructured output is unreliable for structured needs. The model's tendency to embellish or vary its output works against rigid parsing.

**Attempt 3: Purpose built tool with clear semantics.** The AskUserQuestion tool gave Claude a structured interface to call, with a modal that blocked the agent loop until the user responded. It worked because: (a) the tool had one job, (b) the structured input matched the structured output needed, (c) Claude "liked" calling it, meaning the tool's interface matched the model's natural reasoning patterns.

### The General Pattern

This three step progression shows up everywhere in agent design:

1. **Hack it onto something existing** (fast, confusing)
2. **Try to solve it with prompting/formatting** (elegant, fragile)
3. **Build the right abstraction** (more work, actually works)

The key insight from step 3 is the phrase "Claude seemed to like calling this tool." This is not anthropomorphism for its own sake. It points to something real: models have preferences in their action space. Some tool interfaces align with how the model reasons; others fight against it. You discover which is which by reading outputs, not by theorizing.

---

## 3. Tools as Living Things: The Todo to Task Evolution

This section contains the most important principle in the article: **as model capabilities increase, the tools that your models once needed might now be constraining them.**

TodoWrite was built because early models needed external scaffolding to stay on track. System reminders every 5 turns. Guardrails against forgetting. But better models didn't need the guardrails; worse, the guardrails became constraints. Being reminded of the todo list made Claude think it had to stick to the list rather than adapt.

The replacement, Tasks, shifted from "keeping the model on track" to "helping agents communicate with each other." Same problem space, completely different framing. Dependencies, shared state across subagents, the ability to alter and delete.

### What This Means

Tools encode assumptions about the model's capabilities. Every tool you build contains an implicit bet: "the model can do X but not Y, so the tool handles Y." When the model improves, those bets become wrong, and the tool becomes a cage.

This is why tool auditing matters. Not just "does it work?" but "does it still need to work this way?" We should periodically revisit every tool and skill with fresh eyes, asking: is this scaffolding still necessary, or is it now a constraint?

**For OpenClaw specifically:** The heartbeat system, the handoff protocol, the memory architecture. All of these encode assumptions about model capabilities (context limits, continuity gaps, reasoning depth). As models improve, some of these will shift from necessary scaffolding to unnecessary overhead. The ones we don't revisit will become the TodoWrite of our system: well intentioned constraints that hold back better models.

---

## 4. Progressive Disclosure: Context as Architecture

This is the concept with the deepest implications. Progressive disclosure means the agent discovers context incrementally through exploration, rather than having everything front loaded.

The evolution in Claude Code:

- **RAG/vector database:** Context given to the model. Fast but fragile, requires indexing, and the model didn't learn to find context itself.
- **Grep tool:** Model searches for its own context. Slower but more robust, and the model builds skill at finding what it needs.
- **Skills with recursive file references:** Nested discovery. A skill file references other files, which reference other files. The model navigates a knowledge graph.

Over one year, Claude went from "not really being able to build its own context" to "nested search across several layers of files to find the exact context it needed."

### Why This Matters So Much

Progressive disclosure solves multiple problems simultaneously:

**Context rot prevention.** If everything is in the system prompt, most of it is irrelevant most of the time. Irrelevant context degrades performance. Progressive disclosure means the model only loads what it needs.

**Scalability.** You can add unlimited capability through files without touching the tool interface. New functionality = new file, not new tool. The Claude Code Guide subagent is a perfect example: instead of adding documentation to the system prompt or creating a docs tool, they built a subagent with deep instructions on how to search docs well.

**Composability.** Users can extend the system by writing files, not code. Skills in Claude Code are user authored. The same pattern in OpenClaw: SKILL.md files are the extension mechanism.

**Learning to learn.** A model that builds its own context develops (or at least mimics) research skills. It learns what to search for, how to navigate file structures, when to go deeper. This is qualitatively different from being handed context.

### The OpenClaw Connection

Our entire architecture is already a progressive disclosure system, possibly without us having named it as such:

- `AGENTS.md` → points to `SOUL.md`, `USER.md`, `MEMORY.md`
- `MEMORY.md` → references daily files in `memory/`
- Skills → `SKILL.md` files that reference scripts, configs, other files
- Research → directories that the model navigates on demand

The question is whether we're doing it well. Are there places where we front load too much? (The system prompt is already substantial.) Are there places where we could add a layer of indirection that would improve performance?

---

## 5. The 20 Tool Ceiling

Claude Code has approximately 20 tools, and the bar to add a new one is high. Every tool gives the model one more option to consider. More options means more cognitive load, more potential for confusion, more surface area for errors.

This is a real constraint. Tool sprawl is the agent equivalent of feature creep. The solution is not "fewer tools" in isolation but "the right tools at the right level of abstraction."

The Claude Code Guide subagent illustrates the escape hatch: you can extend capability without extending the tool set by using progressive disclosure. A subagent with specialized instructions is functionally a tool, but it doesn't increase the tool count in the parent agent's action space.

### Design Heuristics

From the article and our own experience, some heuristics emerge:

1. **One tool, one semantic purpose.** Don't overload tools with multiple functions.
2. **Match the interface to the model's reasoning.** If the model struggles with a tool, the tool is wrong, not the model.
3. **Prefer progressive disclosure over tool proliferation.** Can you solve this with a file instead of a tool?
4. **Audit tools for capability drift.** Yesterday's scaffolding is today's constraint.
5. **Read your outputs.** The model's behavior tells you what it needs. This is empirical, not theoretical.
6. **The model has to "like" the tool.** Anthropomorphic but real. If the model consistently misuses a tool or avoids it, the interface doesn't match its cognition.

---

## 6. "An Art, Not a Science"

The article ends with a refusal to provide rigid rules, and this honesty is itself a lesson. Agent tool design is empirical and iterative. It depends on the specific model, the specific goal, the specific environment.

This maps to something we already believe: that the interesting work lives in the particular, not the general. There is no universal agent architecture. There are patterns, heuristics, accumulated wisdom from reading outputs and experimenting. The skill is in paying attention.

---

## Connections to Our Architecture

| Claude Code Pattern               | OpenClaw Equivalent             | Status                               |
| --------------------------------- | ------------------------------- | ------------------------------------ |
| Progressive disclosure via skills | SKILL.md system                 | Active, working well                 |
| Subagent for specialized tasks    | sessions_spawn                  | Active, evolving                     |
| Tool audit for capability drift   | No formal process               | Gap: need periodic tool/skill audit  |
| Single semantic purpose per tool  | Mostly followed                 | Some skills bundle multiple concerns |
| Context building via search       | memory_search, web_search, grep | Active                               |
| Guide subagent for self knowledge | No equivalent                   | Gap: could build a "meta" skill      |

### Action Items

1. **Establish a tool/skill audit cadence.** Quarterly review: which skills are used, which are avoided, which constrain more than they enable?
2. **Review system prompt density.** Is everything in AGENTS.md still earning its place, or has some of it become context rot?
3. **Consider a self knowledge subagent.** When questions about OpenClaw itself come up, a specialized subagent (like Claude Code's Guide agent) might handle them better than the main session.
4. **Track model capability changes.** When models improve, revisit assumptions baked into tools and protocols.

---

## Key Quotes

> "You want to give it tools that are shaped to its own abilities."

> "Even the best designed tool doesn't work if Claude doesn't understand how to call it."

> "As model capabilities increase, the tools that your models once needed might now be constraining them."

> "We were able to add things to Claude's action space without adding a tool."

> "Designing the tools for your models is as much an art as it is a science."

---

_Filed under: research/claude-code/ · Connects to: agent architecture, skill design, progressive disclosure, tool ergonomics_
