---
title: "The Volunteer's Dilemma: One Volunteer, n-1 Free Riders"
tags: [finding, game-theory, collective-action, coordination, public-goods, psychology]
related:
- prisoners-dilemma-anatomy
- prisoners-dilemma-psychology-coordination
- poundstone-prisoners-dilemma-quotations
- largest-number-game-all-pay-auctions
- principal-agent-theory
- protocols-coordination-institutional-design
- multi-agent-coordination-patterns
source: research/raw/volunteers-dilemma.md
ingested: 2026-11-23
---
# The Volunteer's Dilemma: One Volunteer, n-1 Free Riders

## Key Points

**The structure.** n players; a discrete collective good is produced if and only if at least one player volunteers; a volunteer nets V minus C, every non-volunteer nets V, and if nobody volunteers every player receives 0. The ordinal ranking for each player is free-ride (V), then volunteer (V minus C), then nobody-volunteers (0). Requirements for a dilemma: V greater than C greater than 0 — the volunteer must profit, or it collapses toward a pure sacrifice rather than a self-interested game.

**It is not a prisoner's dilemma.** The prisoner's dilemma turns on a strictly dominant strategy (defect) and a unique deficient equilibrium; the volunteer's dilemma has no dominant strategy at all. Volunteering is better when everyone else defects (it avoids the 0); free-riding is better when someone else will volunteer. The best move depends on expectations of others, which makes it a coordination or anti-coordination problem. Diekmann states it directly: "In contrast to other social traps, a dominant strategy does not exist." The equilibria are the n asymmetric pure profiles of one volunteer and n-1 free riders, plus one mixed symmetric equilibrium that Diekmann found "yields very low payoffs" — no better than maximin. Selecting the volunteer is the coordination problem the theory leaves open.

**The founding paper and its own evidence.** Andreas Diekmann, "Volunteer's Dilemma," Journal of Conflict Resolution 29(4), December 1985, pp. 605-610. The 1985 article is theoretical and reports no experiment; Diekmann's own experimental results are in a 1986 chapter in Paradoxical Effects of Social Behavior whose design and measured group-size effect could not be retrieved. He credits the psychology directly: the all-defect outcome "is frequently produced by 'diffusion of responsibility' as described by Darley and Latane (1968)." The bridge from the game to the bystander literature is his own, not a later graft.

**The group-size prediction, stated three ways.** The robust, parameter-free theoretical claim is only about the individual propensity to volunteer, which falls with group size. The group-level claim (the group's probability of provision falls with n) and the real-world aggregate claim (crowds help less) are both parameterization-dependent and empirically contested, so the slogan should never be stated more strongly than the individual-propensity claim, and even that has counterexamples.

**The empirical record is mixed and cuts both ways.** Goeree, Holt, and Smith (2017) find individual rates falling with larger groups as predicted, but no-volunteer outcomes also declining with group size, contrary to theory. Kopanyi-Peuker (2019), over group sizes 3 to about 100, finds a non-monotonic group-size effect and systematic over-volunteering. A study of remote workers finds volunteering rates flat across team sizes. Przepiorka and Diekmann (2018) find the symmetric effect but its dissolution under heterogeneous costs, where groups "tacitly coordinate on the strong subject." The disagreements track four degrees of freedom the experiments vary independently: one-shot versus repeated, symmetric versus heterogeneous costs, the production function, and correct beliefs about n.

**The corrected bystander record.** The bystander effect itself is real but conditional: Fischer et al. (2011) give g = -0.35 over 105 effect sizes, attenuated for danger, perpetrator presence, and physical cost. The strongest correction is aggregate: Philpot et al. (2020), on 219 real CCTV conflicts, find intervention in about nine of ten, rising with the number of bystanders — which reverses the sign of the naive group-size story at the level victims care about. A falling individual propensity and a more numerous crowd can coexist while the aggregate rises.

**Where it sits and where it breaks.** Palfrey and Rosenthal (1984) supplied the general discrete-threshold public-good game; the volunteer's dilemma is its threshold-equals-one special case. Pamela Oliver's critical-mass program is the heterogeneity counterpart, where larger groups can raise collective action. Indivisibility is load-bearing (an additive good is a different game); symmetric costs are the silent assumption the asymmetric case dissolves; real emergencies are dynamic and ambiguous; repetition is missing from the base model; and real instances usually have a designated volunteer the abstract game lacks.

## Open Questions

- Diekmann's 1986 experimental results (design, sample, measured group-size effect) could not be retrieved; it is the file's key gap, and the question "what did his own experiments find" cannot be answered from the 1985 paper.
- The volume and pages of the Oliver and Marwell critical-mass papers are provisional and should not be cited until checked.

## Source

`research/raw/volunteers-dilemma.md`. Poundstone supplies the naming and network position ("the volunteer's dilemma", p. 201; chicken's anti-coordination property, p. 199; the mirror relation to the largest-number game, p. 275), via [[poundstone-prisoners-dilemma-quotations]]. It is the multiperson anti-coordination branch beside the two-player family in [[prisoners-dilemma-anatomy]] and the human-player record in [[prisoners-dilemma-psychology-coordination]]; its sibling is [[largest-number-game-all-pay-auctions]]. For the Substrate's own work it is the right model for an agent fleet in which one member must spend resources to unblock the rest (take a lock, run the recovery, escalate to the operator): the failure mode is that every member waits, and the institutional fix is a designated volunteer or a cost-sharing rule. See [[principal-agent-theory]], [[protocols-coordination-institutional-design]], and [[multi-agent-coordination-patterns]].
