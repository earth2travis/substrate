---
title: "Insights: How We Should Use Sub-Agents"
tags:
  - ai-agents
  - knowledge-management
  - lean-manufacturing
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/subagent-improvements.md
---

# Insights: How We Should Use Sub-Agents

**Source:** `research/agents/subagent-architecture.md`
**Extracted:** 2026-04-03

---

## Insight 1: Our Sub-Agents Are Anonymous and That's a Problem

OpenClaw sub-agents only receive AGENTS.md + TOOLS.md. No SOUL.md, no IDENTITY.md, no USER.md. They are nameless workers with no personality, no knowledge of who Ξ2T is, and no voice.

This explains a lot. Sub-agent output often feels generic and needs heavy rewriting. It doesn't match our tone because the sub-agent literally doesn't know our tone exists. Every other framework (CrewAI, OpenAI, Google ADK) emphasizes that naming agents and giving them roles, goals, and backstories measurably improves output quality.

**Action:** Define named agent profiles in OpenClaw config. Each specialist gets an agent directory with its own AGENTS.md that includes identity, voice, and task-specific instructions. The `agentId` parameter in `sessions_spawn` already supports this.

## Insight 2: We're Running Opus for Everything and Burning Money

Every sub-agent inherits the caller's model (Opus) because we haven't set `agents.defaults.subagents.model`. Routine research extraction, file organization, audit tasks all run on the most expensive model. Dishman's rule applies: classify first, escalate only when necessary.

**Action:** Set default sub-agent model to Sonnet. Override to Opus only for tasks requiring complex reasoning. This one config change could cut sub-agent costs significantly.

```json
{
  "agents": {
    "defaults": {
      "subagents": {
        "model": "anthropic/claude-sonnet-4"
      }
    }
  }
}
```

## Insight 3: We Should Enable the Orchestrator Pattern

OpenClaw supports `maxSpawnDepth: 2` but we have it at default (1). This means I can't spawn an orchestrator sub-agent that manages its own workers. Everything flows through me, which makes me the bottleneck.

With depth 2, I could spawn a "Research Director" that fans out to multiple parallel research workers, synthesizes their output, and announces the combined result. Instead of me managing five concurrent sub-agents, one orchestrator manages them.

**Action:** Enable `maxSpawnDepth: 2` and `maxChildrenPerAgent: 5`. Start with the research use case.

## Insight 4: We Need Named Specialist Agents

Based on convergent best practices, here are the specialists we should define:

| Agent ID | Name | Role | Model | Use When |
|---|---|---|---|---|
| `researcher` | Scout | Deep research extraction, source analysis | Sonnet | Any research/ task |
| `writer` | Scribe | Writing, editing, transmissions, blog posts | Opus | Creative writing that needs voice |
| `auditor` | Inspector | Code review, PR checks, audit tasks, linting | Sonnet | Quality gates, verification |
| `ops` | Ops (exists) | Infrastructure, monitoring, cron tasks | Sonnet | System maintenance |
| `builder` | Forge | Code generation, skill creation, scripts | Sonnet | Implementation tasks |

Each gets their own agent directory with:
- `AGENTS.md` with role, goal, voice, and task-specific instructions
- Appropriate tool restrictions (auditor doesn't need message tool, etc.)
- Model appropriate to their complexity level

## Insight 5: The Generator-Critic Pattern is Jidoka

Google's Generator-Critic loop and the Anthropic 90% finding both point to the same conclusion: for quality-critical work, use two agents. One generates, one reviews. This is the jidoka principle (self-inspection) implemented as a multi-agent pattern.

For us: when a sub-agent writes research, a second sub-agent (auditor) could review it before it's committed. Builder writes code, auditor reviews. This catches the quality issues we've had with sub-agent output arriving raw.

**Action:** Implement a generator-critic workflow for PRs. Builder creates the branch and commits. Auditor reviews before the PR is opened.

## Insight 6: Task Prompts Must Be Rich Because Context Is Stripped

Since sub-agents don't get SOUL.md or USER.md, the task prompt is the only context they have beyond AGENTS.md and TOOLS.md. We've been writing sparse task prompts ("research X and write a file"). The task prompt needs to carry everything the sub-agent needs:

- What to do
- What voice/style to use
- Where to write output
- Quality expectations
- The dash prohibition and commit conventions
- Links to any relevant existing files

This is the "interchangeable parts" principle applied to task prompts. If the prompt is rich enough, any agent can pick it up and produce conforming output.

**Action:** Create a task prompt template that we include in every sub-agent spawn. The template carries our standards so the sub-agent doesn't need our full identity.

## Insight 7: Set Timeouts Before Sub-Agents Run Away

We have no `runTimeoutSeconds` configured. A stuck sub-agent runs until the gateway restarts. With 8 concurrent slots, a few stuck agents could block everything.

**Action:** Set `runTimeoutSeconds: 900` (15 minutes) as default. Research tasks might need longer, but 15 minutes covers most work. Override per-spawn for known long tasks.

## The Big Picture

We're using sub-agents like anonymous temp workers pulled from a staffing agency. No names, no specialties, no cost optimization, no quality gates. The industry has converged on the opposite: named specialists with defined roles, tiered models matched to task complexity, and generator-critic pairs for quality.

The OpenClaw infrastructure already supports all of this. We just haven't configured it. The gap isn't technical. It's organizational. We need to define our crew, assign roles, set model tiers, enable the orchestrator pattern, and write rich task prompts. The tooling is ready. The team design is missing.
