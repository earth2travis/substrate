# AutoResearchClaw: Deep Analysis for Experiment Driven Development

**Repository:** [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)
**Version analyzed:** v0.3.0 (2026-03-17)
**Filed:** 2026-03-17
**Purpose:** Evaluate architecture, scientific fidelity, and adaptation potential for Sivart/Synthweave

---

## 1. Overview and Architecture

AutoResearchClaw is a fully autonomous research pipeline that takes a topic string and produces a conference ready paper with real literature, sandbox experiments, statistical analysis, multi agent peer review, and LaTeX output targeting NeurIPS/ICML/ICLR.

**Core design philosophy:** Linear stage pipeline with feedback loops. 23 stages organized into 8 phases, executed sequentially with three human in the loop gate stages (5, 9, 20) that can be auto approved. The pipeline is a state machine: each stage has typed input/output contracts (`StageContract`), status transitions, and rollback rules.

**Key technical choices:**
- Python 3.11+, YAML config, JSONL for persistence
- LLM agnostic: OpenAI compatible API or ACP (Agent Client Protocol) for coding agents
- Real literature from OpenAlex, Semantic Scholar, arXiv (not hallucinated)
- Hardware aware: auto detects GPU/MPS/CPU and adapts code generation
- Sandbox execution with AST validation, NaN/Inf detection, self healing repair loops
- OpenClaw integration via bridge adapters (cron, message, memory, sessions, web fetch, browser)

**What it produces per run:**
- `paper_draft.md` and `paper.tex` (conference ready LaTeX)
- `references.bib` (real, verified BibTeX)
- `experiment runs/` with generated code and structured JSON metrics
- `charts/` with auto generated comparison charts
- `reviews.md` from multi agent peer review
- `evolution/` with self learning lessons
- `verification_report.json` with 4 layer citation integrity check
- `deliverables/` folder ready for Overleaf

---

## 2. The 23 Stage Pipeline

### Phase A: Research Scoping (Stages 1-2)

**Stage 1: TOPIC_INIT.** Takes the topic string, generates a SMART goal statement, and runs hardware detection (GPU type, VRAM, CPU). Outputs `goal.md` and `hardware_profile.json`. No LLM fallback needed for hardware detection; the goal is always LLM generated.

**Stage 2: PROBLEM_DECOMPOSE.** Decomposes the topic into 4+ prioritized sub questions with risks. The prompt asks for "Source, Sub-questions, Priority Ranking, Risks." This feeds the literature search strategy.

### Phase B: Literature Discovery (Stages 3-6)

**Stage 3: SEARCH_STRATEGY.** Generates search plan YAML with 3+ strategies and 8+ keyword queries. Covers core topic, related methods, benchmarks, theoretical foundations, applications. Also generates `queries.json` for API calls.

**Stage 4: LITERATURE_COLLECT.** The most technically interesting early stage. Tries real API search first (OpenAlex, Semantic Scholar, arXiv) with query expansion, deduplication, and circuit breaker with graceful degradation. Falls back to LLM generated candidates only if all APIs fail. Produces `candidates.jsonl` with real paper metadata including DOIs and arXiv IDs.

**Stage 5: LITERATURE_SCREEN. [GATE]** Dual relevance + quality screening. Domain aware rejection of off topic papers. On rejection, rolls back to Stage 4 (re collect). This is the first human checkpoint.

**Stage 6: KNOWLEDGE_EXTRACT.** Extracts structured knowledge cards per shortlisted paper: problem, method, data, metrics, findings, limitations, citation. JSON output preserves cite keys for downstream reference.

### Phase C: Knowledge Synthesis (Stages 7-8)

**Stage 7: SYNTHESIS.** Clusters findings, identifies 2+ research gaps. Outputs topic clusters and prioritized opportunities.

**Stage 8: HYPOTHESIS_GEN.** Uses multi agent debate (multiple LLM perspectives with different system prompts) to generate 2+ "falsifiable" hypotheses. Each hypothesis includes rationale, measurable prediction, and failure condition. Also runs a novelty check against Semantic Scholar to see if the hypotheses overlap existing work.

### Phase D: Experiment Design (Stages 9-11)

**Stage 9: EXPERIMENT_DESIGN. [GATE]** Designs experiment plan as YAML: objectives, datasets, baselines, proposed methods, ablations, metrics, risks, compute budget. On rejection, rolls back to Stage 8 (re hypothesize). Injects domain specific guidance (RL step guidance, framework docs, dataset guidance).

**Stage 10: CODE_GENERATION.** Generates multi file Python experiment project. Uses either a single shot LLM call or the advanced CodeAgent (multi agent code generation with planning, implementation, validation, repair cycles). AST validated. Forbidden patterns: subprocess, os.system, eval, exec. Auto installs missing sandbox safe packages (numpy, torch, sklearn, etc.).

**Stage 11: RESOURCE_PLANNING.** Creates GPU/time schedule JSON for experiment execution.

### Phase E: Experiment Execution (Stages 12-13)

