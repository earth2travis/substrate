Raw research file. Notes on MIT 6.034 Lecture 4 (Patrick Winston, Fall 2010): depth-first, hill climbing, and beam search under one queue framework, produced 2026-10-05: source material for later synthesis, not a finished essay.

Series: `local-search.md`, `informed-search.md`, `search-depth-first-hill-climbing-beam.md`, `eval-hill-climbing.md`, `explore-exploit-ad-testing.md` (hill-climbing series, 2026-10-05).

Related Substrate nodes: [[local-search]] (sibling theory file: local versions of the same hill-climbing and beam ideas), [[agent-architectures]] (adjacent: search as a model of agent reasoning), [[agent-evaluation]] (downstream application).

---

# Search: Depth-First, Hill Climbing, Beam

Notes from MIT 6.034 Artificial Intelligence, Fall 2010, Lecture 4, Patrick Winston.
Source: [MIT OpenCourseWare](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/resources/lecture-4-search-depth-first-hill-climbing-beam/) (CC BY-NC-SA).

---

## The core idea

**Search is about choice, not maps.** Maps are a clear way to show search. But search is any process where you make a sequence of decisions and explore the options.

Humans often find a good path on a map with their eyes in seconds. We do not know how vision does this. Programs have no eyes, so they need explicit procedures.

---

## The example graph

All examples use this graph. Start at **S**. Goal is **G**.

```
        A ------- D
       / \         \
      S   \         G
       \   \
        B---+
         \
          C ------- E
```

Edges: S-A, S-B, A-B, A-D, B-C, C-E, D-G.

Heuristic (straight-line distance to G): B is about 6. A is about 7. A and C are equally far from G.

### Conventions (important for quizzes)

- **Lexical order.** List the children of a node in alphabetical order.
- **No loops.** A path never revisits a node already on that path.

---

## British Museum search

Find **every** possible path. No cleverness helps, because you must find everything.

All paths from S:

```
S ─┬─ A ─┬─ B ── C ── E      (dead end)
   │     └─ D ── G           (goal)
   └─ B ─┬─ A ── D ── G      (goal)
         └─ C ── E           (dead end)
```

---

## Depth-first search

Plunge down the leftmost branch. Go deep before you go wide.

1. S → A → B → C → E. Dead end.
2. **Backtrack** to the last choice point (at A, where we chose B over D).
3. S → A → D → G. Done.

**Backtracking** means: at a dead end, go back to the last place you made a choice, and take the next branch. It is optional in principle, but you would almost always use it with depth-first search.

In the demo on the Cambridge map, depth-first produced the "thief's path": a long, roundabout route.

---

## Breadth-first search

Build the tree level by level. Stop when a level contains the goal.

```
Level 1:  S-A   S-B
Level 2:  S-A-B   S-A-D   S-B-A   S-B-C
Level 3:  S-A-B-C   S-A-D-G   S-B-A-D   S-B-C-E   ← G found
```

It always finds a path with the fewest steps. But the number of paths grows fast. In the demo, it wasted time exploring away from the goal.

---

## One algorithm for all searches

Every search here uses the same loop. Keep a **queue of paths**.

```
1. Initialize the queue with the one-node path (S).
2. Loop:
   a. If the first path on the queue reaches the goal → done.
   b. Remove the first path. Extend it (one new path per neighbor).
   c. Add the new paths to the queue.    ← the only line that changes
   d. If the queue is empty → fail.
```

Step **c** decides which search you get:

| Search        | How to add new paths to the queue           |
|---------------|---------------------------------------------|
| Depth-first   | Add to the **front**                        |
| Breadth-first | Add to the **back**                         |
| Hill Climbing | Sort new paths by heuristic, add to **front** |
| Beam          | Keep only the **w best** at each level      |
| Best-first    | Keep the whole queue sorted by heuristic    |

### Depth-first queue trace

Paths are written in reverse (newest node first), Lisp style.

