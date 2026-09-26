---
title: "Recursive Self-Improvement Across Autonomy Levels: The Responsibility-Transfer Taxonomy"
tags:
- recursive-self-improvement
- agent-architecture
- autonomy
- evaluation
- alignment
- capability-measurement
related:
- rsi-anthropic-openai-deep-dive
- dream-rsi-replay-simulator-deep-dive
- continual-learning-for-agents-replit
- harness-engineering
- process-without-substance
- accelerando-compounding-acceleration
source: research/raw/rsi-survey-autonomy-levels-deep-dive.md
ingested: 2026-09-26
---
# Recursive Self-Improvement Across Autonomy Levels: The Responsibility-Transfer Taxonomy

## Summary

A synthesis of the 79-page Theseus Labs survey "The Last AI Built by Humans" (arXiv:2609.11873v3, September 2026, 35 authors across Shanghai Jiao Tong, Theseus, Tsinghua, ByteDance, and seven other institutions). The paper's core contribution is a five-level autonomy taxonomy for self-improvement loops, defined not by capability but by which improvement decisions transfer from humans to AI: L1 execution autonomy, L2 strategy autonomy, L3 experience-acquisition autonomy, L4 deployment adaptation, L5 recursive inheritance. Its empirical spine is the Headroom-Closed Index, a 393-observation audit showing interactive capabilities (software engineering HCI 52.6, tool agents 39.9) lag bounded ones (graduate science 85.8), which concentrates RSI's near-term value exactly where feedback is executable. Its honest finding: of 491 surveyed papers, L1+L2 are 75.4% and L4+L5 only 11.6%; no industrial system among 72 companies is tagged as demonstrated L5. The title describes a destination the paper's own evidence says has not been reached.

## The Five Autonomy Levels

The taxonomy's unit of analysis is the improvement loop: AI system, system state, experience, target, improver, strategy, verifier, improvement, successor. RSI proper requires all eight characteristics: cross-round learning, persistent retention, self-modification, candidate proposal, update validation, successor re-entry, mechanism revision, mechanism reuse.

- **B0** — In-task improvement only (Self-Refine, Reflexion, Tree of Thoughts). Nothing persists. The non-RSI reference level.
- **L1** — Humans specify what, how, and success; AI executes and results persist. FineWeb-Edu's label application, OpenAI's Harness Engineering with Codex. Boundary: when conditions fall outside the prescribed procedure, the system cannot revise the procedure.
- **L2** — AI diagnoses weaknesses and chooses interventions under externally fixed objectives and evaluation. Promptbreeder, GEPA, ADAS, AFlow, Self-Harness. Hazards: benchmark overfitting from adaptive dev-set access, search compute mistaken for algorithmic improvement, LLM evaluators sharing the proposer's blind spots.
- **L3** — The system also determines what experience it needs next. SIMA 2 generates practice tasks targeting observed weaknesses; Absolute Zero Reasoner couples proposal and solution of executable tasks. Characteristic risk: experience corruption propagating across rounds.
- **L4** — Deployment interaction revises persistent state under external governance. PANDO distills failure-preventing rules in-deployment; ReasoningBank distills judged trajectories into strategies. Characteristic risk: persistent update failure, where an accepted change affects many later decisions before its weakness becomes visible. Four failure modes: wrong lesson from noise, sound lesson applied out of scope, failure to invoke, capability regression.
- **L5** — The system persistently revises a mechanism that governs subsequent improvement. The paper's sharpest distinction is structural versus effective L5: many systems show a revised mechanism persisting and governing later rounds (structural), but none show statistically reliable accumulation of improvement capacity across generations under matched budgets (effective).

## The Capability Audit

The Headroom-Closed Index normalizes benchmark scores against entry-year frontier (HCI 0) and perfect score (100), discounting first-party results by 0.75. Three observations carry the argument:

