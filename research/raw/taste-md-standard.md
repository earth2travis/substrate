# TASTE.md Standardization

## Standard Format

Every TASTE.md file follows this structure:

1. **Header:** `# [Agent Name] - [Role] Instincts` (e.g., `# Scout - Research Instincts`)
2. **What Good [X] Looks Like:** One or two paragraphs defining quality for this role, including the contrast between good and bad output.
3. **The Instinct:** Core instincts as a H2 section. Each instinct is a bolded principle followed by a paragraph of explanation in full sentences. Taste is described in prose, not bullet points.
4. **What Taste Avoids:** Anti-patterns specific to this role. Things that are technically acceptable but tonally wrong. Not violations of CONTRACT.md standards, but violations of instinct. Listed as bullet points with bolded categories and explanations.
5. **When to Question the Instinct:** Explicit guidance on when breaking the instinct is the right call. Includes the universal "if you find yourself breaking the instinct more than following it, the instinct is wrong and should be rewritten" clause.

## Why This Format

The four-section structure maps to how an agent uses the file:

- **What Good Looks Like:** Orienting statement. Tells the agent what quality feels like before the details.
- **The Instinct:** The actual taste. Written in prose because taste is described, not enumerated. Each principle is a paragraph so the agent understands the reasoning, not just the rule.
- **What Taste Avoids:** Negative space. What the agent should recognize and reject. These are patterns that pass a correctness check but fail a quality check.
- **When to Question the Instinct:** Escape valve. Taste is a compass, not a map. There are legitimate cases where the instinct conflicts with constraints, direction, or context. Naming them prevents the agent from either rigidly following the instinct when it produces bad outcomes or ignoring it when it should not.

## TASTE.md vs Other Context Stack Files

**TASTE.md vs VALUES.md:** Values are principles you can rank. Taste is instinct you can only recognize. Values answer "what do I optimize for when things conflict?" Taste answers "what feels right before I can explain why?"

**TASTE.md vs DESIGN.md:** DESIGN.md is the system. TASTE.md is the judgment that shaped the system. DESIGN.md says "use 16px body font." TASTE.md says "typography should feel intentional, not decorative." DESIGN.md is the recipe. TASTE.md is the chef's palate.

**TASTE.md vs CONTRACT.md:** CONTRACT.md has teeth. It defines what must never happen. TASTE.md has no teeth. It defines what should not happen but might be acceptable in context. Breaking a contract is a breach. Breaking taste is a miss.

## Template

The fillable template is at `agents/templates/TASTE.md`. It contains the exact structure with bracketed placeholders explaining what to write in each section.

## Process for Writing TASTE.md

Writing TASTE.md is the hardest of the four Context Stack files because it requires articulating what you normally just feel. The process:

1. **Start with examples.** Collect five pieces of work that feel right for the role and five that feel wrong. Read them. Extract what makes the difference.
2. **Write the Instinct section first.** The positive instincts are easier to name than the anti-patterns. Write what you look for in good work.
3. **Write What Taste Avoids second.** The anti-patterns emerge from the instincts. If an instinct says "value simplicity," the avoidance section says "avoid cleverness for its own sake."
4. **Write What Good Looks Like last.** The orienting paragraph synthesizes the instincts into a coherent picture. It is easier to write after the details are on the page.
5. **Write When to Question the Instinct last.** The exceptions are rare. Name them honestly. If none come to mind, include the default four.
6. **Review for consistency.** Does the TASTE.md contradict the CONTRACT.md? Does it align with the AGENTS.md? If there is a conflict, resolve it. Taste must not fight the contract.

## Application

All five sub-agents now have TASTE.md files in the standardized format:

- `agents/scout/TASTE.md` - Research instincts: depth over breadth, primary sources first, stop at diminishing returns
- `agents/scribe/TASTE.md` - Writing instincts: rhythm, active voice, concrete over abstract, cut the hedges
- `agents/forge/TASTE.md` - Code style instincts: simplicity over cleverness, one job per function, early returns
- `agents/inspector/TASTE.md` - Code quality instincts: tests are evidence, naming describes intent, automation beats manual review
- `agents/ops/TASTE.md` - Infrastructure instincts: redundancy where it matters, monitoring before incidents, simple is reliable
