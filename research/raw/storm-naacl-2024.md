---
source_url: https://arxiv.org/abs/2402.14207
ingested: 2026-06-26
sha256: TBD
---

# STORM: Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking

**Paper:** "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models"
**Authors:** Yijia Shao, Yucheng Jiang, Theodore A. Kanell, Peter Xu, Omar Khattab, Monica S. Lam
**Affiliation:** Stanford University, OVAL Lab (Open Virtual Assistant Lab)
**Venue:** NAACL 2024 Main Conference
**arXiv:** 2402.14207v2 (submitted February 22, 2024; revised April 8, 2024)
**Categories:** cs.CL, cs.AI
**Pages:** 27
**License:** arXiv non-exclusive distribution license
**Code:** https://github.com/stanford-oval/storm (MIT license, 28K+ stars)
**Live Demo:** https://storm.genie.stanford.edu (free, no signup)
**Datasets:** FreshWiki (100 high-quality Wikipedia articles), WildSeek (user information-seeking records with goals)

## What STORM Is

STORM is a research system that generates grounded, Wikipedia-style long-form articles from scratch. It was published at NAACL 2024, the field's top venue. It addresses a problem that most LLM-based writing systems sidestep: how do you research a topic thoroughly enough before writing to produce something with real depth and breadth?

The question is specifically about the **pre-writing stage**, not just generation. Before an article can be written well, the system must answer: what do I know, what do I not know, and what should the structure be? STORM's contribution is a systematic method for the pre-writing research.

## Core Methodology

STORM models the pre-writing stage through a three-step pipeline:

**Step 1: Perspective Discovery.** Given a topic, STORM discovers diverse perspectives from which to research it. Instead of a single framing, it generates multiple expert views. The paper's examples work with Wikipedia editor perspectives: different angles that a real Wikipedia contributor might bring to a topic. These perspectives are not fixed; they are inferred from the topic itself, which is critical because the right perspectives vary by domain.

**Step 2: Multi-Perspective Conversation Simulation.** For each perspective, STORM simulates a conversation between a questioner (a "writer" carrying that perspective) and a topic expert (an LLM grounded in real internet search results, not parametric knowledge alone). The questioner asks questions, the expert answers, and the conversation is grounded in retrieved web sources throughout. This is where the Retrieval in the acronym comes in. Every answer is backed by search results from trusted internet sources. The system queries live search engines, retrieves relevant content, and uses it to ground the expert's responses.

**Step 3: Outline Curation and Article Generation.** The collected information from all conversations is curated into an outline. The outline then drives the article generation. The final output is a Wikipedia-style article with citations to the sources used during the research phase.

The key innovation is the combination of multi-perspective question asking WITH retrieval and grounding. The perspectives drive what questions get asked. The retrieval provides real answers. The curation organizes everything into a coherent structure. Without retrieval, the perspectives are just the model's opinions dressed in different voices. Without perspectives, retrieval returns the same information every time. The combination is what catches blind spots.

## Evaluation

### FreshWiki Dataset

The authors curated FreshWiki, a dataset of 100 high-quality recent Wikipedia articles focusing on the most-edited pages from February 2022 to September 2023. This serves as the ground truth for evaluation. The dataset is available on HuggingFace (EchoShao8899/FreshWiki) and the construction pipeline source code is archived to allow future replication without data contamination.

### Automatic Evaluation

STORM outperforms a strong retrieval-augmented generation (RAG) baseline on all automatic metrics, including LM-based evaluation and comparison metrics against human-written Wikipedia articles. The baseline is an outline-driven retrieval-augmented system, not a naive single-pass generator. This is a meaningful comparison.

### Human Evaluation: Expert Wikipedia Editors

Experienced Wikipedia editors evaluated the output. Key results:

- **Organization:** 25% absolute increase in articles deemed "organized" compared to the baseline. This means 25 percentage points more articles were rated as having clear structure.
- **Coverage breadth:** 10% absolute increase in articles deemed "broad in coverage."
- All participating editors agreed the system was helpful for the pre-writing stage.

