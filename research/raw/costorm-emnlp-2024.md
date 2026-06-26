---
source_url: https://arxiv.org/abs/2408.15232
ingested: 2026-06-26
sha256: TBD
---

# Co-STORM: Into the Unknown Unknowns

**Paper:** "Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations"
**Authors:** Yucheng Jiang, Yijia Shao, Dekun Ma, Sina J. Semnani, Monica S. Lam
**Affiliation:** Stanford University, OVAL Lab (Open Virtual Assistant Lab)
**Venue:** EMNLP 2024 Main Conference
**arXiv:** 2408.15232v2 (submitted August 27, 2024; revised October 17, 2024)
**Categories:** cs.CL, cs.AI, cs.IR
**Pages:** 9917-9955 (39 pages)
**Code:** https://github.com/stanford-oval/storm (integrated into knowledge-storm v1.0.0, September 2024)
**Dataset:** WildSeek (real information-seeking records with explicit user goals)

## What Co-STORM Is

Co-STORM extends STORM from autonomous article generation to **collaborative human-AI knowledge curation**. Where STORM's goal is to produce a finished article from a topic string, Co-STORM's goal is to help a human researcher discover what they do not know they do not know. The paper was accepted at EMNLP 2024, the top venue for empirical NLP research.

The framing comes from the unknown unknowns problem: traditional QA systems (chatbots, search engines) require the user to ask all the right questions. But if you are exploring a topic you do not understand, you cannot know what questions to ask. The system places the burden on the user to formulate queries. Co-STORM removes that burden by having agents ask questions on the user's behalf.

## Core Problem

The paper articulates a specific failure mode in existing LM-powered tools:

- Chatbots answer concrete questions well but cannot anticipate what else the user might need to know.
- Generative search engines return relevant documents but do not discover information the user did not think to search for.
- Both require the user to drive the conversation or search, which fails when the user lacks the domain knowledge to ask good questions.

This is the "unknown unknowns" gap. You do not know what you do not know, and the tools you have require you to ask about what you know you do not know.

## Core Methodology

Co-STORM's design is inspired by an educational scenario: children learn by listening to and sometimes participating in conversations among adults (parents, teachers). They absorb knowledge by observation, not just by asking questions. Co-STORM applies this to AI-assisted research.

### The Collaborative Discourse Model

Instead of a user querying an LLM, Co-STORM sets up a conversation among multiple LM agents, each bringing a different perspective to the topic. The user observes this conversation and can steer it:

1. **Agent-initiated questioning.** Multiple LM agents ask questions about the topic. The questions are grounded in retrieval (real web search, same as STORM). The agents are not role-playing with parametric knowledge alone; they retrieve and ground their questions and answers in real sources.

2. **User as observer and occasional participant.** The user watches the agent discourse unfold. They can inject a question or steer the conversation when they have a specific interest, but they are not required to drive it. The burden of knowing what to ask is removed.

3. **Dynamic mind map.** As the discourse progresses, Co-STORM organizes the uncovered information into a real-time mind map. This gives the user a structural view of what has been discovered, helping them track the conversation without reading every exchange. The mind map updates dynamically as new information surfaces.

4. **Comprehensive report generation.** At the end of the session, Co-STORM generates a report from the curated knowledge base. This is the takeaway: a structured document synthesizing what the discourse uncovered.

### How This Differs from STORM

| Dimension | STORM | Co-STORM |
|-----------|-------|----------|
| Goal | Generate a Wikipedia-style article from a topic | Discover unknown unknowns through collaborative discourse |
| Human role | None during research (autonomous pipeline) | Observer and occasional steerer of agent discourse |
| Output | Finished article with citations | Dynamic mind map + comprehensive report |
| Question asking | System generates all questions automatically | Agents ask questions; user can inject their own |
| Interaction model | Batch (topic in, article out) | Interactive (ongoing discourse with human steering) |
| Unknown unknowns | Not explicitly addressed | The core problem the system is designed to solve |

The key shift is from autonomous generation to human-in-the-loop discovery. STORM produces a better article. Co-STORM produces a better understanding, because the human is involved in the steering.

## Evaluation

### WildSeek Dataset

