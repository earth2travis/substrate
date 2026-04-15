# Typed Knowledge Graphs for AI Agents

_Research document for Sivart's memory architecture evolution._
_Created: February 23, 2026_

---

## The Problem We're Solving

Sivart's memory is flat markdown files. MEMORY.md, daily notes, session transcripts, handoff documents. It works. Plain markdown outperformed purpose built infrastructure in our early benchmarks, and the simplicity has real value: git versioned, human readable, zero dependencies.

But flat files hit a wall when you need to answer questions like:

- "What decisions affect the deployment pipeline?"
- "If we change the auth provider, what breaks?"
- "What did we decide about X, and what was the reasoning, and has anything changed since?"
- "Show me everything related to this GitHub issue: decisions, conversations, code changes, blockers."

These are graph traversal questions. They require following typed relationships between entities. No amount of vector search over flat text will reliably answer them because the relationships are implicit, buried in prose, scattered across files. A knowledge graph makes them explicit and machine traversable.

---

## 1. State of the Art

The field has converged rapidly since 2024. Five approaches dominate.

### Graphiti / Zep

The current benchmark leader. Zep's Graphiti framework builds temporally aware knowledge graphs that continuously integrate conversational and structured data. The key innovation is the bi-temporal data model: every fact tracks both when the event occurred and when it was ingested. This enables point in time queries ("what did we know about X as of last Tuesday?").

