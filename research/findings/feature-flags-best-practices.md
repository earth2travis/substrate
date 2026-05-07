---
title: "Feature Flags: Best Practices and Opportunities"
tags: [research, feature-flags, experimentation, posthog]
related: [agent-native-operations, kanban-doctrine, centaur-principle, institutional-ai-redesign]
source: "Research compiled February 12, 2026, Issue #158"
---


# Feature Flags: Best Practices and Opportunities

## Summary

Feature flags (toggles/switches) enable decoupling deploy from release, phased rollouts, kill switches, user targeting, A/B testing, remote configuration, and beta programs. Research covers 12 commandments, 7 deadly mistakes, and strategic opportunities for agent operations.

## Key Concepts

**Flag Types by Lifecycle:**
- Release flags: days to weeks (new feature rollouts, dark launches)
- Experiment flags: weeks to months (A/B tests, multivariate)
- Ops flags: permanent (kill switches, circuit breakers, log levels)
- Permission flags: permanent (entitlements, beta access, tiers)

**The 12 Commandments:**
1. Clear naming (what, when added, who owns, when removed)
2. Centralized management (single source of truth)
3. Keep flags short-lived (30-day default for release flags; Flag Friday cleanup)
4. Document thoroughly (purpose, owner, impact, expiration, removal plan)
5. Access controls (four eyes for production)
6. Monitor and log usage (stale flag alerts after 30 days)
7. Integrate with CI/CD (test all combinations, automate cleanup tickets)
8. Test before deployment (functional, regression, combinatorial)
9. Use flags for rollbacks (toggle flip faster than deployment rollback)
10. A/B testing and experimentation
11. Canary releases (internal → 1% → 10% → 50% → GA)
12. Target user segments (plan, role, geography, device)

**Seven Deadly Mistakes:**
The "and" problem (one flag = one function), placeholder names, abandoned ownership, dumping on ops, technical debt accumulation (chest freezer problem), not distinguishing permanent flags, flag reuse (Knight Capital lost $440M in 45 minutes).

**Agent-Specific Opportunities:**
- Model selection flags
- Tool access toggles per environment
- Progressive autonomy (graduated trust with instant rollback)
- Multi-agent coordination flags
- Kill switches for safety
- Infrastructure migration control

## Applications

PostHog provides boolean/multivariate flags, percentage rollouts, cohort targeting, local evaluation, bootstrapping, and experiments with statistical significance. Critical for AI systems needing instant disable capability without code deployment. [[agent-native-operations]] [[kanban-doctrine]] [[progressive-autonomy]]