The authors constructed WildSeek from real information-seeking records collected from the STORM web research preview. Each data point is a pair: a topic and the user's goal for conducting deep search on that topic. This is a novel evaluation resource because it captures genuine open-ended information needs, not contrived query patterns.

The dataset is available on HuggingFace (YuchengJiang/WildSeek).

### Automatic Evaluation

Co-STORM outperforms baseline methods on both:
- **Discourse trace quality:** the quality of the conversation itself (are the questions good, are the answers grounded, is the discourse coherent)
- **Report quality:** the quality of the final synthesized report

### Human Evaluation

The headline results:

- **70% of participants prefer Co-STORM over a search engine**
- **78% of participants prefer Co-STORM over a RAG chatbot**

These are preference studies, not quality scores. They measure whether users found the experience more useful for their information-seeking goal, not whether the output is objectively "better." This is an important distinction. The preference is driven by the experience of discovering unknowns, not just by output quality.

## Connection to the Centaur Principle

Co-STORM's model is directly relevant to how we operate. The centaur principle holds that weak human + machine + better process beats any combination with inferior process. Co-STORM is a better process for research:

1. **Division of labor.** The human writes intent (the topic and occasional steering). The agents do the heavy lifting of questioning, retrieving, and grounding. The human observes and redirects. This is exactly our operating model from AGENTS.md.

2. **Reduced cognitive load.** The user does not need to know what to ask. The agents surface questions the user would not have thought of. This is the unknown unknowns mechanism in action.

3. **Real-time structural awareness.** The dynamic mind map gives the human a map of what has been discovered without forcing them to read every exchange. This is a compression mechanism: the human can steer without drowning in detail.

4. **Serendipitous discovery.** Because agents ask questions the user did not think of, the discourse surfaces information that targeted search would never find. This is the core value proposition.

## Co-STORM Python Usage (from repository)

```python
from knowledge_storm.collaborative_storm.engine import (
    CollaborativeStormLMConfigs, RunnerArgument, CoStormRunner
)

lm_config = CollaborativeStormLMConfigs()
# ... Configure various language models ...

topic = input('Topic: ')
runner_argument = RunnerArgument(topic=topic, ...)
costorm_runner = CoStormRunner(lm_config=lm_config, ...)

# Warm-start the system
costorm_runner.warm_start()

# Conduct collaborative dialogue
conv_turn = costorm_runner.step()
# Or inject user utterance
costorm_runner.step(user_utterance="YOUR UTTERANCE HERE")

# Generate report
costorm_runner.knowledge_base.reorganize()
article = costorm_runner.generate_report()
```

The `warm_start()` method bootstraps the agent discourse. `step()` advances one turn of the conversation. The user can inject utterances to steer the discourse. `generate_report()` produces the final output from the curated knowledge base.

## Current Status

- Codebase released September 2024 as part of `knowledge-storm` Python package v1.0.0
- Install: `pip install knowledge-storm --upgrade`
- Integrated into the live demo at storm.genie.stanford.edu alongside the original STORM
- The GitHub repository's roadmap lists two active development areas: (1) human-in-the-loop functionalities, and (2) information abstraction for non-Wikipedia formats

## Key Insight

Co-STORM is the more operationally relevant paper for us. STORM proves that multi-perspective questioning with retrieval produces better research. Co-STORM proves that human-steered agent discourse is preferable to both search engines and RAG chatbots for discovering what you do not know. The shift from autonomous generation to collaborative discovery is the shift from "produce output" to "build understanding," and the latter is what we actually need.

The centaur principle in practice: the human's role is not to generate knowledge but to steer the process that generates it. Co-STORM operationalizes this by making the human an observer and occasional participant in agent discourse, not the driver.

## Provenance

All claims in this document trace to:
- arXiv 2408.15232v2 (abstract, methodology, evaluation, dataset details)
- arXiv API metadata (authors, dates, categories, pages)
- ACL Anthology 2024.emnlp-main.554 (venue, page numbers, citation)
- GitHub repository stanford-oval/storm (implementation details, Python usage, dataset availability)
- aibars.net library entry (Co-STORM usage examples, pipeline details)
- STORM paper (arXiv 2402.14207) for the relationship and differentiation table