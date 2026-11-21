---
title: "Minimax Theorem: Statement, Proofs, and Mathematical Structure"
tags: [finding, game-theory, mathematics, proofs, complexity]
related:
- prisoners-dilemma-anatomy
- irl-theoretical-foundations
- multi-agent-coordination-patterns
source: research/raw/minimax-theorem-statement-proofs.md
ingested: 2026-11-15
---
# Minimax Theorem: Statement, Proofs, and Mathematical Structure

## Key Points

**The theorem, precisely.** For every m x n real matrix A: max over x in Delta_m of min over y in Delta_n of x^T A y equals min over y of max over x. The common value v is the game's value; optimal mixed strategies form a saddle point. Security-level interpretation: the row player can guarantee v, the column player can cap row at v, so neither gains from knowing the other's plan. This is what makes zero-sum games solvable in a strong sense.

**Mixed strategies are the object, not a convenience.** Matching pennies has no pure saddle point (maximin -1, minimax +1); the unique equilibrium is (1/2, 1/2) with value 0, via the equalization principle: an optimal mix makes the opponent indifferent among its support. Determinism leaks information; the only way to be unexploitable is to randomize so the opponent's best response is a tie. Equalization reappears as complementary slackness in the LP formulation.

**Four proof families, each load-bearing somewhere.** (a) Separating hyperplane (Ville 1938): the conceptual core; LP duality is itself proved by separation. (b) Brouwer fixed point (von Neumann 1928 flavor): best-response correction maps on compact convex sets. (c) Kakutani correspondence fixed point (1941): exactly the machinery Nash used in 1950 for general n-player existence. (d) LP duality (Dantzig, Gale-Kuhn-Tucker 1951): the modern textbook standard because it is short and constructive. Minimax and LP strong duality are mathematically equivalent theorems, not merely analogous; each reduces to the other.

**The complexity boundary is sharp.** Two-player zero-sum equilibrium is in P via LP (interior point methods). General Nash equilibrium is PPAD-complete (Daskalakis-Goldberg-Papadimitriou 2006/2009; Chen-Deng 2006 for two players, both verified). In zero-sum games the best-response conditions collapse to one LP; in general-sum they form a linear complementarity problem that is PPAD-complete. Minimax is the tractable island inside the intractable sea of equilibrium computation.

**In non-zero-sum games, minimax stops characterizing rational play.** No single value; multiple non-interchangeable equilibria; minimax strategies can be irrational against non-adversarial opponents. The prisoner's dilemma in one line: the minimax strategy is defect, and its value is strictly worse than the cooperative payoff; that is precisely the dilemma.

**Generalizations and their limits.** Sion 1958 (Pacific Journal of Mathematics 8(1):171-176, verified) is the standard general form: quasiconcave-quasiconvex, one-sided compactness suffices, semicontinuity. Hypotheses are tight: Sion's own counterexample fails without semicontinuity, and naturals-with-sign payoffs fail without compactness. Far kin: Gale-Stewart (1953) and Martin's Borel determinacy (1975, verified) assert max-min equals min-max for win-lose infinite games, requiring definability hypotheses; the axiom of choice manufactures counterexamples on both sides.

## Related

- [[riemann-hypothesis-2026-claims]] -- Statement fidelity versus compilation as the crux of a formal proof claim
- [[riemann-hypothesis-what-a-proof-would-mean]] -- What a formal proof buys and does not buy
- [[ai-math-verification-bottleneck]] -- Verification, not generation, as the binding constraint
