---
title: "Zookooree First Production Run: 3P Findings from the First Weekend"
tags: [finding, agent-factory, production-run, lean, toyota, 3p, verification, yield, andon, defect]
related:
- agent-factory-production-system
- dark-factory
- lean-doctrine
- harness-engineering
- proof-of-work
- reference-free-evaluation
- chamath-software-factory-thesis
source: research/raw/zookooree-first-production-run-findings.md
ingested: 2026-07-14
---
# Zookooree First Production Run: 3P Findings from the First Weekend

## Summary

The Zookooree Agent Factory ran its first production shift (2026-07-11 to 2026-07-13) as a 3P exercise (Toyota's Production Preparation Process): stand up a small real line, run product through it, and harden the standard work against what breaks. The floor is a git repository. The assembly line has seven stations (Work Order, Design, Assemble, Verify, Certify, Deploy, Operate). Nothing leaves without a Certificate of Conformance. The andon is a watchdog timer that rings when an expected artifact goes missing, because with software agents silence is the sound failure makes. A 3P run is judged by what it surfaces, not by a clean scoreboard.

## What the Run Produced

Five certified units, chosen to exercise every station and all three families (skill, tool, agent): op-headless 1.1 (a re-certification, proving the machinery of a perishable certificate), validate-work-order 1.0 (a tool, the factory dogfooding its own intake gate), silence-watchdog 1.0 (a tool closing the line's actual historical failure mode), todo-issue-sync 1.0 (a skill pulled by real demand), and koda 1.0 (an agent, the decommissioned CTO re-manufactured). Plus the infrastructure: two standing GitHub Actions loops (a daily silence watchdog and a weekly re-certification sweep) and a public storefront with a clickable homepage claim and a certificates shelf carrying real content hashes and published defects.

## Finding 1: Independent Review Was the Dominant Defect-Catcher

The most important finding on the obeya board: the process step that caught the most real defects this weekend was independent code review, not the automated gate stack. One unit passed all its automated gates and then lost real yield to three defects that independent review caught afterward. This is a direct signal about where to invest: the verification building (reference-free judgment and human-audit layers), not more assembly automation. It validates the [[agent-factory-production-system]] thesis that verification is the expensive building and assembly is nearly free.

This connects to [[proof-of-work]] and [[reference-free-evaluation]] but adds a crucial empirical caveat: the automated verification stack catches mechanical correctness, but independent human review catches what the gates cannot see yet. The implication is that verification leverage (the path to reducing operator attention per unit, see [[zookooree-factory-doctrine-learnings]]) must raise the quality of automated gates to where they approach independent review's catch rate. Until then, independent review remains load-bearing.

## Finding 2: Yield Reported Honestly, Defects Treated as the Brand

The yield was recorded without flattering it. Of five units, two passed their gates clean on the first run. op-headless opened red by design (its own prior defect record predicted the failure). todo-issue-sync passed its gates and then lost yield to three review escapes, all fixed the same shift and counted honestly against the number. koda ran roughly 75 percent first-pass. None of these misses were painted over. The operating principle: defects are the brand, published rather than hidden. The obeya board deliberately reads as not-all-green because it is not, and that honesty is the deliverable.

This is a culture-level reinforcement of [[lean-doctrine]]'s hansei (self-reflection without deflection) and the [[agent-factory-production-system]] Jidoka pillar. It also embodies [[chamath-software-factory-thesis]]'s test of "end-to-end accountability": if defects are published, accountability is structural, not performative.

## Finding 3: The Line Caught Its Own Corrosion

Several failures were caught by the line itself, which is the design working, not failing. A false andon fired when GitHub changed its search API and a watchdog probe began throwing a 422. The watchdog failed closed and rang exactly as designed, and the probe was fixed. The docs deploy was found serving a starter template rather than real content, because the assumption it was live had never been verified. A certificate false alarm claimed a just-certified agent was invalidated; the check proved it conforming and the install requirement was hardened against the stale checkout that caused it. Each failure is a unit of learning baked back into the standard work.

This is the empirical evidence for the corrosion thesis in [[zookooree-factory-doctrine-learnings]]. The andon and the re-certification sweep are the line's immune system against silent decay. When they fire, that is the system working. A false alarm is not a bug: it is the andon doing its job against an environment that changed underneath the line.

## Finding 4: Named Open Gaps Between Pilot and Production

The run surfaced, without softening, the honest work remaining before a production plant with a customer who is not us. Cost per certified unit is unmetered, so the price-minus promise has no gauge yet (the only figure on record is a single-digit-dollar estimate under a 25 dollar target). The orchestration role that runs the line is ephemeral, not persistent. A maintenance relationship ("done, and maintained") needs to become an operational model, not a slogan. The vocabulary still carries imports from other domains (the biology of germline and soma) that want migrating to manufacturing-native terms. And verification leverage (reference-free judges that turn human review from "check everything" into "audit the auditor") is the capacity lever that is not yet built. Every gap was filed as a tracked issue so nothing is lost when the session ends.

## Related

- [[agent-factory-production-system]] -- The framework the run exercised
- [[zookooree-factory-doctrine-learnings]] -- Doctrine reframings derived from this run
- [[zookooree-governance-authority-learnings]] -- Authority delegation findings from the same weekend
- [[dark-factory]] -- The autonomous endpoint this run is a step toward
- [[lean-doctrine]] -- The TPS principles the run validated and refined
- [[harness-engineering]] -- The verification infrastructure the run tested
- [[proof-of-work]] -- The layered verification stack the gates implement
- [[reference-free-evaluation]] -- The verification-leverage lever not yet built
- [[chamath-software-factory-thesis]] -- External validation context