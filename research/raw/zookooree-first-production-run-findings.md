# Zookooree Agent Factory: First Production Run Findings (3P)

Source: The Zookooree Agent Factory's first production shift, 2026-07-11 to 2026-07-13. Derived from `docs/pilot-plan.md` and the obeya board `reports/2026-07-13-trial-production.md` in zookooree/the-agent-factory, plus the weekend retro in `quality/retros/`. Raw learnings for synthesis.

## What the run was

A 3P run (Toyota's Production Preparation Process): the line was stood up small and real, and product was run through it before scaling. The floor is a git repository. The assembly line has seven stations (Work Order, Design, Assemble, Verify, Certify, Deploy, Operate), and nothing leaves without a Certificate of Conformance. The andon is a watchdog: a timer that rings when an expected artifact goes missing, because with software agents silence is the sound failure makes. A 3P run is judged by what it surfaces, not by a clean scoreboard.

## What it produced

Five certified units, chosen to exercise every station and all three families (skill, tool, agent): op-headless 1.1 (a re-certification, proving the machinery of a perishable certificate), validate-work-order 1.0 (a tool, the factory dogfooding its own intake gate), silence-watchdog 1.0 (a tool closing the line's actual historical failure), todo-issue-sync 1.0 (a skill pulled by real demand), and koda 1.0 (an agent, the decommissioned CTO re-manufactured). Plus the infrastructure that makes the plant a plant: two standing loops running as GitHub Actions independent of any session (a daily silence watchdog and a weekly re-certification sweep), and a public storefront with the homepage claim made literally clickable and a certificates shelf carrying real content hashes and published defects.

## Finding 1: Independent review was the dominant defect-catcher, not the automated gates

The most important finding on the obeya board: the process step that caught the most real defects this weekend was independent code review, not the automated gate stack. One unit passed all its automated gates and then lost real yield to three defects that independent review caught afterward. This is a direct signal about where to invest: the verification building (the reference-free judgment and human-audit layers), not more assembly automation. It also validates the thesis that verification is the expensive building and assembly is nearly free.

## Finding 2: Yield reported honestly, defects treated as the brand

The yield was recorded without flattering it. Of five units, two passed their gates clean on the first run. op-headless opened red by design (its own prior defect record predicted the failure). todo-issue-sync passed its gates and then lost yield to the three review escapes, all fixed the same shift and counted honestly against the number. koda ran roughly 75 percent first-pass. None of these misses were painted over. The operating principle: defects are the brand, published rather than hidden; the obeya board deliberately reads as not-all-green because it is not, and that honesty is the deliverable.

## Finding 3: The line caught its own corrosion

Several failures were caught by the line itself, which is the design working, not failing. A false andon fired when GitHub changed its search API and a watchdog probe began throwing a 422; the watchdog failed closed and rang exactly as designed, and the probe was fixed. The docs deploy was found to be serving a starter template rather than the real content, because the assumption it was live had never been verified; curling the real URL surfaced the truth and a verify step now guards it. A certificate false alarm claimed a just-certified agent was invalidated; the check proved it conforming and the install requirement was hardened against the stale checkout that caused it. Each of these is a unit of learning baked back into the standard work.

## Finding 4: Named open gaps between pilot and production

The run surfaced, without softening, the honest work remaining before a production plant with a customer who is not us. Cost per certified unit is unmetered, so the price-minus promise has no gauge yet (the only figure on record is a single-digit-dollar estimate under a 25 dollar target). The orchestration role that runs the line is ephemeral, not persistent. A maintenance relationship ("done, and maintained") needs to become an operational model, not a slogan. The vocabulary still carries imports from other domains (the biology of germline and soma) that want migrating to manufacturing-native terms. And verification leverage (reference-free judges that turn human review from "check everything" into "audit the auditor") is the capacity lever that is not yet built. Every gap was filed as a tracked issue so nothing is lost when the session ends.
