# Agent Architectures

## The Landscape

Every LLM agent architecture answers one question: how should the model decide what to do next? The answers range from "one step at a time" to "plan everything first" to "try many paths and pick the best." Each makes different tradeoffs between latency, cost, reliability, and capability.

## Core Architectures

### ReAct (Reasoning + Acting)

**How it works:** The model alternates between thinking (Thought) and doing (Action), observing results before deciding the next step. Each cycle: Thought → Action → Observation → repeat.

**Example flow:**
```
Thought: I need to find the user's last email about Project X
Action: search_email(query="Project X")
Observation: Found 3 emails, most recent from March 5...
Thought: Now I should summarize the key points
Action: respond(summary="...")
```

**When to use:** Most general tasks. Default choice for single-agent systems. Works well when the task unfolds naturally and doesn't require deep planning.

**Tradeoffs:**
- ✅ Simple, robust, well-understood
- ✅ Naturally handles uncertainty (observe and adapt)
- ✅ Low overhead per step
- ❌ Can wander: no global plan means it may take inefficient paths
- ❌ Struggles with tasks requiring coordinated multi-step strategy
- ❌ Each step is myopic: optimizes locally, not globally

**Key insight:** ReAct is the workhorse. It's what most deployed agents actually use because it's reliable enough and simple enough to debug. OpenAI's function calling, Anthropic's tool use, LangChain agents: all fundamentally ReAct variants.

### Plan-and-Execute

**How it works:** First, create a complete plan (sequence of steps). Then execute each step. Optionally re-plan if something changes. Often implemented as two models or two prompts: a planner and an executor.

**Example flow:**
```
Plan:
1. Search for relevant files
2. Read the most relevant file
3. Extract key information
4. Write summary to output file
5. Commit changes

Execute step 1...
Execute step 2...
[Re-plan if step 2 revealed unexpected structure]
```

**When to use:** Complex, multi-step tasks where the overall strategy matters. Software engineering, research synthesis, project planning.

**Tradeoffs:**
- ✅ Global coherence: each step serves the whole
- ✅ Can estimate cost/time upfront
- ✅ Easier to debug (plan is inspectable)
- ❌ Planning costs tokens before any work happens
- ❌ Plans go stale: reality diverges from assumptions
- ❌ Re-planning is expensive and risks infinite loops
- ❌ Requires the model to be good at planning (many aren't)

**Key insight:** Plan-and-execute shines for well-defined tasks in known domains. It struggles when the task itself is ambiguous or the environment is unpredictable. The best implementations are "plan loosely, execute tightly": sketch a direction, then use ReAct for each step.

### Reflection / Self-Critique

**How it works:** After generating output, the model critiques its own work and iterates. Can be single-model (prompt the same model to review) or dual-model (separate critic).

**Patterns:**
- **Reflexion** (Shinn et al., 2023): Agent acts, evaluates outcome, generates verbal reflection, retries with reflection in context
- **Self-refine**: Generate → Critique → Refine loop
- **Constitutional AI style**: Check output against principles, revise

**When to use:** Tasks where quality matters more than speed. Writing, code review, analysis. Anywhere "good enough on first try" isn't good enough.

**Tradeoffs:**
- ✅ Catches errors the first pass missed
- ✅ Can improve without external feedback
- ✅ Natural way to implement quality standards
- ❌ 2-3x token cost (generate + critique + revise)
- ❌ Models are often bad at finding their own mistakes
- ❌ Can over-correct: nitpick good work into something worse
- ❌ Diminishing returns after 1-2 iterations

**Key insight:** One round of reflection is almost always worth it. Two rounds sometimes. Three rounds almost never. The model's ability to critique is bounded by the same capabilities that produced the original output. External signals (test results, user feedback) are more valuable than self-critique.

### Tree of Thought (ToT)

**How it works:** Instead of a single chain of reasoning, explore multiple reasoning paths simultaneously. Branch at decision points, evaluate each branch, prune bad ones, continue with promising ones. Think: breadth-first or best-first search over reasoning chains.

**When to use:** Problems with multiple valid approaches where the best one isn't obvious. Puzzles, creative tasks, mathematical proofs, strategic decisions.

**Tradeoffs:**
- ✅ Explores solution space more thoroughly
- ✅ Can find solutions that linear reasoning misses
- ✅ Naturally handles ambiguity
- ❌ Dramatically higher cost (proportional to branching factor × depth)
- ❌ Requires good evaluation of partial solutions (hard!)
- ❌ Overkill for most practical tasks
- ❌ Difficult to implement well

**Key insight:** ToT is academically interesting but rarely practical for agent systems. The cost explosion is real. Most agent tasks don't benefit from exploring 5 approaches when one would do. Where it does help: selecting between architectural approaches, debugging when the root cause is unclear.

### LATS (Language Agent Tree Search)

**How it works:** Combines ToT with Monte Carlo Tree Search (MCTS). Uses the LLM as both the policy (what to try next) and the value function (how good is this state). Builds a search tree, uses UCB1 or similar for exploration-exploitation balance.

**When to use:** Complex reasoning tasks where you can afford high compute. Competitive programming, hard math, complex code generation.

**Tradeoffs:**
- ✅ State-of-the-art on hard reasoning benchmarks
- ✅ Principled exploration (not just random branching)
- ✅ Can leverage environment feedback (test cases, etc.)
- ❌ Very expensive: many LLM calls per solution
- ❌ Requires well-defined success criteria for value estimation
- ❌ Complex to implement correctly
- ❌ Latency is prohibitive for interactive use

**Key insight:** LATS represents the frontier of "throw compute at it" approaches. It works when you have clear success criteria (tests pass, proof checks out) and can afford 10-50x the compute of a single attempt. Not for conversational agents. Potentially valuable for automated software engineering pipelines where correctness is paramount.

## Hybrid Approaches (What Actually Works)

The best production agents don't use a single architecture. They combine patterns:

1. **ReAct + Reflection:** Do the work reactively, then review. This is what Claude Code and Cursor effectively do: act, check, fix.

2. **Plan-and-Execute + ReAct:** Plan at the high level, ReAct for each step. LangGraph's plan-and-execute template does this.

3. **ReAct + Selective ToT:** Use linear reasoning by default, branch only at genuine decision points. Cost-efficient exploration.

4. **Hierarchical:** An orchestrator plans and delegates to specialist ReAct agents. This is what multi-agent frameworks (CrewAI, AutoGen) implement.

## What We Should Use

For Sivart's architecture, the answer is clear:

**Primary: ReAct with structured reflection.** This is what we already do (AGENTS.md's process is essentially a structured ReAct loop with built-in checkpoints). The tool-use pattern with observation-action cycles is battle-tested.

**Layer on: Lightweight planning for complex tasks.** When a task has >5 steps or involves multiple files, sketch a plan first. But keep it loose: 3-5 bullet points, not a detailed spec.

**Add: One round of reflection for high-stakes output.** Reports, external communications, architectural decisions. Not everything: the cost isn't worth it for routine file edits.

**Skip: ToT and LATS.** Not worth the complexity for our use case. We're not doing competitive programming. If we need to explore multiple approaches, we can do it explicitly (try approach A, if it fails, try B) which is cheaper and more debuggable.

**The real insight:** Architecture matters less than tool design and prompt structure. A well-prompted ReAct agent with good tools beats a sophisticated LATS agent with bad tools every time. Invest in the tools and the context, not the meta-reasoning framework.
