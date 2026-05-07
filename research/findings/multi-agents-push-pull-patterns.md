---
title: "Multi-Agents: The Push, The Pull, and The Practical Patterns"
tags: [finding, multi-agent, context-engineering, smart-friend, delegation]
related: [[agent-native-operations]], [[agent-memory]], [[context-stack]]
source: research/raw/multi-agents-push-pull-patterns.md
ingested: 2026-05-07
---

# Multi-Agents: The Push, The Pull, and The Practical Patterns

Walden Yan's analysis of multi-agent evolution driven by a "push" from increased agent usage (management bottlenecks) and a "pull" from rising costs (needing cheaper, smarter architectures).

## Key Points

**The "Clean-Context" Review Loop.** Review agents work best when they do not share context with the coding agent. Shared context leads to "Context Rot" (diminished attention at long context lengths). A clean-context reviewer is forced to reason backward from the implementation, often catching logic errors and security vulnerabilities the original agent missed due to instruction bias or context overload. The primary agent uses its broader context to filter reviewer feedback, preventing infinite loops.

**The "Smart Friend" Pattern.** Smaller/cheaper models call out to larger/expensive "Smart Friends" for tricky sub-tasks. The challenge: getting a "dumber" primary model to know when to escalate and what to ask. The fix: the primary shares a fork of its full context and asks broad questions ("What should I do?"). The Smart Friend should be "over-scoped," looking beyond the immediate question to suggest important guidance based on the agent's trajectory. Cross-frontier routing shifts from difficulty escalation to capability routing (Claude for debugging, GPT for visual reasoning).

**Higher-Level Delegation (Map-Reduce-and-Manage).** For large scopes spanning multiple PRs, a Manager agent breaks work into pieces for Child agents. The friction: managers default to being overly prescriptive because they lack deep codebase context. The solution: dedicated context engineering so children surface discoveries that should change siblings' work. The practical shape is Map-Reduce-and-Manage, not unstructured swarms.

**The core through-line.** "Writes stay single-threaded; additional agents contribute intelligence." Whether clean-context reviewer, smart friend, or manager, robust systems avoid parallel writes. Multiple agents inject intelligence at every stage while keeping final decision-making cohesive and single-threaded.

## Relevance

These patterns are directly applicable to Substrate backfill batch processing: clean-context review for quality, smart-friend routing for cost optimization, and Map-Reduce for parallel ingestion.

## Related

- [[agent-native-operations]] -- Executive layer and smart-friend routing
- [[agent-memory]] -- Context management to prevent Context Rot
- [[context-stack]] -- Where agent context is encoded
