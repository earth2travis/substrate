---
title: ClawVault Deep Dive Research
tags:
  - research
  - infrastructure
related:
  - [[2026-02-10-ai-career-convergence]]
  - [[actual-occasions]]
  - [[ai-sdk-research]]
  - [[alfred-north-whitehead]]
source: research/raw/clawvault-deep-dive.md
---

# ClawVault Deep Dive Research

**Date:** 2026-02-16
**Issue:** #217
**Status:** Verified, Real, Worth Studying

---

## Verification Results

### GitHub Repository ✅

- **URL:** https://github.com/Versatly/clawvault
- **Stars:** 173
- **Forks:** 13
- **Created:** 2026-01-30
- **Language:** TypeScript
- **License:** MIT
- **Active:** Yes (updated within 24 hours)

### npm Package ✅

- **Name:** clawvault
- **Version:** 2.6.0
- **Maintainer:** g9pedro (pedeluccasobral@gmail.com)
- **Keywords:** ai-agent, memory, knowledge-graph, obsidian, openclaw

### LoCoMo Benchmark ✅

- **Source:** Snap Research
- **Paper:** arxiv.org/abs/2402.17753 (Feb 2024)
- **Website:** snap-research.github.io/locomo/
- **Purpose:** Evaluates long-term conversational memory in LLMs
- **Follow-up:** LoCoMo-Plus (arxiv 2602.10715, Feb 2026)

---

## Architecture Analysis

### Memory Model

ClawVault uses a **typed document model** with these categories:

| Category    | Purpose                        |
| ----------- | ------------------------------ |
| decisions   | Choices made, with reasoning   |
| preferences | Likes, dislikes, defaults      |
| rules       | Constraints, guidelines        |
| patterns    | Recurring behaviors            |
| people      | Relationships, contacts        |
| projects    | Work contexts                  |
| goals       | Objectives, targets            |
| lessons     | What was learned from mistakes |
| commitments | Promises, deadlines            |
| handoffs    | Session transitions            |
| tasks       | Active work items              |
| backlog     | Future work                    |
| research    | Investigation topics           |
| transcripts | Conversation logs              |

### Document Structure

Each document is a markdown file with YAML frontmatter:

```yaml
---
title: "Decision Title"
date: 2026-02-16
category: decisions
memoryType: decision
priority: 🔴
tags: [architecture, backend]
related: [[other-doc]]
---
Content body with [[wiki-links]] and #tags.
```

### Observation Format

ClawVault parses observations with scored metadata:

```
[decision|c=0.9|i=0.8] Chose PostgreSQL for data layer
```

Where:

- `c` = confidence (0-1)
- `i` = importance (0-1)

Or legacy emoji format:

- 🔴 = Critical (c=0.9, i=0.9)
- 🟡 = Notable (c=0.8, i=0.6)
- 🟢 = Background (c=0.7, i=0.2)

### Type Inference

Types are inferred via regex patterns:

| Pattern                             | Inferred Type |
| ----------------------------------- | ------------- |
| "decided", "chose", "selected"      | decision      |
| "prefer", "likes", "default to"     | preference    |
| "committed", "promised", "deadline" | commitment    |
| "todo:", "need to", "don't forget"  | todo          |
| "learned", "lesson", "never again"  | lesson        |
| "talked to", "met with", "client"   | relationship  |
| "project", "feature", "repo"        | project       |
| "released", "shipped", "launched"   | milestone     |

### Knowledge Graph

Documents are linked via:

1. **Wiki-links:** `[[document-id]]` extracted with regex
2. **Tags:** `#tag-name` extracted from content
3. **Frontmatter relations:** `related`, `depends_on`, `blocked_by`, `owner`, `project`

Graph is stored in `.clawvault/graph-index.json` with:

- Nodes: id, title, type, category, path, tags, degree
- Edges: source, target, type (wiki_link, tag, frontmatter_relation)

