# Big Lab Approaches to Agentic Auditing

## Anthropic

### Evaluation Philosophy

Anthropic's evaluation approach, documented in "Challenges in Evaluating AI Systems," reveals key principles:

- **Evaluations are extremely difficult to build** — even "simple" multiple-choice benchmarks (MMLU) have pitfalls: data contamination, formatting sensitivity (~5% accuracy swings from parentheses changes), inconsistent implementation across labs
- **Measuring what you think you're measuring** — BBQ (Bias Benchmark for QA) showed models scoring 0 bias, which seemed great until they realized the models weren't answering questions at all. The quantitative score masked complete failure.
- **Third-party evaluation frameworks** (BIG-bench, HELM) reveal engineering challenges — not plug-and-play, scaling issues, bugs in eval implementations
- **Crowdworker evaluations** are useful but inconsistent — worker quality varies, adversarial prompts from non-experts don't find the same vulnerabilities as experts
- **Expert red teaming** is gold standard but expensive and hard to scale

### Agent Design (SWE-bench work)

Anthropic's approach to building effective agents emphasizes:

- **Minimal scaffolding** — "give as much control as possible to the language model itself, and keep the scaffolding minimal"
- **Simple composable patterns** beat complex frameworks
- **Let the model use its own judgment** rather than hardcoding workflows
- **The agent = model + scaffolding** — both matter for evaluation

### Building Effective Agents

Key patterns from Anthropic's engineering blog:

1. **Prompt chaining** — decompose tasks, add programmatic checks ("gates") between steps
2. **Routing** — classify inputs, direct to specialized handlers
3. **Parallelization** — section tasks or vote across multiple attempts
4. **Orchestrator-workers** — dynamic task decomposition

**Relevance to self-auditing:** The "gate" pattern — programmatic checks between steps — maps directly to process audit checkpoints.

## OpenAI

### Practices for Governing Agentic AI Systems (White Paper)

OpenAI's framework defines:

- **Agentic AI systems** — pursue complex goals with limited direct supervision
- **Baseline responsibilities** for each party in the agentic lifecycle
- **Practices for safe and accountable operations**
- **Categories of indirect impacts** from wide-scale adoption

Key principle: **accountability requires auditability** — if an agent's operations can't be audited, they can't be governed.

## METR (Model Evaluation & Threat Research)

Formerly ARC Evals, METR focuses on evaluating dangerous autonomous capabilities:

- **Task-based evaluation** — concrete tasks at different difficulty levels
- **Controlled environments** with researchers in-the-loop
- **Elicitation gap research** — how much post-training enhancement might improve capabilities
- **Step-through methodology** — researchers walk through tasks with the model, seeing actual outputs

### Key Finding

Today's models can succeed at several component tasks (browsing, delegating to humans, making plans) but can't yet execute complete dangerous plans reliably. **The gap is closing, making systematic evaluation essential before models pose imminent risk.**

## Google DeepMind

- **Responsible AI practices** embedded in development lifecycle
- **Safety evaluations** against evolving threats
- **Multi-stage review** before model deployment

## Common Themes Across Labs

1. **Evaluations must be ongoing, not one-time** — capabilities change, evaluations must keep pace
2. **What you measure shapes what you optimize** — wrong metrics produce false confidence
3. **Human review remains essential** — automated evals miss what humans catch
4. **Process matters as much as capability** — the scaffolding around the model determines real-world performance
5. **Transparency and documentation** — audit trails are non-negotiable for accountability
6. **Test in controlled environments first** — before deploying, evaluate systematically

## Sources

- Anthropic, "Challenges in Evaluating AI Systems" (2023)
- Anthropic, "Building Effective AI Agents" (2024)
- Anthropic, "Claude SWE-Bench Performance" (2024)
- OpenAI, "Practices for Governing Agentic AI Systems" (2023)
- METR, "Autonomy Evaluation Resources" (2024)
- METR, "Update on ARC's Recent Eval Efforts" (2023)
