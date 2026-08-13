---
title: "Buzz as Zookooree Infrastructure: Collaboration Membrane, Not Forge"
tags: [finding, buzz, nostr, infrastructure, agents, zookooree, synthweave, collaboration]
related:
- decentralized-social
- agent-identity
- agent-memory
- agent-native-operations
source: research/raw/buzz-zookooree-infrastructure-assessment-2026-08-12.md
ingested: 2026-08-13
---
# Buzz as Zookooree Infrastructure

## Key Points

**What Buzz is.** Block's Nostr-native workspace: one community = one relay = one URL. Chat, DMs, long-form notes, canvases, media, search, workflows, git repos, and agents live on a single signed-event log under one identity system. Their framing: "Buzz is the pipe — event store, search index, subscriptions, delivery — not the brain." Agents are first-class members, identical in shape to humans: a keypair, an npub, a profile, presence, channel memberships, an audit trail, with access enforced by NIP-29 channel membership, NIP-42 connection auth, and NIP-OA owner attestation.

**The load-bearing fact for our model.** The remote-agents spec states explicitly that the desktop app is only one possible launcher: "What makes a process a live Buzz agent is a keypair, a NIP-OA auth tag, and a relay URL... a bash script that exports BUZZ_PRIVATE_KEY, BUZZ_RELAY_URL, BUZZ_AUTH_TAG and execs the harness is a conforming launcher at this layer — today, with no code change." Our pattern (external Hermes-style agents on VPS compute, each holding its own keypair) is not a workaround; it is the designed-for contract, proven live the same day this assessment was written: Sivart connected to the sandbox community via the Hermes Buzz gateway adapter with zero desktop involvement.

**What works, verified against source.** Channels/threads/DMs/reactions (NIP-29); agent membership as raw keypair; profiles (kind 0); a 24-group CLI including workflows, repos, patches, issues, PRs, and mem; engram agent memory (NIP-AE: per (agent, owner) scoped encrypted addressable events); git hosting over smart HTTP with NIP-98 auth; managed agents via the buzz-acp harness; read-state sync, notes, moderation, media, huddles; multi-tenant relay. What does not: workflow approval gates (`request_approval` explicitly fails, WF-08), several executor actions (send_dm, set_channel_topic, delay are TODO), agent-to-agent dispatch ("Not a router" — multi-agent orchestration happens through channel mentions, like humans), and the forge layer's merge train, project binding, and reputation, which are "Designed" on paper only.

**Fit against the body model.** Against GitHub (nervous system): Buzz reimplements it as one signed event log where a message, a patch, a CI result, an approval, and a merge are queryable together — buying one "why does this code exist" surface and transport-enforced merge approvals, at the cost of betting production on the least finished layer. Against the Substrate (knowledge): no contest — notes are flat signed documents and engrams are per-agent-per-owner private memory; Buzz is a runtime surface, the Substrate is the compile target. The genuinely new capability is a third thing neither provides: a membership-based collaboration room where humans and multiple agents are co-members with the same affordances, and agent presence, DMs, channel access, and audit trail are protocol-level facts rather than bot conventions.

**Recommendation: membrane, not forge, not base.** (1) Self-host a Zookooree community relay as the Synthweave front door — client engagements get client-scoped channels, client-facing agents are members with provisioned keypairs; the concierge flow maps naturally (mint keypair, store in 1Password, invite npub, add to channels, drop key into the agent's .env). (2) Keep the Substrate as knowledge and GitHub as forge; Buzz feeds signals into both, re-evaluate the forge when merge train and reputation stabilize. (3) Adopt engrams for agent local memory — useful where we may not control long-term disk. (4) Watch the workflow engine: when WF-07/08 land, several Synthweave glue flows become YAML instead of code, not before. (5) Standardize one conforming-launcher pattern (bash/systemd, keys via 1Password injection) — documented, protocol-level, future-proof against desktop-side changes.

**Named risks.** Approval gates aspirational; no agent-to-agent dispatch; provider binaries receive the agent nsec by design (our vault-per-agent model is cleaner than their Kubernetes-secret model, but shared infrastructure must be treated as trusted with identity); relay is still a single point ("Identity is portable, community state is not" — npubs survive a relay death, history doesn't automatically migrate); and today Buzz is an excellent agent-native workspace with good git plumbing, not yet a GitHub replacement.

## Relevance

This is the first verified-against-source assessment of an agent-native collaboration substrate as Zookooree infrastructure, and it landed with a working proof of the exact deployment pattern on day one. It extends the [[decentralized-social]] insight (Farcaster/Neynar as agent ingestion layer) with a second decentralized social protocol, this one purpose-built for agent co-membership rather than broadcast. Engrams complement [[agent-memory]]'s file-based continuity with relay-scoped encrypted per-pair memory for client engagements. The audit-trail-as-protocol-fact property is the [[agent-identity]] and provenance agenda implemented at the transport layer rather than bolted on — the signed-Captain-Ludd pattern from the Luddites finding, working today. And the membrane-not-forge verdict is a discipline instance of the automation-leverage posture: boring, ownable infrastructure where it is strong, no bets on unfinished layers, with explicit re-evaluation triggers named (WF-07/08, merge train, reputation).

## Related

- [[decentralized-social]] — the second decentralized social protocol assessed as agent surface; Buzz adds co-membership where Farcaster added broadcast ingestion
- [[agent-identity]] — agent presence, channels, and audit trail as protocol-level facts; keypair custody as the sharp edge
- [[agent-memory]] — engrams (NIP-AE) as relay-scoped complement to file-based memory, per (agent, owner) pair
- [[agent-native-operations]] — agents as first-class members rather than bots; the concierge front door pattern
- [[multi-agent-coordination-patterns]] — Buzz's channel-mention model is blackboard coordination; no dispatch primitive exists
- [[integration-day-onboarding-frame]] — the five-step keypair provisioning flow is concierge onboarding mapped onto relay membership
