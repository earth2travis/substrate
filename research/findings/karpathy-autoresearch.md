---
title: "Karpathy Autoresearch: Agent-Native Research as Incomplete Contract"
tags: [agents, research, autoresearch, karpathy, mission-contracts, skills, proof-of-work, delegation, incomplete-contract, llm-training]
related:
  - [[karpathy-autoresearch]]
  - [[mission-contracts]]
  - [[kanban-doctrine]]
  - [[skills-as-portable-knowledge]]
  - [[proof-of-work]]
  - [[goal-primitive]]
  - [[eureka-labs]]
  - [[nanochat]]
  - [[management-by-objectives]]
  - [[principal-agent-theory]]
  - [[auftragstaktik-mission-command]]
  - [[agent-native-operations]]
source: research/raw/karpathy-autoresearch.md
---

# Karpathy Autoresearch: Agent-Native Research as Incomplete Contract

## The Core Pattern

Karpathy's autoresearch is a minimal, working implementation of what Substrate calls agent-native operations: a human specifies intent in natural language (`program.md`), an agent executes autonomously (`train.py`), and the system produces a verifiable artifact trail (`results.tsv` + git branch history). The entire setup is three files, one GPU, and one metric. The agent never asks for permission once the loop starts.

This is not a toy. It is a real LLM training pipeline where the agent searches an architectural and hyperparameter space overnight, advancing the branch on improvement and resetting on failure. The human's job is to iterate `program.md`: the "research org code" that governs agent behavior.

## program.md as Mission Contract

`program.md` is a mission contract in everything but name. It specifies:
- **Objective:** Lower `val_bpb`
- **Constraints:** Modify only `train.py`, no new packages, fixed 5-minute budget
- **Autonomy level:** "NEVER STOP. Do NOT ask 'should I keep going?' The human might be asleep."
- **Termination:** Manual interrupt only
- **Verification:** `results.tsv` with keep/discard/crash, git commit hash for every experiment

This maps precisely to the six handoffs in [[mission-contracts]]: the principal (human researcher) delegates the search to the agent, the agent executes with residual control over architectural decisions, and the branch history serves as the agency cost ledger: every experiment is logged, every failure is recorded, every advance is traceable.

The contract is incomplete by design. The human does not specify which experiments to run. The agent must generate its own hypotheses, try them, and evaluate them. This is delegation with intent preservation but not instruction preservation: the agent preserves "get lower val_bpb" but not "try learning rate 0.04 first."

## The Skill Layer

Karpathy explicitly calls `program.md` a "super lightweight skill." This validates the [[skills-as-portable-knowledge]] thesis: a skill is not a library or a framework. It is a natural language governance document that an agent reads to shape its behavior. The skill is the contract. The contract is the skill.

In Hermes terms, `program.md` is equivalent to a SKILL.md file: it contains the context, constraints, and workflow that the agent needs to operate. The difference is that Hermes skills are typically loaded at agent startup, while `program.md` is read per-session and iterated by the human as the research org evolves.

This suggests a convergence: the Mission Contract and the Skill are the same abstraction at different scales. A skill governs a single agent's capabilities. A mission contract governs multi-agent orchestration. Both are natural language governance over code execution.

## Branch as Proof-of-Work Ledger

The experiment loop uses git branches as a ledger:
- Each run gets `autoresearch/<tag>`
- Advances on success (`val_bpb` improved)
- Resets on failure or equal result
- Crash attempts logged in `results.tsv` with commit hash

This is a version-controlled proof-of-work chain. The branch history is the evidence trail. The human can inspect the commit log to see what the agent tried, what worked, and what did not. This is [[proof-of-work]] in practice: the agent's output is not just a model but a verifiable record of the search process.

The `results.tsv` file is the Agency Cost Ledger: every experiment has a cost (time, compute, VRAM) and a payoff (val_bpb delta). The keep/discard/crash labels make the cost explicit. The human can see at a glance what fraction of experiments succeeded, which is exactly the kind of transparency that [[principal-agent-theory]] demands for delegated execution.

## Fixed-Time Budget as Evaluation Normalization

