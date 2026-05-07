---
title: "The Five Whys: Compact Root Cause Analysis"
tags: [root-cause-analysis, five-whys, toyota, lean, methodology]
related: [[5-whys]], [[kaizen-and-continuous-improvement]], [[fishbone-diagrams]]
source: research/raw/the-five-whys-root-cause-analysis.md
---

# The Five Whys: Compact Root Cause Analysis

The Five Whys is a root cause analysis technique developed by Sakichi Toyoda in the 1930s and refined by Taiichi Ohno as a cornerstone of the Toyota Production System. The method involves asking "Why?" repeatedly — typically five times — to move past symptoms and identify the underlying systemic flaw.

## The Process

1. Define the problem clearly
2. Ask "Why did this happen?"
3. Take the answer and ask "Why?" again
4. Continue until reaching a cause that, if fixed, prevents recurrence

**Example chain:**
- Problem: production server crashed
- Why? Memory usage hit 100%
- Why? Memory leak in the new feature
- Why? It wasn't caught in code review
- Why? No automated memory testing in CI/CD
- Why? Prioritized feature speed over infrastructure reliability

**Root cause:** cultural/prioritization problem, not just a code problem.
**Countermeasure:** update CI/CD pipeline with memory profiling; adjust schedule for tech debt.

## Key Principles

- **Blame the process, not the person:** find the process failure that allowed a human mistake
- **Fact-based, not assumption-based:** every answer must be verifiable
- **Stop at the root:** once the cause would prevent recurrence, stop. Sometimes 3 whys; sometimes 8

## Limitations

- **Linear thinking:** assumes one path; complex failures often have multiple interconnected "whys"
- **Stopping too early:** stopping at "the developer made a mistake" fixes nothing. Must reach the systemic layer.

## Relevance to the Agent Factory

The Five Whys is the intellectual engine of self-reflection:
- When a strategic insight fails, ask whether it was lack of context, bad prompt, or limitation in the knowledge base
- When a build fails, determine whether it was a flaky test or a gap in the contract or tooling
- Every major failure should result in a Five Whys entry in the shared knowledge graph
