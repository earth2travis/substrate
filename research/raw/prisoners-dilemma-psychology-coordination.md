# The Human Player: Psychology and Coordination in the Prisoner's Dilemma

Raw research file. Part 3 of 4 in a deep-dive series on the prisoner's dilemma. This file covers what actual humans do in the game, the psychological mechanisms underneath, the institutions humans build to solve coordination failure, and the dark side: when cooperation itself is the problem. It is source material for later synthesis, not a finished essay.

Stance: report what experiments show, report what the literature claims, mark the boundary between them. FACT tags apply to claims verified live this session (URLs in Sources); BACKGROUND marks established record not re-verified; INTERPRETATION marks analytic connections; UNVERIFIED flags what could not be checked.

Series: prisoners-dilemma-anatomy.md, iterated-prisoners-dilemma-axelrod-tournaments.md, prisoners-dilemma-psychology-coordination.md (this file), faustian-bargain-prisoners-dilemma-crypto-ai.md.

Related Substrate nodes: [[principal-agent-theory]] (contracts as payoff rewrites), [[multi-agent-coordination]], [[protocols-coordination]], [[irl-moral-psychology-connection]].

---

## 1. What humans actually do in one-shot play

Standard game theory predicts universal defection in a one-shot, anonymous prisoner's dilemma. Defection strictly dominates. Humans do not comply with the prediction.

- [BACKGROUND/UNVERIFIED on exact figures] In Rapoport and Chammah's 1965 experiments with iterated PD blocks, overall cooperation rates averaged near 50%, with wide variance across payoff matrices. Their "Prisoner's Dilemma" (University of Michigan Press) remains the foundational empirical dataset.
- [FACT] Sally (1995), "Conversation and Cooperation in Social Dilemmas," Rationality and Society 7(1): 58-92, meta-analyzed 35 years of PD experiments (1958-1992) across 130+ conditions. Mean cooperation was about 37%, rising to roughly 70% when communication was allowed, and falling when players were anonymous strangers.
- [FACT] Communication is the single largest cooperation lever in the meta-analytic record. Even non-binding "cheap talk" before a one-shot PD roughly doubles cooperation (Sally 1995).
- [BACKGROUND] Payoff structure matters: as the temptation payoff rises relative to mutual cooperation, cooperation falls. Rapoport and Chammah formalized this with cooperation indices built from the matrix; modern lab work confirms payoff magnitudes still move rates.
- [BACKGROUND] Culture and demographics move baseline rates, but no single "culture effect" dominates; the interaction with framing is larger.
- [INTERPRETATION] The one-shot PD is not a test of rationality. It is a Rorschach. The same payoff matrix yields 20% cooperation under one label and 70% under another. What the game measures is which social script the player thinks they are inside.

## 2. Psychological mechanisms

### Social preferences and inequity aversion

- [BACKGROUND] Fehr and Schmidt (1999), "A Theory of Fairness, Competition, and Cooperation," QJE 114(3): 817-868. Agents dislike unequal outcomes even when inequality favors them, and dislike it more when it disfavors them. PD cooperation emerges as a corner solution of inequity aversion: cooperating when the partner cooperates avoids the guilt of being the defector in a (C,D) outcome.
- [BACKGROUND] Related models: Bolton and Ockenfels (2000) ERC; Rabin (1993) fairness equilibria in psychological game theory. All put others' payoffs inside one's own utility function.
- [INTERPRETATION] Social preference models retrofit utility theory to the data and risk tautology: any observed behavior can be fit by adjusting the parameter. Their predictive content comes from cross-game consistency: the same parameter should explain ultimatum rejections, dictator giving, and PD cooperation.

### Trust and oxytocin (with skepticism)

- [FACT] Kosfeld et al. (2005), "Oxytocin increases trust in humans," Nature 435: 673-676. Intranasal oxytocin increased money transfers in a trust game.
- [FACT] The finding has not replicated robustly. Lane et al. (2015), PLoS ONE 10(8): e0137000, failed to replicate. Nave, Camerer, and McCullough (2015, Trends in Cognitive Sciences) reviewed the intranasal-oxytocin literature and found most studies underpowered with publication bias.
- [INTERPRETATION] Treat all single-hormone/single-behavior claims in social neuroscience as provisional. The oxytocin-trust story is the canonical beautiful result that dissolved under replication pressure. The behavior (trust game transfers) is real; the pharmacological lever is not established.

