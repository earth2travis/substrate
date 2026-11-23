---
title: "The Dollar Auction: Shubik's Paradigm for Escalation"
tags: [finding, game-theory, escalation, sunk-cost, mechanism-design, economics, psychology]
related:
- poundstone-prisoners-dilemma-quotations
- poundstone-prisoners-dilemma-book
- largest-number-game-all-pay-auctions
- prisoners-dilemma-anatomy
- principal-agent-theory
- multi-agent-coordination-patterns
- faustian-bargain-prisoners-dilemma-crypto-ai
- protocols-coordination-institutional-design
source: research/raw/dollar-auction-escalation.md
ingested: 2026-11-23
---
# The Dollar Auction: Shubik's Paradigm for Escalation

## Key Points

**The game.** A dollar bill is auctioned so that the highest bidder pays their bid and receives the dollar, and the second-highest bidder also pays their bid and receives nothing. Both leaders lose once bidding passes a dollar; the promoter profits. Each marginal bid above the prize is individually defensible and collectively ruinous, and "the only conceivable reason to keep bidding is to reduce a certain loss." Shubik's citation is firm: "The Dollar Auction Game: A Paradox in Noncooperative Behavior and Escalation," Journal of Conflict Resolution 15(1), March 1971, pp. 109-111.

**Shubik framed it as a paradox of rules and social psychology, not of a payoff matrix.** He presents it first as a parlour game, notes that selling a dollar for three to five dollars "is not uncommon," and says its play "appears to depend upon virtually only the social-psychology of the players." He distinguishes it from the prisoner's dilemma on exactly this ground: the auction "is even simpler... where at least the concept of a 2 x 2 payoff matrix must be taught." His own formal analysis is deliberately thin: a trivial equilibrium, a "max-min the difference" damage-exchange-rate reading with no upper bound, and the verdict that there is "no neat game theoretic solution" and the model alone "does not appear to be adequate."

**The engine is communication.** With credible precommitment a first bid of five cents would end the game; without it the only signal is the bid itself ("put your money where your mouth is"), and bidders cannot state contingent intentions. Shubik is explicit that the generalization to nations is "useful only in a limited manner" because international negotiation has signals and quasi-commitment the parlour game strips out.

**The experimental and organizational record.** Teger, Too Much Invested to Quit (Pergamon, 1980), is the book-length laboratory study, in which pairs played the auction and bidding regularly passed the prize's value. Staw, "Knee-deep in the Big Muddy" (Organizational Behavior and Human Performance 16(1):27-44, 1976), names escalating commitment and tests it as a business-investment simulation; Arkes and Blumer, "The Psychology of Sunk Cost" (OBHDP 35(1):124-140, 1985), isolates the sunk-cost component; Brockner 1992 is the later consolidation.

**The entrapment stack.** Loss framing replaces gain framing past the prize's value (the "look of realization" when the two top bids exceed a dollar); prior bids are unrecoverable and the second bidder's stake is a sunk loss further bidding appears to reduce; the person responsible for the earlier choice is most driven to defend it; there is no stopping rule ("no obvious place to draw the line between a rational bid and an irrational one"); communication is stripped to the bare bid; and "the player with more money, even a penny more, can always outbid the other." The inversion is the sharp lesson: "If the player who ends the escalation is the more 'rational' one, the dollar auction penalizes rationality."

**Where it turns up.** Strikes ("Strikes that threaten to ruin both labor and management have much in common with the dollar auction"); the Vietnam war, which Shubik recognized as an "exquisite example" but not an inspiration; the Concorde-fallacy capital project; and, on-chain, priority gas auctions, where each round's bid is sunk, only the top placement captures the value, and the total paid can exceed the value extracted.

**Where the mapping breaks.** The auction is a demonstration of escalation, not a solved model; the rationality framing fails because the stopping point, not the outcome, is what is chosen; the "two bidders, one prize" simplification hides a profiting third party (Shubik's own formalization is three-person, with an auctioneer); real escalation has commitment technology the parlour game removes; the two bidders are unrealistically symmetric; and the auction penalizes whichever side is more rational.

## Open Questions

- Whether Shubik circulated the game before 1971 (a 1960s working paper or RAND-adjacent document) is unverified; the game as a party game clearly predates the paper but is not dated.
- Teger 1980's experimental design (pairs, prize sizes, increments, feeling measures) was not read; the publisher blurb and one secondary reference are the basis.
- The derivation of Poundstone's "the 'rational' first bid would be 72 cents" (p. 269) is unrecorded and does not align with the 5-cent increment, so it should not be presented as Shubik's own figure.

## Source

`research/raw/dollar-auction-escalation.md` (Shubik 1971 read in full text from a course PDF; Poundstone anchors from the operator's transcription). Its nearest well-studied relatives are enumerated in [[largest-number-game-all-pay-auctions]], its neighbouring escalation structure in [[prisoners-dilemma-anatomy]] (chicken, brinkmanship), and its live market instance in [[faustian-bargain-prisoners-dilemma-crypto-ai]]. For the Substrate's own operating context it is the cleanest formalization of sunk-cost escalation available: an agent with no stopping rule and no credible commitment is not playing a game with a rational solution, it is running the auction. See also [[principal-agent-theory]] (entrapment as a commitment and monitoring problem), [[multi-agent-coordination-patterns]] (agents that can bid, retry, or reinvest without a stopping rule), and [[protocols-coordination-institutional-design]] (the auction's pathology belongs to its payment rule).
