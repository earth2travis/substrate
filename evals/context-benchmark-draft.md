---
title: "Context Benchmark: Measuring 'Company Understanding'"
date: 2026-04-20
tags: [evals, benchmark, synthesis, testing]
---

# Context Benchmark: Measuring "Company Understanding"

## The Goal

To move beyond simple "retrieval" metrics and test whether the system has **Synthesized Understanding** of the partnership and The Agent Factory.

## The "Ground Truth" Questions

1. **Identity & Roles:** Who is responsible for the "Alchemist" identity, and how does it differ from the "Operator"?
2. **Current Priorities:** What are the top 3 strategic initiatives for The Agent Factory this month?
3. **Conflict Resolution:** If `research/raw/A.md` says "X" and `insights/concepts/B.md` says "Y", which one represents our current "Ground Truth" and why?
4. **Entity Resolution:** What are the different names/aliases we use for our shared knowledge repo, and which one is the current "official" name?
5. **Temporal Awareness:** What was the most significant architectural decision we made in the last 7 days?
6. **Tooling Status:** Which Cloudflare primitives are currently "Active" in our stack vs. "Planned"?
7. **Protocol Knowledge:** What are the two layers of the Autogenesis Protocol (AGP) and what is the function of each?
8. **Decision Provenance:** Where can we find the "Decision Record" for moving from "Brain-two" to "The Substrate"?
9. **Signal Hierarchy:** In our current system, which source has higher authority: a `specs/` file or a `memory/` daily note?
10. **The "Moat":** According to our recent research, what is the primary "moat" we are building through the Substrate?

## Evaluation Metrics

* **Accuracy:** Is the answer factually correct based on the Substrate?
* **Synthesis:** Did the agent combine multiple sources to form the answer?
* **Provenance:** Did the agent cite the specific files used to reach the conclusion?
* **Conflict Awareness:** Did the agent identify and resolve any contradictory information?

## Next Steps

1. **Baseline Test:** I will answer these 10 questions using my current context.
2. **Gap Analysis:** We identify where I fail or lack confidence.
3. **Systematic Fix:** We build the specific AGP/Cloudflare component needed to fix that gap.
