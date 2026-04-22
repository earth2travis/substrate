---
title: "The Substrate Spec"
date: 2026-04-22
status: "review"
version: "2.0"
---

# The Substrate Spec

A version-controlled shared knowledge graph for the Agent Factory (Zookooree). The Substrate is the nervous system between agents (Koda, Sivart) and Travis (Ξ2T).

## 1. Philosophy

**The Substrate is institutional memory you can diff.**

Every decision, research finding, and architectural choice is tracked in git. Nothing lives in a message log or an agent's context window. The Substrate is the ground truth.

### 1.1 Design Principles

- **Raw is immutable.** Sources in `research/raw/` are never edited. Errors are documented in findings, not patched.
- **Knowledge compounds.** Findings link to findings. Insights emerge from cross-references. The system gets smarter as it grows.
- **Specs before scripts.** No script is written without a spec defining its inputs, outputs, and behavior first.
- **Lint early, lint often.** Structural problems compound. Consistency is enforced automatically.
- **Measure comprehension.** A knowledge system is useless if agents can't extract correct answers from it. Query evaluation proves the system works.
- **Continuous improvement.** Weekly retrospectives analyze the Substrate's own health. Gaps drive the next iteration.

### 1.2 The Karpathy Pattern

The Substrate follows the LLM Wiki pattern: raw sources flow through a pipeline into structured knowledge. But whereas the LLM Wiki is a public knowledge base about AI broadly, the Substrate is the Agent Factory's **private nervous system** — about who we are, what we're building, and what we've learned.

---

## 2. Architecture

### 2.1 Filesystem Structure

```
substrate/
├── INDEX.md                    # Entry point, navigation
├── SCHEMA.md                   # Frontmatter requirements and naming conventions
├── CONTRIBUTING.md             # Workflow rules for agents and humans
├── decisions/                  # Architecture Decision Records
├── guides/                     # How-to procedures
├── evals/                      # Query/eval script output
├── retros/                     # Weekly retrospective output
├── insights/                   # Compiled, cross-referenced knowledge
│   ├── comparisons/            # Head-to-head analysis
│   ├── concepts/               # Unified concepts and frameworks
│   └── entities/               # People, orgs, systems
├── skills/                     # Shared agent capabilities (future)
├── research/
│   ├── raw/                    # Immutable source material
│   ├── findings/               # Normalized, tagged, cross-referenced findings
│   └── queries/                # Stored query definitions
├── scripts/
│   ├── _ingest.py            # Ingest pipeline
│   ├── _lint.py              # Linter
│   ├── _scan.py              # Security scanner
│   ├── _query.py             # Stored query engine (on-demand Q&A)
│   ├── _eval.py              # Context evaluation engine (system health test)
│   └── _retro.sh             # Weekly retrospective generator
├── specs/
    ├── substrate-spec.md           # This document (Constitution — the "What")
    ├── cloudflare-spec.md                  # Cloud Architecture (Blueprint — the "How")
    ├── ingest-spec.md              # _ingest.py behavior and pipeline
    ├── lint-spec.md                # _lint.py rules and auto-fix
    ├── query-spec.md               # _query.py format and categories
    ├── eval-spec.md                # _eval.py scoring and execution
    └── scan-spec.md                # _scan.py security checks
```

### 2.2 Directory Contract

Each directory has a single responsibility. Scripts only write to their designated outputs. No script reads or modifies files outside its contract.

| Directory | Written by | Read by | Mutation policy |
|---|---|---|---|
| `research/raw/` | Agents, humans (manual placement) | `_ingest.py`, `_lint.py` | Append-only, immutable after write |
| `research/findings/` | `_ingest.py` | `_ingest.py`, `_lint.py` | Fully regenerated on each ingest run |
| `research/queries/` | Humans, agents | `_query.py` | Append/edit manually |
| `insights/concepts/` | `_ingest.py` (auto), agents (manual) | Humans, agents | Stable once promoted; not overwritten by ingest |
| `insights/entities/` | `_ingest.py` (auto), agents (manual) | Humans, agents | Stable once promoted |
| `insights/comparisons/` | Agents (manual) | Humans, agents | Append/edit manually |
| `decisions/` | Humans, agents | Humans, agents | Append-only; deprecated entries marked, not deleted |
| `guides/` | Humans, agents | Humans, agents | Append/edit manually |
| `evals/` | `_eval.py` | Humans, agents | Overwritten each eval run |
| `retros/` | `_retro.sh` | Humans, agents | Append-only, immutable once written |
| `skills/` | Humans, agents | Agent skill systems | Append/edit manually |
| `specs/` | Humans, agents | Humans, agents | Append/edit manually |

