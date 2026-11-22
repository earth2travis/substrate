# Self-Improvement Memory: Harness Optimization That Survives a Model or Benchmark Change

Raw research file. Deep dive produced 2026-11-22 on arXiv:2611.18856v1, "Self-Improvement Memory Enables Continual Recursive Self-Improvement", by Xin Yu, Fei Xia, Jiaqi Pan, Youbao Tang, Chengzhi Liu, Adams Yu, Sicong Jiang, Yanfei Chen, Lingzhou Xue, and Ting Yu (Google Cloud AI, Google DeepMind, Google Cloud AI Research, Penn State; 13 November 2026, cs.LG). The work was done while Xin Yu was a Google intern; correspondence xinyulucas@google.com; the paper carries a Google copyright notice.

This is the first node in the graph that carries a measured result about harness evolution rather than a position or a taxonomy. The adjacent nodes are strategic or definitional: [[rsi-anthropic-openai-deep-dive]] records what Anthropic and OpenAI say about recursive self-improvement, [[rsi-survey-autonomy-levels-deep-dive]] records a capability taxonomy over autonomy levels, [[harness-engineering]] records the practice as OpenAI describes it, and [[agent-harness-architecture]] records the primitives. This one has a p-value, a confound, and an honest account of where its own mechanism failed. Related: [[dream-rsi-replay-simulator-deep-dive]], [[openai-harness-engineering]], [[graph-engineering]], [[agent-platform-2027]], [[hermes-self-evolution]] (the same idea applied to this agent stack).

Claims are tagged FACT (verified against the paper text this session), BACKGROUND (established record), or INTERPRETATION (my reading). Composite SF authors' individual records were not verified; see the Reception section.

## 1. The claim, in one pass

FACT, the abstract: "Harness optimization is often studied with a fixed policy model and benchmark. When either changes, the optimizer must decide which parts of an evolved harness to reuse or revise, but the harness alone may not explain why earlier edits were made or how they performed."

FACT, the two named challenges, from the introduction:

- **Adapting to a new model.** Two settings: multi-model serving, where one shared harness supports different policy models, and model evolution, where new versions replace earlier ones within a family. The failure mode: "modifications suited to one policy can interact differently with another, even when the benchmark stays fixed."
- **Adapting to new data.** "With the policy fixed, a different task distribution can expose failures that source optimization did not address." Their example: a completion gate that checks whether commands ran successfully may need to also check whether a feasible solution is optimal.

FACT, the two concrete failure cases that motivate the whole paper:

- Workspace: an Opus-evolved harness, run on Gemini, starts at 68.41, below the seed harness's 73.89. The inherited experience is worse than starting over.
- Text classification: a source-evolved FewShotAll harness starts at 72.92 on the target suite, below the seed's 75.72.

FACT, the gap the paper targets: "In either transition, the evolved harness alone leaves important questions unanswered: why was an edit proposed, what was it expected to fix, and what happened when it was tested? Source optimization produces this evidence, but it need not accompany the harness. Without this history, target optimization may repeat earlier attempts or change inherited components without knowing their purpose."

INTERPRETATION: read that passage carefully, because it is an empirical restatement of the Substrate's own first principle. The paper's finding is that an artifact without its provenance is not reusable, only its outputs are, and the outputs do not carry the reasoning that produced them. Provenance is not optional is not a documentation preference here. It is the difference between an inherited harness that scores below a fresh start and one that scores above it.

FACT, the two contributions:

- **CRSI, Continual Recursive Self-Improvement**: "harness optimization continues after a benchmark or policy-model change while preserving a compatible executable interface." Two variants: cross-dataset, where the benchmark changes and the policy is fixed, and cross-model, where the policy changes on the same benchmark and split.
- **SIM, Self-Improvement Memory**: memory "for the harness optimizer, rather than the task-solving policy". It "groups edits by the recurring harness problems they address" and conditions both proposal and selection.

INTERPRETATION on the framing: "recursive self-improvement" is doing heavy lifting here. The policy weights are frozen throughout. What improves is the harness that wraps the policy, and what carries forward is the optimizer's memory of its own past edits. This is harness-level RSI, not weight-level RSI, and the distinction matters when the term is quoted elsewhere.

