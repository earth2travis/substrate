---
title: "Dark Factory / Lights-Out Manufacturing"
tags: [finding, automation, manufacturing, dark-factory, fanuc, industry-4.0]
related: [[dark-factory]], [[harness-engineering]], [[codex]], [[lean-doctrine]]
source: research/raw/dark-factory-lights-out-manufacturing.md
ingested: 2026-05-07
---

# Dark Factory / Lights-Out Manufacturing

"Lights-out" or "dark factory" manufacturing refers to fully automated production facilities that operate without human presence. The concept, coined in the 1980s, has migrated from physical production to software development.

## Key Points

**Historical lineage.** From Karel Capek's R.U.R. (1920) to Ford's Rouge Plant (raw ore in, cars out) to FANUC's self-building robot factories (robots running 30 days unsupervised) to Siemens Amberg (99.99885% quality rate, same workforce since 1989 with 61 million products/year).

**FANUC: the canonical dark factory.** ~50 robots building ~50 robots per day. Quality checks, material loading, and subcomponent assembly performed autonomously. The domain knowledge is identical between builder and built; standardized processes require no creative problem-solving.

**GM Hamtramck: the cautionary tale.** 1980s vision of lights-out automation failed because technology was immature, over-reliance on automation lacked human oversight, and quality issues required manual rework. The vision was ahead of the reality.

**Software equivalent: OpenAI Frontier.** Ryan Lopopolo's team built a software dark factory: 1B tokens/day, 0 lines of human-written code, 6+ hour autonomous runs, agent-to-agent review as quality sensors. In software, there are no physical constraints; full automation is easier than in manufacturing.

**Industry 4.0 enabling technologies.** IoT sensor networks, machine vision, digital twins, AI/ML predictive maintenance, cobots, and 5G connectivity have revitalized the concept. Modern examples include Tesla's hybrid approach and Haier's mass-customization factory.

**Key principles.** Self-monitoring systems with automated error detection; predictive maintenance via sensors; standardized interfaces and modular design; redundancy and graceful degradation; continuous improvement via data feedback; human exception handling for novel situations.

## Related

- [[dark-factory]] -- Concept page for autonomous production
- [[harness-engineering]] -- Methodology enabling software dark factories
- [[codex]] -- Primary agent tool in frontier automation
- [[lean-doctrine]] -- Jidoka and Kaizen as dark-factory principles
