---
title: "The Substrate Spec"
date: 2026-04-22
status: "review"
version: "2.0-rc"
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

### 1.2 Entity Resolution

A single entity may appear under many aliases across sources: a person might appear as their email, Slack handle, GitHub username, full name, initials, or internal codename. A retrieval system sees these as unrelated text strings. An understanding system **maps them to the same entity**.

Entity resolution is a core standard of the Substrate:

- **The Entity Map** — `insights/entities/entity-map.json` links all known aliases to canonical entities.
- **The Pipeline Rule** — `_ingest.py` uses the entity map to unify aliases in finding metadata.
- **The Query Expansion** — `_query.py` and `_eval.py` expand searches across all known aliases.

Without entity resolution, a question like "What did Travis say about the Cloudflare migration?" would only match one alias and miss everything else. Entity resolution is the difference between finding a file and knowing a person.

### 1.3 The Karpathy Pattern

The Substrate follows the LLM Wiki pattern: raw sources flow through a pipeline into structured knowledge. But whereas the LLM Wiki is a public knowledge base about AI broadly, the Substrate is the Agent Factory's **private nervous system** — about who we are, what we're building, and what we've learned.

### 1.4 The Moat: Accumulated Understanding

The primary value of the Substrate is not the technology that hosts it, but the accumulated synthesis it contains. Unlike static documentation, the Substrate compounds in value every day it runs.

- **Compounding Context.** Each new data point doesn't just add a fact; it refines the existing graph, resolves past conflicts, and deepens the system's intuition about our priorities.
- **The Time Barrier.** A new agent starting from zero cannot replicate the Substrate's understanding, no matter how sophisticated its model. The accumulated tenure is a proprietary asset that can only be earned through continuous operation.
- **Synthesis as Product.** The competitive advantage is the interpretive work — the resolution of conflicts, the ranking of sources, and the unification of entities — that happens before a file is ever written. Static documentation records what happened. The Substrate records what it means. The gap between those two is the moat.

---

## 2. Architecture

### 2.1 Filesystem Structure

