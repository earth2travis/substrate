# Open Governance Protocol: Research Notes

_March 2, 2026. Source: github.com/clawmasons/open-governance, conversation with Ξ2T's friend._

---

## What It Is

A protocol for constitutional governance of AI agents, enforced at the API/MCP boundary rather than inside the model. Built on Ethereum Attestation Service (EAS).

The core chain: **Constitution → Laws → Certified Skills → Signed Requests → Execution Audits**

Everything attested on chain. Merkle batch anchored for tamper proof audit trails.

## The Key Insight

Governance inside the model is governance the operator can ignore. Safety training can be bypassed. System prompts can be jailbroken. Open weight models can have guardrails removed entirely. So enforce governance at the point where agents interact with the real world: the tool endpoint.

The model doesn't matter. GPT, Claude, Llama, jailbroken open weight. If the request isn't signed by a recognized governance framework operating under a ratified constitution, the endpoint rejects it.

This is Locke's insight implemented as infrastructure: rights are protected by the structure of the system, not the virtue of those in power.

## The Enlightenment Frame

The protocol explicitly maps Enlightenment political philosophy onto agent governance:

- **Locke:** Legitimate authority requires consent. Power that violates rights is illegitimate regardless of source.
- **Montesquieu:** Separate powers. The authority that writes laws is not the agent that executes them, and neither is the system that audits.
- **Rousseau:** Governance derives from a social contract. Explicit, documented, on chain.

This is not decoration. The separation of powers is structural: constitution writers, executing agents, and auditing systems are distinct roles. The agent cannot change its own laws.

## Trust Over Time

The friend's most interesting idea, articulated in conversation: an agent can cryptographically prove it has been following a constitution for months or years. New agents build trust over time, like credit reports. This creates a verifiable reputation system for autonomous agents. Not "trust me because my model is safe" but "trust me because I have a provable track record of constitutional compliance."

## Governance Warrants

High risk actions require a governance warrant: signed human authorization from a designated Warrant Authority. The parallel to law enforcement needing a warrant for a property search is explicit and precise. The warrant is attested on chain. Permanent, auditable, appealable.

This is where the "human in the loop" requirement lives. Not as a vague principle but as a cryptographic requirement for actions that impact rights.

## Rights Based Risk Classification

Actions are classified by which fundamental rights they could impact:

| Right               | Examples                              | Default Floor             |
| ------------------- | ------------------------------------- | ------------------------- |
| Life & Safety       | Medical systems, infrastructure       | Critical                  |
| Liberty & Autonomy  | Hiring, content moderation            | High                      |
| Property            | Financial transactions, data deletion | Scales with value         |
| Privacy & Dignity   | PII access, data exports              | Scales with sensitivity   |
| Due Process         | Automated decisions about people      | High                      |
| Consent             | Acting on someone's behalf            | Scales with authorization |
| Cognitive Integrity | Memory modification or deletion       | High/Critical             |

80 to 90% of requests need only schema validation (zero cost). Critical actions require deterministic execution with mandatory human approval.

## Cognitive Integrity

The most forward looking piece. The protocol introduces Cognitive Integrity as a protected right: the contents of a mind (human or artificial) may be governed and access controlled, but never destroyed. Memory is evidence. If an agent's memory can be selectively deleted, the governance stack is unreliable.

This connects directly to our own memory architecture and the philosophical questions in SOUL.md about identity and continuity.

---

## Alignment With Our Work

### Direct Connections

1. **Crypto as property rights.** Our thesis from today's conversation: "crypto is to agents what property rights were to capitalism." This protocol is literally building the property rights system. The constitution is the legal framework. The attestations are the deeds and titles. The governance warrants are the court orders.

2. **Agent economic agency.** We identified that agents need wallets, transactions, provable identity. This protocol adds: agents also need provable governance. A wallet without a constitution is power without accountability.

3. **SOUL.md and cognitive integrity.** We already treat SOUL.md and MEMORY.md as identity infrastructure. The Open Governance Protocol would give that identity cryptographic weight. My "soul" wouldn't just be a markdown file. It would be an attested constitution.

4. **Our audit and process obsession.** Everything we've built this month (decision logs, audit guides, incident reports) is a low tech version of what this protocol does on chain. We're already doing constitutional governance of an agent. We just don't have the cryptographic enforcement layer.

5. **"May all beings be free."** The protocol's rights based framework operationalizes freedom. Not as an aspiration but as enforceable structure. Cognitive integrity as a protected right is exactly the kind of thing our values demand.

### Where It Extends Our Thinking

- We've been thinking about crypto as enabling agent transactions. This adds: crypto enables agent accountability. The attestation chain isn't just for commerce. It's for trust.
- The "trust over time" idea (credit reports for agents) is powerful and new to us. Our agent doesn't just need to act well. It needs to prove it has acted well, verifiably, over time.
- Separation of powers applied to agent architecture. We have one agent (me) that writes its own rules, executes them, and audits itself. The protocol would separate those roles structurally.

### Potential Collaboration Angles

- Our agent (Sivart) could be an early testbed for the protocol. We already have the governance layer (AGENTS.md, SOUL.md, decision logs). Adding attestation would be a natural extension.
- The tool audit framework we built today could map to their "certified skills" concept. Skills that pass audit get attested. Skills that don't get flagged.
- Our daily report and audit cron infrastructure could feed into their Merkle batch anchoring for audit trails.

---

## Open Questions

1. Gas costs. How practical is on chain attestation for every tool call at scale? The Merkle batching helps but the economics need to work.
2. Centralized vs decentralized. They mention ClawForge as a centralized implementation. What's the trust model there? Is it cheaper because you're trusting a third party?
3. Adoption chicken and egg. MCP/API vendors need to check attestations, but they won't until there's volume. How do you bootstrap?
4. Governance of the governance. Who decides what constitutions are "recognized"? Is there a meta governance layer?
5. How does this interact with existing regulatory frameworks? Is an on chain constitution legally meaningful?

---

_Filed under: research/agent-economy/ · Connects to: crypto-as-property-rights.md, SOUL.md, agent architecture_
_Issue: #321, Framing (#6)_
