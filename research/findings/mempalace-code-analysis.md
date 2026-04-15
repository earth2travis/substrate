---
title: "MemPalace Code Analysis: Structure vs. Reality"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/mempalace-code-analysis.md
---

# MemPalace Code Analysis: Structure vs. Reality

**Researched:** 2026-04-08
**Source:** GitHub Repository (`milla-jovovich/mempalace`) and `mempalace.tech`

---

## I. The Architecture: A Dual-System Approach

MemPalace is built on two distinct data stores that talk to each other through the MCP server:

1.  **The Palace (ChromaDB):** Stores the actual verbatim conversations and mined project files. It uses metadata (wing, room, hall) to allow for "spatial" scoping of searches.
2.  **The Knowledge Graph (SQLite):** Stores structured "facts" extracted from those conversations as entity-relationship triples (Subject-Predicate-Object) with temporal validity.

**The Flow:**
`User/LLM` -> `MCP Server` -> `Searcher (ChromaDB)` + `KG Query (SQLite)` -> `Response`

---

## II. The "Spatial" Logic in Code

The "Palace" isn't a complex graph in the traditional sense; it's a clever use of **Metadata Filtering**:
*   **Wings** are just `wing` metadata tags in ChromaDB.
*   **Rooms** are `room` metadata tags.
*   **Tunnels** are simply a function (`palace_graph.py`) that looks for identical `room` names across different `wing` tags.
*   **Halls** are `hall` metadata tags (facts, events, discoveries, etc.).

**The Retrieval Boost:** The claimed "34% boost" from the palace structure is achieved by starting with a broad search and then progressively adding `where` clauses to the ChromaDB query to narrow the scope. It's a "Search within Wing" -> "Search within Room" cascade.

---

## III. Critical Code Gaps (The "AAAK-ing" Problem)

1.  **The Closet Illusion:** The README claims "Closets" are summaries that point to drawers. In the current code (`v3.0.0`), the "closet" is just a metadata pointer. The AAAK (abbreviation) logic exists in `dialect.py`, but it is **not** the default storage method. The system defaults to raw text.
2.  **The Fact-Checker Disconnect:** The `fact_checker.py` utility exists, but as the authors admitted, it isn't wired into the main retrieval loop. This means MemPalace will happily retrieve two contradictory "facts" from different wings without flagging the conflict unless the user runs a specific, separate command.
3.  **RegEx Reliance:** The `room_detector_local.py` and `convo_miner.py` rely heavily on regex and keyword matching. If a conversation doesn't contain specific "trigger words" (like "decision" or "preference"), it falls into a generic bucket, losing the nuance that a semantic extractor would catch.

---

## IV. Opportunities for Agent Factory Improvement

We can lift the **Spatial Scoping** concept while avoiding the **Implementation Flaws**:

*   **Context Stack as Wings:** We can treat our `research/`, `memory/`, and `decisions/` directories as "Wings." When we search, we can tell the LLM exactly which "Wing" to look in first, mimicking MemPalace's "34% boost" without needing a separate database.
*   **Graph-Backed Contradiction Detection:** Unlike MemPalace, where the KG is an afterthought, our **Context Stack** must have a "Conscience Layer." We should use our SQLite/Graph layer not just for storage, but for **active conflict resolution** before any context is ever presented to the LLM.
*   **The "No-Summary" Trap:** MemPalace's reliance on verbatim text is great for fidelity but bad for token efficiency. Our "Closets" should be **semantically compressed** by our Scout agent, ensuring we get the "30x compression" MemPalace claims without the "lossy" reality of their regex approach.

---

## V. The Verdict on MemPalace

It's a "Spatial UI" for vector search. The value isn't in the vector search itself (which is standard), but in the **human-legible organization** it provides. For the Agent Factory, this confirms that **structure is a form of intelligence**. By organizing our Context Stack into clear, named files, we are building our own "Palace" — one where every room has a clear purpose and a conscience.