**Stage 12: EXPERIMENT_RUN.** Runs experiments in sandbox (subprocess with timeout, memory limits). Parses structured metrics from stdout (`name: value` format). Detects NaN/Inf divergence. Captures per condition metrics with optional regime tags. Extracts paired statistical comparisons.

**Stage 13: ITERATIVE_REFINE.** The edit run eval keep/discard loop. Up to 10 iterations. Self healing: when code fails, sends error + full project context to LLM for targeted repair. Detects metric saturation and injects difficulty upgrade hints. Tracks condition coverage gaps and forces multi condition labeling. Convergence detection with early stopping.

### Phase F: Analysis and Decision (Stages 14-15)

**Stage 14: RESULT_ANALYSIS.** Multi agent debate again (multiple analyst perspectives). Merges Stage 13 refinement results. Generates comparison charts via FigureAgent (multi agent: planner, codegen, renderer, critic, integrator) or legacy matplotlib. Outputs `analysis.md` with statistical interpretation.

**Stage 15: RESEARCH_DECISION.** The critical decision point. Parses PROCEED/PIVOT/REFINE from LLM output. PIVOT rolls back to Stage 8 (new hypotheses). REFINE rolls back to Stage 13 (re run experiments). Maximum 2 pivots to prevent infinite loops. Detects degenerate refine cycles (saturated or identical metrics) and forces PROCEED with quality warning. Decision rationale is extracted and stored in `decision_structured.json`.

### Phase G: Paper Writing (Stages 16-19)

**Stage 16: PAPER_OUTLINE.** Detailed outline with per section goals and evidence links.

**Stage 17: PAPER_DRAFT.** Full paper: 5,000-6,500 words targeting 9 page conference format. Section by section with minimum word counts. Anti fabrication: must use real experimental data, never approximate numbers. Injects conference writing principles (novelty, narrative, strong baselines, ablations, honesty).

