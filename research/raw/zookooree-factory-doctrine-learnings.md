# Zookooree Agent Factory: Doctrine Learnings from the First Production Weekend

Source: The Zookooree Agent Factory's first production shift, 2026-07-11 to 2026-07-13. Derived from the shift's own artifacts in zookooree/the-agent-factory: `handoffs/2026-07-12-shift-end.md`, `docs/pilot-plan.md`, `docs/factory-design.md` (the six theses), and `reports/2026-07-13-trial-production.md`. These are raw learnings for synthesis, not settled doctrine documents.

## Context

Zookooree is an agent factory built on the Toyota Production System. The factory is the product; what it manufactures is verified trust. A unit (an agent, a tool, or a skill) counts as produced only when it carries a Certificate of Conformance: a bill of materials with content hashes, evidence it works, provenance, liability, and an expiry date. The public promise is "Agents you can run unattended. Claims you can check." The first customer is the factory itself. The weekend was a 3P run (Toyota's Production Preparation Process): stand up a small real line, run product through it, and harden the standard work against what breaks. Three doctrine reframings emerged from doing the work, described below.

## Learning 1: Corrosion is the organizing enemy

In a plant where nothing physically breaks, correctness and trust still decay silently. Models drift, dependencies change, documentation goes stale, knowledge rots. Nothing fails loudly; things quietly stop being true. This is the factory's rust, and because it is not caused by a defect event, no defect event catches it.

The evidence is the factory's own history, not an abstraction: everything built in a March 2026 burst was rotten by July without a single defect occurring. A credential expired quietly. An export pipeline began shipping empty placeholder files. Roadmap dates elapsed unrevised. Nothing failed; everything decayed.

The reframing: corrosion is the north-star idea, cleaner than six separate theses. The original six theses (verification is the expensive building; there are no finished goods; the andon must ring for silence; doctrine must compile; germline and soma change control; the operator's attention is the constraint) become tactics against one named enemy rather than independent principles. Each thesis maps to a specific form of corrosion: silent defects, staleness, absence, culture decay, propagated defects, and bottleneck rot. A single named enemy gives every design decision one test: does this reduce corrosion, or does it just look tidy today.

## Learning 2: "Done, and maintained," not "nothing is ever finished"

A certificate is perishable. Deployment is not exit; it is transfer from a high-frequency inspection zone to a low-frequency one. The right industrial analogy for the back half of the line is aviation's continuing airworthiness: telemetry return, scheduled re-certification, and a recall mechanism.

The reframing sharpens the earlier "nothing is ever finished" slogan into something operational: "done, and maintained." Every stage gets a real definition of done, and done is then kept alive by scheduled maintenance (re-certification on expiry or on trigger conditions like a model swap or dependency change). This is the differentiator against "shipped and forgotten" on one side and against the demoralizing "never finished" on the other. Maintenance is a first-class model, an after-sales relationship with each unit, not a virtue or an afterthought.

## Learning 3: The operator's attention is the plant's constraint, not takt

This is a one-human plant with no external customer yet, so takt time (a demand-driven rhythm) is the wrong frame. The binding constraint is the human operator's attention. Every certified unit spends that attention twice: once at intake (writing the work order and stating intent) and once at certification (accepting the claim and its evidence). Compute is not the constraint; agent throughput is not the constraint; human trust-bandwidth is.

The consequence is a Theory-of-Constraints posture (the Five Focusing Steps): identify, exploit, subordinate to, and then elevate the human constraint. The only way to raise plant capacity is verification leverage, not more agents: reference-free judges and delegated authority that turn human review from "check everything" into "audit the auditor." Overproduction is redefined as building agents faster than anyone can trust them. The honest metric is operator-touches per certified unit, trending toward zero. Delegating germline merge authority out of the operator's person (see the governance learnings) is one concrete elevation of the constraint.
