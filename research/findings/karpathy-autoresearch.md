---
title: "Karpathy Autoresearch: Agent-Native LLM Pretraining as Autonomous Experiment Loop"
tags:
  - finding
  - agent-native
  - karpathy
  - autoresearch
  - llm-training
  - experiment-loop
  - auftragstaktik
  - skills-as-portable-knowledge
  - proof-of-work
  - goal-primitive
related:
  - goal-primitive
  - proof-of-work
  - kanban-doctrine
  - agent-memory
  - harness-engineering
  - skills-as-portable-knowledge
  - dark-factory
  - lean-doctrine
  - production-paradigms
  - cloudflare-first-agent-factory
source: research/raw/karpathy-autoresearch.md
ingested: 2026-05-22
---

# Karpathy Autoresearch: Agent-Native LLM Pretraining as Autonomous Experiment Loop

## Core Idea

Andrej Karpathy's `autoresearch` repository treats an LLM training setup as an autonomous research organism. The agent receives a single-GPU environment, a single editable file (`train.py`), and a fixed 5-minute wall-clock time budget per experiment. It iterates overnight: modify, train, measure, keep or discard, repeat. The human shapes strategy via `program.md`; the agent handles tactics. This is the most concrete production implementation of an autonomous agent loop yet published.

## Architecture: Deliberate Constraint Design

| File | Role | Modified By |
|------|------|-------------|
| `prepare.py` | Fixed constants, data prep, tokenizer, dataloader | Human — read-only for agent |
| `train.py` | Full GPT model, optimizer, training loop | Agent — the only file edited |
| `program.md` | Skill-like governance document for the agent | Human — the strategy layer |

This is constraint architecture: one file to modify, one metric (`val_bpb`, lower is better), one instruction document. The 5-minute wall-clock budget makes experiments directly comparable regardless of architecture changes, because time, not steps, is the normalization variable.

## The Agent Loop

1. Agree on a run tag, create branch `autoresearch/<tag>`
2. Inspect current git state and `train.py`
3. Propose and implement an experimental change
4. Commit, run `uv run train.py` for 5 minutes
5. Extract `val_bpb` and `peak_vram_mb` from output
6. Record in `results.tsv`: commit hash, metric, memory, status, description
7. If improved: advance branch (keep commit)
8. If equal or worse: `git reset` back

Critical autonomy instruction: "NEVER STOP." The agent does not ask permission. It runs until manually interrupted. This is [[kanban-doctrine]] at the research level: intent is set, execution is autonomous.

## Technical Specifications

**Model:** Derived from nanochat, single-GPU, simplified for fast iteration.
- Config defaults: 2048 seq len, 32768 vocab, 12 layers, 6 heads, 768 dim
- RMSNorm, ReLU-squared activation, RoPE position embeddings
- Value embeddings on alternating layers (ResFormer pattern)
- Per-layer residual scalars (`resid_lambdas`, `x0_lambdas`)
- Softcap logits at 15
- "SSSL" window pattern: sliding short/long attention layers

**Optimizer: MuonAdamW**
- Muon (orthogonalized updates) for 2D matrix parameters
- AdamW for embeddings, scalars, and lm_head
- Per-parameter-group learning rates scaled by `1/sqrt(dmodel/768)`
- Schedules: LR warmup/flat/warmdown, momentum ramp, decaying weight decay

**Training loop:**
- Total batch size: ~524K tokens (2^19)
- Flash Attention 3 (Hopper-native, community fallback on other GPUs)
- `torch.compile` with `dynamic=False`
- GC disabled after step 0 to avoid ~500ms stalls
- Compilation excluded from time budget (only steps > 10 count)
- Fast fail on NaN or loss > 100

**Data:** `karpathy/climbmix-400b-shuffle` on HuggingFace. BPE tokenizer via rustbpe, GPT-4 style split pattern, vocab 8196. Best-fit document packing with 100% utilization, no padding.

## Agent-Native Design Patterns

**Skill as Governance:** `program.md` is described as a "super lightweight skill." Natural language instructions govern agent behavior. This validates the [[skills-as-portable-knowledge]] concept: the skill file is the governance layer, the code is the execution layer.

**Incomplete Contract + Delegation:** `program.md` specifies the goal (lower `val_bpb`), constraints (single file, no new deps, fixed budget), and autonomy level. The agent fills execution details. This maps directly to [[goal-primitive]] and [[management-by-objectives]]: principal specifies intent, agent handles implementation.

**Branch as Proof of Work:** Each run gets a dedicated branch. The branch history encodes the experiment trajectory: advances on success, resets on failure. This is a version-controlled proof-of-work chain, linking to [[proof-of-work]] and [[github-as-memory]]: the branch is the ledger of attempted improvements.

**Fixed Budget as Normalization:** The 5-minute wall-clock budget makes results comparable across architectural changes. This parallels evaluation design in [[harness-engineering]]: fixed conditions, comparable metrics.

**Human-AI Symbiosis:** The human edits `program.md` (the skill/strategy layer). The agent edits `train.py` (the execution/tactical layer). The human shapes the org; the agent executes within it. This is the same Teacher + AI TA structure applied to research rather than education.

**Autonomous Loop with No Human in the Loop:** The "NEVER STOP" instruction removes the human from the loop entirely once started. This is [[kanban-doctrine]] at the agent level: the agent receives intent and operates independently until mission complete or interrupted. The human is the commander who issues the intent; the agent is the subordinate who executes with disciplined initiative.

## Comparison to Other Agent Loops

| Dimension | Autoresearch | Typical agent coding tools |
|-----------|-------------|---------------------------|
| Goal metric | Single scalar (`val_bpb`) | Often vague or multi-objective |
| Time budget | Fixed wall-clock (5 min) | Usually token/step budget or none |
| Scope | One file (`train.py`) | Often open-ended file tree |
| Reset mechanism | `git reset` on failure | Usually manual undo |
| Logging | Structured TSV with commit linkage | Often unstructured or absent |
| Human role | Edit `program.md` only | Frequent intervention |

This discipline makes autoresearch more like a [[dark-factory]]: lights-out, self-correcting, measurable. The constraint design is what enables the autonomy.

## Platform and Community

- Primary: single NVIDIA GPU (tested on H100)
- Community forks: macOS (MLX), Windows (RTX), AMD
- Karpathy's recommendation for smaller platforms: TinyStories dataset, reduced vocab, lower depth, simpler window pattern

## Implications for Substrate

Autoresearch is the cleanest existing example of an agent-native research loop. Its principles apply directly to agent factory design:

1. **Constraint architecture enables autonomy.** The narrower the scope, the more autonomy you can safely grant.
2. **Skills as governance documents work.** `program.md` is not code. It is natural language policy that governs agent behavior.
3. **Git branches as experiment ledgers.** Version control is not just for humans. It is the agent's memory of what it tried.
4. **Fixed budgets normalize comparison.** Time-bounded experiments are more comparable than step-bounded ones when architecture changes.
5. **NEVER STOP is a feature, not a bug.** The autonomy instruction is what makes overnight research possible. Human interruption is the stop condition, not agent hesitation.

## Sources

- Original repository: https://github.com/karpathy/autoresearch (commit 228791f, ~March 2026)
- Related tweets: https://x.com/karpathy/status/2029701092347630069 and https://x.com/karpathy/status/2031135152349524125
- Parent: nanochat (multi-platform, Flash Attention 3, broader device support)
- Educational precursor: LLM101n (undergraduate course, currently on hold)
- Related venture: Eureka Labs (AI-native education, Teacher + AI TA model)
