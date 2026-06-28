---
title: "Co-STORM: Collaborative Human-AI Knowledge Curation for Unknown Unknowns"
tags: [research, ai, nlp, collaboration, knowledge-management, discovery, human-in-loop]
related:
- synthesis-over-retrieval
- llm-wiki-pattern
- centaur-principle
- karpathy-llm-knowledge-bases
- rag-vs-wiki
- agent-memory
source: research/raw/costorm-emnlp-2024.md
---
# Co-STORM: Collaborative Human-AI Knowledge Curation for Unknown Unknowns

## Summary

Co-STORM extends STORM from autonomous article generation to collaborative human-AI knowledge curation. Published at EMNLP 2024. Its core problem: traditional QA systems and chatbots require the user to ask all the right questions, but if you are exploring a topic you do not understand, you cannot know what questions to ask. Co-STORM removes that burden by having agents ask questions on the user's behalf.

## The Unknown Unknowns Problem

Chatbots answer concrete questions well but cannot anticipate what else the user might need to know. Generative search engines return relevant documents but do not discover information the user did not think to search for. Both require the user to drive the conversation. This fails when the user lacks domain knowledge to ask good questions. You do not know what you do not know, and the tools you have require you to ask about what you know you do not know.

## Collaborative Discourse Model

Instead of a user querying an LLM, Co-STORM sets up a conversation among multiple LM agents, each bringing a different perspective. The user observes and can steer:

1. **Agent-initiated questioning:** Multiple LM agents ask questions grounded in real web search retrieval. Agents are not role-playing with parametric knowledge alone.
2. **User as observer and occasional participant:** The user watches the discourse unfold and can inject a question or steer when interested, but is not required to drive it.
3. **Dynamic mind map:** Co-STORM organizes uncovered information into a real-time mind map, giving the user a structural view of what has been discovered without reading every exchange.
4. **Comprehensive report generation:** At session end, Co-STORM generates a structured report synthesizing what the discourse uncovered.

## Evaluation

WildSeek dataset constructed from real information-seeking records. Headline results: 70% of participants prefer Co-STORM over a search engine; 78% prefer Co-STORM over a RAG chatbot. These are preference studies measuring the experience of discovering unknowns, not just output quality.

## Why This Matters for the Substrate

Co-STORM is the more operationally relevant paper. STORM proves multi-perspective questioning with retrieval produces better research. Co-STORM proves human-steered agent discourse is preferable to both search engines and RAG chatbots for discovering what you do not know. The shift from autonomous generation to collaborative discovery is the shift from "produce output" to "build understanding."

This operationalizes the [[centaur-principle]] directly: the human's role is not to generate knowledge but to steer the process that generates it. The human writes intent (topic and occasional steering); agents do the heavy lifting of questioning, retrieving, and grounding. This is the Substrate's division of labor — the human curates sources and directs analysis; the agent summarizes, cross-references, and files.

The dynamic mind map is a compression mechanism: the human can steer without drowning in detail. This connects to [[agent-memory]] — structural awareness of what has been discovered without forcing the human to read every exchange. The serendipitous discovery (agents ask questions the user did not think of) is the core value proposition that [[rag-vs-wiki]] argues synthesis achieves but retrieval cannot.

The shift from "produce output" to "build understanding" maps to the difference between a finding (a compiled artifact) and the research process that produced it. The Substrate keeps both: the process is logged, the output is filed.

## Related

- [[synthesis-over-retrieval]] — Synthesis builds understanding; retrieval returns fragments
- [[llm-wiki-pattern]] — Compounding knowledge base maintained by LLMs
- [[centaur-principle]] — Human steers, agents execute; the division of labor
- [[rag-vs-wiki]] — RAG starts from zero per query; synthesis compounds