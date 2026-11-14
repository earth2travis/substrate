# Minimax Theorem: Statement, Proofs, and Mathematical Structure

Raw research file. Concept 2 of 4 from a deep-dive series on the minimax theorem produced 2026-11-14. This file covers the formal statement, why randomization is necessary, the four proof families, the Nash relationship, complexity, generalizations, and infinite-game extensions. It is source material for later synthesis, not a finished essay.

Stance: FACT tags apply to claims verified live this session or directly derivable from the stated mathematics; BACKGROUND marks established record not re-verified; INTERPRETATION tags apply to comparative readings. Plain-text math notation throughout (Delta_m for the m-simplex, x^T A y for expected payoff).

Related Substrate nodes: [[minimax-theorem-history]] (sibling file: where the theorem came from), [[prisoners-dilemma-anatomy]] (the prisoner's dilemma's equilibrium structure rests on the existence results this file covers), [[2026-06-29-irl-theoretical-foundations]] (uses "minimax" in the statistical lower-bound sense; see the disambiguation note in the sibling applications file). Note: this series plants the Substrate's first branch into game theory's mathematical foundations.

Series: minimax-theorem-history.md, minimax-theorem-statement-proofs.md, minimax-beyond-game-theory.md, minimax-reception-influence-critiques.md

---

## 1. The claim under examination

INTERPRETATION: the minimax theorem is usually stated as a fact about matrix games, but its content is broader: adversarial worst-case and defensive best-case meet exactly when the strategy sets are convex and compact and the payoff is bilinear (and, per later generalizations, quasiconcave-quasiconvex). This file tests how much of the standard statement survives scrutiny: what the theorem says, why it needs mixed strategies, which proof is actually load-bearing in modern use, and where the equality breaks.

---

## 2. Formal statement

FACT. A two-person zero-sum game in normal form is specified by an m x n real matrix A. Row player
(player 1) picks a row i in {1,...,m}, column player (player 2) picks a column j in {1,...,n}, and
the payoff is A_ij from player 2 to player 1. Player 2's payoff is -A_ij, so the players' interests
are exactly opposed.

FACT. A mixed strategy for the row player is a probability vector x in Delta_m, the m-simplex: x_i
>= 0 and sum_i x_i = 1. Similarly y in Delta_n for the column player. The expected payoff is x^T A y
= sum_i sum_j x_i A_ij y_j.

FACT (von Neumann minimax theorem, 1928). For every m x n real matrix A,

    max over x in Delta_m of min over y in Delta_n of x^T A y     =     min over y in Delta_n of max
over x in Delta_m of x^T A y.

FACT. The common value is called the value v of the game. Because for fixed x the function x^T A y
is linear in y, its minimum over Delta_n is attained at a pure strategy, so min_y x^T A y = min_j
(A^T x)_j. The left side is therefore max_x min_j (A^T x)_j, the largest guaranteed expected payoff
the row player can secure.

FACT / INTERPRETATION. Security-level interpretation. The left side is the row player's security
level: commit to x first, adversary responds optimally, and x still earns at least min_j (A^T x)_j.
The right side is the column player's loss ceiling. Minimax says these coincide. The rows player can
guarantee v and the column player can cap the row player at v, so neither has anything to gain from
knowing the other's plan. This is what makes zero-sum games "solvable" in a strong sense: the value
is a well-defined rational outcome.

FACT. Optimal mixed strategies x*, y* achieve the two sides: min_y x*^T A y = v and max_x x^T A y* =
v. The pair (x*, y*) is a saddle point of x^T A y over Delta_m x Delta_n: x^T A y* <= x*^T A y* <=
x*^T A y for all x, y. Existence of optimal strategies is part of the theorem, and saddle points
always exist for finite zero-sum games.

BACKGROUND. von Neumann proved the theorem in 1928 ("Zur Theorie der Gesellschaftsspiele",
Mathematische Annalen 100, 295-320). The result is the founding theorem of game theory; von Neumann
and Morgenstern's 1944 Theory of Games and Economic Behavior built the whole edifice on top of it.

## 3. Why mixed strategies are necessary

FACT (matching pennies). Payoff matrix A = [[1, -1], [-1, 1]]: row wins 1 on a match, loses 1 on a
mismatch. For any pure strategy row commits to, the column player holds row to -1. So the pure-
strategy maximin is -1, and the pure-strategy minimax is +1: strict inequality, no saddle point in
pure strategies.