The 5-minute wall-clock budget is a critical design choice. It makes experiments comparable across model size, architecture, and batch size changes. Without this, a larger model would always look worse because it trains slower. With the fixed budget, the metric becomes "what is the best model you can find in 5 minutes?" rather than "how fast can you train to convergence?"

This is a normalization strategy for search in an uncontrolled variable space. It parallels how benchmarks like MMLU or GSM8K fix the evaluation conditions so models can be compared. The difference is that autoresearch applies this principle to the research process itself: the evaluation condition is time, not task.

## The "Never Stop" Instruction and Auftragstaktik

The most aggressive line in `program.md`: "The loop runs until the human interrupts you, period." This is [[auftragstaktik]] at the agent level. The agent receives an Auftrag (mission order) and operates with full autonomy until completion or countermand. The human is the commander who issues intent; the agent is the subordinate who executes with disciplined initiative.

The instruction also includes contingency: "If you run out of ideas, think harder — read papers referenced in the code, re-read the in-scope files for new angles, try combining previous near-misses, try more radical architectural changes." This is the backbrief and shared mental model of Auftragstaktik: the agent is expected to maintain situational awareness and generate its own options, not wait for orders.

## Connection to Eureka Labs and LLM101n

Autoresearch shares structural DNA with [[eureka-labs]] and [[LLM101n]]:
- **Eureka Labs:** Teacher + AI TA symbiosis on a shared platform. Autoresearch is the same pattern applied to research: the human is the Teacher (designs the research org via `program.md`), the agent is the AI TA (executes experiments autonomously).
- **LLM101n:** The course takes students from zero to a functioning ChatGPT-like web app. Autoresearch is the compressed adult version: an agent that already knows the curriculum and now applies it to improve itself.

Karpathy's tweet (March 2026) explicitly frames autoresearch as the beginning of a future where "research is now entirely the domain of autonomous swarms of AI agents running across compute cluster megastructures." The repo is positioned as historical artifact: "This repo is the story of how it all began."

## Implications for Missions.md

Autoresearch provides a concrete reference for what a mission-driven agent execution system looks like at minimum viable scale:

1. **One file for intent (`program.md`)** = the Mission Contract
2. **One file for execution (`train.py`)** = the Work Product
3. **One metric for evaluation (`val_bpb`)** = the Success Criterion
4. **One branch for history** = the Agency Cost Ledger
5. **One log for transparency (`results.tsv`)** = the Proof of Work

For missions.md, this suggests that the simplest possible mission contract is: a markdown file with objective, constraints, autonomy level, and verification method. The agent reads it, executes against it, and produces a verifiable trail. Complexity scales by adding agents, not by adding ceremony.

The autoresearch model also demonstrates that the "human asleep" scenario is not an edge case; it is the design center. The system is built for the human to be absent. This is the same assumption that underlies Hermes Kanban: workers run autonomously, the orchestrator reviews asynchronously.

## Open Questions

- How does autoresearch scale to multi-agent? Karpathy mentions "add more agents to the mix" but the current implementation is single-agent. The branch model works for one agent but would need coordination primitives for multiple agents editing the same file or different files.
- How does the human iterate `program.md`? The current repo provides no guidance on when or how the human should update the skill. Is it after every sleep cycle? When the agent gets stuck? When a new paper is published?
- What is the transfer learning between experiments? The agent starts from scratch on each experiment (git reset on discard). There is no accumulation of partial knowledge across the branch except what the agent retains in its context window. This limits the depth of the search tree.

## Cross-References
- [[karpathy-autoresearch]] — Full raw source and technical deep dive
- [[mission-contracts]] — Multi-agent orchestration via structured intent delegation
- [[kanban-doctrine]] — Auftragstaktik as agent operating system
- [[skills-as-portable-knowledge]] — Skills as instruction sets for agent systems
- [[proof-of-work]] — Verification stack for autonomous agent output
- [[eureka-labs]] — Karpathy's AI-native education venture
- [[goal-primitive]] — /goal as emerging coordination primitive
- [[management-by-objectives]] — Drucker's MBO as incomplete contract
- [[principal-agent-theory]] — Economics of delegation across mission domains
- [[auftragstaktik-mission-command]] — Command by intent rather than instruction
