# The Dollar Auction: Shubik's Escalation Game, Its Experimental Record, and the Psychology of Entrapment

Raw research file. Single-concept deep dive produced 2026-11-23. The concept surfaced while the operator read William Poundstone, Prisoner's Dilemma (1992). This file is scoped to one object, the dollar auction, plus the escalation literature it anchors: the game and its rules, Martin Shubik's own 1971 framing and the origin question, the experimental record (Teger 1980), the organizational literature (Staw 1976, Arkes and Blumer 1985, Brockner 1992), the psychological mechanisms of entrapment, real-world instances, the honest limits of the mapping, and compression points for synthesis. It does not re-derive the prisoner's dilemma formalism, the Axelrod tournaments, dilemma psychology, or the crypto and AI application layer; those live in the sibling files named below. Its primary source is read in full text this session: Shubik's original paper, which is short and available as a direct PDF.

Tag key: [FACT] verified live this session with a URL inline. [BACKGROUND] established record cited but not re-verified here. [INTERPRETATION] analysis. [UNVERIFIED] could not check, with the reason. No citation, date, page number, or quotation below is fabricated.

Related Substrate nodes: [[poundstone-prisoners-dilemma-quotations]] and [[poundstone-prisoners-dilemma-book]] (provenance for every Poundstone page anchor and quotation used here), [[prisoners-dilemma-anatomy]] (chicken and brinkmanship as the neighbouring escalation structure the auction is contrasted against), [[largest-number-game-all-pay-auctions]] (sibling file, which carries the all-pay auction generalisation this file deliberately does not develop), [[principal-agent-theory]] (entrapment read as a commitment and monitoring problem, where a principal cannot cheaply discontinue an agent's sunk course), [[multi-agent-coordination-patterns]] (agents that can bid, retry, or reinvest with no stopping rule), [[faustian-bargain-prisoners-dilemma-crypto-ai]] (priority gas auctions and MEV as a live escalation market), [[protocols-coordination-institutional-design]] (the rules-as-institution point, since the auction's pathology is a property of its payment rule).

Companion files, all committed 2026-11-23: this file, [[howard-metagame-theory]], [[dollar-auction-escalation]], [[largest-number-game-all-pay-auctions]], [[volunteers-dilemma]], with provenance in [[poundstone-prisoners-dilemma-quotations]] and [[poundstone-prisoners-dilemma-book]].

---

## 1. The game and its rules