### Context Profiles

Different tasks load different memory subsets:

| Profile  | Triggered By                         | Priority               |
| -------- | ------------------------------------ | ---------------------- |
| default  | General tasks                        | Balanced               |
| planning | "design", "architecture", "proposal" | Decisions, patterns    |
| incident | "outage", "broken", "urgent"         | Lessons, recent        |
| handoff  | "resume", "continue", "where was I"  | Handoffs, last session |

### Session Lifecycle

```bash
clawvault wake          # Start session, load context
clawvault checkpoint    # Save progress mid-session
clawvault sleep "summary" --next "next steps"  # End session
```

### [[OpenClaw]] Integration

ClawVault has explicit [[OpenClaw]] hook integration:

```bash
openclaw hooks install clawvault
openclaw hooks enable clawvault
```

This bridges ClawVault's memory with [[OpenClaw]]'s agent lifecycle.

---

## Key Insights

### 1. File-Based Beats Database

Their benchmark finding (68.5% specialized tools vs 74.0% markdown files) suggests:

- LLMs are trained on text, not database schemas
- Grep/search over files is surprisingly effective
- Complexity isn't always better

### 2. Type Inference Is Critical

Don't ask users to classify memories. Infer from content using patterns. This reduces friction and improves consistency.

### 3. Budget-Aware Injection

Context windows are finite. Load high-priority (🔴) first, then fill remaining budget with lower priority. Never truncate critical memories.

### 4. Graph Emerges from Links

Don't force users to build a graph. Extract wiki-links from natural writing. The graph emerges organically.

### 5. Obsidian Compatibility = Human Inspectability

When agent memory IS Obsidian vault, humans can browse, audit, and edit it. Transparency isn't a feature; it's the point.

---

## Patterns to Adopt for [[Sivart]]

### Immediate (Low Effort)

1. ✅ **Memory type taxonomy** (already done in MEMORY.md)
2. ✅ **Priority tags** (already done: 🔴/🟡/🟢)
3. **Wiki-links in MEMORY.md** for cross-references
4. **Frontmatter in daily notes** for metadata

### Medium Term

5. **Type inference** in daily note writing (auto-classify as decision/lesson/etc.)
6. **Context profiles** for different task types
7. **Session lifecycle** commands (wake/checkpoint/sleep equivalent)

### Longer Term (If Needed)

8. **Install ClawVault** for formal memory management
9. **[[OpenClaw]] hooks** integration
10. **Graph visualization** in Obsidian

---

## Comparison: ClawVault vs Our Current Approach

| Aspect     | ClawVault                | [[Sivart]] Current      |
| ---------- | ------------------------ | ----------------------- |
| Storage    | Typed markdown files     | MEMORY.md + daily notes |
| Categories | 17 predefined            | 8 sections in MEMORY.md |
| Linking    | Wiki-links + frontmatter | Manual references       |
| Search     | qmd + vector search      | memory_search tool      |
| Priority   | Confidence × Importance  | 🔴/🟡/🟢 tags           |
| Graph      | Auto-built from links    | None                    |
| Session    | wake/checkpoint/sleep    | HEARTBEAT.md + handoffs |
| Obsidian   | Native compatible        | Compatible but not used |

**Assessment:** ClawVault is more sophisticated, but our current approach covers 80% of the value with 20% of the complexity. Worth monitoring but not urgent to adopt.

---

## Open Questions

1. How does ClawVault handle compaction/context overflow?
2. What's the actual LoCoMo benchmark methodology?
3. How does qmd (their query tool) compare to our memory_search?
4. Is their [[OpenClaw]] integration compatible with our version?

---

## References

- GitHub: https://github.com/Versatly/clawvault
- npm: https://www.npmjs.com/package/clawvault
- LoCoMo paper: https://arxiv.org/abs/2402.17753
- LoCoMo site: https://snap-research.github.io/locomo/
- Obsidian: https://obsidian.md
