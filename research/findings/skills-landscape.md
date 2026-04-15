---
title: Skills Landscape for Agentic Systems (March 2026)
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/skills-landscape.md
---

# Skills Landscape for Agentic Systems (March 2026)

## What Are Skills?

Skills are reusable packages of procedural knowledge for AI agents. They tell an agent **how** to accomplish a category of tasks, as opposed to tools which give agents **capabilities** to act.

Anthropic introduced the concept formally in October 2025. By December, OpenAI adopted the same format for Codex and started using Skills internally in ChatGPT. The Agent AI Foundation (which now governs MCP) lists Skills alongside MCP and agents.md as founding sibling projects.

Skills are becoming a cross-platform standard.

## Anthropic's Skill System (The Reference Implementation)

Source: `research/skills/anthropic-skills-guide.md`

### Structure

```
skill-name/
├── SKILL.md          # Required. Instructions in markdown with YAML frontmatter
├── scripts/          # Optional. Executable code
├── references/       # Optional. Documentation loaded as needed
└── assets/           # Optional. Templates, fonts, icons
```

### Progressive Disclosure (The Key Design Pattern)

Three levels of loading:

1. **YAML frontmatter**: Always in system prompt. Tells the model when to activate the skill. Must be under 1024 chars.
2. **SKILL.md body**: Loaded when model thinks the skill is relevant. Full instructions.
3. **Linked files**: Discovered only as needed (scripts, references, assets).

This is brilliant because it respects context window limits. Most skills are invisible most of the time. Only the trigger description occupies permanent context space.

### Skill Categories

1. **Document & Asset Creation**: Style guides, templates, quality checklists. No external tools needed.
2. **Workflow Automation**: Multi-step processes with validation gates and iterative refinement.
3. **MCP Enhancement**: Orchestrates multiple MCP tool calls with domain expertise and error handling.

Category 3 is where Skills and MCP intersect. A skill wraps MCP tools with procedural knowledge: "To deploy a service, first check the health endpoint, then update the config, then trigger the deploy tool, then verify the health endpoint again."

### What Works

- **Portable across environments**: Same skill works in Claude.ai, Claude Code, and API
- **Composable**: Skills work alongside other skills without conflict
- **Testable**: Three testing dimensions (triggering, functional, performance comparison)
- **Versionable**: Plain files in a repo. Git-friendly.
- **Low overhead**: Frontmatter-only cost when skill isn't active

### What Doesn't

- **Discovery is manual**: No registry or marketplace (yet). Skills are distributed as zip files or folder drops.
- **No runtime verification**: Skills are instructions, not contracts. The model might not follow them perfectly.
- **Trigger precision**: Getting skills to activate at the right time (and not at the wrong time) requires careful prompt engineering of the description field.
- **No inter-skill coordination**: Skills can coexist but don't explicitly compose with each other.

## How Other Frameworks Handle Reusable Agent Knowledge

### OpenAI agents.md

OpenAI's approach to reusable agent knowledge is `agents.md`, a convention for placing agent instructions in repository files (similar to how AGENTS.md works in our workspace).

- Agents discover their instructions by reading markdown files in the repo
- Convention-based, not framework-enforced
- Simpler than Skills: just markdown files, no formal structure
- No progressive disclosure; the agent reads what it reads

**Comparison to Skills:** agents.md is more freeform. Skills are more structured and optimized for context efficiency. agents.md works well for repo-scoped agents. Skills work well for cross-context portable knowledge.

### CrewAI: Role Definitions as Implicit Skills

CrewAI encodes agent knowledge in role definitions:

```python
Agent(
    role="Senior Data Analyst",
    goal="Analyze datasets and produce actionable insights",
    backstory="You are a veteran data analyst with 15 years of experience..."
)
```

This is skills-as-prompt-engineering. The "backstory" is procedural knowledge embedded in a character description. It works for simple cases but:
- Not portable (tied to CrewAI's agent abstraction)
- Not composable (one backstory per agent)
- Not testable (how do you test a backstory?)
- Mixes identity with knowledge

### LangGraph: No Explicit Skill System

LangGraph encodes procedural knowledge in graph structure itself. The workflow IS the knowledge: which nodes to visit, in what order, with what conditions.

- Knowledge is structural, not declarative
- Very precise (explicit state transitions) but not reusable across different graphs
- Custom "prompt templates" per node serve as lightweight skill equivalents
- No portability across contexts

### AutoGen: System Messages as Skills

AutoGen agents receive system messages that define their behavior:

```python
AssistantAgent(
    system_message="You are a code reviewer. Review code for bugs, 
    security issues, and style violations. Always check for..."
)
```

Similar to CrewAI's approach: knowledge embedded in prompts, not structured as reusable units.

### Emerging: Community Skill Ecosystems

By early 2026, community skills are proliferating:
- **Official skills** from Anthropic and Vercel
- **Community/third-party skills** from users, startups, open-source projects
- Skill directories and curated lists appearing (though no formal registry)
- OpenAI adopting the same skill format suggests convergence

## The Skills vs MCP Relationship

Skills and MCP are complementary, not competitive:

| Dimension | MCP | Skills |
|-----------|-----|--------|
| Provides | Capabilities (tools, data, resources) | Knowledge (how to use capabilities) |
| Runtime | Server process with API | Markdown files loaded into context |
| Scope | Individual actions | Multi-step workflows |
| State | Stateful connections (moving to stateless) | Stateless instructions |
| Composability | Tools are independent | Skills orchestrate tools |

**The most powerful pattern:** A Skill that orchestrates MCP tools. The Skill provides the workflow logic ("do A, check B, if C then D"), and MCP provides the tool execution ("here's how to actually do A").

MCP's new Sampling capability (server-initiated LLM calls with tool support) starts to blur this line, but the conceptual separation remains useful.

## What Synthweave/Loom Should Use

### Adopt the Anthropic Skill format

It's becoming the standard. OpenAI already adopted it. The progressive disclosure pattern is genuinely good engineering. The format is simple (markdown + YAML + optional scripts), portable, and versionable.

### Build a skill library for our domains

Every recurring workflow should be a skill:
- Deployment procedures
- Research methodologies
- Code review standards
- Communication templates
- Debugging runbooks

### Extend Skills with runtime contracts

Anthropic's skills are pure instructions. We should add:
- **Required tools**: Declare which MCP tools a skill needs (fail fast if unavailable)
- **Preconditions**: What must be true before the skill activates
- **Postconditions**: What should be true after successful execution
- **Token budget estimates**: How much context this skill typically consumes

### Don't overinvest in skill registries yet

The ecosystem is too young. A directory of skill folders in our repo is sufficient. When a formal registry standard emerges (likely through the Agent AI Foundation), adopt it then.

### Skills as the bridge between tools and workflows

In our stack:
- **MCP servers** provide individual capabilities
- **Skills** encode how to orchestrate those capabilities
- **Workflow orchestration** (Symphony-style) manages when skills get activated

This three-layer architecture (tools → skills → orchestration) cleanly separates concerns and lets each layer evolve independently.
