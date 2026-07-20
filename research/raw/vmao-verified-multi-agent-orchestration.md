# Verified Multi-Agent Orchestration (VMAO): Plan-Execute-Verify-Replan Framework

**Source:** arXiv:2603.11445v2 [cs.AI], March 15, 2026
**Authors:** Xing Zhang, Yanwei Cui, Guanghui Wang, Wei Qiu, Ziyuan Li, Fangwei Han, Yajing Huang, Hengzhi Qiu, Bing Zhu, Peiyang He
**Affiliations:** AWS Generative AI Innovation Center (1), HSBC (2)
**Venue:** ICLR 2026 Workshop on MALGAI
**DOI:** https://doi.org/10.48550/arXiv.2603.11445

---

## Abstract

VMAO is a framework that coordinates specialized LLM-based agents through a verification-driven iterative loop. A complex query is decomposed into a directed acyclic graph (DAG) of sub-questions, executed through domain-specific agents in parallel, verified for completeness via LLM-based evaluation, and adaptively replanned to address gaps. On 25 expert-curated market research queries, VMAO improves answer completeness from 3.1 to 4.2 and source quality from 2.6 to 4.1 (1-5 scale) compared to a single-agent baseline.

## The Problem

Production multi-agent systems face a coordination challenge: how to organize specialized agents for complex queries requiring heterogeneous sources and diverse expertise, while ensuring result quality without constant human oversight. Existing frameworks fall short:

- Debate-style approaches (Du et al., 2023) improve reasoning but lack structured task decomposition
- Role-playing frameworks (CAMEL, Li et al., 2023) enable collaboration but provide no mechanism for verifying completeness
- AutoGen (Wu et al., 2024) and MetaGPT (Hong et al., 2024) offer flexible interaction but lack principled quality verification and adaptive refinement

The gap: no verification at the orchestration level. Individual agent outputs can be verified, but nobody checks whether the collective results from multiple agents adequately address the original query, or triggers targeted replanning when gaps are detected.

## Core Contributions

1. **DAG-Based Query Decomposition and Execution:** Complex queries decomposed into sub-questions organized as a DAG with dependency-aware parallel execution and automatic context propagation from upstream results.

2. **Verification-Driven Adaptive Replanning:** An LLM-based verifier evaluates result completeness at the orchestration level, triggering adaptive replanning when gaps are identified. This provides a coordination signal decoupled from individual agent implementations.

3. **Configurable Stop Conditions:** Termination decisions based on completeness thresholds, confidence scores, and resource constraints, enabling explicit quality-cost tradeoffs.

## Architecture

Five phases operate in a loop: Plan, Execute, Verify, Replan, Synthesize.

### Phase 1: Plan

The QueryPlanner decomposes a complex query into sub-questions organized as a DAG. Each sub-question has:
- id (e.g., sq_001)
- question text
- assigned agent type
- dependencies (IDs of sub-questions that must complete first)
- priority (1-10, higher = more important)
- context_from_deps flag (whether to include dependency results in prompt)
- verification criteria

Planning rules from the prompt template:
- RAG First: always search internal knowledge base first or in parallel
- Maximize Parallelism: execute independent questions simultaneously
- Minimize Dependencies: only when results feed into other questions
- Be Specific: clear, answerable scope for each question

### Phase 2: Execute

The DAGExecutor orchestrates execution respecting dependencies and maximizing parallelism (default max_concurrent=3). It iteratively identifies ready questions (dependencies completed) and executes batches in parallel. Sub-questions with context_from_deps enabled get results from dependencies prepended to the query. Each execution wrapped with a configurable timeout (default 600s) and a tool call limiter.

### Phase 3: Verify

The ResultVerifier evaluates whether execution results adequately answer their sub-questions. For each result it produces:
- status (complete/partial/incomplete)
- completeness score (0-1)
- missing aspects
- contradictions
- recommendation (accept/retry/escalate)

Results already marked complete are reused to avoid redundant LLM calls.

### Phase 4: Replan

