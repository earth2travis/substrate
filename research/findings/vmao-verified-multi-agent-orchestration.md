---
title: "VMAO: Verified Multi-Agent Orchestration (Plan-Execute-Verify-Replan)"
tags: [finding, vmao, multi-agent, orchestration, verification, dag, planning, evaluation, aws, research-paper]
related:
- multi-agent-coordination-patterns
- loops-as-orchestration-primitive
- agent-orchestrator-pattern
- subagent-architecture
- feedback-loop-discipline
source: research/raw/vmao-verified-multi-agent-orchestration.md
ingested: 2026-07-21
---
# VMAO: Verified Multi-Agent Orchestration (Plan-Execute-Verify-Replan)

## Summary

AWS Generative AI Innovation Center + HSBC, arXiv:2603.11445v2 (March 2026), ICLR 2026 MALGAI workshop. VMAO coordinates specialized LLM agents through a verification-driven iterative loop: a complex query decomposes into a DAG of sub-questions, executes through domain agents in parallel, is verified for completeness at the orchestration level by an LLM judge, and adaptively replans to fill gaps. On 25 expert-curated market research queries, VMAO lifts answer completeness from 3.1 to 4.2 (+35%) and source quality from 2.6 to 4.1 (+58%) over a single-agent baseline, at 8.5x the token cost (850K vs 100K per query) and 10-20 minutes of execution. The novel contribution is not any individual phase but the placement of the verifier: it evaluates whether the collective output of all agents adequately addresses the original query, producing a coordination signal decoupled from individual agent implementations.

## The Gap It Fills

Existing multi-agent frameworks verify at the wrong altitude. Debate-style approaches improve reasoning without structured decomposition. Role-playing frameworks (CAMEL) collaborate without completeness checks. AutoGen and MetaGPT offer flexible interaction without principled quality verification or adaptive refinement. Individual agent outputs can be checked; nobody was checking whether the ensemble answered the question. VMAO's verifier sits at the orchestration level and its verdict (complete/partial/incomplete, completeness score, missing aspects, contradictions, accept/retry/escalate) drives the loop.

## Architecture: Five Phases in a Loop

1. **Plan.** QueryPlanner decomposes the query into a DAG of sub-questions, each with id, question text, assigned agent type, dependencies, priority, context_from_deps flag, and verification criteria. Prompt rules: RAG first, maximize parallelism, minimize dependencies, be specific.
2. **Execute.** DAGExecutor runs dependency-aware parallel batches (default max_concurrent=3), prepends upstream results where flagged, wraps each execution in a 600s timeout and tool-call limiters (max 10 consecutive same-tool, 50 total per agent).
3. **Verify.** ResultVerifier scores each sub-question result for completeness with structured output; already-complete results are reused to avoid redundant LLM calls.
4. **Replan.** AdaptiveReplanner retries low-scoring sub-questions, introduces new queries for missing aspects, and merges results across attempts. Key feature: result preservation, so retries refine progressively rather than starting over.
5. **Synthesize.** Hierarchical for large result sets (>15K chars or 10+ results): group by agent type, condense within groups, integrate with source attribution.

**Agent taxonomy:** three tiers (data gathering, analysis, output), 42 tools across eight MCP servers. RAG alone has 13 tools; reasoning has 24.

**Stop conditions** (evaluated after each verification): 80% completeness → synthesize; 75% confidence + 50% complete → early stop; <5% improvement → diminishing returns; 1M token budget; max 3 iterations. Over 75% of queries terminate on resource-based conditions, a sign the defaults prioritize thoroughness over speed.

**Stack:** LangGraph orchestration, Strands agents, Bedrock hosting, Claude Sonnet 4.5 execution with Haiku 4.5 fallback, Claude Opus 4.5 as the independent verifier, MCP for tools, SSE for observability.

## Results and What They Mean

| Method | Completeness | Source Quality | Tokens | Time |
|--------|-------------|----------------|--------|------|
| Single-Agent | 3.1 | 2.6 | 100K | 165s |
| Static Pipeline | 3.5 | 3.2 | 350K | 420s |
| VMAO | 4.2 | 4.1 | 850K | 900s |

Three findings carry the weight:

- **Verification pays most where decomposition is hardest.** Largest gains on Strategic Assessment queries (+53% completeness), where the initial plan inevitably misses aspects. Smallest on Performance Analysis, where well-defined sources mean single agents already find most of it. Verification is a hedge against uncharacterizable query spaces.
- **Execution variance beats planning failure.** Most replanning actions are retries of incomplete sub-questions, not new ones. Tool failures and thin search results cause more gaps than poor decomposition. Implication: invest in execution robustness before planner sophistication.
- **Quality is bought with tokens.** 8.5x cost over single-agent. Execution is 61% of spend, verification 16%, planning 10%, synthesis 8%, replanning 5%.

Evaluation caveat the paper is honest about: the LLM judge (Opus 4.5) and the execution models are the same family, a shared-bias risk; human experts adjusted fewer than 15% of LLM scores, typically by ±0.5. Also: 25 queries, no confidence intervals, no component-level ablation (the static pipeline baseline tests verification and replanning jointly), single model family.

## Why It Matters for Substrate

VMAO is the formalized, evaluated version of the orchestration loop already present across the wiki: plan → execute → verify → replan is [[feedback-loop-discipline]] at the multi-agent level, and the orchestration-level verifier is the missing piece named in [[multi-agent-coordination-patterns]]. The practical imports:

- **Verify at the orchestration boundary, not just per-agent.** A swarm of individually correct agents can collectively miss the question.
- **Make stop conditions explicit and configurable.** The quality-cost tradeoff should be a parameter surface, not a vibe. VMAO's five conditions are a usable template.
- **Preserve results across replans.** Retry-with-merge beats retry-from-scratch.
- **Use a stronger model for verification than execution** (Opus verifies, Sonnet executes) as a cheap independence signal.
- **Expect the gains on open-ended, multi-dimensional queries** (research, strategy, diligence) and not on well-specified retrieval. This maps directly to when deep-research-style orchestration beats a single strong agent, connecting to the Deep Research systems in [[rsi-anthropic-openai-deep-dive]] and the loop-based swarms in [[self-driving-company-replit]].

## Limitations (as stated)

LLM verification checks completeness, not truth; poor decomposition propagates (the verifier can accept a well-sourced irrelevant answer); 8.5x token cost; single model family untested elsewhere; modest eval set; judge/executor family overlap; no ablation isolating verification from replanning.

## Connections

- [[multi-agent-coordination-patterns]] — VMAO adds the verification-and-replan layer the pattern catalog lacked.
- [[agent-orchestrator-pattern]] — the QueryPlanner/DAGExecutor split is the orchestrator pattern with a verifier attached.
- [[loops-as-orchestration-primitive]] — the outer plan-execute-verify-replan cycle is a loop with an explicit completeness gate and five stop conditions.
- [[subagent-architecture]] — DAG-delegated subagents with context propagation from upstream results.
- [[feedback-loop-discipline]] — verification-driven iteration as disciplined feedback, with measured diminishing returns.