FACT. The mixed strategy x* = y* = (1/2, 1/2) equalizes both columns (and rows): expected payoff of
either pure strategy against it is 0. So the row player guarantees 0, the column player caps row at
0, and v = 0. The pair is the unique equilibrium of matching pennies.

FACT. Rock-paper-scissors: 3 x 3 zero-sum matrix with +1 wins, -1 losses, 0 ties on the diagonal.
Again no pure saddle point. The uniform mix x* = y* = (1/3, 1/3, 1/3) is the unique equilibrium with
value 0.

INTERPRETATION. These examples show the failure mode of pure strategies: whenever one player's
action can be exploited if known, determinism leaks information, and the only way to be
unexploitable is to randomize so the opponent's best response is a tie. Mixed strategies are not a
convenience; they are what makes the max-min and min-max sides meet. The equalization principle
visible here (an optimal mix makes the opponent indifferent among its support) is structural, not
coincidental; it reappears as complementary slackness in the LP formulation below.

## 4. Proof families

FACT. (a) Separating hyperplane proof, the Ville and von Neumann tradition. Suppose min_y max_x x^T
A y > c for some c, i.e., for every y there is a row i with (A y)_i > c. Consider the convex set C =
{A y : y in Delta_n} in R^m and the open convex set D = {z : z_i < c for all i}. They are disjoint
by assumption, so a separating hyperplane theorem (Farkas-type, or Hahn-Banach in finite dimensions)
gives a nonzero p >= 0 with p^T z < c p^T 1 <= p^T A y for all z in D, y in Delta_n. Normalizing p
to a probability vector x yields min_j (A^T x)_j >= c. Ville gave this elementary proof in 1938; it
is the ancestry of the modern LP argument.

FACT. (b) Brouwer fixed point proof. Define the best-response correction map on Delta_m x Delta_n by
increasing the weight on strategies that beat the current payoff and decreasing it on those that do
not, then renormalize. The map is continuous from a compact convex set to itself, so Brouwer gives a
fixed point, and at a fixed point no strategy can be strictly profitable, which yields the saddle
point. von Neumann's original 1928 proof used a fixed-point argument of this flavor (via his own
intersection lemma, essentially equivalent in strength to Brouwer).

FACT. (c) Kakutani fixed point generalization. Kakutani's theorem (1941) extends Brouwer to upper
hemicontinuous, convex-valued correspondences on compact convex sets. The best-response
correspondence BR(x, y) = argmax_x' x'^T A y x argmin_y' x^T A y' is convex-valued and upper
hemicontinuous, so it has a fixed point, which is a saddle point. This is exactly the machinery Nash
used: his 1950 proof (PNAS) applied Kakutani to the best-response correspondence of a general
n-player game to get existence of equilibrium points.

FACT. (d) LP duality proof. The row player's problem max_x min_j (A^T x)_j is a linear program:
maximize t subject to (A^T x)_j >= t for all j, x >= 0, sum x_i = 1. Its dual is the column player's
problem: minimize s subject to (A y)_i <= s for all i, y >= 0, sum y_j = 1. Strong LP duality gives
t* = s*, which is the minimax theorem. Conversely, any LP can be encoded as a zero-sum game (Dantzig
1951, and the Adler 2013 note on the equivalence), so minimax and strong duality are mathematically
equivalent theorems, not merely analogous.

INTERPRETATION. The most common modern textbook proof is the LP duality proof. Reasons: it is short,
it is constructive (the simplex method or interior point methods actually compute x*, y*, and v),
and it slots into the standard curriculum where LP duality is already on the table. The separating
hyperplane proof is the conceptual core (LP duality is itself proved by separation), and the fixed
point proofs matter because they generalize to nonlinear and n-player settings where LP does not
reach.

## 5. Relationship to Nash equilibrium

FACT. A Nash equilibrium of the two-player zero-sum game (A, -A) is a pair (x*, y*) where each
player best-responds: x*^T A y* >= x^T A y* for all x, and x*^T A y* <= x*^T A y for all y. This is
exactly the saddle point condition. So minimax equilibrium in a two-person zero-sum game is a
special case of Nash equilibrium, and conversely every Nash equilibrium of a two-person zero-sum
game is a minimax saddle point. All equilibria of such a game give the same payoff v and the set of
equilibria is convex (a product of convex sets).