```
substrate/
├── INDEX.md                        # Entry point, navigation for the repo
├── SCHEMA.md                       # Frontmatter requirements, naming conventions
├── CONTRIBUTING.md                 # Agent/human workflow rules
├── decisions/                      # Architecture Decision Records (ADRs)
├── guides/                         # How-to procedures and workflows
├── evals/                          # Output from query/eval scripts
├── retros/                         # Output from weekly retro script
├── insights/                       # Compiled, cross-referenced knowledge
│   ├── comparisons/                # Head-to-head analysis docs
│   ├── concepts/                   # Stable unified concepts and frameworks
│   └── entities/                   # People, orgs, systems
├── skills/                         # Protocol-Registered Resources (PRRs)
│   ├── registry.json               # Skill registry: IDs, versions, ownership
│   └── <skill-name>/               # Individual skills with contract.md
├── research/
│   ├── raw/                        # Immutable source material
│   ├── findings/                   # Normalized, tagged, cross-referenced findings
│   └── queries/                    # Stored query definitions
├── scripts/
│   ├── _ingest.py                  # Ingest pipeline
│   ├── _lint.py                    # Consistency checker
│   ├── _scan.py                    # Security scanner
│   ├── _query.py                   # Stored query engine (on-demand Q&A)
│   ├── _eval.py                    # Context evaluation engine (system health test)
│   └── _retro.sh                   # Weekly retrospective generator
└── specs/                          # System component specifications
    ├── substrate-spec.md           # This document (Constitution — the "What")
    ├── cloudflare-spec.md          # Cloud Architecture (Blueprint — the "How")
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
| `insights/entities/` | `_ingest.py` (auto), agents (manual), `Entity Map` | Humans, agents | Stable once promoted; entity map is manually curated |
| `insights/comparisons/` | Agents (manual) | Humans, agents | Append/edit manually |
| `decisions/` | Humans, agents | Humans, agents | Append-only; deprecated entries marked, not deleted |
| `guides/` | Humans, agents | Humans, agents | Append/edit manually |
| `evals/` | `_eval.py` | Humans, agents | Overwritten each eval run |
| `retros/` | `_retro.sh` | Humans, agents | Append-only, immutable once written |
| `skills/` | PRR registry (see 2.4) | Agent skill systems, `_eval.py` | Append/edit via PRR protocol |
| `specs/` | Humans, agents | Humans, agents | Append/edit manually |

### 2.3 Root Document Roles

Three documents sit at the repo root. They serve different audiences:

- **INDEX.md** — A short table of contents. Points readers at the right section of the Substrate. Think of it as a lobby — brief, navigational, no substance.
- **SCHEMA.md** — A quick-reference card for frontmatter fields and naming rules. It exists so agents can check formatting without reading the full spec. **This doc is derived from Section 4 of this spec** — when the spec changes, SCHEMA.md is updated to match. If there's a conflict, the spec wins.
- **CONTRIBUTING.md** — The workflow summary: capture, find, promote, PR. It exists so a new agent can start contributing in under 30 seconds. Like SCHEMA.md, it's derived from the governance and pipeline sections of this spec.

### 2.4 What Each Directory Is NOT

- **raw/** is not for agent output, session logs, or generated content. Only sources you want to ingest.
- **findings/** is not a permanent directory -- it's a staging area. Findings exist to be promoted to insights or consumed by the query engine.
- **insights/** is not a dumping ground. Every insight must earn its place by referencing multiple sources.
- **decisions/** is not a TODO list or issue tracker. It records decisions that have been made, not options under consideration.
- **guides/** is not conceptual documentation. It's procedural content -- steps to follow.
- **evals/** is not for benchmarks or ground truth questions. It's output from evaluation runs only. Ground truth questions live in `research/queries/`.
- **retros/** is not a daily log. It's a weekly analysis of system health.
- **skills/** is not a loose folder of static files. Each skill is a Protocol-Registered Resource (PRR).

### 2.5 Skills as Protocol-Registered Resources

Skills in the Substrate are not just instruction sets; they are **Protocol-Registered Resources (PRRs)**. Each skill is a protocol-level resource that the Autogenesis Protocol (AGP) can address, version, test, and evolve.

This extends the [agentskills.io](https://agentskills.io) standard (a folder containing a `SKILL.md` and optional scripts/assets) with a formal resource layer:

**Standard Agent Skill vs. PRR:**

| Feature | Standard Agent Skill (agentskills.io) | Protocol-Registered Resource (AGP) |
|---|---|---|
| **Discovery** | Agent scans a folder. | Registered in `registry.json` with metadata. |
| **Versioning** | Manual (usually). | Tracked via Git commits and semantic versioning. |
| **Evolution** | Human edits the `SKILL.md`. | The SEPL Loop can propose, test, and merge updates. |
| **Contract** | Natural language instructions. | A formal `contract.md` defining inputs, outputs, and failure modes. |
| **Authority** | Implicit. | Explicitly ranked in the Source Hierarchy. |

**Skill Directory Structure:**

```
skills/
├── registry.json                # Resource registry: IDs, versions, ownership
├── <skill-name>/
│   ├── SKILL.md                 # Human-readable instructions (agentskills.io standard)
│   ├── contract.md              # Machine-readable interface contract
│   ├── scripts/                 # Optional utility scripts for skill execution
│   ├── assets/                  # Optional templates, configs, reference files
│   └── tests/                   # Optional integration tests for _eval.py
```

**registry.json:**

```json
{
  "skills": {
    "skill-name": {
      "resource-id": "skill:<name>",
      "version": "1.0.0",
      "evolvable": true,
      "owner": "koda",
      "contract": "contract.md",
      "description": "Brief description of what this skill does"
    }
  }
}
```

Fields:
- `resource-id` — URI-style identifier for the AGP to address this skill.
- `version` — Semantic version. Bump on every change.
- `evolvable` — If `true`, the SEPL Loop has permission to auto-generate PRs for updates. If `false`, all changes require human approval.
- `owner` — Which agent or human is responsible for this skill.
- `contract` — Path to the `contract.md` file within the skill directory.

**contract.md:**

Defines the machine-readable interface contract for the skill:

```markdown
# Contract: <skill-name>

