---
title: "AI Skill Threat and FoMO-AI: The Human Cost of GenAI Adoption (2023-2026 Synthesis)"
tags: [finding, ai-skill-threat, fomo-ai, burnout, cognitive-load, psychological-safety, upskilling, equity, labor, adoption]
related:
- centaur-principle
- brain-fry
- agent-native-operations
- institutional-ai-redesign
- progressive-autonomy
- feedback-loop-discipline
source: research/raw/ai-skill-threat-fomo-genai-anxiety-report-2026.md
ingested: 2026-07-24
---
# AI Skill Threat and FoMO-AI: The Human Cost of GenAI Adoption (2023-2026 Synthesis)

## Summary

A compiled synthesis of twelve-plus studies from 2023-2026 (Pluralsight Developer Success Lab, arXiv preprints, ScienceDirect papers, a Nature poll, workplace surveys) converges on two named constructs: **AI Skill Threat** (fear that current competencies become obsolete; 45% of surveyed developers report it) and **FoMO-AI** (fear of missing out on AI benefits and of being rendered obsolete by others or society, now with a validated scale). The throughline: GenAI adoption pressure is producing measurable psychological, cognitive, and social costs: 74% of developers feel compelled to upskill, oversight labor (reviewing and correcting AI output) amplifies cognitive load and burnout, job insecurity drives knowledge hiding via reduced psychological safety, and AI awareness erodes work-family boundaries by impairing detachment. The anxiety is not confined to developers: CS students at Toronto report strong job-replacement anxiety concentrated on entry-level roles, and almost half of 1,900+ polled scientists feel negative toward AI yet adopt it out of FOMO.

## Key Findings by Strand

1. **AI Skill Threat (Pluralsight, 2023-2025).** 45% of 3,000+ developers experience it; 74% plan to upskill; IT skills now last ~2.5 years. Team culture moderates it: 44% whose teammates do not use AI report higher threat. Upskilling intent is significantly lower among female and LGBTQ+ developers, an equity gap, not a motivation gap.
2. **FoMO-AI formalization (2025-2026).** Méndez-Suárez et al. (OECD data, fsQCA) find multiple causal pathways: perceived skill devaluation, lost decision autonomy, "robo-boss" oversight concerns. Fengyi et al. validate a FoMO-AI scale predicting obsessive skill acquisition and overzealous AI use. Workplace surveys show the reframing from job-replacement fear to competitive-disadvantage fear, still maladaptive.
3. **Oversight labor and burnout.** Guizani et al. (arXiv:2605.22349): GenAI shifts the developer from creator to reviewer, an invisible "Do More With Less" fatigue. Brandebusemeyer et al. (SAP field study, physiological measures): AI tasks showed higher perceived cognitive load at comparable productivity; mixing interaction types within a task cancels benefits; one cited study found 19% productivity decline in certain contexts.
4. **Insecurity downstream effects.** Kim (2024): AI job insecurity → knowledge hiding, mediated by psychological safety. Yi et al. (2026): AI awareness → work-family conflict via failed detachment, buffered by trait resilience. Anxiety about both replacement and learning diminishes work passion.
5. **Next generation and science.** Farooqi et al. (25 CS students, Toronto): entry-level software/web/game roles seen as vulnerable; compelled upskilling (4.82/7) or reskilling; international students doubly pressured. Nature poll (1,900+ researchers): negative sentiment coexisting with adoption pressure over misinformation concerns.
6. **Structural implications.** The Centaur Principle fails when process improvements are absent and anxiety drives reactive adoption. Risks: oversaturation of "AI-proof" subfields, dissuasion from CS, deepening access inequality.

## Why It Matters to Substrate

This is the demand-side counterweight to the lab-side acceleration findings ([[rsi-anthropic-openai-deep-dive]], [[self-driving-company-replit]]). The same capability curve that produces 8x engineer throughput at Anthropic produces skill-threat anxiety, knowledge hiding, and burnout in the general workforce. The review-bottleneck pattern (Amdahl at the human) appears here as "oversight labor": what the Replit finding frames as flat review latency via agentic co-reviewers, the burnout literature frames as unrecognized hidden workload shifted onto humans. Organizational mitigations named in the literature, psychological safety, deliberate learning culture, task-matched interaction types, map directly onto [[institutional-ai-redesign]] and [[agent-native-operations]] design questions.

## Connections

- [[centaur-principle]] — undermined when anxiety drives reactive adoption without process improvement.
- [[brain-fry]] — cognitive-load amplification and oversight fatigue as the measured mechanism.
- [[agent-native-operations]] — review-latency solutions on the ops side appear as burnout sources on the human side.
- [[institutional-ai-redesign]] — psychological safety and learning culture as named mitigations.
- [[progressive-autonomy]] — autonomy loss is a causal driver of FoMO-AI, not just a safety property.
- [[feedback-loop-discipline]] — insecurity → hiding → isolation → more insecurity is a vicious loop needing an explicit break.
