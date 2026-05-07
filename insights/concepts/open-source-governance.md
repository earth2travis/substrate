---
title: "Open Source Governance"
tags: [open-source, governance, philosophy, repository, community, history]
related: [[open-source-best-practices]], [[github-as-knowledge-graph]], [[toyota-production-system]], [[lean-doctrine]]
updated: 2026-05-07
---

# Open Source Governance

Open source is not just a development methodology. It is a philosophy, a political act, and a governance experiment. Understanding its history and models is essential for anyone building in the open.

## Historical Arc

**1960s-70s:** Software shared freely among researchers. Proprietary software seemed bizarre.
**Late 1970s:** Personal computer revolution makes software independently valuable. Gates's 1976 "Open Letter to Hobbyists" marks the enclosure.
**1983:** Stallman launches GNU Project. Four freedoms: run, study/modify, redistribute, distribute modified versions. GPL encodes them legally with copyleft.
**1991:** Torvalds posts Linux kernel. "Just a hobby, won't be big and professional like gnu."
**1997:** Raymond's "Cathedral and the Bazaar": "Given enough eyeballs, all bugs are shallow."
**1998:** Peterson coins "open source." OSI founded. Rebranding emphasizes pragmatism over philosophy.
**2008:** Bitcoin — pseudonymous founder, no company, working code. Satoshi's disappearance ensures the project can never be captured.
**2008:** GitHub turns distributed version control into a social network.
**2015:** Ethereum extends Bitcoin's insight into general-purpose computation. The DAO fork proves governance is always political.

## Governance Models

**BDFL (Benevolent Dictator for Life)**
One person makes final decisions. Linus Torvalds for Linux, Guido van Rossum for Python. Works with good judgment and community trust. Breaks with burnout, unpopular decisions, or bottleneck.

**Pseudonymous Founder + Disappearance**
Bitcoin's unique contribution. The protocol's rules constrain behavior more effectively than any human leader. Governance by architecture. Only works when rules are sufficiently clear and self-enforcing.

**Meritocracy**
Contributors earn authority through demonstrated competence. Apache formalized: contributor → committer → PMC member. In theory, best ideas win. In practice, reproduces existing power dynamics.

**Foundation-Led**
Linux Foundation, Apache, Ethereum Foundation. Adds legitimacy, longevity, bureaucracy, and corporate sponsor influence.

**Rough Consensus and Running Code**
IETF principle adopted by many crypto projects. "We reject kings, presidents, and voting. We believe in rough consensus and running code." No formal voting — discussion continues until disagreements narrow, then chairs judge consensus.

**Corporate-Backed**
React (Meta), Angular (Google). Well-funded, well-maintained, but creates dependency on sponsor interests. Redis and HashiCorp relicensing controversies (2023-24) revealed the tension.

## Philosophical Currents

| Tradition | Proponent | Core Claim |
|---|---|---|
| Ethical | Stallman | Software freedom is a moral imperative. Proprietary software is injustice. |
| Pragmatic | Raymond | Open source is superior development methodology. License is a tool, not values. |
| Cypherpunk | Hughes, May | Code is speech. Cryptography is a human right. Build freedom without permission. |
| Commons | Ostrom | Shared resource governed by community norms. Tragedy of the commons is the perpetual threat. |

## Best Practices

**Community Standards:** README (front door), CONTRIBUTING (contributor's map), CODE_OF_CONDUCT (behavioral expectations), SECURITY (vulnerability reporting), LICENSE (non-negotiable), SUPPORT (help channels), FUNDING (sustainability)

**Branch Protection:** require PR reviews, status checks, linear history, restrict direct pushes

**CI/CD:** lint, format, type check, tests on every PR; build and deploy on merge; scheduled dependency and security scanning

**Documentation Hierarchy:** inline comments (why, not what) → README → docs/ → external site

## Case Studies

**GNU:** A manifesto can be a founding document. The four freedoms became a constitution. Warns that the leader's vision must be separable from the leader's person.

**Bitcoin:** Deliberate slowness in critical paths. Not every part moves fast. Explicit non-hierarchy: "there is no particular concept of 'Bitcoin Core developers' in the sense of privileged people."

**Ethereum:** Structured deliberation (EIP process with numbered proposals and lifecycles). Multi-stakeholder model with no single veto. The DAO fork proved governance is social, not technical.

## Core Principles

- Automate the routine, humanize the exceptions
- Document decisions, not just outcomes
- Values first, process second
- Start simple, add complexity only when you feel the pain
- Governance is transparency, not bureaucracy
- The founder must be separable from the project