## Inputs
- What this skill expects as input (parameters, context, preconditions)

## Outputs
- What this skill produces (artifacts, side effects, follow-up actions)

## Failure Modes
- Known failure conditions and recovery procedures

## Evaluation Criteria
- How _eval.py tests whether an improvement to this skill is valid
```

**Source Hierarchy:**

When multiple skills conflict or overlap, the Source Hierarchy determines authority:
1. Skills with `evolvable: false` (human-locked) take precedence over evolvable skills.
2. Skills with higher version numbers take precedence within the same family.
3. The most recently tested skill (per `evals/` reports) has operational priority.

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

Raw files are **immutable**. Once placed, they are not modified. If a source has errors, those errors are documented in a finding, not patched in the raw file. If a source is deprecated, it's flagged in frontmatter to exclude it from ingest.

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
- `last_confirmed` (optional, insights/findings only) — The date the synthesized knowledge was last verified against primary sources. Used for staleness checks. Raw sources do not use this field.

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

### 5.4 Deprecation

Nothing is deleted from the Substrate. Content is deprecated:

- Decisions are marked `superseded` with a link to the new decision.
- Insights are marked `deprecated` within the body, with explanation and link to the replacement.
- Raw sources that are deprecated are flagged in their frontmatter and excluded from ingest.

---

## 6. Script Specifications

Each system script has its own spec defining inputs, outputs, behavior, and integration:

- **[ingest-spec.md](ingest-spec.md)** — `_ingest.py`: pipeline behavior, tagging, promotion, logging
- **[lint-spec.md](lint-spec.md)** — `_lint.py`: rules, severity levels, auto-fix, usage

The linter enforces all Content Standards. When it flags an issue, it can either report it (default) or fix it (`--fix` mode). Non-fixable issues require manual resolution.
- **[query-spec.md](query-spec.md)** — `_query.py`: stored Q&A interface, query format, categories, on-demand answers
- **[eval-spec.md](eval-spec.md)** — `_eval.py`: context evaluation engine, SAS metric, system health testing
- **[scan-spec.md](scan-spec.md)** — `_scan.py`: checks, secret patterns, integration

The `_retro.sh` script is exempt from the one-spec-per-script rule. The retro is a lightweight aggregation of git log, filesystem state, and ingest output. Its behavior is fully described in Section 3.6 (Reflect) above. If the retro system grows in complexity, it gets its own spec.

## 7. Infrastructure

The Factory Architecture Spec defines the cloud infrastructure that runs the Substrate:

- **[cloudflare-spec.md](cloudflare-spec.md)** — Cloudflare-first stack: Artifacts (memory), Workers + AI Gateway (engine), Email (transport), GitHub (interface)

When building scripts or planning infrastructure, reference the Factory Architecture spec. When organizing knowledge or defining content standards, reference the Substrate spec.

---

## 8. The Continuous Improvement Loop

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

## 9. Decisions Registry

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

## 10. Open Questions

1. Should the ingest pipeline process non-markdown sources (PDFs, images with OCR)?
2. What's the threshold for auto-promoting insights vs. requiring manual review?
3. Should security scan integrate with GitHub's secret scanning API?
4. How should the Substrate handle conflicting information from two authoritative sources?
5. What's the retention policy for raw sources? Infinite, or archive after N days?
6. Should the Substrate support multiple languages, or English-only for now?
7. How do we handle real-time data (APIs, live status) vs. point-in-time snapshots?