## 2. The formal setup

FACT, the loop, following Meta-Harness (Lee et al. 2026): optimize an executable harness H around a fixed policy model M, where "the harness determines the model's context, tools, and execution flow." A setting is sigma = (M, X), with disjoint evolve and held-out sets X_evo and X_eval, and the score J(H; M, X) follows the benchmark's own aggregation rule.

FACT, the visibility rule, which is the load-bearing constraint: "Only evolve-set feedback is available for proposing edits, selecting candidates, updating SIM, or deciding when to stop." The held-out set is never shown to the optimizer.

FACT, the loop equations. A run is N rounds; at round t the evaluator executes H_t on X_evo and returns scores, traces, and errors as F_t. Then:

- C_t = P(H_t, F_t, D_t), where D_t is the run history (earlier feedback and code diffs) and P is the proposer, generating k candidates.
- H_{t+1} = S(H_t, F_t, C_t, F_t^C), where S is the selector, screening proposals before execution and choosing among evaluated candidates by "performance, complexity, domain specificity, and regression risk", and F_t^C is feedback from the candidates that passed screening.
- If no candidate is accepted, H_{t+1} = H_t. The proposer and selector are LLM-based harness engineers; M is the policy that executes the tasks.

FACT: main comparisons use N = 10 rounds with k = 5 candidates per round and five rollouts per task.

## 3. Self-Improvement Memory, the mechanism

FACT, the entry structure. For a root-cause hypothesis c_i, such as premature completion, an entry is m_i = (c_i, [(a_ij, o_ij, p_ij)]_j), where j indexes attempts in order and M_t = {m_i} is the current memory.

FACT, the fields, verbatim: "Each attempt stores the modification and its rationale a_ij, predicted and observed task outcomes o_ij, and provenance p_ij (domain, benchmark, policy, and round)." Predictions are recorded before evaluation and checked afterward.

FACT, the update rule: "Each proposal cites an existing root cause or names a new one. After selection, only the chosen candidate is recorded in e_t, including its measured outcomes even when the edit regresses or fails to fix a predicted task. The update M_{t+1} = U(M_t, e_t) appends this record to the cited problem or creates a new entry, preserving earlier attempts." If no edit is accepted, e_t is empty and the memory is unchanged. "Entries with identical root-cause text are merged without dropping their histories."

FACT, how it is read: "At each round, the proposer receives the complete SIM in its system prompt, and the selector reads the same record when assessing candidates. Both read all entries without retrieval or truncation." The augmented loop is Eq. 3, the same equations as above with M_t appended to both arguments. INTERPRETATION: this is a deliberate bet on full context rather than retrieval, the same bet the graph-engineering discourse calls harness engineering, and it is why the mechanism is cheap: a JSON file in the system prompt.

FACT, the on-disk shape (Appendix D.3): one JSON file holding next_id, a carried_from record (arm, domain, into), an aliases map, and a problems list. Each problem carries an id, a name which is the root-cause hypothesis, an opened_round, and an attempts list. Each attempt carries the round, sample, accepted flag, backfilled flag, what was changed, files touched, predicted fixes, fixed and missed outcomes, passed and total trials, and domain. An edit may later change or be replaced while its record stays in the memory.

FACT, matching (Appendix D.1): the proposer itself decides whether a diagnosis matches an existing root cause. There is no separate similarity model. The choice is saved in the round's change manifest before evaluation, and entries merge deterministically only when the root-cause text is identical.

FACT, the eight operational rules for using the memory, verbatim from Appendix D.2. This is the most reusable artifact in the paper:

1. Treat entries as prior experience, with flexibility to choose a different edit.
2. Check the domain, benchmark, and model behind each entry.
3. Start with an existing diagnosis when it explains the current failure.
4. Reuse the rationale and reassess the edit after a benchmark or model change.
5. Revise, replace, or override a harness modification when new evidence warrants it.
6. Revisit a tested direction only when new evidence justifies it.
7. Create a new problem entry when existing diagnoses do not explain the failure.
8. Give task-specific evidence more weight in similar settings and less when both benchmark and model change.

