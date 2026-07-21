---
title: "Recursive Self-Improvement: Anthropic and OpenAI Positions, Mid-2026"
tags: [finding, recursive-self-improvement, anthropic, openai, alignment, preparedness, metr, timelines, coordination]
related:
- accelerando-compounding-acceleration
- karpathy-autoresearch
- loops-as-orchestration-primitive
- agent-factory-production-system
- deployment-governance
source: research/raw/rsi-anthropic-openai-deep-dive.md
ingested: 2026-07-21
---
# Recursive Self-Improvement: Anthropic and OpenAI Positions, Mid-2026

## Summary

A compiled deep-dive on where the two frontier labs actually stand on recursive self-improvement (RSI) as of July 2026. Anthropic's "When AI Builds Itself" (Favaro and Clark, Anthropic Institute) is the most data-rich public account of internal acceleration: >80% of merged code Claude-authored, engineers merging 8x the 2024 code volume, a 52x speedup on training-code optimization (Mythos Preview vs. ~3x for Opus 4 a year earlier), agents recovering 97% of a research-task gap vs. 23% for human researchers, and research judgment beating human next-move choice 64% of the time. OpenAI's posture is threshold-based rather than data-based: the Preparedness Framework v2 defines AI self-improvement as a Tracked Category with a Critical halt condition (superhuman research scientist agent, or a generational model jump in 1/5th the 2024 wall-clock time, sustained), while Altman privately floated RSI "less than six months away" and delaying the IPO because of it. The convergence: both labs are independently building agents that do AI research. The divergence: Anthropic publicizes the acceleration curve and builds verification for a coordinated slowdown; OpenAI defines tripwires and hires people to not cross them unprepared.

## Anthropic's Internal Evidence

The engineering numbers, in one place:

- **Code authorship:** >80% of merged code written by Claude as of May 2026, from low single digits before Claude Code's February 2025 research preview.
- **Throughput:** lines of code per engineer per day flat 2021-2024, climbing in 2025, steep in 2026; Q2 2026 typical engineer merging 8x the 2024 daily volume. The file flags the obvious caveat: quantity is not productivity.
- **Two inflection points:** (1) Claude began running code rather than suggesting it, (2) models began working autonomously over longer horizons. Both are loop-closures, matching the [[loops-as-orchestration-primitive]] lineage.
- **Research acceleration:** Opus 4 (May 2025) ~3x on training-code optimization; Mythos Preview (April 2026) ~52x. A skilled human needs 4-8 hours to reach 4x.
- **Open-ended research:** April 2026, first end-to-end agent-run research project (weak-model-supervises-strong-model). Humans recovered 23% of the gap in a week; agents recovered 97% over 800 cumulative hours and ~$18K compute. Caveats: did not transfer to production scale, humans still chose the problem and the rubric.
- **Research judgment:** next-step decisions beat human choice 51% (Opus 4.5, Nov 2025) rising to 64% (Mythos, April 2026). On moments where the human's move was already strong, models were judged better only ~20% of the time, a check against judge bias.

**The human role narrows to goal-setting.** Humans supply goals, not methods. The large remaining gap is research taste. And Amdahl's law applies to organizations: once code generation accelerates, human review becomes the bottleneck. This is the same bottleneck Replit hit and routed around with agentic co-reviewers ([[self-driving-company-replit]]).

**Task horizons:** doubling roughly every 4 months (accelerating from every 7). Opus 3 did 4-minute tasks (March 2024), Sonnet 3.7 did 1.5 hours (March 2025), Opus 4.6 did 12 hours (March 2026), METR found Mythos Preview working "at least" 16 hours. SWE-bench saturated in two years; CORE-Bench in 15 months.

## Anthropic's Three Scenarios

