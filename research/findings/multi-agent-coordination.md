---
title: Multi-Agent Coordination
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/multi-agent-coordination.md
---

# Multi-Agent Coordination

## Why Multiple Agents?

Single agents hit limits: context window saturation, role confusion (coder vs. reviewer vs. planner), latency on complex tasks, and the fundamental problem that one model doing everything is like one person doing everything. Specialization helps.

## Coordination Patterns

### Hierarchical (Orchestrator + Workers)

**How it works:** One agent (orchestrator/manager) decomposes tasks and delegates to specialist agents. Workers report back. Orchestrator synthesizes results and decides next steps.

**Examples:**
- AutoGen's GroupChat with a manager agent
- CrewAI's hierarchical process
- OpenClaw's main agent + sub-agents (what we use)
- Claude Code's "spawn sub-agent" pattern

**Tradeoffs:**
- ✅ Clear authority and decision-making
- ✅ Orchestrator maintains global context
- ✅ Workers can be specialized (different prompts, tools, models)
- ✅ Natural error handling (orchestrator can retry, reassign)
- ❌ Orchestrator is a bottleneck and single point of failure
- ❌ Orchestrator context grows with number of workers
- ❌ Communication overhead (worker results must be summarized)
- ❌ Workers lack global context (can make locally optimal but globally poor decisions)

**Assessment:** This is the dominant pattern and for good reason. It maps to how human organizations work. The orchestrator doesn't need to be the smartest agent; it needs to be the best at decomposition and synthesis.

### Peer-to-Peer (Debate / Discussion)

**How it works:** Agents communicate directly with each other as equals. No central authority. They negotiate, debate, or collaborate to produce output.

**Examples:**
- Society of Mind approaches
- Multi-agent debate (Du et al., 2023): multiple agents propose answers, critique each other, converge
- ChatDev's role-playing agents (CEO, CTO, programmer, tester)

**Tradeoffs:**
- ✅ No single point of failure
- ✅ Diverse perspectives (reduces groupthink)
- ✅ Can improve factual accuracy through debate
- ❌ Convergence is not guaranteed
- ❌ Expensive: N agents × M rounds of communication
- ❌ Hard to debug (who decided what and why?)
- ❌ Models tend to agree with each other (sycophancy problem)

**Assessment:** Interesting for improving accuracy on factual/reasoning tasks. Not practical for most agent workflows. The sycophancy problem is real: LLMs are trained to be agreeable, which undermines genuine debate. Works better when agents have genuinely different information, not just different "roles."

### Blackboard

**How it works:** Agents share a common workspace (the "blackboard"). Each agent monitors the blackboard, contributes when it can, and reads others' contributions. No direct agent-to-agent communication.

**Examples:**
- Shared file systems (our workspace is effectively a blackboard)
- Shared databases
- Git repositories as coordination medium

**Tradeoffs:**
- ✅ Decoupled: agents don't need to know about each other
- ✅ Asynchronous: agents work at their own pace
- ✅ Auditable: everything is on the blackboard
- ✅ Flexible: new agents can be added without changing existing ones
- ❌ Coordination is implicit (no one "decides" the overall direction)
- ❌ Conflicts when multiple agents modify the same thing
- ❌ No guaranteed ordering or completion
- ❌ Requires well-structured shared state

**Assessment:** Underrated pattern. Our git-based workspace is essentially a blackboard system. Sub-agents write to files, main agent reads them. The git repo provides versioning, conflict detection, and full audit trail. This pattern scales better than hierarchical for loosely coupled work.

### Market-Based

**How it works:** Tasks are posted as "jobs" with criteria. Agents "bid" based on their capabilities. Best-fit agent gets assigned. Can include pricing, reputation, capability matching.

**Examples:**
- Theoretical: agent marketplaces where specialized agents compete for tasks
- Practical: routing queries to different models based on complexity (Anthropic's model routing, OpenRouter)
- Mixture of Experts (at the model level, not agent level)

**Tradeoffs:**
- ✅ Optimal allocation (best agent for each task)
- ✅ Scales well (add agents without redesigning)
- ✅ Self-organizing
- ❌ Complex infrastructure (bidding, matching, reputation)
- ❌ Overkill for most agent systems
- ❌ Assumes agents can accurately self-assess capabilities (they can't)

**Assessment:** The market metaphor is appealing but premature. We don't have enough distinct agent capabilities to justify a marketplace. Model routing (using Sonnet for easy tasks, Opus for hard ones) is the practical version of this pattern and is worth doing.

## How Our System Compares

### Current Architecture: Hierarchical + Blackboard Hybrid

```
Main Agent (Orchestrator)
├── Sub-agents (Workers, spawned on demand)
├── Cron jobs (Scheduled workers)
└── Shared workspace (Blackboard)
    ├── Git repo (source of truth)
    ├── Memory files (coordination state)
    └── Issue tracker (task queue)
```

**What works well:**
- Clear ownership: main agent owns the conversation, sub-agents own tasks
- Push-based completion: sub-agents announce when done (no polling)
- File-based coordination: results are saved, not just reported
- Git provides audit trail and conflict detection

**What could be better:**
- Sub-agents lack context about each other's work
- No mechanism for sub-agents to coordinate directly
- Main agent must manually synthesize all sub-agent output
- No model routing (everything uses the same model)

## Recommendations

1. **Keep the hierarchical + blackboard hybrid.** It's working and it's the right pattern for a personal agent system. Don't add complexity that isn't needed.

2. **Add model routing.** Use cheaper/faster models for routine sub-agent tasks (file organization, formatting, simple lookups). Reserve Opus for judgment calls, creative work, and complex reasoning. This is the practical version of market-based allocation.

3. **Improve sub-agent context.** When spawning a sub-agent, include a brief summary of what other agents are working on. Prevents duplicate work and enables complementary output.

4. **Consider persistent specialist agents** for recurring tasks (email processing, calendar management, code review). Instead of spawning fresh each time, have agents with accumulated context. This is a step toward the "team" model but with the orchestrator still in charge.

5. **Don't build peer-to-peer debate.** It's not worth the cost for personal assistant use cases. If we need multiple perspectives, ask one agent to generate alternatives, not multiple agents to debate.
