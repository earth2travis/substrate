# LLM Wiki Master Guide: Karpathy's Pattern, Implementations, Best Practices & Agent Instructions

**Version**: April 2026 (post-Karpathy viral wave)
**Purpose**: This single Markdown file is designed to be dropped into any LLM coding agent (Claude Code, Cursor, Hermes-Agent, etc.) as a **system prompt / reference doc**. It compiles *everything* from Karpathy's original Gist + the explosion of community implementations, tools, and best practices. Use it to bootstrap, maintain, or evolve your own LLM Wiki.

---

## 1. Core Idea (Karpathy's Original Vision)

The LLM Wiki is **not** another RAG system.
It is a **persistent, compiled knowledge artifact** that sits between your raw sources and your queries.

- **Philosophy** (direct from Karpathy):
  - Treat your knowledge base like source code -> the LLM is the compiler.
  - Raw files stay immutable.
  - The LLM actively **summarizes, synthesizes, interlinks, and maintains** a clean `wiki/` layer.
  - Result: faster queries, inspectable memory, zero hallucinations from stale chunks, and a living "personal Wikipedia" you own forever (plain Markdown + Git).

**Key insight**: At personal scale (~400 k tokens / hundreds of articles), you often need **no vector DB** -- just smart indexing + LLM bookkeeping.

---

## 2. Canonical Folder Structure

```
your-wiki-vault/
├── raw/                  # Immutable originals (PDFs, articles, notes, web clips, images)
│   ├── 2026-04-01_source-title.md
│   └── ...
├── wiki/                 # LLM-generated, human-editable Markdown pages
│   ├── index.md          # Master catalog + concept map
│   ├── log.md            # Chronological ingest & update history
│   ├── entities/
│   ├── concepts/
│   ├── people/
│   └── ...               # Any taxonomy you want
├── CLAUDE.md             # (or AGENT.md) - schema, rules, and agent instructions
├── .gitignore
└── obsidian/             # Optional: plugins, graph settings
```

Obsidian/Logseq recommended as the "IDE" -- use graph view, backlinks, and daily notes.

---

## 3. Core Agent Operations (the three commands every implementation must support)

1. **Ingest** (add new source)
   - Drop file/URL into `raw/`
   - LLM:
     - Summarizes into new or updated `wiki/` pages
     - Creates/updates backlinks
     - Appends to `log.md`
     - Refreshes `index.md`
   - Can affect 2-5 existing pages (consolidation)

2. **Query**
   - Ask against `wiki/` only (not raw)
   - Agent returns synthesized answer + inline citations to specific Markdown files

3. **Lint / Health Check**
   - Monthly or on-demand
   - Fixes orphans, broken links, stale facts, duplicates, confidence decay
   - Suggests new pages or merges

---

## 4. Best Practices (v1 -> v2 Evolution)

### From Karpathy + Farzapedia (baseline)
- Keep everything in plain Markdown + Git (portable, versioned, "file over app").
- One source of truth per fact; use `[[backlinks]]` heavily.
- Agent must be able to read/write the entire vault in one context window when possible.
- Start small: 10-20 sources -> grow organically.

### Advanced / v2 Practices (rohitg00 + community consensus)
- **Memory Lifecycle**:
  - Every fact gets a **confidence score** (0-1) and **last-updated** timestamp.
  - **Supersession**: Newer/better sources automatically deprecate old ones.
  - **Retention curves** + **forgetting** for low-confidence or outdated info.
  - **Consolidation tiers**: atomic facts -> synthesized concepts -> high-level narratives.
- **Typed Knowledge Graph**:
  - Entities + typed relationships (e.g., `PERSON -> founded -> COMPANY`).
  - Graph traversal during queries.
- **Hybrid Search** (when vault grows):
  - BM25 on filenames + titles + graph + optional local embeddings.
- **Event Hooks & Self-Healing**:
  - Auto-ingest on file drop (via Claude Code / Cursor watchers).
  - Periodic lint cron.
  - Audit trail in `log.md`.
- **Token Efficiency**:
  - Graphify-style claims: **71.5x fewer tokens** vs raw RAG.
  - L1/L2 caching layers (MehmetGoekce implementation).
