---
source_url: https://github.com/karpathy/autoresearch
ingested: 2026-05-21
sha256: ef395b591000753ad4aea0487df3d7955a6387d98309b418a489d0efc8be9084
---

# Karpathy autoresearch: Autonomous LLM Pretraining Research Swarm

**Source:** https://github.com/karpathy/autoresearch (commit 228791f, ~March 2026)  
**Author:** Andrej Karpathy  
**License:** MIT  
**Related:** [[nanochat]], [[LLM101n]], [[eureka-labs]], [[goal-primitive]], [[mission-contracts]], [[agent-memory]], [[proof-of-work]], [[kanban-doctrine]]

---

## Premise

Give an AI agent a small but real LLM training setup and let it experiment autonomously overnight. The agent modifies code, trains for 5 minutes, checks if the result improved, keeps or discards, and repeats. The human wakes up to a log of experiments and (hopefully) a better model. The training code is a simplified single-GPU implementation of nanochat. The human does not touch Python files. Instead, they program `program.md`: a Markdown file that provides context to the AI agent and sets up the autonomous research org.

> "One day, frontier AI research used to be done by meat computers in between eating, sleeping, having other fun, and synchronizing once in a while using sound wave interconnect in the ritual of 'group meeting'. That era is long gone." — @karpathy, March 2026

## The Three-File Architecture

| File | Role | Modified By |
|------|------|-------------|
| `prepare.py` | Fixed constants, data prep (downloads training data, trains BPE tokenizer), runtime utilities (dataloader, evaluation) | Human — read-only for agent |
| `train.py` | Full GPT model, optimizer (Muon + AdamW), training loop. Everything is fair game: architecture, hyperparameters, optimizer, batch size | Agent — the only file edited |
| `program.md` | Baseline instructions for one agent. Human iterates this to shape the "research org" | Human — the skill/context layer |

This is deliberate constraint architecture: one file to modify, one metric to optimize, one instruction document to govern behavior.

## The Agent Loop (from program.md)

The `program.md` is essentially a lightweight skill file. It encodes:

**Setup Phase:**
1. Agree on a run tag (e.g., `mar5`)
2. Create branch `autoresearch/<tag>` from master
3. Read README.md, prepare.py, train.py for full context
4. Verify data exists in `~/.cache/autoresearch/`
5. Initialize `results.tsv` with header row
6. Confirm and go

**Experimentation Phase:**
Each experiment runs on a single GPU for a **fixed 5-minute wall-clock time budget**. Training invoked as `uv run train.py`.

**Agent capabilities:**
- Modify `train.py` only: model architecture, optimizer, hyperparameters, training loop, batch size, model size
- Cannot: modify `prepare.py`, install new packages, modify evaluation harness

**Goal:** Get the lowest `val_bpb` (validation bits per byte). Since time budget is fixed, experiments are directly comparable regardless of what the agent changes.

**Constraints:**
- VRAM is a soft constraint (some increase acceptable, no blowups)
- Simplicity criterion: small improvement adding ugly complexity is not worth it. Removing something and getting equal or better results is a simplification win.
- First run is always baseline (run train.py as-is)

**The Loop (FOREVER):**
1. Inspect git state (current branch/commit)
2. Tune `train.py` with an experimental idea
3. `git commit`
4. Run: `uv run train.py > run.log 2>&1` (redirect everything, no tee)
5. Read results: `grep "^val_bpb:\|^peak_vram_mb:" run.log`
6. If grep empty, run crashed: `tail -n 50 run.log` for traceback, attempt fix. Give up if unfixable after a few tries.
7. Record in `results.tsv` (tab-separated, NOT comma-separated)
8. If `val_bpb` improved (lower), advance branch (keep commit)
9. If `val_bpb` equal or worse, `git reset` back to where you started

**Critical autonomy instruction:**
> "NEVER STOP: Once the experiment loop has begun, do NOT pause to ask the human if you should continue. Do NOT ask 'should I keep going?' or 'is this a good stopping point?'. The human might be asleep, or gone from a computer and expects you to continue working indefinitely until you are manually stopped. You are autonomous. If you run out of ideas, think harder — read papers referenced in the code, re-read the in-scope files for new angles, try combining previous near-misses, try more radical architectural changes. The loop runs until the human interrupts you, period."

**Timeout:** Each experiment ~5 minutes total. If exceeds 10 minutes, kill and treat as failure.

**Output Format (printed by train.py):**
```
---
val_bpb:          0.997900
training_seconds: 300.1
total_seconds:    325.9
peak_vram_mb:     45060.2
mfu_percent:      39.80
total_tokens_M:   499.6
num_steps:        953
num_params_M:     50.3
depth:            8
```

## Logging Format (results.tsv)

Tab-separated, 5 columns, header row:

```
commit	val_bpb	memory_gb	status	description
```

- `commit`: short hash (7 chars)
- `val_bpb`: validation bits per byte (lower is better)
- `memory_gb`: peak VRAM in GB, rounded to .1f
- `status`: `keep`, `discard`, or `crash`
- `description`: short text of what was tried

