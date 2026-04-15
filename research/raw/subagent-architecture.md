# Sub-Agent Architecture: OpenClaw, Big Labs, and Open Source

**Researched:** 2026-04-03
**Purpose:** Understand best practices for sub-agent systems to improve how we use them.

---

## Part 1: OpenClaw Sub-Agent Capabilities (from docs)

**Source:** https://docs.openclaw.ai/tools/subagents

### What Sub-Agents Are

Background agent runs spawned from an existing agent run. Own session, own context, own token usage. When finished, they announce results back to the requester channel.

### Spawn Methods

- **`sessions_spawn` tool:** Programmatic. The main agent spawns workers.
- **`/subagents spawn` slash command:** Manual. User spawns directly.

### Key Parameters

- `task` (required): What the sub-agent should do
- `label`: Human-readable name for the run
- `agentId`: Spawn under a different agent profile (requires allowlist)
- `model`: Override model for cost optimization
- `thinking`: Override thinking level
- `runTimeoutSeconds`: Kill if it takes too long
- `thread`: Bind to a channel thread (Discord only currently)
- `mode`: `run` (one-shot) or `session` (persistent, requires thread)
- `cleanup`: `delete` or `keep`
- `sandbox`: `inherit` or `require`

### Orchestrator Pattern (Nested Sub-Agents)

OpenClaw supports two levels of nesting with `maxSpawnDepth: 2`:

| Depth | Role | Can Spawn? |
|---|---|---|
| 0 | Main agent | Always |
| 1 | Orchestrator sub-agent | Only if maxSpawnDepth >= 2 |
| 2 | Leaf worker | Never |

The orchestrator gets session tools (sessions_spawn, subagents, sessions_list, sessions_history). Leaf workers do not. Results flow back up: worker announces to orchestrator, orchestrator synthesizes and announces to main.

### Configuration Options

```json
{
  "agents": {
    "defaults": {
      "subagents": {
        "maxSpawnDepth": 2,
        "maxChildrenPerAgent": 5,
        "maxConcurrent": 8,
        "runTimeoutSeconds": 900,
        "model": "anthropic/claude-sonnet-4"
      }
    }
  }
}
```

### Critical Detail: Context Injection

**Sub-agents only get AGENTS.md + TOOLS.md.** They do NOT get SOUL.md, IDENTITY.md, USER.md, HEARTBEAT.md, or BOOTSTRAP.md. This means sub-agents have no identity, no knowledge of who they serve, and no personality. They are anonymous workers by default.

### Agent Profiles

You can define named agents in `agents.list[]` with their own:
- Workspace directory
- Agent directory (for separate AGENTS.md, auth, etc.)
- Model override
- Heartbeat config
- Tool restrictions
- Sub-agent allowlists

### What We Currently Have

Two agents configured:
- `main` (Sivart): Opus, full workspace, can spawn main or ops sub-agents
- `ops`: Opus, separate workspace at /home/clawd/ops-agent, no browser/canvas/messaging

No named specialist sub-agents. No model tiering. No orchestrator pattern enabled. Sub-agents run on default (inherits Opus from caller). No run timeouts configured.

---

## Part 2: Industry Patterns

### Anthropic: Building Effective Agents

Anthropic's research on multi-agent systems identifies key findings:

**The 90% finding:** For complex tasks requiring multiple independent directions simultaneously, multi-agent systems outperform single-agent systems by 90.2%. This is the threshold where specialization pays off.

**When to go multi-agent:**
- Single agent exceeds 10-15 tools
- Task requires pursuit of multiple independent directions
- Different domains need different expertise
- Parallelization would significantly reduce time

**When single agent suffices:**
- Simple, linear tasks
- Few tools needed
- No specialization benefit

**Key principle:** Context management is the bottleneck. As context grows too complex for a single orchestrator, performance degrades. The orchestrator should coordinate, not do the work.

### OpenAI: Agents SDK (successor to Swarm)

