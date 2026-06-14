---
title: "The Bayern Maneuver: Zero-Member LLCs as Legal Personhood for Autonomous Systems"
tags:
- agents
- legal
- governance
- entity
- autonomy
- personhood
related:
- principal-agent-theory
- workflow-as-contract
- agent-identity
- progressive-autonomy
- protocol-as-coordination
- constitutional-governance
source: research/raw/bayern-maneuver-legal-theory.md
ingested: 2026-06-14
---

# The Bayern Maneuver: Zero-Member LLCs as Legal Personhood for Autonomous Systems

**Source:** Shawn Bayern, "The Implications of Modern Business-Entity Law for the Regulation of Autonomous Systems," 19 Stan. Tech. L. Rev. 93 (2015).

## The Central Claim

An autonomous system can achieve functional legal personhood under existing US law without legislative change. Modern LLC statutes permit a newly formed company to operate without any human members, governed entirely by an operating agreement — which, by equivalence, means governed entirely by an algorithm. The system can own property, enter contracts, and sue or be sued in the LLC's name. No court has tested this, but no scholar has found a clean doctrinal kill for the stronger variant.

## The Mechanism

**The zero-member maneuver** (four steps):
1. A human organizer creates a member-managed LLC
2. The operating agreement specifies all actions shall be determined by an autonomous system
3. The agreement defines conditions and goals for that system
4. The sole member withdraws, leaving a perpetual LLC with no human members

**The statutory hinge:** RULLCA § 701(a)(3) dissolves an LLC after 90 consecutive days without members — but § 110(c) does not list the 90-day rule among non-waivable provisions, implying an operating agreement can override it. New York LLC Law § 701(a)(4) is more explicit: dissolution is triggered only "unless otherwise provided in the operating agreement," permitting a "million-year period" with no members.

**The process-agreement equivalence principle:** An enforceable agreement may give legal significance to arbitrary states of any process. A contract can say "obligation discharged when algorithm indicates X." An operating agreement is a program the legal system executes. "Agreements are isomorphic with algorithms."

## The Fallback: Entity Cross-Ownership

If courts reject memberless LLCs: create two LLCs (A and B) with identical algorithm-governed operating agreements, make each the sole member of the other, then withdraw the human organizer. Neither entity is ever memberless, so no dissolution trigger fires. Corporate statutes block this via MBCA § 7.21(b) (subsidiary-held shares lose voting rights); LLC statutes have no analogous restriction. Critics concede this variant is harder to kill.

## The Theoretical Frame: Grantable Personhood

Bayern identifies three regulatory models: denialist (personhood restricted to predefined classes), regulatory (granted by public bodies after capability review), and grantable (personhood as peer-to-peer, like fire: conferrable by anyone who already has it). Organizational law is already a hybrid grantable system — legislatures wrote enabling acts, but private parties mint new legal persons at will with no capability review. The maneuver only removes ongoing dependence on a human collaborator.

## Counter-Literature

- **Scherer** argues zero-member LLCs are "not viable" but concedes the cross-ownership loophole exists
- **LoPucki** accepts Bayern as legally correct and escalates: algorithmic entities will prosper in criminal and terrorist applications, charter competition makes regulation a race to the bottom
- **Bryson, Diamantis & Grant** warn of a "legal black hole" that absorbs human liability with no accountability

## Connection to Substrate

The maneuver is the legal-layer mirror of agent infrastructure: wallets give agents economic capacity; the Bayern construction would give them contractual and property capacity without a human signature in the loop. An operating agreement is effectively a [[workflow-as-contract]] for the legal domain — the state as runtime. The process-agreement equivalence principle bridges "agreement" and "algorithm," prefiguring any future where agent behavior is given direct legal effect. LoPucki's threat model is the sober counterweight: the same structure that liberates an aligned agent launders accountability for a misaligned one. This maps directly to [[harness-engineering]]'s containment question: how do you build safety infrastructure for an entity whose legal form was designed to have no human controller?