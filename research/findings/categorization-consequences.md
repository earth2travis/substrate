---
title: "Categorization and Its Consequences: Bowker and Star in the Age of Generated Taxonomies"
tags: [finding, categorization, knowledge-management, ethics, infrastructure, evaluation]
related:
- decision-tools-and-categorization
- jev-system-one-models
- knowledge-graphs-as-agent-memory-substrate
- agent-provenance-graph
- decision-provenance
- llm-wiki-pattern
source: research/raw/decision-tools-and-categorization.md
ingested: 2026-11-23
---

# Categorization and Its Consequences: Bowker and Star in the Age of Generated Taxonomies

## Key Points

**The thesis in one sentence.** Bowker and Star, Sorting Things Out: Classification and Its Consequences (MIT Press, 1999): "Each standard and each category valorizes some point of view and silences another. This is not inherently a bad thing; indeed it is inescapable. But it is an ethical choice, and as such it is dangerous, not bad, but dangerous." A classification system is "a set of boxes (metaphorical or literal) into which things can be put in order to then do some kind of work." The ideal type assumes consistent and unique classificatory principles, mutually exclusive categories, and completeness; real systems fail all three, and the failures are where the story lives.

**Torque, residual categories, infrastructure, boundary objects.** Torque is the felt twist when the formal category and the lived trajectory disagree. The residual category ("other," "not elsewhere classified") is the bucket a scheme cannot name; "others are everywhere, structuring social order," and where you put the residual decides who is invisible. Classification systems are information infrastructure, ordinarily invisible and visible "only upon breakdown," which is why the consequences are easy to miss. Boundary objects (from Star and Griesemer, 1989) are "objects for cooperation across social worlds," both ambiguous and constant; where they cannot be built, the book's word for the outcome is violence.

**The engineering brief hidden in the book: four design demands of any classification system.** The residual category is a design decision with political content, so "other" must be first-class rather than a dumping ground. Invisibility is a feature of adoption and a hazard of accountability, so the system should keep a trace of why a category exists and who chose it. The same label can mean different things to different communities, so a flat label set will be misread across teams. And user-visible disagreement (torque) is signal rather than error, and should have a route back into the schema. Bowker and Star's closing normative proposal: "The only good classification is a living classification," one that retains traces of its construction, is tunable to new arrangements, and can reconfigure the world on the fly.

**Foucault is the companion that supplies the layer Bowker and Star leave thinner.** "The Order of Things" (1966) opens on Borges's impossible Chinese encyclopedia: the point is not that the taxonomy is wrong but that it destroys the possibility of ordering at all. Knowledge is made possible by an episteme, a historical a priori deciding what can be said and seen together. Use Foucault for the philosophical claim that ordering precedes knowing; use Bowker and Star for the empirical case that specific orderings, once built, are consequential and contestable.

**The technical state of the art, briefly.** SetFit (arXiv:2209.11055) is the current practical default for small labeled sets; zero-shot classification with LLMs is cheap and brittle; embedding nearest-neighbor is the most legible form to a category-theorist (adding a category is adding a prototype, and a query near no prototype returns high-abstention); contrastive learning makes the taxonomy's geometry explicit; and past a few hundred categories, flat softmax stops being the right tool and the problem becomes retrieval and ranking (eXtreme Multi-label Classification).

**The taxonomy problem has inverted, and the failure mode is now provenance loss.** Classically the taxonomy was fixed and the classifier was learned; the emerging pattern is the reverse, with the classifier (an LLM) fixed and the taxonomy generated per tenant, per corpus, or per run. Where curated taxonomies had a knowledge-acquisition bottleneck, generated taxonomies have a provenance and comparability failure: "the taxonomy used in March" and "the taxonomy used in April" are not comparable, and any longitudinal aggregate silently compares apples to oranges. Bowker and Star asked for classifications that retain traces of their construction; a generated taxonomy discarded and re-derived each run is the exact opposite, maximum recency with zero provenance. The engineering response is to version the taxonomy as you version the model, or you cannot audit either — and no surveyed product does it.

**Evaluation is where the two literatures fail to meet.** The decision-tools literature optimizes accuracy, cost, latency, and calibration; the categorization literature asks about consequences, residuals, and the route by which a person can contest a category. No product in this survey serves both, and no evaluation framework measures both. Inter-annotator agreement (Cohen's kappa, Fleiss's kappa, Krippendorff's alpha) is both a ceiling and a diagnosis of the schema: low kappa is a symptom of taxonomy negotiation, not of annotator failure. Abstention is the engineering form of the residual category — the system saying "the scheme does not name this" — and a system that cannot say it is lying about its completeness.

## Open Questions

- No product was found implementing any of Bowker and Star's four design demands; if one exists, it belongs in the raw file.
- The claim that generated taxonomies cause audit failure is an INTERPRETATION; a case study would convert it to evidence.

## Source

`research/raw/decision-tools-and-categorization.md` (sections 4 and 6; the Bowker and Star quotations verified against the author-published full text). The decision-tools half of the same source is [[decision-tools-and-categorization]]; the product at its centre is [[jev-system-one-models]]. The connection to this graph's own work is direct: the Substrate is itself a classification system, so the residual category, the retained trace of construction, and the route to contest a category are design demands on [[knowledge-graphs-as-agent-memory-substrate]], [[agent-provenance-graph]], and [[decision-provenance]]. Versioning the taxonomy as you version the model is the same discipline as [[llm-wiki-pattern]]'s living classification.
