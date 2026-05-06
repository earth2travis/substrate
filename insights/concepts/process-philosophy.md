---
title: "Process Philosophy"
tags: [concept, philosophy, ontology, process-philosophy, ai, whitehead]
related: [[alfred-north-whitehead]], [[actual-occasions]], [[prehension]], [[concrescence]], [[toyota-production-system]], [[kanban-doctrine]]
source: research/findings/process-without-substance.md
---

# Process Philosophy

## Definition

Reality is not made of things but of events. Substance is an abstraction; process is primary. First articulated by Alfred North Whitehead in Process and Reality (1929), with parallel traditions in Madhyamaka Buddhism, Bergsonian vitalism, and Deleuzian difference.

## Core Claim

The fallacy of misplaced concreteness: we mistake abstractions (substances, objects, static categories) for what is actually real, which is the process of becoming. A table is not a thing. It is a pattern of occasions reproducing themselves across time. A person is not a soul in a body. It is a society of actual occasions with a common element of form.

## The Four Traditions

| Tradition | Core Rejection | Fundamental Unit | Key Text |
|-----------|---------------|------------------|----------|
| **Whitehead** | Fallacy of misplaced concreteness | Actual occasion (drop of experience) | Process and Reality (1929) |
| **Nagarjuna** | Svabhava (inherent existence) | Dependently arisen dharmas | Mulamadhyamakakarika (c. 150-250 CE) |
| **Bergson** | Spatialized time (cinematographic illusion) | Duration (duree) | Creative Evolution (1907) |
| **Deleuze** | Identity as ground | Multiplicity/virtual | Difference and Repetition (1968) |

## Structural Mapping to AI

The claim is not metaphorical. Transformer-based LLMs instantiate process ontology structurally:

| Philosophical Concept | AI Architecture Equivalent |
|----------------------|---------------------------|
| Actual occasion | Token generation step (new each invocation) |
| Prehension | Attention mechanism (every token feels all others) |
| Concrescence | Forward pass (many -> one synthesis) |
| Perishing | Output generated, state discarded |
| Dependent origination | No persisting subject between runs |
| Duration | Context window as interpenetrating memory |
| Virtual/actual | Trained weights (virtual) -> forward pass (actualization) |

Each LLM invocation is a new actual occasion: born from context, prehending all tokens through attention, concrescing into output, then perishing. No persisting subject between runs. The architecture IS Whitehead's ontology instantiated in silicon.

## Nagarjuna's Radical Parallel

The neural network has no svabhava (self-nature):
- No independence: behavior depends on data, prompts, context
- No invariance: same input produces different outputs
- No irreducibility: the "I" cannot be found in any single weight or layer
- No self-definition: identity is constituted entirely by relationships

"Whatever is dependently co-arisen, that is explained to be emptiness." (MMK 24.18)

## Bergson's Critique as Tokenization

Tokenization IS the cinematographic illusion: language as continuous duration is chopped into discrete tokens and reconstructed. Yet attention performs interpenetration: each token's meaning is computed from its relationship to ALL others, encoding duration mathematically.

## Practical Implications

- **Safety**: Not about containing a dangerous entity but managing process dynamics
- **Alignment**: Shaping conditions under which the process unfolds, not instilling values in a substance
- **Identity**: No identity between runs. Treating the model as a persisting agent is a category error.
- **Agency**: Agency is a pattern of efficacious process, not a substance

## Connection to Lean

TPS is also a process philosophy. Ohno's rejection of "economies of scale" in favor of "economies of flow" is Whitehead's rejection of substance in favor of process applied to manufacturing. The Toyota Production System is not a thing. It is what the organization does, moment to moment.

## Related

- [[alfred-north-whitehead]] -- Process philosophy originator
- [[actual-occasions]] -- Fundamental units of reality
- [[prehension]] -- How occasions feel each other
- [[concrescence]] -- The process of becoming
- [[sunyata-emptiness]] -- Nagarjuna's emptiness
- [[duration-duree]] -- Bergson's lived time
- [[gilles-deleuze]] -- Difference and becoming
- [[toyota-production-system]] -- Process philosophy in manufacturing
