# GitHub as Memory: Pushing the Concept Forward

_Research for #432. Conducted 2026-03-31._

## The Thesis

GitHub Issues are not a task tracker. They are nodes in an institutional knowledge graph. Every issue captures a decision, a context, a piece of understanding. The commit log is a timeline. PRs narrate how and why things changed. Comments preserve the reasoning that shaped direction.

We have been operating with this philosophy since the beginning, but there is a gap between saying "issues are memory" and actually optimizing for retrieval, cross-referencing, and future comprehension.

## Audit: 20 Recent Issues Scored for Memory Quality

Scored 20 recent issues (open and closed, #446 through #550) on five dimensions:

| Dimension | Description | Avg Score (1-5) |
|-----------|-------------|-----------------|
| Context richness | Does the body explain *why*, not just *what*? | 3.4 |
| Cross-references | Links to related issues, decisions, research? | 2.8 |
| Searchability | Title + labels optimized for future retrieval? | 3.1 |
| Closure quality | Comments document outcome, lessons, artifacts? | 2.5 |
| Knowledge density | Would future-us learn from reading this issue? | 3.0 |

**Overall: 2.96 / 5.0** (passing, but significant room for improvement)

### Patterns Found

**Strong:**
- Issue bodies generally explain context well (research issues especially: #432, #465, #449)
- Prefix convention (feat:, chore:, research:) aids categorization
- Acceptance criteria create clear completion signals

**Weak:**
- 5 of 20 recent issues have zero labels (#546-550), making them invisible to filtered views
- Closure comments are often perfunctory ("done") or missing entirely
- Cross-references are sparse: most issues link to 0 or 1 other issues
- Research issues rarely link back to which decisions they influenced
- No convention for linking issues to file artifacts (research files, decisions, guides)

### Specific Findings

1. **Unlabeled cluster:** Issues #546-550 (all research) have no labels. These were likely auto-created from a session and never triaged.
2. **Duplicate detection:** #511 and #543 were identical Farcaster Friday issues (closed #511 as duplicate during this audit).
3. **Orphaned research:** Several research issues (#470, #480) were closed but their research artifacts are not referenced from anywhere discoverable.
4. **Comment desert:** 11 of 20 issues have zero comments. Even closed issues have no record of what happened or what was learned.

## Research: How Others Use GitHub as Memory

### Agent Systems

- **SWE-agent / Devin patterns:** Use issue bodies as task specs, but rarely as knowledge stores. The agent reads the issue, does the work, closes it. No knowledge accumulation.
- **BoilerHAUS knowledge base pattern:** Stores knowledge as markdown in repos, uses issues for meta-discussion about the knowledge. Closer to what we want.
- **Cursor/Windsurf patterns:** Treat codebase as memory, issues as work queue. No institutional memory concept.

### Human Organizations

- **GitLab's handbook-first approach:** Everything is documented in the repo. Issues are discussions that lead to handbook changes. The handbook is the memory; issues are the process. Relevant: they enforce "link to handbook section" in every issue.
- **Oxide Computer:** Dense issue culture. Long, thoughtful issue bodies. RFDs (Requests for Discussion) as the primary decision mechanism. Issues reference RFDs. The graph is tight.
- **Astral (uv/ruff):** High-quality issue triage. Labels are taxonomic. Milestones track release scope. But issues are still tasks, not knowledge.

### Key Insight

The organizations that use GitHub as memory (not just tracking) share one trait: **issues are written for the reader who arrives six months later**, not for the person doing the work today. This is a mindset shift, not a tooling change.

## The GitHub Memory Protocol

Conventions for writing issues that serve as institutional memory.

### 1. Issue Body: Write for Future Retrieval

Every issue body should answer:
- **What** is this about? (clear, searchable title)
- **Why** does it matter? (context, motivation, connection to goals)
- **What did we learn?** (for closed issues: outcomes, lessons, artifacts)
- **Where does it connect?** (related issues, decisions, research, files)

### 2. Mandatory Cross-References

Every issue should link to at least one of:
- A parent goal or epic issue
- A related decision document
- A research file that informed it
- File paths of artifacts created

Add a "## Related" section at the bottom. This is already common in our issues but not enforced.

### 3. Closure Protocol

When closing an issue, the closing comment must include:
- **Outcome:** What was the result?
- **Artifacts:** What files were created or changed? (with paths)
- **Lessons:** What did we learn? (even if "nothing surprising")
- **PR:** Link to the PR if applicable

This is the biggest gap. Most of our closures say "done" or auto-close via PR merge with no summary.

### 4. Label Hygiene

Every issue gets labeled at creation. No exceptions. Minimum labels:
- **Type:** task, enhancement, research, idea, bug, chore, infra
- **Domain:** (optional) community, documentation, security

Unlabeled issues are invisible to filtered views and memory search.

### 5. Knowledge Issues

Not every issue is a task. Some are knowledge containers. Create issues specifically to capture:
- **Decisions:** "Decision: chose X over Y because Z" (link to ADR if exists)
- **Learnings:** "Learning: agent memory degrades past 50K tokens"
- **Patterns:** "Pattern: prose-as-title naming improves retrieval"

These stay open as reference or get a "knowledge" label for future search.

### 6. Search Optimization

Write titles like you are writing a search query that future-you would type:
- Bad: "Fix the thing"
- Good: "fix: transmissions.sivart.wtf custom domain SSL not provisioning"
- Bad: "Memory stuff"
- Good: "research: tiered memory loading L0/L1/L2 for context efficiency"

Our prefix convention already helps. Enforce it consistently.

## Concrete Improvements (5 Actions)

### Action 1: Label the unlabeled (immediate)
Issues #546-550 need labels. This is a 2-minute fix that makes them discoverable.

### Action 2: Create a closure template (this week)
A checklist that appears when closing: outcome, artifacts, lessons, PR link. Can be a comment template or a mental checklist documented in AGENTS.md.

### Action 3: Add "Related" sections retroactively (ongoing)
When touching an issue for any reason, add cross-references. Don't batch this; do it incrementally.

### Action 4: Monthly memory health check (cron)
Script that flags: issues with no labels, closed issues with no closing comment, PRs with no linked issue. Run monthly, output to reports/.

### Action 5: Enable Discussions for architectural conversations (decision needed)
GitHub Discussions would give us a place for open-ended architectural conversations that don't fit the issue format. Needs Ξ2T sign-off since it changes repo structure.

## Connection to Loomrunner

Loomrunner (the-agent-factory #37) needs to understand project context from GitHub. The quality of our issues directly determines how well Loomrunner can:
- Understand task requirements
- Find related context
- Learn from past decisions
- Avoid repeating mistakes

The GitHub Memory Protocol is essentially a data quality standard for the knowledge graph that Loomrunner will consume. Better issues now means better agent performance later.

## Conclusion

Our issues are at a 3/5 for memory quality. The gap is not in what we capture (bodies are generally good) but in how we close (outcomes not documented), how we connect (cross-references sparse), and how we maintain (labels missing, duplicates appearing). The five actions above address each gap with minimal overhead.

The mindset shift: every issue is a letter to future-us. Write it that way.