The AdaptiveReplanner determines corrective actions when verification identifies gaps:
- Retry sub-questions with low scores while preserving previous results
- Introduce new queries to address specific missing aspects
- Merge results from multiple attempts

Key feature: result preservation. Previous results stored and merged with retry attempts, enabling progressive refinement without losing earlier findings.

### Phase 5: Synthesize

For large result sets (>15K characters or 10+ results), hierarchical synthesis: group results by agent type, synthesize within each group to produce condensed summaries, then integrate group summaries into a coherent final answer with proper source attribution.

## Agent Taxonomy

Three functional tiers, 42 unique tools across eight MCP servers:

**Tier 1: Data Gathering**
- RAG (13 tools): semantic, keyword, hybrid retrieval; metadata filtering
- Web Search (4 tools): general and AI-powered search, news retrieval
- Financial (7 tools): stock quotes, technical indicators, fundamentals
- Competitor (11 tools): market positioning, benchmarks, competitor news

**Tier 2: Analysis**
- Analysis (20 tools): survey analytics, financial and competitor analysis
- Reasoning (24 tools): cross-domain reasoning with RAG, web, financial tools
- Raw Data (1 tool): Python execution (pandas, matplotlib)

**Tier 3: Output**
- Document (4 tools): report generation, tables, source citations
- Visualization (6 tools): chart generation, statistical summaries

## Stop Conditions

Five configurable conditions evaluated after each verification phase:

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| Ready for Synthesis | 80% complete | Sufficient sub-questions answered |
| High Confidence | 75% conf, 50% complete | High reliability despite partial coverage |
| Diminishing Returns | <5% improvement | Further iteration yields minimal gain |
| Token Budget | 1M tokens | Hard cost limit |
| Max Iterations | 3 iterations | Hard iteration limit |

Default config: max_iterations=3, token_budget=1M, ready_threshold=0.8, high_confidence=0.75, diminishing_returns=0.05, max_concurrent=3, agent_timeout=600s.

## Implementation

- LangGraph for workflow orchestration
- Strands Agent framework for agent execution
- AWS Bedrock for model hosting
- Claude Sonnet 4.5 primary, Claude Haiku 4.5 fallback
- Claude Opus 4.5 for verification and evaluation (independent quality signal)
- MCP (Model Context Protocol) for tool access via independent HTTP microservices
- Tool call limiters: max 10 consecutive same-tool calls, 50 total per agent
- Server-Sent Events for real-time observability streaming to frontend

## Evaluation

Dataset: 25 expert-curated market research queries across four categories:
- Performance Analysis (8 queries)
- Competitive Intelligence (7 queries)
- Financial Investigation (5 queries)
- Strategic Assessment (5 queries)

Query complexity ranges from 3-5 sub-questions (2-3 agent types) to 8-12 sub-questions (5+ agent types with multi-level dependencies). Each query consumes 500K-1.1M tokens and requires 10-20 minutes of execution.

### Baselines

- **Single-Agent:** One reasoning agent with access to all tools
- **Static Pipeline:** Predefined agent sequence (RAG, Web, Financial, Analysis, Synthesis) without verification or replanning
- **VMAO:** Full framework with dynamic decomposition, parallel execution, verification-driven replanning, and stop conditions

All use Claude Sonnet 4.5 for execution and the same tool set.

### Results

| Method | Completeness | Source Quality | Avg Tokens | Avg Time (s) |
|--------|-------------|----------------|------------|--------------|
| Single-Agent | 3.1 | 2.6 | 100K | 165 |
| Static Pipeline | 3.5 | 3.2 | 350K | 420 |
| VMAO (Ours) | 4.2 | 4.1 | 850K | 900 |

VMAO achieves +35% completeness and +58% source quality over Single-Agent. Token cost is 8.5x Single-Agent (850K vs 100K). Execution dominates at 61% of token usage, verification at 16%, synthesis at 8%, planning at 10%, replanning at 5%.

Largest gains on Strategic Assessment queries (+53% completeness), where initial decomposition inevitably misses relevant aspects. Smallest gains on Performance Analysis queries, where well-defined data sources mean single agents already locate most information.

