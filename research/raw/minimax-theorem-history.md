# Minimax Theorem: Mathematical History

The minimax theorem is the founding result of game theory. It states that in a finite two-person zero-sum game, there exists a value V and mixed strategies for both players such that the maximizing player can guarantee at least V and the minimizing player can guarantee at most V. Formally: max over x of min over y of f(x, y) equals min over y of max over x of f(x, y), where x and y range over mixed strategy simplices. This brief traces the mathematical lineage of that result, from its prehistory in Borel through von Neumann's 1928 proof, the fixed-point reformulations of the 1930s and 1940s, and the postwar algebraic and analytic generalizations.

Related nodes: [[prisoners-dilemma-anatomy]], [[ziebart-alignment-agent]]

## Prehistory: Borel and the Search for an Optimal Method of Play

Emile Borel opened the mathematical study of games in a series of notes beginning in 1921 ("La theorie du jeu et les equations integrales a noyau symetrique", Comptes rendus de l'Academie des Sciences, translated by Leonard Savage in Econometrica 1953). Borel defined the symmetric normal form game and the notion of a "methode de jeu" (method of play), and asked whether an optimal method must always exist. He found optimal mixed strategies for 2 by 2 and 3 by 3 cases, but conjectured, incorrectly, that for larger games the maximin and minimax need not coincide. The question sat open. Maurice Frechet later claimed priority for Borel in a 1953 Econometrica note, prompting a public priority dispute with von Neumann, who answered in the same journal that Borel had posed the problem but had not proved the theorem and had in fact conjectured against it.

## 1928: von Neumann's Proof

John von Neumann, then a Privatdozent in Berlin, proved the theorem in "Zur Theorie der Gesellschaftsspiele" (Mathematische Annalen 100, 1928, pp. 295 to 320). The paper lays out the full architecture of the theory: the extensive form of a game, the reduction to normal form via pure strategies, mixed strategies as probability distributions, and the theorem that every finite two-person zero-sum game has a value in mixed strategies.

The 1928 proof is long and non-elementary. Von Neumann's route went through what he called the function f(x, y) and a property he labeled (K), requiring that the upper level sets in one variable and lower level sets in the other be convex. As the historian Tinne Hoff Kjeldsen established in "John von Neumann's Conception of the Minimax Theorem" (Archive for History of Exact Sciences, 2001), this means von Neumann actually proved the theorem for what we now call quasiconcave-quasiconvex functions, a strictly more general result than the bilinear payoff case he is usually credited with. The standard attribution of only the bilinear case comes from the presentation in the 1944 book with Morgenstern, where the minimax theorem appears in Section 17.6 for bilinear forms.

The 1928 paper was untranslated into English for decades. A translation by Sonya Bargmann, "On the Theory of Games of Strategy", appeared in 1959 in Contributions to the Theory of Games, volume 4, edited by Tucker and Luce (Princeton University Press). The short announcement note was translated by Ben-El-Mechaiekh and Dimand in the International Game Theory Review (2010).

Von Neumann regarded the theorem as the load-bearing piece of the entire subject. In a 1953 letter to Frechet he wrote: "As far as I can see, there could be no theory of games on these bases without that theorem. I thought there was nothing worth publishing until the minimax theorem was proved."

## 1937: The Fixed-Point Turn

Von Neumann returned to the minimax idea in "Uber ein okonomisches Gleichungssystem und eine Verallgemeinerung des Brouwerschen Fixpunktsatzes" (Ergebnisse eines Mathematischen Kolloquiums 8, 1937, translated by Morgenstern as "A Model of General Economic Equilibrium", Review of Economic Studies 13, 1945 to 1946). There he proved a generalization of Brouwer's fixed-point theorem to a set-valued (multivalued) mapping and used it to establish existence for an expanding economy model. The minimax theorem follows as a consequence. This is historically significant twice over: it recast the saddle-point existence question as a fixed-point existence question, and it supplied the tool that Shizuo Kakutani would sharpen four years later.

## 1941: Kakutani's Fixed-Point Theorem

Shizuo Kakutani published "A generalization of Brouwer's fixed-point theorem" (Duke Mathematical Journal 8, 1941), proving that an upper hemicontinuous correspondence from a compact convex set to itself, with nonempty convex values, has a fixed point. Kakutani's theorem directly implies von Neumann's minimax theorem and intersection lemma. It became the standard existence engine: John Nash used it in 1950 to prove equilibrium existence for general finite games, and Debreu, Arrow, and McKenzie used it to prove existence of general competitive equilibrium. The line of descent is Brouwer (1911), von Neumann (1937), Kakutani (1941), Nash (1950).

## Elementary and Alternative Proofs

The original 1928 proof was widely considered difficult, and a small industry of simplification followed:

- Jean Ville gave the first elementary proof in 1938, in his contribution to Borel's "Traite du calcul des probabilites et de ses applications", using only separating hyperplane arguments.
- Hermann Weyl gave another elementary proof in 1950 ("Elementary proof of a minimax theorem due to von Neumann", in Contributions to the Theory of Games, volume 1).
- George Dantzig's development of linear programming in the late 1940s revealed that every two-person zero-sum game is equivalent to a linear program, and conversely that LP duality and minimax are two faces of the same fact. The 1951 result of Gale, Kuhn, and Tucker tied LP duality rigorously to the minimax theorem.
- Lloyd Shapley and R. N. Snow gave a proof via basic solutions of linear systems (1950).

## Generalizations After 1944

The 1944 book "Theory of Games and Economic Behavior" by von Neumann and Morgenstern presented minimax for bilinear payoffs, and postwar work pushed in two directions.

- Ky Fan proved a minimax theorem for convex-concave-like functions on topological vector spaces in 1952 and 1953, using his own fixed-point theorem (a Kakutani variant).
- M. Shiffman was, per Sion's account, among the first to treat concave-convex functions explicitly.
- Maurice Sion's "On general minimax theorems" (Pacific Journal of Mathematics, 1958) gave the now-standard generalization: the theorem holds for quasiconcave-quasiconvex functions on compact convex sets with a continuity condition, with the striking feature that only one side needs compactness when the function has the right semicontinuity. Sion's theorem is often cited as the definitive general form, though per Kjeldsen its quasiconcave-quasiconvex core was already inside von Neumann's 1928 proof, a fact Sion and his cited predecessors appear to have missed because they read the 1944 book rather than the 1928 paper.
- Later abstract work (Ha, Kneser, Fan-Konig, and the minimax theorems via KKM theory) unified minimax results with intersection lemmas and variational inequalities.

## Why This Matters Downstream

Minimax is the ancestor of every equilibrium existence argument in the Substrate's neighborhood. Nash equilibrium existence (and hence the equilibrium framing in [[prisoners-dilemma-anatomy]]) runs through Kakutani, which runs through von Neumann 1937. The minimax regret criterion and adversarial formulations in learning theory, including the worst-case-reward estimation underlying maximum causal entropy IRL rates discussed in [[ziebart-alignment-agent]], inherit the same saddle-point logic: one player picks a policy, nature or an adversary picks the environment or reward, and the value of the game certifies what the first player can guarantee.

## Key Sources

- von Neumann, J. (1928). "Zur Theorie der Gesellschaftsspiele." Mathematische Annalen 100: 295 to 320. English translation: "On the Theory of Games of Strategy", in Contributions to the Theory of Games, vol. 4, Tucker and Luce eds., Princeton, 1959.
- von Neumann, J. (1937). "Uber ein okonomisches Gleichungssystem und eine Verallgemeinerung des Brouwerschen Fixpunktsatzes." Ergebnisse eines Mathematischen Kolloquiums 8. English translation: "A Model of General Economic Equilibrium", Review of Economic Studies 13 (1945 to 46): 1 to 9.
- Kjeldsen, T. H. (2001). "John von Neumann's Conception of the Minimax Theorem: A Journey Through Different Mathematical Contexts." Archive for History of Exact Sciences 56: 39 to 68.
- Kakutani, S. (1941). "A generalization of Brouwer's fixed-point theorem." Duke Mathematical Journal 8: 457 to 459.
- Sion, M. (1958). "On general minimax theorems." Pacific Journal of Mathematics 8: 171 to 176.
- Ville, J. (1938). "Sur la theorie generale des jeux ou intervient l'habilete des joueurs." In Borel, Traite du calcul des probabilites et de ses applications, vol. 2.
- von Neumann, J. and Morgenstern, O. (1944). Theory of Games and Economic Behavior. Princeton University Press.
- Frechet, M. (1953) and von Neumann, J. (1953). Priority correspondence in Econometrica 21.
- Ben-El-Mechaiekh, H. and Dimand, R. W. (2010). "A Simpler Proof of the Von Neumann Minimax Theorem." International Game Theory Review 12(2): 115 to 137.
