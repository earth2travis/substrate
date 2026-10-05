---
title: "Search as a Queue Discipline: Depth-First, Hill Climbing, and Beam from MIT 6.034"
tags: [finding, search, algorithms, ai, mit, winston, queue-discipline]
related:
- local-search
- informed-search
- agent-evaluation
source: research/raw/search-depth-first-hill-climbing-beam.md
ingested: 2026-10-05
---
# Search as a Queue Discipline

## Key Points

**One loop generates every search.** Keep a queue of paths. Initialize with the start state. Loop: if the first path reaches the goal, done; otherwise remove it, extend it one step per neighbor, add the new paths to the queue. The only line that changes between depth-first, breadth-first, hill climbing, beam, and best-first is **how the new paths are inserted**. Depth-first adds to the front; breadth-first to the back; hill climbing sorts new paths by heuristic and adds to the front; beam keeps only the w best per level; best-first keeps the whole queue sorted by heuristic. Search is a family of queue disciplines, not a family of algorithms.

**Search is about choice, not maps.** Maps make search visible, but the process is any sequence of decisions with explorable options. Winston's framing: humans see paths in seconds; we do not know how vision does it; programs need explicit procedures. This matters for agent design: the agent's "map" is its context, and its search is explicit and inspectable, unlike human intuition.

**The extended list is a generic deduplication fix.** Breadth-first wastes effort extending paths that end at nodes already expanded. Keep a list of nodes that have been the last node of an extended path; never extend a path ending in one. Helps every search except British Museum (find-everything). In the lecture demo, an extended list cut a breadth-first queue from 103 paths to a fraction of that.

**Hill climbing is depth-first with a heuristic tie-breaker.** Choose the child closest to the goal (by heuristic) instead of alphabetically first. In Winston's demo, depth-first used 48 enqueues and produced the "thief's path" (long and roundabout); hill climbing used 23 and produced a straighter path. Rule of thumb: if you have a signal that you are getting closer, use it. The three failure modes in continuous spaces: local maximum (all neighbors worse), plateau (no gradient, the "telephone pole problem"), ridge (axis moves fail, diagonal needed). Hikers have died on Mt. Washington's plateaus waiting for a gradient.

**Beam search is breadth-first with a width cap.** At each level, keep only the w best paths by heuristic. With w = 2 on the example graph, the search reaches G in three levels with a fraction of breadth-first's work. Hill climbing relates to depth-first as beam relates to breadth-first: both bolt a heuristic onto an uninformed base.

**None of these searches guarantee optimality.** They find good paths. Optimal search (A*, branch and bound) is a different lecture. The distinction matters for agent work: most agent reasoning is satisficing search over actions, not optimal planning.

**Search finds meaning in stories, not just paths on maps.** The Genesis system reads Macbeth, builds an elaboration graph, and searches the graph for patterns matching concepts like revenge and Pyrrhic victory. It answers "why" questions at two levels: common-sense (nearby links) and reflective (which higher-level patterns contain the event). The same queue discipline that finds a route on a map finds narrative structure in a text.

## Relevance

This is the pedagogical spine of the hill-climbing series. Where [[local-search]] (Berkeley) and [[informed-search]] (AIMA deck) present local search as landscape navigation, this file presents all search as one loop with swappable queue disciplines. Two contributions are load-bearing for the Substrate. First, the queue-discipline unification is the cleanest mental model for agent reasoning loops: an agent's ReAct loop, its planning step, and its eval-driven improvement loop are all the same skeleton with different insertion rules, which connects directly to [[agentic-architecture]] and [[goal-primitive]]. Second, the Genesis demonstration shows that search over structured representations is a meaning-making operation, not just a navigation operation, which is the same move the Substrate itself makes when it searches its own graph for synthesis candidates. The "search is about choice, not maps" frame is the sharpest one-line summary of why agent evaluation ([[agent-evaluation]]) cannot be reduced to path-checking: the agent is making choices in a space, and what we evaluate is the choice quality.

## Related

- [[local-search]] — sibling: local search as landscape navigation
- [[informed-search]] — sibling: the AIMA deck version
- [[agent-evaluation]] — downstream: evaluating choice quality, not path correctness
- [[agentic-architecture]] — the ReAct loop as a queue discipline
- [[goal-primitive]] — goal-directed search as an emerging agent primitive
