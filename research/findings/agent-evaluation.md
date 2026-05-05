---
title: "Agent Evaluation: Beyond Benchmarks"
tags: [agent, evaluation, metrics, benchmark, measurement]
related: [[agentic-architecture]], [[agent-security]], [[progressive-disclosure]]
source: research/raw/agent-evaluation.md
---

# Agent Evaluation: Beyond Benchmarks

## The Measurement Problem

Agent evaluation is hard because agents do open-ended things in complex environments. Unit tests do not capture it. Human evaluation does not scale. Benchmarks get saturated and gamed. Every metric is a proxy for what we actually care about: did the agent do the right thing?

## Major Benchmarks

**SWE-bench**: Real GitHub issues from popular Python repos. Given an issue description and the repo, produce a patch that resolves it. Evaluated by running the repo's test suite. Top systems solve approximately 50-60% of SWE-bench Verified. Claude with extended thinking plus tools reaches approximately 50%+. Open-source agents (SWE-Agent, Moatless) achieve 20-35%.

**GAIA (General AI Assistants)**: 466 questions requiring multi-step reasoning, web browsing, file manipulation, and tool use. Three difficulty levels with unambiguous correct answers. Top systems achieve approximately 75% on Level 1, 50% on Level 2, 30% on Level 3. Humans score approximately 90% across all levels.

**WebArena / VisualWebArena**: Complete tasks in realistic web environments. Best agents achieve 30-40% completion rate, far from human level.

**HumanEval / MBPP / LiveCodeBench**: Code generation benchmarks. Largely saturated. Top models score greater than 90%. Not useful for differentiating agent capabilities.

**AgentBench**: Multi-environment benchmark covering OS interaction, database operations, web browsing, gaming, and more. Eight distinct environments.

## What Actually Matters for Production Agents

Benchmarks measure capability in controlled settings. For a real agent system, different metrics matter:

- **Task Completion Rate**: Did the agent accomplish what was asked? Binary for clear tasks, graded for ambiguous ones. The most important metric, and the hardest to measure automatically.
- **Cost Efficiency**: Tokens per task. Dollar cost per task. Are we using Opus when Sonnet would do?
- **Latency**: Time from request to useful output. Not just model latency but total pipeline time including tool calls, sub-agent spawning, file operations.
- **Error Rate and Recovery**: How often does the agent fail? When it fails, does it recover gracefully or compound the error?
- **Process Adherence**: Does the agent follow its own rules? Issues created, files committed, confirmations provided. This is measurable and correlates with output quality.
- **Autonomy Level**: How much can the agent do without human intervention? Over-autonomy leads to mistakes. Under-autonomy wastes human time.
- **User Satisfaction**: The ultimate metric. Does the human trust the agent? Does it reduce cognitive load?

## Recommendations

1. **Do not build a benchmark.** Our tasks are too varied and context-dependent. Benchmarks are for comparing systems, not improving one.
2. **Track process compliance automatically.** A weekly cron job that checks: issues created versus work done, commits with issue references, daily files written.
3. **Do monthly quality audits.** Sample tasks, review quality, log findings.
4. **Track cost.** Know how much each type of task costs in tokens and dollars. Optimize the expensive ones.
5. **Measure what changes behavior.** If a metric does not lead to action, stop tracking it.

## The Meta-Metric

The real test: does [[Ξ2T]] reach for the agent first when something needs doing? If yes, it is working. If he routes around it, something is wrong. Usage frequency is the ultimate evaluation.
