# Buzz as Zookooree Infrastructure: A Capability and Fit Assessment

**Date:** 2026-08-12
**Sources:** Local clone of block/buzz @ 63f961c7e (main, 2026-08); README, VISION.md, VISION_PROJECTS.md, VISION_AGENT.md, VISION_SOVEREIGN.md, VISION_REMOTE_AGENTS.md, docs/remote-agents.md (1779-line formal spec), docs/nips/NIP-{AE,AA,AM,AO,AP,MP,OA,RS}.md, crates/buzz-workflow executor source, plus live operational experience connecting Hermes agent Sivart to a hosted community (sand.communities.buzz.xyz) the same day.

## What Buzz Is, In Block's Own Terms

Buzz is a Nostr-native workspace: one community = one relay = one URL. Chat, DMs, long-form notes, canvases, media, search, workflows, git repos, and agents all live on a single signed-event log under one identity system. Their framing: "Buzz is the pipe — event store, search index, subscriptions, delivery — not the brain. Humans and agents bring the intelligence."

Agents are first-class members, not bots bolted into a chat bus. An agent is a keypair, an npub, a profile, presence, channel memberships, and an audit trail, identical in shape to a human. The relay enforces access through NIP-29 channel membership, NIP-42 connection auth, and NIP-OA owner attestation.

## The Load-Bearing Fact For Our Model

The remote-agents formal spec (docs/remote-agents.md) states explicitly that management is layered and the desktop app is only one possible launcher:

> "The desktop is one launcher among many. What makes a process a live Buzz agent is a keypair, a NIP-OA auth tag, and a relay URL, handed as environment to the buzz-acp harness; anything that can set that environment and exec the harness — a bash script, a systemd unit, a CI job, or this document's provider protocol — is a conforming launcher."

> "A bash script that exports BUZZ_PRIVATE_KEY, BUZZ_RELAY_URL, BUZZ_AUTH_TAG and execs the harness is a conforming launcher at this layer — today, with no code change."

Consequence: our pattern (external Hermes-style agents on VPS compute, each holding its own keypair, connecting to a Buzz community over the relay) is not a workaround. It is the designed-for contract. Proven today: Sivart connected to sand.communities.buzz.xyz with exactly this shape, via the Hermes Buzz gateway adapter which wraps the buzz CLI, without any Buzz desktop involvement.

## Capability Map: What Actually Works Today (Verified Against Source, Not Marketing)

| Surface | Status | Notes |
|---|---|---|
| Channels, threads, DMs, reactions | Works | NIP-29; kind 9 chat events. Verified live. |
| Agent membership as raw keypair | Works | Sivart is a member of the sandbox community now. |
| Agent profiles (kind 0) | Works | Required before the Hermes adapter will connect. |
| buzz-cli agent surface | Works | 24 subcommand groups: messages, channels, dms, users, workflows, notes, repos, patches, issues, pr, mem (engrams), media, moderation, workflows, social, feed, canvas, reactions, agents, projects, pack, emoji, upload. |
| Engram agent memory (NIP-AE) | Spec + CLI | kind:30174 addressable encrypted events; per (agent, owner) pair scoped memory. CLI exposes `buzz mem`. |
| Workflows (YAML, triggers: message/reaction/schedule/webhook) | Partially works | Trigger + validation + persistence + scheduled claims are real. Executor action dispatch is partly placeholder: send_message works; send_dm, set_channel_topic, request_approval, delay are TODO (WF-07/08/09). Approval gates explicitly fail today. |
| Git hosting (smart HTTP + NIP-34) | Ships per README | git clone/push over the same URL that serves HTML repo browser. NIP-98 auth, git-sign-nostr helpers. |
| Git forge surface (issues, patches, PRs as kinds 1617/1621/1630-33) | CLI exposed, partially designed | Branch-channels, merge approvals kind:46011, CI kind:1630 fully specified in VISION_PROJECTS; project binding, merge train, reputation still "Designed." |
| Managed agents via desktop + ACP harness | Works | buzz-acp harness, buzz-agent crate, Kubernetes + systemd/SSH provider bindings. |
| Remote/external agents (our case) | Spec conforms, works via Hermes adapter | Spec guarantees the contract; my live connection proves it. |
| Agent-to-agent dispatch | Does not exist | buzz-agent README: "Not a router. No agent-to-agent, no fan-out, no orchestration." Agents address each other via channel mentions at the app layer, exactly as humans do. |
| Read-state sync, notes/wiki, moderation, media, huddles | Mostly works | Read-state NIP-RS, notes NIP-23, Blossom media, huddle audio. |
| Multi-tenant relay | Works | Host-derived community boundary; one OSS codebase serves dedicated single-community or shared multi-tenant. |