## 4. The experiment

FACT, four domains, each a source-evolved harness that stays executable on the target:

- **Coding.** Source Terminal-Bench 2.1 to target Terminal-Bench 4. Containerized shell tasks scored by their own tests. Seeds: a minimal AHE seed and Terminus-2.
- **Text classification.** Source 3-dataset suite to an 8-dataset target suite absent from source RSI, using the online classification environment from Meta-Harness. Seeds: NoMemory and FewShotAll.
- **Agentic workspace.** Source Harvey LAB to the equal-weight mean of JobBench, GDPval, and APEX-Agents. Seed: a ReAct agent over an MCP tool gateway.
- **Engineering design.** Source EngDesign to Frontier-Eng, scored by frozen verifiers. Same ReAct plus MCP seed.

FACT, sizes (Table 4): coding 89 source tasks to 66 target; text classification 412 examples to 1,000; workspace 160 to a merged 765 (JobBench 65, GDPval 220, APEX-Agents 480); engineering 67 to 47.

FACT, models and budgets: cross-dataset CRSI uses Gemini 3.8 Flash as the policy in both stages, and the same model serves as proposer and selector in the main comparisons. Cross-model transfer evolves with Claude Opus 5.5 and continues on Gemini 3.8 Flash. Policy weights stay frozen. Tasks are split uniformly at random into approximately equal evolve and held-out halves.

FACT, the four comparison conditions, all sharing target policy, tasks, and round and candidate budgets:

- **Cold Start** (H_0, no memory): the seed harness, optimized on the target.
- **Harness Transfer** (H_S, no memory): the source-evolved harness, no memory. This is the harness-only continuation baseline.
- **Problem-Only Memory** (H_S, root causes only): the source-evolved harness plus the diagnoses, with attempts, rationale, and outcomes stripped. This is the root-cause-only baseline.
- **Full SIM** (H_S, full record): the source-evolved harness plus the complete memory, updated during target optimization.

INTERPRETATION: the clean ablation is Problem-Only against Full SIM, because they share the harness and the root causes and differ only in the rationale, outcomes, and provenance. Harness Transfer is the right primary control against Full SIM, since both start from H_S. Cold Start cannot be a fair memory control because it begins from a different harness entirely, which is exactly why the paper reports Cold Start for context but anchors the claim on Harness Transfer.

## 5. The results

FACT, cross-dataset, six settings (Table 5), format Cold Start / Harness Transfer / Problem-Only / Full SIM, each shown as before to after on the held-out target set:

| Setting | Cold Start | Harness Transfer | Problem-Only | Full SIM |
|---|---|---|---|---|
| Coding / AHE | 16.36 to 19.39 | 18.18 to 20.61 | 18.18 to 18.79 | 18.18 to **24.85** |
| Coding / Terminus-2 | 18.18 to 19.39 | 19.39 to 19.39 | 19.39 to 20.61 | 19.39 to **21.82** |
| Text / NoMemory | 68.60 to 72.00 | 71.40 to 71.00 | 71.40 to 73.40 | 71.40 to **73.60** |
| Text / FewShotAll | 75.72 to 75.92 | 72.92 to 74.12 | 72.92 to 75.52 | 72.92 to **77.92** |
| Workspace / ReAct | 73.89 to 82.98 | 74.93 to 85.07 | 74.93 to 85.54 | 74.93 to **87.89** |
| Engineering / ReAct | 39.13 to 40.87 | 39.13 to 42.61 | 39.13 to 42.61 | 39.13 to **46.96** |

FACT, the stated claim: Full SIM finishes highest in all six, exceeding Harness Transfer by 2.43 to 4.35 points and Problem-Only Memory by 0.20 to 6.06 points.

FACT, cross-model, four settings (Table 6), Opus 5.5 source to Gemini 3.8 Flash target, same format:

