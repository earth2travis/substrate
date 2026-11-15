---
title: "Minimax Theorem: Mathematical History"
tags: [finding, game-theory, mathematics, history, economics]
related:
- prisoners-dilemma-anatomy
- iterated-prisoners-dilemma-axelrod-tournaments
- ziebart-maxent-irl-alignment-conscience
source: research/raw/minimax-theorem-history.md
ingested: 2026-11-15
---
# Minimax Theorem: Mathematical History

## Key Points

**Borel posed the problem and conjectured against its solution.** Borel opened the mathematical study of games in 1921, defined the symmetric normal form and the "methode de jeu," found optimal mixed strategies for 2x2 and 3x3 cases, but conjectured, incorrectly, that maximin and minimax need not coincide for larger games. The question sat open until von Neumann. Frechet's 1953 priority claim for Borel prompted a public dispute; von Neumann answered that Borel had posed the problem but proved nothing and had in fact conjectured against the theorem.

**Von Neumann's 1928 proof was stronger than the version history remembers.** "Zur Theorie der Gesellschaftsspiele" (Mathematische Annalen 100: 295-320) laid out the full architecture: extensive form, reduction to normal form, mixed strategies, and the theorem that every finite two-person zero-sum game has a value in mixed strategies. Per Kjeldsen (2001), von Neumann actually proved the theorem for quasiconcave-quasiconvex functions, a strictly more general result than the bilinear payoff case he is usually credited with; the narrower attribution comes from the 1944 book with Morgenstern, which presented only the bilinear form. Sion's celebrated 1958 generalization was, unbeknownst to Sion, already inside the 1928 proof. Von Neumann regarded the theorem as load-bearing: "there could be no theory of games on these bases without that theorem."

**The fixed-point turn made equilibrium existence a general engine.** Von Neumann's 1937 paper generalized Brouwer's fixed-point theorem to set-valued mappings for an expanding-economy model; minimax follows as a consequence. Kakutani (1941, Duke Mathematical Journal) sharpened this: upper hemicontinuous convex-valued correspondences on compact convex sets have fixed points. The line of descent is Brouwer (1911), von Neumann (1937), Kakutani (1941), Nash (1950), and from Nash to Debreu-Arrow-McKenzie general equilibrium. Minimax is the ancestor of every equilibrium existence argument in the Substrate's neighborhood.

**Elementary proofs multiplied.** Ville gave the first elementary proof in 1938 using separating hyperplanes; Weyl another in 1950; Dantzig's linear programming revealed every two-person zero-sum game is equivalent to an LP, with LP duality and minimax as two faces of one fact (Gale, Kuhn, Tucker 1951); Shapley and Snow gave a basic-solutions proof in 1950.

**Downstream significance for the Substrate.** Nash equilibrium existence, and hence the equilibrium framing in the prisoner's dilemma series, runs through Kakutani, which runs through von Neumann 1937. The minimax regret criterion and adversarial formulations in learning theory, including the worst-case-reward estimation underlying maximum causal entropy IRL, inherit the same saddle-point logic: one player picks a policy, nature or an adversary picks the environment, and the value of the game certifies the guarantee.
