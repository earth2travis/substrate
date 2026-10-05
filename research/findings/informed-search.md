---
title: "Informed Search: Local Search Methods from the AIMA Chapter 4(b) Deck"
tags: [finding, search, optimization, ai, algorithms, local-search, ant-colony, tabu-search]
related:
- local-search
- agent-evaluation
- harness-engineering
source: research/raw/informed-search.md
ingested: 2026-10-05
---
# Informed Search: Local Search Methods

## Key Points

**This is a second provenance pass over AIMA Chapter 4.** The sibling file [[local-search]] covers the same four core algorithms (hill climbing, simulated annealing, local beam, genetic algorithms) from the Berkeley CS 188 source. This deck adds ant colony optimization, tabu search, worked 8-puzzle and 8-Queens examples, and errata on the deck itself. The two files are complementary, not redundant.

**Hill climbing has two modes with different tradeoffs.** Simple hill climbing takes the first upward step found; steepest-ascent examines all successors and takes the best. The deck formalizes steepest-ascent as: move from n to s if h(s) < h(n) and h(s) ≤ h(t) for all successors t (minimization convention). Both modes keep exactly one state in memory. Both are not complete.

**The 8-puzzle example exposes a deck inconsistency.** The worked path includes a sideways move from f = −3 to f = −3. The strict formal rule on the same deck (h(s) < h(n)) forbids this. The deck also claims 8-Queens has 65 successors; the correct number is 56 (8 queens × 7 other rows). These are teaching artifacts, not method flaws, but they matter when the deck is the primary source.

**Ridges are the failure mode that matters most for high-dimensional spaces.** A ridge is a narrow high line with drops on each side. Axis-aligned steps (N, S, E, W) all go down, so hill climbing stops. Diagonal steps go up. In high dimensions, most directions are axis-aligned relative to any single coordinate, so ridge-trapping gets worse, not better, as dimensionality increases. This is why one-change-at-a-time agent improvement stalls.

**Ant colony optimization is agents communicating through their environment.** Ants leave pheromone trails; shorter paths accumulate more pheromone per unit time; the path strengthens autocatalytically. ACO is probabilistic, works on graph-reducible problems, and demonstrates stigmergic coordination: no ant has the map, but the colony finds the shortest path. The deck lists it as a sixth method but gives no completeness analysis.

**Tabu search is a metaheuristic, not a search method.** Keep a list of the k most recent states (the tabu list) and forbid returning to them. It wraps hill climbing (or another base method) and prevents immediate backtracking into local optima. It is the memory-augmented version of hill climbing, trading state for escape capability.

**Simulated annealing's guarantee is conditional on the cooling schedule.** The deck states SA is "complete and admissible" if T decreases slowly enough. The acceptance probability for a bad move is P = e^(−(f(B) − f(A))/T) under the deck's minimization convention. When T → 0, SA degenerates to hill climbing. The schedule is the tunable that trades optimality against time.

## Relevance

This file is the errata-and-extensions layer for [[local-search]]. Its unique contributions: (1) ACO and tabu search as methods not covered in the Berkeley source; (2) the ridge failure mode as the dominant risk in high-dimensional agent improvement; (3) the deck's internal inconsistencies as a reminder that even canonical teaching materials have errors that propagate. For the Substrate's agent-improvement cluster, the ridge analysis is the sharpest tool: it explains why single-edit prompt tuning plateaus and why coordinated changes (tool + prompt + grader) are necessary to cross ridges. The ACO section connects to [[multi-agent-coordination-patterns]] as a stigmergic coordination model, and tabu search's memory-augmented escape connects to [[agent-memory]] as a design pattern: sometimes the solution to being stuck is remembering where you have been.

## Related

- [[local-search]] — sibling: same AIMA chapter from the Berkeley CS 188 source
- [[agent-evaluation]] — downstream: the objective function being optimized
- [[harness-engineering]] — the loop that runs the search
- [[multi-agent-coordination-patterns]] — ACO as stigmergic coordination
- [[agent-memory]] — tabu list as episodic memory for search
