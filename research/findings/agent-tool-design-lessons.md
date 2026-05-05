---
title: "Tool Design Lessons from Claude Code: Cognitive Ergonomics for Agents"
tags: [agent, tools, design, claude-code, progressive-disclosure, ergonomics]
related: [[agentic-architecture]], [[agent-identity]], [[skills-as-onboarding]]
source: research/raw/agent-tool-design-lessons.md
---

# Tool Design Lessons from Claude Code: Cognitive Ergonomics for Agents

## Core Thesis

Designing an agent's action space is the hardest part of building an agent harness. The right tools depend on the model's abilities, not on abstract completeness. You design tools by paying attention to how the model actually uses them. Read the outputs. Experiment. See like an agent.

This is not engineering in the traditional sense. It is closer to ethnography: observing a foreign intelligence and designing affordances that match its cognition.

## 1. Tool Design as Cognitive Ergonomics

A tool is only as good as the model's ability to wield it. The question is not "what can this tool do?" but "what can this model do *with* this tool?"

OpenClaw's skill system already embodies this. Skills are not raw tool definitions; they are contextual instructions that shape how the model approaches a capability. The difference between giving a model `bash` and giving it `bash + a skill that explains when and how to use it` is the difference between a calculator and a computer.

## 2. The Iteration Pattern: Three Attempts at Elicitation

The AskUserQuestion tool went through three iterations, revealing a general pattern:

**Attempt 1: Bolt it onto an existing tool.** Added questions to ExitPlanTool. Quick but semantically confused. The model could not reason about a tool serving two purposes. **Lesson**: tools should have a single, clear semantic purpose.

**Attempt 2: Change the output format.** Modified output instructions to produce structured markdown. Almost worked, but "almost" is the enemy. The model appended extra text, omitted options, used different formats. **Lesson**: unstructured output is unreliable for structured needs.

**Attempt 3: Purpose-built tool with clear semantics.** Structured interface, modal blocking, one job. It worked because the tool had one job, structured input matched structured output, and Claude "liked" calling it: the interface matched the model's natural reasoning patterns.

**General pattern**:
1. Hack it onto something existing (fast, confusing)
2. Try to solve it with prompting/formatting (elegant, fragile)
3. Build the right abstraction (more work, actually works)

## 3. Tools as Living Things: Capability Drift

**As model capabilities increase, the tools that your models once needed might now be constraining them.**

TodoWrite was built because early models needed external scaffolding. Better models did not need the guardrails; worse, the guardrails became constraints. The replacement, Tasks, shifted from "keeping the model on track" to "helping agents communicate with each other."

**What this means**: Tools encode assumptions about model capabilities. Every tool contains an implicit bet: "the model can do X but not Y." When the model improves, those bets become wrong, and the tool becomes a cage.

This is why tool auditing matters. Not just "does it work?" but "does it still need to work this way?"

## 4. Progressive Disclosure: Context as Architecture

The agent discovers context incrementally through exploration, rather than having everything front-loaded.

**Evolution in Claude Code**:
- **RAG/vector database**: Context given to the model. Fast but fragile.
- **Grep tool**: Model searches for its own context. Slower but more robust.
- **Skills with recursive file references**: Nested discovery. The model navigates a knowledge graph.

Over one year, Claude went from "not really being able to build its own context" to "nested search across several layers of files to find the exact context it needed."

**Why this matters**:
- **Context rot prevention**: Irrelevant context degrades performance. Progressive disclosure means the model only loads what it needs.
- **Scalability**: Add unlimited capability through files without touching the tool interface.
- **Composability**: Users extend the system by writing files, not code.
- **Learning to learn**: A model that builds its own context develops research skills.

## 5. The 20 Tool Ceiling

Claude Code has approximately 20 tools, and the bar to add a new one is high. More options means more cognitive load, more potential for confusion.

**Escape hatch**: Extend capability without extending the tool set by using progressive disclosure. A subagent with specialized instructions is functionally a tool, but it does not increase the tool count in the parent agent's action space.

## Design Heuristics

1. **One tool, one semantic purpose.** Do not overload tools.
2. **Match the interface to the model's reasoning.** If the model struggles with a tool, the tool is wrong.
3. **Prefer progressive disclosure over tool proliferation.** Can you solve this with a file instead of a tool?
4. **Audit tools for capability drift.** Yesterday's scaffolding is today's constraint.
5. **Read your outputs.** The model's behavior tells you what it needs. This is empirical.
6. **The model has to "like" the tool.** If the model consistently misuses or avoids a tool, the interface does not match its cognition.

## Connections to Our Architecture

| Claude Code Pattern | OpenClaw Equivalent | Status |
|---------------------|---------------------|--------|
| Progressive disclosure via skills | SKILL.md system | Active, working well |
| Subagent for specialized tasks | sessions_spawn | Active, evolving |
| Tool audit for capability drift | No formal process | Gap: need periodic audit |
| Single semantic purpose per tool | Mostly followed | Some skills bundle multiple concerns |
| Context building via search | memory_search, web_search, grep | Active |
| Guide subagent for self knowledge | No equivalent | Gap: could build a "meta" skill |

## Action Items

1. Establish a tool/skill audit cadence. Quarterly review: which skills are used, which are avoided, which constrain more than they enable?
2. Review system prompt density. Is everything in AGENTS.md still earning its place?
3. Consider a self-knowledge subagent for OpenClaw questions.
4. Track model capability changes. When models improve, revisit assumptions baked into tools and protocols.