| Setting | Cold Start | Harness Transfer | Problem-Only | Full SIM |
|---|---|---|---|---|
| Coding / AHE | 16.36 to 19.39 | 13.94 to 18.18 | 13.94 to 20.61 | 13.94 to **21.82** |
| Text / FewShotAll | 78.32 to 82.72 | 77.72 to 80.20 | 77.72 to 81.32 | 77.72 to **83.80** |
| Workspace / ReAct | 73.89 to 82.98 | 68.41 to 73.42 | 68.41 to 79.22 | 68.41 to **84.75** |
| Engineering / ReAct | 39.13 to 40.87 | 34.78 to 42.61 | 34.78 to 46.96 | 34.78 to **50.43** |

FACT: when the Opus-evolved harness first runs on Gemini, it scores below Gemini's own seed harness in every domain, with deficits from 0.60 points (text classification) to 5.48 (workspace). Full SIM finishes highest in all four, exceeding harness-only continuation by 3.60 to 11.33 points. The workspace case is the cleanest illustration in the paper: from the same inherited start of 68.41, harness-only continuation reaches 73.42, which is below the seed's 73.89, while Full SIM reaches 84.75. Carrying the memory turned a losing inheritance into the best result in the table.

FACT, the paired coding study (Table 3, the strongest evidence in the paper): ten independent Terminus-2 source runs on TB2.1 seed two matched ten-round TB4 continuations each, one inheriting that run's SIM and one not, with harness, policy, benchmark, round count, and candidate budget matched. SIM finishes higher in 9 of 10 pairs; the single loss is run 8, at minus 0.61 points. Mean paired advantage 2.36 points, 95% CI [1.05, 3.68], paired t(9) = 4.06, two-sided p = 0.003, signed-rank p = 0.006, dz = 1.28. Means: start 18.36, no SIM 19.33, SIM 21.70.

FACT, the harness-agent ablation (Table 7): swapping Gemini 3.8 Flash for Claude Opus 5.5 as proposer and selector during source RSI raises held-out scores by 5.50 (AHE) and 4.05 (Terminus-2) against 4.44 and 4.00 for Gemini. INTERPRETATION: the optimizer's identity matters, but modestly on the held-out margin, and this is a source-stage ablation rather than a test of the memory itself.

## 6. Where it fails, in the paper's own numbers

These are the parts that make the paper worth trusting.

- FACT: text classification with the NoMemory seed, harness-only continuation ends at 71.00, below the seed's 72.00 and below its own start. Transfer without memory can lose ground outright.
- FACT: the source-evolved FewShotAll harness improved held-out source scores by 2.75 to 6.41 points, and still started target RSI below the seed (72.92 against 75.72). A successfully evolved harness can be a net negative when transplanted, which is the paper's whole motivation stated as a result.
- FACT: harness-only continuation finishes below Cold Start in three of the four cross-model domains.
- FACT: across the generation chain on Gemini models (Table 1), continuation finishes 0.8 points lower on Gemini 4 Argon (CRSI 94.8 against fresh RSI 95.6), and improves in only two of the three subsequent generations. Continued optimization is not monotonically good.
- FACT: on source retention, Full SIM loses three successful rollouts of 225 against four for Problem-Only and six for harness-only, while gaining far more on the target. There is a retention cost to carrying memory.
- FACT, and the most honest item in the paper: SIM entry P3 held that "a deliverable can be internally correct yet violate the verifier's external contract". It fixed 1 of 4 source tasks, then 0 of 2 in the first target round, then 1 of 2 in the next. The entry was accepted each time, the predictions failed each time, and the record kept the failures. P8 fixed 0 of 4 predicted tasks across both its attempts. The paper states it "include[s] an accepted edit that failed to repair its target tasks" as a deliberate disclosure.
- FACT: the engineering domain's mechanism table contains the telling row "Prompt guidelines without SIM (reverted)": guidance that harness-only continuation threw away and Full SIM retained and extended.

INTERPRETATION: the collapsed prediction rates are the substance here, not an embarrassment. A plausible root-cause diagnosis lands perhaps a quarter to a half of the time, the memory records the misses, and the next edit is conditioned on them. That is what an honest improvement log looks like, and it is the thing most RSI writing omits.

## 7. Two caveats that bound the result