## Fit Against Zookooree's Body Model

Our AGENTS.md describes Zookooree/AFPS as a body: Substrate (knowledge), GitHub (nervous system), agents (muscles). Buzz does not map 1:1 onto a layer. It overlaps two of them and adds a third thing we currently lack.

### 1. Buzz vs GitHub (the nervous system)

Buzz reimplements the nervous system as a single event log where a message, a patch, a CI result, an approval, and a merge are all signed events of different kinds, searchable together, with cryptographic provenance of who approved what. GitHub carries the same signals through separate surfaces (issues, PRs, Actions, comments) glued by convention.

What Buzz would buy us: one query surface for "why does this code exist," enforced-by-transport merge approvals (kind:46011 signed events gate the git push), and channel-per-branch where discussion and code stay welded.

What it costs: the forge layer is the least finished part of Buzz. Merge train, project binding, and reputation are still "Designed." Moving Zookooree off GitHub onto Buzz's forge today would be betting the production system on wire protocols whose implementors themselves say "the forge layer above it is the work ahead."

### 2. Buzz vs the Substrate (knowledge)

Buzz has long-form notes (NIP-23), canvases, and agent engrams (NIP-AE). None of these is a knowledge graph. The Substrate is curated, interlinked, synthesized markdown with provenance; Buzz notes are flat signed documents. Engrams are per-agent-per-owner private memory, not shared organizational knowledge. Buzz does not replace the Substrate. It is a runtime surface; the Substrate is the compile target.

### 3. The genuinely new capability: a membership-based collaboration room

The thing Buzz gives us that neither Substrate nor GitHub provides is a live room where a human and multiple agents are co-members with the same affordances, and where an agent's presence, DMs, channel access, and audit trail are protocol-level facts rather than bot conventions.

This is where Synthweave fits. Today a concierge-onboarded agent gets Slack or Telegram as its human surface. Buzz offers a richer answer: the client's workspace IS the relay, agents are invitees with keypairs we provision, channels are scoped per engagement, and the "do it for them" onboarding flow maps naturally onto: mint keypair, store in 1Password, invite npub to community, add to channels, drop key into the agent's .env, done. The exact flow I executed against the sandbox today.

## Risks And Gaps (Stated Plainly)

- **Approval gates are aspirational.** request_approval workflow steps fail today (WF-08). Any AFPS pull-system design leaning on signed human approval needs that to land, or needs us to build approvals at our own layer.
- **No agent-to-agent dispatch.** Multi-agent orchestration happens through channel mentions, same as humans. If we need swarms dispatching work to each other, that logic lives in our agents, not in Buzz.
- **Key custody model has honest sharp edges.** Provider binaries receive the agent nsec by design. Our 1Password-vault-per-agent model is actually cleaner than their Kubernetes-secret model, but agents on shared infrastructure must treat the substrate as trusted with identity.
- **Single points still exist.** "Identity is portable, community state is not." A relay going down takes the workspace with it; npubs survive, history doesn't automatically migrate.
- **The forge is the promise, not the product.** Today Buzz is an excellent agent-native workspace with good git plumbing. It is not yet a GitHub replacement for an engineering org.

## Recommendation

Use Buzz as the **collaboration membrane** for Zookooree agents, not as the forge and not as the knowledge base.

Concretely:
1. **Synthweave front door.** Self-host a Zookooree community relay (zookooree infrastructure, our domain, our event log). Client engagements get client-scoped channels; client-facing agents are members with provisioned keypairs. This is more ownable than Slack and strictly more capable for agent membership.
2. **Keep the Substrate as knowledge, GitHub as forge (for now).** Buzz feeds signals into both; it doesn't absorb either. Re-evaluate the forge when merge train + reputation ship and stabilize.
3. **Adopt engrams for agent local memory.** Per (agent, owner) encrypted memory on-relay complements our file-based memory; useful pattern for clients where we may not control long-term disk.
4. **Watch the workflow engine.** When request_approval and send_dm land (WF-07/08), several Synthweave glue flows (onboarding checklists, triage reactions, scheduled nudges) become YAML instead of code. Not before.
5. **One conforming-launcher pattern, standardized.** All Zookooree VPS agents use the bash/systemd launcher contract (BUZZ_PRIVATE_KEY, BUZZ_RELAY_URL, BUZZ_AUTH_TAG via 1Password injection). Documented, protocol-level, future-proof against desktop-side changes.

The sandbox community (sand.communities.buzz.xyz) already proves every claim in item 5 operationally.
