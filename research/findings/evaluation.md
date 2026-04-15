---
title: Agent Evaluation
tags:
  - ai-agents
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/evaluation.md
---

# Agent Evaluation

## The Measurement Problem

Agent evaluation is hard because agents do open-ended things in complex environments. Unit tests don't capture it. Human evaluation doesn't scale. Benchmarks get saturated and gamed. Every metric is a proxy for what we actually care about: "did the agent do the right thing?"

## Major Benchmarks

### SWE-bench

**What:** Real GitHub issues from popular Python repos. Given an issue description and the repo, produce a patch that resolves it. Evaluated by running the repo's test suite.

**Versions:**
- SWE-bench (full): 2,294 tasks. Noisy, includes easy and hard.
- SWE-bench Lite: 300 curated tasks. Cleaner signal.
- SWE-bench Verified: 500 tasks verified by human developers. Current gold standard.

**State of the art (early 2025):**
- Top systems solve ~50-60% of SWE-bench Verified
- Claude with extended thinking + tools: ~50%+ on Verified
- Open-source agents (SWE-Agent, Moatless): 20-35%

**What it measures well:** Real-world software engineering capability. Can the agent understand a codebase, localize a bug, and write a correct fix?

**What it misses:** Speed, cost, code quality beyond "tests pass," communication with humans, incremental work over multiple sessions.

### GAIA (General AI Assistants)

**What:** 466 questions requiring multi-step reasoning, web browsing, file manipulation, and tool use. Three difficulty levels. Questions have unambiguous correct answers.

**Examples:** "What was the GDP per capita of the country that won the 2022 FIFA World Cup?" (requires search, data lookup, calculation)

**State of the art:** Top systems ~75% on Level 1, ~50% on Level 2, ~30% on Level 3. Humans score ~90% across all levels.

**What it measures well:** General tool-use competence, multi-step reasoning, information synthesis.

**What it misses:** Creative tasks, subjective quality, long-running tasks, real-world messiness.

### WebArena / VisualWebArena

**What:** Complete tasks in realistic web environments (shopping sites, forums, GitLab, maps). Measured by task completion rate.

**What it measures well:** UI understanding, navigation, form filling, web-based workflows.

**Current performance:** ~30-40% for best agents. Far from human-level.

### HumanEval / MBPP / LiveCodeBench

**What:** Code generation benchmarks. Given a function signature and docstring, produce correct code.

**Status:** Largely saturated. Top models score >90%. Not useful for differentiating agent capabilities.

### AgentBench

**What:** Multi-environment benchmark covering OS interaction, database operations, web browsing, gaming, and more. Eight distinct environments.

**What it measures well:** Breadth of capability across different domains.

## What Actually Matters (Beyond Benchmarks)

Benchmarks measure capability in controlled settings. For a real agent system like ours, different metrics matter:

### Task Completion Rate
Did the agent accomplish what was asked? Binary for clear tasks, graded for ambiguous ones. The most important metric, and the hardest to measure automatically.

### Cost Efficiency
Tokens per task. Dollar cost per task. Are we using Opus when Sonnet would do? Are sub-agents burning tokens on low-value work?

### Latency
Time from request to useful output. Not just model latency but total pipeline time including tool calls, sub-agent spawning, file operations.

### Error Rate and Recovery
How often does the agent fail? When it fails, does it recover gracefully or compound the error? Does it know when to ask for help?

### Process Adherence
Does the agent follow its own rules? (Issues created, files committed, confirmations provided.) This is measurable and correlates with output quality.

### Autonomy Level
How much can the agent do without human intervention? This is a spectrum, and the right answer isn't "everything." Over-autonomy leads to mistakes. Under-autonomy wastes human time.

### User Satisfaction
The ultimate metric. Does the human trust the agent? Does it reduce cognitive load? Is the interaction pleasant? Hard to quantify but impossible to ignore.

## How to Measure Our Agent

### Automated Metrics (Can Implement Now)
1. **Process compliance score:** % of tasks with issues, commits, confirmations. Checkable from git log and issue tracker.
2. **Sub-agent success rate:** % of sub-agents that complete their task vs. fail/timeout.
3. **Token efficiency:** Tokens per task category. Track over time.
4. **Memory hygiene:** Are daily files being written? Is MEMORY.md being updated? Measurable from file timestamps.

### Manual Metrics (Periodic Review)
1. **Task quality audit:** Sample 10 completed tasks per week. Were they done well?
2. **Decision quality:** Review logged decisions. Were they good ones?
3. **Communication quality:** Was the agent's communication clear, concise, and helpful?

### The Meta-Metric
The real test: **Does [[Ξ2T]] reach for the agent first when something needs doing?** If yes, it's working. If he routes around it, something's wrong. Usage frequency is the ultimate evaluation.

## Recommendations

1. **Don't build a benchmark.** Our tasks are too varied and context-dependent. Benchmarks are for comparing systems, not improving one.

2. **Track process compliance automatically.** This is low-hanging fruit. A weekly cron job that checks: issues created vs. work done, commits with issue references, daily files written.

3. **Do monthly quality audits.** Sample tasks, review quality, log findings. This is the audit guide already, so just do it consistently.

4. **Track cost.** Know how much each type of task costs in tokens/dollars. Optimize the expensive ones.

5. **Measure what changes behavior.** If a metric doesn't lead to action, stop tracking it. Every metric should answer: "what would I do differently if this number changed?"