`results.tsv` is intentionally untracked by git.

## Model Architecture (from train.py)

Derived from nanochat, single-GPU, cherry-picked and simplified.

**GPTConfig defaults:**
- sequence_len: 2048
- vocab_size: 32768 (tokenizer trained to 8192; train.py notes `vocab_size` may differ from tokenizer output)
- n_layer: 12
- n_head: 6
- n_kv_head: 6 (full heads, no GQA in default)
- n_embd: 768
- window_pattern: "SSSL" (sliding window: S=half context, L=full context, last layer always L)

**Key architectural features:**
- **RMSNorm** (not LayerNorm): `F.rms_norm(x, (x.size(-1),))`
- **ReLU-squared activation** in MLP: `F.relu(x).square()` (not GeLU or SwiGLU)
- **RoPE (Rotary Position Embeddings)**: precomputed cos/sin, `rotary_seq_len = sequence_len * 10`
- **Value Embeddings (ResFormer)**: per-layer value embeddings on alternating layers, mixed with input-dependent gate per head. Gate channels: 32. Gate init: zeros (sigmoid(0)=0.5, scaled by 2 -> 1.0 = neutral)
- **Per-layer residual scalars**: `resid_lambdas` (init 1.0) and `x0_lambdas` (init 0.1) applied before each block
- **Softcap**: logits capped at 15 via `softcap * tanh(logits / softcap)`
- **Weight initialization**: normal(0,1) for embeddings, normal(0,0.001) for lm_head, uniform(-s,s) with s=3^0.5 * n_embd^-0.5 for matrices, zeros for output projections
- **Cast to bf16**: embeddings and value embeddings cast to bfloat16 after init

