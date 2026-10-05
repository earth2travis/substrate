Raw research file. Local search methods from the 'Informed Search, Chapter 4 (b)' lecture deck (AIMA Chapter 4 figures), produced 2026-10-05: source material for later synthesis, not a finished essay. Overlaps `local-search.md` on the four core algorithms (different provenance, same source chapter) but adds ant colony optimization, tabu search, 8-puzzle worked examples, and errata on the deck.

Series: `local-search.md`, `informed-search.md`, `search-depth-first-hill-climbing-beam.md`, `eval-hill-climbing.md`, `explore-exploit-ad-testing.md` (hill-climbing series, 2026-10-05).

Related Substrate nodes: [[local-search]] (sibling theory file covering the same AIMA chapter from the Berkeley CS 188 source), [[agent-evaluation]] (downstream application).

---

# Informed Search: Local Search Methods

Source: `informed-search.pdf` in this folder. It is a 24-slide lecture deck, "Informed Search, Chapter 4 (b)". Some material is adapted from notes by Charles R. Dyer, University of Wisconsin-Madison. The figures come from Russell and Norvig, *Artificial Intelligence: A Modern Approach* (AIMA), Chapter 4.

---

## Scope

The deck covers **iterative improvement** methods, also called **local search**. These methods move from one possible solution to the next until they reach a goal.

Methods in the deck:

1. Hill climbing
2. Simulated annealing
3. Local beam search
4. Genetic algorithms
5. Ant colony optimization
6. Tabu search

The deck lists **online search** in the agenda and in the summary. It does not explain online search.

---

## 1. Hill climbing

### Rule

Always take a step that goes up.

| Type | Rule |
|---|---|
| Simple hill climbing | Take the first upward step that you find. |
| Steepest-ascent hill climbing | Examine all steps. Take the step that goes up most. |

Hill climbing needs almost no memory. It keeps only the current state.

### Formal rule (deck uses minimization)

Move from the current state *n* to a successor *s* if both conditions are true:

- h(s) < h(n). The successor is better than the current state.
- h(s) ≤ h(t) for all successors *t*. The successor is the best successor.

If no successor meets these conditions, stop at *n*.

### Relation to other searches

- It is like **greedy search**, but it cannot backtrack or jump to a different path. It has no memory of other paths.
- It is like **beam search with a beam width of 1**.

### Properties

Hill climbing is **not complete**. It can stop at a local optimum, a plateau, or a ridge.

### Example: 8-puzzle

Evaluation function: f(n) = −(number of tiles out of place). Higher is better. The goal has f = 0.

```
start (−4)    →    (−3)    →    (−3)    →    (−2)    →    (−1)    →    goal (0)
 2 8 3            2 8 3          2 . 3          . 2 3        1 2 3          1 2 3
 1 6 4            1 . 4          1 8 4          1 8 4        . 8 4          8 . 4
 7 . 5            7 6 5          7 6 5          7 6 5        7 6 5          7 6 5
```

At each step, the search picks the successor with the highest value. The other successors have values of −5, −4, or −3.

The second step goes from −3 to −3. This is a **sideways move**. The strict rule above (h(s) < h(n)) does not permit it. A strict hill climb stops at the second state.

---

## 2. The landscape and its problems

Picture each state as a point on a surface. The evaluation function gives the height.

| Feature | Description | Effect on hill climbing |
|---|---|---|
| Local maximum | A peak that is not the highest point. | The search stops. All neighbors are lower. |
| Plateau | A broad flat area. | The search has no direction. The deck suggests a random walk. |
| Ridge | A narrow high line with drops on each side. | A step north, east, south, or west can go down. A diagonal step (for example, northwest) can go up. The search stops but it is not at a peak. |

### Example: local optimum in the 8-puzzle

```
start (−3)        All successors (−4)            goal (0)
 1 2 5            . 2 5    1 2 5    1 2 5         1 2 3
 . 7 4            1 7 4    7 . 4    8 7 4         8 . 4
 8 6 3            8 6 3    8 6 3    . 6 3         7 6 5
```

