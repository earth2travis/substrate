---
title: "Context Stack Observations: Spec Development Log"
tags: [context-engineering, agent-identity, specification, development-log, knowledge-architecture]
related:
  - [[the-context-stack-spec]]
  - [[interchangeable-context]]
  - [[context-stack-as-conscience]]
  - [[memory-systems]]
  - [[agent-identity]]
source: research/raw/context-stack-observations.md
---

# Context Stack Observations: Spec Development Log

## Summary

A living log of insights, questions, and test results as the Context Stack specification was developed. The document captures the founding conversation of 2026-03-26, key moves during the design process, and open questions. The original stack proposal included SOUL.md, VISION.md, VALUES.md, EXPERIENCE.md, DESIGN.md, AGENTS.md, OBJECTIVES.md, MISSIONS.md, DECISIONS.md, INTENT.md, ROLES.md, plus skills/, research/, and knowledge/ directories. Key additions during design: RELATIONSHIPS.md (moved to Intelligence layer), CONTRACT.md (enforcement layer), TASTE.md (instinct over principle), and TODO.md (working surface). The final count is 14 files plus 4 directories across 4 layers.

## Key Claims

1. **RELATIONSHIPS moved from Identity to Intelligence.** Relationships aren't identity; they're intelligence gathered about the world outside yourself. Identity is who you are in isolation. Intelligence is what you know about everything outside yourself. Changed from a single file to a directory (relationships/) so each relationship gets its own file.

2. **CONTRACT.md bridges internal context and external commitments.** SOUL.md is who you are to yourself. CONTRACT.md is who you are to others, enforceable. Values are weighted. Contracts are binary.

3. **TASTE.md captures instinct over principle.** Adjacent to VALUES.md but distinct: values are rankable principles, taste is recognizable but not easily articulable. The hardest file to write because it requires articulating what you normally just feel.

4. **TODO.md is directional, not operational.** The working surface is one of Factory AI's four compaction anchors that must survive every context compression. It answers "where am I going next," not "how do I do it."

5. **Four states of knowing in Intelligence:** skills/ (what you can do), research/ (what you're learning), knowledge/ (what you know), relationships/ (who you know).

## Implications

The spec emerged through iterative conversation rather than top-down design. Each addition was driven by a gap in the existing structure. The development log proves that a good specification is discovered, not declared. It also surfaces open questions: how to test the spec, how to handle versioning, how the stack works for entities that are both individual and organization.

## Related

- [[the-context-stack-spec]] — The finalized universal specification
- [[interchangeable-context]] — Structural parallel to interchangeable parts
- [[context-stack-as-conscience]] — Moral architecture built on the stack
- [[memory-systems]] — Memory architectures complementing the stack
- [[agent-identity]] — Identity as the foundation of agent behavior