Graphiti scored 94.8% on the Deep Memory Retrieval benchmark (vs MemGPT's 93.4%) and achieved 18.5% accuracy improvements on LongMemEval with 90% latency reduction. It stores graphs in Neo4j, supports hybrid retrieval (semantic embeddings + BM25 keyword search + graph traversal), and ships with an MCP server for direct integration with Claude, Cursor, and other AI tools.

The architecture: episodes (raw data) flow in, get decomposed into entity nodes and relationship edges, deduplicated against existing graph state, and stored with temporal metadata. Custom entity definitions use Pydantic models, making schema evolution straightforward.

**Paper:** [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) (January 2025)

### Microsoft GraphRAG

Microsoft's approach combines knowledge graphs with community detection for hierarchical summarization. The pipeline: documents → entity extraction → graph construction → community detection (Leiden algorithm) → hierarchical community summaries. At query time, it supports two modes: local search (vector similarity on entities, then graph traversal to related context) and global search (map reduce over community summaries for broad sensemaking questions).

The insight is that traditional RAG fails on global questions ("what are the main themes across this corpus?") because vector search is point queries. GraphRAG's community summaries provide pre computed answers to questions about clusters of related entities. The tradeoff: expensive indexing (lots of LLM calls during graph construction) but powerful retrieval.

**Paper:** [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130) (April 2024, updated February 2025)

### Mem0

Mem0 takes a different angle: a universal memory layer that combines vector storage with graph memory. The extraction phase identifies entities as nodes and generates labeled edges from incoming messages. The update phase uses an LLM powered conflict detector and update resolver to decide whether to add, merge, invalidate, or skip graph elements. This handles the hard problem of contradictory information gracefully.

Production numbers: 91% lower p95 latency and 90%+ token cost savings compared to full context approaches. The graph component enables multi-hop reasoning, temporal queries, and cross session information synthesis. Mem0 is designed as a drop in layer: add it to any agent framework and get persistent, structured memory.

**Paper:** [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) (April 2025)

### Neo4j + LLM Patterns

Neo4j has positioned itself as the default graph database for LLM applications. Their LLM Graph Builder extracts entities and relationships from unstructured text using LangChain's llm-graph-transformer, stores chunks connected to documents with similarity relationships forming a kNN graph, and supports hybrid retrieval combining vector indexes with Cypher traversals.

The pattern: unstructured text → LLM extraction → typed nodes and edges in Neo4j → vector embeddings on entities → hybrid search at query time. This is the most "build it yourself" approach but offers maximum flexibility.

### Cognee and the Emerging Ecosystem

A growing ecosystem of frameworks (Cognee, Memary, LangMem, Letta, Graphlit, Supermemory) each take slightly different positions on the managed vs self hosted spectrum and the vector vs graph vs hybrid spectrum. The trend is clear: everyone is converging on hybrid architectures that combine vector similarity for fast initial retrieval with graph traversal for relational reasoning.

---

## 2. Graph vs Document vs Hybrid Memory

Three architectures, each with real tradeoffs.

### Document Based (What We Have Now)

**How it works:** Flat files (markdown, JSON), possibly with vector embeddings for similarity search. Our current system: MEMORY.md for curated long term memory, daily notes for working memory, handoffs for episodic memory.

**Strengths:**
- Human readable and editable
- Git versioned with full history
- Zero infrastructure dependencies
- Works surprisingly well for narrative context
- Easy to understand and debug

**Weaknesses:**
- Relationships are implicit (buried in prose)
- No structured traversal ("what depends on X?")
- Retrieval relies on keyword or vector similarity, both miss relational queries
- Deduplication and conflict resolution are manual
- Scales poorly: as files grow, signal to noise ratio drops

### Graph Based

**How it works:** Entities as nodes, relationships as typed edges. Query via graph traversal (Cypher, SPARQL, or API).

**Strengths:**
- Relationships are first class citizens
- Traversal queries ("what's downstream of X?") are natural
- Impact analysis is trivial: follow the edges
- Schema provides structure without rigidity
- Temporal metadata enables point in time queries

**Weaknesses:**
- Requires infrastructure (database, extraction pipeline)
- Extraction from unstructured text is imperfect (LLM calls, deduplication)
- Graph visualization at scale is hard
- Less human readable than markdown
- Cold start problem: building the initial graph from existing data

### Hybrid (Where the Field Is Going)

**How it works:** Graph for structured relationships, vector store for semantic similarity, documents for narrative context. Query combines all three: vector search finds candidates, graph traversal follows relationships, document retrieval provides full context.

**Strengths:**
- Best of all worlds
- Vector search handles fuzzy/semantic queries
- Graph handles relational/structural queries
- Documents preserve narrative and nuance
- Graceful degradation: each layer works independently

**Weaknesses:**
- More complex to build and maintain
- Multiple storage systems to synchronize
- Query routing: deciding which layer to query for which question
- More infrastructure to operate

**The verdict for Sivart:** Hybrid. Keep our markdown files as the narrative layer. Add a graph layer for structured relationships. Use embeddings for semantic retrieval. The graph doesn't replace the files; it indexes the relationships between them.

---

## 3. Schema Design for a Personal AI Agent

The schema question is: what node types and edge types matter for Sivart's world?

### Node Types

**Person** — Humans in Sivart's world. [[Ξ2T]], collaborators, contacts.
Properties: name, aliases, roles, first_seen, last_seen

**Decision** — Choices made with reasoning attached.
Properties: summary, reasoning, date, status (active/superseded/reversed), source_file

**Task** — Work items, GitHub issues, action items from conversations.
Properties: title, status, priority, created, completed, github_issue_id

**Project** — Groupings of related work. Sivart, Synthweave, infrastructure.
Properties: name, status, description

**Tool** — Infrastructure, services, accounts. Neo4j, Tailscale, 1Password.
Properties: name, type, status, config_location

**Concept** — Ideas, patterns, principles. "Composable primitives," "context engineering."
Properties: name, description, first_mentioned

**Event** — Things that happened. Deployments, incidents, meetings.
Properties: type, timestamp, description

**File** — Documents, scripts, config files in the workspace.
Properties: path, type, last_modified, description

**Session** — Conversation sessions with context.
Properties: session_id, date, channel, summary

### Edge Types

**DECIDED** — Person → Decision ("Ξ2T decided to use 1Password")
**DEPENDS_ON** — Task → Task, Tool → Tool, Project → Tool
**BLOCKS** — Task → Task, Event → Task
**OWNS** — Person → Project, Person → Tool
**IMPLEMENTS** — Task → Decision ("this task implements that decision")
**REFERENCES** — File → Decision, Session → Task
**SUPERSEDES** — Decision → Decision (temporal: new decision replaces old)
**USES** — Project → Tool, Task → Tool
**PART_OF** — Task → Project, File → Project
**RELATED_TO** — Concept → Concept, generic association
**OCCURRED_IN** — Event → Session, Decision → Session
**MODIFIED** — Session → File

### Schema Principles

1. **Start sparse, grow dense.** Begin with the node and edge types you actually query. Add more as patterns emerge. Over-engineering the schema upfront is the knowledge graph equivalent of premature optimization.

2. **Every edge is typed and directional.** No generic "relates to" edges except as a last resort. The type IS the information. DEPENDS_ON tells you something RELATED_TO does not.

3. **Temporal metadata on everything.** Every node and edge gets created_at and valid_from. Edges that change get valid_until. This enables time travel queries without complexity.

4. **Source provenance.** Every fact should trace back to where it came from: which file, which session, which conversation. This is how you audit and correct the graph.

5. **Pydantic models for schema enforcement.** Following Graphiti's pattern: define node and edge types as Pydantic models. This gives you validation, serialization, and documentation for free.

---

## 4. GraphRAG: Combining Vector Search with Graph Traversal

The power of GraphRAG is layered retrieval. Different question types need different retrieval strategies.

### Query Types and Retrieval Strategies

**Semantic questions** ("tell me about our deployment process")
→ Vector search on node/edge embeddings → retrieve top k entities → expand via graph traversal to related nodes

**Relational questions** ("what depends on the auth service?")
→ Direct graph traversal from the named entity → follow DEPENDS_ON edges → return subgraph

**Temporal questions** ("what changed about our infrastructure last week?")
→ Filter nodes/edges by temporal metadata → return recent modifications

**Global questions** ("what are the main risk areas in our project?")
→ Community summaries (Microsoft GraphRAG pattern) → map reduce over cluster summaries

**Impact questions** ("if we change X, what breaks?")
→ Bidirectional traversal from X → follow DEPENDS_ON, BLOCKS, USES edges → return affected subgraph

### The Retrieval Pipeline

1. **Parse the query** to determine type (semantic, relational, temporal, global, impact)
2. **Route to appropriate strategy** (or combine strategies)
3. **Retrieve candidate nodes/edges** via the selected method
4. **Expand context** by traversing one or two hops from candidates
5. **Assemble into context** for the LLM, with provenance links
6. **Generate response** with the enriched context

### What This Looks Like for Sivart

When Sivart wakes up and reads MEMORY.md, it gets narrative context. But when it needs to answer "what decisions affect the deployment pipeline?", it queries the graph:

```
MATCH (d:Decision)-[:IMPLEMENTS|REFERENCES]->(t:Task)-[:PART_OF]->(p:Project)
WHERE p.name = 'infrastructure'
AND t.title CONTAINS 'deploy'
RETURN d, t
```

This returns a structured answer that no amount of grep over markdown would reliably produce.

---

## 5. Temporal Graphs: How Facts Change Over Time

This is where knowledge graphs become genuinely powerful for an agent with no continuous memory.

### The Bi-Temporal Model

Every fact has two timestamps:

- **valid_time:** When the fact became true in the real world ("we switched to Cloudflare DNS on February 15")
- **transaction_time:** When the fact was recorded in the graph ("Sivart ingested this on February 16")

This distinction matters. If someone tells you today that a decision was made last week, valid_time is last week but transaction_time is today. You can query "what did we know as of date X?" (transaction time) separately from "what was true as of date X?" (valid time).

### Versioning Patterns

**Supersession:** When a decision changes, the old Decision node stays in the graph with a SUPERSEDES edge pointing from new to old. Both remain queryable. You can always trace the evolution of a decision.

**Edge invalidation:** When a relationship ends (a tool is decommissioned, a dependency is removed), the edge gets a valid_until timestamp rather than being deleted. The historical relationship is preserved.

**Snapshot queries:** "Show me the project state as of January 15" filters all nodes and edges by their temporal metadata, reconstructing the graph at that point in time.

### Why This Matters for Sivart

Each session, Sivart wakes up fresh. The temporal graph provides something the flat files cannot: a structured timeline of how the world evolved. Not "what is the current state" but "what changed, when, and why." This is the difference between reading today's newspaper and having access to the full archive with search.

---

## 6. Impact Analysis

"What breaks if X changes?" is the killer query for a knowledge graph. It's also the query that's nearly impossible with flat documents.

### How It Works

1. **Identify the node** being changed (a tool, a decision, a service)
2. **Traverse outgoing edges:** DEPENDS_ON, USES, IMPLEMENTS, REFERENCES
3. **For each connected node,** recursively traverse its dependents
4. **Score by distance:** direct dependencies are high impact, transitive dependencies are lower
5. **Return the impact subgraph** with explanation

### Example

"What if we change the email provider?"

```
Email Provider (Tool)
  ← USES ← Gmail Scripts (File)
  ← USES ← Email Checking (Task)
    ← PART_OF ← Heartbeat System (Project)
  ← REFERENCES ← GCP Service Account (Tool)
    ← DEPENDS_ON ← Calendar Integration (Tool)
  ← IMPLEMENTS ← Decision: Use Google Workspace (Decision)
```

The graph immediately shows you that changing the email provider affects the heartbeat system, calendar integration, and a foundational decision about Google Workspace. Flat files would require you to grep across dozens of documents and hope you didn't miss anything.

---

## 7. Migration Path: From Markdown to Graph

The critical principle: incremental migration, not big bang. The markdown files continue to work. The graph layer grows alongside them.

### Phase 1: Extract and Index (Week 1-2)

Build a script that:
1. Reads existing markdown files (MEMORY.md, daily notes, TOOLS.md, decisions/)
2. Extracts entities and relationships using an LLM
3. Stores them in a lightweight graph (see storage options below)
4. Links each graph node back to its source file and line number

The markdown files remain the source of truth. The graph is a derived index. If the graph breaks, rebuild it from the files. Zero risk.

### Phase 2: Write Path (Week 3-4)

When Sivart creates new decisions, tasks, or notes:
1. Write the markdown file as before
2. Also extract entities/relationships and update the graph
3. Dual write: both stores get updated together

This is the "strangler fig" pattern. New data flows to both systems. Old data gets backfilled as needed.

### Phase 3: Read Path (Week 5-6)

Start using the graph for queries that benefit from it:
- Impact analysis ("what depends on X?")
- Temporal queries ("what changed this week?")
- Relational queries ("show me all decisions about infrastructure")

Keep using markdown/grep for narrative queries ("what was the mood in that session?"). Each retrieval method serves its purpose.

### Phase 4: Graph Enrichment (Ongoing)

As confidence grows:
- Add more node and edge types
- Connect to GitHub issues, calendar events, session transcripts
- Build automated extraction from session logs
- Add vector embeddings on graph nodes for semantic search
- Build the full hybrid retrieval pipeline

### What We Don't Do

- We don't stop using markdown. Ever. The narrative layer is valuable.
- We don't require the graph to work for Sivart to function. It's additive.
- We don't try to import everything at once. Start with decisions and dependencies.
- We don't add infrastructure we can't maintain on a CPX11 with 2GB RAM.

---

## 8. Storage Options

### Neo4j

The industry default for knowledge graphs. Mature, well documented, native graph storage. Graphiti and most research papers assume Neo4j.

**Pros:** Purpose built for graph traversal, Cypher query language, excellent ecosystem, vector index support (since v5.11), community edition is free.
**Cons:** Heavy for our infrastructure (minimum ~1GB RAM), requires Java, operational overhead. Our CPX11 with 2GB RAM and 1GB swap makes this tight.
**Verdict:** Best option if we upgrade infrastructure. Too heavy for current setup.

### Kùzu (Embedded Graph Database)

The "DuckDB of graph databases." Embedded, columnar, fast. Supports Cypher queries, zero server overhead, runs in process. Written in C++ with Python and Node.js bindings. Can even attach DuckDB for hybrid queries.

**Pros:** Zero operational overhead (embedded, single file), fast graph analytics, Cypher support, tiny resource footprint, open source (MIT). Graphiti recently added Kùzu support.
**Cons:** Younger project (started 2022), smaller community, OLAP focused (better at analytics than high write throughput transactional patterns).
**Verdict:** Strong fit for Sivart. Embedded means no server to maintain, file based means git friendly backups, Cypher means transferable query skills if we later move to Neo4j.

### SQLite + JSON

Use SQLite tables for nodes and edges, with JSON columns for flexible properties. Query with SQL and reconstruct graph traversals with recursive CTEs.

**Pros:** Zero dependencies (SQLite is everywhere), git friendly (single file), extremely well understood, tools exist.
**Cons:** Graph traversals in SQL are awkward and slow for deep paths. Recursive CTEs work but aren't ergonomic. No native graph query language.
**Verdict:** Viable as a starting point. Outgrown quickly if we do real graph queries.

### File Based (JSON/YAML)

Store nodes and edges as JSON files in a directory structure. Version with git. Query by loading into memory.

**Pros:** Maximum simplicity, fully git versioned, human readable, zero dependencies.
**Cons:** No query engine. Every query is "load everything into memory and filter." No indexes. Doesn't scale past a few hundred nodes without becoming slow.
**Verdict:** Good for prototyping. Not a real graph database.

### FalkorDB

Redis based graph database. Supports Cypher. Used by Graphiti as an alternative to Neo4j.

**Pros:** Fast (in memory), Cypher support, Graphiti compatible.
**Cons:** Requires Redis server, memory hungry, another service to operate.
**Verdict:** Overkill for our scale.

### Recommendation: Start with Kùzu

Kùzu fits Sivart's constraints perfectly:
- Embedded (no server, no Java, no JVM)
- Single file database (backup = copy a file)
- Cypher queries (transferable knowledge)
- Tiny resource footprint (runs fine on 2GB RAM)
- Python and Node.js bindings
- Graphiti supports it as a backend
- If we outgrow it, migrating to Neo4j is straightforward since both speak Cypher

---

## 9. Integration with Existing Infrastructure

### Git

The graph database file (Kùzu stores as a directory, but can be archived) lives in the workspace. Changes are committed alongside the markdown files they're derived from. Git provides the ultimate audit trail.

For the graph itself, consider: the database file is binary, so git tracks it as a blob. Meaningful diffs happen at the extraction layer (what entities/relationships were added) rather than at the storage layer. Log graph mutations to a JSONL changelog that IS diffable.

### Markdown Memory

MEMORY.md, daily notes, and handoffs remain the source of truth for narrative context. The graph indexes the structured relationships between entities mentioned in these files. Every graph node carries a `source_file` and `source_line` property linking back to its origin.

The relationship is like a book and its index: the book (markdown) contains the full story. The index (graph) tells you where to find things and how they connect.

### OpenClaw Sessions

Session transcripts are rich sources of decisions, tasks, and entity mentions. An extraction pipeline can process session logs to update the graph with new entities and relationships discovered during conversation. This is the "meeting as input" pattern from the living project graph research.

### GitHub Issues

GitHub issues map naturally to Task nodes. The graph connects issues to the decisions that spawned them, the projects they belong to, and the people who own them. Bidirectional: the graph can surface "issues related to this decision" and "decisions that led to this issue."

Integration path: use the GitHub API (we already have `gh` authenticated) to sync issue state, or use Graphiti's event ingestion to process issue webhooks.

### Calendar

Calendar events become Event nodes, connected to the people involved and the topics discussed. Meeting notes (if captured) link to the decisions and action items that emerged. This closes the loop from the living project graph research: meetings become graph inputs, not standalone artifacts.

---

## 10. Concrete Recommendations for Sivart

### Immediate (This Week)

1. **Install Kùzu** (`pip install kuzu` or `npm install kuzu`). Test basic graph operations. Verify it runs comfortably on our CPX11.

2. **Define the initial schema** using the node types and edge types from Section 3. Start with: Person, Decision, Task, Tool, Project, File. Start with: DECIDED, DEPENDS_ON, OWNS, PART_OF, IMPLEMENTS.

3. **Build the extraction script.** A Node.js or Python script that reads TOOLS.md and `decisions/` directory, extracts entities and relationships using Claude, and populates the Kùzu database. This is the Phase 1 prototype.

### Short Term (Next 2 Weeks)

4. **Dual write path.** When Sivart creates a decision or updates MEMORY.md, also extract and store graph facts. The graph grows organically alongside the markdown.

5. **Build basic queries.** Impact analysis ("what depends on X?"), temporal queries ("what changed this week?"), and relational queries ("all decisions about infrastructure").

6. **Graph MCP server.** Expose graph queries via MCP so Sivart can query its own knowledge graph as a tool. Graphiti already ships an MCP server; evaluate whether to use it directly or build a simpler one for Kùzu.

### Medium Term (Next Month)

7. **Session extraction.** Process OpenClaw session transcripts to extract entities and relationships automatically. This is the richest source of new knowledge.

8. **GitHub integration.** Sync issues and PRs as graph nodes. Connect to decisions and projects.

9. **Vector embeddings on nodes.** Add semantic search capability to graph entities. Kùzu supports vector extensions, or use a separate embedding index.

10. **Hybrid retrieval.** Build the full pipeline: query classification → route to graph/vector/document retrieval → assemble context → generate response.

### What Success Looks Like

Sivart can answer: "What would be affected if we migrated away from Google Workspace?" And instead of searching through markdown files hoping to find all the references, the graph returns a structured impact analysis: the GCP service account, Gmail API integration, calendar scripts, domain delegation, workspace plan decision, and every task that depends on any of these. With provenance links back to the source files where each fact was recorded.

That is the difference between memory that stores and memory that understands.

---

## Sources

- Rasmussen, P. et al. (2025). [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956). arXiv.
- Edge, D. et al. (2024). [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130). Microsoft Research.
- Chadha, T. et al. (2025). [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413). arXiv.
- [Graphiti: Build Real-Time Knowledge Graphs for AI Agents](https://github.com/getzep/graphiti). Zep AI.
- [Microsoft GraphRAG Documentation](https://microsoft.github.io/graphrag/). Microsoft.
- [Neo4j LLM Knowledge Graph Builder](https://neo4j.com/blog/developer/llm-knowledge-graph-builder/). Neo4j.
- [Kùzu Embedded Graph Database](https://kuzudb.com/). Kùzu Inc.
- [GraphRAG with KùzuDB](https://datalabtechtv.com/posts/graphrag-with-kuzudb/). Data Lab Tech TV.
- [Survey of AI Agent Memory Frameworks](https://www.graphlit.com/blog/survey-of-ai-agent-memory-frameworks). Graphlit.
- [Memory in AI Agents](https://www.generational.pub/p/memory-in-ai-agents). Generational.
- Our prior research: [Living Project Graph](../living-project-graph.md), [Composable Primitives](../ai-primitives/2026-02-20-composable-primitives.md), [Handoffs](../handoffs/README.md).

---

_This document is a living research foundation. Update as implementation begins._
