---
title: Designing loops with Fable 5
source: https://x.com/RLanceMartin/status/2064397389189071163
ingested: 2026-06-10
tags: [agent, loop, fable, claude, anthropic, self-correction, memory, managed-agents]
related: [[loops-x-conversation-june-2026]], [[goal-primitive]], [[harness-engineering]], [[karpathy-autoresearch]], [[agent-memory]], [[context-stack]]
---

# Designing loops with Fable 5

> Original article by Lance Martin (@RLanceMartin), Anthropic engineer. Published on X, June 9, 2026. This raw file captures the full article text from an archived mirror plus supporting technical context.

---

## Source Article (Full Text)

**Self-correction loops: Letting models self-correct in feedback**

Recently, many people have started paying attention to "loops." @bcherny said his work is essentially "writing loops." In Claude Code this corresponds to `/goal`; in Claude Managed Agent it corresponds to Outcomes. Both are concrete implementations of the same general idea: give the model a goal or scoring standard, let it collect feedback in a running environment, self-correct, until the goal is achieved.

Fable 5 stands out in these kinds of loops because it actually adjusts its strategy based on feedback each iteration, rather than mechanically repeating.

**Parameter Golf Experiment**: This is an open-source ML engineering challenge: train the best model possible within the constraints of a 16MB artifact, 10 minutes, and 8xH100. Similar to Karpathy's AutoResearch project, it tests the Agent's ability to edit training code, launch training, read logs, judge, and make next-step decisions in a complete loop.

Using Claude Managed Agent (CMA), this challenge was run on both Fable 5 and Opus 4.7. Key design: a verifier sub-Agent independently scores (makes judgments in an isolated context window), rather than having the model self-critique its own output. The latter has been proven ineffective multiple times. The Outcomes grader stops only when all experimental criteria are met.

**Results**: Fable 5 achieved approximately **6x improvement** over Opus 4.7 in the training pipeline. Breaking it down, Opus 4.7 produced a small gain in its first experiment, then almost all subsequent experiments spun in the same template: adjust one scalar, test, keep if positive. Fable 5, in contrast, made larger structural bets (changing architecture rather than tuning constants), and did not give up when hitting quantization regression, pushing all the way to maximum gain.

**Memory: The outer loop across Sessions**

Memory is another area where Fable 5 is significantly stronger than previous models. It can be understood as an outer loop that spans Sessions: the model writes memory during a Session, and that memory can be retrieved in future Sessions.

**Continual Learning Bench 1.0 Test**: A benchmark released by @pgasawa's team, where one task examines whether an Agent can answer sequentially-related questions given filesystem memory. Each question is an independent Agent Session.

Using CMA's memory feature (a filesystem shared across Sessions), Fable 5, Opus 4.7, and Sonnet 4.6 were tested. The results are clearly stratified:

- **Sonnet 4.6** stayed at Step 1: its storage contained only failure notes and guesses ("maybe should use prc instead of prc_usd?"), rarely actively consulting previous records, needing task-specific memory instructions to improve performance.
- **Opus 4.7** reached around Step 3: created schema references with uncertainty markers ("possibly in cents? needs verification"), but verification coverage was low, 7-33% (median ~17%).
- **Fable 5** could complete the entire path: strongest runtime verification coverage reached 73% (22 out of 30 questions), and could distill what was learned into general rules for future tasks.

Effective memory use follows a progression chain: **failure recording → investigating cause → verifying diagnosis → distilling into general rules → consulting rules rather than re-deriving**. Previous models had breakpoints in this chain; Fable 5 is currently the only one that can stably complete it.

**Core Conclusion**

Rather than directly prompting and steering Fable 5, it is better to design loops that let it self-correct through environmental feedback (via /goal or Outcomes), and manage its own context window through memory.

This is not a new paradigm, but Fable 5 makes it actually land.

---

## Technical Context: Claude Managed Agents

Lance Martin's article references Claude Managed Agents (CMA), Anthropic's pre-built agent harness for long-running tasks. CMA provides the infrastructure for autonomous agent loops without requiring the user to build their own.

### Core Concepts (from Anthropic docs, 2026-04-01 beta)

| Concept | Description |
|---------|-------------|
| **Agent** | The model, system prompt, tools, MCP servers, and skills |
| **Environment** | Where sessions run: Anthropic-managed cloud sandbox or self-hosted |
| **Session** | A running agent instance performing a specific task |
| **Events** | Messages exchanged between application and agent |

### How It Works

1. Create an agent (model, prompt, tools, MCP, skills) once, reference by ID
2. Create an environment (cloud or self-hosted sandbox)
3. Start a session referencing agent and environment
4. Send events; Claude autonomously executes tools and streams results via SSE
5. Steer or interrupt mid-execution