```
((S))
((A S) (B S))
((B A S) (D A S) (B S))
((C B A S) (D A S) (B S))
((E C B A S) (D A S) (B S))
((D A S) (B S))                 ← E is a dead end; it just drops off
((G D A S) (B S))               ← first path reaches G. Done.
```

---

## The extended list

Breadth-first search is wasteful: it extends many paths that end at the same node.

**Fix:** Keep a list of nodes that have already been the *last node of an extended path*. Do not extend a path whose last node is already on that list.

In the demo, a breadth-first search put 103 paths on the queue. With the extended list, it needed far fewer.

The extended list helps depth-first, breadth-first, and the informed searches. Nothing helps the British Museum search.

---

## Hill Climbing

Depth-first search, but **break ties by distance to the goal** instead of alphabetical order.

1. From S: A (~7) or B (6). Choose **B**.
2. From B: A or C. They are equally far. Use lexical order: choose **A**.
3. From A: only D.
4. From D: G. Done.

Path: S → B → A → D → G. No backtracking in this example (this is luck, not a rule). Not the shortest path, but a good one.

In the demo, depth-first used 48 enqueueings. Hill Climbing used 23 and gave a much straighter path.

**Rule:** If you have a heuristic that tells you whether you are getting closer, use it.

### Problems with Hill Climbing in continuous spaces

Picture yourself on a mountain in fog. You test a step north, south, east, and west, and move in the direction that goes up most.

1. **Local maximum.** You reach a small peak and every step goes down. You are not at the real top.
2. **Plateau ("telephone pole problem").** The ground is flat. No step looks better than another, so you get no guidance. Hikers on the flat shoulders of Mt. Washington have died this way.
3. **Ridge.** A sharp ridge runs diagonally. Every step along an axis (N, S, E, W) goes down, so you think you are at the top. You are not stuck, but fooled. This is worse in high-dimensional spaces.

---

## Beam Search

Breadth-first search with a limit: at each level, keep only the **w** best paths (the beam width), ranked by the heuristic.

With w = 2:

```
Level 1:  S-A   S-B                       (keep both)
Level 2:  S-A-B   S-A-D   S-B-A   S-B-C   → keep the 2 closest to G: ends B and D
Level 3:  S-A-B-C   S-A-D-G               ← G found
```

Hill Climbing relates to depth-first the same way Beam relates to breadth-first: both add a heuristic. In the demo, Beam search did not waste effort on nodes that move away from the goal.

---

## Best-first search

Always extend the leaf (anywhere in the tree) that is closest to the goal. It can jump around the tree. The symbolic integration program from an earlier lecture works this way: it always takes the easiest open problem next.

---

## Summary table

| Search         | Backtracking? | Extended list helps? | Informed (uses heuristic)? |
|----------------|---------------|----------------------|----------------------------|
| British Museum | No            | No                   | No                         |
| Depth-first    | Yes           | Yes                  | No                         |
| Breadth-first  | No            | Yes                  | No                         |
| Hill Climbing  | Yes           | Yes                  | Yes                        |
| Beam           | No            | Yes                  | Yes                        |

None of these searches guarantee the **optimal** path. They find good paths. Optimal search is a later lecture.

---

## Search as a model of thinking

Do we search in our heads? Yes: every time we make a plan, we evaluate choices.

Winston showed the **Genesis** system. It reads a plain-English version of *Macbeth*, plus common-sense rules (for example, "if someone kills you, you are dead") and descriptions of higher-level concepts such as *revenge* and *Pyrrhic victory*.

- Genesis builds an **elaboration graph** of the story.
- It **searches** the graph for patterns that match each concept. It found revenge, and a Pyrrhic victory: Macbeth wants to be king, becomes king, and is killed as a result.
- It answers "why" questions on two levels:
  - **Common sense:** look at nearby links in the graph (Macduff killed Macbeth because Macbeth angered him).
  - **Reflective:** report which higher-level patterns contain the event (the killing is part of revenge and a Pyrrhic victory).

The point: the same search ideas that find a path on a map can also find meaning in a story.
