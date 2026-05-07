---
title: "Obsidian"
tags: [finding, tools, memory, knowledge-graph, markdown]
related:
- agent-memory
- context-stack
- llm-wiki-pattern
source: research/raw/obsidian.md
ingested: 2026-05-07
---
# Obsidian

Markdown-based note-taking application with local-first storage, wikilinks, graph view, and plugin ecosystem. Each vault is a directory of `.md` files, making it ideal for LLM-maintained wikis.

## Key Points

**Local-first, agent-native format.** No proprietary format or remote database. The LLM reads, writes, and modifies files directly via standard file operations. This removes the translation layer that corrupts most agent-memory integrations.

**Wikilinks and graph view.** `[[page name]]` syntax creates clickable links between notes. The graph view shows hubs, orphans, and the overall shape of the knowledge base. For agents, this is a navigable topology, not just a search index.

**YAML frontmatter and Dataview.** Pages can have structured metadata that plugins query to generate dynamic tables, lists, and summaries. This enables the wiki to be both human-readable and machine-queryable.

**The IDE metaphor.** Karpathy's framing: "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase." The human browses, follows links, checks graph view. The LLM makes edits. This separation of concerns is sustainable.

**Key plugins for agent wikis.** Dataview for metadata queries. Web Clipper for article ingestion. Marp for slide decks from wiki content.

## Relevance

Substrate is an Obsidian-compatible markdown wiki with agent-driven maintenance. The design decisions (wikilinks, frontmatter, directory structure) are directly transferrable to any Obsidian vault.

## Related

- [[agent-memory]] -- Agent memory architecture
- [[context-stack]] -- Layered agent memory system
- [[llm-wiki-pattern]] -- The wiki approach to agent knowledge
