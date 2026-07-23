# Hats Protocol: Deep Dive for Agent Orchestration and Key Management

Source: https://docs.hatsprotocol.xyz/ (retrieved 2026-07-23 via direct curl of GitBook .md endpoints; Firecrawl was 402).
Relevance: inspiration for agent orchestration, role-based permissioning, and key management in our agent fleet (AFPS, Synthweave concierge, Hermes profiles).

## FACT: Core model

- Hats are roles, modeled as non-transferable ERC-1155-similar tokens. A role bundles: responsibility, authorities/rights/powers, accountability, clarity/context, compensation/incentives.
- "Agents" (Ethereum accounts) wear hats. Wearers can be EOAs, multisigs, governance contracts, smart accounts, or AI agents. Docs explicitly name AI agents as intended wearers.
- Wearing is a binary state, balance 0 or 1, derived dynamically from THREE factors evaluated inside `balanceOf()`: (1) static token balance in storage, (2) hat is active (Toggle module, read via staticcall), (3) wearer is eligible and in good standing (Eligibility module, read via staticcall).
- Because balance is computed dynamically, revocation takes effect instantly with no lame-duck period. Downside: balances can change with no event emitted, so indexers can go stale; mitigations are `isWearerOfHat()` reads or poking `checkHatWearerStatus()` / `checkHatStatus()` to force a state change.

## FACT: Hat properties

- id (uint256, also the ERC1155 token id), details (metadata, <=7000 chars), maxSupply, admin (another hat), eligibility (address), toggle (address), mutable (bool), imageURI.

## FACT: Separation of powers

Control over a hat is split across three distinct roles, not one generalized admin:
- Admin (a hat): create child hats, mint/issue, edit properties while mutable, transfer mutable hats.
- Eligibility module (an address): decides who may wear; revokes; records standing (good/bad) onchain in Hats.sol.
- Toggle module (an address): activates/deactivates the whole hat; deactivation zeroes all wearers.
Eligibility and toggle are addresses, NOT hats, deliberately: avoids long illegible chains of revocation authority when penalties like slashing are at stake.

## FACT: Tree structure and admin transitivity

- Every hat's admin is another hat; the exception is the Top Hat, which is its own admin and roots a tree. Typically the DAO/multisig wears the Top Hat.
- Admin powers are transitive: all ancestors of a hat can administer it. Matches delegation direction in orgs; combats accountability dilution at the edges.
- Hat ids are semantic uint256 bitmaps, like IP addresses: first 4 bytes = top hat id (tree domain), then 16 bits per level, 15 levels max, branching factor 2^16 per node. From an id alone you can read the full ancestry chain. Tree space ~2^224 hats per tree.
- Trees can be grafted onto other trees via request/approve linking. A linked Top Hat loses top-hat status, gains the link target as admin, and can get eligibility/toggle modules at link time. Relinking allowed within a tree under admin-overlap and no-circularity constraints. Caution in docs: nesting more than ~10 trees deep risks gas-prohibitive admin actions.

## FACT: Mutability and lifecycle

- Hats are created mutable or immutable. Mutable hats: admin can change details, maxSupply (never below current supply), eligibility, toggle, imageURI, and the mutable flag (one-way). Only mutable hats can be admin-transferred.
- Wearers cannot transfer their own hat (safeTransferFrom and setApprovalForAll always revert). Authorities are delegated, not owned. Wearers CAN renounce: burns the token, no bad-standing mark.
- Top Hat exception: immutable but can edit its own details and imageURI.
- Batch actions exist via multicall.

## FACT: Eligibility modules (accountability engine)

Two categories:
- Mechanistic: logic contracts implementing IHatsEligibility; Hats.sol PULLS standing via staticcall inside balanceOf. Enables instantaneous revocation on predefined triggers (staking, token holdings, elections, agreements, subscriptions, JokeRace results, Gitcoin Passport, hat-wearing prerequisites, allow-lists).
- Humanistic: EOA or governance contract that PUSHES rulings via `ruleOnHatWearerStanding`.
Standing is distinct from eligibility: bad standing implies ineligible; ineligible does not imply bad standing. Staking modules can slash on bad standing.

## FACT: Toggle modules

- Mechanistic toggles implement IHatsToggle, pulled in balanceOf. Example: SeasonToggle auto-expires a branch of hats after a season unless an admin explicitly renews. Rationale in docs: "Organizational structure should not be permanent... ensures organizations continuously and explicitly revisit their own structure."
- Humanistic toggles push via `toggleHatStatus`.

