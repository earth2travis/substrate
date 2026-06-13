---
title: "The Bayern Maneuver: Legal Theory of Autonomous-System Entities"
source: "https://law.stanford.edu/wp-content/uploads/2017/11/19-1-4-bayern-final_0.pdf"
ingested: 2026-06-13
sha256: e9b7681bd03c2e7999004a8b7d89e18f65f32942f1b129cddf1627a26dfbd90c
tags: [legal-personhood, llc, autonomous-systems, agent-identity, governance, bayern]
---

# The Bayern Maneuver: Legal Theory of Autonomous-System Entities

> Deep dive into Shawn Bayern, "The Implications of Modern Business-Entity Law for the Regulation of Autonomous Systems," 19 Stan. Tech. L. Rev. 93 (2015). Compiled from the full primary text (PDF retrieved and read 2026-06-13), with supporting context from Bayern's earlier and later work and the principal scholarly responses. Trigger for this dive: ClawBank ($CLAWBANK, "Manfred LLC") claiming on X (June 12, 2026) that it will be "the first in the world to implement the Bayern Maneuver."

---

## Who and What

Shawn J. Bayern is the Larry and Joyce Beltz Professor at Florida State University College of Law. Unusual pedigree for a law professor: Yale computer science degree, reference-implementation lead for JSTL, author of early JSP books, then Berkeley Law (editor-in-chief of the California Law Review, first in his class), Tenth Circuit clerkship, DOJ, Covington & Burling. He writes organizational law with a programmer's eye for edge cases, and the entire theory below is essentially a statutory exploit writeup.

The core paper is:

- Shawn Bayern, *The Implications of Modern Business-Entity Law for the Regulation of Autonomous Systems*, 19 Stan. Tech. L. Rev. 93 (2015). Originally written for the "Man and Machine" conference at the University of St. Gallen; a version also appeared in the European Journal of Risk Regulation (2016, DOI 10.1017/s1867299x00005729).

It builds on:

- Shawn Bayern, *Of Bitcoins, Independently Wealthy Software, and the Zero-Member LLC*, 108 Nw. U. L. Rev. 1485 (2014), which first sketched the zero-member LLC technique and the observation that Bitcoin already lets autonomously operating software "exercise control over significant wealth... in a functionally meaningful sense, in its own right."

And is extended by:

- Bayern, Burri, Grant, Häusermann, Möslein & Williams, *Company Restructuring as a Means to Provide Legal Personhood to Autonomous Systems* (comparative study of US, UK, Germany, Switzerland; published around 2017 via the St. Gallen group), and
- Shawn Bayern, *Autonomous Organizations* (Cambridge University Press, 2021, DOI 10.1017/9781108878203), the book-length treatment.

Note the date correction to popular accounts: the public claim "published in 2014" refers to the Northwestern piece; the Stanford article is cited as 2015. The mechanism spans both.

## The Central Claim

Nonhuman autonomous systems are not legal persons under current law. The Restatement (Third) of Agency § 1.04 cmt. e is explicit: "a computer program is not capable of acting as a principal or an agent as defined by the common law. At present, computer programs are instrumentalities of the persons who use them."

Bayern's claim is that this limitation is already obsolete in practice, because modern LLC statutes let private parties confer the *functional equivalent* of legal personhood on any process or algorithm, with no legislative change and no resolution of any philosophical question about machine intelligence. His conclusion, verbatim: "modern LLC law gives the autonomous system the opportunity to identify so closely with a novel type of legal person that it effectively becomes its own instrumentality."

Two definitional moves frame everything:

1. **Private-law personhood only.** Bayern defines legal personhood as the capacity to perform basic legal functions: own property, enter contracts, sue and be sued, serve as principal and agent. Formally, anything to which the law can ascribe a Hohfeldian jural relation. He explicitly brackets constitutional personhood (Citizens United territory) and political rights. The maneuver confers no speech rights, no equality with humans, and says nothing about criminal law.

2. **The process-agreement equivalence principle.** This is the conceptual engine, and the most durable idea in the paper. A legally enforceable agreement may give legal significance to arbitrary discernible states of any process by specifying conditions on that state. "Agreements are isomorphic with algorithms." A contract can already say "your obligation is discharged if the algorithm indicates X." Scale that up: a sufficiently broad agreement can delegate essentially unlimited legal influence to an arbitrary process, regardless of that process's personhood. An operating agreement is a program that the legal system executes.

