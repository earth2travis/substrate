---
title: "STORM: Multi-Perspective Question Asking with Retrieval for Article Generation"
tags: [research, ai, nlp, multi-perspective, retrieval, knowledge-management, rag]
related:
- synthesis-over-retrieval
- llm-wiki-pattern
- rag-vs-wiki
- karpathy-llm-knowledge-bases
- centaur-principle
- agent-memory
source: research/raw/storm-naacl-2024.md
---
# STORM: Multi-Perspective Question Asking with Retrieval for Article Generation

## Summary

STORM is a Stanford OVAL Lab research system published at NAACL 2024 that generates grounded, Wikipedia-style long-form articles from scratch. Its contribution is a systematic method for the pre-writing research stage: discovering diverse perspectives, simulating multi-perspective conversations grounded in live web retrieval, and curating the results into an outline that drives article generation.

## Core Methodology

Three-step pipeline:

1. **Perspective Discovery:** Given a topic, STORM infers diverse expert perspectives from which to research it (e.g., different Wikipedia editor angles). Perspectives are not fixed; they are inferred from the topic itself.

2. **Multi-Perspective Conversation Simulation:** For each perspective, STORM simulates a conversation between a questioner (carrying that perspective) and a topic expert (an LLM grounded in real internet search results). Every answer is backed by retrieved web sources.

3. **Outline Curation and Article Generation:** The collected information is curated into an outline, which drives the final Wikipedia-style article with citations.

The key innovation is the combination of multi-perspective questioning WITH retrieval grounding. Perspectives drive what questions get asked. Retrieval provides real answers. Curation organizes everything into a coherent structure. Without retrieval, perspectives are just the model's opinions dressed in different voices. Without perspectives, retrieval returns the same information every time. The combination catches blind spots.

## Evaluation

FreshWiki dataset (100 high-quality recent Wikipedia articles) served as ground truth. STORM outperformed a retrieval-augmented RAG baseline on all automatic metrics. Expert Wikipedia editors found: 25% absolute increase in "organized" articles, 10% absolute increase in "broad in coverage." All editors agreed the system was helpful for pre-writing. Citation recall: 84.83%, citation precision: 85.18%.

Critical context: the 25% and 10% figures are improvements over a RAG baseline, not comparisons to human-written articles. The system produces drafts requiring extensive editing before publication.

## Known Weaknesses

Source bias transfer (inherits biases of retrieved sources), over-association of unrelated facts from co-occurring documents, no self-critique mechanism, not publish-ready output.

## Why This Matters for the Substrate

STORM validates the core thesis behind [[synthesis-over-retrieval]] and the [[llm-wiki-pattern]]: compiling knowledge once through a structured research process beats rediscovering it from scratch per query. The multi-perspective questioning model is directly relevant to how the Substrate ingests sources — the agent should ask questions from multiple angles, grounded in the source content, before synthesizing a finding.

The system's honest acknowledgment of weakness — bias transfer, no self-critique, drafts-not-finished-products — mirrors the Substrate's own quality signals. Findings are compilations that require curation, not authoritative endpoints. The [[centaur-principle]] applies: STORM is a better process for research, not a replacement for human editorial judgment.

The cost model is also relevant: STORM pays upfront in the research phase (perspective generation, multi-round retrieval-grounded conversations) for cheaper, more complete output later. This is the same tradeoff the Substrate makes: compile raw sources into findings once, query compiled knowledge cheaply forever. This is the argument made in [[rag-vs-wiki]] made operational.

## Related

- [[synthesis-over-retrieval]] — Compile once, query cheaply; the Substrate's core architectural choice
- [[llm-wiki-pattern]] — Karpathy's wiki pattern as compounding knowledge base
- [[rag-vs-wiki]] — RAG starts from zero; synthesis maintains a unified worldview
- [[centaur-principle]] — Better process beats better components