Evaluation: LLM judge (Claude Opus 4.5) first scores each response using structured rubrics, then human domain experts review and adjust. Human reviewers adjusted fewer than 15% of LLM scores, typically by +/-0.5 points.

## Key Findings

**When verification helps most:** The largest gains from verification-driven replanning appear on open-ended, multi-dimensional queries where initial decomposition inevitably misses relevant aspects. Verification is most valuable when the query space is difficult to fully characterize upfront, precisely where static pipelines fail.

**Replanning patterns:** The majority of replanning actions are retries of incomplete sub-questions rather than introduction of entirely new ones. Agent execution variance (tool failures, insufficient search results) is a larger contributor to gaps than poor initial decomposition.

**Cost tradeoff:** 8.5x token cost relative to single agent. Most queries (>75%) terminate via resource-based conditions (diminishing returns, max iterations, or token budget), reflecting conservative thresholds prioritizing thoroughness over speed. Parameters are configurable for deployments requiring faster responses or lower costs.

## Limitations

1. LLM-based verification may miss subtle factual errors or hallucinations. It evaluates completeness, not accuracy. The verifier can confirm a claim is present and sourced but cannot independently establish its truth.

2. Poor query decomposition propagates errors downstream. If the planner misframes a sub-question, the verifier may accept a well-sourced but irrelevant answer.

3. 8.5x token cost may be prohibitive for latency-sensitive or cost-constrained settings.

4. All experiments use a single model family (Claude). Effectiveness with other LLM families untested.

5. 25 queries is a modest evaluation set without reported confidence intervals.

6. LLM judge and execution model belong to the same family (potential shared biases).

7. No component-level ablation: Static Pipeline baseline tests verification and replanning jointly.

## Connections to Related Work

The paper synthesizes three threads:
- Multi-agent coordination (AutoGen, CAMEL, MetaGPT, HuggingGPT)
- Planning and decomposition (Chain-of-Thought, Tree-of-Thoughts, Least-to-Most)
- Output quality (Self-Consistency, Self-Refine, Reflexion)

What is new: verification at the orchestration level, not the individual response level. The LLM-based verifier evaluates whether collective results from multiple agents satisfy the original query, and the replanner acts on that signal.

Open-source alternative to closed commercial systems (Perplexity, OpenAI deep research) with explicit, configurable coordination mechanisms.

## Future Directions

- Learning-based stop conditions trained on execution traces
- Component-level ablation studies to isolate each framework element's contribution
- Evaluation with diverse model families
- Human-in-the-loop verification for high-stakes queries
- Transfer to domains like legal discovery or scientific literature review

## Prompt Templates (Appendix A)

Four core prompts provided:

1. **Planning Prompt:** Decomposes complex queries into sub-questions with fields (id, question, agent type, dependencies, priority, context_from_deps, verification criteria). Rules: RAG first, maximize parallelism, minimize dependencies, be specific.

2. **Verification Prompt:** Evaluates completeness, evidence quality, metadata, specificity, contradictions. Outputs status, completeness score, missing aspects, confidence, recommendation.

3. **Replanning Prompt:** Determines next actions. Completeness >0.8 proceeds to synthesis. Incomplete results add ALL to retry list. Completeness 0.5-0.8 adds new sub-questions. Contradictions add queries targeting different sources. Max iterations returns empty lists.

4. **Synthesis Prompt:** Produces executive summary, key findings with source citations, analysis connecting insights, conclusions with confidence level and limitations.

## Configuration Parameters (Appendix B)

| Parameter | Default | Description |
|-----------|---------|-------------|
| max_iterations | 3 | Maximum replanning iterations |
| token_budget | 1M | Maximum tokens before stopping |
| ready_threshold | 0.8 | Completeness ratio for synthesis |
| high_confidence | 0.75 | Confidence threshold for early stop |
| diminishing_returns | 0.05 | Minimum improvement to continue |
| max_concurrent | 3 | Parallel agent executions |
| agent_timeout | 600s | Per-agent timeout |