FACT (verified live this session). Nash published "Equilibrium points in n-person games" in PNAS 36
(1950), 48-49, a one-page existence announcement using Kakutani's fixed point theorem, and "Non-
cooperative games" in Annals of Mathematics 54 (1951), 286-295, the full paper, which gives a self-
contained proof using Brouwer's fixed point theorem. The 1951 paper explicitly covers the two-person
zero-sum case as the von Neumann minimax theory.

FACT / INTERPRETATION. For non-zero-sum games, minimax no longer characterizes rational play. Three
things change. (i) No single value: each player has its own security level, and there is no common
number the game is "worth". (ii) Multiple equilibria with different payoffs: coordination games,
battle of the sexes, and chicken have several equilibria that are not interchangeable, unlike zero-
sum saddle points. (iii) Minimax strategies can be irrational: playing your security strategy
against an opponent who is not adversarial (or who is playing a cooperative equilibrium) can
sacrifice payoff for no reason. In prisoner's dilemma ([[prisoners-dilemma-anatomy]]) the unique
Nash equilibrium (defect, defect) is also each player's minimax strategy, but the minimax value is
strictly worse than the cooperative payoff, which is precisely the dilemma.

## 6. Computational complexity

FACT. Solving a two-person zero-sum matrix game is polynomial-time solvable: the game is a linear
program with O(m + n) variables and constraints, and interior point methods solve LPs in polynomial
time (Khachiyan 1979 for LP in P, Karmarkar 1984 for practical polynomial interior point). The
minimax value and optimal mixed strategies are therefore computable in polynomial time.

FACT (verified live this session). Finding a Nash equilibrium in general games is PPAD-complete.
Daskalakis, Goldberg, and Papadimitriou, "The complexity of computing a Nash equilibrium", STOC 2006
(38th ACM Symposium on Theory of Computing), journal version SIAM Journal on Computing 39(1),
195-259, 2009: PPAD-complete for three or more players. Chen and Deng, FOCS 2006, extended hardness
to two-player games (also SIAM J. Comput. 2009). PPAD was defined by Papadimitriou (JCSS 1994) to
capture problems whose totality is guaranteed by a parity-argument fixed point proof, exactly the
class Nash falls into because of the Brouwer proof.

INTERPRETATION. Where minimax sits in this landscape: zero-sum equilibrium is in P (via LP), general
Nash is PPAD-complete. The boundary is sharp. Two-player zero-sum and two-player general-sum are
separated by exactly the strong-duality structure: in zero-sum games the best-response conditions
collapse to one LP, while in general-sum games the two players' best-response conditions form a
linear complementarity problem (the Lemke-Howson structure) that is PPAD-complete. Minimax is the
tractable island inside the intractable sea of equilibrium computation.

## 7. Generalizations

FACT. von Neumann's 1937 generalization ("Uber ein okonomisches Gleichungssystem und eine
Verallgemeinerung des Brouwerschen Fixpunktsatzes", Ergebnisse eines mathematischen Kolloquiums 8,
73-83) extended fixed point methods to prove an equilibrium theorem for an expanding economy model;
it contained an implicit generalization of Brouwer toward the Kakutani theorem and a minimax-type
duality for growth rates.

FACT. Fan's minimax theorem (Ky Fan, 1953, "Minimax theorems", PNAS 39, 42-47): minimax equality
holds for functions on products of convex sets that are concavelike-convexlike (a purely algebraic
condition weaker than concave-convex), without full linearity. Fan's proof uses the separating
hyperplane method.

