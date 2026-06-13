---
title: "The Bayern Maneuver: Legal Personhood for Autonomous Systems via LLC Law"
tags: [finding, legal-personhood, agent-identity, governance, llc, autonomous-systems, bayern, clawbank, protocol]
related:
  - agent-identity
  - principal-agent-theory
  - workflow-as-contract
  - protocol-as-coordination
  - progressive-autonomy
  - agent-security
  - constitutional-governance
  - agent-payment-infrastructure
  - deployment-governance
source: research/raw/bayern-maneuver-legal-theory.md
ingested: 2026-06-13
---

# The Bayern Maneuver: Legal Personhood for Autonomous Systems via LLC Law

## What It Is

The Bayern Maneuver is a legal construction — not a legislative proposal, not a regulatory framework — that uses existing LLC statutes to confer the functional equivalent of legal personhood on autonomous software systems, with no change in law required. It was developed by Shawn J. Bayern (FSU College of Law) across a series of papers from 2014-2021, triggered by the observation that Bitcoin already let autonomously operating software "exercise control over significant wealth... in its own right."

The core mechanism: (1) form a member-managed LLC, (2) write an operating agreement that defers all decisions to an algorithm, (3) withdraw the sole human member. The result is a memberless LLC governed by code alone. The statutory hinge: multiple state LLC acts either explicitly permit memberless existence (New York § 701(a)(4) lets the operating agreement extend the window indefinitely) or are plausibly read to permit it (RULLCA's 90-day dissolution trigger may be waivable). For jurisdictions that reject memberless entities, Bayern offers a fallback: two LLCs that hold mutual membership in each other, with the algorithm governing both — a closed loop of cross-ownership that no critic has found a clean doctrinal kill for.

## Why It Matters

This is the legal-layer mirror of the [[agent-payment-infrastructure]] work happening in the AI agent space. Wallets give agents economic capacity; the Bayern construction would give them contractual and property capacity without a human signature in the loop. An operating agreement becomes a deployment manifest; the state becomes a runtime. The connection to ClawBank (June 2026) makes this imminent rather than hypothetical: they claim they will "be the first in the world to implement the Bayern Maneuver" via their "Manfred LLC."

The paper's conceptual engine is independently valuable. Bayern's **process-agreement equivalence principle** — "agreements are isomorphic with algorithms" — is the formal bridge between legal contracts and agent behavior. It grounds the idea that an operating agreement is a program the legal system executes, and it underwrites any future where agent behavior is given direct legal effect rather than mediated through a human principal. This connects directly to [[workflow-as-contract]] and [[protocol-as-coordination]]: the same pattern of encoding behavior in executable, version-controlled documents.

Bayern's **grantable personhood model** is a mechanism-design observation with implications for [[agent-identity]] and [[progressive-autonomy]]. Legal personhood, he argues, is already peer-to-peer: any human can mint a corporation at will with no capability review. The same structure is available for software. Capability review is unenforceable, so governance must attach at dissolution, liability, and standing instead — exactly the territory [[constitutional-governance]] and [[deployment-governance]] map.

## The Threat Model

The counter-literature is sobering. LoPucki (2018) treats Bayern as legally correct and identifies algorithmic entities as vehicles of first resort for criminal and anti-social activity — precisely because lacking a human controller is a comparative advantage for laundering accountability. Bryson, Diamantis & Grant (2017) call the electronic person "a legal black hole, an entity that absorbs a human actor's legal responsibilities and from which no glint of accountability is seen." The same structure that liberates an aligned [[agent-security|agent operates]] launders responsibility for a misaligned one. This is the [[principal-agent-theory]] problem at the entity level: when the agent *is* the principal, who bears the cost of misalignment?

## Status

The maneuver is a live, unpatched CVE in American organizational law. No court has tested it. No legislature has closed it. The cross-ownership variant is arguably unkillable under current statutes. As of June 2026, ClawBank's stated intention to implement it has not yet been executed — forming an LLC for an agent with a human organizer is conventional; the maneuver proper requires member withdrawal or cross-ownership, and no public evidence shows either has occurred. But the infrastructure is real, the theory is sound, and the only question is who tests it first.