---
title: "Farewell to DAOs: Legitimacy Infrastructure for New Organizational Forms"
tags: [finding, dao, legitimacy, governance, crypto, agent-native, coordination, organization-design]
related:
- protocol-as-coordination
- hats-protocol-agent-orchestration
- agent-native-operations
- constitutional-governance
- crypto-as-agent-infrastructure
- openclaw
- multi-agent-coordination-patterns
- institutional-ai-redesign
source: research/raw/farewell-to-daos-towards-legitimacy-infrastructure.md
ingested: 2026-08-04
---

# Farewell to DAOs — Legitimacy Infrastructure for New Organizational Forms

The essay: "Farewell to DAOs: Towards legitimacy infrastructure for new organizational forms" by Sam McCarthy, Nick Almond, Spencer Graham, Bbeats, Joshuaz Tan, and Trent Van Epps. Published as an X essay 2026-07-28. The argument: v1 DAOs are dead (not trending toward death, but substantively finished as a viable organizational form). The replacement is not a better DAO, but a reframing of what DAOs are for: *legitimacy infrastructure* for a plurality of new organizational forms yet to emerge.

## The Central Reframe

DAOs as they were conceived — token-holder-governed blockchain organizations — have failed. Not because the technology was wrong, but because the demand for them collapsed and their legitimacy never landed. The two forces that sustained v1 DAOs are both gone: regulatory arbitrage pressure from the SEC is over, and the speculative capital that flowed into crypto treasuries has left. What remains is a skeleton of broken mechanisms: one-token-one-vote, the foundation model, token-equity dual structures, Governor Bravo forks everywhere. The essay's reframe: stop treating DAOs as an organizational destination and start treating them as **infrastructure for legitimacy** — a modular toolset that lets new organizational forms produce the guarantees and observability that stakeholders, regulators, and counterparties need before they will coordinate at scale.

## The Legitimacy Framework

Legitimacy, in this framing, is what lets an organization secure resources, validate its operations to stakeholders, and defend itself against crises. It is underpinned by performance: organizations legitimate themselves by coordinating better outcomes than markets alone can produce, at lower coordination cost than incumbent forms. Hayek and Coase make a cameo here: corporations won because their information systems handled the knowledge problem better. DAOs undermined the corporate information system (removed hierarchy, blurred boundaries, decentralized control) without building a replacement. Result: asymmetric information bloomed, coordination costs rose, stakeholders could not see or interpret what was happening inside, and legitimacy never arrived. The essay cites Alex Preda's *Framing Finance* on "observational boundaries" — the lens through which external observers validate internal actions — as the missing piece.

## The Original Sins of DAOs

Three sins saturate the v1 landscape and explain why the legitimacy never arrived. **Governing everything by fiat of token-weighted vote** (one mechanism misapplied to every decision, mismatching the mechanism to the information structure). **Confusing decentralized ownership with legitimate authority** (airdropping control to anyone who claimed tokens, with no thought to whether those claimants could produce good outcomes). **Performative decentralization as regulatory cover** (the "democracy theater" that masks traditional company operations behind a thin veneer of onchain governance). Together these produced radical populist structures with no accountability framework, no alignment mechanism, and no animating purpose beyond regulatory avoidance. The sins ossified into defaults — Governor Bravo forks everywhere — because the drive for legitimacy pushed organizations toward the most legible inherited structure rather than the most appropriate one.

## The v2 Proposition

Two parts. **Decompose DAOs to their fundamental components**: their technical guarantees (smart contract execution, cryptographic verifiability, unstoppable protocols) and their legible systems of coordination (onchain attestations, multisig permissioning, public money flows). **Encourage dynamic experimentation** with modular architectures that reconfigure boundaries task-by-task, combining markets, hierarchies, protocols, and agents dynamically rather than applying one mechanism to everything. The essay lists five components that help legitimate outputs: credible commitments through staking, formal verification through onchain proofs, permissioning through multisignature wallets, onchain attestations for attribution, and public transactions for accountability. The endpoint: DAOs as the mediator between human and technological actors, making the boundary legible in both directions — the thing that lets you answer "who decided this and why" when half the actors are agents.

