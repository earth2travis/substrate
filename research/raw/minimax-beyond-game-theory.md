# Minimax Beyond Game Theory: Decision Theory, Statistics, and AI

Raw research file. Concept 3 of 4 from a deep-dive series on the minimax theorem produced 2026-11-14. This file covers what the minimax idea became outside game theory: Wald's statistical decision theory, minimax regret, game-playing AI from Shannon to AlphaZero, GANs and adversarial training, minimax lower bounds, and regret-minimizing poker AI. It is source material for later synthesis, not a finished essay.

Stance: FACT tags apply to claims verified live this session; BACKGROUND marks standard textbook or established record not re-verified; INTERPRETATION marks synthesis or judgment. Plain-text math throughout.

Related Substrate nodes: [[2026-06-29-irl-theoretical-foundations]] (uses "minimax" in the statistical lower-bound sense covered in section 6), [[ziebart-alignment-agent]] (maxent IRL as the mirror image: maximum over uncertainty versus minimum over worst cases; see section 8), [[prisoners-dilemma-anatomy]] (the game-theory core these applications inherit), [[minimax-theorem-statement-proofs]] (sibling file: the theorem being applied). Note: "minimax" names at least three distinct objects in the literature, a statistical optimality yardstick, a game-tree search rule, and a saddle-point training objective; this file disambiguates them.

Series: minimax-theorem-history.md, minimax-theorem-statement-proofs.md, minimax-beyond-game-theory.md, minimax-reception-influence-critiques.md

---

## 1. The claim under examination

INTERPRETATION: von Neumann's 1928 theorem left game theory along three independent export routes: Wald converted it into a normative standard for inference (1945 to 1950), Shannon converted it into a search procedure for machines (1950), and the online-learning tradition converted Savage's regret variant into an algorithm design principle (1957 to 2007). Each export changed what the word "minimax" means in its new field. This file traces each route and asks what survives of the original theorem in its descendants.

---

## 2. Wald's statistical decision theory

FACT: Abraham Wald's book "Statistical Decision Functions" (Wiley, 1950) founded statistical decision theory by treating estimation, hypothesis testing, and prediction as instances of a single unified decision problem.

BACKGROUND: The timing matters. Wald wrote during and just after the war years, when game theory (von Neumann and Morgenstern, "Theory of Games and Economic Behavior," 1944) and operations research were being assembled into a general science of rational choice under conflict. Wald had already produced the sequential probability ratio test during wartime consulting work, and the 1950 book generalizes that wartime practice into theory. Statistical decision theory is, in this sense, demobilized game theory: the same mathematics, redirected from adversaries to experiments.

BACKGROUND: In Wald's framework the statistician picks a decision rule delta (a mapping from data to actions), Nature picks a state theta, and the rule is evaluated by a risk function R(theta, delta) = E_theta[L(theta, delta(X))], the expected loss when the true state is theta. Because theta is unknown, a rule cannot be judged by its risk at one point; it must be judged by the whole risk function.

BACKGROUND: A rule delta* is minimax if it minimizes the worst-case risk: delta* = argmin_delta sup_theta R(theta, delta). In words, the minimax rule is the estimator or test with the best worst-case performance over all states of Nature. A rule is admissible if no other rule has risk less than or equal to it everywhere and strictly less somewhere.

BACKGROUND: Two concrete consequences show the framework at work. First, the sample mean is minimax for estimating a normal mean under squared error, a nontrivial theorem whose proof goes through the least favorable prior, an increasingly flat sequence of normals. Second, admissibility can fail dramatically: Stein's 1956 paradox showed the sample mean is inadmissible in dimension three and higher, dominated by shrinkage rules, and the dominating James-Stein estimator is itself not minimax-optimal in the naive sense but strictly better everywhere. Decision theory's vocabulary was built to make such statements precise.

FACT: Wald explicitly modeled statistical decision as a zero-sum two-person game in which the statistician plays against Nature. The framing appears in his foundational papers, notably "Statistical Decision Functions Which Minimize the Maximum Risk" (Annals of Mathematical Statistics, 1945), and pervades the 1950 book: the statistician is the minimizing player choosing a (possibly randomized) decision rule, Nature is the maximizing opponent choosing the state, and the payoff is the risk.

FACT: The complete class theorem, developed by Wald in the 1950 book, states in broad form that all admissible decision rules are Bayes rules or limits of Bayes rules: every rule worth using is Bayes for some prior, so the class of generalized Bayes rules is essentially complete. A corollary used constantly in practice is that, under regularity conditions, the minimax rule is the Bayes rule for the least favorable prior, the prior whose Bayes risk is largest. Proving minimaxity therefore reduces to finding a prior hard enough that its Bayes rule has constant risk.