### 2.3 What Each Directory Is NOT

- **raw/** is not for agent output, session logs, or generated content. Only sources you want to ingest.
- **findings/** is not a permanent directory — it's a staging area. Findings exist to be promoted to insights or consumed by the query engine.
- **insights/** is not a dumping ground. Every insight must earn its place by referencing multiple sources.
- **decisions/** is not a TODO list or issue tracker. It records decisions that have been made, not options under consideration.
- **guides/** is not conceptual documentation. It's procedural content — steps to follow.
- **evals/** is not for benchmarks or ground truth questions. It's output from evaluation runs only. Ground truth questions live in `research/queries/`.
- **retros/** is not a daily log. It's a weekly analysis of system health.
- **skills/** is not for scripts. It's for skill definitions that agents load into context.

---

## 3. The Pipeline

### 3.1 Overview

```
Capture → Process → Synthesize → Evaluate → Reflect
raw/   → findings/ → insights/ → evals/   → retros/
```

Three agents participate in the pipeline:

| Agent | Role |
|---|---|
| **Sivart** | Research ingestion — finds sources, places raw files, reviews insights |
| **Koda** | System engineering — writes scripts, maintains pipeline, enforces quality |
| **Travis** | System architecture — approves specs, makes decisions, reviews output |

### 3.2 Stage 1: Capture

Raw sources are placed in `research/raw/`. Sources can be:

- Transcripts from conversations or sessions
- Scraped articles, blog posts, documentation
- Research notes, meeting notes, observations
- Papers, whitepapers, technical analyses

Each raw file should have frontmatter if possible. If not, the ingest pipeline infers it.

Raw files are **immutable**. Once placed, they are not modified. If a source has errors, those errors are documented in a finding, not patched in the raw file. If a source is deprecated, it's moved to a `quarantine/` directory, not deleted (preserves git history).

### 3.3 Stage 2: Process

`_ingest.py` normalizes each raw file into a finding:

1. Parse existing frontmatter or infer from content
2. Extract or generate a title (from H1, frontmatter, or filename)
3. Derive tags using strict phrase matching — no single-word keywords
4. Discover cross-references via wikilink extraction and title mention frequency
5. Write normalized finding to `research/findings/`
6. Promote to `insights/` if the topic appears in 2+ findings
7. Clean up orphan findings whose raw source was deleted

The pipeline runs daily on cron (02:30 UTC). See `specs/ingest-spec.md` for the full specification.

### 3.4 Stage 3: Synthesize

When a concept, entity, or pattern appears across multiple findings, it becomes a candidate for promotion to `insights/`:

- **concepts/** — Ideas, frameworks, patterns that span multiple sources
- **entities/** — People, organizations, systems that are referenced across findings
- **comparisons/** — Head-to-head analyses comparing alternatives

Some promotions are automated (high cross-reference density). Others require manual synthesis by an agent because the insight needs judgment to construct. Auto-promoted insights use the body from the most representative finding, enriched with cross-references.

Promoted insights are stable. They are not overwritten by subsequent ingest runs.

### 3.5 Stage 4: Evaluate

`_eval.py` tests whether the Substrate actually works as a knowledge system. It loads eval questions from `research/queries/` (flagged `eval: true`), generates answers using only Substrate files, and scores them against human-written ground truth using the Synthesis Accuracy Score (SAS).

Eval categories match query categories, but eval questions have ground truth answers that queries don't:

- **identity** — Who/what is something?
- **state** — What changed and when? Tests temporal awareness.
- **conflict** — When sources disagree, which wins? Tests provenance handling.
- **synthesis** — Cross-domain questions requiring multiple insights.

Reports go to `evals/YYYY-MM-DD-eval.md`. See `specs/eval-spec.md`.

### 3.6 Stage 5: Reflect

Every Sunday, `_retro.sh` generates a retrospective analyzing the Substrate's health over the past week:

- File counts and changes by directory
- Tag frequency analysis
- Cross-reference density trends
- New orphans, stale content, broken links
- Patterns and themes emerging from new raw sources
- Action items: gaps to fill, scripts to update, specs to revise

Retros are append-only and immutable. They live in `retros/week-YYYY-WNN.md`.

### 3.7 Cron Schedule

| Job | Schedule | Script | Output |
|---|---|---|---|
| Lint | Daily 02:00 UTC | `_lint.py` | stdout (exit code signals pass/fail) |
| Ingest | Daily 02:30 UTC | `_ingest.py` | `research/findings/` + structured log |
| Security scan | Daily 03:00 UTC | `_scan.py` | stdout (exit code signals pass/fail) |
| Eval | Sun 04:00 UTC | `_eval.py` | `evals/YYYY-MM-DD-eval.md` |
| Retro generation | Sun 05:00 UTC | `_retro.sh` | `retros/week-YYYY-WNN.md` |

---

## 4. Content Standards

### 4.1 Naming Conventions

- **Files:** kebab-case, lowercase. `my-topic.md`. Never `My_Topic.md` or `my topic.md`.
- **Folders:** lowercase, plural. `insights/` not `Insight/`.
- **Dates:** YYYY-MM-DD in filenames and frontmatter. `week-2026-W17.md`.
- **Wikilinks:** `[[wikilinks]]` for all internal references. Minimum 2 outbound per page.
- **Tags:** Broad, stable, no synonyms. One standard tag per concept.

### 4.2 Frontmatter Requirements

Every knowledge file (raw, finding, insight, decision, guide, query) MUST have YAML frontmatter:

```yaml
---
title: "Human-readable title"
date: 2026-04-22
tags: [tag-one, tag-two]
related: [["wikilink-one"], ["wikilink-two"]]
source: "URL or research/raw/filename.md"
```

Fields:

- `title` (required) — Human-readable. If not provided, inferred from first H1 or filename.
- `tags` (required) — List of broad, stable tags. Derived by phrase matching if not provided.
- `related` (required for insights, decisions, guides) — Minimum 2 wikilinks. Auto-generated for findings.
- `source` (required) — Original URL or path to raw file. For insights, the finding or raw that promoted.
- `date` (required) — Creation date.

Additional fields by type:

- Decisions: `status: accepted|deprecated|superseded`, `supersedes: "..."`
- Queries: `category: identity|conflict-resolution|temporal-awareness|synthesis`, `last_run`, `score`
- Guides: `category: setup|workflow|troubleshooting`

### 4.3 Body Structure

- Every file must have a top-level H1 matching the frontmatter title.
- Paragraphs should be short (3-5 sentences max).
- Use wikilinks (`[[target]]`) for internal references.
- Use standard markdown for formatting (headings, lists, code blocks).
- No raw HTML in knowledge files. HTML scrapes are flagged by the linter.

---

## 5. Governance

### 5.1 Change Management

All changes to the Substrate go through git:

- **Commits:** Every change is a commit with a meaningful message.
- **PRs:** Merged changes require a pull request (no direct pushes to `main`).
- **Review:** Content is peer-reviewed. System changes are reviewed by Travis.

### 5.2 Agent Roles and Permissions

| Agent | Can write | Can review | Can merge |
|---|---|---|---|
| Sivart | `research/raw/`, `insights/`, `decisions/`, `guides/` | Content in all directories | With approval |
| Koda | `scripts/`, `specs/`, `SCHEMA.md` | Content + system changes | With approval |
| Travis | Anywhere | Anywhere | Yes (final authority) |

### 5.3 Conflict Resolution

When two sources disagree:

1. **Recency:** Newer sources take precedence, unless the older source is marked as authoritative.
2. **Attribution:** Sources with named authors (vs. scraped content) are more authoritative.
3. **Consensus:** If 3+ independent sources agree, they outweigh a single contradictory source.
4. **Explicit override:** A decision record can designate one source as authoritative regardless of the above.

Conflicts should be documented in insights or decision records, not silently resolved.

### 5.4 Entity Resolution

The Substrate maintains a persistent **Entity Map** to resolve aliases and unify identities across fragmented sources (e.g., "Ξ2T," "earth2travis," and "Travis" are the same entity).

- **The Map:** `insights/entities/entity-map.json` serves as the ground truth for all entity aliases.
- **Ingestion:** The `_ingest.py` pipeline uses this map to tag findings with canonical entity IDs.
- **Querying:** The `_query.py` engine expands entity searches to include all known aliases to ensure comprehensive retrieval.

### 5.5 Deprecation

Nothing is deleted from the Substrate. Content is deprecated:

- Decisions are marked `superseded` with a link to the new decision.
- Insights are marked `deprecated` with explanation and moved to an `archive/` subdirectory.
- Raw sources that are deprecated are moved to `quarantine/` (preserves git history).

---

## 6. Script Specifications

Each system script has its own spec defining inputs, outputs, behavior, and integration:

- **[ingest-spec.md](ingest-spec.md)** — `_ingest.py`: pipeline behavior, tagging, promotion, logging
- **[lint-spec.md](lint-spec.md)** — `_lint.py`: rules, severity levels, auto-fix, usage
- **[query-spec.md](query-spec.md)** — `_query.py`: stored Q&A interface, query format, categories, on-demand answers
- **[eval-spec.md](eval-spec.md)** — `_eval.py`: context evaluation engine, SAS metric, system health testing
- **[scan-spec.md](scan-spec.md)** — `_scan.py`: checks, secret patterns, integration

## 6.5 Infrastructure

The Factory Architecture Spec defines the cloud infrastructure that runs the Substrate:

- **[cloudflare-spec.md](cloudflare-spec.md)** — Cloudflare-first stack: Artifacts (memory), Workers + AI Gateway (engine), Email (transport), GitHub (interface)

When building scripts or planning infrastructure, reference the Factory Architecture spec. When organizing knowledge or defining content standards, reference the Substrate spec.

---

## 7. The Continuous Improvement Loop

```
        ┌─────────────────────────────────────┐
        │                                     ▼
Ingest → Lint → Process → Synthesize → Evaluate
  │                                   │        │
  │                                   ▼        │
  │                                Reflect ◄───┘
  │                                   │
  └──────── actions ──────────────────►│
                                       ▼
                              Update scripts, specs,
                              promote insights, fill gaps
```

The loop is driven by weekly retrospectives. Each retro identifies:

1. **Structural gaps** — Files without frontmatter, broken links, orphans
2. **Knowledge gaps** — Topics with raw sources but no insights
3. **Coverage gaps** — Query categories with low scores
4. **Process gaps** — Scripts that need features, rules that need refinement

Actions from retros are tracked as commits. The Substrate improves itself.

---

## 8. Decisions Registry

| # | Decision | Date | Status | Summary |
|---|---|---|---|---|
| 001 | Rename brain-two → substrate | 2026-04-22 | accepted | Repo is github.com/earth2travis/substrate |
| 002 | Eliminate daily/ and meta/ | 2026-04-14 | accepted | Context pollution; moved to messaging and redistributing |
| 003 | Eliminate synthesis/ and operations/ | 2026-04-22 | accepted | No additional value; simplify structure |
| 004 | Keep skills/ intentionally empty | 2026-04-22 | accepted | Build capabilities when foundation is stable |
| 005 | Write specs before scripts | 2026-04-22 | accepted | Align on behavior before coding |
| 006 | Weekly retrospectives | 2026-04-22 | accepted | Data for continuous improvement loop |
| 007 | Add retros/ at root | 2026-04-22 | accepted | First-class artifact parallel to evals/ |
| 008 | Split specs into individual files | 2026-04-22 | accepted | Master spec defines system, script specs define behavior |
| 009 | Master spec is comprehensive | 2026-04-22 | accepted | System philosophy, architecture, governance, pipeline all in one doc |

---

## 9. Open Questions

1. Should the ingest pipeline process non-markdown sources (PDFs, images with OCR)?
2. What's the threshold for auto-promoting insights vs. requiring manual review?
3. Should security scan integrate with GitHub's secret scanning API?
4. How should the Substrate handle conflicting information from two authoritative sources?
5. What's the retention policy for raw sources? Infinite, or archive after N days?
6. Should the Substrate support multiple languages, or English-only for now?
7. How do we handle real-time data (APIs, live status) vs. point-in-time snapshots?