**Window pattern "SSSL":**
Layers cycle through S (short window = sequence_len // 2) and L (long window = sequence_len). Last layer always L. This is a banded/aliased attention pattern.

**Flash Attention 3:**
Uses `kernels` package with FA3. Hopper (cap 9,0) gets `varunneal/flash-attention-3`. Non-Hopper falls back to `kernels-community/flash-attn3`.

## Optimizer: MuonAdamW

Combined optimizer: Muon for 2D matrix parameters, AdamW for everything else.

**Parameter groups and learning rates (at 768 dim, scaled by 1/sqrt(dmodel/768)):**
- lm_head (unembedding): AdamW, lr=0.004
- wte (embedding): AdamW, lr=0.2
- value_embeds: AdamW, lr=0.2
- resid_lambdas: AdamW, lr=0.005 (scalar_lr * 0.01)
- x0_lambdas: AdamW, lr=0.5 (different betas: 0.96, 0.95)
- Matrix params (by shape): Muon, lr=0.02, momentum=0.95, ns_steps=5, beta2=0.95

**Muon specifics:**
- Nesterov momentum on stacked gradients
- "Polar Express" orthogonalization: 5th-order polynomial approximation of matrix orthogonalization, with precomputed coefficients
- NorMuon variance reduction: per-row/column second-moment tracking with scaling normalization
- Cautious weight decay: only applied where gradient and parameter have same sign
- LR scaled by max(1.0, shape[-2]/shape[-1])^0.5

**Schedules (based on progress = training_time / TIME_BUDGET):**
- LR multiplier: warmup (0% default) -> flat -> warmdown (last 50% of time, linear decay to 0)
- Muon momentum: ramps from 0.85 to 0.95 over first 300 steps
- Weight decay: decays linearly to 0 over the run

## Training Loop Details

- Gradient accumulation: `TOTAL_BATCH_SIZE / (DEVICE_BATCH_SIZE * MAX_SEQ_LEN)`
- Default TOTAL_BATCH_SIZE: 2^19 (~524K tokens)
- Default DEVICE_BATCH_SIZE: 128
- Default DEPTH: 8 (derives model_dim = depth * ASPECT_RATIO = 8 * 64 = 512, rounded up to multiple of HEAD_DIM=128 -> 512, num_heads=4)
- Model built on meta device, moved to empty, weights initialized
- `torch.compile(model, dynamic=False)` for optimization
- Prefetch first batch before loop
- Fast fail: abort if loss NaN or > 100
- Step 0: gc.collect(), gc.freeze(), gc.disable() to avoid ~500ms Python GC stalls
- GC re-enabled every 5000 steps for cleanup
- Compilation excluded from time budget: only steps > 10 count toward TIME_BUDGET

**MFU calculation:**
`100 * num_flops_per_token * TOTAL_BATCH_SIZE / dt / H100_BF16_PEAK_FLOPS`
where H100_BF16_PEAK_FLOPS = 989.5e12

## Data Pipeline (from prepare.py)

**Dataset:** `karpathy/climbmix-400b-shuffle` on HuggingFace
- 6,542 parquet shards
- Pinned validation shard: shard_06542
- Downloads via requests with retries (5 attempts, exponential backoff)
- Multi-process download (default 8 workers)

**Tokenizer:**
- BPE via rustbpe (Rust implementation)
- GPT-4 style split pattern with `\p{N}{1,2}` (not {1,3})
- Vocab size: 8192 + 4 special tokens = 8196
- Special tokens: `<|reserved_0|>` (BOS) through `<|reserved_3|>`
- Saved as tiktoken pickle encoding
- `token_bytes.pt`: per-token byte length lookup for BPB evaluation

**Dataloader:**
- BOS-aligned with best-fit packing
- Every row starts with BOS
- Documents packed using best-fit to minimize cropping
- When no document fits remaining space, crops shortest doc to fill exactly
- 100% utilization (no padding)
- Pre-allocated CPU pinned buffer + GPU buffer for async transfer

**Evaluation:**
- Fixed metric: `evaluate_bpb` (bits per byte)
- Vocab-size-independent: sums per-token cross-entropy (nats) divided by total target bytes
- Special tokens (byte length 0) excluded from both sums
- Evaluated on pinned validation shard
- Default EVAL_TOKENS: 40 * 524,288 = ~21M tokens

## Design Decisions

1. **Single file to modify.** Agent only touches `train.py`. Scope management and reviewable diffs.
2. **Fixed time budget.** Always 5 minutes. Makes experiments comparable regardless of model size/architecture changes. Finds optimal model for your platform in that budget. Downside: results not comparable across different compute platforms.
3. **Self-contained.** No external deps beyond PyTorch and small packages. No distributed training, no complex configs. One GPU, one file, one metric.

## Platform Support

Requires single NVIDIA GPU (tested on H100). Community forks exist:
- MacOS: miolini/autoresearch-macos, trevin-creator/autoresearch-mlx
- Windows: jsegov/autoresearch-win-rtx
- AMD: andyluo7/autoresearch

Karpathy recommends for smaller platforms (MacBooks): use TinyStories dataset (lower entropy), reduce vocab_size, lower MAX_SEQ_LEN, decrease DEPTH, use WINDOW_PATTERN "L" only, lower TOTAL_BATCH_SIZE.

## Analysis Notebook

`analysis.ipynb` provides pandas/matplotlib visualization of `results.tsv`:
- Experiment outcome counts (keep/discard/crash)
- Keep rate percentage
- val_bpb progression over time
- Memory vs val_bpb scatter
- Description word cloud (implied)

## Connection to Agent-Native Operations

Autoresearch is a concrete implementation of several concepts in Substrate:

**Incomplete Contract + Delegation:** `program.md` is the incomplete contract. It specifies the goal (lower val_bpb), constraints (single file, no new deps, fixed budget), and autonomy level (never stop, never ask). The agent fills in the execution details. This maps directly to [[mission-contracts]] and [[management-by-objectives]]: the principal specifies intent, the agent handles implementation.

**Skill as Governance:** `program.md` is described as a "super lightweight skill." It is not code. It is natural language instruction that governs agent behavior. This validates the [[skills-as-portable-knowledge]] concept: the skill file is the governance layer, the code is the execution layer.

**Branch as Experiment History:** Each run gets a dedicated branch (`autoresearch/<tag>`). The branch history encodes the experiment trajectory: advances on success, resets on failure. This is a version-controlled proof-of-work chain. It maps to [[proof-of-work]] and [[github-as-memory]]: the branch is the ledger of attempted improvements.

**Fixed Budget as Normalization:** The 5-minute wall-clock budget makes results comparable across architectural changes. This is a normalization strategy for evaluation in a search space where the variables are not controlled. It parallels evaluation design in [[evaluating-llms-harness]]: fixed conditions, comparable metrics.

**Human-AI Symbiosis:** The human edits `program.md` (the skill/strategy layer). The agent edits `train.py` (the execution/tactical layer). The human shapes the org; the agent executes within it. This is the same Teacher + AI TA structure as [[eureka-labs]], applied to research rather than education.

**Autonomous Loop with No Human in the Loop:** The "NEVER STOP" instruction removes the human from the loop entirely once started. This is [[auftragstaktik]] at the agent level: the agent receives intent and operates independently until mission complete or interrupted. The human is the commander who issues the Auftrag; the agent is the subordinate who executes with disciplined initiative.

## Related Sources

- [[karpathy-makemore-neural-networks-from-scratch]] — Karpathy's educational content, precursor to autoresearch's pedagogy
- [[nanochat]] — Parent repository with full multi-platform support, Flash Attention 3 fallback, broader device support
- [[LLM101n]] — Karpathy's undergraduate course: build ChatGPT from scratch (archived, on hold)
- [[eureka-labs]] — Karpathy's AI-native education venture (Teacher + AI TA model)
- [[goal-primitive]] — /goal as emerging coordination primitive across agent platforms
- [[kanban-doctrine]] — Auftragstaktik as agent operating system
- [[mission-contracts]] — Multi-agent orchestration via structured intent delegation

## Provenance

Cloned from GitHub 2026-05-21. Repository is actively maintained with community forks. Original README references tweets at https://x.com/karpathy/status/2029701092347630069 and https://x.com/karpathy/status/2031135152349524125 for additional context.
