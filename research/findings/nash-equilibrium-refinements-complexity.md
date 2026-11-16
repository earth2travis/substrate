---
title: "Nash Equilibrium: Refinements, Complexity, and the Behavioral Critique"
tags: [finding, game-theory, complexity, behavioral-economics, decision-theory]
related:
- nash-equilibrium-foundations
- minimax-theorem-statement-proofs
- prisoners-dilemma-psychology-coordination
- ziebart-maxent-irl-alignment-conscience
source: research/raw/nash-equilibrium.md
ingested: 2026-11-16
---
# Nash Equilibrium: Refinements, Complexity, and the Behavioral Critique

## Key Points

**Non-uniqueness is the norm, refinements are the patch.** Multiple equilibria are common (coordination games, Battle of the Sexes, chicken). For generic finite games the number of equilibria is odd (Harsanyi 1973). Some equilibria rest on non-credible threats off the equilibrium path. Selten's subgame perfection (1965) eliminates those; trembling-hand perfection (1975, IJGT 4(1):25-55) requires robustness to arbitrarily small strategy perturbations. Harsanyi (1967-68) extends equilibrium to incomplete information via Bayesian type spaces. The 1994 Nobel split the credit along exactly these lines: Nash foundations, Selten dynamics, Harsanyi incomplete information.

**Computing Nash is PPAD-complete.** Daskalakis-Goldberg-Papadimitriou proved PPAD-hardness for 3+ player games (STOC 2006; SICOMP 39(1):195-259, 2009); Chen and Deng (FOCS 2006) extended it to two players. PPAD (Papadimitriou 1994) captures total search problems whose existence proofs rest on parity/end-of-the-line arguments, the same structure underlying Sperner's lemma and Brouwer fixed points. Nash computation is not believed NP-complete: the problem is total, so NP-hardness would imply an unlikely collapse. This is the sharp boundary described in [[minimax-theorem-statement-proofs]]: two-player zero-sum is in P via LP; general-sum is PPAD-complete.

**The intractability result is a foundational critique, not an engineering footnote.** The authors state it explicitly: "An equilibrium concept should be efficiently computable if it is to be taken seriously as a prediction of what a group of agents will do... if computing a particular kind of equilibrium is an intractable problem, it is ludicrous to expect that it can be arrived at in real life." Even idealized perfectly rational agents with unbounded deliberation could not, in general, find an equilibrium faster than exhaustive search in the worst case. The concept's justification must come from dynamics (learning, evolution, adjustment), not static calculation.

**People do not play Nash.** The laboratory record is systematic:
- Beauty contest (Nagel 1995, AER 85(5):1313-1326, verified): unique equilibrium is all-play-0 for p<1, but first-period means ran 24-40 across parameterizations, no subject chose 0, and choices cluster around iteration steps 1 and 2 (roughly 50% of first-period play), consistent with bounded depth of reasoning. Convergence toward equilibrium over four rounds is partial: even in round 4, only 3 of 48 subjects in p=1/2 sessions chose 0.
- Ultimatum game: proposers offer well above the subgame-perfect minimal split; responders reject positive offers.
- Public goods: contributions start positive despite free-riding being dominant, decaying with repetition.
- Centipede (McKelvey and Palfrey 1992): subjects do not take at the first node as backward induction requires.

**The behavioral literature relocates Nash rather than refuting it.** Simon's satisficing (1955-56) and Kahneman's dual-process account (System 1 default, equilibrium reasoning as rare System 2 activity) explain the deviations. Quantal response equilibrium (McKelvey and Palfrey 1995, GEB 10(1):6-38, verified) models noisy best response with a logit precision parameter interpolating from uniform random play to Nash; it systematically outperforms Nash on lab data. Level-k and cognitive hierarchy models (Nagel 1995; Stahl and Wilson 1994; Camerer, Ho, Chong 2004) find populations dominated by level-1 and level-2 reasoners, not equilibrium players. Nash predicts where experienced adaptive populations end up more reliably than where naive individuals start. This parallels the rationality-assumption failure documented in [[ziebart-maxent-irl-alignment-conscience]] and the cooperation psychology in [[prisoners-dilemma-psychology-coordination]].

**The theory's two deepest problems are one problem.** People don't play Nash; computers can't find it. Both are faces of the same gap between equilibrium as a fixed point and equilibrium as a process. The mass-action interpretation from [[nash-equilibrium-foundations]] is the only reading that survives both critiques.

## Open Questions

- PPAD-completeness is worst-case: two-player zero-sum, potential games, and structured game classes remain tractable. The result bounds generality, not applicability.
- The behavioral critique may overstate: deviations often move in the direction Nash predicts over repetition (beauty contest choices converge toward 0; public goods contributions decay). Nash as model of experienced populations coexists with Nash as failure for naive individuals.

## Source

`research/raw/nash-equilibrium.md` (sections 4, 5, 7; compression points 5-6). Daskalakis-Goldberg-Papadimitriou survey and SICOMP abstract, Chen-Deng 2006, Nagel 1995 full text, McKelvey-Palfrey 1995, Selten 1975 citation, all verified in the raw file.
