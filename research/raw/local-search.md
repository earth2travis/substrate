Raw research file. Local search theory from AIMA Chapter 4 via the UC Berkeley CS 188 textbook, produced 2026-10-05: source material for later synthesis, not a finished essay. This is the Substrate's first coverage of classical AI search methods; it plants a new branch.

Series: `local-search.md`, `informed-search.md`, `search-depth-first-hill-climbing-beam.md`, `eval-hill-climbing.md`, `explore-exploit-ad-testing.md` (hill-climbing series, 2026-10-05).

Related Substrate nodes: [[agent-evaluation]] (downstream application: hill climbing on eval scores), [[continual-learning-for-agents-replit]] (adjacent: iterative agent improvement loops).

---

# Local Search: Hill Climbing, Simulated Annealing, Local Beam, Genetic Algorithms

Source: [UC Berkeley CS 188 textbook, 1.5 Local Search](https://inst.eecs.berkeley.edu/~cs188/textbook/search/local.html). The figures on that page come from Russell and Norvig, *Artificial Intelligence: A Modern Approach* (AIMA), Chapter 4. Details from those figures are included here.

---

## What local search is

Classic search (depth-first, breadth-first, A*) finds a **path** to a goal. Local search finds a **goal state** only. The path does not matter.

Use local search when:

- The problem is to find a configuration that satisfies constraints (for example, 8-Queens).
- The problem is to optimize an objective function (for example, a schedule or a layout).

Local search keeps only the current state (or a small set of states). It does not keep a search tree. So it uses very little memory, and it works on very large or continuous state spaces.

### The state-space landscape

Picture every state as a point on a surface. The height of each point is the objective value. The goal is the highest point.

| Feature | Description |
|---|---|
| Global maximum | The highest point on the surface. This is the best solution. |
| Local maximum | A peak that is higher than all its neighbors, but lower than the global maximum. |
| Flat local maximum | A flat area. No neighbor is higher. |
| Shoulder | A flat area that goes up again at one edge. Progress is possible but slow. |

To minimize (for example, cost), turn the surface upside down. Then the goal is the lowest valley.

---

## 1. Hill-climbing search

### Mechanism

Hill climbing is also called **steepest-ascent** search.

1. Start at a state.
2. Look at all neighbors of the current state.
3. Move to the neighbor with the highest objective value.
4. Stop when no neighbor is higher than the current state.

Pseudocode (AIMA):

```
function HILL-CLIMBING(problem) returns a state that is a local maximum
    current ← problem.INITIAL-STATE
    loop do
        neighbor ← a highest-valued successor of current
        if neighbor.VALUE ≤ current.VALUE then return current
        current ← neighbor
```

### Properties

- **Not complete.** It can stop at a local maximum and never find the goal.
- **Fast.** It often makes fast progress toward a solution.
- **Low memory.** It stores one state.

### Where it fails

- **Local maxima.** Every neighbor is lower, so the search stops.
- **Plateaus.** All neighbors have the same value, so the search has no direction.
- **Shoulders.** The search can stop on the flat part before it reaches the higher part.

### Variants

| Variant | How it works | Effect |
|---|---|---|
| Stochastic hill climbing | Select a random uphill move. Steeper moves can have a higher probability. | Slower to converge. Sometimes finds higher maxima. |
| Sideways moves | Permit moves to neighbors with the same value. Set a limit on the number of these moves. | Lets the search cross shoulders. |
| Random-restart hill climbing | Run hill climbing many times, each from a random start state. Keep the best result. | **Complete**, because a random start state can eventually be the goal. |

Gradient descent is hill climbing for minimization in continuous spaces. It moves in the direction of the steepest decrease.

---

## 2. Simulated annealing

### Idea

Hill climbing never moves down, so it gets stuck. A random walk moves anywhere, so it is complete but very slow. Simulated annealing combines the two.

The name comes from metallurgy. Annealing is the process of heating metal and then cooling it slowly. The atoms settle into a low-energy, strong structure.

### Mechanism

1. At each step, select a **random** neighbor.
2. If the neighbor is better, always move to it.
3. If the neighbor is worse, move to it with a probability. This probability depends on a **temperature** parameter *T*.
4. Decrease *T* over time, as given by a **schedule**.

At the start, *T* is high, so the search accepts many bad moves. It explores. At the end, *T* is low, so the search accepts almost no bad moves. It acts like hill climbing.

### Acceptance probability (AIMA)

Let ΔE = value(neighbor) − value(current). If ΔE < 0, accept the move with probability:

```
P = e^(ΔE / T)
```

- A move that is much worse (large negative ΔE) has a low probability.
- The same move has a higher probability when *T* is high.

Pseudocode (AIMA):

```
function SIMULATED-ANNEALING(problem, schedule) returns a solution state
    current ← problem.INITIAL-STATE
    for t = 1 to ∞ do
        T ← schedule(t)
        if T = 0 then return current
        next ← a randomly selected successor of current
        ΔE ← next.VALUE − current.VALUE
        if ΔE > 0 then current ← next
        else current ← next only with probability e^(ΔE/T)
```

### Guarantee

If the temperature decreases slowly enough, simulated annealing finds the global maximum with a probability that approaches 1.

---

## 3. Local beam search

### Mechanism

1. Start with *k* random states.
2. Generate all successors of all *k* states.
3. If one successor is a goal, stop.
4. Otherwise, select the *k* best successors from the **full** list. These are the new states.
5. Go to step 2.

### Difference from *k* independent hill climbs

The *k* threads share information. A state that produces many good successors gets more of the *k* places in the next step. Weak threads stop, and the search moves its effort to the best region of the landscape.

### Problems

- The *k* states can collect in one small region. Then the search loses diversity and acts like one hill climb.
- It can stop on flat regions.

### Variant

**Stochastic beam search** selects the *k* successors at random. The probability of each successor increases with its value. This keeps more diversity and helps on flat regions.

### Relation to beam search in classic search

Beam search in path search (MIT 6.034, Lecture 4) keeps the *w* best **paths** at each level. Local beam search keeps the *k* best **states**. The idea is the same: limit the width, keep the best.

---

## 4. Genetic algorithms

### Idea

A genetic algorithm is a type of stochastic beam search. A successor comes from **two** parent states, not from one. The model is natural selection.

### Terms

| Term | Meaning |
|---|---|
| Population | The *k* current states. |
| Individual | One state, written as a string over a finite alphabet. |
| Fitness function | The objective function. Higher is better. |
| Selection | Pick parents. The probability of selection is proportional to fitness. |
| Crossover | Cut two parents at a random point. Join the first part of one with the second part of the other. |
| Mutation | Change one random position in a child, with a small independent probability. |

### Mechanism

1. Start with *k* random individuals.
2. Calculate the fitness of each individual.
3. Select pairs of parents. Fitter individuals are selected more often.
4. For each pair, select a random crossover point and make children.
5. Apply mutation to each child.
6. The children are the new population. Go to step 2.

### 8-Queens example (AIMA Figure 4.6)

**Encoding.** A state is 8 digits. Each digit is one column. The digit (1 to 8) is the row of the queen in that column.

**Fitness.** The number of pairs of queens that do not attack each other. The maximum is 8 × 7 / 2 = **28**. A solution has fitness 28.

**Initial population and selection probabilities:**

| Individual | Fitness | Selection probability |
|---|---|---|
| 24748552 | 24 | 31% |
| 32752411 | 23 | 29% |
| 24415124 | 20 | 26% |
| 32543213 | 11 | 14% |

Each probability is fitness ÷ total fitness (24 + 23 + 20 + 11 = 78).

**Steps shown in the figure:**

1. **Selection.** Four parents are picked by these probabilities. 32752411 is picked twice. 32543213 is not picked.
2. **Pairing.** The parents form two pairs.
3. **Crossover.** Each pair is cut at a random point. For example, 327|52411 and 247|48552 make 32748552 and 24752411.
4. **Mutation.** Some children have one digit changed at random.

### Why crossover helps

Crossover joins blocks of a string that were evolved separately. If each block is good, the child can be better than both parents. For 8-Queens, the first three columns of one parent and the last five of another parent can combine into a better board.

Crossover helps only when the encoding puts related parts next to each other. If good blocks do not map to adjacent positions, crossover mostly breaks them.

### Strengths

- Moves uphill, and also explores the state space with random variation.
- Shares information between threads through crossover.

---

## Comparison

| Algorithm | States kept | Bad moves? | Complete? | Main risk |
|---|---|---|---|---|
| Hill climbing | 1 | No | No | Local maxima, plateaus |
| Random-restart hill climbing | 1 per run | No | Yes | Many restarts on hard landscapes |
| Simulated annealing | 1 | Yes, with probability e^(ΔE/T) | Yes, with a slow schedule | Schedule tuning |
| Local beam search | *k* | No | No | Loss of diversity |
| Stochastic beam search | *k* | Yes, by random selection | No | Slower convergence |
| Genetic algorithm | *k* (population) | Yes, through mutation | No | Encoding must support crossover |

---

## Key points

1. Local search finds good states, not paths. It uses almost no memory.
2. Pure hill climbing is fast but stops at local maxima.
3. Randomness fixes this: random restarts, random moves, temperature, mutation.
4. Keeping *k* states and sharing information between them (beam search, genetic algorithms) moves effort to the best regions.
5. Each method balances **exploitation** (go up now) against **exploration** (look elsewhere).