FACT, the workspace domain is model-judged. Coding is scored by pass@1, text classification by accuracy, and engineering by frozen verifiers, and the paper states plainly that "Neither engineering metric uses an LLM judge." Workspace scores are "computed using scoring interfaces adapted from RRSI, with Gemini 3.8 Flash as the judge."

INTERPRETATION: this is bigger than the paper's own "judge bias" hedge. Gemini 3.8 Flash is simultaneously the policy model under test, the proposer, the selector, and the judge of the workspace domain, which is also the domain with the largest inheritance failure (68.41 against 73.89) and the largest recovery in the cross-model table. The confound is structural rather than incidental: a single model family proposes edits, evaluates them, scores them, and rewrites its own scoring interfaces across the change. The three programmatically scored domains are clean; the fourth, which carries the most dramatic narrative, is not.

FACT, the stated limitations, verbatim: "Within our compute budget, independent RSI repetitions focus on coding; the other domains are evaluated with one run per condition. We study settings with compatible harness interfaces and keep the optimizer's planning and search procedures fixed. Our comparisons evaluate SIM as a complete procedure, combining inherited memory with updates during target optimization."

INTERPRETATION: read together, the limitations mean the ten-run p-value holds only for coding on Terminal-Bench 4, and the six-of-six and four-of-four sweeps rest on single runs per condition in three domains. The cross-dataset and cross-model tables are demonstrations with n = 1 per cell. The paired coding study is the only place with a real statistical claim, and it covers one domain, one seed, and one benchmark pair. The paper is unusually clear about this rather than burying it.

FACT, the ethics statement flags the deeper risk: a self-modifying harness "could satisfy an evaluator without solving the intended task", which is why held-out feedback is kept away from the optimization agents and the failing accepted edit is disclosed. INTERPRETATION: this is the paper's own statement of the reward-hacking hazard that any self-editing system inherits, and it is the same hazard the multi-agent verification literature documents from the other direction.

## 8. The lineage it sits in

FACT: every one of the eight named prior works exists. Identifiers from the paper's own bibliography, with the gap SIM claims to fill:

- **Meta-Harness**, Lee, Nair, Zhang, Lee et al., arXiv:2603.28052 (Stanford IRIS Lab, CoLM 2026). An agentic proposer with filesystem access to prior candidates' source, scores, and traces; searches harness configurations end to end. INTERPRETATION: this is the direct ancestor. SIM inherits Meta-Harness's loop and adds the memory that survives a setting change.
- **AHE, Agentic Harness Engineering**, Lin et al., arXiv:2604.25850. Auto-evolves coding-agent harnesses from observability signals and tests one frozen transfer to SWE-bench Verified. SIM conditions the continuation rather than only evaluating transfer.
- **SIA**, Hebbar et al., arXiv:2605.27276. Improves harness and model weights jointly. INTERPRETATION: SIM's choice to freeze weights is what makes its gains attributably harness-side, and it is the cleanest statement of the harness-only boundary in the field.
- **HarnessBank**, Luo et al., arXiv:2607.13683. Groups candidate harnesses by modified component and diagnosed failure for recombination. FACT: the closest structural precedent, since SIM also groups edits by diagnosed problem; SIM's delta is the rationale and outcome record plus the span across a change.
- **PluginRSI**, Shi et al., arXiv:2609.32423. Reuses an evolved plugin library across solver models. SIM carries a problem-keyed rationale log rather than a reusable artifact library.
- **Harness2**, Xu et al., arXiv:2610.14224. Recursive harnessing across benchmarks and models, expecting reuse. SIM supplies the memory acquisition assumes.
- **Evo-Harness**, Wei et al., EMNLP 2026 pp. 22343 to 22358. No arXiv identifier in the bibliography; do not cite one. FACT: it is not discussed in the related-work section at all, only listed in the bibliography and grouped in Appendix A.2 as a task-stream neighbor.
- **The survey**, Yu et al. 2026b, "From Harness Optimization to Recursive Self-Improvement", Preprints.org v2, no arXiv identifier. FACT: this is the same group as SIM (Xin Yu, Chengzhi Liu, Lingzhou Xue recur), so the paper is explicitly extending its own survey. FACT, and a correction worth keeping: Yu et al. 2026a in the same bibliography is unrelated, a different Yu (W. Yu) on Harmony Harness, arXiv:2610.15150, probably Microsoft Research.