INTERPRETATION: Wald's move was decisive for the career of minimax outside game theory. It converted von Neumann's 1928 minimax theorem from a statement about parlor games into a general normative standard for inference under ignorance: if you cannot or will not name a prior, evaluate rules by their worst case. The least-favorable-prior characterization also gave statisticians the standard constructive route to minimax rules, the same route later used to prove optimality in nonparametric estimation and, much later, the lower-bound machinery of Section 5.

BACKGROUND: The game-against-Nature framing was never uncontested. Bayesian critics from Savage onward argued that Nature is not adversarial and that worst-case reasoning is pessimistic; the reply, then and now, is that minimax is the only coherent standard when priors are contested, which is precisely the situation in robustness applications.

BACKGROUND: The framework also fixed the vocabulary still in use. A decision rule maps observations to terminal actions; randomization over rules is allowed and often necessary, exactly as mixed strategies are necessary in games; and the minimax value of the statistical game, sup over priors of the Bayes risk, equals the infimum over rules of the maximum risk under mild conditions. This is von Neumann's minimax theorem transported into inference, and it is why "minimax" in statistics is a statement about an exchange of sup and inf, not merely a style of caution.

INTERPRETATION: For the Substrate, Wald is the hinge. Everything after him, from Fano-style lower bounds to Wasserstein DRO to adversarial training, is an attempt to compute, bound, or optimize the same object he defined: the best worst case. The 1950 book is dense reading, but its central compression, one game, one risk function, one saddle, is the template this entire brief elaborates.

## 3. Minimax regret

FACT: Leonard J. Savage introduced the minimax regret criterion in "The Theory of Statistical Decision" (Journal of the American Statistical Association, 1951). Savage defined the regret (or opportunity loss) of an act under a state as the difference between its loss and the loss of the best act available under that state: regret(a, theta) = L(a, theta) - min_a' L(a', theta). The criterion chooses the act that minimizes the maximum regret.

BACKGROUND: Minimax regret differs from Wald's minimax risk in what is compared. Risk compares a rule to an absolute zero of loss; regret compares it to the best achievable performance in each state. The two can select different acts: a rule with uniformly moderate risk can have huge regret in states where an easy near-perfect act exists, while a rule that is best in easy states can be catastrophic in hard ones.

BACKGROUND: Savage himself recanted the criterion in "The Foundations of Statistics" (1954), where his axioms led to subjective expected utility and he showed minimax regret violates some of them (notably independence of irrelevant alternatives). Milnor's 1954 paper "Games Against Nature" axiomatized ten decision criteria under ignorance and showed no single criterion satisfies all reasonable desiderata, which is why minimax risk and minimax regret coexist to this day.

BACKGROUND: Minimax regret re-emerged as the standard robustness criterion in decision-making under deep uncertainty, where probabilities are unavailable or contested. It underlies robust decision making (Lempert, Popper, and Bankes, "Shaping the Next One Hundred Years," RAND, 2003), info-gap decision theory (Ben-Haim), econometric treatment choice under partial identification (Manski, from the 2000s), and much operations research on robust scheduling and facility location. The climate-policy applications are representative: when scenario probabilities are themselves unknowable, planners rank options by the worst regret across scenarios, which yields different, typically more hedged, choices than expected-cost minimization under an assumed distribution.

BACKGROUND: There is also a cautionary literature. Minimax regret can select acts that are stochastically dominated or that sacrifice enormous upside to shave a sliver of worst-case shortfall, and it is sensitive to the act set: adding an irrelevant act can change the recommendation, the property Savage used against it in 1954. Practitioners therefore pair it with scenario stress tests rather than trusting it as a sole criterion.