OpenAI evolved from the experimental Swarm framework to a production Agents SDK with:

**Named, specialized agents:** Each agent has a unique system prompt, tools, and optional knowledge bases. The "God Bot" anti-pattern (one agent doing everything) is explicitly warned against.

**Four patterns:**
1. **Triage and dynamic handoff:** Central agent classifies and routes to specialists
2. **Sequential chains:** Assembly-line processing (research → analysis → reporting)
3. **Parallel execution:** Multiple specialists work concurrently
4. **Agents-as-tools:** One agent callable as a tool by another

**Key practice: explicit handoffs over opaque automation.** The routing decisions should be visible and debuggable, not hidden in prompt magic.

### Google ADK: Eight Design Patterns

Google's Agent Development Kit identifies eight fundamental patterns:

1. **Coordinator/Dispatcher:** Central agent routes to specialists
2. **Sequential Pipeline:** Agents process in order
3. **Parallel Processing:** Simultaneous execution with shared state
4. **Generator and Critic Loop:** Iterative refinement for quality
5. **Composite Pattern:** Combines multiple patterns
6. Human-in-the-Loop
7. Delegation hierarchies
8. Tool-agent composition

**Design philosophy:** "Reliability comes from decentralization and specialization." Assigning specific roles (Parser, Critic, Dispatcher) to individual agents creates systems that are inherently modular, testable, and reliable. The AI equivalent of microservices.

### CrewAI: Role-Based Agent Design

CrewAI's open-source framework uses three defining attributes per agent:

- **Role:** Specific expertise ("Senior Data Researcher" not "Researcher")
- **Goal:** What the agent is trying to achieve
- **Backstory:** Personality and context that shapes behavior

**Key finding: specialists over generalists.** "Creative Storyteller" outperforms "Writer." Specific roles produce more consistent, higher-quality output. The backstory isn't decorative; it measurably improves performance by giving the model a persona to anchor to.

**Expertise levels:** Novice (simple tasks), Intermediate (standard), Expert (complex), World-class (critical). Mix levels in a crew for cost optimization.

---

## Part 3: Converging Best Practices

### 1. Name and Specialize Your Agents

Every major framework agrees: named, specialized agents with clear roles outperform generic "do everything" agents. The name and role aren't cosmetic. They anchor the model's behavior and improve output quality.

### 2. Match Model to Task Complexity

Clanker's pattern (rules first, cheap classification, expensive reasoning only when needed) is the consensus. Sub-agents doing routine work should run on cheaper models. Only complex reasoning tasks need frontier models.

### 3. Orchestrator Coordinates, Workers Execute

The orchestrator's job is decomposition, routing, and synthesis. It should not do the detail work. This is exactly the executive layer model we describe in AGENTS.md, but we haven't implemented it for sub-agents.

### 4. Explicit Handoffs, Not Magic

OpenAI emphasizes this: routing decisions should be visible and debuggable. Don't hide delegation logic in prompts. Make the handoff explicit.

### 5. Context Isolation is a Feature

Sub-agents having their own context window (not sharing the parent's) is correct. It prevents context pollution and lets each agent focus. But they need enough context to do their job, which means the task prompt must be rich.

### 6. Quality Through Composition

Google's Generator-Critic loop and CrewAI's multi-level expertise both point to the same thing: use pairs of agents (builder + reviewer) for quality-critical work. One generates, one critiques. This is jidoka for sub-agents.

---

## Sources

- OpenClaw docs: https://docs.openclaw.ai/tools/subagents
- Anthropic: "Building Effective AI Agents: Architecture Patterns and Implementation Frameworks"
- OpenAI: Agents SDK documentation, Swarm patterns
- Google: Agent Development Kit, "Developer's Guide to Multi-Agent Patterns in ADK"
- CrewAI: Agent customization docs, "Crafting Effective Agents"
- Clanker: Jack Dishman, event-driven agent architecture (see research/agents/clanker-event-driven-architecture.md)
