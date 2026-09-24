# Dream-RSI: Replay Simulators for Meta-Exploration, and What "Dreaming" Buys Recursive Self-Improvement

Raw research file. Deep dive on "Dream-RSI: Recursive Self-Improvement through Evolving Worlds" (Zheng, Wu, Zhang et al., arXiv:2609.14858v1, 14 Sep 2026; Google, Google DeepMind, University of Maryland, University of Virginia; 17 authors, 36-page PDF including appendices). This file covers the paper's core mechanism (discovery history as replay simulator), its formalism, its empirical claims across three domains, and where the claims hold or break. Source material for later synthesis, not a finished essay.

Stance: report what the paper claims, tag FACT for claims verified against the extracted full text (PDF pulled from arXiv this session and read in full), INTERPRETATION for readings connecting the paper to adjacent Substrate nodes, BACKGROUND for established record not re-verified.

Related Substrate nodes: [[rsi-survey-autonomy-levels-deep-dive]] (the Theseus Labs autonomy-levels survey filed 2026-09-24; Dream-RSI maps cleanly onto its L2-to-L5 boundary questions), [[rsi-anthropic-openai-deep-dive]] (frontier-lab RSI positions), [[audit-replay]] (our own audit-replay node: agent traces as reconstructible state, the infrastructural cousin of Dream-RSI's replay trees), [[dreams-are-cognitive-maintenance-not-prophecy]] (hippocampal replay during sleep; the biological referent of the paper's "dreaming" metaphor), [[harness-engineering]] (Dream-RSI improves the exploration harness while leaving the underlying agent untouched), [[per-run-learning]] (experience files as persistent state), [[accelerando-compounding-acceleration]] (discovery loops feeding capability development), [[continual-learning-for-agents-replit]] (harness-as-learner).

---

## 1. The subject's claim

Framing claim (INTERPRETATION): The strongest version of the paper's thesis is that the binding constraint on recursive self-improvement at the exploration layer is not agent capability but feedback economics. Improving an exploration policy requires observing how it shapes a long discovery rollout, and each such observation costs a full online run. Dream-RSI's answer: a completed discovery run already recorded everything a policy could have done, so the recorded tree itself is a simulator. Evaluate candidate policies against the recording, not the world. This converts meta-level policy improvement from expensive online trial-and-error into cheap off-policy "dreaming," and each improved policy redeployed online expands the simulator pool, closing a recursive loop.

### 1.1 The bottleneck: meta-level feedback is delayed and expensive (FACT)

From the introduction: "unlike evaluating an individual candidate, assessing an exploration policy requires observing how it shapes the subsequent discovery process over many proposal-evaluation cycles." And: "a newly proposed policy may perform poorly, so many alternatives may need to be tried." Prior work treats past discovery history "merely as static textual context or training data for weight fine-tuning." The paper's claim is that the history is more than either: it is a structured tree of decisions and realized execution outcomes, and once organized, it is "a grounded model of the portion of the discovery space that has already been observed."

### 1.2 The core mechanism: replay over a recorded tree (FACT)

The formalism (section 3). A discovery tree is rooted at the initial workspace state r. Each node records the inherited context, the generation-evaluation attempt, the resulting filesystem snapshot, the generated artifact, evaluation diagnostics, and a score s_v under a fixed task-scoring protocol. The exploration policy observes the current tree and selects a batch of nodes (up to W parallel workers) from which to continue: eligible nodes are the root plus current leaves. That single interface is used both online and offline; the phases differ only in the transition after a batch is selected.

Online: the discovery agent actually generates new candidates from selected nodes; transitions are stochastic. Offline replay: the recorded children of selected nodes are returned deterministically. For a non-root leaf, replay returns its unique recorded child if one exists; for the root, replay returns the earliest-created unopened child, opening a previously recorded branch. No outcomes beyond the recorded tree are ever generated. Replay ends when the policy selects an empty batch, hits the round cap, or has revealed the whole recorded tree.

The replay score (equation 1) balances three terms: best solution quality revealed, a penalty on the number of generation-evaluation requests the trajectory represents (execution cost), and a bonus for average attempts per decision round (parallelism). A policy version's evaluation score is its average replay score across all historical trees.

Policy improvement: a fixed LLM-based policy-development agent inspects replay trajectories and scores, revises the executable policy code, and produces M versions per offline phase. Because the candidate set always includes the current policy, the selected next policy is guaranteed no worse than the current one in average replay score on the fixed history: V(m*) >= V(0). Only the exploration-policy code changes; the underlying models, evaluator, and execution interfaces stay fixed.