### Built-in Tools

- Bash: Run shell commands in sandbox
- File operations: Read, write, edit, glob, grep
- Web search and fetch
- MCP servers: Connect to external tool providers

### Key Feature: Outcomes

The "Outcomes grader" mentioned in the article is part of CMA's mechanism for defining stopping conditions. A verifier sub-Agent evaluates whether the task meets defined criteria, operating in an isolated context window to avoid self-critique bias.

---

## Related Entities and Concepts

- **Lance Martin**: Anthropic engineer, contributor to the Anthropic Cookbook (github.com/rlancemartin/anthropic-cookbook)
- **Boris Cherny (@bcherny)**: Creator of Claude Code, Anthropic. Defined the "loop" abstraction at Acquired Unplugged (June 2, 2026): "My job is to write loops." See also [[loops-x-conversation-june-2026]].
- **Fable 5**: "Mythos-class" model from Anthropic. The article notes it is part of the "Fable" model family, distinguished by stronger self-correction and memory capabilities compared to Opus 4.7 and Sonnet 4.6.
- **Parameter Golf**: Open-source ML engineering challenge. Constraints: 16MB artifact, 10 minutes, 8xH100. Tests agent loop capabilities: edit training code, launch training, read logs, judge, decide next step. Parallel to Karpathy's AutoResearch.
- **Continual Learning Bench 1.0**: Benchmark from @pgasawa's team testing agent memory across independent sessions with filesystem persistence.
- **Karpathy AutoResearch**: Autonomous LLM pretraining loop with constraint architecture (one file to edit), fixed 5-minute budget, NEVER STOP autonomy. See [[karpathy-autoresearch]].

---

## Synthesis Notes (for findings)

This article is a significant data point in the agent loop discourse because it comes from inside Anthropic and includes controlled experiment results comparing Fable 5 to previous Claude models.

### Key Findings for Synthesis

1. **Verifier Pattern Validated**: The article confirms that self-critique (model evaluating its own output) is inferior to an isolated verifier sub-Agent. This aligns with the generator-critic pattern documented in [[subagent-architecture]].

2. **Structural vs. Scalar Betting**: The 6x improvement gap between Fable 5 and Opus 4.7 in Parameter Golf is explained by strategic depth. Opus made scalar adjustments (tune one constant, test, keep if positive). Fable 5 made structural bets (change architecture) and persisted through quantization regression. This suggests model capability determines not just loop execution but loop strategy quality.

3. **Memory as Outer Loop**: The Continual Learning Bench results stratify three models across a five-step memory progression chain. Only Fable 5 completes all five steps. This is evidence that memory is not merely storage but a recursive loop mechanism: failure → investigation → verification → rule distillation → rule consultation.

4. **Loop Design > Prompting**: The core thesis echoes Boris Cherny's claim and Peter Steinberger's viral tweet. The shift from "prompting agents" to "designing loops" is now backed by internal Anthropic experiments with quantitative results.

5. **Model Class Distinction**: The article explicitly contrasts "Mythos-class models like Claude Fable 5" with previous generations. This suggests Anthropic is using model class nomenclature (Sonnet, Opus, Fable/Mythos) to signal capability tiers relevant to loop-based workflows.

---

## Cross-References to Existing Substrate Content

- [[loops-x-conversation-june-2026]]: The broader loop lineage (ReAct → AutoGPT → Ralph → /goal → orchestration). Boris Cherny's definition. Steinberger's skill thesis.
- [[goal-primitive]]: `/goal` as emerging coordination primitive. The article confirms `/goal` as Anthropic's loop primitive in Claude Code.
- [[harness-engineering]]: Designing environments and feedback loops for agent reliability. CMA is Anthropic's harness.
- [[karpathy-autoresearch]]: Constraint architecture, fixed budgets, autonomous loops. Parameter Golf is a similar challenge.
- [[agent-memory]]: From flat files to structured continuity. The memory progression chain in this article provides empirical validation.
- [[context-stack]]: Portable identity for agents. Memory across sessions is a precondition for context-stack portability.
- [[subagent-architecture]]: Verifier sub-Agent pattern (generator-critic) confirmed effective.
- [[centaur-principle]]: Human + AI + process. Lance Martin designs loops; Fable 5 executes within them.

---

## Source URLs

- Original tweet: https://x.com/RLanceMartin/status/2064397389189071163
- Article archive (SOTA Sync): https://sotasync.com/reader/2026-06-10-designing-loops-with-fable-5/
- Anthropic Cookbook: https://github.com/anthropics/anthropic-cookbook
- Claude Managed Agents docs: https://platform.claude.com/docs/en/managed-agents/overview
- Lance Martin GitHub: https://github.com/rlancemartin