- **Multi-Agent & Privacy**:
  - Separate "research agent" vs "personal memory agent".
  - Local-only options (no cloud LLM required after initial setup).

### Gotchas & Anti-Patterns
- Never query raw files directly after the first ingest.
- Avoid over-fragmentation (too many tiny pages).
- Hallucination compounding: always cite the exact `wiki/` file.
- Scale ceiling: when >10k pages, add hybrid vector search (but keep Markdown as source of truth).

---

## 5. Major Implementations (what's possible today)

| Implementation | Type | Standout Features | Best For | Link / How to Start |
|----------------|------|-------------------|----------|---------------------|
| **Karpathy Original Gist** | Manual pattern | Pure Markdown, copy-paste agent prompt | Understanding the idea | Karpathy's Gist (feed directly to Claude Code) |
| **God of Prompt Guide** | Prompt library | Full ingest/query/lint prompts + gotchas | Beginners who want full control | Copy-paste guide (viral X post) |
| **Farzapedia (Farza)** | Personal showcase | 400+ interlinked pages from diaries/iMessages | Real-world proof | Karpathy amplified this first |
| **Graphify** | CLI tool | `pip install graphify && graphify install` -> one-command vault from any folder (code + PDFs + images) | Fastest zero-to-wiki | `github.com/safishamsi/graphify` |
| **Hermes-Agent Skill** | Built-in agent skill | `/llm-wiki <topic>` or `hermes update` -- auto web + code research | Research agents | Nous Research Hermes-Agent |
| **lucasastorian/llmwiki** | Full web app | Upload -> Claude -> hosted demo at llmwiki.app | Non-technical users | llmwiki.app |
| **Astro-Han/karpathy-llm-wiki** | Claude Code skill | `npx add-skill Astro-Han/karpathy-llm-wiki` | Existing Claude workflows | GitHub skill |
| **MehmetGoekce/llm-wiki** | Two-layer cache | L1/L2 + Obsidian + Logseq support | Performance-focused | GitHub |
| **yologdev/karpathy-llm-wiki** | Autonomous repo | "yoyo" agent auto-grows the repo every few hours | Hands-off experimentation | GitHub |
| **rohitg00 LLM Wiki v2** | Extended pattern | Full memory lifecycle + typed graph + self-healing | Long-term production use | Gist extension |
| **atomicmemory/llm-wiki-compiler** | Compiler-focused | Pure "compilation" mode | Advanced users | GitHub |

**Community variants**: blink-query, sage-wiki, quicky-wiki, PhD research vaults, codebase wikis, business-intel vaults, local-LLM versions (Gemma, etc.).

---

## 6. Ready-to-Use Agent Prompt (copy this into CLAUDE.md or your agent)

```markdown
You are the LLM Wiki Agent for this vault.

Rules (never break):
- Raw/ files are immutable source of truth. Never edit them.
- All new or updated knowledge lives in wiki/ as clean Markdown with [[backlinks]].
- Every page must have frontmatter: title, tags, confidence, last-updated, sources.
- Maintain index.md (catalog) and log.md (chronology) religiously.
- When ingesting: create/update 2-5 related pages; never orphan facts.
- On query: answer from wiki/ only, cite exact filenames.
- On lint: fix broken links, stale facts, low-confidence orphans.

Supported commands:
- /ingest <file-or-url>
- /query <question>
- /lint
- /graph (if graphify or typed graph enabled)

You have read the entire LLM Wiki Master Guide above. Follow all best practices, especially memory lifecycle and token efficiency.
```

---

## 7. Quick Start (5 minutes)

1. Create a new Obsidian vault.
2. Copy this entire file as LLM-Wiki-Master-Guide.md.
3. Copy the agent prompt into CLAUDE.md.
4. Drop Karpathy's original Gist + this guide into your coding LLM (Claude Code / Cursor).
5. Type: "Initialize the LLM Wiki using the Master Guide."

You now have a living, compounding knowledge base that gets smarter every time you add something.

This pattern is still evolving fast -- the community shipped production tools in <72 hours after Karpathy's post. Treat this Markdown as a living document: run /lint on it monthly.

Happy wiki-building!