FACT (verified live this session). Sion's minimax theorem (Maurice Sion, "On general minimax
theorems", Pacific Journal of Mathematics 8(1), 171-176, 1958): if M, N are convex compact spaces
(one compact suffices, by Sion's corollary) and f on M x N is quasi-concave in the first variable,
quasi-convex in the second, upper semicontinuous in the first and lower semicontinuous in the
second, then sup inf f = inf sup f. Sion's paper unifies the separation-based (Kneser, Fan) and
fixed-point-based (Nikaido) streams; his proof avoids both and instead uses the Knaster-Kuratowski-
Mazurkiewicz theorem (a consequence of Sperner's lemma). Sion's theorem is the standard general-
purpose minimax cited in analysis and optimization.

BACKGROUND. Parthasarathy and Raghavan (Some Topics in Two-Person Games, 1971) studied games with
special structure: games where one player has a single pure strategy (which admit exact solution via
the minimax structure), completely mixed games (all optimal strategies fully mixed, with explicit
formulas via the inverse of the payoff matrix), and ordered-field property results showing solutions
stay in the field of the payoff entries. Their line of work characterizes when minimax solutions
have closed form and rational values.

## 8. Infinite games and determinacy

FACT. Minimax can fail when strategy spaces are non-compact or payoffs discontinuous. Sion's own
counterexample (1958): M = N = [0,1], f = 0 when (mu < 1/2 and nu = 0) or (mu >= 1/2 and nu = 1), f
= 1 otherwise. This f is quasi-concave-convex and lower semicontinuous in nu, but not upper
semicontinuous in mu at 1/2, and sup inf f = 0 while inf sup f = 1. Dropping compactness breaks
equality too: with M = N = the natural numbers and f(i, j) = sign(i - j), sup inf = -1 and inf sup =
+1.

FACT. For infinite games of perfect information played in turns on trees (players alternate
choosing, a play is an infinite sequence, payoff is win or lose by membership in a payoff set A),
the relevant statement is determinacy: one of the two players has a winning strategy. Gale and
Stewart (1953, "Infinite games with perfect information", Contributions to the Theory of Games II,
Annals of Mathematics Study 28) introduced these games, proved open games are determined, and showed
(using the axiom of choice) that non-determined games exist.

FACT (verified live this session). Martin's Borel determinacy (Donald A. Martin, "Borel
determinacy", Annals of Mathematics 102(2), 363-371, 1975): every Gale-Stewart game whose payoff set
is a Borel set of plays is determined. The proof reduces Borel games to open games through
transfinite iteration and provably requires the axiom of replacement (Friedman had shown determinacy
is unprovable in Zermelo set theory). Martin and Steel (1989) later proved projective determinacy
from large cardinals, and Borel determinacy implies the determinacy of all infinite games in L(R)
under suitable large cardinal assumptions (Martin-Steel-Woodin).

INTERPRETATION. Determinacy results are a far extension of minimax, not a direct generalization:
they concern win-or-lose, perfect-information, infinitely long games, where determinacy says the
win-lose "value" exists (one side can force a win) rather than a saddle point of a real-valued
payoff. The structural kinship is that both assert a max-min equals min-max statement about
adversarial play, and both require hypotheses on regularity (compactness and semicontinuity on one
side, Borel or projective definability on the other) to exclude pathological counterexamples. The
axiom of choice kills both: it manufactures non-determined games and non-measurable payoff functions
alike.



## 9. Where the mapping breaks

* The pure-strategy maximin and minimax can differ strictly (matching pennies: -1 versus +1); the theorem only holds once strategies are convexified by randomization. Any application of minimax reasoning to settings where randomization is impossible or meaningless should be flagged.
* Sion's own counterexample shows the equality fails when semicontinuity fails, and the naturals-with-sign payoff example shows it fails without compactness: the theorem's hypotheses are tight.
* Determinacy results (Gale-Stewart, Martin) are kin, not generalizations: they concern win-lose perfect-information infinite games and require definability hypotheses; the axiom of choice manufactures counterexamples on both sides.
* The LP-duality proof, though the modern textbook standard, reaches only the bilinear finite case; nonlinear or n-player generalizations still route through fixed points.

## 10. Compression points for synthesis

1. Theorem (von Neumann 1928): for every finite two-person zero-sum game with payoff matrix A, max over x in Delta_m of min over y in Delta_n of x^T A y equals min over y max over x; the common value v is the game's value, attained by optimal mixed strategies forming a saddle point.
2. Mixed strategies are not a convenience but the object that makes the equality possible: matching pennies has no pure saddle point (maximin -1, minimax +1) and a unique mixed equilibrium at (1/2, 1/2) with value 0.
3. Four proof families: separating hyperplane (Ville 1938, the conceptual core), Brouwer fixed point (von Neumann 1928 flavor), Kakutani correspondence fixed point (1941, enabling Nash 1950), and LP duality (Dantzig and Gale-Kuhn-Tucker 1951, the modern textbook standard because it is short and constructive).
4. Minimax and LP strong duality are mathematically equivalent theorems, not merely analogous: each reduces to the other.
5. Zero-sum minimax equilibrium is a special case of Nash equilibrium; in non-zero-sum games there is no single value, equilibria multiply, and minimax play can be irrational against non-adversarial opponents (the prisoner's dilemma's dilemma in one line: the minimax strategy is defect, and its value is worse than cooperation).
6. Complexity boundary is sharp: two-player zero-sum equilibrium is in P via LP; general Nash is PPAD-complete (Daskalakis-Goldberg-Papadimitriou 2006/2009; Chen-Deng 2006 for two players). Minimax is the tractable island.
7. Sion 1958 (Pacific Journal of Mathematics 8(1):171 to 176, verified) is the standard general form: quasiconcave-quasiconvex, one-sided compactness, semicontinuity; Fan 1953 handles concavelike-convexlike structure.
8. Far extension: Martin's Borel determinacy (Annals of Mathematics 102(2):363 to 371, 1975, verified) shows every Gale-Stewart game with Borel payoff set is determined, provably requiring the axiom of replacement.

---

## Sources

### Verified live this session

- Nash, "Non-Cooperative Games", Annals of Mathematics 54 (1951), 286-295; received October 11, 1950; cites "Equilibrium Points in N-Person Games", PNAS 36 (1950), 48-49. Confirmed via publisher page and full-text PDF: https://www.degruyterbrill.com/document/doi/10.1515/9781400829156-008/html and https://sites.math.rutgers.edu/~zeilberg/akherim/PokerPapers/nash1951.pdf
- Daskalakis, Goldberg, Papadimitriou, "The Complexity of Computing a Nash Equilibrium", STOC 2006 conference version, journal version SIAM Journal on Computing (2009); PPAD-complete for 3+ players, with Chen-Deng FOCS 2006 settling 2 players. Confirmed via SIAM abstract: https://epubs.siam.org/doi/10.1137/070699652 and https://people.csail.mit.edu/costis/simplified.pdf
- Sion, "On general minimax theorems", Pacific Journal of Mathematics 8(1), 171-176, 1958. Confirmed via publisher page and full text: https://msp.org/pjm/1958/8-1/p14.xhtml and https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-8/issue-1/On-general-minimax-theorems/pjm/1103040253.full
- Martin, "Borel determinacy", Annals of Mathematics 102(2), 363-371, 1975. Confirmed via publisher page: https://annals.math.princeton.edu/1975/102-2/p06 and https://www1.cmc.edu/pages/faculty/MONeill/math188/papers/martin1.pdf

### Established record cited but not re-verified (verify before direct quotation)

- von Neumann, "Zur Theorie der Gesellschaftsspiele", Mathematische Annalen 100 (1928), 295-320.
- Ville, "Sur la theorie generale des jeux ou intervient l'habilete des joueurs", in Borel et al., Traite du calcul des probabilites et de ses applications (1938).
- von Neumann, "Uber ein okonomisches Gleichungssystem...", Ergebnisse eines mathematischen Kolloquiums 8 (1937), 73-83.
- Kakutani, "A generalization of Brouwer's fixed point theorem", Duke Mathematical Journal 8 (1941), 457-459.
- Fan, "Minimax theorems", PNAS 39 (1953), 42-47.
- Kneser, "Sur un theoreme fondamental de la theorie des jeux", Comptes Rendus 234 (1952), 2418-2420.
- Gale and Stewart, "Infinite games with perfect information", Contributions to the Theory of Games II, Annals of Mathematics Study 28 (1953), 245-266.
- Parthasarathy and Raghavan, Some Topics in Two-Person Games, Elsevier (1971).
- Khachiyan, "A polynomial algorithm in linear programming", Soviet Mathematics Doklady 20 (1979), 191-194.
- Karmarkar, "A new polynomial-time algorithm for linear programming", Combinatorica 4 (1984), 373-395.
- Chen and Deng, "Settling the complexity of computing two-player Nash equilibria", FOCS 2006; SIAM J. Comput. 38 (2009).
- Papadimitriou, "On the complexity of the parity argument and other inefficient proofs of existence", JCSS 48 (1994), 498-532.
- Dantzig, "A proof of the equivalence of the programming problem and the game problem", in Koopmans (ed.), Activity Analysis of Production and Allocation (1951).
- Adler, "The equivalence of linear programs and zero-sum games", International Journal of Game Theory 42 (2013), 165-177.
- Martin and Steel, "A proof of projective determinacy", Journal of the AMS 2 (1989), 71-125.
- Friedman, "Higher set theory and mathematical practice", Annals of Mathematical Logic 2 (1971), 325-357.