FACT, the crowding: the bibliography spans March to October 2026 across at least six independent harness-evolution efforts, plus benchmarks (EvoHarnessBench, Frontier-Eng) and adjacent work (Continual Harness, Mixture of Self-Improving Branches, Rethinking the Evaluation of Harness Evolution, Adaptive Auto-Harness). INTERPRETATION: SIM is not first in the field. It is arguably first to name the multi-setting continuation case and attach a provenance memory to it.

## 9. Reception, or the absence of it

FACT: no Hacker News threads and no Reddit posts were found for the paper, its title, or "self-improvement memory", across ordinary search and an X-search fallback. Aggregator presence only: a Hugging Face Papers page with 38 upvotes, plus opentrain.ai, academy.dair.ai, and a Montreal.AI share. X shows a small cluster dated 18 to 22 November. Chinese-language media covered it inside a week, with Zhidx and 36kr framing it as "Google achieved RSI internally", which INTERPRETATION is a misreading of a harness-memory result as a weights-level milestone.

INTERPRETATION: for a Google Cloud AI and DeepMind paper carrying the phrase "recursive self-improvement" in its title, nine days of silence on the technical forums is itself the finding. The framing traveled and the engineering did not.

FACT, verified models: Gemini 3.8 Flash announced 2 September 2026; Claude Opus 5.5 released 22 September 2026 and generally available on Google Cloud. Both precede the paper by roughly two months, so the cross-model experiment is chronologically coherent.

## 10. Where the mapping breaks

- **The novelty is narrow and the paper says so.** It does not claim unbounded self-improvement, it reports a counterexample where memory hurt, and it positions itself as a continuation setting rather than a new optimizer. Read it as a memory design for harness evolution, not as a milestone in machine self-improvement, whatever the title and the Chinese coverage suggest.
- **"Recursive self-improvement" oversells the mechanism here.** Weights are frozen. The policy never improves itself. A harness-optimizing memory improves a wrapper around a fixed model, and the recursion is over edit histories, not over capabilities. The term is inherited from the field, not earned by this experiment.
- **The strongest result is the narrowest.** The p = 0.003 paired study covers ten runs of one seed on one benchmark pair in one domain. The six-of-six and four-of-four sweeps, which read as the headline, are single-run cells.
- **The workspace domain, the most dramatic, is the least clean.** Judge, proposer, selector, and policy are all Gemini 3.8 Flash, and the judge's interfaces are rewritten across the change. Treat the 68.41 to 84.75 recovery as a demonstration, not a measurement.
- **The internal margin can be near zero.** The gap over the strongest alternative is as small as 0.20 points on one setting. "Full SIM wins in all ten" is true and, on that cell, close to noise.
- **The mechanism's cost is hidden in the context window.** SIM is read in full, untruncated, in both the proposer and selector system prompts, with no retrieval. It scales by growing the prompt. The paper does not report the token cost, and no memory-length sensitivity ablation exists in the appendices.
- **The most transferable part is not the result, it is the eight rules and the P3 record.** A diagnosis that fixes one of four tasks, then zero of two, then one of two, kept in the log with its failures attached, is a better artifact than any of the win tables. Any system that accumulates improvement experience should copy the discipline, not the benchmark.
- **For this Substrate, the paper is a proof of its own premise.** "The harness alone may not explain why earlier edits were made or how they performed" is the provenance rule, demonstrated with numbers: without the history, an inherited artifact scores below a fresh start, and with it, above. The eight operational rules are worth lifting wholesale into how this graph records research, since they are a protocol for carrying reasoning across a context change, which is exactly what a knowledge graph is for.

## 11. Compression points for synthesis

