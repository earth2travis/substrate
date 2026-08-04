# Substrate Schema

## Inventory
- research/raw/ — 403 immutable source files.
- research/findings/ — 397 synthesized findings.
- insights/concepts/ — 91 durable concepts.
- insights/entities/ — 2 biographical entities.
- decisions/ — 1 ADR.
- guides/ — 2 field manuals.

## Frontmatter Requirements
Every knowledge file (research, insights, decisions) must include:
- `title:` (string)
- `tags:` (list of strings)
- `related:` (list of wikilinks to peer pages)
- `source:` (URL or path to `research/raw/`)

## Naming Conventions
- **Files:** kebab-case, lowercase. Date-prefixed for chronological content.
- **Folders:** lowercase, plural.
- **Wikilinks:** Use `[[wikilinks]]` for all internal references. Minimum two outbound links per page.

## Tag Taxonomy
- Use broad, stable tags for high-level categorization.
- Avoid synonyms; pick one standard tag per concept.

## Lint Exemptions

The following are intentional and should not be treated as errors:

1. **`duplicate-title` across layers** — `insights/`, `research/findings/`, and `research/raw/` files may share the same title. Findings inherit titles from raw sources; insights inherit from findings. The linter only flags duplicates **within** the same directory.

2. **Root files without frontmatter** — `SCHEMA.md`, `INDEX.md`, `log.md`, and `CONTRIBUTING.md` at the repo root follow different conventions and do not require YAML frontmatter.

3. **Root file naming** — Root files (e.g., `SCHEMA.md`, `INDEX.md`) are exempt from `naming-convention` kebab-case enforcement.

4. **`specs/` `fm-related-missing`** — Specification documents in `specs/` are design documents, not knowledge graph pages. They do not require `related:` links. The linter still reports them as warnings for visibility but they are not treated as blockers.

5. **`research/raw/` `fm-title-missing`** — Raw files are immutable sources. The linter extracts titles from H1 headings. These are reported as WARNING (not ERROR) since raw files are source material, not synthesized output.

6. **`research/raw/` `broken-wikilink` as INFO** — Raw files may reference concepts not yet in Substrate. These are forward references, not errors.
