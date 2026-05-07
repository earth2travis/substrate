---
title: "The 5 Whys"
tags: [concept, lean, problem-solving, methodology, root-cause]
related:
- toyota-production-system
- taiichi-ohno
- a3-thinking
- pdca-cycle
- kaizen-and-continuous-improvement
- lean-doctrine
- fishbone-diagrams
source: research/raw/5-whys.md
---
# The 5 Whys

## Definition

A diagnostic technique that traces symptoms back to systemic causes through iterative questioning. Ask "why" five times (or until reaching bedrock) to move beyond symptoms to root causes.

## Origins

Developed by Sakichi Toyoda, founder of Toyota Industries. Formalized by his successor Taiichi Ohno as part of the Toyota Production System. Older roots: Plato's Meno uses repeated questioning; Leibniz applied iterative whys to theodicy in 1671.

## Why It Works

The technique works because of the cultural soil in which it grew:
- Problems are signals, not nuisances
- Every defect is information
- Honest answers are safe
- The question is "what allowed this?" not "who messed up?"

## Limitations

- Single causal chain may miss interacting causes
- Requires genuine curiosity, not blame
- Works best when combined with fishbone diagrams (for breadth) and A3 thinking (for structure)
- Western companies often fail by copying the tool without the culture

## Complementary Tools

- **Fishbone diagrams**: Fan out across many possible causes
- **A3 thinking**: Capture full investigation on one page
- **PDCA cycle**: Frame the fix as an experiment that feeds the next iteration

## For Agent Systems

When an agent repeats an error, use the 5 Whys:
1. Why did the agent produce incorrect output?
2. Why was the context insufficient?
3. Why didn't the context include the relevant prior decision?
4. Why wasn't the decision written to the persistent memory?
5. Why does the memory protocol lack a write gate before responding?

The fifth why often reveals a systemic gap, not a one-off mistake.