The start state has a value of −3. All three successors have a value of −4. Hill climbing stops at the start state, but the goal is not reached.

### Remedies

| Remedy | How it works |
|---|---|
| Random restart | Start the search again from a random state. Continue until you find a goal. |
| Problem reformulation | Change the state space so that these features do not occur. |

Some problem spaces are good for hill climbing. Others are very bad for it.

---

## 3. Hill climbing on 8-Queens

### Setup

- Put one queen in each column, in a random row.
- **Goal:** no two queens attack each other.
- **Action:** move one queen to a different row in its column.
- **Successors:** each state has 8 × 7 = 56 successors.
- **Heuristic h:** the number of pairs of queens that attack each other. h = 0 is a solution.

### AIMA Figure 4.3

**(a)** A state with h = 17. Each square shows the value of h if the queen in that column moves to that square. The best value is 12. Eight moves give h = 12.

**(b)** A local minimum. The state has h = 1, but every successor has a higher h. Hill climbing stops here, one pair away from a solution.

---

## 4. Simulated annealing

### Origin

In metallurgy, **annealing** is the process of heating a material and then cooling it in a controlled way. This makes the crystals larger and decreases defects.

- Heat makes atoms leave their initial positions. These positions are local minima of internal energy. The atoms move at random through states of higher energy.
- Slow cooling gives the atoms more time to find a structure with lower energy than the initial structure.

### Method

- Simulated annealing (SA) uses a random search.
- It accepts all changes that improve the objective function *f*.
- It accepts some changes that make *f* worse.
- A control parameter *T* (the **temperature**) sets how many bad moves are accepted.
- *T* starts high and decreases toward 0.

### Intuition: the ping-pong ball

The goal is to get a ping-pong ball into the deepest hole on a bumpy surface.

- Shake the surface to get the ball out of shallow holes (local minima).
- Do not shake too hard, or the ball leaves the deepest hole (global minimum).
- Start with hard shaking (high *T*). Decrease the shaking slowly (lower *T*).

SA combines the **efficiency** of hill climbing with the **completeness** of a random walk.

### Acceptance probability

The deck minimizes *f*. A bad move from state A to state B makes *f* larger. SA accepts it with this probability:

```
P = e^( −(f(B) − f(A)) / T )
```

- A higher *T* gives a higher probability of a bad move.
- When *T* goes to 0, the probability goes to 0. SA then acts like hill climbing.
- If *T* decreases slowly enough, SA is **complete and admissible** (it finds the optimal solution).

---

## 5. Local beam search

### Method

1. Start with *k* random states.
2. Generate all successors of all *k* states.
3. Keep the *k* best successors.
4. Go to step 2.

Local beam search shares information across *k* searches in a simple and efficient way.

### Variant: stochastic beam search

The probability of keeping a state depends on its heuristic value. Better states have a higher probability, but weaker states can also stay.

---

## 6. Genetic algorithms (GA)

### Method

- A search method that copies evolution.
- Similar to stochastic beam search.
- Start with a **population** of *k* random states.
- Make new states in one of two ways:
  - **Mutation:** change a single state.
  - **Reproduction:** combine two parent states.
- Select parents by **fitness**.
- The **encoding** of an individual (its genome) has a large effect on how the search behaves.

### 8-Queens encoding

- A state is a string of 8 digits, each from 1 to 8.
- Each digit is one column. The digit is the row of the queen.
- Example: S = 32752411.
- **Fitness:** the number of pairs of queens that do not attack each other.
- Minimum fitness = 0. Maximum fitness = 8 × 7 / 2 = **28**. A solution has fitness 28.

### Worked example (AIMA Figure 4.6)

**(a) Initial population and (b) fitness:**

| Individual | Fitness | Selection probability |
|---|---|---|
| 24748552 | 24 | 24 / 78 = 31% |
| 32752411 | 23 | 23 / 78 = 29% |
| 24415124 | 20 | 20 / 78 = 26% |
| 32543213 | 11 | 11 / 78 = 14% |