INTERPRETATION: That monotonicity guarantee is cheap. It holds only on the fixed history, and the history is exactly what the current policy generated. A policy that overfits the recorded tree's idiosyncrasies scores well in replay and poorly online. The paper does not discuss replay-to-online generalization gap as a risk; the closest it comes is the prefix-only constraint in the policy-development prompt (appendix B.2), which prevents policies from reading unrevealed scores.

### 1.3 The analogy stack (FACT)

Section 2 grounds the idea in model-based RL and the Dreamer lineage (Ha and Schmidhuber 2018; Hafner et al. 2019, 2020, 2023, 2025): an agent learns a compact dynamics model from collected experience and improves its policy by imagining trajectories within that model. Dream-RSI's twist: no learned model. The "world model" is the literal recorded tree, exact by construction within its support, and undefined outside it.

---

## 2. The current state, measurably

All experiments compare Dream-RSI against Recursive Fixed Exploration: identical discovery agent, evaluator, initialization, and per-round budgets, but with the exploration policy frozen across rounds. Both start from the same hand-designed parallel-refine policy, so round 1 is identical by construction. Agents: Gemini-3.1 Pro (10 parallel workspaces x 11 refinement steps = 110 calls/round) and Gemini-3.7-Flash (32 x 20 = 640 calls/round), driven via Gemini CLI.

### 2.1 Algorithm engineering: Lasso regularization path (FACT)

SimpleTES benchmark setting: 17 synthetic instances for discovery, six held-out downstream datasets (Gisette, RCV1, DNA, Leukemia, Colon, Duke Breast) for generalization. Five recursive rounds.

- Gemini-3.1 Pro: average held-out runtime 3587.1 ms (fixed) to 2931.0 ms (Dream-RSI), using 317 discovery-agent calls vs 550.
- Gemini-3.7-Flash: 2516.7 ms to 2350.6 ms, using 1879 calls vs 3200.
- Both discovered solvers beat sklearn and glmnet on all six held-out datasets.
- Versus SimpleTES (GPT-OSS-120B, 51,200 generations, average 3804.8 ms): Dream-RSI achieves lower average runtime with roughly two orders of magnitude fewer discovery-agent calls (317 vs 51,200 is ~162x; the paper says "up to 162x over SimpleTES").
- The discovered solver (appendix C, full C++/Eigen source included): strong-rule screening plus adaptive Cauchy-Schwarz KKT pruning, recomputing exact gradients only when the bound cannot certify a feature, with active-set bookkeeping, lazy Gram-matrix construction, and hardware-aware alignment. Distinct from SimpleTES's LARS/coordinate-descent dimension switch: adaptivity lives inside the active-set loop.

INTERPRETATION: the 162x comparison is real but asymmetric. SimpleTES ran a different agent (GPT-OSS-120B) under a different framework; the controlled claim is the ~1.7x call reduction and runtime improvement versus Recursive Fixed Exploration on the same Gemini backbones. The order-of-magnitude figure is a cross-system comparison and should be read as such.

### 2.2 Mathematical optimization: three open problems (FACT)

Ten rounds, Gemini-3.1 Pro, on Sum-Difference (maximize), Circle Packing n in {26, 32} (maximize sum of radii), and Autocorrelation Inequalities (minimize). Compared against AlphaEvolve, AlphaEvolveV2, OpenEvolve, CodeEvolve, ShinkaEvolve, TTS-Discovery, ThetaEvolve, EvoX, SimpleTES.

- Sum-Difference: Dream-RSI 1.145427, best of the compared methods (Recursive Fixed 1.144047, SimpleTES 1.143975, AlphaEvolveV2 1.121936).
- Circle Packing: 2.635983, matching the strongest reported result (SimpleTES, TTS-Discovery, ThetaEvolve all 2.635983).
- Autocorrelation: 1.456375, competitive but not SOTA; SimpleTES holds 1.453675 but spent 51,200 generations versus Dream-RSI's fewer than 1,000, a >50x budget difference.

### 2.3 GPU kernel engineering: KernelBench (FACT)

Four tasks (VGG16, LayerNorm, ConvDiv, ConvMax), Gemini-3.1 Pro, scored by inverse runtime subject to correctness checks.

- VGG16: comparable final performance with 2.43x fewer generations.
- LayerNorm: comparable performance with 1.79x fewer generations.
- ConvDiv: 2.09x higher performance under comparable budgets.
- ConvMax: 1.44x higher performance under comparable budgets.

### 2.4 Behavioral analysis (FACT)

