---
title: "Zookooree Factory Doctrine: Corrosion, Done-and-Maintained, and Attention as Constraint"
tags: [finding, agent-factory, corrosion, lean, toyota, production-system, maintenance, theory-of-constraints, verification]
related:
- agent-factory-production-system
- dark-factory
- lean-doctrine
- harness-engineering
- proof-of-work
- reference-free-evaluation
- chamath-software-factory-thesis
source: research/raw/zookooree-factory-doctrine-learnings.md
ingested: 2026-07-14
---
# Zookooree Factory Doctrine: Corrosion, Done-and-Maintained, and Attention as Constraint

## Summary

Three doctrine reframings emerged from the Zookooree Agent Factory's first production shift (2026-07-11 to 2026-07-13), a 3P run (Toyota's Production Preparation Process). The factory is built on the Toyota Production System and produces verified trust as its product: agents, tools, and skills that carry a Certificate of Conformance. The weekend surfaced a single organizing enemy, a sharper model of "done," and a constraint reframing that together restructure the factory's operating theory.

## Learning 1: Corrosion is the Organizing Enemy

In a software agent factory, nothing physically breaks. Correctness and trust decay silently: models drift, dependencies change, documentation goes stale, knowledge rots. Nothing fails loudly. Things quietly stop being true. This is the factory's rust, and because it is not caused by a defect event, no defect event catches it.

The evidence is the factory's own history. Everything built in a March 2026 burst was rotten by July without a single defect occurring. A credential expired quietly. An export pipeline began shipping empty placeholder files. Roadmap dates elapsed unrevised. Nothing failed. Everything decayed.

The reframing unifies the factory's original six theses (verification is the expensive building; there are no finished goods; the andon must ring for silence; doctrine must compile; germline and soma change control; the operator's attention is the constraint) under one north-star idea. Each thesis maps to a specific form of corrosion: silent defects, staleness, absence, culture decay, propagated defects, and bottleneck rot. A single named enemy gives every design decision one test: does this reduce corrosion, or does it just look tidy today.

This connects directly to the existing [[agent-factory-production-system]] Jidoka pillar (autonomy with oversight, no silent failures) but sharpens it. Jidoka catches defect events. Corrosion is what happens between defect events. The andon cord is necessary but not sufficient: you also need scheduled re-certification, drift detection, and expiry dates on every claim. See [[proof-of-work]] for the verification stack and [[reference-free-evaluation]] for the real-time confidence signal that makes corrosion visible.

## Learning 2: "Done, and Maintained," Not "Nothing is Ever Finished"

A certificate is perishable. Deployment is not exit. It is transfer from a high-frequency inspection zone to a low-frequency one. The right industrial analogy for the back half of the line is aviation's continuing airworthiness: telemetry return, scheduled re-certification, and a recall mechanism.

The reframing sharpens the earlier "nothing is ever finished" slogan into something operational. Every stage gets a real definition of done, and done is then kept alive by scheduled maintenance: re-certification on expiry or on trigger conditions like a model swap or dependency change. This is the differentiator against "shipped and forgotten" on one side and against the demoralizing "never finished" on the other. Maintenance is a first-class model, an after-sales relationship with each unit, not a virtue or an afterthought.

This operationalizes the "there are no finished goods" thesis from [[agent-factory-production-system]] and connects to [[chamath-software-factory-thesis]]'s test of "coherence under continuous change." The certificate expiry date is what makes the factory's promise falsifiable over time.

## Learning 3: The Operator's Attention is the Plant's Constraint, Not Takt

The factory is a one-human plant with no external customer yet, so takt time (a demand-driven rhythm) is the wrong frame. The binding constraint is the human operator's attention. Every certified unit spends that attention twice: once at intake (writing the work order and stating intent) and once at certification (accepting the claim and its evidence). Compute is not the constraint. Agent throughput is not the constraint. Human trust-bandwidth is.

The consequence is a Theory-of-Constraints posture (the Five Focusing Steps): identify, exploit, subordinate to, and then elevate the human constraint. The only way to raise plant capacity is verification leverage, not more agents. Reference-free judges and delegated authority turn human review from "check everything" into "audit the auditor." Overproduction is redefined as building agents faster than anyone can trust them. The honest metric is operator-touches per certified unit, trending toward zero.

Delegating germline merge authority out of the operator's person (see the [[zookooree-governance-authority-learnings]]) is one concrete elevation of the constraint. This reframes [[progressive-autonomy]] not as a trust dial but as a constraint-elevation strategy: each delegated authority is a focused-step intervention that raises the bottleneck's capacity.

## Related

- [[agent-factory-production-system]] -- The production framework these learnings refine
- [[dark-factory]] -- The autonomous endpoint; corrosion is what makes it not dark
- [[lean-doctrine]] -- JIT and Jidoka as corrosion tactics
- [[harness-engineering]] -- Verification infrastructure as corrosion defense
- [[proof-of-work]] -- The layered verification stack
- [[reference-free-evaluation]] -- Real-time confidence signals that surface corrosion
- [[chamath-software-factory-thesis]] -- External validation of the factory thesis
- [[zookooree-first-production-run-findings]] -- The empirical run that produced these learnings
- [[zookooree-governance-authority-learnings]] -- Authority delegation as constraint elevation