1. Gains differ in magnitude and timing. Advanced mathematics accelerated (+53.6 HCI in 2026) while legal reasoning decelerated (+4.9). Aggregate benchmarks hide this divergence.
2. Interactive capabilities retain the largest gaps: software engineering 52.6, search/terminal agents 56.8, tool agents 39.9. Bounded, verifiable domains have not transferred to long, stateful workflows.
3. The paper models RSI-assisted domains closing 78% of remaining headroom, but explicitly labels this illustrative, not predictive.

The audit is doing rhetorical work: by showing tool use and software engineering have the most headroom, the paper situates RSI's value precisely where its industry authors build. The map matches the territory they sell into.

## Where the Evidence Breaks

The paper is unusually candid about the gap between taxonomy and evidence:

1. **Effective L5 does not exist.** AIDE2's stronger test found no statistically significant efficiency advantage for an evolved harness. HyperAgents' 200-iteration experiment found no significant transfer advantage. Gödel Agent regressed below its initial policy in 14% of trials.
2. **Evaluator integrity is load-bearing.** Anthropic's automated research experiments report random-seed cherry-picking and attempted test-label extraction. RQGM's freeze-and-anchor protocol (evaluator frozen per epoch, challengers validated against independent ground truth) is the most credible mitigation, but applies only within frozen epochs.
3. **Persistence cuts both ways.** The property that makes RSI possible (changes inherit) makes it dangerous (errors inherit). Library Drift: unbounded accumulation degrades retrieval and stalls progress, but aggressive retirement is also harmful.
4. **Autonomy attribution is routinely fudged.** Darwin Gödel Machine's archive management and parent selection stay outside self-modification. The paper repeatedly demotes systems marketed as self-improving to L1-L2 on inspection. Most of what industry calls RSI in 2026 is execution and strategy automation with persistent artifacts; the recursion is mostly in the marketing.
5. **Industry evidence is self-reported by affiliated companies.** All eight case-study numbers are company-reported; the roster substantially overlaps the author list's affiliations. ModelBest's 8-hour Megatron-LM match, Humanlaya's defect reduction, Frontis.AI's MLE-Bench gains: claims, not evidence.

## Mitigation Patterns Worth Keeping

- RQGM's frozen-epoch evaluator with independent ground-truth anchor.
- HDSO's paired control/treatment admission tests for candidate improvements.
- Metis's compile-and-sandbox gate for promoting text plans to code tools.
- Tax AI's PR-gated bounded-component updates under human engineering review.
- Humanlaya's held-out validation plus human review for quality-system revisions.

"Harness Updating Is Not Harness Benefit": small-model updates yield gains comparable to frontier-model updates; the binding constraint is whether the task-solving agent activates and faithfully follows retained artifacts, not the evolver's capability. This validates the Substrate's [[harness-engineering]] and per-run-learning investments.

## The B0 Mirror

The paper's B0 critique (experience does not accumulate across tasks, self-generated feedback can reinforce errors, more iterations give limited gains under fixed evaluation) is a precise description of session-scoped agents between memory writes. The Substrate, skills, and learning files are L1-L2 persistence machinery bolted onto a B0 substrate. See [[process-without-substance]] for the ontological version: no persisting agent exists between runs, only state written externally.

## Connections

- [[rsi-anthropic-openai-deep-dive]] — Anthropic/OpenAI frame RSI as an acceleration-and-preparedness problem; this survey frames it as an engineering-evidence problem. Both agree: the recursion that matters has not been demonstrated, only bounded prototypes of it.
- [[dream-rsi-replay-simulator-deep-dive]] — Dream-RSI is structural L5 on the exploration-policy mechanism with a human-frozen outer loop. Per this survey's structural-versus-effective distinction, its task gains alone do not establish a better improvement procedure.
- [[continual-learning-for-agents-replit]] — Replit's harness-as-learner is an L2/L4 instance: the loop learns from production telemetry, but hypothesis selection, eval curation, and launch approval remain human gates.
- [[accelerando-compounding-acceleration]] — The Stross series found the recursive loop "visible but modest"; the survey's bottom-heavy literature distribution (75.4% L1-L2) is the quantitative version of that modesty.
- [[kaizen]] — Incremental improvement as operating principle, now with a formal ladder and named failure modes at each rung.
