---
title: "Hill Climbing on Evals: Improving an Agent with Search"
tags: [finding, evaluation, hill-climbing, local-search, agent-improvement, noise, goodhart]
related:
- local-search
- informed-search
- agent-evaluation
- harness-engineering
- reference-free-evaluation
source: research/raw/eval-hill-climbing.md
ingested: 2026-10-05
---
# Hill Climbing on Evals

## Key Points

**The loop is local search with evals as the objective function.** Run evals, record the baseline, read failed transcripts, categorize failures, make one change targeting one category, re-run, keep or revert. Cline used this on Terminal Bench (89 tasks) and went from 47% to 57%. LangChain's "Better Harness" recipe is the same loop. The state is the agent version (model, prompt, tools, harness settings); the neighbor is one change; the objective is the eval score.

**Noise is the first enemy.** Cline ran one unchanged configuration six times: scores were 0.49, 0.43, 0.45, 0.44, 0.48, 0.46. Six points of range with zero change. A 3-point gain can be pure noise. For pass/fail scores, SE = √(p(1−p)/n). On 50 tasks at 50% pass rate, the 95% confidence interval is ±14 points. Two versions on different task sets need ~20 points of difference to be significant. Do not lower temperature to hide variance; it biases the result.

**Controls that actually reduce noise.** Paired comparison (same tasks, both versions) cancels most variance. K = 2–4 trials per task cuts variance by a third to a half. More tasks help at √n. Cluster tasks from one account or conversation; ignoring clustering can make SE look 3x smaller than it is. Use pass@k when one success is enough, pass^k when reliability is mandatory (live money, production accounts).

**Goodhart's law is the second enemy.** When a measure becomes a target, it stops being a good measure. Failure modes: specification gaming (the agent cheats the grader), prompt overfitting (instructions that fix one eval task and waste tokens), brittle graders (one exact tool-call path), saturation (100% pass rate = no signal). Recht et al. (2019) rebuilt CIFAR-10 and ImageNet test sets: accuracy dropped 3–15%, but rankings held. The lesson: absolute scores on a fixed set are inflated; relative rankings are more trustworthy.

**The eight Goodhart controls.** Holdout set (optimize on one split, check on another). Regression set (core tasks that must always pass). Positive and negative cases (test both action and restraint). Outcome grading (grade the final state, not the transcript). Grader checks (read transcripts for graders that reject good work). Human review (a person reads the change and traces). Production check (real use is the final measure). Eval refresh (remove saturated tasks, add new ones from production failures).

**Local maxima are the third enemy.** Signs: each new change gives 0–2 points (inside noise); the same failure categories recur; ~25% of Cline's failures needed a better model, not a better config. Responses: random restart (different design, not a small edit), larger step (planned group of changes together: tool + prompt + grader), new landscape (change the model), escape the plateau (add harder tasks).

**Error analysis drives the steps.** Husain's method: open coding (free notes on each problem), axial coding (group into a failure taxonomy), read 30+ traces before automation, continue to ~100 or until no new types. Use pass/fail, not 1–5 scales. If an LLM grades, measure true positive and true negative rates against human labels. Give the judge only the context it needs. Teams in Husain's projects spent 60–80% of development time on error analysis and evaluation.

**The ten rules for agent evals.** Same tasks on both versions, compare task by task. 2–4 trials per task, report mean and spread. No gain smaller than the noise. pass^k for live accounts. Cluster tasks from one source. Keep a holdout. Keep a regression set. Grade decisions and outcomes, not tool-call paths. Read transcripts before trusting a score change. When steps stop helping, make a larger change.

## Relevance

This is the operational manual that turns [[local-search]] and [[informed-search]] theory into a daily practice. It extends [[agent-evaluation]]'s benchmark catalog with the statistics of improvement: how to know a change worked, how to avoid fooling yourself, and when to stop tuning prompts and change the model. The noise math (SE = √(p(1−p)/n)) is the same math that [[explore-exploit-ad-testing]] applies to ad testing; the two files are sibling applications of the same statistical spine. The Goodhart controls connect to [[harness-engineering]]'s feedback loops and [[reference-free-evaluation]]'s confidence grading: the holdout set is the harness's version of reference-free validation. The ridge-crossing advice (planned group changes) is the eval version of [[kaizen]] hitting a wall and needing a step change, not another small edit.

## Related

- [[local-search]] — theory: the landscape being climbed
- [[informed-search]] — theory: ridge failure modes in high dimensions
- [[agent-evaluation]] — the benchmark catalog this file's noise math extends
- [[explore-exploit-ad-testing]] — sibling: same statistics applied to media buying
- [[harness-engineering]] — the feedback loop that runs the climb
- [[reference-free-evaluation]] — confidence grading as a holdout control
- [[kaizen]] — continuous improvement as hill climbing; step changes as ridge crossing