BACKGROUND: For completeness, two siblings of the criterion deserve mention. Maximin (Wald's rule applied to gains rather than losses) is the pessimist's criterion; Hurwicz's optimism-pessimism index interpolates between best case and worst case with a personal coefficient. Regret occupies the middle ground: pessimistic about missing the best, indifferent to the absolute scale of losses. Which of the three a field adopts is largely a historical accident of which problem arrived first: statistics got risk, planning got regret, and online learning inherited regret because its comparator, the best fixed action in hindsight, is defined relative to the realized sequence.

BACKGROUND: The criterion also migrated into machine decisions directly. In online learning and bandits, "regret" is defined exactly as Savage defined it in 1951, cumulative loss minus the cumulative loss of the best fixed comparator, and the design goal is sublinear regret. Littlestone and Warmuth's weighted majority algorithm, Freund and Schapire's Hedge, and the exponential-weights family are all minimax-regret machines: their guarantees hold against an adversarial sequence of losses, no stochastic model of Nature required.

INTERPRETATION: Regret is the machine-age variant of minimax. Where Wald's worst case guards against an adversarial Nature, regret guards against an aspirational benchmark, the best you could have done. That reformulation is exactly what online learning later needed (Section 6): compare your algorithm to the best fixed action or policy in hindsight, and demand that the gap shrink. The shift from risk to regret is also a shift from guarantees about a model to guarantees about a process, which is why regret, not risk, became the native currency of sequential decision-making.

## 4. Games and AI: the minimax search lineage

FACT: Claude Shannon's "Programming a Computer for Playing Chess" (Philosophical Magazine, 1950) proposed evaluating a game tree by alternating maximizing and minimizing over a static evaluation function, the minimax search scheme, and distinguished brute-force (type A) from selective (type B) search. Alan Turing and Konrad Zuse had sketched similar schemes in the 1940s; Turing's Turochamp (1948, with Champernowne) was the first chess program to be specified, though it ran only by hand simulation.

BACKGROUND: Shannon's paper is doubly foundational because it separates the two questions every game program since has had to answer: what to compute (the minimax value of the tree) and how to approximate it within a time budget (the evaluation function plus the search-depth policy). His estimate of roughly 10^120 chess games, the Shannon number, was a way of arguing that brute force is hopeless and that the type B, selective, direction was where intelligence would have to live. Seventy years later the field converged on exactly that diagnosis, though the selectivity now comes from learned policy networks rather than hand-written quiescence rules.

BACKGROUND: Alpha-beta pruning cuts branches that cannot affect the final minimax value: if a minimizing node has already found a value below what the maximizing ancestor can guarantee elsewhere, its remaining children are irrelevant. The idea circulated in the late 1950s. John McCarthy proposed a version of it during the Dartmouth-era discussions and credited the thought to hearing about a related trick; Arthur Samuel used an equivalent cut in his checkers program; some accounts trace the seed of the idea to early Los Alamos computing culture around the MANIAC chess experiments.

FACT: The first rigorous analysis is Donald Knuth and Ronald Moore, "An Analysis of Alpha-Beta Pruning," Artificial Intelligence 6 (1975), 293-326. They showed that with perfect move ordering alpha-beta examines on the order of b^(d/2) terminal positions at even depth d (versus b^d for full minimax), effectively doubling the searchable depth for the same work, and analyzed the average case under random leaf values.

FACT: Arthur Samuel's checkers player ("Some Studies in Machine Learning Using the Game of Checkers," IBM Journal, 1959) combined minimax search over the game tree with a learned polynomial evaluation function whose coefficients were adjusted by self-play and rote learning, the first working fusion of learning and minimax search. By 1962 a version of the program beat a checkers master, Robert Nealey.

BACKGROUND: Samuel's 1959 design deserves slow reading because it contains the entire future of the field in miniature. The search is minimax with alpha-beta-style cuts; the evaluation is a learned linear combination of board features; the training signal comes from comparing the backed-up search value against the static evaluation, a proto form of bootstrapping. Replace the polynomial with a deep network and the rote learning with gradient descent and you have, in outline, every strong game-playing system built since, from TD-Gammon to AlphaZero. Checkers itself was eventually weakly solved by Schaeffer's Chinook lineage and, definitively, by the 2007 proof that perfect play draws, a result achieved by search and endgame databases rather than by learning.

BACKGROUND: The backgammon lineage runs through Hans Berliner's BKG program, which in 1979 beat the reigning human world champion Luigi Villa 7-1, the first program to defeat a reigning world champion in any board game, and culminated in Gerald Tesauro's TD-Gammon (1992), which replaced hand-crafted evaluation with temporal-difference learning on a neural net plus shallow search and reached strong master level.

FACT: IBM's Deep Blue defeated world chess champion Garry Kasparov 3.5 to 2.5 in a six-game match in May 1997, the first computer match victory over a reigning world champion under standard time controls. Deep Blue was classical minimax taken to hardware scale: alpha-beta search on 480 custom chess chips, a hand-tuned evaluation of roughly 8000 features, and throughput on the order of 200 million positions per second. Kasparov had beaten its predecessor Deep Blue I in 1996, and the 1997 rematch included the famous game-two moment in which the machine declined a perpetual check, a move Kasparov read as deeper than machine play, though later accounts attribute it to a fortuitous quirk of the search.

INTERPRETATION: Deep Blue was both the triumph and the ceiling of classical minimax. Go resisted the approach for two structural reasons: a branching factor near 250 (versus about 35 for chess) makes deep full-width search infeasible, and no reliable static evaluation function for Go was ever found. The counter-tradition that broke Go replaced deep search with sampled search plus learned guidance.

BACKGROUND: Monte Carlo tree search, crystallized in the UCT algorithm of Kocsis and Szepesvari (2006), estimates node values by randomized rollouts rather than by a static evaluation, and balances exploration against exploitation with bandit-style upper-confidence bounds. MCTS is not minimax search: it estimates expected values under the current playout policy rather than exact worst-case values, which is both its weakness (no adversarial guarantee per node) and its strength (it scales where minimax cannot).

FACT: AlphaGo (Silver et al., "Mastering the game of Go with deep neural networks and tree search," Nature 529, 2016) beat European champion Fan Hui in 2015 and Lee Sedol 4-1 in March 2016 by replacing deep minimax search with Monte Carlo tree search guided by policy and value convolutional networks trained on human games and self-play. AlphaZero (2017-2018) generalized the recipe, learning chess and shogi from scratch and defeating Stockfish; guided MCTS thereby displaced classical hand-tuned minimax as the state of the art in large perfect-information games.

INTERPRETATION: The counter-tradition is best read as a change of opponent model, not a rejection of minimax. Classical minimax assumes the opponent plays the worst-case line at every node; MCTS with learned guidance assumes the opponent plays roughly like itself and buys depth through sampling and value approximation. AlphaZero's value head is in effect Samuel's 1959 learned evaluation, retrained by self-play at modern scale, and the search around it still alternates max and min perspectives. The minimax skeleton survived; the brute-force flesh was replaced by learned tissue.

## 5. Adversarial machine learning and GANs

FACT: Goodfellow et al., "Generative Adversarial Nets," NeurIPS (then NIPS) 2014, defines a GAN as a two-player minimax game with value function V(D, G):

  min_G max_D V(D, G) = E_{x ~ p_data}[log D(x)] + E_{z ~ p_z}[log(1 - D(G(z)))].

The discriminator D outputs the probability that x came from the data and maximizes the objective; the generator G minimizes it. In the space of arbitrary functions the game has a unique solution: G recovers the data distribution and D equals 1/2 everywhere.

BACKGROUND: The paper's own framing is explicitly game-theoretic. The authors describe the generator as a team of counterfeiters and the discriminator as the police, note that competition drives both to improve until the fakes are indistinguishable, and prove that the global optimum of the minimax game is exactly the data distribution. The counterfeiters-police metaphor did real work: it made clear that the learning signal for the generator is not a fixed loss landscape but an adaptive opponent, which is why GAN training cannot be reduced to ordinary minimization.

BACKGROUND: In practice GAN training runs simultaneous gradient descent-ascent in parameter space, where the game is not convex-concave and the classical saddle-point guarantees vanish. Observed failure modes are limit cycling (parameters orbit the equilibrium without settling), non-convergence of loss curves, and mode collapse (the generator maps large regions of noise space to a few outputs, winning locally against the current discriminator while covering only part of the data distribution). The loss curves are famously uninformative: a falling discriminator loss can indicate learning or can indicate generator collapse, which is why the field fell back on sample-quality proxies like the inception score and Frechet inception distance.

BACKGROUND: The deep reason cycling appears is geometric. For a bilinear game f(x, y) = x^T A y, simultaneous gradient descent follows dynamics whose Jacobian has purely imaginary eigenvalues at the saddle, so iterates spiral outward or orbit rather than contract. Adding a conservative field (the optimism term, or an extragradient extrapolation step) rotates the dynamics inward. This diagnosis, visible in toy form in Daskalakis et al. and developed across the variational-inequality literature (Gidel et al.; Mokhtari, Ozdaglar, and Pattathil on extragradient), explains why the fix is a one-line change to the update rule and why it cannot come from learning-rate tuning alone.

FACT: Daskalakis, Ilyas, Syrgkanis, and Zeng, "Training GANs with Optimism" (ICLR 2018; arXiv 1711.00141), analyze GAN training as a zero-sum game solved by simultaneous no-regret dynamics. They show that simultaneous gradient descent cycles even in bilinear zero-sum games, while Optimistic Mirror Descent converges in the last iterate for bilinear games, and they introduce Optimistic Adam, which empirically improves Wasserstein GAN training (better KL divergence on synthetic DNA-sequence data, better inception scores on CIFAR10).

BACKGROUND: The broader theoretical literature on minimax optimization in non-convex settings grew rapidly after: local saddle points and their computability, extragradient and optimistic methods for monotone variational inequalities, and negative results showing that even convex-concave simultaneous gradient descent can diverge. The common thread is that the GAN objective made a classical question urgent again: when do the dynamics of a minimax problem actually find its solution?

BACKGROUND: The Wasserstein GAN (Arjovsky, Chintala, and Bottou, 2017) replaced the log-loss discriminator with a critic approximating the earth-mover distance, and it is the Wasserstein variant that Daskalakis et al. analyze, because its value function is closer to the bilinear games where convergence theory is sharpest. The line from the original GAN objective to WGAN to optimistic training is a line of increasingly explicit engagement with the minimax structure rather than an attempt to escape it.

INTERPRETATION: GANs made Wald's game against Nature literal, except Nature is now a learned opponent and the saddle is non-convex. Mode collapse has a crisp game-theoretic reading: it is a non-equilibrium local optimum of sequential play, stable only because the players update myopically rather than solving the game. And the optimism fix has a clean genealogy: it imports into deep learning a result from online learning, that predicting your opponent's next gradient converts cycling into convergence, which is itself a descendant of the regret analysis in Section 6. The GAN training problem and the poker equilibrium problem turned out to be the same problem in different clothing.

## 6. Minimax in modern ML theory

BACKGROUND: Distributionally robust optimization (DRO) optimizes the worst-case expected loss over an ambiguity set U of distributions: min_theta sup_{Q in U} E_Q[loss(theta, x)]. Wasserstein DRO takes U to be a Wasserstein ball around the empirical distribution (Esfahani and Kuhn, Mathematical Programming, 2018; Blanchet and Murthy; surveyed by Rahimian and Mehrotra), which for many losses yields a tractable convex reformulation and, via the dual, a form of norm regularization. DRO is Wald's framework with the ambiguity set replacing Nature's pure strategies, and the radius of the ball playing the role of a prior-free robustness budget. In practice the worst-case distribution concentrates mass on hard examples near the decision boundary, which is why DRO-trained models behave like adversarially trained ones and why group DRO (Sagawa et al., 2020) uses the same template for fairness across subpopulations.

BACKGROUND: Minimax lower bounds are the standard optimality yardstick in mathematical statistics: one shows that no estimator can achieve risk below some rate uniformly over a model class by exhibiting a hard subfamily. The three workhorses: Le Cam's two-point method (lower bound via the total variation distance between two hypotheses), Fano's inequality (lower bound via mutual information over multiple hypotheses), and Assouad's lemma (lower bound via a hypercube of hypotheses, the standard tool for nonparametric rates). This is the sense of "minimax" used in the Substrate's [[2026-06-29-irl-theoretical-foundations]] file, which reports minimax estimation rates for inverse RL: statements that no algorithm can learn a reward function faster than a stated rate, proved in exactly this style.

FACT: Madry, Makelov, Schmidt, Tsipras, and Vladu, "Towards Deep Learning Models Resistant to Adversarial Attacks" (ICLR 2018; arXiv 1706.06083), cast adversarial robustness as a saddle-point problem:

  min_theta E_{(x,y)} [ max_{delta in S} loss(theta, x + delta, y) ].

The inner maximization is the attacker (in their experiments, projected gradient descent within an L-infinity ball); the outer minimization is the defender's training objective. This min-max formulation became the canonical definition of empirical robust training for neural networks.

BACKGROUND: The three workhorse lower-bound techniques differ in the geometry of the hard subfamily. Le Cam's method pits two nearly indistinguishable distributions against each other and converts testing error into estimation error; Fano's inequality handles many hypotheses at once through an information budget; Assouad's lemma decomposes the model into independent binary choices and sums the per-coordinate testing errors. All three are constructive in Wald's sense: they exhibit the least favorable configuration rather than merely asserting it exists, which is why minimax rates in modern statistics are usually stated as matching upper and lower bounds, estimator plus hard family.

INTERPRETATION: In all three uses (DRO, minimax lower bounds, adversarial robustness) minimax plays the role Wald assigned it: a guarantee that survives an unspecified or adversarial opponent. The modern difference is computational explicitness. The inner maximization is either dualized in closed form (Wasserstein DRO), bounded information-theoretically (lower bounds), or approximated by gradient attack (robust training). The 1950s game is now an inner loop.

## 7. Game-playing today: regret and poker

BACKGROUND: Hannan consistency (Hannan, 1957) asks for an online strategy whose average regret against any sequence of outcomes goes to zero. Regret matching (Hart and Mas-Colell, 2000) is a simple Hannan-consistent rule: play each action with probability proportional to its accumulated positive regret. A key folk theorem: in two-player zero-sum games, if both players run no-regret dynamics, their time-averaged strategies converge to a Nash equilibrium, which in a zero-sum game is exactly the minimax solution.

BACKGROUND: Counterfactual regret minimization (CFR; Zinkevich, Johanson, Bowling, and Piccione, NeurIPS 2007) extends regret matching to extensive-form games with imperfect information by decomposing overall regret into per-information-set counterfactual regrets. The key theorem is that the sum of per-information-set regrets upper-bounds the overall regret, so local regret matching at every decision point yields global Hannan consistency, and in self-play the time-averaged strategy profile approaches equilibrium at rate O(1/sqrt(T)). This made equilibrium computation feasible for games with trillions of states, far beyond linear-programming methods, and it is why every top poker AI since 2015 is built on some CFR descendant: CFR+, Monte Carlo CFR, Deep CFR, and the discounted variants.

BACKGROUND: The conceptual through-line from Section 2 to this section is worth stating plainly. Savage's regret was a decision criterion, a way to choose once. Hannan turned it into an asymptotic requirement on a sequence of plays. Hart and Mas-Colell made it a simple update rule. CFR made the rule decomposable across information sets. Each step preserved the minimax destination while shrinking the computational requirement, until the destination, an approximate Nash saddle of a trillion-state game, became reachable on a cluster.

FACT: Bowling, Burch, Johanson, and Tammelin, "Heads-up limit hold'em poker is solved," Science 347 (2015), 145-149, used the CFR+ variant to essentially solve heads-up limit Texas hold'em, the first imperfect-information game played competitively by humans to be solved, with a strategy so close to equilibrium that a lifetime of play could not distinguish it.

FACT: Libratus (Brown and Sandholm, "Superhuman AI for heads-up no-limit poker: Libratus beats top professionals," Science 359, 2018, 418-424) defeated four top professionals over 120,000 hands of heads-up no-limit hold'em in January 2017, using CFR-family self-play for a blueprint strategy plus real-time subgame solving and continual self-improvement. The margin was statistically decisive, about 14.7 big blinds per 100 hands against the pros collectively.

BACKGROUND: No-limit hold'em is the harder game by orders of magnitude: roughly 10^160 decision points versus about 10^13 for the limit variant, which is why Libratus needed the blueprint-plus-search architecture rather than a single solved strategy. The 2017 event, the Brains vs. AI rematch, was the second time the CMU team ran such a contest; the 2015 predecessor Claudico lost, and the two-year gap between losing and winning is a compressed measure of how fast CFR-family engineering was moving.

FACT: Pluribus (Brown and Sandholm, "Superhuman AI for multiplayer poker," Science 365, 2019, 885-890) defeated elite professionals, including Darren Elias and Chris Ferguson, in six-player no-limit hold'em, using Monte Carlo CFR for a blueprint plus a limited-lookahead search. The authors are explicit that the algorithm has no convergence guarantees outside two-player zero-sum games yet produced superhuman multiplayer play.

BACKGROUND: Pluribus also changed the economics of the milestone. Its blueprint was trained in eight days on a 64-core server for an estimated cloud cost under two hundred dollars, and it played live on two CPUs, orders of magnitude cheaper than Deep Blue's custom hardware or AlphaGo's TPU pods. The minimax family had become not just stronger but radically cheaper, because regret-based self-play compresses the game into a strategy rather than re-deriving it move by move.

BACKGROUND: A final clarification on terminology for the Substrate: CFR is "a minimax-family algorithm" in the precise sense that, for two-player zero-sum games, the equilibrium it approximates is the minimax saddle, and its guarantees are regret guarantees of exactly the Savage-Hannan lineage. It is not minimax search: no game tree is ever enumerated. Calling CFR "minimax" is therefore a statement about the destination, not the route.

BACKGROUND: The distinction between blueprint and search matters. CFR-based systems compute a Nash-approximate blueprint strategy offline, then repair it online with limited-lookahead subgame solving, a hybrid that resembles AlphaZero's search-and-value split transplanted to imperfect information. In both lineages, the equilibrium object is a minimax object (in two-player zero-sum games the Nash saddle is the minimax saddle), and the engineering question is how much of it to precompute and how much to resolve at play time.

INTERPRETATION: The poker lineage is the cleanest contemporary demonstration that minimax is an algorithm, not just a bound. Regret, Savage's 1951 quantity, turned out to be the computable path to von Neumann's equilibrium in games with trillions of states where Shannon-style tree search cannot reach. The bridge from Section 2 is direct: minimize regret in self-play, and minimax falls out as the time average. Pluribus also marks the honest edge of the theory: in multiplayer games the minimax guarantee dissolves, and the field proceeds on empirical strength rather than proof, a reversion to engineering judgment that Wald would have recognized and bracketed with caveats.



## 8. Synthesis across domains

INTERPRETATION: Across all six domains, minimax is one idea wearing three costumes. As a norm (Wald, Savage) it says what "best" means when no prior is legitimate. As a search principle (Shannon through Deep Blue) it computes the norm exactly in perfect-information games, until the games grow past full-width search and learned guidance takes over. As an optimization template (GANs, DRO, adversarial training, CFR) it turns the norm into a saddle problem whose dynamics must be engineered to converge. The recurring tension, from Wald's least favorable prior to Optimistic Adam to Pluribus's unproven multiplayer behavior, is that the minimax solution is easy to define and hard to reach. For the Substrate, the file's role is to disambiguate the word: in [[2026-06-29-irl-theoretical-foundations]] "minimax" names a statistical optimality yardstick; in the game-AI literature it names a search rule; in GANs and robust training it names a saddle objective. Same mathematics, different theorems.

INTERPRETATION: Three open seams are worth flagging for future Substrate work. First, the convergence theory for non-convex minimax optimization remains local and fragile; GAN-style problems beyond the bilinear case have no general last-iterate guarantees. Second, multiplayer and general-sum settings, where Pluribus succeeded empirically, lack any minimax-style guarantee, and no one knows whether one can exist. Third, the statistical and algorithmic senses of minimax have never been fully unified: minimax lower bounds tell you what no algorithm can do, while CFR and MCTS tell you what particular algorithms did do, and the gap between the two kinds of statement is where most current research lives.

INTERPRETATION: A closing note for readers arriving from [[ziebart-alignment-agent]]: maxent IRL is the mirror image of this file. Ziebart's principle picks the maximum-entropy distribution subject to constraints, a maximum over uncertainty, while minimax picks the minimum over worst cases. The two meet in the Lagrangian of the maxent problem, whose dual is a minimax game between feature matching and entropy. Alignment-relevant learning theory keeps rediscovering that duality, and this brief is meant to make the pattern legible.

## 9. Where the mapping breaks

* The game-against-Nature framing was never uncontested: Bayesian critics from Savage onward argued Nature is not adversarial and worst-case reasoning is pessimistic; minimax survives as the standard mainly where priors are genuinely contested.
* MCTS is not minimax search: it estimates expected values under the current playout policy rather than exact worst-case values. The AlphaGo lineage displaced classical minimax precisely by abandoning the adversarial guarantee per node.
* GAN training in parameter space is not convex-concave, so the classical saddle-point guarantees vanish: cycling and mode collapse are the observed failure modes, and the fixes (optimism, extragradient) are imports from online learning, not from game theory proper.
* CFR is "a minimax-family algorithm" only about the destination: in two-player zero-sum games the equilibrium it approximates is the minimax saddle, but no game tree is ever enumerated. Pluribus succeeded in multiplayer poker where no minimax guarantee exists; that edge is empirical, not proven.
* The statistical and algorithmic senses of minimax have never been fully unified: lower bounds state what no algorithm can do, while CFR and MCTS state what particular algorithms did do; most current research lives in the gap.

## 10. Compression points for synthesis

1. Wald (Statistical Decision Functions, Wiley 1950; Annals of Mathematical Statistics 1945) explicitly modeled statistics as a zero-sum game against Nature: the minimax rule is argmin over rules of sup over states of risk, and the complete class theorem ties minimax rules to Bayes rules under the least favorable prior.
2. Savage's minimax regret (JASA 1951) compares acts to the best achievable per state, not to absolute loss; Savage recanted it in 1954, and Milnor 1954 showed no decision criterion under ignorance satisfies all desiderata. Regret, not risk, became the native currency of sequential decision-making.
3. The game-AI lineage is Shannon 1950 (minimax search scheme) to Knuth-Moore 1975 (alpha-beta analysis, b^(d/2) effective branching, verified) to Samuel 1959 (learning plus minimax, the template for everything since) to Deep Blue 1997 (classical minimax at hardware scale, both triumph and ceiling) to MCTS/AlphaGo 2016 (Nature 529, verified: learned guidance displaced full-width search).
4. GANs (Goodfellow et al., NeurIPS 2014, verified) are an explicit two-player minimax game whose ideal solution recovers the data distribution; training dynamics fail in non-convex settings, and Daskalakis et al. 2018 (ICLR, verified) show optimistic mirror descent restores last-iterate convergence in the bilinear case.
5. Three modern theory uses all instantiate Wald's guarantee: Wasserstein DRO (worst case over an ambiguity ball), minimax lower bounds (Le Cam, Fano, Assouad; the sense used in the Substrate's IRL file), and Madry et al. 2018 adversarial training (ICLR, verified) as an explicit min-max saddle.
6. The poker lineage: CFR (Zinkevich et al., NeurIPS 2007) decomposes regret across information sets; Bowling et al. solved heads-up limit hold'em (Science 347:145 to 149, 2015, verified); Libratus (2017) and Pluribus (Science 365:885 to 890, 2019, verified) extended to no-limit and multiplayer, with Pluribus's blueprint trained for under two hundred dollars of compute.
7. Disambiguation for the Substrate: "minimax" names a statistical yardstick (Wald), a search rule (Shannon), and a saddle objective (GANs, DRO, robust training). Same mathematics, different theorems.

