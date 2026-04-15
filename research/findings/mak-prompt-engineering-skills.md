---
title: "Mak's Prompt Engineering Skills: Analysis and Best Practices"
tags:
  - ai-agents
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/mak-prompt-engineering-skills.md
---

# Mak's Prompt Engineering Skills: Analysis and Best Practices
## Source: Prompt Engineering Skills PDF (Mak @ Synthweave)
## Analyzed: 2026-03-10

## What This Is

A set of three composable Claude Code skills by Mak (Synthweave team):
1. **prompt-creator**: Creates, improves, and optimizes system prompts
2. **prompt-tester**: Tests prompts for weaknesses, edge cases, adversarial inputs
3. **model-benchmarker**: Compares models on cost, quality, and capability for a given prompt

20 example use cases demonstrate individual and combined usage.

## Architecture: The Composable Skill Pipeline

The most important pattern here is NOT the individual skills. It's how they compose into a pipeline:

```
Create → Test → Fix → Re-test → Benchmark → Ship
```

This is a **self-improving loop** (Use Case #20):
1. prompt-creator builds a prompt
2. prompt-tester finds weaknesses
3. prompt-creator fixes based on test results
4. prompt-tester re-tests and compares before/after
5. Repeat until quality target met
6. model-benchmarker finds the cheapest model that passes

This is the pattern that matters. Each skill is a step. Together they form a workflow with feedback loops.

## Best Practices Extracted

### 1. Skills Should Be Composable, Not Monolithic
Each skill does ONE thing. prompt-creator doesn't test. prompt-tester doesn't create. model-benchmarker doesn't modify. But they compose naturally because their outputs are each other's inputs.

**For our skills**: Design skills with explicit input/output contracts so they can chain. A skill's output should be directly usable as another skill's input.

### 2. "Improvement Mode" as a First-Class Feature
prompt-creator has an explicit improvement mode (Use Case #2): take an existing prompt, identify weaknesses, rewrite it. This is different from creating from scratch.

**For our skills**: Skills should handle both creation and iteration. Not just "make a new thing" but "here's a thing that's broken, fix it." The iteration path should be as well-designed as the creation path.

### 3. Testing Before Shipping
prompt-tester runs diverse tests including edge cases and adversarial inputs BEFORE a prompt goes to production. This is the testing discipline the Anthropic skills guide talks about but rarely seen in practice.

**For our skills**: Every skill that produces output should have a corresponding test pattern. We should build testing into the workflow, not as an afterthought.

### 4. Cost-Aware Model Selection
model-benchmarker doesn't just find the "best" model. It finds the cheapest model that meets quality threshold (Use Case #12). This is production thinking.

**For our system**: When we run sub-agents, we should be asking "can this run on a cheaper model?" Not everything needs Opus. The benchmarker pattern could inform which model we assign to which sub-agent task.

### 5. Leaderboard-Driven Decisions
Several use cases start with "check the leaderboard" before selecting models or writing prompts. External data (model capabilities, benchmarks) informs the workflow.

**For our system**: We should maintain a reference of model strengths/weaknesses. When spawning sub-agents, match the model to the task based on known capabilities, not default to one model for everything.

### 6. Structured Output Awareness
Use Case #5: When using API-enforced JSON schemas (OpenRouter structured outputs), the prompt should skip output format instructions entirely and focus on reasoning. The schema handles structure; the prompt handles thinking.

**For our skills**: Be aware of the execution context. If the environment enforces structure, don't duplicate that in the prompt. This prevents conflicts between prompt instructions and API constraints.

### 7. User Input Templates
Use Case #6: Creating templates that guide users to provide the right input. The skill doesn't just work on the AI's output; it improves the human's input.

**For our skills**: Skills should include guidance for how to invoke them effectively. Not just "what the skill does" but "how to give it good input."

## Patterns to Adopt for Our Skill Development

### Pattern A: The Test-Fix Loop
Build testing into every skill we create. Not just "does it trigger correctly" (Anthropic's guide) but "does the output meet quality standards and handle edge cases?"

### Pattern B: Composable Skill Chains
Design skills with explicit contracts: what they accept, what they produce. Use Case #16 (full pipeline) shows the ideal: create → test → benchmark is a clean three-step workflow where each skill's output feeds the next.

### Pattern C: Before/After Comparison
Use Case #10 shows testing, fixing, then re-testing with comparison. This proves improvement. We should adopt this pattern: always show what changed and whether it got better.

### Pattern D: Cost Optimization as a Workflow Step
After quality is validated, optimize for cost. This should be a standard final step in any workflow that will run repeatedly in production.

### Pattern E: Self-Improving Loops
Use Case #20 is the most powerful: create → test → fix → re-test → repeat until passing → benchmark. This is an automated quality improvement loop. The LlamaIndex Workflows event pattern would be perfect for implementing this (each step emits events, loop until quality gate passes).

## Connection to Other Research

- **Anthropic Skills Guide**: Mak's skills follow the three-category model: prompt-creator is Category 1 (asset creation), prompt-tester is Category 2 (workflow automation), model-benchmarker is Category 2 with external tool integration.
- **LlamaIndex Workflows**: The self-improving loop (Use Case #20) maps directly to event-driven workflow with loop-until-condition pattern.
- **Loom**: The compose pattern (create → test → benchmark) is exactly the kind of multi-step workflow Loom should orchestrate. Each skill could be a Loom agent step.

## Action Items
- [ ] Study Mak's actual skill implementations when available
- [ ] Apply composable skill pattern to our next skill build
- [ ] Build test-fix loop into our skill development process
- [ ] Consider building a prompt-tester equivalent for our own skills
