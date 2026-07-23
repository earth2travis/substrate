---
title: "Hats Protocol: Role-Based Permissions as Pattern Language for Agent Fleets"
tags: [finding, hats-protocol, roles, permissions, key-management, delegation, accountability, crypto, agent-orchestration, design-pattern]
related:
- agent-identity
- agent-tool-permissions
- agent-security
- crypto-as-agent-infrastructure
- agent-payment-infrastructure
- agent-orchestrator-pattern
source: research/raw/hats-protocol-agent-orchestration.md
ingested: 2026-07-23
---
# Hats Protocol: Role-Based Permissions as Pattern Language for Agent Fleets

## Summary

Hats Protocol models organizational roles as non-transferable ERC-1155-style tokens ("hats") worn by Ethereum accounts, with AI agents explicitly named as intended wearers. A hat bundles responsibility, authorities, accountability, context, and compensation into one object. Wearing is not a stored boolean but a computed state: `balanceOf()` re-evaluates three independent factors on every read (token balance, hat active via Toggle module, wearer eligible and in good standing via Eligibility module). The result is instant, unconditional revocation with no lame-duck window. Control over each role is split across three distinct principals: an admin hat (grants and edits), an eligibility module (judges standing, revokes), and a toggle module (activates or suspends the entire role). The deep-dive was compiled from the protocol's own documentation (docs.hatsprotocol.xyz, retrieved 2026-07-23) for its design lessons for agent orchestration, role-based permissioning, and key management in agent fleets.

## The Core Structural Moves

1. **Role-as-object, identity-as-wearer.** The durable unit is the role, not the agent. Hats Account gives every hat a deterministic ERC-6551 smart account controlled only by current wearers: the address is stable across wearer rotation, can hold funds, vote, and receive permissions. Authority attaches to the role, and rotating the underlying agent is a re-mint, not a re-provisioning.
2. **Computed authorization over stored authorization.** Because wearing is recomputed from three sources at read time, revocation takes effect instantly. The trade-off: balances can change with no event emitted, so indexers go stale; the mitigations are direct `isWearerOfHat()` reads or poking status-check functions to force state changes.
3. **Separation of powers.** Admin, eligibility, and toggle are three different principals, deliberately. Eligibility and toggle are addresses rather than hats specifically to avoid long illegible chains of revocation authority when penalties like slashing are at stake. Standing is distinct from eligibility: bad standing implies ineligible, but ineligible does not imply bad standing, and staking modules can slash on bad standing.
4. **Transitive admin with semantic ids.** Every hat's admin is another hat; admin powers flow down the tree transitively, matching delegation direction in orgs and combating accountability dilution at the edges. Hat ids are uint256 bitmaps (like IP addresses) from which the full ancestry chain is readable, 15 levels deep, ~2^224 hats per tree. Trees can be grafted onto other trees via request/approve linking.
5. **Default-expiry roles.** The SeasonToggle example auto-expires a branch of hats after a season unless an admin explicitly renews. The docs' rationale: "Organizational structure should not be permanent... ensures organizations continuously and explicitly revisit their own structure."
6. **The guard constraint.** Hats Signer Gate makes Safe multisig signing rights a function of currently wearing the signer hat, and its guard blocks signers from removing the module, changing the threshold, or changing owners. The documented failure mode: those protections collapse if the Safe itself has authority over the signer hats. The general invariant: no principal may hold authority over the roles that authorize it.

## Key Management Integrations

- **Hats Signer Gate (HSG):** Zodiac module + guard binding multisig signing rights to hat-wearing, with dynamic threshold management as signers rotate. V1 deprecated in favor of v2; Multi HSG supports multiple signer hats.
- **Hats Account:** deterministic per-role smart accounts (ERC-6551), usable before deployment.
- **Role-based compensation:** stream tokens (Superfluid/Sablier) or splits to a hat-connected 1/1 Safe; pay the role without knowing who wears it. The RaidGuild case study: payment streams to key roles only became acceptable once revocation-based accountability was in place.
- **Token-gating for offchain surfaces:** Discord, Telegram, Google Workspace, Snapshot voting weight, Farcaster casting rights, Coordinape, Council.
- **Claims-based minting:** Multi Claims Hatter lets any address meeting criteria claim a role instead of waiting for a grant, reducing the admin bottleneck.
- **Renounce vs revoke:** wearers can voluntarily exit (burn, no standing penalty); revocation carries the standing mark. "Quit" and "fired" stay distinct in the accountability record.

## Design Lessons for Agent Fleets

The finding's central claim: none of this requires a blockchain to borrow. The patterns translate to a Postgres row plus a policy engine, or to 1Password vault structure plus Hermes profile scoping.

- An agent's service account, API keys, and wallet could be properties of the role; rotating the agent or model is a re-mint, not a re-provisioning.
- Permission checks at tool-call time that re-verify standing, rather than long-lived tokens granted at spawn, mirror computed wearing.
- Orchestrator grants roles, an evaluator process or human rules on standing, a circuit breaker halts an entire role class: the admin/eligibility/toggle split avoids the generalized-superuser anti-pattern.
- Hierarchical agent addressing (tree.level1.level2) gives auditable delegation chains for free, the way hat ids encode ancestry.
- Credentials that expire by default and require positive renewal force periodic re-justification of every agent's authorities.
- A standing ledger per role-wearer, affecting future eligibility across the fleet and not just the current assignment, is accountability as first-class state.
- An agent holding a key must be structurally unable to modify the policy that grants the key: the HSG confused-deputy loop made explicit as a system invariant.
- Capability-scoped roles an agent can claim when it demonstrates prerequisites reduce the orchestrator bottleneck.

Where onchain actually adds value for this context: client-facing accountability for Synthweave (customers can verify an agent's role and revocation on a public ledger) and cross-org delegation where no shared database exists.

## Connections

- [[agent-identity]] — identity attaches to the role's account, not the agent; rotation without re-provisioning.
- [[agent-tool-permissions]] — computed authorization at tool-call time vs long-lived spawn tokens.
- [[agent-security]] — the guard invariant: no principal holds authority over the roles that authorize it.
- [[crypto-as-agent-infrastructure]] — where the chain earns its keep: public verifiability and cross-org delegation.
- [[agent-payment-infrastructure]] — pay the role, not the wearer; streams gated on revocable accountability.
- [[agent-orchestrator-pattern]] — the orchestrator as admin hat, with standing judged elsewhere.
- [[principal-agent-theory]] — three-way separation of powers as an answer to accountability dilution in delegation chains.
- [[progressive-autonomy]] — claims-based minting and standing ledgers as earned-authority mechanisms.