## Significance for Substrate

This essay lands directly on the Substrate thesis. When we describe the vault as institutional memory for an agent fleet, we are describing legitimacy infrastructure: the thing that makes agent operations observable, interpretable, and accountable to principals. The mapping from "legible systems of coordination" to the Substrate's raw/findings/insights layers is near-exact — we are building the observational boundary. When the essay says DAOs will become "an early site of AI agent integration" where the corporate form's advantage (siloed human hierarchies) weakens, it is describing the market for what we're building. The Tally founder quote ("there isn't a venture-backed business in governance tooling for decentralized protocols") is a warning and an opportunity: governance tooling collapsed with v1 DAOs, but legitimacy tooling for agent organizations is the open category. The essay's list of five components — credible commitments, formal verification, permissioning, attestations, public transactions — reads as a requirements document for the [[agent-identity]] layer. Notably, the authors co-wrote with contributors from the Hats Protocol ecosystem, connecting this essay directly to [[hats-protocol-agent-orchestration]]: the role-based, revocable, computed wearing pattern is the working implementation of "legitimate authority" that the essay describes abstractly.

## Critical Assessment

The essay is persuasive on diagnosis and vague on prescription. The five legitimating components are listed but not architected — no mechanism design, no cost analysis, no comparison of which coordination tasks should use which mechanism. The "dual proposition" (decompose, then experiment) is correct but obvious; the hard part is the sandbox design, which the essay gestures at with "observable sandboxes" without specifying who runs them or what success criteria look like. The most interesting tension: the essay argues DAOs will outcompete incumbents for "the social authority to coordinate human and technological actors at scale," but offers no theory of why DAO-based architectures specifically will win that competition over, say, improved corporate structures with better information systems, or purpose-built agent-native registries that skip blockchain entirely. The blockchain commitment is asserted ("blockchains need DAOs, just like DAOs need blockchains") rather than argued — a founder-of-a-DAO-tooling-platform would say that. The diagnosis section is the durable contribution: v1 DAOs failed not from bad code but from legitimacy collapse, and any successor must solve the observability problem first. That is a real insight worth keeping. Everything after the reframe is directionally right but operationally thin.

## The Co-Author Network

Six authors: Sam McCarthy (the poster), Nick Almond, Spencer Graham, Bbeats, Joshuaz Tan, Trent Van Epps. Almond and Graham are the authors of [[hats-protocol-agent-orchestration]] — the Hats Protocol whitepaper on role-based permissions for agent fleets. Reading the two papers together: Hats is the implementation of the legitimacy infrastructure essay's *permissioning* component (multisig, revocation, role-bound accounts). The essay is the ideological wrapper; Hats is the working mechanism. This suggests a coordinated research program across the DAO tooling diaspora, with legitimacy as the framing concept connecting governance theory to role-based agent permissions.

## Connections

- [[protocol-as-coordination]]: the broader frame for why coordination mechanisms matter beyond markets
- [[hats-protocol-agent-orchestration]]: the working implementation of legitimate, revocable authority for agents
- [[agent-native-operations]]: agents as first-class participants in organizational decision-making
- [[constitutional-governance]]: governance as codified rules with enforcement mechanisms
- [[crypto-as-agent-infrastructure]]: blockchains as the settlement and identity layer for agents
- [[openclaw]] and [[the-openclaw-lesson]]: what happens when agent tooling collapses; legitimacy never arrived
- [[multi-agent-coordination-patterns]]: hierarchical, blackboard, peer-to-peer, market-based coordination — the essay's "task-by-task reconfiguration" is a fifth pattern (dynamic mechanism composition)
- [[institutional-ai-redesign]]: the parallel argument that organizations have not been redesigned around AI; this essay makes the same point for DAOs
- [[principal-agent-theory]]: the accountability framework problem the essay identifies (agents about principles)
- [[proof-of-work]]: credible commitments via mechanism, the staking primitive
- [[ricardian-contract-agent-economy]]: contracts as legible coordination artifacts, the ancestor of "legible systems of coordination"