1. **The trend stalls.** S-curves, supply-chain binding constraints (energy, chips, interconnect). Even frozen, the consequences are large (Project Glasswing's 10,000+ high/critical vulnerabilities; 100-person companies doing 1,000-person work). Anthropic explicitly does not believe this one: every measurable capability follows the same curve, and the curve hasn't bent.
2. **Compounding efficiency gains.** AI development substantially automated, humans set direction. 100-person companies doing the work of 100,000. Amdahl bottlenecks already visible. Explosion of ideas beyond capacity to pursue.
3. **Full RSI.** Systems design their own successors; pace set entirely by compute. Humans move to oversight of an expanding "virtual lab." Alignment is flagged as the least certain factor: misalignment could compound as models build successors.

Anthropic's policy position: a pause is good only if coordinated and verifiable. Unilateral pause accomplishes little. AI is easier to conceal than missile silos; the incentive to defect quietly is enormous. The Anthropic Institute will organize multi-stakeholder conversations and build the verification systems a credible slowdown would require.

## OpenAI's Position

- **Alignment blog "Hello World" (Dec 2025):** explicitly researching safe development of AI "capable of recursive self-improvement." Framed as a lab notebook. "No one should deploy superintelligent systems without being able to robustly align and control them."
- **Preparedness Framework v2 (April 2025):** AI self-improvement is a Tracked Category. High threshold: model impact equivalent to giving every OpenAI researcher a performant mid-career engineer assistant. Critical threshold: a superhuman research scientist agent (leading) or a generational model improvement in 1/5th the 2024 wall-clock time sustained for months (lagging). At Critical: halt development until Critical-standard safeguards are specified.
- **Deep Research (Feb 2025):** the research-loop infrastructure (gather, analyze, synthesize, report) as a declared step toward AGI that produces novel research. ResearcherBench (arXiv:2507.16280) confirms OpenAI and Gemini Deep Research lead on frontier scientific questions, framing this as "a meaningful step toward AI self-improvement."
- **RSI safety hiring (2026):** Preparedness team roles for loss-of-control mitigations, RSI-relevant training interventions, and RSI safety cases.
- **Altman (June 2026, leaked Slack):** OpenAI possibly "less than six months away from Recursive Self Improvement"; fast RSI "could weaken the push for a quick IPO" because "there might be good reasons to be a private company during that time." Internal milestones: automated intern-level by ~September 2026, automated AI researcher by ~March 2028.

## Comparison

| Metric | Anthropic (2026) | OpenAI (2025-2026) |
|--------|------------------|---------------------|
| Code authored by AI | >80% of merged code | Not disclosed |
| Engineer throughput | 8x 2024 code/day | Not disclosed |
| Research speedup | 52x training optimization | Not disclosed |
| Task horizon | 16+ hours (METR) | Not disclosed |
| Research judgment | 64% beats human | Not disclosed |
| RSI timeline | Years (implied) | <6 months (Altman) |
| Safety framework | ASL levels + verification for coordinated slowdown | Preparedness Framework v2, halt at Critical |

The asymmetry is the story: Anthropic is measuring and publicizing the curve; OpenAI is defining the tripwire and hiring the people who decide what to do when it trips. Both agree RSI is a when, not an if; both agree unilateral action is insufficient; both want to be the ones making the call.

## Open Questions

1. Can research taste be learned? Judgment is improving fast (51% to 64% in six months) but problem selection remains the human advantage.
2. S-curve or exponential? Anthropic says the curve hasn't bent; Altman says six months. Both can be right if the bend is just past the inflection.
3. Is verification of a coordinated slowdown possible? Both labs treat it as an open build problem, and AI development is harder to monitor than nuclear weapons.
4. What happens to the economy under Scenario 3? Neither lab has an answer.
5. Who decides? Multi-stakeholder conversation vs. staying private long enough to decide internally.

## Connections

- [[accelerando-compounding-acceleration]] — the Stross series found the recursive loop "visible but modest (~1.5-4x)"; Anthropic's 52x training-optimization number and 8x engineer throughput are the strongest evidence the modest multiplier is compounding faster than that reading suggested.
- [[karpathy-autoresearch]] — the autoresearch loop pattern instantiated at frontier-lab scale.
- [[agent-factory-production-system]] — the factory is now building the next factory.
- [[deployment-governance]] — Preparedness Framework halt conditions and ASL levels as the two governance instruments.
- [[self-driving-company-replit]] — the same Amdahl-bottleneck dynamic (review as constraint) observed at company scale.