**Critical context on the metrics:** The 25% and 10% figures are improvements over a retrieval-augmented baseline, NOT comparisons to human-written articles or to PhD-level researchers. The system does not claim to match or exceed human quality. It claims to improve the pre-writing research process for article generation.

### Citation Quality

From the GitHub repository and associated SkillPack evaluation:
- Citation recall: 84.83%
- Citation precision: 85.18%

These metrics are for the full STORM system with active retrieval. They measure whether cited sources actually support the claims they are attached to.

## Known Weaknesses (Identified by the Authors)

The paper is notably honest about limitations:

1. **Source bias transfer.** STORM inherits the biases of its sources. If the retrieved web content is skewed toward one perspective, the article will reflect that bias. The system has no mechanism to detect or correct for systematic bias in search results.

2. **Over-association of unrelated facts.** The system sometimes draws connections between facts that appear in the same retrieved document but have no actual relationship. The curation step does not fully distinguish topical co-occurrence from genuine semantic connection.

3. **No self-critique mechanism.** The system does not review its own output for errors, contradictions, or gaps. This was flagged by the authors as a target for future work.

4. **Not publish-ready.** Experienced editors found the output helpful for pre-writing but explicitly noted that the articles require extensive editing before they could be published. The system produces drafts, not finished articles.

## System Architecture and Implementation

The system is implemented as a Python pipeline:

- **Language models:** Supports multiple LLM backends. Originally tested with GPT-3.5 and GPT-4. Added `litellm` integration in January 2025 for broader model support.
- **Retrieval:** Supports multiple search backends including `YouRM` (You.com search), `BingSearch`, and `VectorRM` (user-provided document collections). The retrieval interface is modular.
- **Pipeline stages:** The config exposes `do_research`, `do_generate_outline`, `do_generate_article`, and `do_polish_article` as independent toggles, allowing partial runs for debugging or custom workflows.
- **Modular design:** The pipeline interface is defined to support customization. `storm_wiki` is the reference implementation demonstrating how to instantiate it.

### Python Usage (from repository README)

```python
from knowledge_storm import STORMWaveLMConfigs, STORMWikiRunnerArguments, STORMWikiRunner

lm_config = STORMWaveLMConfigs()
# ... Configure language models ...

runner_args = STORMWikiRunnerArguments(
    topic=topic,
    do_research=True,
    do_generate_outline=True,
    do_generate_article=True,
    do_polish_article=True,
)
runner = STORMWikiRunner(lm_config=lm_config, engine_args=runner_args)
runner.run()
```

## Roadmap (from GitHub)

The team's active development directions:
1. Human-in-the-Loop functionalities for user participation in knowledge curation
2. Information abstraction for presentation formats beyond Wikipedia-style reports

## Key Insight

The entire point of STORM is that multi-perspective questioning combined with grounded retrieval catches blind spots that single-pass research (whether by human or LLM) misses. The retrieval is what makes the perspectives meaningful. Without it, you are just asking the model to roleplay as five different experts using only what it already knows. The system's value comes from the combination of perspective diversity AND real grounding in external sources.

## Next Step: Co-STORM

The followup paper, "Into the Unknown Unknowns" (EMNLP 2024, arXiv 2408.15232), extends STORM from autonomous article generation to collaborative human-AI knowledge curation. See `research/raw/costorm-emnlp-2024.md`.

## Cross-References in This Brain

This research relates to:
- The centaur principle: human + machine + better process beats inferior process. STORM is a better process for research.
- The unknown unknowns problem: articulated in systems we have studied.
- Multi-perspective questioning as a general methodology, applicable beyond Wikipedia-style writing.
- Co-STORM's model of human-steered agent discourse maps to our operating model.

## Provenance

All claims in this document trace to:
- arXiv 2402.14207v2 (abstract, methodology, evaluation details)
- arXiv API metadata (authors, dates, categories)
- GitHub repository stanford-oval/storm (implementation details, roadmap, metrics)
- ACL Anthology 2024.naacl-long.347 (venue confirmation)
- SkillPack evaluation page (citation metrics)
- aibars.net library entry (FreshWiki/WildSeek dataset details, pipeline toggles, Co-STORM usage example)