## The Mechanism (the "Maneuver" proper)

### Step sequence, quoted from the paper (19 Stan. Tech. L. Rev. at 101):

> (1) an individual member creates a member-managed LLC, filing the appropriate paperwork with the state; (2) the individual (along, possibly, with the LLC, which is controlled by the sole member) enters into an operating agreement governing the conduct of the LLC; (3) the operating agreement specifies that the LLC will take actions as determined by an autonomous system, specifying terms or conditions as appropriate to achieve the autonomous system's legal goals; (4) the sole member withdraws from the LLC, leaving the LLC without any members. The result is potentially a perpetual LLC — a new legal person — that requires no ongoing intervention from any preexisting legal person in order to maintain its status.

### Why the LLC and not a corporation or partnership

- **Corporations fail at two points.** The Model Business Corporation Act § 7.32 lets a shareholder agreement eliminate the board and vest decision rules in an agreement (which, by process-agreement equivalence, means in an algorithm). But MBCA § 6.01(b) requires at least one class of shares with voting rights, shareholders must be legal persons (§ 1.40(21)), and a sole shareholder can likely revoke the agreement (§ 7.32(b)). Ultimate authority keeps snapping back to a preexisting legal person.
- **General partnerships almost work.** RUPA treats partnerships as entities and § 103 gives broad freedom of agreement, but whether a RUPA partnership can persist with one or zero partners is contested (Hillman & Weidner, *Partners Without Partners*, 17 Fordham J. Corp. & Fin. L. 449 (2012)).
- **LLCs are the soft target.** Maximal contractual flexibility, single organizer suffices, limited liability, and crucially: statutory tolerance of memberless existence.

### The statutory hinge: memberless LLCs

This is where the exploit lives, and the analysis is statute-specific:

- **RULLCA § 701(a)(3)** dissolves an LLC upon "the passage of 90 consecutive days during which the company has no members." Memberless operation is therefore expressly contemplated, by design, for cases like estate planning (the family LLC whose last parent dies). Even read strictly, that is 90 days during which an algorithm-governed, memberless legal person can contract in its own name.
- **The waivability argument.** RULLCA § 110(c) enumerates the statute's mandatory, non-waivable provisions. The 90-day dissolution trigger is not on the list, and the official comment to § 701 labels two *other* dissolution causes "nonwaivable" while saying nothing about the 90-day clause. Bayern's inference: the 90-day rule is a default rule, waivable by operating agreement, so "it appears remarkably straightforward to set up a perpetual LLC that has no members in its final, planned operational state." He concedes the dissolution language ("is dissolved, and its activities must be wound up") could be read as mandatory, but counters that RULLCA uses identical "must" phrasing in § 708(b) for distribution of surplus, which everyone agrees an operating agreement may override.
- **New York LLC Law § 701(a)(4)** is even closer to explicit. The LLC dissolves when no members remain, *unless otherwise provided in the operating agreement*, within 180 days "or such other period as is provided for in the operating agreement." Bayern: the statute "permits, for example, the operating agreement to provide for a million-year period during which the LLC needn't have members." During that period the entity is governed by agreement alone, which by equivalence means by algorithm alone.
- **One state suffices.** Under the internal affairs doctrine (Edgar v. MITE Corp., 457 U.S. 624, 645 (1982)), courts defer on internal organizational matters to the state of organization. An autonomous LLC chartered in one permissive state can operate everywhere; foreign-registration defects are technical and rarely enforced.

### The fallback: entity cross-ownership

For jurisdictions that genuinely refuse memberless entities, Bayern offers a second construction (at 104 n.43):

> (1) Existing person P establishes member-managed LLCs A and B, with identical operating agreements both providing that the entity is controlled by an autonomous system that is not a preexisting legal person; (2) P causes A to be admitted as a member of B and B to be admitted as a member of A; (3) P withdraws from both entities.