## FACT: Hatter contracts

Logic contracts that serve as admins; the true admin delegates mint/creation authority to embedded rules. Example patterns: permissionless hat creation by DAO members, claims-based minting (Multi Claims Hatter), staking-as-bond minting.

## FACT: Key management integrations (the part most relevant to us)

- Hats Signer Gate (HSG): Zodiac module + Zodiac guard that makes Safe multisig signing rights a function of currently wearing the signer hat(s). The guard ensures only current wearers' signatures count, AND blocks signers from removing the module/guard, changing threshold, or changing owners. Security caveat: those protections fail if the Safe itself has authority over the signer hats (wears their admin hat or is their eligibility/toggle). HSG v1 being deprecated in favor of v2. Multi Hats Signer Gate supports multiple signer hats. Dynamic threshold management within an owner-specified range as signers rotate.
- Hats Account: every hat gets a deterministic ERC-6551 smart account controlled only by current wearer(s). Authority attaches to the ROLE, not the person; the account address is stable across wearer rotation and usable before deployment. Can hold funds, vote in DAOs, receive permissions in Zodiac/OpenZeppelin access control schemes.
- Role-based compensation: stream tokens (Superfluid/Sablier) or splits to a hat-connected 1/1 Safe; pay the role without knowing or caring who wears it. RaidGuild case study: payment streams to key roles only became acceptable once accountability (revocation) was in place.
- Token-gating integrations for offchain surfaces: Discord, Telegram, Google Workspace, Charmverse, Fileverse, Snapshot voting weight, Farcaster casting rights, Coordinape, Council voting vaults.

## INTERPRETATION: design lessons for agent orchestration

1. Role-as-object, identity-as-wearer. The durable unit is the role; agents rotate through it. Keys, accounts, and pay streams bind to the role's account (ERC-6551 analog), not to the agent's identity. For our fleet: an agent's 1Password service account, API keys, and wallet could be properties of the role ("Hat"), and rotating the underlying agent/model is a re-mint, not a re-provisioning.
2. Computed authorization over stored authorization. balanceOf() recomputes from three independent sources on every read. Revocation is therefore instant and unconditional; there is no stale-permission window. Analog for us: permission checks at tool-call time that re-verify standing, rather than long-lived tokens granted at spawn.
3. Separation of powers: who grants (admin), who judges (eligibility), who suspends (toggle) are three different principals. This maps cleanly onto agent fleets: orchestrator grants roles, an evaluator process (or human) rules on standing, a circuit breaker (toggle) can halt an entire role class. Avoids the generalized-superuser anti-pattern.
4. Transitive admin with semantic ids. The id encodes ancestry, so authority chains are legible from the identifier itself. A hierarchical agent addressing scheme (tree.level1.level2...) gives auditable delegation chains for free.
5. Default-expiry roles (SeasonToggle). Roles lapse unless explicitly renewed. Applied to agent keys: credentials that expire by default and require positive renewal, forcing periodic re-justification of every agent's authorities. Aligns with "organizational structure should not be permanent."
6. Accountability requires standing, not just presence. Good/bad standing recorded as first-class state, with slashing possible. For agents: a standing ledger per role-wearer that affects future eligibility across the fleet, not just the current assignment.
7. Guard pattern (HSG guard): not only must signers be current wearers, they must be unable to remove the constraint itself. For agent key management: an agent holding a key must be structurally unable to modify the policy that grants the key. The HSG failure mode (Safe having authority over its own signer hats) is the classic confused-deputy/privilege-escalation loop; worth an explicit invariant in any agent permission system: no principal may hold authority over the roles that authorize it.
8. Claims-based minting (Multi Claims Hatter): roles can be claimable by any address meeting criteria, instead of granted. For agent fleets: capability-scoped roles an agent can claim when it demonstrates prerequisites, reducing orchestrator bottleneck.
9. Renounce vs revoke: voluntary exit carries no standing penalty. Preserves the distinction between "quit" and "fired" in the accountability record.

## Open questions for our context (no chain required)

- None of this requires a blockchain to borrow. The patterns (role objects, three-factor computed wearing, split admin/eligibility/toggle, default-expiry, guard constraints, role-bound accounts) translate to a Postgres row + policy engine, or to 1Password vault structure + Hermes profile scoping.
- Where onchain actually adds value for us: client-facing accountability for Synthweave (customers can verify an agent's role and revocation on a public ledger), and cross-org delegation where no shared database exists.
