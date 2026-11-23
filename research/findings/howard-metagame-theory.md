---
title: "Howard's Metagame: Intentions as Strategies"
tags: [finding, game-theory, cooperation, mechanism-design, coordination]
related:
- prisoners-dilemma-anatomy
- iterated-prisoners-dilemma-axelrod-tournaments
- prisoners-dilemma-psychology-coordination
- nash-equilibrium-foundations
- multi-agent-coordination-patterns
- principal-agent-theory
- protocols-coordination-institutional-design
- poundstone-prisoners-dilemma-quotations
source: research/raw/howard-metagame-theory.md
ingested: 2026-11-23
---
# Howard's Metagame: Intentions as Strategies

## Key Points

**The construction.** A metagame augments a game by letting each player choose among conditional strategies: a policy that specifies what the player will do in response to every strategy the opponent might pick. The unit of choice becomes an intention rather than an action. The metagame then takes the Nash equilibria of this enlarged game, and among them are outcomes that maximize joint payoff — which is how it is said to dissolve the prisoner's dilemma rather than restate it. It is a game about the game, the same construction by which a metalanguage is a language about a language.

**The concrete build, from Shubik's 1969 Cowles paper.** Give the second player four conditional strategies (play 1 regardless; coordinate-contingent; anti-coordinate-contingent; play 2 regardless); the first player then has sixteen, written as strings like 1111, 1112, 1121. A 16 x 4 matrix results with three equilibria, two jointly optimal and the old (0, 0). The four strategies split into "inner-directed" (1 and 4) and "other-directed" (2 and 3): strategy 2 states an intent to coordinate, strategy 3 an intent to avoid coordination. Shubik's one-sentence characterization: the metagame is "an attempt to build complete plausibility for a restricted set of intents." Higher regressions add nothing, which is why the name is earned: one level of remove suffices.

**It enlarges the model rather than proving a new theorem.** Shubik's summary: the resolution "came about through the enlarging of the model rather than the invocation of new mathematical properties of the original model." Where Poundstone writes that "fundamentally, game theory is about abstract problems of maximization" (p. 225), Howard's move accepts the maximizing frame and adds a layer of intentions rather than rejecting the maximizing player.

**The lineage, four levers to the same cooperation-without-enforcer end.** Howard (1966, 1971): choose an intention over a contingency plan. Hofstadter's superrationality (Metamagical Themas, 1985): reason symmetrically with a twin. Tennenholtz's program equilibrium (Games and Economic Behavior 49(2):363-373, 2004), where each player submits a program and "in a program equilibrium of the one-shot prisoners dilemma mutual cooperation is obtained." Bacharach's team reasoning (Beyond Individual Choice, 2006): reason as a team. The metagame is the weakest of the four in its assumptions (it needs only that both players choose contingency plans) and, correspondingly, the least determinate in result.

**It is not the iterated game.** The repeated-play resolution appears in Shubik's same paper as a separate solution and needs no intentions at all, only the shadow of future retaliation. The metagame reaches cooperation in the one-shot game by changing the unit of choice. Same destination, opposite mechanism — repetition versus reframing — which is why it earns a node beside [[iterated-prisoners-dilemma-axelrod-tournaments]].

**Reception, reported plainly.** Metagame theory was largely ignored by mainstream economics and game theory. Rapoport called it "the resolution" of the prisoner's dilemma; Shubik, an insider, recorded his own dissent in the same breath, calling it "mathematically interesting" but no general resolution and ranking it as needing "an additional socio-psychological assumption." Its afterlife ran through political science, operational analysis, and policing, ending in Howard and Bennett's confrontation analysis for "operations other than war." The name survives in a different, informal sense (a strategy layer) that descends from competitive gaming, not from Howard.

**Where it breaks.** It does not select a unique solution (Shubik's own count is three equilibria); "conditional on the other's strategy" is well defined only under complete information and a defined choice order; it leans on a socio-psychological assumption that players treat intentions, not just payoffs, as the thing to respond to; and it presupposes a common-knowledge rationality that the dilemma's own statement is often used to question. Against the Substrate's material, the honest limit is that the metagame is a reframing device, not a mechanism: it dissolves the one-shot dilemma by asking players to choose jointly optimal intentions, which is close to assuming the cooperation it claims to derive.

## Open Questions

- The contents of Howard 1971 (its worked examples and any crisis applications) and of Howard and Bennett 1999 could not be read; no page-level claim is made from either.
- Whether the metagame was reviewed in any economics journal, and with what verdict, was not located.
- The precise provenance of the "Tit-for-tat"/"Tat-for-tit" labels in Brams's textbook metagame figure is a teaching gloss, not verified as Howard's own vocabulary.

## Source

`research/raw/howard-metagame-theory.md` (Shubik's Cowles Foundation Discussion Paper No. 274, 1969, section 3.3, read in full text; Poundstone anchors via the operator's transcription). It sits beside the paradox it claims to dissolve in [[prisoners-dilemma-anatomy]], the other escape route in [[iterated-prisoners-dilemma-axelrod-tournaments]], the equilibrium concept it departs from in [[nash-equilibrium-foundations]], and the informal use of "meta-game" for a different thing in [[prisoners-dilemma-psychology-coordination]]. The usable extract for the Substrate is the primitive, not the puzzle solution: choosing an intention over an action, and making intentions of the coordinate-versus-avoid kind explicit before play, is a coordination device that recurs wherever an agent commits to a policy rather than a single call. See [[multi-agent-coordination-patterns]], [[principal-agent-theory]], and [[protocols-coordination-institutional-design]].