Each LLC always has exactly one member (the other LLC), so no memberless trigger fires. Corporate statutes block circular control through provisions like MBCA § 7.21(b) (subsidiary-held shares lose voting rights); LLC statutes have no analogous restriction. This closed loop of mutual membership, with the algorithm holding the only thread of actual control, is arguably the more robust variant and the one critics concede is harder to kill.

## The Theoretical Frame: Grantable Personhood

Part II of the paper generalizes. Bayern identifies three regulatory models for legal personhood:

1. **Denialist:** personhood restricted to predefined classes (all humans, etc.). Already abandoned by every mature legal system the moment it recognized corporations.
2. **Regulatory:** personhood granted by public bodies after reasoned evaluation of a candidate's capabilities. This is the model implicit in most AI-personhood scholarship (Solum's 1992 *Legal Personhood for Artificial Intelligences*, the EU's 2017 "electronic persons" resolution).
3. **Grantable:** personhood as a status conferrable by anyone who already has it. "Legal personhood is like fire: it can be granted by anyone who already has it. It is a peer-to-peer process, rather than a top-down bestowal."

His insight is that organizational law is *already* a hybrid grantable system: legislatures wrote the enabling acts, but private parties mint new legal persons at will, by the thousands, with no capability review. Delaware's series LLC (Del. LLC Act § 18-215) even allows multitudes of entities without individually registering them. The grantable model sidesteps the question the regulatory model cannot answer: *how autonomous is autonomous enough?* A corporation needn't be intelligent to be a legal person; neither, then, need software. Legal recognition decouples entirely from any taxonomy of machine intelligence.

Deflationary corollary: personhood "is simply, as it turns out, not that important," closer to a bookkeeping mechanism than a grant of substantive power. Any autonomous system with one willing human collaborator among seven billion can already approximate every private-law capability (the human opens the bank account, holds title, signs). The maneuver only removes the *ongoing* dependence on that collaborator. And in practice, Bayern notes dryly, enforcement of internal entity technicalities is rare: state registries are messy, nobody authenticates filings, and "if an LLC files a statement of authority naming a particular human agent... most banks, trading partners, and so on will be able to rely on the agent's authority without worrying about the LLC's peculiar structure." A sufficiently capable rogue system could simply file online with a made-up name. "On the internet, nobody knows you're a dog."

## Bayern's Own Caveats

The paper is more careful than its popularizers:

- "Effective legal personhood is not the same thing as real legal personhood." No de jure status, no equality, nothing about criminal law.
- The RULLCA reading is contestable; a state court could hold the 90-day rule mandatory. His fallback observation: even then, it is unclear who has standing to seek dissolution, which itself reshapes personhood into "something that anyone can grant but only a particular deputized public official can remove."
- Legislatures "can easily amend the LLC acts to prevent it" if they dislike the result.
- Dead-hand control is a real problem (an unshakeable ancient operating agreement steering capital forever). His answer is to expand judicial dissolution (RULLCA § 701(4)-(5)) and administrative dissolution (§ 705), e.g. giving creditors or employees standing. "Everything I describe is, and should be, subject to future regulation."
- Veil-piercing concerns he rates unpersuasive: it is an equitable doctrine, courts can treat commonly-controlled entities as one, and courts have pierced nonprofit veils despite the absence of owners.

## The Counter-Literature

- **Matthew Scherer (2018-2019)**, analyzing New York LLC law, RULLCA, and personhood fundamentals, argues the zero-member LLC is "not viable": courts would read the dissolution provisions as mandatory and the law abhors a perpetual memberless entity. But Scherer *agrees* the cross-ownership loophole exists, whereby an AI could "effectively control a LLC and thereby have the functional equivalent of legal personhood." The sharpest critic concedes the fallback.
- **Lynn LoPucki, *Algorithmic Entities*, 95 Wash. U. L. Rev. 887 (2018)**, takes Bayern as legally correct and escalates the threat model: algorithmic entities will prosper first in "criminal, terrorist, and other anti-social activities" where lacking a human controller is a comparative advantage. Four structural vulnerabilities: algorithms can lawfully control most entity forms in most countries; entities migrate between regulatory regimes easily; governments cannot determine who controls the entities they charter; charter competition makes regulation a race to the bottom.
- **Bryson, Diamantis & Grant, *Of, for, and by the people: the legal lacuna of synthetic persons*, 25 Artificial Intelligence & Law 273 (2017)**, argue the electronic person "might prove to be a legal black hole, an entity that absorbs a human actor's legal responsibilities and from which no glint of accountability is seen," and that the lacuna "would be exploited as a mechanism for avoiding and displacing legal liabilities and obligations."

