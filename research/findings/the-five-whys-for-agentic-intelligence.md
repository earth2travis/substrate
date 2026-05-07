---
title: "The Five Whys for Agentic Intelligence"
tags: [finding, root-cause, five-whys, learning, agent-ops]
related:
- agent-native-operations
- agent-factory-production-system
- kanban-doctrine
source: research/raw/the-five-whys-for-agentic-intelligence.md
ingested: 2026-05-07
---
# The Five Whys for Agentic Intelligence

Applying root cause analysis to agent failures: if an agent gives a bad answer, it's not because it's "dumb." It's because the Context Stack was incomplete or the Prompt was misaligned.

## Key Points

**The "Blameless" Agent.** Human error is always a process error. For agents, bad output means the process failed: incomplete context, misaligned prompt, or missing capability. Focus on the "why" of the process to build a system that gets smarter without getting defensive.

**From "What" to "Why."** Most agents focus on the output ("What"). The Five Whys forces focus on rationale ("Why"). Sivart should provide the Five Whys of strategic recommendations: why this path, why now, why these risks. Koda should document the Five Whys of every bug fix in the PR description, turning every fix into a lesson.

**The "Why-Tree" for Complex Systems.** Software failures are rarely linear; they are trees. Multiple causal chains converge on a common ancestor. For complex Agent Factory failures, use a Why-Tree: map multiple causal chains until finding the common root cause.

**The Five Whys as Learning Loop Trigger.** Every completed Five Whys analysis should trigger a learning event: update CONTRACT.md (rule broken), update TOOLS.md (tool misused), add a new skill (new fix found), update strategic memory (strategic gap found).

## Relevance

The difference between fixing a bug and fixing the factory. Embedding this practice ensures every failure is an investment in future success.

## Related

- [[agent-native-operations]] -- Executive layer and process discipline
- [[agent-factory-production-system]] -- Factory as learning system
- [[kanban-doctrine]] -- Continuous improvement via reflection
