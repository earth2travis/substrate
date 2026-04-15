---
title: "The Five Whys: Root Cause Analysis"
tags:
  - ai-agents
  - knowledge-management
  - lean-manufacturing
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/the-five-whys-root-cause-analysis.md
---

# The Five Whys: Root Cause Analysis

**Researched:** 2026-04-12
**Topic:** Five Whys, Toyota Production System, Root Cause Analysis

---

## I. Overview
The **Five Whys** is a simple yet powerful root cause analysis technique developed by **Sakichi Toyoda** in the 1930s. It was later refined by **Taiichi Ohno** and became a cornerstone of the Toyota Production System (TPS). The method involves asking "Why?" repeatedly—typically five times—to move past symptoms and identify the underlying systemic flaw.

## II. The Process
The beauty of the Five Whys is its simplicity. It requires no complex math or tools, just a commitment to factual inquiry.

1.  **Define the Problem:** Clearly state the issue (e.g., "The production server crashed").
2.  **Ask Why #1:** "Why did it crash?" (Answer: "Because memory usage hit 100%").
3.  **Ask Why #2:** "Why did memory hit 100%?" (Answer: "Because of a memory leak in the new feature").
4.  **Ask Why #3:** "Why was there a memory leak?" (Answer: "Because it wasn't caught in code review").
5.  **Ask Why #4:** "Why wasn't it caught?" (Answer: "Because we don't have automated memory testing in CI/CD").
6.  **Ask Why #5:** "Why don't we have automated testing?" (Answer: "Because we prioritized feature speed over infrastructure reliability").

**The Root Cause:** We have a cultural or prioritization problem, not just a code problem.
**The Countermeasure:** Update the CI/CD pipeline to include memory profiling and adjust our "Heijunka" schedule to include tech debt time.

## III. Key Principles
*   **Blame the Process, Not the Person:** The goal is to find the "process failure" that allowed a human to make a mistake. If a developer forgets a semicolon, the "Why" isn't "they were careless"; it's "why doesn't the linter catch missing semicolons?"
*   **Fact-Based, Not Assumption-Based:** Every answer must be verifiable. You can't just guess; you must look at the logs, the code, or the data.
*   **Stop at the Root:** Once you reach a cause that, if fixed, would prevent the problem from ever recurring, you stop. Sometimes it's 3 Whys; sometimes it's 8.

## IV. Limitations
*   **Linear Thinking:** It assumes one linear path. Complex software failures often have multiple, interconnected "whys" (a "why-tree" instead of a "why-line").
*   **Stopping Too Early:** If you stop at "the developer made a mistake," you haven't fixed anything. You must reach the **systemic** layer.

---

## V. Relevance to the Agent Factory
The Five Whys is the **intellectual engine** of our "Self-Reflection" skills.
1.  **Hermes (Sivart):** When I fail to provide a good strategic insight, I must use the Five Whys to determine if the failure was due to a lack of context, a bad prompt, or a limitation in my `research/` files.
2.  **OpenClaw (Koda):** When a build fails or a PR is rejected, Koda must use the Five Whys to determine if the failure was a "flaky test" or a fundamental gap in our `CONTRACT.md` or tooling.
3.  **The Brain-Two Log:** Every major failure in our system should result in a "Five Whys" entry in our shared knowledge graph, ensuring we never make the same mistake twice.

---

## VI. Sources
- Ohno, Taiichi. *Toyota Production System: Beyond Large-Scale Production.*
- Atlassian: "The 5 Whys Method."
- Salesforce Engineering: "How, Not Why: An Alternative to the 5 Whys for Post-Mortems."