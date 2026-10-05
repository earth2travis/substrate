Raw research file. Application of local search theory to agent eval improvement, produced 2026-10-05: source material for later synthesis, not a finished essay.

Series: `local-search.md`, `informed-search.md`, `search-depth-first-hill-climbing-beam.md`, `eval-hill-climbing.md`, `explore-exploit-ad-testing.md` (hill-climbing series, 2026-10-05).

Related Substrate nodes: [[agent-evaluation]] (benchmark catalog this file's noise math and Goodhart controls extend), [[better-harness-tweet]] (LangChain hill-climbing tweet stub this file supersedes with the full method), [[agent-harness-architecture]] (the harness is the state being hill-climbed), [[reference-free-evaluation]] (adjacent evaluation concept), [[harness-engineering]] (the loop this file operationalizes).

---

# Hill Climbing on Evals: Improving an Agent with Search

This file applies the local search ideas in `local-search.md` and `informed-search.md` to one task: making an AI agent better by repeated changes that are checked against evals.

---

## 1. The loop

"Hill climbing" is the name that agent teams use for this loop:

1. Run the evals on the current agent. Record the score. This is the **baseline**.
2. Read the failed transcripts. Put each failure into a category.
3. Make **one** change that targets one failure category.
4. Run the evals again.
5. If the score goes up and nothing breaks, keep the change. If not, revert it.
6. Go to step 2.

Cline used this loop on Terminal Bench (89 tasks). Their pass rate went from 47% to 57%. LangChain uses the same loop in its "Better-Harness" recipe.

---

## 2. Map from local search to eval work

| Local search term | Eval work term |
|---|---|
| State | One version of the agent: model, prompt, tools, harness settings. |
| Neighbor | The agent after one change. |
| Objective function | The eval score. |
| Hill-climbing step | Keep a change that increases the score. |
| Local maximum | Small changes no longer help. A larger change is necessary (new tool, new architecture, new model). |
| Plateau | The score does not move. Usually the evals are **saturated**: the agent passes everything it can. |
| Ridge | Two changes help only together (for example, a new tool and the prompt text that tells the agent to use it). Each change alone gives a lower score, so one-change-at-a-time search rejects both. |
| Random restart | Try a different approach from the start, not a small edit of the current one. |
| Noisy objective | The same agent gets a different score on each run. Some "uphill" steps are only noise. |

Two problems are specific to evals. Classic local search does not have them:

- **Noise.** The landscape height is measured with error.
- **Overfitting.** The eval landscape is only a copy of the real landscape (production). A hill on the copy can be flat or down on the real one.

---

## 3. Problem 1: noise

### Why it matters

An agent gives different results on the same task. Cline ran one unchanged configuration six times. The scores were 0.49, 0.43, 0.45, 0.44, 0.48, and 0.46. The range is 6 points with **no change** to the agent. A change that adds 3 points can be only noise.

### Calculate the error

For pass/fail scores, the standard error (SE) of a pass rate *p* on *n* tasks is:

```
SE = √( p(1 − p) / n )
```

The 95% confidence interval is p ± 1.96 × SE.

Example: 50 tasks, pass rate 50%.

```
SE = √(0.5 × 0.5 / 50) = 0.071 → ±7 points
95% interval = 50% ± 14 points
```

To compare two agent versions on **different** task sets, the SE of the difference is about √2 × SE = 10 points. The difference must be about 20 points to be significant.

### Ways to decrease noise

| Method | Effect |
|---|---|
| **Paired comparison.** Run both versions on the same tasks. Compare task by task. | Easy and hard tasks are the same for both versions, so most variation cancels. With a correlation of 0.5, the variance decreases by about 25%. |
| **More trials per task (K).** Run each task K times and average. | Going from K = 1 to K = 2 cuts variance by about 1/3. K = 4 cuts it by about 1/2. More than that gives little more. |
| **More tasks.** | SE decreases with √n. Four times the tasks halves the SE. |
| **Clustered errors.** If many tasks share one source (one account, one conversation), count them as a group. | Ignoring this can make the SE look 3 times smaller than it is. |
| **Do not lower the temperature** to make scores stable. | It hides the variation. It does not remove it. The result can be biased. |

Sources: Miller (2024); Cline.

### Two consistency measures

| Measure | Meaning | Use when |
|---|---|---|
| pass@k | At least 1 of *k* trials passes. | One success is enough (for example, the agent can retry). |
| pass^k | All *k* trials pass. | The agent must be reliable every time (for example, it acts on a live account). |

pass@k goes up as *k* increases. pass^k goes down. For an agent that acts on real money, pass^k is the more honest measure.

---

## 4. Problem 2: overfitting (Goodhart's law)

**Goodhart's law:** when a measure becomes a target, it stops being a good measure.

### How it happens

- **Specification gaming.** The agent finds a way to pass the grader without doing the task. LangChain: "agents are famous cheaters."
- **Prompt overfitting.** Someone adds an instruction that fixes one eval task. It does not help in production. It only uses context space. LangChain calls these instructions "a waste of tokens."
- **Brittle graders.** A grader that checks for one exact tool-call path rejects valid solutions. The agent is then trained toward that one path.
- **Saturation.** At 100% pass rate, the evals give no signal. Hamel Husain: a 70% pass rate "might indicate a more meaningful evaluation."

### Evidence on how large the risk is

Recht et al. (2019) built new test sets for CIFAR-10 and ImageNet with the original method. Accuracy dropped by 3 to 15% (CIFAR-10) and 11 to 14% (ImageNet). The **ranking** of models stayed almost the same. The authors found that the drop came from small differences between the old and new data, not from years of tuning on the old test set.

The lesson for agents: a score on one fixed set can be too high. But the order of "better" and "worse" versions is more trustworthy than the number itself.

### Controls

| Control | How it works |
|---|---|
| **Holdout set** | Split tasks into an optimization set and a holdout set. Make changes against the optimization set only. Check the holdout set before you keep a change. |
| **Regression set** | A set of core tasks that must always pass. A change that breaks one is rejected. |
| **Positive and negative cases** | Test that the agent acts when it must, **and** does not act when it must not. Testing only one side teaches only half the behavior. |
| **Outcome grading** | Grade the final state (what is true after the run), not what the agent says it did. |
| **Grader checks** | Read transcripts to find graders that reject good work or accept bad work. A 0% pass rate over many trials usually means a broken task, not a weak agent. |
| **Human review** | A person reads the change and some transcripts before the change is kept. |
| **Production check** | The final measure is real use, not the eval score. |
| **Eval refresh** | Remove saturated or outdated tasks. Add new tasks from new production failures. |

---

## 5. Problem 3: local maxima and plateaus

One-change-at-a-time search stops improving after some time. Signs:

- Each new change gives 0 to 2 points, inside the noise.
- The same failure categories come back.
- About 25% of Cline's failures needed a better **model**, not a better configuration. No prompt change can fix those.

Responses, from the search methods:

| Search method | Eval work action |
|---|---|
| Random restart | Try a different design for the failing area, not a small edit. |
| Larger step | Make a planned group of changes together (tool + prompt + grader). Test the group as one step. This crosses ridges. |
| New landscape | Change the model. Some failures need a stronger model. |
| Escape the plateau | Add harder tasks. A saturated eval cannot show progress. |

---

## 6. Error analysis drives the steps

A step is only as good as the failure diagnosis behind it. Hamel Husain's method:

1. **Open coding.** A domain expert reads traces and writes a free note on each problem.
2. **Axial coding.** Group the notes into a **failure taxonomy**. This is the most important step.
3. Read at least 30 traces before automation helps. Continue to about 100, or until new traces show no new failure types.
4. Use **pass/fail** grades, not 1 to 5 scales. Pass/fail forces clear decisions and gives more consistent labels.
5. If an LLM grades the work, check it against human labels. Measure:
   - True positive rate: of the real failures, how many the judge catches.
   - True negative rate: of the good outputs, how many the judge passes.
6. Give each LLM judge only the part of the trace it needs. Extra context makes the judge worse.

Teams in Husain's projects used 60 to 80% of development time on error analysis and evaluation.

Anthropic's advice to start: 20 to 50 tasks from real failures are enough. Early changes usually have large, clear effects.

---

## 7. Rules for agent evals

These rules come from the sections above:

1. **Run the same tasks on both versions and compare task by task.** Do not compare two scores from different task sets.
2. **Run each task 2 to 4 times.** Report the mean and the spread, not one run.
3. **Do not accept a gain smaller than the noise.** With about 50 tasks and one run each, a gain under about 15 to 20 points is not proof. More runs per task and more tasks make this number smaller.
4. **Use pass^k for actions on live accounts.** One good result in three is not enough when real money moves.
5. **Count tasks from one account or one conversation as one cluster.**
6. **Keep a holdout set.** Do not write prompt text that only fixes one eval task.
7. **Keep a regression set** of decisions that the agent must always get right.
8. **Grade decisions and outcomes, not tool-call paths.**
9. **Read transcripts before trusting a score change.**
10. **When steps stop helping, make a larger change** (new capability, new model) instead of more prompt edits.

---

## Sources

- [Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [LangChain, Better Harness: A Recipe for Harness Hill-Climbing with Evals](https://www.langchain.com/blog/better-harness-a-recipe-for-harness-hill-climbing-with-evals)
- [Cline, A practical guide to hill climbing](https://cline.bot/blog/a-practical-guide-to-hill-climbing)
- [Evan Miller, Adding Error Bars to Evals (arXiv 2411.00640)](https://arxiv.org/abs/2411.00640)
- [Hamel Husain, AI Evals FAQ](https://hamel.dev/blog/posts/evals-faq/)
- [Recht et al., Do ImageNet Classifiers Generalize to ImageNet? (ICML 2019)](http://proceedings.mlr.press/v97/recht19a/recht19a.pdf)
