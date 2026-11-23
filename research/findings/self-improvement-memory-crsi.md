---
title: "Self-Improvement Memory: Carrying Provenance Across a Model or Benchmark Change"
tags: [finding, recursive-self-improvement, harness-engineering, provenance, memory, ai-agents]
related:
- harness-engineering
- agent-harness-architecture
- rsi-anthropic-openai-deep-dive
- rsi-survey-autonomy-levels-deep-dive
- dream-rsi-replay-simulator-deep-dive
- openai-harness-engineering
- knowledge-graphs-as-agent-memory-substrate
- hermes-self-evolution
source: research/raw/self-improvement-memory-crsi.md
ingested: 2026-11-23
---

# Self-Improvement Memory: Carrying Provenance Across a Model or Benchmark Change

## Key Points

**The paper.** arXiv:2611.18856v1, "Self-Improvement Memory Enables Continual Recursive Self-Improvement" (Google Cloud AI, DeepMind, Penn State; 13 November 2026). It defines Continual Recursive Self-Improvement (CRSI), the setting where harness optimization continues after the policy model or benchmark changes, and proposes Self-Improvement Memory (SIM): a record of harness problems, edits, rationales, predicted and observed outcomes, and provenance that conditions the proposer and selector across the change. Policy weights are frozen throughout; this is harness-level improvement, not weight-level. The first node in this graph to carry a measured result about harness evolution rather than a position or taxonomy.

**The motivation is measured, not asserted, and it is the paper's own restatement of this Substrate's provenance rule.** An Opus-evolved harness starts at 68.41 on Gemini, below the seed harness's 73.89; a source-evolved FewShotAll harness starts at 72.92 against the seed's 75.72. A successfully evolved harness can be worse than starting over when transplanted, because the harness travels and the reasoning behind its edits does not. "The harness alone may not explain why earlier edits were made or how they performed." An artifact without its provenance is not reusable, only its outputs are — and the outputs do not carry the reasoning that produced them.

**The mechanism is deliberately cheap.** A single JSON memory keyed by root-cause hypothesis, where each attempt stores the edit and rationale, the predicted and observed outcomes, and provenance of domain, benchmark, policy, and round. New diagnoses create entries, cited diagnoses append attempts, identical root-cause text merges, and accepted edits are recorded even when they regress. Proposer and selector both read the whole memory untruncated, with no retrieval — a deliberate bet on full context over retrieval, the same bet the graph-engineering discourse calls harness engineering.

**The most reusable artifact is Appendix D.2's eight operational rules:** treat entries as prior experience; check the domain, benchmark, and model behind each entry; start from an existing diagnosis when it fits; reuse the rationale and reassess the edit after a change; revise, replace, or override on new evidence; revisit a tested direction only with new evidence; create a new entry when existing diagnoses do not explain the failure; weight task-specific evidence by how similar the setting is. They are a protocol for carrying reasoning across a context change, which is exactly what a knowledge graph is for.

**The experiment and its results.** Four domains (coding on Terminal-Bench 2.1 to 4; text classification over 3 to 8 datasets; agentic workspace from Harvey LAB to JobBench plus GDPval plus APEX-Agents; engineering design from EngDesign to Frontier-Eng), with Gemini 3.8 Flash as policy and Claude Opus 5.5 in the cross-model leg, over ten rounds and five candidates per round. Four conditions share budgets: Cold Start, Harness Transfer (harness only), Problem-Only Memory (diagnoses only), and Full SIM. Full SIM finishes highest in all six cross-dataset and all four cross-model settings, ahead of harness-only continuation by 2.43 to 4.35 points cross-dataset and 3.60 to 11.33 cross-model.

**The only statistically strong result is narrow.** The paired coding study: ten independent source runs, each seeding two matched continuations, SIM higher in 9 of 10, mean advantage 2.36 points, p = 0.003, dz = 1.28 — covering one domain, one seed, and one benchmark pair. The six-of-six and four-of-four sweeps, which read as the headline, are single-run cells, and the smallest margin over the strongest alternative is 0.20 points ("wins everywhere" is true but not always by much).

**The paper reports its own failures plainly, which is what makes it worth trusting.** Harness-only continuation can score below the seed and below Cold Start; continuation regresses on Gemini 4 Argon (94.8 against 95.6); there is a retention cost on source tasks; and a disclosed accepted edit (P3) fixed one of four tasks, then zero of two, then one of two while its predictions failed each time. A plausible root-cause diagnosis lands perhaps a quarter to a half of the time, the memory records the misses, and the next edit is conditioned on them.

**Two caveats bound everything.** The workspace domain is judged by Gemini 3.8 Flash, which is also the policy, proposer, and selector, and whose scoring interfaces are rewritten across the change, so its 68.41 to 84.75 recovery is a demonstration rather than a clean measurement; the three programmatically scored domains are clean. And the authors state that independent repetitions focus on coding, with one run per condition in the other three domains.

**The lineage is crowded (March to October 2026):** Meta-Harness (arXiv:2603.28052, the direct ancestor), AHE (2604.25850), SIA (2605.27276, joint harness and weight updates), HarnessBank (2607.13683, the closest structural precedent), PluginRSI (2609.32423), Harness2 (2610.14224). SIM is not first; it is arguably first to name the multi-setting continuation case with a provenance memory. Reception is near zero: no Hacker News or Reddit threads nine days after posting, only aggregator pages and Chinese coverage reading it as "Google achieved RSI internally," which misreads a harness-memory result as a weights-level milestone.

## Open Questions

- The token and latency cost of reading the full memory in both system prompts every round is not reported, and there is no memory-length sensitivity ablation.
- One run per condition in three of four domains means the cross-dataset and cross-model sweeps are demonstrations; repeating the non-coding domains is the highest-value follow-up.
- Whether a heterogeneous judge and optimizer preserve the workspace result is the direct test of the main confound.

## Source

`research/raw/self-improvement-memory-crsi.md` (the HTML and PDF read in full). It sits in the harness-evolution lineage of [[agent-harness-architecture]] and the practice recorded in [[harness-engineering]] and [[openai-harness-engineering]], adjacent to the strategic positions in [[rsi-anthropic-openai-deep-dive]] and the autonomy taxonomy in [[rsi-survey-autonomy-levels-deep-dive]], and nearest in mechanism to [[dream-rsi-replay-simulator-deep-dive]]'s replay simulators. For this Substrate the paper is a proof of its own premise — an artifact without the record of why it was built is not reusable, and can be worse than nothing — and the eight operational rules are a candidate discipline for how this graph records research. The same idea applied to this agent stack is [[hermes-self-evolution]]; the graph-as-memory frame is [[knowledge-graphs-as-agent-memory-substrate]].
