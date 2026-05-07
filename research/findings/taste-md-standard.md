---
title: "TASTE.md: Standardizing Agent Taste Documents"
tags: [agents, taste, quality, context-stack, standards, conventions]
related:
  - [[context-stack]]
  - [[agent-identity]]
  - [[workflow-as-contract]]
  - [[agent-native-operations]]
source: research/raw/taste-md-standard.md
---

# TASTE.md: Standardizing Agent Taste Documents

## The Format

Every TASTE.md follows a four-section structure:

1. **Header:** `# [Agent Name] - [Role] Instincts`
2. **What Good [X] Looks Like:** One or two paragraphs defining quality for this role, including contrast between good and bad output.
3. **The Instinct:** Core instincts as a H2 section. Each instinct is a bolded principle followed by a paragraph of explanation in full sentences. Taste is described in prose, not bullet points.
4. **What Taste Avoids:** Anti-patterns specific to this role. Things that are technically acceptable but tonally wrong. Not violations of CONTRACT.md standards, but violations of instinct.
5. **When to Question the Instinct:** Explicit guidance on when breaking the instinct is the right call. Includes the universal clause: "if you find yourself breaking the instinct more than following it, the instinct is wrong and should be rewritten."

## Why This Format

The structure maps to how an agent uses the file:

- **What Good Looks Like:** Orienting statement. Tells the agent what quality feels like before the details.
- **The Instinct:** The actual taste. Written in prose because taste is described, not enumerated.
- **What Taste Avoids:** Negative space. Patterns that pass correctness but fail quality.
- **When to Question:** Escape valve. Taste is a compass, not a map.

## TASTE.md vs Other Context Stack Files

**TASTE.md vs VALUES.md:** Values are principles you can rank. Taste is instinct you can only recognize. Values answer "what do I optimize for when things conflict?" Taste answers "what feels right before I can explain why?"

**TASTE.md vs DESIGN.md:** DESIGN.md is the system. TASTE.md is the judgment that shaped the system. DESIGN.md says "use 16px body font." TASTE.md says "typography should feel intentional, not decorative." DESIGN.md is the recipe. TASTE.md is the chef's palate.

**TASTE.md vs CONTRACT.md:** CONTRACT.md has teeth. It defines what must never happen. TASTE.md has no teeth. It defines what should not happen but might be acceptable in context. Breaking a contract is a breach. Breaking taste is a miss.

## The Writing Process

Writing TASTE.md is the hardest of the four Context Stack files because it requires articulating what you normally just feel. The process:

1. **Start with examples.** Collect five pieces of work that feel right and five that feel wrong. Extract what makes the difference.
2. **Write the Instinct section first.** Positive instincts are easier to name than anti-patterns.
3. **Write What Taste Avoids second.** The anti-patterns emerge from the instincts.
4. **Write What Good Looks Like last.** The orienting paragraph synthesizes the instincts into a coherent picture.
5. **Write When to Question last.** The exceptions are rare. Name them honestly.
6. **Review for consistency.** Does TASTE.md contradict CONTRACT.md? Does it align with AGENTS.md? Resolve conflicts. Taste must not fight the contract.

## Application

All five sub-agents have TASTE.md files in the standardized format:

- `agents/scout/TASTE.md` - Research instincts: depth over breadth, primary sources first, stop at diminishing returns
- `agents/scribe/TASTE.md` - Writing instincts: rhythm, active voice, concrete over abstract, cut the hedges
- `agents/forge/TASTE.md` - Code style instincts: simplicity over cleverness, one job per function, early returns
- `agents/inspector/TASTE.md` - Code quality instincts: tests are evidence, naming describes intent, automation beats manual review
- `agents/ops/TASTE.md` - Infrastructure instincts: redundancy where it matters, monitoring before incidents, simple is reliable