### In-group / out-group effects

- [BACKGROUND] The minimal group paradigm (Tajfel): arbitrary group labels produce in-group favoritism in allocation games. Players cooperate more with in-group partners and defect more against out-group partners even when group membership is meaningless.
- [BACKGROUND] Intergroup PD (Bornstein's line of work): individuals cooperate more when playing for their group against another group than when playing one-on-one. Competition between groups raises within-group cooperation.
- [INTERPRETATION] Group identity is a coordination technology. It solves the PD by redefining the payoff boundary: the in-group's payoff becomes partially internal to the player's utility.

### Guilt aversion and psychological game theory

- [BACKGROUND] Battigalli and Dufwenberg (2007), "Guilt in Games," AER P&P 97(2): 170-176, building on Geanakoplos, Pearce, and Stacchetti (1989). Utility depends on beliefs about others' beliefs. Guilt aversion: players cooperate to avoid letting down a partner they believe expects cooperation.
- [INTERPRETATION] Guilt aversion explains why communication works. Cheap talk creates expectations; expectations create guilt; guilt changes payoffs. The PD's material matrix is fixed, but its psychological matrix is not.

### Strong reciprocity and altruistic punishment

- [BACKGROUND] Gintis (2000), "Strong Reciprocity and Human Sociality," J. Theoretical Biology 206: 169-179; Bowles and Gintis, A Cooperative Species (2011). Strong reciprocity: predisposition to cooperate conditional on others cooperating, and to punish defectors even at personal cost, even in one-shot anonymous settings.
- [FACT] Fehr and Gächter (2002), "Altruistic Punishment in Humans," Nature 415: 137-140. In public goods games with a punishment option, players paid real money to punish free-riders despite no material gain; cooperation rose and stabilized near full contribution. Without punishment, cooperation decayed across rounds.
- [BACKGROUND] Cross-cultural replication (Herrmann, Thöni, Gächter 2008, Science 319: 1362-1367) found antisocial punishment (punishing cooperators) in some participant pools, inversely correlated with rule-of-law indicators. Altruistic punishment is not universal; its target depends on local norms.
- [INTERPRETATION] Punishment converts the PD from a two-player game into a meta-game with an enforcement technology. Once punishment exists, cooperation can be stable among strangers. The puzzle shifts from "why cooperate" to "why pay to punish"; the strong-reciprocity answer is emotion: anger at defectors is the proximate mechanism (per Fehr and Gächter's own abstract).

### Moral foundations

- [BACKGROUND/UNVERIFIED on effect sizes] Haidt's moral foundations (care, fairness, loyalty, authority, sanctity, liberty) map onto PD behavior unevenly: fairness/reciprocity predicts cooperation; loyalty/authority predicts in-group cooperation and out-group defection. Direct PD experiments using MFQ scores exist but effects are modest.

## 3. Institutions as PD-solvers

If the PD is the formalization of the collective action problem, institutions are the accumulated solutions. Each modifies the game: the payoffs, the information, the repetition structure, or the player set. [BACKGROUND throughout unless tagged]

- **Reputation systems.** Reputation converts one-shot games into iterated games with an audience: eBay feedback, credit scores, academic citation. Nowak and Sigmund's indirect reciprocity work ("image scoring," Nature 1998) formalized it: help those who help others. The Substrate's [[erc-8004-trustless-agents]] node is this mechanism ported to autonomous agents: on-chain reputation registries so agents "find and trust another agent it has never interacted with before," converting every agent encounter into a shadowed future.
- **Contracts and enforcement.** Contracts do not change preferences; they change payoffs. An enforceable penalty for breach transforms the matrix so cooperate dominates. The state is, among other things, a third-party enforcement technology. This is [[principal-agent-theory]]'s whole subject seen from the PD side.
- **Law.** Hart's obligation rules (The Concept of Law, 1961): law converts moral norms into backed commitments. Antitrust law exists precisely because cartel cooperation is a solved PD that society wants to unsolve (section 4).
- **Norms.** Self-enforcing when backed by social punishment (gossip, shunning). Ellickson's Order Without Law (1991) documented Shasta County ranchers resolving disputes through norms diverging from formal law.
- **Schelling focal points.** The Strategy of Conflict (1960): when multiple equilibria exist, salience coordinates without communication. In PD-adjacent coordination games (stag hunt), focal points determine whether groups land on cooperate-cooperate or defect-defect.
- **Costly signaling.** Zahavi's handicap principle; Spence job-market signaling. Costly-to-fake signals (religious observance, gang tattoos, degrees) certify cooperativeness because defectors would not pay the cost.
- **Commitment devices.** Schelling again: burning bridges, hostages, Ulysses contracts. Removing your own exit option makes your promise credible. Cortés scuttling his ships is the canonical anecdote.
- **Ostracism.** Exclusion from the group is the ancient punishment; it works because humans are obligate cooperators. Lab ostracism experiments (Cyberball) show excluded players' cooperation collapses and social pain activates.

### Ostrom's design principles

- [FACT] Ostrom, Governing the Commons (1990), derived eight design principles from long-enduring common-pool resource institutions (irrigation systems in Spain and the Philippines, fisheries, forests). Nobel Prize in Economic Sciences 2009. The list, verified via Wilson, Ostrom, and Cox (2013, J. Economic Behavior and Organization 90S):
  1. Clearly defined boundaries (who is in, who is out).
  2. Proportional equivalence between benefits and costs (rules fit local conditions).
  3. Collective-choice arrangements (users participate in making rules).
  4. Monitoring (by monitors accountable to users).
  5. Graduated sanctions (start light, escalate).
  6. Conflict-resolution mechanisms (cheap, fast, local).
  7. Minimal recognition of rights to organize (external authority does not override).
  8. Nested enterprises (governance in layers; polycentricity).
- [INTERPRETATION] Ostrom is the empirical answer to the n-player PD. Hardin's "tragedy of the commons" assumed the PD was unsolvable without privatization or Leviathan. Ostrom's fieldwork showed communities solving it repeatedly, and reverse-engineered the common features. Principles 4 and 5 (monitoring plus graduated sanctions) are institutionalized altruistic punishment; principle 3 is communication institutionalized; principle 1 is the in-group boundary institutionalized. The lab findings of section 2 and the field findings of Ostrom are the same finding at different scales.

## 4. The dark side: when cooperation is the problem

The PD is morally symmetric. The same machinery that produces public goods produces cartels.

- [BACKGROUND] Cartels and price-fixing: OPEC, the lysine cartel (ADM, 1990s), the vitamins cartel. Cartel members face a PD: everyone benefits from the cartel price if all comply, but each gains by secretly undercutting. Cartels build exactly the institutions of section 3 to survive: monitoring (audited sales reports), graduated sanctions, communication (trade association meetings), boundaries. Antitrust enforcers use the PD deliberately: leniency programs give the first defector immunity, manufacturing a race to defect. The DOJ leniency program is the PD weaponized against cooperation.
- [BACKGROUND] Omertà: Mafia codes of silence are cooperation equilibria maintained by extreme punishment. The state's counter-strategy (witness protection, plea bargains) is again the manufactured PD.
- [BACKGROUND] Disarmament: arms races are PDs where mutual defection (arming) is the bad equilibrium and mutual cooperation (disarming) the good one. But the mirror image matters: sometimes mutual defection is desirable. Competition between firms, political candidates, and species is mutual defection that benefits third parties.
- [INTERPRETATION] "Cooperation" is not a moral category in the PD. It is a strategy label. Whether C-C is good depends on whose payoffs count. Adam Smith's invisible hand is, formally, a society that has arranged for mutual defection among producers to benefit consumers.
- [INTERPRETATION] The PD formalizes "individually rational, collectively stupid." Its dual is "individually irrational, collectively smart": every act of cooperation is, from the narrow payoff view, a mistake. Moral progress consists largely of building institutions that align the two; moral disaster consists of institutions that align them toward the wrong collective output.

## 5. Framing effects

- [FACT] Liberman, Samuels, and Ross (2004), "The Name of the Game: Predictive Power of Reputations versus Situational Labels in Determining Prisoner's Dilemma Game Moves," PSPB 30(9): 1175-1185. Stanford undergrads played an identical 7-round PD labeled either "Wall Street Game" or "Community Game." Cooperation in the Community Game was roughly double the Wall Street Game (first-round cooperation roughly 67-69% vs. 33-37%).
- [FACT] The label swamped reputation. Players nominated by peers as "most likely cooperators" defected in the Wall Street Game; players nominated as "most likely defectors" cooperated in the Community Game. The situational label predicted behavior better than peer reputation did.
- [BACKGROUND] Related framing findings: "Give Some" vs. "Take Some" public goods framing (Brewer and Kramer 1986); "trust game" vs. "investment game"; losses vs. gains framing changes cooperation with identical expected values.
- [INTERPRETATION] Framing effects are not noise. They are the interface between the formal game and the player's social script library. A game is never played as a bare payoff matrix; it is played as a story about what kind of situation this is. Whoever names the game chooses the script. This is why lawyers, negotiators, and propagandists fight over labels before they fight over terms.

## 6. Humans in iterated play

- [BACKGROUND] Humans in finitely iterated PD experiments do not play subgame-perfect defection. They cooperate early and defect near the end (the endgame effect), consistent with reputation building rather than backward induction. Selten and Stoecker (1986) is the classic demonstration.
- [BACKGROUND] In indefinitely iterated PD (random continuation probability), human play resembles noisy tit-for-tat: cooperative, retaliatory, forgiving, error-prone. Dal Bó and Fréchette (AER 2011) show cooperation rises with the continuation probability, as theory predicts, but levels stay below theoretical benchmarks; strategies are heterogeneous, with TFT, Grim, and always-cooperate coexisting.
- [BACKGROUND] Fudenberg, Rand, and Dreber (2012), "Slow to Anger and Fast to Forgive," AER 102(2): 720-749: in noisy lab iterated PD, successful human strategies are lenient (don't punish the first defection) and forgiving (return to cooperation quickly), matching what evolutionary models predict for noisy environments.
- [BACKGROUND] Strategy heterogeneity is the stable finding. No single strategy describes the population; the mix itself is the equilibrium. Strategy-frequency estimation typically recovers TFT-like, Grim, ALL-C, ALL-D, and WSLS (Pavlov) clusters.
- [INTERPRETATION] Axelrod's tournaments asked which strategy wins against a fixed ecology of programs. The lab literature asks what humans actually are. The answer: imperfect reciprocators with forgiveness built in, precisely the strategy class evolution selects when the world has noise. Humans arrive at the lab pre-equipped with the strategies that won a much older tournament.

## 7. Where the mapping breaks

- The replication crisis cut this field. Oxytocin-trust is the cautionary case [FACT, section 2]. Social priming claims adjacent to framing work have fallen. The robust core: communication effects, endgame effects, punishment effects, framing effects. All four have decades of replication.
- Lab PD players are disproportionately WEIRD (Western, educated, industrialized, rich, democratic) students. Cross-cultural work (Herrmann et al. 2008) shows punishment behavior itself varies with local institutions; the "human player" is partly a local player.
- Social preference models explain everything and predict little unless pinned across games. Cooperation "because inequity aversion" can be relabeling rather than explanation.
- Stakes in the lab are small. Extrapolating from $10 games to arms races and commons governance assumes payoff-scale invariance that is asserted more often than demonstrated.
- Institutions are usually studied as solutions to PD, but institutions also manufacture PDs (antitrust leniency, plea bargaining). The solver and the disease share machinery; section 4 is not a footnote.

## 8. Compression points for synthesis

1. Sally (1995) meta-analysis: mean one-shot PD cooperation around 37%, roughly doubling with communication. [FACT]
2. Liberman, Samuels, Ross (2004): naming an identical PD "Community Game" vs. "Wall Street Game" roughly doubled cooperation and swamped peer-reputation predictions. [FACT]
3. Fehr and Gächter (2002): costly altruistic punishment of defectors sustains cooperation in public goods games; without it, cooperation decays. [FACT]
4. Kosfeld et al. (2005) oxytocin-trust failed robust replication (Lane et al. 2015; Nave et al. 2015); treat the hormone-trust link as unestablished. [FACT]
5. Ostrom's eight design principles (boundaries, proportionality, participation, monitoring, graduated sanctions, conflict resolution, recognition, nesting) are the empirically derived institutional solution to the n-player PD. [FACT]
6. Humans in iterated PD play noisy, lenient, forgiving TFT-like strategies; cooperation rises with continuation probability but below theory. [BACKGROUND]
7. Cartels solve the PD with the same tools as commons communities (monitoring, sanctions, communication); antitrust leniency programs win by re-imposing the PD on cartel members. [BACKGROUND]
8. Fehr-Schmidt inequity aversion and Battigalli-Dufwenberg guilt aversion explain cooperation via social preferences and belief-dependent utility; powerful but tautology-prone. [BACKGROUND]
9. In-group/out-group boundaries shift PD cooperation strongly; group identity is a coordination technology that redraws the payoff boundary. [BACKGROUND]
10. "Cooperation" in a PD is morally neutral: whether C-C is good depends on whose payoffs count (cartels bad, disarmament good, product competition as beneficial mutual defection). [INTERPRETATION]
11. Framing effects are script selection, not noise: whoever names the game chooses the equilibrium the players aim at. [INTERPRETATION grounded in FACT]
12. For agent systems, the human literature implies: give agents communication channels, identity persistence, punishment capability, and long horizons, and cooperation emerges without central authority; the Substrate's [[multi-agent-coordination]] and [[erc-8004-trustless-agents]] nodes are exactly these levers in machine form. [INTERPRETATION]

---

## Sources

Verified live this session:

- Sally, "Conversation and Cooperation in Social Dilemmas: A Meta-Analysis of Experiments from 1958 to 1992," Rationality and Society 7(1): 58-92 (1995). https://journals.sagepub.com/doi/10.1177/1043463195007001004
- Liberman, Samuels, & Ross, "The Name of the Game," PSPB 30(9): 1175-1185 (2004). https://pubmed.ncbi.nlm.nih.gov/15359020/
- Fehr & Gächter, "Altruistic Punishment in Humans," Nature 415: 137-140 (2002). https://pubmed.ncbi.nlm.nih.gov/11805825/
- Kosfeld et al., "Oxytocin increases trust in humans," Nature 435: 673-676 (2005). https://pubmed.ncbi.nlm.nih.gov/15931222/
- Lane et al., "Failed Replication of Oxytocin Effects on Trust," PLoS ONE 10(8): e0137000 (2015). https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0137000
- Nave, Camerer, & McCullough, oxytocin review critique, Trends in Cognitive Sciences (2015). Verified via ResearchGate record; verify the journal page before direct quotation.
- Wilson, Ostrom, & Cox, "Generalizing the core design principles for the efficacy of groups," J. Economic Behavior and Organization 90S (2013). https://www.sciencedirect.com/science/article/abs/pii/S0167268112002697

Established record cited but not re-verified this session (verify before direct quotation):

- Rapoport & Chammah, Prisoner's Dilemma (University of Michigan Press, 1965). Exact cooperation percentages UNVERIFIED.
- Fehr & Schmidt, "A Theory of Fairness, Competition, and Cooperation," QJE 114(3): 817-868 (1999).
- Battigalli & Dufwenberg, "Guilt in Games," AER P&P 97(2): 170-176 (2007).
- Gintis, "Strong Reciprocity and Human Sociality," J. Theoretical Biology 206: 169-179 (2000).
- Herrmann, Thöni, & Gächter, "Antisocial Punishment Across Societies," Science 319: 1362-1367 (2008).
- Ostrom, Governing the Commons (1990).
- Ellickson, Order Without Law (1991).
- Schelling, The Strategy of Conflict (1960).
- Selten & Stoecker (1986), finite iterated PD endgame behavior.
- Dal Bó & Fréchette, "The Evolution of Cooperation in Infinitely Repeated Games: Experimental Evidence," AER (2011).
- Fudenberg, Rand, & Dreber, "Slow to Anger and Fast to Forgive," AER 102(2): 720-749 (2012).
- Brewer & Kramer (1986), give-some/take-some framing.
- Haidt, moral foundations theory; MFQ-PD effect sizes UNVERIFIED.
