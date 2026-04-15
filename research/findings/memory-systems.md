---
title: Agent Memory Systems
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/memory-systems.md
---

# Agent Memory Systems

## The Problem

LLMs have no memory. Every session starts blank. Every context window is finite. Every conversation eventually gets compacted or lost. Memory systems are the prosthetics we build to compensate.

## Memory Taxonomy

### Short-Term Memory (Context Window)

**What it is:** The conversation itself. The tokens currently loaded into the model's attention.

**Properties:**
- Immediate, fast, high-fidelity
- Finite (200K tokens for Claude, 128K-1M for others)
- Lost on session end or compaction
- Everything the model "knows" right now

**How systems implement it:**
- Raw conversation history (most basic)
- Sliding window with summarization (ChatGPT, most chatbots)
- Structured context injection (system prompts, file contents)
- Compaction: summarize old context to fit new context (OpenClaw, Claude Code)

**The core tension:** More context = better understanding, but also more cost, more noise, more potential for the model to lose focus. The context window is not RAM; it's more like a desk. Too much on the desk and you can't find anything.

### Long-Term Memory (Persistent Storage)

**What it is:** Information that survives across sessions. Files, databases, vector stores.

**Implementations across systems:**

| System | Approach | Storage |
|--------|----------|---------|
| ChatGPT Memory | Key-value facts extracted from conversation | OpenAI's servers |
| Claude Projects | Project knowledge (uploaded files) | Anthropic's servers |
| MemGPT/Letta | Tiered memory (core/archival/recall) with self-editing | SQLite/Postgres + embeddings |
| AutoGPT | File-based workspace + vector DB | Local files + ChromaDB |
| Our system | MEMORY.md + daily files + workspace | Git-versioned files |

**Key design decisions:**
1. **Who writes memory?** The model itself (MemGPT) vs. the system (ChatGPT) vs. explicit process (us)
2. **What format?** Natural language vs. structured data vs. embeddings
3. **When to retrieve?** Every turn vs. on-demand vs. triggered by relevance
4. **How to forget?** Explicit deletion vs. decay vs. never

### Episodic Memory (Session Logs)

**What it is:** Records of what happened. Conversations, actions taken, outcomes observed. Like a human's autobiographical memory.

**Implementations:**
- **Session logs:** Full conversation transcripts (our daily files)
- **Reflexion-style:** Verbal summaries of what went well/wrong
- **Trace logs:** Action-observation pairs without the reasoning
- **Handoff documents:** Curated session summaries (our handoffs/)

**Value:** Enables learning from experience. "Last time I tried X, it failed because Y" is enormously valuable. Most agent systems don't do this well.

### Semantic Memory (Embeddings / Knowledge)

**What it is:** General knowledge organized for retrieval. Usually implemented with vector databases and embedding models.

**How it works:**
1. Chunk documents/experiences into segments
2. Embed each chunk into a vector
3. On query, embed the query and find similar chunks
4. Inject retrieved chunks into context

**Systems:**
- RAG (Retrieval-Augmented Generation): Standard pattern
- Vector DBs: Pinecone, Weaviate, ChromaDB, pgvector
- Hybrid: BM25 keyword search + semantic similarity

**Tradeoffs:**
- ✅ Scales to large knowledge bases
- ✅ Only retrieves what's relevant (efficient context use)
- ❌ Retrieval quality is noisy (wrong chunks, missing context)
- ❌ Embedding models lose nuance
- ❌ Chunking destroys document structure
- ❌ Operational complexity (embedding pipeline, vector DB, reindexing)

## Comparison: Our Approach vs. Alternatives

### What We Do (MEMORY.md + Daily Files)

```
MEMORY.md          → Curated long-term memory (human-maintained feel)
memory/YYYY-MM-DD  → Daily episodic logs (what happened)
handoffs/          → Session transition documents
AGENTS.md          → Procedural memory (how to do things)
SOUL.md            → Identity memory (who am I)
```

**Strengths:**
- Human-readable and auditable
- Git-versioned (full history, diffable)
- No infrastructure dependencies (no vector DB, no embedding pipeline)
- The model can read AND write its own memory
- Curated > comprehensive: MEMORY.md is distilled, not dumped
- Natural language: no schema to maintain

**Weaknesses:**
- Doesn't scale beyond ~50-100KB of memory files
- No semantic search: must load entire files
- Relies on the model remembering TO read memory files
- No automatic relevance filtering
- Manual curation requires discipline (and heartbeat cycles)

### MemGPT/Letta Approach

The most sophisticated open-source memory system. Treats the context window as "main memory" and external storage as "disk," with the agent managing its own memory operations (read, write, search, archive).

**Key ideas:**
- **Core memory:** Always in context. Editable by the agent. Small (~2K tokens). Contains user info, agent persona.
- **Archival memory:** Vector-indexed long-term store. Agent explicitly searches it.
- **Recall memory:** Conversation history, searchable.
- **Self-directed memory management:** The agent decides what to remember and forget.

**Assessment:** Clever but fragile. The agent's memory management adds cognitive load to every interaction. In practice, agents make bad memory decisions: they save trivial things and forget important ones. The analogy to OS memory management is appealing but breaks down because the "CPU" (the LLM) is unreliable.

### What We Should Actually Do

**Keep our current system.** It's working. The simplicity is a feature, not a bug. But evolve it:

1. **Add lightweight search.** Not a vector DB: just `grep` or a simple index over memory files. When the agent needs to find something in MEMORY.md or old daily files, it should be able to search, not just load everything.

2. **Automate the curation cycle.** The heartbeat-based MEMORY.md review is good but inconsistent. A dedicated cron job that summarizes the week's daily files into MEMORY.md candidates would reduce drift.

3. **Structure daily files slightly more.** Add YAML frontmatter with tags/topics. Makes search and filtering possible without embedding infrastructure.

4. **Don't add embeddings yet.** The operational complexity isn't justified at our scale. When MEMORY.md exceeds 50KB or we have >100 daily files, reconsider. Not before.

5. **Consider a "working memory" section.** A small, always-loaded snippet (like MemGPT's core memory) with the 5-10 most important current facts. Cheaper than loading all of MEMORY.md every session. This is essentially what the system prompt context injection already does, but could be more explicit.

**The deeper insight:** Memory systems are only as good as the retrieval. A perfectly indexed vector database is useless if the agent doesn't know when to query it. Our explicit, file-based approach forces the memory operations to be visible and auditable. That's worth more than sophistication.
