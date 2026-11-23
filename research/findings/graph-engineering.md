---
title: "Graph Engineering: A Joke That Became a Discipline"
tags: [finding, ai-agents, orchestration, harness-engineering, terminology, multi-agent]
related:
- harness-engineering
- agent-orchestrator-pattern
- agent-harness-architecture
- workflow-as-contract
- agent-architectures
- knowledge-graphs-as-agent-memory-substrate
- loops-as-orchestration-primitive
- openclaw
source: research/raw/graph-engineering.md
ingested: 2026-11-23
---

# Graph Engineering: A Joke That Became a Discipline

## Key Points

**The coinage was a joke.** On 2026-07-18 Peter Steinberger (@steipete, the OpenClaw creator) posted nine words: "Are we still talking loops or did we shift to graphs yet?" (3.13M views). Louis Bouchard reports that both that post and the follow-up that named the term "were jokes," and that Steinberger "was poking at how fast we rename things." The naming took hold within four days: LangChain published "3 Years of Graph Engineering with LangGraph" on 2026-07-22, opening with "'Graph engineering' surfaced this weekend, kicked off by this tweet." The single most important fact about the term is that a joke about naming churn was read as a research programme, and the field then built the programme.

**What the term means.** A loop lets the agent decide the path, iterating on one task until it meets a bar; a graph has you pre-draw the steps, routes, checkpoints, and gates, as a state machine whose nodes can contain loops but whose overall structure is fixed. Shannon Holmberg's one-line test: the difference is "who decides the path, the agent or you." The stated primitives are state, nodes, and edges, with a router node holding conditional edges. One formulation of the relationship: "A loop is just a single-node graph with an edge back to itself."

**The sequence it belongs to.** LangChain's framing is "the latest term to come out of X's AI content factory, joining prompt engineering, context engineering, harness engineering, and loop engineering." Per-term origins: prompt engineering was diffuse with no naming event; context engineering was proposed by Tobi Lütke on 2025-06-18, popularized by Karpathy on 2025-06-25, canonized by Anthropic in September 2025; harness engineering was first attested by Mitchell Hashimoto on 2026-02-05 and popularized by OpenAI's Codex post on 2026-02-11; loop engineering has no verifiable origin post. Two widely repeated attributions are unverified and should not be asserted: that OpenAI coined "harness engineering" in 2025, and that Hamel Husain wrote "Loop engineering is dead. Enter graph engineering."

**The strongest critique is not that the capabilities are fake but that the word is a naming event attached to existing practice.** Anthropic's "Building Effective Agents" (Schluntz and Zhang, December 2024) drew the same axis as workflows ("predefined code paths") versus agents (dynamic control) nineteen months before the coinage, and named the five patterns now absorbed into the vocabulary. The live critics: Paweł Huryn ("I call BS on graph engineering... None of this is new"), Zach Tratar (a rebrand of two-year-old practice), and David Khourshid, the XState creator. Luckey Faraday's line is the best compression: "Graphs tell you where you can go. State machines tell you when you're allowed to go there. Actors tell you who is making the decision."

**The genuine structural difference is the node.** In a workflow engine the node is a task with fixed semantics; in an agent graph it interprets its work, up to being a full agent run in LangChain's own taxonomy. The graph is structurally the same object the workflow lineage has used for a decade (Airflow, Step Functions, Temporal, XState statecharts). The vendor advocating the term sells both the framework and the tracing platform, and its own post concedes the term "isn't a new idea" and that graphs are sometimes the wrong shape: its own deep research example walked from predefined LangGraph workflows to a more agentic loop, and GPT Researcher made the same move.

**No published head-to-head isolates graph topology from model and tooling on a real task.** The commonly cited GPT Researcher numbers (report quality 0.503 to 0.512, verified citations 18.6 to 35.2) vary the research tooling, not the topology, so they do not support "graphs beat loops."

**The word is four-valued.** A directed graph of computation over shared mutable state (execution, executed not queried); an RDF triple store or labeled property graph (data, static and read at retrieval, the concern of GraphRAG); a reasoning structure (Graph of Thoughts, Besta et al., AAAI 2024); and a model architecture (graph neural networks). This Substrate's own knowledge graph is the data sense, so a reader here is more likely than average to reach for the wrong meaning.

**The risk inside the pattern is directionally supported by peer-reviewed work.** Panickssery, Bowman, and Feng (NeurIPS 2024) show self-preference is causally tied to self-recognition; Cemri et al. (NeurIPS 2025 Datasets and Benchmarks Spotlight) find state-of-the-art multi-agent systems fail at 41 to 86.7 percent with verification defects as a named category. Same-model verifiers over shared flawed context are the worst configuration described. But the overstated version should not be repeated: the skeptical work (Chen et al., arXiv:2510.20963, preprint) shows specific debate protocols failing or tying a single agent under matched budgets, and the recommended fixes buy measured gains on the order of 10 to 15 percent. The defensible claim is that naive agents-verifying-agents on shared context add cost without guaranteeing accuracy.

## Open Questions

- No one has published a controlled comparison of graph topology against a single agent loop on a real task, holding model and tooling constant — the experiment the whole discourse lacks.
- Per-node cost and latency accounting for agent graphs has no published standard.
- The next term in the sequence is not yet named; the "harness engineering is not dead" argument of 2026-11-22 is where to watch for it.

## Source

`research/raw/graph-engineering.md` (LangChain's post, Bouchard's explainer, and Anthropic's "Building Effective Agents" read in full; X material via Grok x_search fallbacks). It is the immediate successor to [[harness-engineering]] in the same axis and extends the framework survey in [[agent-architectures]]. The orchestration layer it formalizes is [[agent-orchestrator-pattern]]; the harness primitives it orchestrates are [[agent-harness-architecture]]; the specification idea it restates in older language is [[workflow-as-contract]]; and the loop lineage it inherits is [[loops-as-orchestration-primitive]]. The data-sense collision is live in [[knowledge-graphs-as-agent-memory-substrate]], and the joke's originator is the entity behind [[openclaw]].
