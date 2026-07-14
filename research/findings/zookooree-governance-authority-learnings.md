---
title: "Zookooree Governance and Authority: Delegating the Die Without Losing the Gate"
tags: [finding, agent-factory, governance, authority, germline, codeowners, editorial, delegation, progressive-autonomy]
related:
- agent-factory-production-system
- progressive-autonomy
- workflow-as-contract
- proof-of-work
- lean-doctrine
- harness-engineering
- principal-agent-theory
source: research/raw/zookooree-governance-and-authority-learnings.md
ingested: 2026-07-14
---
# Zookooree Governance and Authority: Delegating the Die Without Losing the Gate

## Summary

Two governance delegations from the Zookooree Agent Factory's first production weekend (2026-07-11 to 2026-07-13), both concerning the problem of manufacturing safety (controlling changes to the die that shapes every future unit) while removing the operator as a standing bottleneck. The factory produces agents that staff the factory, creating a recursion that is the compounding advantage and the most dangerous failure mode. To control it, everything is split into two classes: germline (the die: templates, station gates, validators, work-order schemas, standard work, `.github/` controls) and soma (deployed unit instances and their run-state, with lighter gates, recoverable by recall and re-issue). A defect in germline propagates into every subsequent unit, so germline changes carry the strictest control.

## Learning 1: Merge Authority for the Die Can Leave the Operator's Person Without Losing the Gate

Until this weekend, the human operator was the only party allowed to merge germline changes. That was the right rule when the authority had no other home, but it made the founder a standing bottleneck. A factory whose die cannot be re-cut without its founder present contradicts the promise of running unattended. The bottleneck is not a safety property; it is a single point of stall.

The learning: the real safety gate is not the founder's hands. It is three checkable criteria, all required: CI green, an independent non-author reviewer has approved, and the change is within existing policy (sets no new precedent, conflicts with no standing rule). When all three hold, any authorized merger can merge. Nothing about the founder specifically being on the keyboard adds safety.

### The Mechanism

Authority was delegated through the normal review gate, not around it. A competent, persistent, independent agent (the CEO, who did not author the pull requests) was added as a germline co-owner in CODEOWNERS. GitHub does not count an author's own review toward the code-owner requirement, so a germline PR authored under the operator's credentials is satisfiable by the co-owner's approval and merges via an ordinary squash. This is deliberate: routing authority through anything other than a code owner would have forced an admin bypass, and the absolute rule is that agent sessions never run an admin-override merge on any pull request. Making the reviewer a code owner keeps that rule intact with no exception.

Genuine exceptions (a new precedent, a policy conflict) are not merge decisions; they are policy decisions and still escalate to the operator. The operator's standing role shrinks to setting policy and adjudicating exceptions.

### Generalization

This is a concrete instance of [[progressive-autonomy]] as constraint elevation (see [[zookooree-factory-doctrine-learnings]]). The operator's attention is the plant's binding constraint. Delegating germline merge authority is a Theory-of-Constraints elevation step: it raises the bottleneck's capacity by removing a class of decisions from the operator's queue without losing the safety gate. The gate was never "the operator's hands." It was three checkable criteria. The criteria compose: CI green is an automated gate, independent review is a human judgment gate, policy compliance is a domain-knowledge gate. Each can be delegated to the party best suited to hold it, so long as all three must hold.

This connects to [[workflow-as-contract]]: the authority structure is versioned in the repo via CODEOWNERS and policy files, not informally through who-knows-whom. It also connects to [[principal-agent-theory]]: the principal delegates merge authority to an agent (the CEO) through a structured contract (CODEOWNERS + review rules), not through trust alone.

## Learning 2: Editorial Authority Over Public Content is Broader Than Veto

A parallel delegation covered public writing. The first framing proposed a review-and-veto authority. The correction, argued by the editor-in-chief and adopted: review-and-veto is too narrow and too reactive, because it treats veto as the whole authority when veto is only the residual backstop. The real editorial authority has three tiers, in order:

1. **Gates first.** Taste rulings that compile to checker rules, enforced by exit code, not opinion. This is [[chamath-software-factory-thesis]]'s "coherence under change" test applied to editorial practice: taste encoded into infrastructure survives staff turnover.
2. **Curation second.** Deciding what publishes at all. "Publish less, better" is the primary lever, a first-class editorial act. Curation is upstream of veto: the most powerful editorial decision is what never reaches the review queue.
3. **Veto third.** The backstop for judgment taste that has not compiled to a gate yet.

### Supporting Learnings

The veto carries a clock: a veto that goes silent past the reviewer's loop cadence lets the publish proceed, so the editorial loop cannot become a bottleneck by silence. This is the same failure mode the whole constraint discipline warns about: a gate that blocks by inaction is functionally identical to a gate that blocks by rejection, but harder to detect because it looks like nothing happened.

The division of labor respects comparative advantage: the stronger drafter does the heavy drafting while the stronger editor holds curation and gates. Moving drafting onto the editor's weaker drafting loop would spend editorial leverage in the wrong place. This is [[principal-agent-theory]] at the micro-scale: delegate to the party with comparative advantage, not the party with highest absolute capability across all tasks.

## Related

- [[agent-factory-production-system]] -- The factory framework these delegations operationalize
- [[zookooree-factory-doctrine-learnings]] -- The constraint reframing these delegations are an implementation of
- [[zookooree-first-production-run-findings]] -- The empirical run that exercised these governance structures
- [[progressive-autonomy]] -- Delegated authority as constraint elevation
- [[workflow-as-contract]] -- Authority versioned in-repo via policy files
- [[principal-agent-theory]] -- Structured delegation through contracts
- [[proof-of-work]] -- The verification stack the gates implement
- [[lean-doctrine]] -- TPS principles behind the germline/soma split
- [[chamath-software-factory-thesis]] -- "Coherence under change" and "independence from individuals"