ConvDiv round-by-round evolution (Figure 6): round-best performance climbs 0.427 to 1.898 (1/ms) across rounds E0-E8 while evaluated attempts per round move 110, 110, 87, 80, 50, 92, 80, 91, 86. The learned policy conserves compute while performance improves (110 down to 50), then re-expands exploration when progress plateaus, coinciding with further gains. This is the clearest evidence in the paper that the policy is genuinely adapting, not just riding a lucky initialization.

The guidance ablation (Figure 5, ConvDiv): injecting explicit semantic direction guidance into prompts consistently underperforms the unguided variant under equal budgets, for both Dream-RSI and fixed exploration. The paper's reading: in long-horizon multi-thread discovery, strong semantic priors over-constrain the search space and impede diverse exploration. INTERPRETATION: this is a notable negative result against the obvious alternative design (history as prompt guidance), and it strengthens the case that the value of history lives in its replay structure, not its summarization.

---

## 3. The discourse

The paper positions itself against three neighborhoods (section 6):

1. LLM discovery systems (AlphaEvolve, OpenEvolve, CodeEvolve, ShinkaEvolve, PACEvolve, DeltaEvolve, MLEvolve) iterate candidate solutions but keep exploration strategies fixed. SkyDiscover, SwarmResearch, and EvoX move toward optimizing exploration itself; Dream-RSI's distinction is doing so off-policy over replayed history rather than online.
2. Self-evolving agents (weights, harnesses, contexts, skills, rubrics, environments) mostly operate at the object level. Meta-level work (Meta^n, MetaSkill-Evolve, EvoX) exists but faces the delayed-feedback cost Dream-RSI targets.
3. Memory and experience reuse (DeltaEvolve's semantic deltas, ReasoningBank, skill libraries): the paper's break with this line is using history as a simulator for evaluating controllers, not as context for the next decision.

Mapping onto the Theseus autonomy taxonomy (INTERPRETATION, via [[rsi-survey-autonomy-levels-deep-dive]]): Dream-RSI is a clean L2-to-L5-boundary specimen. The system autonomously selects how to improve its own exploration strategy (L2 over the improvement of exploration). The edited artifact is the policy that governs subsequent discovery, i.e. a mechanism responsible for future improvement, which is the L5 definition: "the system persistently revises a mechanism that governs subsequent improvement." But the Theseus survey's structural-versus-effective L5 distinction bites here: the policy-development agent, the replay objective, the beta-sweep protocol, and the selection rule (argmax over replay scores, current policy always included) are all fixed by humans. What self-modifies is the exploration policy code; what does not self-modify is the procedure that modifies it. Structural L5 on a narrow mechanism, with the outer improvement loop human-frozen. The Theseus paper's verdict on such systems applies: "task gains alone do not establish a better improvement procedure."

Mapping onto [[audit-replay]] (INTERPRETATION): our audit-replay work treats agent traces as reconstructible state for accountability ("what did Sivart do last Tuesday at 3pm"). Dream-RSI treats the same artifact class as an optimization surface. Same substrate, two purposes: forensics and dreaming. The convergence suggests a shared primitive: any agent framework that records structured, replayable decision trees gets both accountability and cheap meta-optimization for free. Hermes session transcripts plus kanban event logs are closer to this than we have exploited.

Mapping onto [[dreams-are-cognitive-maintenance-not-prophecy]] (INTERPRETATION): the biological dream literature describes hippocampal replay of waking trajectories during sleep, where reactivation predicts subsequent memory gains. Dream-RSI is the engineering homolog: offline replay of recorded trajectories to improve future behavior without new world interaction. The naming is earned, not decorative.

---

## 4. Where the mapping breaks

1. Replay support is the silent constraint (FACT from the formalism, INTERPRETATION in consequence). Replay can only traverse what the recorded tree contains: each non-root node has at most its unique recorded child, and root replay opens branches in recorded creation order. A candidate policy cannot ask "what if I had refined this node twice" or "what if I had tried a direction nobody tried." The simulator is exact inside the realized search space and empty outside it. Policies that would have explored genuinely new directions are unevaluable in replay. The paper's self-improving loop partially addresses this (each online round adds new trees), but the bias compounds: history generated by a conservative policy conservatively constrains the evaluation of future policies. This is the off-policy evaluation problem with the support gap made structural.
2. Monotonicity is replay-local (FACT). The guarantee V(m*) >= V(0) holds on the fixed history only. Nothing bounds the online degradation of a replay-optimal policy. The paper reports no failure case where a dreamed-up policy performed worse online than its predecessor; either none occurred in these runs, or they are not discussed.
3. Stochasticity is collapsed in replay (FACT). Online transitions are stochastic ("the discovery agent may generate different outcomes from the same starting workspace"); replay returns recorded children deterministically. A policy that got lucky online and a policy that would reliably reproduce that outcome are indistinguishable in replay. Variance in the discovery process is invisible to the dreaming phase.
4. The evaluation is author-run, single-framework, two models, one vendor (FACT). All experiments use Gemini models via Gemini CLI, with the authors at Google and Google DeepMind. The controlled baseline (Recursive Fixed Exploration) is the right comparison and the reported deltas (1.7x-2.4x efficiency, 2.09x quality) are against it, but there is no independent replication, no cross-vendor backbone, and no failure-mode reporting.
5. Scale of recursion is modest (FACT). Five rounds (Lasso), ten rounds (math), unspecified rounds for kernels. The recursive loop is demonstrated over a handful of policy revisions, not the hundreds of generations that "recursive self-improvement" evokes. The paper's own title overpromises relative to its evidence depth, in the direction the Theseus survey warns about.
6. The beta mechanism is half-manual (FACT). The offline evaluation sweeps a fixed beta grid and the policy-development agent picks the next default beta from live manifests plus sweep evidence, per rules written into the prompt (raise on plateau if higher beta attains more, lower if high beta adds work without attainment, else default ~0.6). The adaptivity is real but the decision procedure is human-scripted prompt text, which sits awkwardly beside the claim of autonomous policy improvement.
7. "Up to 162x" is a cross-system headline (FACT + INTERPRETATION). The Lasso comparison against SimpleTES conflates agent, framework, and budget. The honest controlled number is ~1.7x fewer calls and ~656 ms faster on the same backbone. The 162x is true arithmetic on incomparable systems.

---

## 5. Compression points for synthesis

1. Dream-RSI's core move: completed discovery trees are replay simulators; candidate exploration policies are scored off-policy against recorded outcomes (quality minus cost plus parallelism bonus), turning meta-level improvement from online trial-and-error into cheap "dreaming."
2. Controlled results: on identical Gemini backbones, dreaming over history beats fixed exploration by ~1.7x fewer agent calls with better downstream runtime (Lasso), 1.79x-2.43x fewer generations (VGG16, LayerNorm), and 1.44x-2.09x higher quality (ConvDiv, ConvMax) under matched budgets.
3. The learned policy exhibits adaptive compute allocation: it contracts evaluated attempts (110 to 50) while performance climbs, re-expands on plateaus. Adaptive exploration effort is demonstrated, not just claimed.
4. Negative result worth keeping: explicit semantic guidance from history underperforms unguided search under equal budgets; history's value is in its replay structure, not its summarization into prompts.
5. Structural limits: replay evaluates only within the realized search space (recorded children only), collapses stochasticity to determinism, and its monotonicity guarantee is replay-local. Off-policy support gaps compound as conservative histories constrain future policy evaluation.
6. Taxonomy placement: Dream-RSI is structural L5 on the exploration-policy mechanism with a human-frozen outer loop (fixed policy-development agent, replay objective, selection rule). Per the Theseus survey's structural-vs-effective distinction, task gains alone do not establish a better improvement procedure.
7. The replay primitive converges with [[audit-replay]]: recorded decision trees serve both accountability and meta-optimization. Agent frameworks that log structured, replayable trees get both for free; Hermes transcripts and kanban logs are underexploited in this direction.
8. Evidence hygiene: all experiments are author-run on Google models with Google-affiliated authors, 5-10 recursive rounds, no independent replication, no reported policy-regression failures. Treat the 162x SimpleTES headline as cross-system marketing; the controlled claim is 1.7x-2.4x.

---

## Sources

Verified live this session:
- arXiv:2609.14858 abstract page (metadata, author list, submission history).
- Full PDF (36 pages incl. appendices) pulled from arxiv.org/pdf/2609.14858, text-extracted with pymupdf to /tmp/dream-rsi.txt; sections 1-7 and appendices A-C read directly. Appendix B contains the full exploration and policy-improvement prompts; appendix C contains the full discovered Lasso solver source.
- Project links referenced by paper: github.com/zhengkid/Dream-RSI and dream-rsi.com (not independently fetched).

Established record cited but not re-verified (verify before direct quotation):
- All third-party systems named by the paper (AlphaEvolve, SimpleTES, EvoX, ThetaEvolve, KernelBench, Dreamer family, etc.) are reported here as the paper characterizes them; their own publications were not re-read this session.
- The SimpleTES 51,200-generation budget and per-task scores are as tabulated by the paper.
