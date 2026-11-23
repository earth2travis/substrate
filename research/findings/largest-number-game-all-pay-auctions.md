---
title: "The Largest-Number Game and the All-Pay Auction Family"
tags: [finding, game-theory, auctions, rent-seeking, escalation, mechanism-design, crypto]
related:
- dollar-auction-escalation
- volunteers-dilemma
- poundstone-prisoners-dilemma-quotations
- protocol-as-coordination
- protocols-coordination-institutional-design
- multi-agent-coordination-patterns
- principal-agent-theory
- crypto-as-agent-infrastructure
- faustian-bargain-prisoners-dilemma-crypto-ai
source: research/raw/largest-number-game-all-pay-auctions.md
ingested: 2026-11-23
---
# The Largest-Number Game and the All-Pay Auction Family

## Key Points

**The largest-number game, and its one independent source outside Poundstone.** Douglas Hofstadter devised it and ran it as the "luring lottery" in Scientific American, June 1983 (reprinted in Metamagical Themas, 1985). The rules: free entry, unlimited entries per person, a single card on which an astronomically large integer may be named, an equal chance per entry, no coordination, and a prize of one million dollars divided by the total number of entries. The intended good outcome is exactly one entry; the actual run produced the over-entry the game predicts (nine players submitted a googol entries, fourteen a googolplex, some filled cards with microscopic nines), so no winner was named. Poundstone presents it as a caricature of escalation: "even one defector can ruin it for everyone" (p. 276), "a hopeless situation" (p. 276), and "almost a mirror image of the volunteer's dilemma" (p. 275).

**The honest structural reading.** The game is best read as a Tullock-family probabilistic rent-seeking lottery with an endogenous prize, not a first-price all-pay auction. The winner is drawn at random in proportion to entries (the imperfectly discriminating branch of Hillman and Riley's 1989 taxonomy), and the prize itself shrinks as aggregate effort grows, which no standard contest models. The all-pay auction is the game's nearest well-studied relative, not its species. What carries across cleanly is the dissipation result and the collective-action shape.

**The all-pay auction family.** In a first-price all-pay auction every player forfeits their bid and only the high bidder wins; with complete information there is no pure-strategy equilibrium, only a unique symmetric mixed equilibrium plus a continuum of asymmetric equilibria, payoff-equivalent but not always revenue-equivalent (Baye, Kovenock, and de Vries, Economic Theory 8(2):291-305, 1996). Rent dissipation: one-prize equilibria dissipate expected rent exactly equal to the prize value; experiments find aggregate overdissipation, the sum of bids exceeding the prize, linked to prize scarcity. The family's reach is wide: rent seeking, R&D and patent races, job-promotion tournaments, and lobbying (Hillman and Riley 1989; Baye, Kovenock, and de Vries 1993).

**The war of attrition is the family's sequential member.** Maynard Smith, "The theory of games and the evolution of animal conflicts" (Journal of Theoretical Biology 47:209-221, 1974), with the mixed ESS by Bishop and Cannings (1978), gives the unique symmetric equilibrium survival function S_i(x) = e^(-x/V_j), zero expected payoff for both. It is the closest formal cousin of the dollar auction: both reward persistence and punish the party who stops.

**In the wild.** Lobbying and political contests (non-refundable influence payments as forfeited bids); R&D and patent races; and blockchains, where priority gas auctions are open-bid first-price auctions that are all-pay because losing searchers still pay gas, and the value is competed away to the block producer as rent. The MEV case is a live escalation, not a static model.

**Where the mapping breaks.** Winner rule (deterministic high bid versus proportional draw), who pays and from where (own budgets versus the common prize pool), the endogenous prize unique to the game, timing (simultaneous one-shot versus sequential), the communication ban as an explicit rule rather than an assumption, and the contamination of the actual Scientific American run by a status motive Poundstone explicitly excludes from a "true" largest-number game. Honest sourcing: outside Poundstone and Hofstadter, the largest-number game has no independent academic literature and no encyclopedia entry.

## Open Questions

- Whether any academic paper analyses the largest-number game or the luring lottery under that name; none was found within budget.
- Tullock 1980's citation details and the precise Tullock contest success function are unverified.
- Whether queueing and congestion games are formally all-pay; named as adjacent, no citation verified.

## Source

`research/raw/largest-number-game-all-pay-auctions.md`. The game and its escalation framing are in [[dollar-auction-escalation]]; the mirror relation is recorded in [[volunteers-dilemma]]; the Poundstone page anchors live in [[poundstone-prisoners-dilemma-quotations]]. The family is the mechanism-design counterpart to [[protocol-as-coordination]] and [[protocols-coordination-institutional-design]]: rent dissipation is what a coordination mechanism is built to prevent. The live instance belongs beside [[faustian-bargain-prisoners-dilemma-crypto-ai]] and [[crypto-as-agent-infrastructure]], and the "agents that can bid without a stopping rule" reading belongs with [[multi-agent-coordination-patterns]] and [[principal-agent-theory]].