[FACT] The dollar auction, as Shubik states it, is an auction of a one-dollar bill in which the highest bidder pays their bid and receives the dollar, and the second highest bidder also pays their bid and receives nothing. Shubik: "The auctioneer auctions off a dollar bill to the highest bidder, with the understanding that both the highest bidder and the second highest bidder will pay." (Shubik 1971, https://www.math.utoronto.ca/mpugh/Teaching/Sci199_03/dollar_auction_1.pdf)

[FACT] In Shubik's worked example, bids advance in multiples of five cents, the game ends when no one bids for a set interval, and ties resolve in favor of the bidder closest to the auctioneer. He explicitly declines to add an upper bound: "the analysis is confined to the (possibly infinite) game without a specific termination point." (same)

[FACT] The mechanism of escalation is a switch in what each bidder is choosing. Shubik: at a standing bid of five cents against ten, raising to fifteen "stands to gain 85 cents," while standing pat "will certainly lose 5 cents." The same logic recurs at every stage. Above a bid of a dollar, "both bidders will be losing, but still may escalate their bids in order to cut down on losses." (same)

[FACT] Shubik marks two thresholds. The first is when the sum of the two top bids exceeds a dollar, at which point the auctioneer is guaranteed a profit regardless of outcome, a "critical zone ... passed for the auctioneer." The second and "most spectacular" is the one-dollar barrier, past which the only conceivable reason to keep bidding is to reduce a certain loss. (same)

[FACT] The outcome is a loss for both bidders, not a win for one. Shubik: "Experience with the game has shown that it is possible to 'sell' a dollar bill for considerably more than a dollar. A total of payments between three and five dollars is not uncommon." (same)

[FACT] Shubik describes the game as suited to a crowd and to lowered calculation: "In playing this game, a large crowd is desirable. Furthermore, experience has indicated that the best time is during a party when spirits are high and the propensity to calculate does not settle in until at least two bids have been made." (same)

[FACT] The generalisation, in one line, is that the dollar auction is an all-pay auction in which the losers also pay: all bidders pay what they commit, and the prize goes only to the top bid. The full theory of all-pay auctions is handed to the sibling file [[largest-number-game-all-pay-auctions]] and is not developed here, beyond noting that the auction's pathology belongs to its payment rule rather than to any payoff matrix.

## 2. Shubik's own account, and the framing the later literature drops

[FACT] Shubik presents the game first as a party trick: "There is an extremely simple, highly amusing, and instructive parlor game which can be played at any party by arranging for the auction of a dollar." (same)

[FACT] He describes the play as an arc of moods, which is the part most later summaries omit. Bidding proceeds "fairly briskly" until the two top bids exceed a dollar, "after which a look of realization comes onto the faces of many participants"; there is "a pause and hesitation" at the one-dollar barrier; then "a duel with bursts of speed until tension builds, bidding then slows and finally peters out." (same)

[FACT] Shubik's central claim is that the game is a creature of its rules and its players, not of its payoff structure. "This simple game is a paradigm for escalation. Once the contest has been joined, the odds are that the end will be a disaster to both." And: "The game's play appears to depend upon virtually only the social-psychology of the players, or other unstated factors of the environment in which it is played." (same)

[FACT] He distinguishes it from the prisoner's dilemma on exactly this ground: the auction "is even simpler than the Prisoner's Dilemma, where at least the concept of a 2 x 2 payoff matrix must be taught." (same)

[FACT] Shubik offers a formalisation, treats it as trivial, and says so plainly. He reads the auction as a three-person constant-sum game (auctioneer plus two bidders), gives the characteristic function, and notes a trivial noncooperative equilibrium in which the first bidder opens at $1.00 and no one else bids, "yields a payoff of zero to all." He then adds the "max-min the difference" reading, a damage-exchange-rate view in which bidders care about relative loss: "for the cost of 5 cents, B can inflict damage of $1.00 on A by bidding $1.05. The damage exchange rate is 20 to 1. Unless there is an upper boundary to the bidding, there is no boundary to the escalation in the damage exchange rate." (same)

[FACT] His verdict on the theory is negative: "There is no neat game theoretic solution to apply to the dynamics of the Dollar Auction, or to escalation between two nations in abstracto. The static game theory analysis is trivial, and although of some value, it is not enlightening concerning how to proceed from statics to dynamics." And: "the game theory analysis of the game in extensive form shows us that the game theory model alone does not appear to be adequate." (same)

[FACT] Shubik locates the engine in communication conditions: "The key to the understanding of the processes at work in this game is in communication conditions." If a bidder could precommit publicly, "the first bidder would bid 5 cents and say, 'If anyone else bids, I will immediately bid $1.00 if he bids less; or I will bid 5 cents more than he, if he bids $1.00 or more,'" which if believed would block the others and net 95 cents. Without a commitment mechanism, "we would need to specify the degree of belief of the other bidders." The only communication in the actual game is the bid itself: "a person is required to 'put your money where your mouth is.'" (same)

[FACT] On application he is explicitly modest: "Can we generalize from this formal structure to interorganization fights or internation escalation? Only in a limited manner is the generalization useful. The internation negotiation has communication conditions considerably different from the parlor game. Signals and quasi-commitment are possible and common." He adds that a clear experimental result on the auction "would be of only limited value in understanding escalation between nations," which needs "a specific understanding of the mechanisms for the enforcement of agreement and the meaning of threat." (same)

[INTERPRETATION] Shubik's own paper is more careful than the escalation folklore that grew from it. He says the game is a paradigm for escalation, that it is a parlor game whose dynamics are social-psychological, and that it has no game-theoretic solution and does not generalise cleanly to nations. The later literature, and Poundstone's popular telling, keep the paradigm and drop the hedges.

## 3. The origin question

[FACT] Shubik 1971 is the first published statement of the game and is credited as its origin. Citation: Shubik, Martin, "The Dollar Auction Game: A Paradox in Noncooperative Behavior and Escalation," Journal of Conflict Resolution 15(1), March 1971, pages 109 to 111, DOI 10.1177/002200277101500111. (https://journals.sagepub.com/doi/10.1177/002200277101500111; APA record at https://psycnet.apa.org/record/1972-22907-001 ; the paper's own running head reads "The Journal of Conflict Resolution, Volume 15, Issue 1 (Mar., 1971), 109-111").

[FACT] The chronology is fixed precisely by the paper itself plus the DOI record: first published March 1971, volume 15, issue 1, pages 109 to 111. The paper was researched under National Science Foundation Grant GS-2840, and Shubik was then at the Department of Administrative Sciences, Yale University. (same PDF, footnote 1)

[FACT] A survey of the game states the standard attribution: "Shubik invented the dollar auction in 1971." (https://drpress.org/ojs/index.php/EHSS/article/download/778/711/743) A commentary on the game states: "The first published discussion of the game is in the Journal of Conflict Resolution, March 1971, pp. 109-111." (https://conversableeconomist.com/2011/11/15/martin-shubiks-dollar-auction-game/)

[INTERPRETATION] So the honest answer to the origin question is a split one. Shubik 1971 is the origin of the dollar auction as a published, citable game, and I found no earlier published source for it. But the paper's internal evidence shows the game itself predates the paper: Shubik describes it as a parlor game played at parties, says "experience with the game has shown" that a dollar sells for more than a dollar, and speaks from a track record of play. The game's origin as a party game is therefore earlier than 1971 and unpublishable to a date; the origin of the formalised, named object is Shubik 1971.

[INTERPRETATION] On whether the argument has an earlier source, the defensible line is that the escalation argument has antecedents in the general theory of conflict and bargaining (Schelling's work on credible commitment and brinkmanship is the obvious upstream neighbour, and the RAND milieu of the 1950s to 1960s is where the escalation frame formed) but the dollar auction as a specific game and a specific paradox is Shubik's. Poundstone records Shubik's own testimony that the Vietnam war was an "exquisite example" but not an inspiration, which is consistent with a game that was invented as a parlor paradox and only afterwards read onto real conflict. (Poundstone, p. 264, [FACT] from the operator's transcription)

[UNVERIFIED] Whether Shubik described or played the game in print before 1971, for instance in a 1960s working paper or a RAND-adjacent document. No such earlier item surfaced within the search budget, and the absence is weak evidence at best.

## 4. The experimental record: Teger, Too Much Invested to Quit (1980)

[FACT] The book-length experimental study is Allan I. Teger, Too Much Invested to Quit (Pergamon Press, 1980). Publisher and citation records confirm it, and it is cited roughly 697 times. (https://www.sciencedirect.com/book/9780080229959/too-much-invested-to-quit) The Pergamon edition is ISBN 978-0-08-022995-9, with an e-book ISBN 9781483152226. (https://shop.elsevier.com/books/too-much-invested-to-quit/teger/978-0-08-022995-9)

[FACT] The book's stated scope is the application of escalation paradigms to real conflict, taking "as backdrop issues in marriage" and reaching toward "the resolution of international relations." The publisher's own description notes that "the book also takes a look at real life and the dollar auction." (same two records)

[FACT] The experimental content, per a psychology reference: a program of laboratory studies "in which pairs of participants played the dollar auction and related games, with the bidding regularly passing the value of the prize," and Teger reported "what people actually feel as this happens." (https://psychology.com/biases/irrational-escalation; DOI 10.1016/C2013-0-0364-8 given there as the book DOI)

[FACT] A later experiment using the same game, Costanza 1988, reports the expected threshold result: "Bids over $1 are clearly in excess of the expected return and represent, even for a winning bid, a case of having 'too much invested to quit.'" (https://www.robertcostanza.com/wp-content/uploads/2017/02/1988_J_Costanza_DollarAuctionGame.pdf) [INTERPRETATION] This is the empirical pattern the whole literature rests on, stated as a rent-dissipation result: bids routinely exceed the prize's value.

[BACKGROUND] The exact design details of Teger's studies (number of pairs, prize sizes, bid increments, the feeling measures) are not in hand, since no copy of the book was read this session. The publisher blurb and the secondary reference establish the book, its topic, and its headline finding; they do not let me quote Teger directly.

## 5. The organizational literature: escalation of commitment and sunk cost

[FACT] Barry M. Staw, "Knee-deep in the Big Muddy: A Study of Escalating Commitment to a Chosen Course of Action," Organizational Behavior and Human Performance 16(1), 1976, pages 27 to 44, DOI 10.1016/0030-5073(76)90005-2. (https://www.sciencedirect.com/science/article/abs/pii/0030507376900052; the paper's full text PDF is hosted at https://strategy.sjsu.edu/www.stable/pdf/Staw,%20B%20M,%201976,%20Organizational%20Behavior%20and%20Human%20Performance.%2016%20pp%2027-44.pdf)

[FACT] Staw's method, in his own words: "The research presented here examined this process of escalating commitment through the simulation of a business investment decision." (same PDF) [BACKGROUND] The finding, as the field reads it, is that decision makers who are personally responsible for an earlier allocation of resources to a failing course of action commit further resources to it, and that this is a self-justification effect rather than a calculation about the future.

[FACT] Hal R. Arkes and Catherine Blumer, "The Psychology of Sunk Cost," Organizational Behavior and Human Decision Processes 35(1), February 1985, pages 124 to 140. (https://econpapers.repec.org/RePEc:eee:jobhdp:v:35:y:1985:i:1:p:124-140 ; the article DOI is 10.1016/0749-5978(85)90049-4) [FACT] The paper's abstract and figures page confirm the title, authors, journal, year, and pagination as shown in the ResearchGate record. (https://www.researchgate.net/publication/4812596_The_psychology_of_sunk_cost) [BACKGROUND] The canonical result: people who have paid more for a good (a season ticket, an expensive dinner, a project) use it more or defend it longer, and past costs that cannot be recovered still drive present decisions, which is economically irrational against standard expected-value reasoning.

[BACKGROUND] Joel Brockner, "The Escalation of Commitment to a Failing Course of Action: Toward Theoretical Progress," Academy of Management Review 17(1), 1992, pages 39 to 61. [FACT, weak] The existence and role of the 1992 Brockner escalation paper is confirmed only indirectly here: it is cited alongside Arkes and Blumer 1985 in the current literature as the standard escalation reference ("(Arkes & Blumer 1985; Brockner 1992)"). No abstract or pagination was fetched this session, so the full title and pages are BACKGROUND, not FACT.

[INTERPRETATION] The three organizational sources divide the labour cleanly. Teger runs the auction itself and documents the behaviour and its feel. Staw names and tests the mechanism, escalating commitment driven by responsibility for the prior decision. Arkes and Blumer isolate the sunk-cost component in decision biases across ordinary life. Brockner is the later theoretical consolidation. Together they convert Shubik's parlor paradox into a research programme.

## 6. The psychological mechanisms of entrapment

[INTERPRETATION] The auction entangles its players through a stack of mechanisms that Shubik's paper and the organizational literature name separately.

1. Loss framing replaces gain framing. Below a dollar the bid is a gamble on a 95-cent gain; past a dollar the identical move is a choice between a certain loss and a smaller expected loss. Shubik's own play-by-play is that reversal: the "look of realization" when the two top bids exceed a dollar, and the escalation "in order to cut down on losses." (Shubik 1971) [BACKGROUND] The underlying asymmetry is loss aversion, the finding that losses loom larger than equivalent gains, and that a loss already incurred reshapes the reference point. [FACT] Shubik's "max-min the difference" formalisation is the same idea in game-theoretic dress: bidders switch from maximising absolute payoff to minimising relative loss, "concerned with their relative gains or losses rather than their absolute gains or losses."

2. Sunk cost. Each prior bid is unrecoverable, and the second-highest bidder's stake is a sunk loss that further bidding appears to reduce. [FACT] Arkes and Blumer 1985 is the field's canonical demonstration.

3. Escalating commitment and self-justification. [BACKGROUND] Following Staw 1976, the person who made the earlier choice is the one most driven to defend it, because abandoning it concedes that the earlier choice was wrong. In the auction every bidder is personally responsible for their own prior bid.

4. Irreversibility and the absence of a stopping rule. [FACT] Shubik specifies the game "without a specific termination point" and notes that an upper bound would remove the interesting phenomena. The ruin is that there is no natural line between a rational bid and an irrational one; Poundstone states this directly: "Maybe the problem is that there is no obvious place to draw the line between a rational bid and an irrational one." (p. 262)

5. Anonymity and stripped communication. [FACT] Shubik: the only communication is the bid, "no contingent statement whatsoever," and the crowd bids independently without discussion or agreements. There is no cheap way to commit, so no credible threat can arrest the spiral.

6. The asymmetry that decides it. [FACT, Poundstone] "The player with more money, even a penny more, can always outbid the other if forced to do so." (p. 270) A deeper pocket converts the escalation into a resource war, and the same feature makes the auction look tractable to whoever is richer.

## 7. Real-world instances, with sources

[FACT] Strikes, military labor disputes: "Strikes that threaten to ruin both labor and management have much in common with the dollar auction." (Poundstone, p. 263) [INTERPRETATION] A strike is an all-pay contest in which both sides pay the cost of the stoppage and only one side's terms can prevail, which is the auction's payment rule in a bargaining frame.

[FACT] The Vietnam war: "Shubik recognizes the Vietnam war as an 'exquisite example' of a dollar auction but doesn't recall it being an inspiration for the game." (Poundstone, p. 264) [INTERPRETATION] The reading is retrospective: the game was not built to explain Vietnam, it was recognised as one. This is Shubik's own hedge in the 1971 paper applied to his own example.

[FACT] Escalating conflict in general: "Many conflicts start this way, with a justifiable action that, in retrospect, becomes the first 'defection' in an escalating dilemma." (Poundstone, p. 265) [INTERPRETATION] The first moving party is not the villain; the first bid is defensible, and it is the subsequent structure that turns it into a trap. This is the point at which the dollar auction rejoins the dilemma literature: the first "defection" is a justifiable single move whose iterated consequence is ruin.

[BACKGROUND] Corporate capital projects and the Concorde, the classic sunk-cost case, where states and firms continue funding a failing programme because the money spent is treated as a reason to continue rather than as unrecoverable. The economics literature calls this the Concorde fallacy; Staw 1976 and Arkes and Blumer 1985 are the behavioural foundations.

[BACKGROUND] Auction and market instances. [FACT] A finance-education treatment presents the game as the standard illustration that rational choice leads to irrational outcomes, with bidders going above a dollar. (https://www.investopedia.com/terms/d/dollar-auction.asp) [FACT] John Kay is quoted on the same theme: "In the dollar bill auction, one party eventually scores a pyrrhic victory and takes possession of the dollar bill." (https://conversableeconomist.com/2011/11/15/martin-shubiks-dollar-auction-game/) [INTERPRETATION] The generic modern instances are bidding wars (houses, eBay, spectrum), patent races, litigation, and campaign spending, all structures in which each side's spending is largely sunk and only one can win.

[INTERPRETATION] On-chain escalation markets. [BACKGROUND] Priority gas auctions and maximal extractable value on a congested chain reproduce the auction structurally: searchers bid up a transaction's placement, each round's bid is sunk, only the top placement captures the value, and the total paid can exceed the value extracted. This is treated at length in the sibling file [[faustian-bargain-prisoners-dilemma-crypto-ai]]; the point recorded here is only that the mechanism matches the dollar auction rather than merely resembling it.

## 8. Where the mapping breaks

[INTERPRETATION] Shubik's own paper is the strongest source of the limits, and it should be read first rather than last.

1. The auction is a demonstration of escalation, not a solved model. Shubik states flatly that "there is no neat game theoretic solution" and that "the game theory model alone does not appear to be adequate." The static game analysis he gives is, in his word, "trivial." The canonical object is a paradox with a formalisation bolted on, not a theorem with an application.

2. The rationality framing fails when the stopping point is what is being chosen. The auction does not present a choice among outcomes with known values; it presents a choice about where to stop, and the value of stopping depends on where the other side stops, which is precisely the quantity no one knows. Poundstone lands this: the problem is "that there is no obvious place to draw the line between a rational bid and an irrational one" (p. 262), and the resolution is that "our concept of rationality is not fixed" (p. 277, from the companion transcription). A model that presupposes a fixed rational stopping rule has assumed away the phenomenon.

3. The "two bidders, one prize" simplification hides a profiting third party. Shubik's own formalisation is a three-person game in which the auctioneer is a player, and in the cooperative reading "the auctioneer is at a disadvantage" while in the noncooperative reading "the locus of the disadvantage changes to the bidders." Real escalation usually has no auctioneer collecting the surplus; there is only the two-sided loss.

4. Real escalation has commitment technology; the parlor game does not. Shubik's generalisation is explicitly "useful only in a limited manner" because international negotiation has "signals and quasi-commitment" that the parlor game strips out. The auction is the escalation case with the escape hatches removed, which is why it is a vivid paradigm and a poor direct model.

5. The symmetry of the two bidders is unrealistic. In the auction both players are identical and the only asymmetry is depth of pocket. In real conflicts the parties differ in interests, information, and resolve, and the payoff ranking is not common knowledge. Shubik's own caveat is that absent precommitment "we would need to specify the degree of belief of the other bidders," which is the quantity real cases conceal.

6. The auction penalises whichever side is more calculating. "If the player who ends the escalation is the more 'rational' one, the dollar auction penalizes rationality." (Poundstone, p. 272) This inverts the standard game-theoretic story in which rationality is rewarded, and it means that importing the auction as a normative model of "how to play" gets the prescription backwards: the model says the more rational party is the one who should lose.

7. The bidding is not the choosing. A further honest break: the auction is sometimes cited as if it explained why escalation happens. It does not. It shows that a specific rule set produces escalation under plausible behaviour; it does not identify the cause in any given case, and Shubik assigns the play to "the social-psychology of the players, or other unstated factors." An explanation of a real escalation requires the case-specific history that the game abstracts away.

## 9. Compression points for synthesis

1. The dollar auction is Shubik's game in which the highest bidder pays their bid and wins the dollar while the second highest also pays their bid and wins nothing, so both leaders lose once bidding passes a dollar. The promoter profits; escalating bids are individually defensible and collectively ruinous. [FACT] Shubik 1971, https://www.math.utoronto.ca/mpugh/Teaching/Sci199_03/dollar_auction_1.pdf

2. Shubik's citation is firm: Journal of Conflict Resolution 15(1), March 1971, pages 109 to 111, DOI 10.1177/002200277101500111. [FACT]

3. On origin: Shubik 1971 is the first published source and the credited origin, and no earlier published source was found; but Shubik presents it as a parlor game with a track record, so the game as a party game predates the paper while the named object originates with it. The escalation argument has upstream neighbours in Schelling and the RAND milieu; the auction itself is Shubik's. [INTERPRETATION over FACT]

4. Shubik's own framing is a paradox of rules and social psychology, not of a payoff matrix: play "appears to depend upon virtually only the social-psychology of the players," and the game is "even simpler than the Prisoner's Dilemma, where at least the concept of a 2 x 2 payoff matrix must be taught." [FACT]

5. Shubik states the two thresholds: the auctioneer is safe once the two top bids exceed a dollar, and the one-dollar barrier is where the game turns into a duel over reducing certain losses. Selling a dollar for three to five dollars is "not uncommon." [FACT]

6. Shubik's formal analysis is deliberately thin and negative: a trivial equilibrium, a "max-min the difference" damage-exchange-rate reading with no upper bound, and the verdict that there is "no neat game theoretic solution" and the model alone "does not appear to be adequate." [FACT]

7. Shubik locates the engine in communication: with credible precommitment a first bid of five cents would end the game; without it the only signal is the bid, and the bidders cannot state contingent intentions. [FACT]

8. Teger, Too Much Invested to Quit (Pergamon, 1980), is the book-length experimental study, in which pairs played the auction and the bidding regularly passed the prize's value. Costanza 1988 reports the same threshold: bids over a dollar are "in excess of the expected return." [FACT for the book and the Costanza line; the design details of Teger's studies are BACKGROUND]

9. Staw 1976 ("Knee-deep in the Big Muddy," Organizational Behavior and Human Performance 16(1), 27 to 44) names escalating commitment and tests it as a business-investment simulation; Arkes and Blumer 1985 (OBHDP 35(1), 124 to 140) isolate the sunk-cost effect; Brockner 1992 is the later consolidation. [FACT for Staw and Arkes and Blumer; BACKGROUND for Brockner]

10. The entrapment stack: loss framing replaces gain framing past the prize's value, sunk costs press toward continuation, personal responsibility drives self-justification, there is no stopping rule, communication is stripped to the bare bid, and a deeper pocket can always outlast. [INTERPRETATION grounded in FACT]

11. The auction is an all-pay auction in which losers also pay; the general theory is developed in [[largest-number-game-all-pay-auctions]], and the auction's pathology belongs to its payment rule, not to a payoff matrix. [INTERPRETATION]

12. Poundstone's page-anchored statements: the auction is "a game of escalation and outrageous behavior" (p. 260); the point is to "incorporate addiction in a game" (p. 260); it "leads to a bad case of buyer's remorse" (pp. 261 to 262); "there is no obvious place to draw the line between a rational bid and an irrational one" (p. 262); strikes "have much in common with the dollar auction" (p. 263); Shubik reads Vietnam as an "exquisite example" but not an inspiration (p. 264); conflicts start with "a justifiable action that, in retrospect, becomes the first 'defection'" (p. 265). [FACT, from the operator's transcription]

13. Poundstone's analytic claims: "The 'rational' first bid would be 72 cents" (p. 269); "each bidder is increasingly worse off, but each has incentive to continue in the short term" (p. 269); "the player with more money, even a penny more, can always outbid the other" (p. 270); "the dollar auction penalizes rationality" (p. 272); "it's a matter of personalities, group psychology, and luck, not game theory; rationality has nothing to do with it" (p. 272). [FACT, from the operator's transcription]

14. Where the mapping breaks: the auction is a demonstration of escalation rather than a solved model; the rationality framing fails because the stopping point, not the outcome, is what is chosen; the parlor game strips the commitment technology and common knowledge that real cases carry, which is why Shubik calls the generalisation only "useful ... in a limited manner." [INTERPRETATION grounded in Shubik's own text]

15. For the Substrate's own operating context, the auction is the cleanest available formalisation of sunk-cost escalation in systems that can bid, retry, or reinvest, and its sharpest lesson is negative: an agent with no stopping rule and no credible commitment is not playing a game with a rational solution, it is running the auction. [INTERPRETATION]

## Sources

### Verified live this session

- Shubik, Martin, "The Dollar Auction Game: A Paradox in Noncooperative Behavior and Escalation," Journal of Conflict Resolution 15(1), March 1971, pp. 109 to 111. Full text read as a direct PDF. https://www.math.utoronto.ca/mpugh/Teaching/Sci199_03/dollar_auction_1.pdf (this is the source for every Shubik quotation in this file)
- Sage Journals landing page and DOI for the same article. https://journals.sagepub.com/doi/10.1177/002200277101500111
- APA PsycNet record for the same article, giving the citation as 15(1), 109 to 111, 1971. https://psycnet.apa.org/record/1972-22907-001
- RePEc / IDEAS record for the same article. https://ideas.repec.org/a/sae/jocore/v15y1971i1p109-111.html
- Wikipedia, "Dollar auction" (the play description, the all-pay structure, and the Shubik 1971 citation). https://en.wikipedia.org/wiki/Dollar_auction
- Conversable Economist, "Martin Shubik's Dollar Auction Game" (the first-published-discussion date and the John Kay quotation). https://conversableeconomist.com/2011/11/15/martin-shubiks-dollar-auction-game/
- DRPress survey, "Strategic Analysis of Dollar Auction" (the "invented the dollar auction in 1971" attribution). https://drpress.org/ojs/index.php/EHSS/article/download/778/711/743
- Investopedia, "Dollar Auction Game" (a standard finance-education treatment). https://www.investopedia.com/terms/d/dollar-auction.asp
- Elsevier / ScienceDirect book record for Teger, Too Much Invested to Quit (1980), ISBN 978-0-08-022995-9, with the publisher description naming the dollar auction. https://www.sciencedirect.com/book/9780080229959/too-much-invested-to-quit and https://shop.elsevier.com/books/too-much-invested-to-quit/teger/978-0-08-022995-9
- Costanza 1988 PDF, an experiment using the dollar auction game (the "bids over $1 ... too much invested to quit" line). https://www.robertcostanza.com/wp-content/uploads/2017/02/1988_J_Costanza_DollarAuctionGame.pdf
- Psychology.com reference, "Irrational Escalation: Meaning and the Dollar Auction" (Teger's 1980 laboratory program and its finding). https://psychology.com/biases/irrational-escalation
- Staw, "Knee-deep in the Big Muddy," full-text PDF and ScienceDirect record (OBHP 16(1), 1976, 27 to 44). https://strategy.sjsu.edu/www.stable/pdf/Staw,%20B%20M,%201976,%20Organizational%20Behavior%20and%20Human%20Performance.%2016%20pp%2027-44.pdf and https://www.sciencedirect.com/science/article/abs/pii/0030507376900052
- Arkes and Blumer, "The psychology of sunk cost," RePEc record (OBHDP 35(1), 1985, 124 to 140) and ResearchGate record. https://econpapers.repec.org/RePEc:eee:jobhdp:v:35:y:1985:i:1:p:124-140 and https://www.researchgate.net/publication/4812596_The_psychology_of_sunk_cost

### Established record cited but not re-verified

- Poundstone, William, Prisoner's Dilemma: John von Neumann, Game Theory, and the Puzzle of the Bomb (Doubleday 1992; First Anchor Books edition, February 1993, ISBN 038541580X). Every Poundstone quotation and page anchor in this file comes from the operator's hand transcription in research/raw/poundstone-prisoners-dilemma-quotations.md, not from a re-read of the print copy this session. Provenance is that of a careful reader, so the wording and page numbers should be confirmed against the print copy before promotion into a finding.
- Teger, Allan I., Too Much Invested to Quit (Pergamon Press, 1980). The book's experimental design and internal findings were not read; the publisher blurb and one secondary reference are the basis for what is said about it.
- Brockner, Joel, "The Escalation of Commitment to a Failing Course of Action: Toward Theoretical Progress," Academy of Management Review 17(1), 1992, 39 to 61. Author, journal, and year are the standard record; the volume, issue, and pages are BACKGROUND and were not fetched this session.
- Staw, Barry M., "The Escalation of Commitment to a Course of Action," Academy of Management Review, 1981. The follow-up essay, cited here only as the field's later Staw statement, not read.
- The Concorde-fallacy framing of sunk cost, and the standard all-pay auction literature. Named as background; not fetched.
- Costanza 1988 full citation (exact journal and pages). The PDF was located by URL but its bibliographic header was not read, so only the author-year and the finding are recorded.

### Still unverified

- Whether Shubik published or circulated the dollar auction before 1971, for example in a 1960s working paper or RAND-adjacent document. No earlier item surfaced; the game as a party game clearly predates the paper but is not dated.
- Teger 1980's experimental design in detail (number of pairs, prize sizes, increments, measures). No copy read.
- Brockner 1992's exact title, volume, issue, and pages. Inferred from the standard citation; not fetched.
- The derivation of Poundstone's figure that "the 'rational' first bid would be 72 cents" (p. 269). The transcription records the figure without the calculation, and 72 cents does not align with the 5-cent bid increment in Shubik's own stated rules, so the number rests on assumptions the transcription does not record. Do not present it as Shubik's own.

---

## Note added at merge, and parent verification of citations

This file was written from a research brief on 2026-11-23 and committed by the curator. Three things were done at merge.

1. Links validated. Every wikilink in this file was checked against the node inventory in research/raw, research/findings, insights/concepts and insights/entities. All resolve. The four sibling files commissioned in the same batch land in the same commit run, so [[howard-metagame-theory]], [[dollar-auction-escalation]], [[largest-number-game-all-pay-auctions]] and [[volunteers-dilemma]] all exist alongside this file.
2. Citations re-verified by the curator against Crossref, independently of the brief, with DOI-precise records: Shubik 1971, Journal of Conflict Resolution 15(1):109 to 111, DOI 10.1177/002200277101500111; Diekmann 1985, Journal of Conflict Resolution 29(4):605 to 610, DOI 10.1177/0022002785029004003; Baye, Kovenock and de Vries 1996, Economic Theory 8(2):291 to 305, DOI 10.1007/BF01211819; Maynard Smith 1974, Journal of Theoretical Biology 47(1):209 to 221, DOI 10.1016/0022-5193(74)90110-6; Tennenholtz 2004, Games and Economic Behavior 49(2):363 to 373, DOI 10.1016/j.geb.2004.02.002; Palfrey and Rosenthal 1984, Journal of Public Economics 24(2):171 to 193, DOI 10.1016/0047-2727(84)90023-9; Arkes and Blumer 1985, Organizational Behavior and Human Decision Processes 35(1):124 to 140, DOI 10.1016/0749-5978(85)90049-4; Staw 1976, Organizational Behavior and Human Performance 16(1):27 to 44, DOI 10.1016/0030-5073(76)90005-2. Hillman and Riley 1989 did not resolve in Crossref under several bibliographic queries and stays BACKGROUND wherever this file cites it.
3. Quotation provenance unchanged. Every Poundstone quotation in this file carries its page anchor from the operator's own transcription of his print copy, the First Anchor Books edition, February 1993, committed at research/raw/poundstone-prisoners-dilemma-quotations.md. Those quotations are second-hand at one remove: a reader's transcription, not a scan. The parent file says so and so does this note.
- 4. The brief read Shubik 1971 in full text from a course PDF, which is why this file can quote his actor-by-actor escalation reasoning rather than summarizing it. Brockner 1992 remains BACKGROUND: the standard record is cited but its bibliographic details were not fetched.
