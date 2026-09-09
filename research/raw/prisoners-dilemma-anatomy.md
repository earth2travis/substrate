# The Prisoner's Dilemma: Anatomy of an Archetypal Game

Raw research file. Part 1 of 4 in a deep-dive series on the prisoner's dilemma. This file covers the game itself: origin, payoff structure, formal properties, the 2x2 game family, economic applications, and the unraveling of finite repetition. It is source material for later synthesis, not a finished essay.

Stance: report what the theory says, report what the record shows, mark the boundary between them. FACT tags apply to claims verified live this session (URL kept in Sources); BACKGROUND marks established record not re-verified; INTERPRETATION marks analytic connections.

Series: prisoners-dilemma-anatomy.md (this file), iterated-prisoners-dilemma-axelrod-tournaments.md, prisoners-dilemma-psychology-coordination.md, faustian-bargain-prisoners-dilemma-crypto-ai.md.

Related Substrate nodes: [[principal-agent-theory]] (contracts that change payoffs), [[multi-agent-coordination]] (the n-player generalization), [[protocols-coordination]], [[erc-8004-trustless-agents]] (reputation infrastructure for agent players).

---

## 1. Origin: RAND, 1950

The game was born experimental, not axiomatic.

- [FACT] The puzzle was designed in 1950 by Merrill Flood and Melvin Dresher during their work at the RAND Corporation.
- [FACT] Flood and Dresher ran an early experiment inviting economist Armen Alchian and mathematician John D. Williams to play one hundred rounds; the players often chose to cooperate rather than follow one-shot defection logic.
- [FACT] John Nash, asked about the results, remarked that rational behavior in the iterated version can differ from the single-round version, an observation that anticipated the folk theorem: cooperation can emerge in repeated interaction even where it is irrational one-shot.
- [FACT] Albert W. Tucker named the game the "prisoner's dilemma" by framing the payoffs as prison sentences (per Poundstone 1993, pp. 8, 117). The standard story: two gang members arrested, held incommunicado, insufficient evidence for the principal charge. Each gets 1 year on the lesser charge if both stay silent; a defector testifying against a silent partner goes free while the partner serves 3 years; if both testify, both serve 2 years.
- [BACKGROUND] RAND in 1950 was the epicenter of early game theory: von Neumann and Morgenstern's Theory of Games and Economic Behavior (1944) was six years old, and Nash's equilibrium paper appeared the same year. The Flood-Dresher experiments were among the first empirical tests of game-theoretic prediction against actual human play. Tucker was Nash's PhD advisor at Princeton; the prison-sentence framing was devised for a psychology department seminar to make the abstract payoff structure concrete.
- [INTERPRETATION] The origin story matters structurally: the gap between the theory's prediction (defect) and the observed behavior (Alchian and Williams cooperated often) is the founding anomaly the entire iterated-game literature grew to explain. The dilemma was a failed prediction before it was a theory.

---

## 2. The payoff structure: T > R > P > S

Canonical generalized form (each player chooses Cooperate or Defect):

|          | C       | D       |
|----------|---------|---------|
| **C**    | R, R    | S, T    |
| **D**    | T, S    | P, P    |

- [FACT] The defining inequality for a strong-sense prisoner's dilemma is T > R > P > S: Temptation (defecting against a cooperator) beats Reward (mutual cooperation), which beats Punishment (mutual defection), which beats the Sucker's payoff (cooperating against a defector).
- [FACT] R > P encodes that mutual cooperation beats mutual defection (the collective-interest clause). T > R and P > S together make defection the dominant strategy: whatever the opponent does, defecting pays more.
- [FACT] For the iterated version, the additional condition 2R > T + S is imposed so that alternating cooperation/defection cannot out-pay steady mutual cooperation. If T + S > 2R, two players could collude to take turns exploiting each other and each average more than R per round; the condition closes that loophole.

Why each inequality matters, one line each [FACT]:

- T > R: the temptation to cheat a cooperator exists; without it, no dilemma.
- R > P: the dilemma is nontrivial; cooperation is genuinely socially better.
- P > S: defecting is also the best reply to defection; without it you have a coordination game instead.
- R > (T+S)/2: the iterated form cannot be gamed by turn-taking exploitation.

[BACKGROUND] Common parameterizations: T=5, R=3, P=1, S=0 is the standard textbook payoff set, used by Axelrod in his tournaments. Check: T+S=5 < 2R=6, so the iterated condition holds. The Poundstone sentence version maps to T=0 (go free), R=-1, P=-2, S=-3 in years served, sign-flipped.