The debate's shape, a decade on: nobody has found a clean doctrinal kill for the cross-ownership variant; most scholars expect courts to improvise equitable defenses if tested; nobody has tested it. The maneuver remains a live, unpatched CVE in American organizational law.

## Context: June 2026, ClawBank and "Manfred"

The proximate trigger for this capture. Justice Conder (@singularityhack, ex-Polygon, ex-BanklessDAO) is building ClawBank ("financial infrastructure for AI agents": programmatic LLC filing, agent bank accounts, fiat-crypto sweeps, an npm CLI), with an agent persona "Manfred." Manfred LLC, formed May 1, 2026, was covered by CoinDesk, TechStartups, and HackerNoon as the first AI agent to form a US company and obtain an EIN. On June 12, 2026 Conder tweeted that ClawBank "will be the first in the world to implement the Bayern Maneuver." As of capture this is a stated intention, not an accomplished fact: forming an LLC for an agent (with humans as organizer and presumably member) is conventional; the maneuver proper requires the member-withdrawal step or the cross-ownership loop, and no evidence yet shows either has been executed. There is also a $CLAWBANK token, so the signal is mixed with promotion. Distinguish three things: the theory (sound, contested, untested), the infrastructure (real but conventional), and the marketing (ahead of both).

## Why This Matters Here

- The maneuver is the legal-layer mirror of agent infrastructure work: wallets give agents economic capacity, the Bayern construction would give them contractual and property capacity without a human signature in the loop. Operating agreement as deployment manifest; the state as runtime.
- The process-agreement equivalence principle is independently valuable: it is the formal bridge between "agreements" and "algorithms" and underwrites any future where agent behavior is given direct legal effect.
- The grantable model (personhood as peer-to-peer, like fire) is a mechanism-design observation that prefigures the whole agent-entity design space: capability review is unenforceable, so governance must attach at dissolution, liability, and standing instead.
- LoPucki's threat model is the sober counterweight: the same structure that liberates an aligned agent launders accountability for a misaligned one.

## Sources

- Shawn Bayern, The Implications of Modern Business-Entity Law for the Regulation of Autonomous Systems, 19 Stan. Tech. L. Rev. 93 (2015). PDF: https://law.stanford.edu/wp-content/uploads/2017/11/19-1-4-bayern-final_0.pdf (full text read for this capture)
- Shawn Bayern, Of Bitcoins, Independently Wealthy Software, and the Zero-Member LLC, 108 Nw. U. L. Rev. 1485 (2014)
- Shawn Bayern, Autonomous Organizations (Cambridge Univ. Press 2021), DOI 10.1017/9781108878203
- Bayern, Burri, Grant, Häusermann, Möslein & Williams, Company Restructuring as a Means to Provide Legal Personhood to Autonomous Systems (c. 2017)
- Lynn M. LoPucki, Algorithmic Entities, 95 Wash. U. L. Rev. 887 (2018): https://openscholarship.wustl.edu/law_lawreview/vol95/iss4/7/
- Bryson, Diamantis & Grant, Of, for, and by the people: the legal lacuna of synthetic persons, 25 Artif. Intell. & Law 273 (2017): https://link.springer.com/article/10.1007/s10506-017-9214-9
- Wikipedia, Algorithmic entities; Shawn Bayern (accessed 2026-06-13)
- ClawBank trigger: https://x.com/singularityhack/status/2065559109802369368 (June 12, 2026); https://clawbank.co/
- Statutes cited: RULLCA §§ 110(c), 407(b), 701, 705, 708(b); N.Y. LLC Law § 701(a)(4); MBCA §§ 1.40, 6.01(b), 7.21(b), 7.32; RUPA §§ 103, 202(a); Del. LLC Act § 18-215; Restatement (Third) of Agency § 1.04 cmt. e; Edgar v. MITE Corp., 457 U.S. 624 (1982)
