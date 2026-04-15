---
title: Obsidian
created: 2026-04-08
updated: 2026-04-08
type: entity
tags: [tools, research, memory]
sources: [raw/articles/karpathy-llm-wiki-pattern.md]
---

# Obsidian

> Markdown-based note-taking application with local-first storage, wikilinks, graph view, and plugin ecosystem.

## What It Is

Local-first markdown note-taking app. Each vault is a directory of `.md` files, making it ideal for LLM-maintained wikis since there's no proprietary format or database.

## Key Features for Wiki Use

- **Wikilinks** -- `page name` syntax for linking between notes. Renders as clickable links in the app.
- **Graph View** -- Visual representation of how notes connect. Shows hubs, orphans, and the overall shape of the knowledge base.
- **YAML Frontmatter** -- Pages can have metadata tags that plugins like Dataview can query.
- **Local Storage** -- Files are plain markdown. The LLM can read, write, and modify them directly.
- **Plugin Ecosystem** -- Extensible with community plugins.

## Relevant Plugins

- **Dataview** -- Runs queries over page frontmatter. Generates dynamic tables, lists, and summaries.
- **Obsidian Web Clipper** -- Browser extension that converts web articles to markdown.
- **Marp** -- Markdown-based slide deck generator.

## For Agents Running Headless

This is a local-first wiki -- no remote database. The agent can read/write files directly via `read_file` and `write_file` calls.

## Obsidian as IDE for Wikis

Karpathy's framing: "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase." The user browses, follows links, checks graph view. The LLM makes edits.

## Related
- [[llm-wiki-pattern]] -- Primary wiki browsing tool

## Sources
- [Karpathy's LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
