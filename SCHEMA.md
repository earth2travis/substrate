# Ansible Schema

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