[INTERPRETATION] The four-letter scheme is a compression of an ordinal structure: only the ordering (plus 2R > T+S) is essential. Any affine rescaling preserves the game. The PD is therefore an equivalence class of matrices, which is why it appears so promiscuously across domains: any situation whose ordinal incentives match is "a prisoner's dilemma." The Operator's interest in rewards, punishments, temptations, and sucker's payoffs is an interest in the four corners of this table; every institution in the series is a technology for moving one of them.

---

## 3. Formal analysis: dominance, equilibrium, inefficiency

- [FACT] Defection strictly dominates cooperation for both players: against C, T > R; against D, P > S. Each player's best response is D regardless of the other's move.
- [FACT] Mutual defection (D, D) is the unique Nash equilibrium, and it is strict: each player does strictly worse by deviating unilaterally.
- [FACT] The equilibrium is Pareto inefficient: (C, C) would make both players strictly better off than (D, D), since R > P. The collectively optimal outcome is unreachable by unilateral self-interest.
- [BACKGROUND] This is the canonical demonstration that Nash equilibrium and Pareto optimality are orthogonal concepts. The PD has no mixed-strategy subtleties since dominance is strict. The game's tension is exactly the gap T - R (private gain from cheating) versus R - P (social loss from mutual defection). Because dominance is independent of beliefs, the result needs no common-knowledge-of-rationality machinery beyond one step.
- [INTERPRETATION] The PD is the minimal formal object in which "rational" and "good" diverge. Every institutional design problem (contract theory, mechanism design, collective action) is downstream of this two-line proof. The Substrate's [[principal-agent-theory]] node lives here: an optimal contract, per that file's treatment of Ross, "should align the agent's incentives with the principal's objectives," which in PD language means rewriting the matrix until the dominant strategy stops being self-defeating.

---

## 4. The family of 2x2 games

