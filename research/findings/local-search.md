---
title: "Local Search: Hill Climbing, Simulated Annealing, Local Beam, Genetic Algorithms"
tags: [finding, search, optimization, ai, algorithms, local-search]
related:
- agent-evaluation
- harness-engineering
- lean-doctrine
- kaizen
source: research/raw/local-search.md
ingested: 2026-10-05
---
# Local Search

## Key Points

**Local search finds goal states, not paths.** Classic search (depth-first, breadth-first, A*) returns a path. Local search returns a configuration that satisfies constraints or optimizes an objective. It keeps only the current state (or a small set), uses almost no memory, and works on very large or continuous spaces. The trade: it gives up completeness and path optimality for tractability.

**The landscape metaphor is the diagnostic frame.** Picture every state as a point on a surface; the objective function is height. Features map to failure modes: global maximum (the goal), local maximum (stuck), plateau (no direction), shoulder (slow progress), ridge (axis-aligned moves fail, diagonal needed). Knowing which feature you are on determines the remedy.

**Hill climbing is the baseline and the cautionary tale.** Always move to the best neighbor. Fast, low-memory, and **not complete**: it stops at local maxima, plateaus, and ridges. Variants exist to patch each failure: stochastic hill climbing (random uphill moves) for plateaus, sideways moves for shoulders, random restarts for global coverage. Random-restart hill climbing is complete in the limit because a random start can land anywhere.

**Simulated annealing escapes by accepting bad moves.** The metallurgy metaphor: heat makes atoms leave local minima; slow cooling lets them settle into lower-energy structures. SA accepts improving moves always and worsening moves with probability e^(ΔE/T), where T (temperature) decreases on a schedule. High T explores; low T exploits. With a slow enough schedule, SA finds the global optimum with probability approaching 1. It is the completeness of a random walk grafted onto the efficiency of hill climbing.

**Local beam search keeps k states and shares information.** Generate all successors of all k states, keep the k best. Threads that produce good successors get more slots; weak threads die. The risk is diversity collapse: all k states collect in one region and the search degenerates to a single hill climb. Stochastic beam search (probability-weighted selection) preserves diversity.

**Genetic algorithms are beam search with recombination.** A population of k individuals; fitness-proportional selection; crossover swaps segments between parents; mutation randomly alters children. The encoding matters: crossover only helps when related parts of a solution are adjacent in the genome. The 8-Queens example (AIMA Figure 4.6) shows a population of 4 with fitness 24, 23, 20, 11; total 78; selection probabilities 31%, 29%, 26%, 14%. Crossover at random cut points produces children; mutation flips single digits. The method moves uphill while exploring via random variation.

**Every method balances exploitation against exploration.** Hill climbing is pure exploitation. Random restarts, temperature, mutation, and stochastic selection are exploration mechanisms. The choice of method is a bet on the landscape shape and the cost of being wrong.

## Relevance

This is the Substrate's first coverage of classical AI search methods. It plants a branch that two sibling files extend: [[eval-hill-climbing]] applies the same landscape math to agent improvement loops, and [[explore-exploit-ad-testing]] maps it onto media buying. The core relevance to existing nodes: [[agent-evaluation]] is the downstream application where the objective function is an eval score; [[harness-engineering]] is the loop that operationalizes the search; [[kaizen]] is the philosophical frame (continuous small steps as hill climbing); [[lean-doctrine]] provides the waste-elimination objective that local search optimizes. The explore/exploit tradeoff is the same one that [[multi-agent-coordination-patterns]] and [[principal-agent-theory]] face when agents must choose between acting on current knowledge and gathering new information.

## Related

- [[agent-evaluation]] — the benchmark catalog and measurement problem this file's noise math extends
- [[eval-hill-climbing]] — sibling: applying local search to agent improvement
- [[explore-exploit-ad-testing]] — sibling: applying bandit methods to ad testing
- [[harness-engineering]] — the feedback loop that runs the search
- [[kaizen]] — continuous improvement as a hill-climbing stance
- [[lean-doctrine]] — waste elimination as the objective function
- [[multi-agent-coordination-patterns]] — explore/exploit at the coordination layer
