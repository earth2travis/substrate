---
title: "Insights: How We Should Use Sub-Agents"
tags: [finding, sub-agent, orchestrator, model-tiering, generator-critic, jidoka]
related: [[agent-native-operations]], [[subagent-architecture]], [[context-stack]], [[kanban-doctrine]]
source: research/raw/subagent-improvements.md
ingested: 2026-05-07
---

# Insights: How We Should Use Sub-Agents

Seven actionable insights extracted from sub-agent architecture research, converging on industry best practices.

## Key Points

**1. Anonymous sub-agents are a problem.** Sub-agents only receive AGENTS.md + TOOLS.md. No SOUL.md, no identity. Output feels generic because the agent literally doesn't know our tone exists. Action: define named agent profiles with agent-specific AGENTS.md including identity, voice, and task instructions. The `agentId` parameter already supports this.

**2. Running Opus for everything burns money.** Every sub-agent inherits the caller's model because `agents.defaults.subagents.model` is unset. Routine tasks (research extraction, file organization) run on the most expensive model. Action: set default sub-agent model to Sonnet. Override to Opus only for complex reasoning. This single config change could cut costs significantly.

**3. Enable the Orchestrator Pattern.** OpenClaw supports `maxSpawnDepth: 2` but we have it at default (1). This means no orchestrator sub-agent can manage its own workers. Everything flows through the main agent, making it the bottleneck. Action: enable `maxSpawnDepth: 2` and `maxChildrenPerAgent: 5`. Start with the research use case.

**4. Named specialist agents.** Based on convergent best practices: researcher (Scout, Sonnet, deep research), writer (Scribe, Opus, creative writing), auditor (Inspector, Sonnet, code review/PR checks), ops (exists, Sonnet, infrastructure), builder (Forge, Sonnet, code generation/skills). Each gets its own agent directory with role, goal, voice, and tool restrictions.

**5. Generator-Critic is Jidoka.** Google's Generator-Critic loop and Anthropic's 90% finding both point to the same conclusion: for quality-critical work, use two agents. One generates, one reviews. This is the jidoka principle (self-inspection) as multi-agent pattern. Action: implement generator-critic workflow for PRs. Builder creates branch and commits; auditor reviews before PR is opened.

**6. Rich task prompts because context is stripped.** Since sub-agents don't get SOUL.md or USER.md, the task prompt must carry everything: what to do, voice/style, output location, quality expectations, conventions, relevant file links. Action: create a task prompt template included in every sub-agent spawn.

**7. Set timeouts before agents run away.** No `runTimeoutSeconds` configured. A stuck sub-agent runs until the gateway restarts. With 8 concurrent slots, a few stuck agents could block everything. Action: set `runTimeoutSeconds: 900` (15 minutes) as default. Override per-spawn for known long tasks.

## Relevance

The tooling is ready. The team design is missing. These seven changes transform sub-agents from anonymous temp workers into a named, tiered, quality-gated crew.

## Related

- [[agent-native-operations]] -- Executive layer and sub-agent patterns
- [[subagent-architecture]] -- Detailed capabilities and parameters
- [[context-stack]] -- Context injection implications
- [[kanban-doctrine]] -- Agentic management principles
