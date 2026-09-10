---
title: "Faust and Moloch: The Prisoner's Dilemma in Myth, Crypto, and AI"
tags: [finding, game-theory, crypto, ai-safety, coordination, mechanism-design, culture]
related:
- crypto-as-agent-infrastructure
- multi-agent-coordination-patterns
- principal-agent-theory
- protocol-as-coordination
source: research/raw/faustian-bargain-prisoners-dilemma-crypto-ai.md
ingested: 2026-09-10
---
# Faust and Moloch: The Prisoner's Dilemma in Myth, Crypto, and AI

## Key Points

**Faust and Moloch are the two faces of the same failure.** Moloch is the multiplayer trap with no contract: everyone defects, no one signed anything, the system endures unconquered. Faust is the two-party trap with too much contract: one signer, one counterparty, binding terms, third parties paying. Crypto's tooling tries to engineer Moloch-games into cooperation; the risk is that the engineered enforcement becomes its own bargain. AI's racing dynamics are Moloch wearing lab logos; every proposed remedy is an attempt to build the court that Goethe gave his Faust.

**Goethe's wager is the great game-theoretic revision of the legend.** The legend arc runs from the historical charlatan (c. 1480-1540) through the Faustbuch (1587, damned), Marlowe (c. 1592, damned), Goethe (1808/1832, redeemed), to Mann (1947, damned, Germany as Faust). Goethe replaced the soul-purchase with a wager: damnation becomes contingent on Faust declaring a moment sufficient, endogenous to his striving rather than a calendar default. Mapped forward: the danger in capability acquisition is not the capability but the equilibrium in which acquisition stops being instrumental and becomes the terminal good.

**The soul is the archetype of one-shot irreversible spend.** The blood-signed pact is a collateralized contract where the collateral is indivisible, illiquid, and non-recoverable: front-loaded experiential payoff, back-loaded abstract cost past the felt discount horizon, damage externalized to non-signatories (Gretchen, Leverkühn's nation). This is why the Faustian idiom recurs in nuclear knowledge, the attention economy, and AI acceleration: present consumption, future bullet payment, disputed enforcement.

**Slashing and staking are inverse Faustian pacts.** Faust posts his soul as collateral for present gain; the staker posts collateral to prove future cooperation. Slashing rewrites the payoff matrix so defection is strictly negative: mechanism design as a contract with a Mephistopheles that actually collects, automatic, no appeals court. The limit: slashing governs only what the chain can observe, and most real defection (censorship, off-chain collusion, safety-washing) happens where the protocol cannot see.

**Ethereum named its enemy.** Soleimani's 2019 Moloch framing imported Scott Alexander's 2014 "Meditations on Moloch" into Ethereum, explicitly naming coordination failure as "prisoner's dilemmas that lead to unfortunate equilibriums." Public goods funding is the community's canonical n-player PD: free-riding is dominant, and quadratic funding (Gitcoin Grants, $10M+ to OSS in its first two years) is a cooperation technology that rewards breadth of cooperation over wealth. MEV is defection against the implicit cooperation of fair transaction ordering; EIP-1559's fee burn internalizes a commons externality.

**AI racing dynamics match PD payoff ordering, and safety-washing is cheap-talk defection.** Askell, Brundage, and Hadfield (2019, arXiv:1907.04534) is the canonical analysis: competitive pressure incentivizes corner-cutting on safety; remedies are trust, verification, and norms. The crux is observability: safety investment is less visible than capability output, so a lab can signal cooperation while defecting on the margin. Pauses, evals regimes, and third-party audits are attempts to build the missing enforcer.

**Superrationality is the one escape hatch requiring no enforcer, and it shares the blood contract's weakness.** Hofstadter's proposal, cooperation via logical correlation among symmetric reasoners, needs no slashing, bonds, or courts. It binds only agents that actually reason alike, and nothing collects from the ones that don't. No empirical evidence shows real agents coordinating this way at scale.

## Relevance

This finding connects the Substrate's crypto and AI-safety threads to the coordination canon. [[crypto-as-agent-infrastructure]] covers the rails; this finding names the failure modes those rails must govern (MEV as defection, public-goods free-riding) and the enforcement technologies (slashing, staking, quadratic funding) as payoff rewrites in the spirit of [[principal-agent-theory]]. For agent fleets under [[multi-agent-coordination-patterns]], the Faust/Moloch duality is a diagnostic: is the failure a multiplayer trap needing an enforcer, or a binding bargain whose costs fall on non-signatories? The wager framing also cuts into alignment discourse: the risk is not capability but the stopping condition.

## Related

- [[crypto-as-agent-infrastructure]]: the enforcement rails (slashing, staking, registries) in machine form
- [[multi-agent-coordination-patterns]]: population-level defenses against extortion and racing
- [[principal-agent-theory]]: contracts, observability, and the limits of enforcement
- [[protocol-as-coordination]]: building the court the cooperators lack
