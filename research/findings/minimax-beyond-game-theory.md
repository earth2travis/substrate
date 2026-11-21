---
title: "Minimax Beyond Game Theory: Decision Theory, Statistics, and AI"
tags: [finding, game-theory, statistics, machine-learning, ai, decision-theory]
related:
- irl-theoretical-foundations
- ziebart-maxent-irl-alignment-conscience
- prisoners-dilemma-anatomy
source: research/raw/minimax-beyond-game-theory.md
ingested: 2026-11-15
---
# Minimax Beyond Game Theory: Decision Theory, Statistics, and AI

## Key Points

**Three export routes from von Neumann's 1928 theorem.** Wald converted minimax into a normative standard for inference (1945-1950): the statistician plays a zero-sum game against Nature, the minimax rule minimizes worst-case risk, and the complete class theorem ties minimax rules to Bayes rules under the least favorable prior. Shannon converted it into a search procedure for machines (1950): evaluate the game tree by alternating max and min over a static evaluation function, with the Shannon number (10^120) arguing brute force is hopeless. The online-learning tradition converted Savage's regret variant into an algorithm design principle (Hannan 1957, Hart-Mas-Colell 2000, CFR 2007). Each export changed what "minimax" means: a statistical optimality yardstick, a game-tree search rule, a saddle-point training objective.

**Wald is the hinge for the Substrate.** Statistical decision theory is demobilized game theory: the same mathematics redirected from adversaries to experiments. Everything after, Fano-style lower bounds, Wasserstein DRO, adversarial training, is an attempt to compute, bound, or optimize the object Wald defined: the best worst case. Minimax in statistics is a statement about exchanging sup and inf, not merely a style of caution.

**Regret is the machine-age variant.** Savage's minimax regret (JASA 1951) compares acts to the best achievable per state; Savage recanted in 1954, Milnor showed no criterion under ignorance satisfies all desiderata, and regret re-emerged as the robustness standard under deep uncertainty (RAND RDM, info-gap, Manski). Online learning inherited regret because its comparator, the best fixed action in hindsight, is defined relative to the realized sequence. The shift from risk to regret is a shift from guarantees about a model to guarantees about a process.

**The game-AI lineage is minimax search, then its learned displacement.** Shannon 1950 (scheme), Knuth-Moore 1975 (alpha-beta analysis: b^(d/2) effective branching, verified), Samuel 1959 (learning plus minimax, the template for everything since), Deep Blue 1997 (classical minimax at hardware scale, both triumph and ceiling), then MCTS/AlphaGo (Nature 2016, verified): learned policy and value networks guiding sampled search displaced full-width adversarial search. The counter-tradition is a change of opponent model, not a rejection of minimax: MCTS assumes the opponent plays roughly like itself rather than the worst-case line. The minimax skeleton survived; the brute-force flesh was replaced by learned tissue.

**GANs made Wald's game literal, with a learned opponent.** Goodfellow et al. 2014 (verified) define an explicit two-player minimax game whose ideal solution recovers the data distribution. Training fails in non-convex parameter space: simultaneous gradient descent cycles even in bilinear games (Jacobian eigenvalues purely imaginary at the saddle), and mode collapse is a non-equilibrium local optimum of myopic sequential play. Daskalakis et al. 2018 (verified) show Optimistic Mirror Descent restores last-iterate convergence in the bilinear case; the fix is an import from online learning, not game theory proper.

**The poker lineage is minimax as algorithm, not bound.** CFR (Zinkevich et al., NeurIPS 2007) decomposes regret across information sets; self-play time-averaged strategies converge to the minimax saddle in two-player zero-sum games. Heads-up limit hold'em solved (Bowling et al., Science 2015, verified); Libratus (2017) and Pluribus (Science 2019, verified) extended to no-limit and multiplayer, with Pluribus's blueprint trained for under $200 of compute. CFR is minimax about the destination, not the route: no game tree is ever enumerated. Pluribus's multiplayer success has no minimax guarantee; that edge is empirical.

**Disambiguation for the Substrate.** In the IRL theoretical-foundations file, "minimax" names the statistical yardstick (Le Cam, Fano, Assouad lower bounds). In game AI it names a search rule. In GANs, DRO, and adversarial training (Madry et al. 2018, verified) it names a saddle objective. Same mathematics, different theorems. MaxEnt IRL is the mirror image: maximum over uncertainty versus minimum over worst cases; the two meet in the Lagrangian dual.

## Related

- [[turing-1950-imitation-game]] -- Turing's 1950 paper names chess as a candidate test domain; Turochamp lineage