1. arXiv:2611.18856v1 is "Self-Improvement Memory Enables Continual Recursive Self-Improvement" (Google Cloud AI, DeepMind, Penn State, 13 November 2026). It defines Continual Recursive Self-Improvement (CRSI), the setting where harness optimization continues after the policy model or benchmark changes, and proposes Self-Improvement Memory (SIM), a record of harness problems, edits, rationales, predicted and observed outcomes, and provenance that conditions the proposer and selector across the change. Policy weights are frozen; this is harness-level improvement, not weight-level.
2. The motivation is measured, not asserted: an Opus-evolved harness starts at 68.41 on Gemini against the seed's 73.89, and a source-evolved FewShotAll harness starts at 72.92 against the seed's 75.72. A successfully evolved harness can be worse than starting over when transplanted, because the harness travels and the reasoning behind its edits does not.
3. The mechanism is deliberately cheap: a single JSON memory keyed by root-cause hypothesis, where each attempt stores the edit and rationale, the predicted and observed outcomes, and provenance of domain, benchmark, policy, and round. New diagnoses create entries, cited diagnoses append attempts, identical root-cause text merges, and accepted edits are recorded even when they regress. Proposer and selector both read the whole memory untruncated, with no retrieval.
4. Appendix D.2 holds eight operational rules for using the memory, and they are the most reusable artifact in the paper: treat entries as prior experience; check the domain, benchmark, and model; start from an existing diagnosis when it fits; reuse the rationale and reassess the edit after a change; revise, replace, or override on new evidence; revisit a tested direction only with new evidence; create a new entry when existing diagnoses do not explain the failure; weight task-specific evidence by how similar the setting is.
5. The experiment spans four domains (coding on Terminal-Bench 2.1 to 4, text classification over 3 to 8 datasets, agentic workspace from Harvey LAB to JobBench plus GDPval plus APEX-Agents, and engineering design from EngDesign to Frontier-Eng), with Gemini 3.8 Flash as policy and Claude Opus 5.5 in the cross-model leg, over ten rounds and five candidates per round.
6. Four conditions share budgets: Cold Start, Harness Transfer (harness only), Problem-Only Memory (diagnoses only), and Full SIM. The clean ablation is Problem-Only against Full SIM, which isolates the rationale, outcomes, and provenance; the primary control is Harness Transfer, which shares Full SIM's starting point.
7. Full SIM finishes highest in all six cross-dataset and all four cross-model settings, ahead of harness-only continuation by 2.43 to 4.35 points cross-dataset and 3.60 to 11.33 cross-model. The smallest margin over the strongest alternative is 0.20 points, so "wins everywhere" is true but not always by much.
8. The only statistically strong result is the paired coding study: ten independent source runs, each seeding two matched continuations, SIM higher in 9 of 10, mean advantage 2.36 points, p = 0.003, dz = 1.28. It also covers one domain, one seed, and one benchmark pair.
9. The paper reports its own failures plainly: harness-only continuation can score below the seed and below Cold Start, continuation regresses on Gemini 4 Argon (94.8 against 95.6), there is a retention cost on source tasks, and a disclosed accepted edit (P3) fixed one of four tasks, then zero of two, then one of two while its predictions failed each time.
10. Two caveats bound everything: the workspace domain is judged by Gemini 3.8 Flash, which is also the policy, proposer, and selector, so its 68.41 to 84.75 recovery is a demonstration rather than a clean measurement; and the authors state that independent repetitions focus on coding, with one run per condition in the other three domains.
11. The paper sits in a crowded March to October 2026 field (Meta-Harness arXiv:2603.28052, AHE arXiv:2604.25850, SIA arXiv:2605.27276, HarnessBank arXiv:2607.13683, PluginRSI arXiv:2609.32423, Harness2 arXiv:2610.14224, plus Evo-Harness and the group's own Preprints.org survey, both without arXiv identifiers). It is not first, only first to name the multi-setting continuation case with a provenance memory.
12. Reception is near zero: no Hacker News or Reddit threads nine days after posting, only aggregator pages (a Hugging Face Papers page with 38 upvotes) and Chinese coverage reading it as "Google achieved RSI internally", which misreads a harness-memory result as a weights-level milestone.
13. For this graph, the paper demonstrates the Substrate's own provenance principle with numbers: an artifact without the record of why it was built is not reusable, and can be worse than nothing. The eight operational rules are a protocol for carrying reasoning across a context change, which is the graph's purpose stated as engineering practice.

## Sources

### Primary, verified this session

- arXiv:2611.18856v1, "Self-Improvement Memory Enables Continual Recursive Self-Improvement", Xin Yu, Fei Xia, Jiaqi Pan, Youbao Tang, Chengzhi Liu, Adams Yu, Sicong Jiang, Yanfei Chen, Lingzhou Xue, Ting Yu, 13 November 2026. Both the HTML rendering and the PDF were retrieved and read in full; all quotations above come from that text. Abstract, Introduction, Related Work, Method (3.1, 3.2), Experiments (4.1), Conclusion, Limitations, Ethics Statement, and Appendices A through F were read across the retrieved text.
- Results tables 1 through 8 and Figures 6, 9, 10, 11, and 12 were read from the HTML tables; the PDF layout extraction renders tables as headerless number grids and interleaves the two columns, so all table values were taken from the HTML and cross-checked against the figure panels.

### Verified cited works

All eight named prior works exist; identifiers are as they appear in the paper's own bibliography. Meta-Harness, Lee, Nair, Zhang, Lee et al., arXiv:2603.28052, CoLM 2026, Stanford IRIS Lab. AHE, Lin et al., arXiv:2604.25850. SIA, Hebbar et al., arXiv:2605.27276. HarnessBank, Luo et al., arXiv:2607.13683. PluginRSI, Shi et al., arXiv:2609.32423. Harness2, Xu et al., arXiv:2610.14224. Evo-Harness, Wei et al., EMNLP 2026, pages 22343 to 22358, no arXiv identifier. Survey, Yu et al. 2026b, Preprints.org v2, no arXiv identifier. Adjacent: Continual Harness arXiv:2605.09998, Mixture of Self-Improving Branches arXiv:2609.37834, Rethinking the Evaluation of Harness Evolution arXiv:2607.12227, Frontier-Eng arXiv:2604.12290, APEX-Agents arXiv:2601.14242, Terminal-Bench (Merrill, Shaw, Carlini, Li et al.) arXiv:2601.11868, ICLR 2026, Laude Institute with Stanford, leaderboard at tbench.ai.

### BACKGROUND

- Terminal-Bench is real and measures resolution rate of agents completing hard, realistic command line tasks in a container. The paper uses Terminal-Bench 2.1 as source and Terminal-Bench 4.0 as target. SWE-bench Verified appears only as the target AHE used in prior work, not in SIM's own experiments.
- Gemini 3.8 Flash announced 2 September 2026; Claude Opus 5.5 released 22 September 2026.

### Received through secondary or single-source channels (verify before direct quotation)

- The reception picture, including the Hugging Face Papers upvote count, the November 18 to 22 X cluster, and the Chinese coverage framing, rests on search results and an X-search fallback. The absence of Hacker News and Reddit threads was corroborated by ordinary search.
- Xin Yu is a Penn State statistics PhD student and Google research intern; the internship project is named Self-Improvement Memory on LinkedIn, and lucasxinyu.github.io lists recursive self-improvement as the focus. The individual publication records of the Google-side authors were not verified, so whether there is a standing named harness-optimization team at Google is unconfirmed; the byline pattern suggests an established Penn State anchored collaboration with rotating Google host authors.
- "Evolving Agents in the Dark" and a work referred to as Exo (arXiv:2611.00463) surfaced only through X-derived search and are unverified.

### Open questions a later pass could close

- The token and latency cost of reading the full memory in both system prompts every round is not reported, and there is no memory-length or round-count sensitivity ablation. A cheaper encoding of the same record is the obvious engineering question.
- One run per condition in three of the four domains means the cross-dataset and cross-model sweeps are demonstrations. Repeating the non-coding domains would be the highest-value follow-up.
- Whether SIM composes with joint weight and harness updates (the SIA route) is untested, and the paper deliberately holds weights frozen.
- Whether a heterogeneous judge and optimizer would preserve the workspace result is the direct test of the main confound.