[BACKGROUND throughout this section; ordering conventions per standard texts, Rapoport & Guyer's 1966 taxonomy of 78 ordinal 2x2 games.]

Permuting the T/R/P/S ordering generates the classic menagerie:

- **Chicken (hawk-dove):** T > R > S > P. Mutual defection (both escalate: the head-on collision) is now the worst outcome, worse than being the sucker who swerves. No dominant strategy; two pure asymmetric equilibria (one swerves, one doesn't) plus a mixed equilibrium. The logic flips from "defection always wins" to "whoever commits first wins, but joint stubbornness is catastrophic." Models: nuclear brinkmanship (the Cuban missile crisis is the textbook case), lane-merging, labor strikes, auction wars.
- **Stag hunt:** R > T > P > S. Mutual cooperation (hunt the stag together) is best for both, but cooperation requires trusting the other; unilateral cooperation while the partner chases the safe hare leaves you with S. Two pure equilibria: (C,C) payoff-dominant and (D,D) risk-dominant. A coordination game about trust, not temptation. Models: Rousseau's stag hunt parable, bank runs, technology standard adoption, team production.
- **Battle of the sexes:** asymmetric payoffs; both players prefer coordinating on the same venue over miscoordinating, but disagree on which venue. Two pure equilibria with a fairness problem. Models: standard-setting with divergent preferences, any coordination-with-conflict situation.
- **Deadlock:** T > P > R > S (or variants where P > R). Mutual defection is both the dominant-strategy equilibrium and the Pareto optimum; there is no dilemma at all. Useful as the contrast case showing what makes PD special.

[INTERPRETATION] The PD is one vertex of a small combinatorial space. The taxonomy shows "the logic of a game" is entirely a function of ordinal payoff structure: move P above S and you get chicken's brinkmanship; move R above T and you get stag hunt's trust problem; drop R below P and the dilemma evaporates into deadlock. The payoff-order table is the load-bearing artifact, not any particular matrix of numbers.

---

## 5. Economic and social applications

- **Cartels and oligopoly.** [FACT] Without enforceable agreements, cartel members face a multiplayer PD: "cooperating" means holding the agreed price floor, "defecting" means undercutting it and instantly taking business from the others; antitrust authorities therefore want members to mutually defect, delivering the lowest prices to consumers. [BACKGROUND] OPEC is the standard example: quota agreements repeatedly collapse under cheating incentives, with Saudi Arabia historically acting as swing producer to discipline defectors; the 1986 price collapse and recurring quota violations fit the PD-with-enforcement-attempts pattern.
- **Price wars.** [BACKGROUND] Bertrand-style duopoly is a continuous-action PD: undercutting is always tempting, mutual undercutting drives price toward marginal cost, both firms earn less than under tacit collusion. Repeated interaction plus trigger strategies is the standard model of tacit collusion, hence antitrust's focus on facilitating practices.
- **Advertising.** [FACT] Cigarette advertising is a cited real example: rival manufacturers' ads largely canceled each other, raising costs without moving market share; firms would jointly prefer to advertise less, and notably endorsed the legal ban on cigarette advertising as an escape from the dilemma. (Nuance: because best spend depends on the rival's spend, it lacks a strict dominant strategy and is only PD-like.)
- **Arms races and the security dilemma.** [FACT] International relations theory uses the PD to show why cooperation fails under anarchy even when jointly optimal: one state's security-increasing measures provoke matching escalation by others, producing an outcome no party desires, worst when offense and defense are indistinguishable and offense has the advantage. [BACKGROUND] The Cold War nuclear buildup is the canonical application: both superpowers spent trillions to restore a relative position that disarmament would have delivered for free. Critics of realism counter that iteration and the shadow of the future restore cooperation incentives.
- **Tragedy of the commons as n-player PD.** [BACKGROUND] Hardin's 1968 pasture parable is the multiplayer generalization: each herder's dominant move is to add cattle (private gain T, shared cost spread over all), and universal defection degrades the commons though universal restraint would be better. Climate change is the current canonical instance, with a caveat: payoff uncertainty makes climate worse than PD, since the value of cooperation is unknown.
- **Public goods games.** [BACKGROUND] The linear public goods game (contribute or free-ride; contributions multiplied and shared) is the experimental economics workhorse n-player PD: free riding strictly dominates, universal free riding is the unique equilibrium, universal contribution is Pareto optimal. Lab experiments show contribution rates starting around 40-60% of endowment and decaying with repetition; peer punishment sustains cooperation (Fehr & Gächter 2000; see the psychology file in this series).
- **Doping in sports.** [FACT] If neither athlete dopes, neither gains an edge; if only one dopes, that athlete gains a large advantage net of health and legal risk; if both dope, the benefits cancel and only the dangers remain, leaving both worse off than if neither had doped.
- **Free riding.** [BACKGROUND] The generic mechanism unifying the above: any setting with individually appropriate benefits and socially diffuse costs (union membership, herd immunity, team production, open-source contribution) instantiates PD incentives at n-player scale.
- [INTERPRETATION] All applications share one signature: a dominant individual strategy whose universal adoption is collectively self-defeating. The practical corollary: every working solution (cartel enforcement, arms treaties, drug testing, Ostrom's commons governance) changes the game rather than exhorting virtue. Monitoring, sanctions, iteration, or communication convert PD into an assurance or coordination game. This is the design lesson the whole series keeps returning to.

---

## 6. One-shot vs. repeated: the unraveling argument

- [FACT] If the iterated PD is played a known finite number of times, the unique subgame-perfect outcome is defection in every round. The proof is inductive: on the last round there is no future retaliation to fear, so defection dominates; with the last round's outcome fixed, the second-to-last round is strategically terminal, so defection dominates there too; the argument unrolls to round one.
- [BACKGROUND] This is the chain-store paradox pattern (Selten 1978): a monopolist facing finite sequential entrants cannot credibly sustain a predatory reputation, because backward induction unravels deterrence in the final market and therefore in every market. Same skeleton: a finite horizon plus a final-round dominance argument destroys the cooperation equilibrium. The endgame effect is its empirical shadow: cooperation in finite lab and field settings decays sharply as the known final round approaches.
- [FACT] Cooperation between rational players requires the horizon to be unknown or infinite; Aumann showed in 1959 that rational players interacting indefinitely can sustain cooperation, an early statement of what became the folk theorem. Nash's remark on the Flood-Dresher experiment anticipated it.
- [BACKGROUND] The folk theorem in modern form: in infinitely repeated games with sufficiently patient players (discount factor near 1), any feasible individually rational payoff, including full cooperation, can be sustained as an equilibrium by trigger strategies (grim trigger: cooperate until the first defection, then defect forever). The discount factor is the formal shadow of the future: cooperation is sustainable when R/(1-δ) beats the one-shot gain T plus the punishment stream, i.e. when δ ≥ (T-R)/(T-P).
- [FACT] In a 2019 American Economic Review study of real subjects in iterated PD with perfect monitoring, the modal strategies were always-defect, tit-for-tat, and grim trigger, with the choice depending on game parameters.
- [INTERPRETATION] The unraveling argument shows the shadow of the future is doing all the cooperative work. Institutions (repeat business, reputation systems, treaties with no sunset clause, tenure, marriage) are technologies for lengthening that shadow. Axelrod's discount-factor framing gives a measurable design target: to sustain cooperation in any PD-like system, either raise δ (make the relationship durable), raise the detection probability of defection (monitoring), or shrink T - R (lower the spoils of cheating). Real governance mixes all three.

---

## 7. Where the mapping breaks

- The PD is an ordinal skeleton. Real situations carry cardinal information (how much bigger is T than R?), risk attitudes, and non-monetary payoffs (status, guilt, identity) that the matrix discards. The psychology file in this series shows humans systematically import payoffs the matrix omits.
- Dominance reasoning assumes the other player's move is causally independent of yours. Superrationality and evidential decision theory dispute this for symmetric reasoners; see the Faust/crypto/AI file.
- The "PD is everywhere" move over-applies. Many situations labeled PD are actually stag hunts (trust problems, no dominant strategy) or chicken (brinkmanship). Misdiagnosing the game prescribes the wrong fix: enforcement helps PD, but can destroy stag hunt cooperation by signaling distrust.
- Backward induction unraveling is a theorem about idealized players with common knowledge of rationality and a known end. It fails descriptively in nearly every lab setting ever run; its value is diagnostic (why institutions hide end dates), not predictive.
- The one-shot game's prediction (universal defection) is the most famously failed prediction in experimental social science. The theory is not wrong about the game; it is wrong about which game humans think they are playing.

---

## 8. Compression points for synthesis

1. The prisoner's dilemma was designed by Merrill Flood and Melvin Dresher at RAND in 1950 and named by Albert W. Tucker, who reframed the payoffs as prison sentences. [FACT]
2. Flood and Dresher's first experiment (Alchian vs. Williams, 100 rounds) produced frequent cooperation, contradicting one-shot theory; Nash's comment that iterated rationality differs anticipated the folk theorem. [FACT]
3. The game is fully defined by the ordinal condition T > R > P > S plus, for iterated play, 2R > T + S; any matrix with that structure is a PD. [FACT]
4. T > R creates the temptation to cheat, R > P makes cooperation socially superior, P > S makes defection the best reply to defection, and 2R > T + S blocks turn-taking exploitation. [FACT]
5. Defection strictly dominates in the one-shot game; mutual defection is the unique strict Nash equilibrium and is Pareto inefficient. [FACT]
6. The standard parameterization is T=5, R=3, P=1, S=0 (Axelrod's tournament payoffs). [BACKGROUND]
7. Permuting the payoff ordering generates the other classic 2x2 games: chicken (T>R>S>P, brinkmanship), stag hunt (R>T>P>S, trust), battle of the sexes (asymmetric coordination), deadlock (P>R, no dilemma). [BACKGROUND]
8. Cartels, price wars, arms races, doping, commons tragedies, and public goods games share one signature: a dominant individual strategy whose universal adoption is collectively self-defeating. [FACT/BACKGROUND per section 5]
9. In any finitely repeated PD with a known end, backward induction unravels cooperation completely: defection in every round is the unique equilibrium; same logic as Selten's chain-store paradox; empirically visible as the endgame effect. [FACT for PD claim; BACKGROUND for linkage]
10. Cooperation requires an unknown or infinite horizon: Aumann 1959, the folk theorem, and the sustainability condition δ ≥ (T-R)/(T-P). [FACT for Aumann; BACKGROUND for formula]
11. Working solutions to PD-structured problems never rely on exhortation: they change the game via monitoring, sanctions, iteration, or communication. [INTERPRETATION]

---

## Sources

Verified live this session:

- Wikipedia, "Prisoner's dilemma" (fetched 2026-09-09). Origin story, payoff structure, formal analysis, applications, finite repetition, Aumann 1959, 2019 AER study, Axelrod summary. Primary anchor for all FACT tags in this file. https://en.wikipedia.org/wiki/Prisoner%27s_dilemma

Established record cited but not re-verified this session (verify before direct quotation):

- Poundstone, Prisoner's Dilemma (1993), pp. 8, 117 (Tucker naming; story formulation).
- Rapoport & Guyer, "A Taxonomy of 2x2 Games" (1966).
- Hardin, "The Tragedy of the Commons," Science (1968).
- Selten, "The Chain Store Paradox" (1978).
- Axelrod, The Evolution of Cooperation (1984), tournament payoff values.
- Fehr & Gächter, public goods punishment experiments (2000-2002).
