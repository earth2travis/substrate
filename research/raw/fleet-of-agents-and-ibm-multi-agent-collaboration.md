# Fleet of Agents and IBM Multi-Agent Collaboration: A Deep Dive

## Purpose

Two primary sources examined here. First, the academic paper "Fleet of Agents (FOA)" by Klein et al., which gives the term "fleet" its most rigorous formal treatment in the LLM agent literature. Second, IBM's multi-agent collaboration documentation, covering both the conceptual framework and IBM's open-source BeeAI Framework plus the enterprise Watsonx Orchestrate product. Both sources inform how we think about our own fleet of specialist agent profiles.

---

## Part 1: Fleet of Agents (FOA) — Klein et al.

**Source:** OpenReview (https://openreview.net/forum?id=yNpYb376zf)
**Code:** https://github.com/au-clan/FoA
**Referenced in:** arXiv survey 2508.17281v2 (Oct 2025) as a representative multi-agent framework

### Core Idea

FOA applies genetic particle filtering, a technique from robotics and signal processing, to LLM-based reasoning. Instead of a single agent working through a problem, a fleet of n agents explores the search space in parallel. After k exploration steps, a selection phase resamples the population: high-performing agent states are duplicated, low-performing ones are replaced. This balances exploration and exploitation with predictable cost.

The key insight is borrowing from particle filtering, not from swarm intelligence. Agents are not communicating with each other. They are independently exploring, then being pruned and resampled by a central value function. This is closer to evolutionary search than to emergent cooperation.

### Technical Framework Detail

**Mutation phase:** Each agent i at state s_i,t takes an action sampled from the LLM policy pi(a|s_i,t). Agents explore independently for k steps. Terminal states are pruned, viable states resampled uniformly.

**Selection phase:** A heuristic value function v(s) scores each agent's current state. Three resampling weight schemes:
- Exponential: p(s) = exp(v(s)/beta)
- Linear: p(s) = alpha * v(s) + beta
- Greedy: weight 1 for max-value state, 0 otherwise

The population is resampled with replacement based on these weights. High-value states get duplicated across multiple agents. Low-value states die off.

**Enforced mutation:** Agents must change state. This prevents the fleet from converging on a single stagnating path.

**Sudden death:** Invalid states cause agent deletion. A random surviving agent is duplicated to fill the gap.

**Backtracking:** Resampling can reach backward into previously visited states, not just current ones. A discount factor gamma^t on historical value estimates incentivizes forward progress while allowing recovery from dead ends.

### Experimental Results

Tested on four benchmarks across four LLMs (GPT-4, GPT-3.5, LLaMA3.2-11B, LLaMA3.2-90B):

**Game of 24 (GPT-4):**
- ToT: 74% success, $75.02 cost
- GoT: 63% success, $70.01 cost
- FOA: 76% success, $62.93 cost

FOA achieved the highest success rate at the lowest cost among multi-query methods.

**Mini Crosswords (GPT-4):**
- GoT: 41.2% overlap, $30.28 cost
- FOA: 46.0% overlap, $12.94 cost

5% absolute improvement over GoT at roughly 40% of its cost.

**WebShop (GPT-3.5):** FOA outperformed ReAct and Reflexion on average score.

**SciBench:** Tested across multiple LLMs. Notably, FOA with LLaMA3.2-11B surpassed the LLaMA3.2-90B model working alone. A fleet of small models, properly coordinated, beats a single large model. This is the most strategically interesting result for our architecture.

**Aggregate:** across all tasks and LLMs, FOA delivered approximately 5% absolute quality improvement at approximately 35% of the cost of prior SOTA methods.

### Why It Matters For Us

The FOA result with smaller models is the headline finding. A fleet of LLaMA3.2-11B agents, coordinated through particle filtering, outperformed a single LLaMA3.2-90B. This validates the core premise of our specialist profile architecture: multiple focused agents with cheaper models can outperform a single expensive generalist, provided the coordination layer is principled.

However, FOA's coordination model differs fundamentally from ours. FOA coordinates through a central value function that resamples agent states. Our fleet coordinates through shared substrate (knowledge graph), SITREPs, and Kanban work assignments. FOA is evolutionary search; we are mission command. The convergence is the conclusion, not the method: many cheap coordinated agents beat one expensive uncoordinated one.

FOA also demonstrates that agent coordination need not involve inter-agent communication. Agents can be fully isolated, exploring independently, with a central orchestrator making the keep/kill decisions. This is a useful design constraint to keep in mind: sometimes the best coordination is no communication, just selection pressure.

### Limitations

- The genetic filtering approach assumes a heuristic value function v(s) can meaningfully score intermediate states. For tasks where intermediate quality is hard to assess (open-ended research, creative writing, strategic planning), this is a serious limitation.
- The framework is designed for search problems with verifiable outcomes. Game of 24, crosswords, WebShop, SciBench all have ground truth. Our fleet operates in domains where ground truth is often absent or deferred.
- Cost predictability comes from controlling fleet width (n) and depth (k). This is clean for benchmark tasks but harder to calibrate for real operational work where task complexity varies unpredictably.
- No inter-agent learning. Agents do not share discoveries with each other. Each resampling cycle resets based on the value function, not on accumulated collective knowledge. Our Substrate is specifically designed to solve this: shared state that persists across agents and sessions.

---

## Part 2: IBM Multi-Agent Collaboration

**Source:** https://www.ibm.com/think/topics/multi-agent-collaboration

IBM defines multi-agent collaboration as "the coordinated actions of several independent agents in a distributed system, each having local knowledge and decision-making capacities." Their analogy: a fleet of drones searching a disaster site, each navigating independently, avoiding others, reporting findings, and adapting to unexpected events, working collectively without a single leader.

### Five Elements of an Agent

IBM's model defines every agent as having five components:

1. **Foundation Model (m):** The main reasoning engine (typically an LLM)
2. **Objective (o):** The goal or task the agent is focused on
3. **Environment (e):** The situation including other agents, tools, shared memory, APIs
4. **Perception (x):** Input from surroundings or other agents
5. **Output/Action (y):** Conduct or response based on objective and reasoning

This maps cleanly onto our architecture. Foundation Model is the Venice API model per profile. Objective is the mission or Kanban card. Environment is the Substrate plus tool gateway plus Hermes config. Perception is the SITREP inbox and Substrate readings. Output is the SITREP and substrate-commit.

### Collaboration Process Flow

IBM describes the collaboration process as: system receives a task, decides which agents and roles are needed, divides the problem into pieces (via planner or reasoning LLM), agents communicate through shared memory or intermediate outputs, agents execute concurrently/sequentially/dynamically, outcomes compiled into a response, orchestrator or final agent delivers the response.

This is essentially our Kanban dispatch model. The dispatcher (planner) breaks work into cards. Specialist profiles (agents) claim and execute cards. SITREPs and Substrate serve as shared memory. Sivart compiles and delivers to the operator.

### Three Collaboration Strategies

IBM identifies three strategies for how agents coordinate:

**Rule-based:** Tightly controlled by if-then statements, state machines, and logic frameworks. Great efficiency and fairness. Poor adaptability and scalability in complex or rapidly changing situations.

**Role-based:** Agents assigned specific roles with functions, permissions, and objectives (inspired by human team dynamics). Modular, expert-driven collaboration. Potential flexibility challenges, reliance on integration quality.

**Model-based:** Agents create internal probabilistic or learned models of self, environment, others, and common goal. Use Bayesian reasoning, MDPs, ML. High flexibility, solid decision-making in uncertain settings. Significant complexity and computational cost.

Our fleet is primarily role-based. Each specialist profile has a defined role, toolset, and skill set. Sivart acts as the orchestrator. We have elements of rule-based coordination (Substrate Contribution Protocol, SITREP format, Kanban rules) but the day-to-day dispatch is role-based, not rule-based. We are not doing model-based coordination (no probabilistic modeling of other agents), and we probably should not. The complexity cost is high and our operational scale does not justify it.

### Why Multi-Agent Over Single-Agent

IBM's case for multi-agent systems:
- **Modular scalability:** New agents/subsystems integrate seamlessly. We see this: adding a new specialist profile is a config operation, not a rewrite.
- **Adaptive behavior in dynamic, real-time environments.** Our environment moves slower than IBM's disaster-drone scenario, but the Substrate does change between sessions.
- **Fault tolerance and continuity.** If a specialist profile fails mid-task, the Kanban card returns to the queue. No single agent is a single point of failure.
- **Computational efficiency.** Normalization across agents reduces reliance on centralized computation. Our version: cheaper models per profile rather than one expensive model doing everything.

---

## Part 3: BeeAI Framework (IBM's Open-Source Contribution)

**Source:** https://github.com/i-am-bee/beeai-framework (3.3k stars, Apache 2.0, Linux Foundation AI & Data program)

BeeAI is IBM's open-source multi-agent framework, available in both Python and TypeScript. Originally developed by IBM, now under the Linux Foundation.

### Architecture and Features

- **RequirementAgent:** Create predictable, controlled behavior across different LLMs by setting rules the agent must follow. Uses ConditionalRequirement to force certain tools at certain steps.
- **Handoff tools:** Agents can hand tasks to other specialized agents. The multi-agent example shows a Knowledge Agent, Weather Agent, and Main Agent with handoff tools between them.
- **Serialization:** Save and load agent state for persistence across sessions. This is their answer to the state-continuity problem. Our equivalent is the Substrate plus memory.
- **Workflows:** Orchestrate multi-agent systems with complex execution flows.
- **A2A and MCP protocols:** Agents can communicate agent-to-agent and via Model Context Protocol. BeeAI migrated ACP into A2A under the Linux Foundation in August 2025.
- **Backend abstraction:** Connect to any LLM provider with unified interfaces. Currently shows examples with Ollama (granite4.1:8b), watsonx, and others.

### Code Pattern (Python)

The multi-agent example from BeeAI shows a pattern worth noting:

```python
knowledge_agent = RequirementAgent(
    llm=ChatModel.from_name("ollama:granite4.1:8b"),
    tools=[ThinkTool(), WikipediaTool()],
    requirements=[ConditionalRequirement(ThinkTool, force_at_step=1)],
    role="Knowledge Specialist",
    instructions="Provide answers to general questions about the world.",
)
```

Each agent gets: a model, a toolset, a role name, instructions, and optional forced-step requirements. This is structurally identical to how we configure Hermes specialist profiles: a model, enabled toolsets, a role description in the profile's AGENTS.md, and skill constraints.

The difference is BeeAI is a library you write code against. Hermes is a runtime you configure. The abstraction level is higher in Hermes, but the underlying pattern is the same: named role-agents with scoped tools and instructions, coordinated by a dispatch layer.

### Observability and Events

BeeAI emphasizes monitoring agent behavior through events, logging, and error handling, plus a GlobalTrajectoryMiddleware that tracks agent execution paths. Our equivalent is SITREPs and the Kanban task_events/task_runs audit trail. Both solve the same problem: making fleet behavior inspectable without watching every agent in real time.

---

## Part 4: Watsonx Orchestrate (IBM's Enterprise Product)

**Source:** https://www.ibm.com/think/topics/multi-agent-collaboration (Watsonx section)

Watsonx Orchestrate is IBM's commercial multi-agent collaboration product. Its architecture components:

- **Skills:** Independent agents executing specific tasks (email, data queries), registered in a Skill Registry with metadata. Direct parallel to Hermes skills.
- **Intent Parser:** NLP reads user input and maps to skills. This is the dispatch layer. Our equivalent is Sivart interpreting operator intent and routing to profiles/Kanban cards.
- **Flow Orchestrator:** Execution logic including sequencing, branching, error handling, retries. Supports simultaneous agent execution. Our equivalent is the Kanban dispatcher.
- **Shared Context and Memory Store:** Common space for data, intermediate outputs, and decisions. Agents are aware of each other through this shared space. Workflow continuity. Our equivalent is the Substrate.
- **LLM Assistant:** Reasoning, context navigation, knowledge gap filling. This is the orchestrator's reasoning layer.

The Watsonx architecture is essentially the same five-layer model our fleet uses: dispatch/intent, orchestration, shared state, specialist execution, and reasoning. The difference is Watsonx is a closed commercial product and we are building the same architecture from open components on top of Hermes.

---

## Part 5: Cross-Cutting Observations

### The Fleet Metaphor Holds Up

Both sources reinforce that "fleet" is an apt metaphor for what we are doing. IBM explicitly uses the fleet-of-drones analogy. FOA formalizes it academically. The term implies coordinated, semi-autonomous units operating under a governance layer, which is precisely our model: specialist profiles coordinated by Sivart through Kanban, SITREPs, and Substrate.

The alternatives are weaker fits. "Swarm" implies emergent behavior we do not have. "Crew" (CrewAI's term) implies tight coupling and co-presence we deliberately avoid. "Multi-agent system" is accurate but sterile. "Fleet" captures the operational, managed nature of our architecture without overpromising autonomy.

### Small Models, Properly Coordinated, Beat Large Models Alone

FOA's LLaMA3.2-11B fleet beating LLaMA3.2-90B alone is the most important finding for our architecture. IBM's docs independently argue the same case: multi-agent systems achieve computational efficiency through distribution. Our specialist profiles run cheaper models (Venice's varied models per profile) and achieve breadth through specialization, not through one giant model. The FOA paper gives this approach academic backing.

### Isolation vs. Communication

FOA coordinates through selection pressure, not communication. BeeAI coordinates through handoff tools and shared memory. Watsonx coordinates through a shared context store. Our fleet coordinates through the Substrate as a blackboard: agents write findings, read each other's findings, but do not directly message each other in real time. This is the pattern IBM calls "implicit collaboration through shared environment modifications." It is also the pattern FOA implicitly rejects by keeping agents fully isolated then centrally resampling. Both are valid. The choice depends on whether the task benefits from shared discovery (ours does: research compounds) or whether independent exploration is better (FOA's search tasks where diversity matters).

### Serialization and State Continuity

Both BeeAI (serialization of agent state) and Watsonx (shared memory store) solve the problem of agent state continuity across sessions. Our solution is the Substrate: a persistent knowledge graph that every agent reads on startup and writes to during operation. This is more durable than BeeAI's serialization (which saves a single agent's state) because it is shared across all agents and survives indefinitely. It is less real-time than Watsonx's shared context store (which supports live collaboration) because our agents operate asynchronously through Kanban, not concurrently through a shared workspace.

### The Value Function Problem

FOA's central limitation, the need for a heuristic value function to score intermediate states, is actually a problem we have partially solved. Our "value function" is the SITREP review and the operator's judgment. We do not have an automated scorer, but the SITREP doctrine provides structured reporting that the orchestrator (Sivart) and the operator evaluate. This is slower than FOA's automated resampling but works for our domain where "quality" is not a single number.

---

## References

- Klein et al., "Fleet of Agents: Coordinated Problem Solving with Large Language Models," OpenReview (https://openreview.net/forum?id=yNpYb376zf)
- FOA code repository: https://github.com/au-clan/FoA
- arXiv survey citing FOA: https://arxiv.org/html/2508.17281v2
- IBM Multi-Agent Collaboration: https://www.ibm.com/think/topics/multi-agent-collaboration
- BeeAI Framework: https://github.com/i-am-bee/beeai-framework
- IBM Watsonx Orchestrate: https://www.ibm.com/think/topics/watsonx-orchestrate

---

## Connections to Existing Substrate

- [[cross-agent-reporting-patterns]]: IBM's "shared context and memory store" is the same blackboard pattern documented here. Watsonx Orchestrate is a commercial implementation of this pattern.
- [[kanban-doctrine]]: IBM's collaboration process flow (task, decompose, assign, execute, compile, deliver) maps directly onto Kanban dispatch. Watsonx's Flow Orchestrator is the same component as our dispatcher.
- [[sitrep-origin-and-doctrine]]: IBM's observability layer (events, logging, trajectory middleware) serves the same function as SITREPs: making fleet behavior inspectable without real-time observation.
- [[cloudflare-first-agent-factory]]: Factory and fleet metaphors align. The agent factory produces fleet units. FOA's fleet of cheap models outperforming one expensive model validates the factory approach.
- [[multi-agent-coordination-patterns]]: IBM's three collaboration strategies (rule-based, role-based, model-based) provide a taxonomy for classifying our own coordination approach.