Total fitness = 24 + 23 + 20 + 11 = 78.

**(c) Selection.** Four parents are picked at random by these probabilities:

| Pair | Parent 1 | Parent 2 |
|---|---|---|
| 1 | 32752411 | 24748552 |
| 2 | 32752411 | 24415124 |

32752411 is picked twice. 32543213 (the least fit) is not picked.

**(d) Crossover.** Each pair is cut at a random point. The parts are swapped.

| Pair | Cut | Child 1 | Child 2 |
|---|---|---|---|
| 1 | after digit 3 | 327 + 48552 = 32748552 | 247 + 52411 = 24752411 |
| 2 | after digit 5 | 32752 + 124 = 32752124 | 24415 + 411 = 24415411 |

**(e) Mutation.** Some children have one digit changed at random.

| Before | After | Change |
|---|---|---|
| 32748552 | 32748152 | digit 6: 5 → 1 |
| 24752411 | 24752411 | no change |
| 32752124 | 32252124 | digit 3: 7 → 2 |
| 24415411 | 24415417 | digit 8: 1 → 7 |

### Ma + Pa = Offspring (AIMA Figure 4.7)

The figure shows the boards for 32752411 ("Ma") and 24748552 ("Pa"). The child 32748552 keeps the first 3 columns of Ma and the last 5 columns of Pa. The other columns are lost.

---

## 7. Ant colony optimization (ACO)

ACO is a probabilistic search method. It is for problems that you can reduce to finding good paths through a graph.

### Model

1. Ants leave the nest.
2. Ants find food.
3. Ants go back to the nest. They prefer shorter paths.
4. Ants leave a **pheromone** trail.
5. More ants use the shortest path in a given time, so it gets more pheromone. The shortest path becomes stronger.

The figure shows three stages between the nest (N) and the food (F). At first, ants use all branches. At the end, most ants use the shortest path.

ACO is an example of **agents that communicate through their environment**.

---

## 8. Tabu search

- **Problem:** hill climbing can get stuck on local maxima.
- **Solution:** keep a list of the *k* most recent states (the **tabu list**). Do not let the search go back to these states.
- Tabu search is an example of a **metaheuristic**: a general strategy that controls another search method.

---

## Summary

| Method | States kept | How it escapes local optima | Completeness |
|---|---|---|---|
| Hill climbing | 1 | It does not. | Not complete |
| Hill climbing + random restart | 1 per run | New random start | Complete, given enough restarts |
| Simulated annealing | 1 | Accepts bad moves with probability e^(−Δf/T) | Complete and optimal with a slow enough schedule |
| Local beam search | *k* | Shares information across *k* states | Not complete |
| Stochastic beam search | *k* | Random selection by value | Not complete |
| Genetic algorithm | *k* | Crossover and mutation | Not complete |
| Ant colony optimization | Many agents | Pheromone trails guide many agents | Not stated in the deck |
| Tabu search | 1 + tabu list | Does not go back to recent states | Not stated in the deck |

Main points from the deck:

1. Hill climbing keeps only one state in memory, but it can get stuck on local optima.
2. Simulated annealing escapes local optima. It is complete and optimal with a long enough cooling schedule.
3. Genetic algorithms can search a large space by modeling biological evolution.
4. Online search is useful in state spaces with partial or no information.

---

## Notes on the deck

- **Sign conventions change.** The formal hill-climbing rule and the SA formula minimize. The 8-puzzle example maximizes f = −(tiles out of place). The landscape slides use maxima. The 8-Queens slide minimizes h (attacking pairs), but the GA maximizes fitness (non-attacking pairs). The method is the same in each case.
- **8-Queens successor count.** The deck says 65. The correct number is 56 (8 queens × 7 other rows).
- **8-puzzle example.** The path has one sideways move (−3 to −3). The strict rule on the same deck does not permit this move.