---

## Sources

### Verified live this session

- Goodfellow et al., "Generative Adversarial Nets," NeurIPS 2014. https://proceedings.neurips.cc/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html
- Madry et al., "Towards Deep Learning Models Resistant to Adversarial Attacks," ICLR 2018. https://arxiv.org/abs/1706.06083 and https://openreview.net/forum?id=rJzIBfZAb
- Bowling et al., "Heads-up limit hold'em poker is solved," Science 347 (2015), 145-149. https://www.science.org/doi/abs/10.1126/science.1259433
- Brown and Sandholm, "Superhuman AI for multiplayer poker" (Pluribus), Science 365 (2019), 885-890. https://pubmed.ncbi.nlm.nih.gov/31296650 and https://noambrown.com/papers/19-Science-Superhuman.pdf
- Knuth and Moore, "An Analysis of Alpha-Beta Pruning," Artificial Intelligence 6 (1975), 293-326. https://www.sciencedirect.com/science/article/pii/0004370275900193
- Daskalakis et al., "Training GANs with Optimism," ICLR 2018. https://arxiv.org/abs/1711.00141 and https://openreview.net/forum?id=SJJySbbAZ

### Established record cited but not re-verified (verify before direct quotation)

- Wald, "Statistical Decision Functions," Wiley, 1950.
- Wald, "Statistical Decision Functions Which Minimize the Maximum Risk," Annals of Mathematical Statistics 16 (1945), 279-303.
- Savage, "The Theory of Statistical Decision," Journal of the American Statistical Association 46 (1951), 55-67.
- Savage, "The Foundations of Statistics," Wiley, 1954.
- Milnor, "Games Against Nature," in Thrall, Coombs, and Davis (eds.), Decision Processes, 1954.
- Shannon, "Programming a Computer for Playing Chess," Philosophical Magazine 41 (1950), 256-275.
- Samuel, "Some Studies in Machine Learning Using the Game of Checkers," IBM Journal of Research and Development 3 (1959), 210-229.
- Berliner, "Computer Backgammon," Scientific American 242 (1980), 64-72.
- Tesauro, "Temporal Difference Learning and TD-Gammon," Communications of the ACM 38 (1995), 58-68.
- Campbell, Hoane, and Hsu, "Deep Blue," Artificial Intelligence 134 (2002), 57-83.
- Silver et al., "Mastering the game of Go with deep neural networks and tree search," Nature 529 (2016), 484-489.
- Silver et al., "A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play" (AlphaZero), Science 362 (2018), 1140-1144.
- Hannan, "Approximation to Bayes risk in repeated play," Contributions to the Theory of Games III, Princeton, 1957.
- Hart and Mas-Colell, "A Simple Adaptive Procedure Leading to Correlated Equilibrium," Econometrica 68 (2000), 1127-1150.
- Zinkevich, Johanson, Bowling, and Piccione, "Regret Minimization in Games with Incomplete Information," NeurIPS 2007.
- Brown and Sandholm, "Superhuman AI for heads-up no-limit poker: Libratus beats top professionals," Science 359 (2018), 418-424.
- Esfahani and Kuhn, "Data-driven distributionally robust optimization using the Wasserstein metric," Mathematical Programming 171 (2018), 115-166.
- Lempert, Popper, and Bankes, "Shaping the Next One Hundred Years: New Methods for Quantitative, Long-Term Policy Analysis," RAND, 2003.
- Le Cam, "Asymptotic Methods in Statistical Decision Theory," Springer, 1986.
- Fano, "Transmission of Information: A Statistical Theory of Communications," MIT Press, 1961.
- Assouad, "Deux remarques sur l'estimation," Comptes Rendus de l'Academie des Sciences Paris 296 (1983), 1021-1024.
- Manski, "Identification for Prediction and Decision," Harvard University Press, 2007.
- Arjovsky, Chintala, and Bottou, "Wasserstein GAN," arXiv 1701.07875 (2017).