**Stage 18: PEER_REVIEW.** Simulated review from 2+ perspectives. Checks methodology evidence consistency (does the paper claim things the code doesn't support?). Detects trial count fabrication. Checks paper length. Scores 1-10 on NeurIPS rubric. This is the most sophisticated quality check.

**Stage 19: PAPER_REVISION.** Addresses all review comments. Length guard: must maintain or increase paper length.

### Phase H: Finalization (Stages 20-23)

**Stage 20: QUALITY_GATE. [GATE]** Final quality evaluation. JSON output with score, verdict, strengths, weaknesses, required actions. On rejection, rolls back to Stage 16 (rewrite paper).

**Stage 21: KNOWLEDGE_ARCHIVE.** Retrospective + reproducibility bundle. This is a noncritical stage: failure doesn't abort the pipeline.

**Stage 22: EXPORT_PUBLISH.** Markdown to LaTeX conversion with conference template (NeurIPS 2025, ICLR 2026, ICML 2026). Math, tables, figures, cross refs, `\cite{}`.

**Stage 23: CITATION_VERIFY.** 4 layer verification: arXiv ID check, CrossRef/DataCite DOI, Semantic Scholar title match, LLM relevance scoring. Hallucinated references auto removed. This stage is critical: it blocks export if citations fail verification.

---

## 3. Experiment Framework

### Sandbox Architecture

The experiment sandbox (`researchclaw/experiment/sandbox.py`) runs generated Python code as a subprocess with:
- Configurable timeout (`time_budget_sec`, default 300s)
- Memory limits (`max_memory_mb`, default 4096)
- Allowed import whitelist (math, random, json, csv, numpy, torch, sklearn)
- AST validation before execution (no forbidden calls)
- Structured metric parsing from stdout
- NaN/Inf fast fail detection
- Per condition metric extraction with regex patterns

Three execution modes: `sandbox` (local subprocess), `docker` (containerized with network policy), `ssh_remote` (GPU server).

Docker mode adds: network policy (none/setup_only/pip_only/full), GPU passthrough, auto dependency installation.

### Self Healing

When experiments fail, the pipeline:
1. Captures the error (stderr, return code, validation issues)
2. Sends error context + full project files to LLM via `code_repair` or `iterative_repair` sub prompts
3. The repair prompt instructs: "trace the ROOT CAUSE from warnings and error messages. Do not just add try/except to suppress the error."
4. Re runs the repaired code
5. Up to 10 iterations with metric improvement tracking

### Metrics and Statistical Methods

Metrics are parsed from stdout using regex patterns:
- Plain: `metric_name: float_value`
- Condition prefixed: `condition=name metric: value`
- Ratio format: `condition=name metric: N/M`
- Paired comparisons: `PAIRED: method vs baseline mean_diff=X std_diff=Y t_stat=Z p_value=W`

The sandbox skips NaN/Inf values and logs warnings. The result analysis stage generates comparison charts with error bars and confidence intervals. Statistical rigor is encouraged in prompts but not enforced programmatically: the LLM decides what statistical tests to mention.

### The PIVOT/REFINE Loop

Stage 15 produces one of three decisions:
- **PROCEED:** Continue to paper writing (Stages 16+)
- **REFINE:** Roll back to Stage 13 (iterative refinement). Keep hypotheses, re run/improve experiments.
- **PIVOT:** Roll back to Stage 8 (hypothesis generation). Discard hypotheses, start fresh.

Maximum 2 pivot/refine cycles (`MAX_DECISION_PIVOTS = 2`). After that, forces PROCEED regardless. Existing stage directories are versioned before overwriting (`stage-13_v1`, `stage-13_v2`).

Degenerate cycle detection: if all metrics are identical or saturated across refine cycles, the system injects a "PROCEED with quality caveat" hint. Also detects consecutive empty metrics and forces PROCEED.

---

## 4. Multi Agent Debate Pattern

Debate occurs at three pipeline points:

1. **Hypothesis Generation (Stage 8):** Uses `DEBATE_ROLES_HYPOTHESIS` (defined in prompts module). Multiple LLM calls with different system prompts (different "perspectives"). Outputs saved to `perspectives/role_name.md`. Then a synthesis call merges all perspectives into unified hypotheses.

2. **Result Analysis (Stage 14):** Uses `DEBATE_ROLES_ANALYSIS`. Same pattern: multiple perspectives on the experimental results, then synthesis.

3. **Peer Review (Stage 18):** Simulates 2+ reviewer perspectives (Reviewer A, Reviewer B) with methodology evidence consistency checks.

**How debate works mechanically:**
```
_multi_perspective_generate(llm, roles, variables, perspectives_dir)
  → For each role: LLM call with role-specific system prompt
  → Save each perspective to file
  → Return dict of {role_name: response_text}

_synthesize_perspectives(llm, perspectives, sub_prompt_name, prompts)
  → Combine all perspectives into one prompt
  → LLM call to synthesize into unified output
```

**Limitations:** This is parallel generation then synthesis, not iterative debate. The "perspectives" don't respond to each other. There's no back and forth argumentation, no adversarial challenge, no convergence mechanism beyond the synthesis prompt. Each perspective is generated independently and combined by a single arbiter call. This is closer to ensemble averaging than genuine debate.

---

## 5. Self Learning and Knowledge Base

### Evolution System

`researchclaw/evolution.py` implements a JSONL backed lesson store with:

**Lesson extraction:** After each run, `extract_lessons()` scans stage results for:
- Failed stages → error lesson (classified by keywords into 6 categories)
- Blocked stages → pipeline lesson
- PIVOT/REFINE decisions → pipeline lesson with rationale
- Runtime warnings from experiment stderr → experiment lesson
- Metric anomalies (NaN, identical convergence) → analysis lesson

**6 lesson categories:** system, experiment, writing, analysis, literature, pipeline

**Time decay:** 30 day half life, exponential decay (`weight = exp(-age * ln(2) / 30)`). Lessons older than 90 days are dropped entirely (`MAX_AGE_DAYS = 90`).

**Prompt injection:** `build_overlay()` generates a per stage text block with the top N relevant lessons, injected at the end of the user prompt. Lessons are filtered by stage name and sorted by time weighted relevance.

### MetaClaw Integration (v0.3.0)

Cross run learning via the MetaClaw bridge:
- Pipeline failures/warnings → `LessonEntry` objects
- `convert_lessons_to_skills()` sends lessons to LLM → generates structured skill files
- Skills stored as `arc-*/SKILL.md` in `~/.metaclaw/skills/`
- `build_overlay()` reads both intra run lessons (JSONL) and cross run skills (arc-* directories)
- Skills have name, description, category, markdown content with numbered steps and anti patterns
- Controlled by severity threshold (`min_severity: warning`) and max skills per run (default 5)

**Reported improvements:** 18.3% robustness gain, 24.8% retry reduction, 40% refine cycle reduction in controlled A/B tests.

### Knowledge Base

`researchclaw/knowledge/base.py` implements a 6 category KB:
- **questions** (stages 1, 2, 8): Research questions and hypotheses
- **literature** (stages 4, 5, 6): Papers, screening results, knowledge cards
- **experiments** (stages 10, 12, 13): Code, run results, refinement logs
- **findings** (stages 7, 14): Synthesis, analysis results
- **decisions** (stages 3, 9, 11, 15, 20, 21): Strategy, design, resource, research decisions
- **reviews** (stages 16, 17, 18, 19, 22): Paper outlines, drafts, reviews, revisions

Two backends: plain Markdown (default) or Obsidian (adds wikilinks, tags, frontmatter). Each entry gets YAML frontmatter with id, title, stage, run_id, timestamp, tags, evidence refs.

KB entries are written after each successful stage. Content is truncated to 5000 chars for KB storage (full artifacts remain in stage directories).

---

## 6. Sentinel Watchdog

The sentinel is a bash script (`sentinel.sh`) that monitors the pipeline process:

- Checks heartbeat file (`heartbeat.json`) every 60 seconds (configurable)
- Pipeline writes heartbeat after each stage with PID, stage info, timestamp
- If heartbeat is stale (>5 min) AND PID is dead → restart pipeline from checkpoint
- Checks for active child processes before restart (avoids killing running experiments)
- Maximum 5 restart attempts
- Cooldown after 3 consecutive failures (6 min default)
- Logs to `sentinel_recovery.log`

**The in pipeline quality monitoring** is separate from sentinel:
- Template content detection (`quality.py`): regex patterns for placeholders, TODO markers, lorem ipsum, future tense promises. Computes template ratio (0.0 to 1.0).
- Citation verification (Stage 23): 4 layer check (arXiv, CrossRef, DataCite, LLM relevance)
- Peer review methodology evidence consistency check (Stage 18)
- Anti fabrication guard in paper draft prompts

**What sentinel is NOT:** It is not the NaN/Inf detection, citation verification, or anti fabrication system. Those are built into the pipeline stages themselves. Sentinel is purely a process watchdog for crash recovery.

---

## 7. Fidelity to the Scientific Method

This is the critical evaluation. The scientific method, from Bacon's inductive empiricism through Popper's falsificationism to modern experimental design, has a specific structure. The question is whether AutoResearchClaw follows it or merely performs its rituals.

### The Formal Steps

The scientific method, distilled across Bacon, Galileo, Newton, and Popper:

1. **Observation:** Notice a phenomenon or problem in the world
2. **Question:** Formulate a specific question about the phenomenon
3. **Background research:** Survey existing knowledge
4. **Hypothesis:** Propose a testable, falsifiable explanation
5. **Prediction:** Derive specific, measurable predictions from the hypothesis
6. **Experiment:** Design a controlled test that could falsify the prediction
7. **Analysis:** Evaluate results against predictions
8. **Conclusion:** Accept, reject, or modify the hypothesis based on evidence
9. **Communication:** Share findings for peer scrutiny and replication

AutoResearchClaw maps to this sequence. But mapping to the sequence is not the same as following the method.

### Where It Gets the Form Right

**Literature review is real.** Stages 3-6 query actual academic APIs (OpenAlex, Semantic Scholar, arXiv), screen papers by relevance, and extract structured knowledge. This is genuine background research, not hallucinated citation lists. The 4 layer citation verification at Stage 23 actively kills fabricated references. This is a meaningful integrity mechanism.

**The pipeline structure follows the sequence.** Observation/question (Stages 1-2), background research (Stages 3-6), hypothesis (Stage 8), experiment design (Stage 9), experiment execution (Stages 12-13), analysis (Stage 14), conclusion/decision (Stage 15), communication (Stages 16-22). The ordering is correct.

**There are gate stages.** Stages 5, 9, and 20 pause for human approval, creating checkpoints where a human can reject the direction. This is analogous to committee review in real research programs.

### Where It Fails the Substance

#### The Hypothesis Problem

The prompt for Stage 8 says: "Generate at least 2 falsifiable hypotheses from synthesis. For each hypothesis provide rationale, measurable prediction, failure condition."

This sounds right. But examine what actually happens. The LLM generates hypotheses from a synthesis of literature. These are not born from observation of unexplained phenomena. They are generated by a language model pattern matching on existing papers to produce plausible sounding claims. A hypothesis in the Popperian sense is a bold conjecture that risks being wrong. An LLM trained on academic papers will generate conservative, well hedged claims that are likely to "succeed" in the sandbox because they are already well established in the training data.

The "failure condition" in the prompt is structural: the LLM will write one because it was asked to. But the pipeline has no mechanism to evaluate whether the stated failure condition is genuine, whether it is actually testable within the sandbox constraints, or whether the experiment is designed to make failure possible.

**Verdict:** The hypotheses are formally correct but epistemically empty. They look like hypotheses. They have the right fields. But they are not conjectures risking falsification. They are predictions that the LLM is confident will be confirmed.

#### Hypothesis vs. Assumption: A Missing Distinction

The pipeline never distinguishes between hypotheses and assumptions. In real science, this distinction is foundational:

- **Hypothesis:** The claim being tested. "Method X outperforms baseline Y on task Z."
- **Assumptions:** The conditions taken for granted. "The synthetic data distribution is representative." "The loss function correctly measures what we care about." "The optimizer converges to a meaningful solution within the time budget."

AutoResearchClaw's experiment design (Stage 9) generates an experiment plan with objectives, baselines, methods, and metrics. But the assumptions underlying the experiment are never enumerated, never tested, never validated. The sandbox runs on synthetic data with synthetic benchmarks. The assumption that these synthetics are meaningful proxies for the research question is never examined.

In philosophy of science, this is the problem of auxiliary hypotheses (Duhem-Quine thesis): when an experiment "fails," you cannot tell whether the core hypothesis is wrong or an auxiliary assumption is wrong. AutoResearchClaw's PIVOT/REFINE decision at Stage 15 faces exactly this problem and has no mechanism to resolve it. The LLM just decides based on vibes.

#### The Control Problem

Real experiments require controls. A control group establishes what happens without the intervention, so the effect of the intervention can be isolated. AutoResearchClaw's experiment design prompt asks for "baselines" and "ablations," which is the right vocabulary. But:

1. **Baselines are LLM generated.** The LLM picks what to compare against. There is no mechanism to verify that the baselines are appropriate, competitive, or correctly implemented. The prompt says "invest real effort in making baselines competitive" and "reviewers catch weak baselines," but these are instructions to the paper writing stage, not to the experiment design stage.

2. **There are no true controls.** A control in the strict sense (identical conditions minus the variable of interest) is not enforced. The pipeline generates code for multiple "conditions" but does not verify that conditions differ by exactly one variable. Ablations are requested but not validated.

3. **Confounds are not addressed.** The sandbox has no mechanism to identify or control for confounding variables. Randomization is handled by seeds, but the experimental design itself (what factors to vary, how to isolate effects) is entirely delegated to the LLM.

#### PIVOT/REFINE: Optimization, Not Falsification

This is the deepest problem. The PIVOT/REFINE loop at Stage 15 looks like the hypothesis testing cycle (test, reject or refine, re test). But examine what it actually does:

- **REFINE** rolls back to Stage 13 (iterative refinement) to improve experiment code and re run. The goal: get better metrics. This is optimization, not falsification. The hypothesis is not being tested against the possibility of being wrong. The experiment is being tuned to make the hypothesis look right.

- **PIVOT** rolls back to Stage 8 (hypothesis generation) to generate new hypotheses. But "pivot" here means "the LLM couldn't get good numbers, try a different angle." This is not "the evidence contradicts our hypothesis, we must revise our understanding." It is "this approach didn't produce a publishable result, try something else."

- **PROCEED** means "the numbers look good enough to write a paper." Not "the evidence supports the hypothesis and we have failed to falsify it."

The decision prompt says: "Make a PROCEED or PIVOT decision from analysis." The system prompt says: "You are a research program lead making go/no-go decisions." This is project management language, not scientific language. A real falsification cycle asks: "Does the evidence contradict or support the hypothesis? What alternative explanations remain?" The pipeline asks: "Are the results good enough to proceed to paper writing?"

The maximum of 2 pivots (`MAX_DECISION_PIVOTS = 2`) makes this explicit. After two failed attempts, the system forces PROCEED regardless, writes a quality warning, and generates the paper anyway. Real science does not have a retry limit on falsification. If the evidence is insufficient, you do not publish. AutoResearchClaw always publishes.

#### The Metric Optimization Trap

The `ExperimentRunner.run_loop()` follows an edit, run, eval, keep/discard cycle. Each iteration is judged by whether the primary metric improves. This is gradient descent on a loss function, not hypothesis testing. The loop asks: "Did the number go in the right direction?" It does not ask: "Does this number mean what we think it means?"

The saturation detection (Stage 13) is revealing. When all methods achieve near perfect scores, the pipeline injects hints to make the benchmark harder. This is the opposite of the scientific method: instead of concluding that the benchmark is too easy and the results are uninformative, the system adjusts the benchmark to make the results look more interesting. The tail is wagging the dog.

#### The Peer Review Illusion

Stage 18's peer review is genuinely useful as a quality check: it catches methodology evidence inconsistencies, fabricated trial counts, and sections that are too short. But it is not peer review in the scientific sense. Real peer review involves independent experts who bring domain knowledge, skepticism, and awareness of the field that the authors may lack. LLM generated reviewers share the same training distribution as the LLM that wrote the paper. They are unlikely to catch novel errors or challenge assumptions that are baked into the training data.

The methodology evidence consistency check is the best part of this stage: it compares paper claims against actual experiment code and results. This is an auditor function, not a scientific review function, but it is genuinely valuable.

### The Fundamental Issue

AutoResearchClaw automates the **production** of research papers. It does not automate the **doing** of science. These are different activities.

Science is the process of learning about the world by proposing explanations and subjecting them to the risk of being wrong. Paper writing is the process of communicating what was learned. AutoResearchClaw conflates these: the pipeline optimizes for paper quality (length, formatting, citation integrity, reviewer scores) rather than for scientific validity (are the claims true? has the hypothesis been genuinely tested? what did we actually learn?).

The pipeline has no mechanism for:
- **Surprise.** Real science produces unexpected results that force conceptual revision. The pipeline produces expected results because the LLM generates hypotheses it knows how to confirm.
- **Negative results.** If the hypothesis is wrong, the pipeline pivots to a different hypothesis. It never concludes "the hypothesis was wrong and that is the finding." Negative results are failures, not discoveries.
- **Replication.** There is no mechanism to independently replicate findings. The same LLM generates the hypothesis, designs the experiment, writes the code, runs it, analyzes it, and writes the paper. There is no independent verification of the core claims.
- **Questioning the question.** The pipeline never asks whether the research question is well posed, whether the formalization captures the intended phenomenon, or whether the metrics measure what they claim to measure.

### Popper Would Object

Karl Popper's demarcation criterion: a theory is scientific if and only if it is falsifiable, and a genuine test is a sincere attempt to falsify it. AutoResearchClaw generates "falsifiable hypotheses" but never sincerely attempts to falsify them. The experiments are designed to confirm. The REFINE loop optimizes for better numbers. The PIVOT loop abandons hypotheses that don't produce papers, not hypotheses that are scientifically wrong.

Bacon would have a different objection. Baconian induction requires systematic observation of nature, not synthetic benchmarks. The entire experiment framework operates on generated data and simulated environments. There is no "nature" being observed. The pipeline is a closed system: the LLM generates the question, the answer, and the evidence for the answer.

### What It Actually Is

AutoResearchClaw is an **automated academic paper mill** with unusually good quality controls. It is excellent at what it does: producing well structured, properly cited, internally consistent papers that follow conference formatting requirements. The anti fabrication guards, citation verification, and methodology evidence consistency checks are genuinely innovative quality mechanisms.

But it is not doing science. It is doing science cosplay: wearing the costume (hypothesis, experiment, analysis, peer review) without the substance (genuine risk of being wrong, learning from failure, conceptual revision).

### What Would Make It Scientific

To move from cosplay to science, the pipeline would need:

1. **Genuine falsification tests.** Stage 15 should ask: "What evidence would convince us the hypothesis is wrong? Did the experiment produce that evidence?" If the answer is "yes, the hypothesis is wrong," the output should be "here is what we learned from a negative result," not "pivot to a new hypothesis."

2. **Assumption auditing.** A dedicated stage that enumerates assumptions, tests auxiliary hypotheses, and reports which assumptions were validated and which remain untested.

3. **Control verification.** Programmatic checking (not just prompting) that experimental conditions differ by exactly one variable, that controls are included, and that confounds are identified.

4. **Negative result publication.** The pipeline should be able to produce a paper that says "we tested X and it didn't work, here is why, and here is what that tells us." Currently, negative results trigger PIVOT, not publication.

5. **External grounding.** Connection to real data sources, real benchmarks with known properties, or real world observations. The closed loop of LLM generates everything must be broken.

6. **Epistemic honesty signals.** A section in every output that says: "Here is what we are confident about, here is what we are uncertain about, here is what we assumed but did not test."

---

## 8. OpenClaw Integration Pattern

The `RESEARCHCLAW_AGENTS.md` file does not exist in the repo root (returns empty). The integration is via `.claude/skills/researchclaw/SKILL.md`, which provides:

- Trigger conditions (when to activate the skill)
- Prerequisites check (config file, API key)
- Three running modes: CLI, Python API, iterative pipeline
- Clear command syntax with all flags documented

The OpenClaw bridge (`openclaw_bridge` config section) defines 6 optional capabilities:
- `use_cron`: Scheduled research runs
- `use_message`: Progress notifications to Discord/Slack/Telegram
- `use_memory`: Cross session knowledge persistence
- `use_sessions_spawn`: Parallel sub sessions for concurrent stages
- `use_web_fetch`: Live web search during literature review
- `use_browser`: Browser based paper collection

Each flag activates a typed adapter protocol in `researchclaw/adapters.py`. When OpenClaw provides capabilities, the adapters consume them without code changes. When capabilities are absent, the adapters are no ops.

**Pattern assessment:** This is a clean capability negotiation pattern. The tool declares what it can use; the host declares what it provides. No hard dependencies. Good model for other tools to follow. The skill file pattern (`.claude/skills/`) is specifically for Claude Code; `RESEARCHCLAW_AGENTS.md` would be the generic version for any AI assistant.

---

## 9. Adaptation for Sivart: Experiment Protocol Proposal

The most valuable thing in AutoResearchClaw is not the paper pipeline. It is the underlying experiment execution loop: design, code generate, sandbox execute, analyze, decide (proceed/refine/pivot). This pattern generalizes beyond academic papers.

### The Sivart Experiment Protocol

Inspired by AutoResearchClaw's architecture but redesigned for scientific honesty:

```
┌─────────────────────────────────────────────────────┐
│                  EXPERIMENT PROTOCOL                 │
│                                                      │
│  1. QUESTION         What are we trying to learn?    │
│  2. ASSUMPTIONS      What are we taking for granted? │
│  3. HYPOTHESIS       What do we predict will happen? │
│  4. FALSIFICATION    What evidence would prove us     │
│                      wrong?                          │
│  5. DESIGN           Controlled test with baselines  │
│  6. EXECUTE          Sandbox with metrics capture    │
│  7. ANALYZE          Statistical evaluation          │
│  8. VERDICT          Confirmed / Refuted / Unclear   │
│  9. LEARNING         What did we learn regardless    │
│                      of outcome?                     │
│ 10. ARCHIVE          Persist to institutional memory │
└─────────────────────────────────────────────────────┘
```

**Key differences from AutoResearchClaw:**

1. **Assumptions are first class.** Step 2 enumerates what we are assuming. Each assumption gets a confidence level. Assumptions can be promoted to hypotheses and tested separately.

2. **Falsification criteria are defined before the experiment.** Step 4 specifies what failure looks like before any code runs. This prevents post hoc rationalization.

3. **The verdict has three states, not two.** "Confirmed" means the evidence supports the hypothesis and we failed to falsify it. "Refuted" means we found the falsification evidence. "Unclear" means the experiment was inconclusive, likely due to an untested assumption. "Unclear" is a valid and informative outcome.

4. **Learning is mandatory and outcome independent.** Step 9 asks "what did we learn?" regardless of whether the hypothesis was confirmed or refuted. Negative results produce learning. This is the step AutoResearchClaw is missing entirely.

5. **No "pivot to avoid failure."** If the hypothesis is refuted, the protocol does not automatically generate a new hypothesis. It records the refutation as a finding. New hypotheses come from reflecting on what the refutation means.

### Concrete Implementation

For Sivart, this protocol would be implemented as:

**Experiment spec files** (`experiments/YYYYMMDD-description.yaml`):
```yaml
question: "Does X improve Y under conditions Z?"
assumptions:
  - claim: "Synthetic benchmark B is a valid proxy for real performance"
    confidence: medium
    testable: true
  - claim: "The metric M correctly captures the quality we care about"
    confidence: high
    testable: false
hypothesis: "Method X will outperform baseline B by >10% on metric M"
falsification: "If X performs within 5% of B, the hypothesis is refuted"
design:
  conditions: [X, B]
  controlled_variables: [data, seed, hardware, hyperparameters]
  metrics: [M, M2, runtime]
  seeds: 5
  timeout_sec: 300
```

**Experiment results** (`experiments/YYYYMMDD-description-results.yaml`):
```yaml
verdict: refuted | confirmed | unclear
evidence:
  metric_M: {X: 0.72, B: 0.70, diff: 0.02, p_value: 0.34}
learning: |
  X does not meaningfully improve over B on this benchmark.
  The 2% difference is within noise. This suggests the
  bottleneck is not where we thought it was.
assumptions_tested:
  - "Benchmark B validity": untested (separate experiment needed)
next_questions:
  - "Is the bottleneck in data quality rather than method?"
  - "Does X show improvement on harder benchmarks?"
```

### What We Borrow from AutoResearchClaw

- **Sandbox execution:** The sandbox pattern (subprocess, timeout, metric parsing, NaN detection) is directly reusable
- **Self healing:** The code repair loop (error → LLM fix → re run) is valuable for agent development experiments
- **Stage contracts:** Typed input/output contracts per stage are good engineering
- **Evolution store:** JSONL lesson extraction with time decay is a solid learning mechanism
- **Checkpoint/resume:** Pipeline checkpoint after each stage enables resumption
- **Sentinel watchdog:** Process monitoring for long running experiments

### What We Reject

- **The paper mill.** We are not generating academic papers. We are generating knowledge.
- **Optimization as science.** The REFINE loop's "make the numbers better" framing. Our verdict is allowed to be "refuted."
- **Forced PROCEED.** The 2 pivot maximum that forces publication regardless. If the evidence is insufficient, the experiment is inconclusive. That is the finding.
- **Synthetic self confirmation.** The closed loop where the LLM generates everything. Our experiments should test real agent behaviors against real metrics.

---

## 10. Agent Factory Implications

### Experiment Driven Agent Development

The Agent Factory builds agents. Currently, agent quality is assessed informally: does it feel right? Does it pass vibe checks? The experiment protocol above can systematize this:

**Agent configuration experiments:**
```yaml
question: "Does adding a 'no-man' challenger agent improve decision quality?"
hypothesis: "Decisions reviewed by a challenger agent will have 20% fewer errors"
falsification: "If error rate is within 5% with and without challenger, refuted"
design:
  conditions:
    - control: "Agent without challenger"
    - treatment: "Agent with challenger"
  test_cases: 50 standardized decision scenarios
  metrics: [error_rate, decision_time, false_positive_rate]
```

This makes agent development scientific. Instead of "let's try adding a challenger agent and see if it feels better," we define what success looks like, what failure looks like, and measure.

### The No Man Connection

AutoResearchClaw's peer review (Stage 18) and sentinel watchdog are partial implementations of the "no-man" concept from the institutional AI analysis. The peer review checks methodology evidence consistency. The sentinel watches for process crashes.

For Agent Factory, the no man agent would be:
- A dedicated challenger that reviews every agent decision before it executes
- Checks for: logical consistency, evidence support, assumption validity, risk assessment
- Has explicit authority to block actions (not just suggest improvements)
- Maintains a record of challenges, overrides, and outcomes
- This is the sentinel concept elevated from process monitoring to epistemic auditing

### Multi Agent Debate as Governance

AutoResearchClaw's debate pattern (parallel perspectives then synthesis) is too weak. For Agent Factory governance:

**Adversarial debate:** Perspectives respond to each other, not just to the original prompt. The challenger specifically attacks the strongest claim. Multiple rounds until convergence or deadlock.

**Structured dissent:** The no man agent's job is not to agree. It is to find the best argument against the proposed action. If it cannot find one, that is strong evidence the action is correct. If it can, the action needs revision.

**Decision logs with dissent records:** Every decision records what the no man argued and whether it was overridden. This creates institutional accountability.

---

## 11. Loom Spec Connections

### PIVOT/REFINE as an Orchestration Primitive

The Loom spec defines an orchestrator that dispatches work from GitHub Issues, runs coding agents in isolated workspaces, and manages concurrency. AutoResearchClaw's PIVOT/REFINE loop is an orchestration pattern that Loom could adopt:

**Issue state machine:** An issue can PROCEED (continue execution), REFINE (re run with modifications), or PIVOT (close this issue and open a new one with different approach). This maps directly to Loom's retry and dispatch logic.

**Checkpoint resume:** AutoResearchClaw writes checkpoints after each stage. Loom's workspace manager could adopt this pattern for agent runs: if an agent run is interrupted, resume from the last checkpoint rather than restarting.

**Decision gates:** The three gate stages (5, 9, 20) map to Loom's concept of handoff states. A successful run may end at "PR ready for human review," not necessarily "issue closed." This is the same principle: human checkpoints in an automated pipeline.

### Synthweave as Knowledge Layer

AutoResearchClaw's knowledge base (6 categories, YAML frontmatter, evidence refs) is a simplified version of what Synthweave provides. The connection:

- AutoResearchClaw's KB is per run, local. Synthweave's is cross run, shared.
- AutoResearchClaw's evolution store captures lessons from failures. Synthweave captures institutional knowledge across all agent runs.
- The MetaClaw bridge (lesson → skill conversion) is the exact pattern for Synthweave: agent experiences become institutional knowledge that future agents can access.

**Integration opportunity:** If Loom runs AutoResearchClaw as a tool, Synthweave becomes the cross run memory layer. Evolution lessons from one research run are available to all future runs across the organization, not just the `~/.metaclaw/skills/` directory.

---

## 12. Limitations and Risks

### AutoResearchClaw Specific

1. **Scientific validity.** As analyzed in section 7, the pipeline produces papers, not science. The outputs may look rigorous but lack genuine falsification, assumption testing, and epistemic honesty.

2. **LLM dependency.** Every stage except hardware detection and sandbox execution depends on LLM quality. With a weak model, the entire pipeline degrades. The `fallback_models` chain mitigates API failures but not quality issues.

3. **Sandbox limitations.** The sandbox runs generated Python code. Complex experiments (multi GPU training, distributed systems, real data) require Docker or SSH remote modes that introduce operational complexity.

4. **Citation laundering risk.** Real papers are collected and cited, but the pipeline may cite papers it hasn't actually read (only abstracts and metadata are available). The knowledge cards are LLM summaries, not genuine comprehension.

5. **Metric gaming.** The optimization loop can produce code that achieves good metrics on synthetic benchmarks without meaning. The saturation detection is a band aid, not a fix.

### Adaptation Risks

1. **Over engineering.** The 23 stage pipeline is designed for academic papers. Our experiment protocol should be simpler: 10 steps, no paper writing stages.

2. **False rigor.** Adopting the vocabulary (hypothesis, falsification, controlled experiment) without the substance (genuine risk of being wrong, real data, independent verification) would make us worse, not better, because we'd believe we are being scientific when we aren't.

3. **Tool dependency.** Building on AutoResearchClaw directly would couple us to their pipeline. Better to extract patterns and implement our own lightweight version.

---

## 13. Verdict and Next Steps

### What AutoResearchClaw Does Well

- **Engineering quality.** Clean architecture, typed contracts, checkpoint/resume, self healing, bridge adapters. Well built software.
- **Literature integrity.** Real API queries, 4 layer citation verification, anti hallucination guards. The best part of the pipeline.
- **Quality monitoring.** Template detection, methodology evidence consistency checking, peer review with rubric. Genuinely innovative quality layer.
- **Self learning.** Evolution store with time decay, cross run skill generation via MetaClaw. Good institutional memory pattern.

### What It Gets Wrong

- **Conflates paper production with scientific inquiry.** The pipeline optimizes for publishable output, not for learning.
- **No genuine falsification.** Hypotheses are confirmed, not tested. Negative results trigger pivots, not findings.
- **Debate is weak.** Parallel perspectives without interaction, no adversarial challenge, no genuine disagreement mechanism.
- **Closed loop self confirmation.** The same LLM generates everything. No external grounding breaks the cycle.

### Recommended Next Steps

1. **Design the Sivart Experiment Protocol** as specified in section 9. Implement it as a lightweight framework: spec files, sandbox execution, verdict recording, learning archive. No paper pipeline. Issue for tracking.

2. **Extract reusable components.** The sandbox execution pattern, metric parsing, NaN detection, checkpoint system, and evolution store are directly reusable without the paper pipeline. Consider whether to fork these or reimplement.

3. **Build the no man agent.** The institutional AI analysis called for it. AutoResearchClaw's peer review validates the need. A dedicated challenger agent for Agent Factory governance.

4. **Connect to Synthweave.** The evolution store and KB patterns should feed into Synthweave as the cross run intelligence layer. Lessons from agent experiments become institutional knowledge.

5. **Test the experiment protocol on a real question.** Pick a concrete agent development question ("does adding X improve Y?"), run the full protocol, and evaluate whether the process produces genuine learning or just process overhead.
