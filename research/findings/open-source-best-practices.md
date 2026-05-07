---
title: "Open Source: History, Philosophy, and Best Practices"
tags: [open-source, governance, github, history, philosophy, repository-management]
related:
- open-source-governance
- github-as-knowledge-graph
- toyota-production-system
- lean-doctrine
source: research/raw/open-source-best-practices.md
---
# Open Source: History, Philosophy, and Best Practices

## Part 1: History

### Before the Name
In the 1960s-70s, software was shared freely among researchers. Proprietary software became independently valuable in the late 1970s. Bill Gates's 1976 "Open Letter to Hobbyists" marked software as intellectual property.

### The Free Software Movement
Richard Stallman launched the GNU Project (1983) and founded the FSF (1985). Four freedoms: run, study/modify, redistribute, distribute modified versions. The GPL (1989) encoded these legally with copyleft.

### The Cypherpunk Thread
Eric Hughes, Tim May, and John Gilmore gathered in 1992. Their motto: "Cypherpunks write code." They built anonymous remailers, PGP networks, and debated digital cash. The line to Bitcoin to Ethereum is direct.

### Linux and the Cathedral vs. the Bazaar
Linus Torvalds's 1991 kernel filled the GNU gap. Eric Raymond's 1997 essay captured the difference: "Given enough eyeballs, all bugs are shallow." The bazaar model: release early, release often, delegate everything.

### Key Inflection Points
- **Apache (1995):** permissive license, foundation governance model
- **SourceForge (1999):** lowered barrier to participation at scale
- **Bitcoin (2008):** pseudonymous founder, no company, working code. Satoshi's disappearance in 2010 ensured the project could never be captured
- **GitHub (2008):** turned distributed version control into a social network
- **Ethereum (2015):** "world computer" with smart contracts. The DAO fork (2016) proved governance in decentralized systems is always political
- **Node.js/npm:** ecosystem model revealed both power and fragility (left-pad incident, 2016)

### Governance Models
- **BDFL:** Linus Torvalds, Guido van Rossum. Works with good judgment; breaks with burnout
- **Pseudonymous founder + disappearance:** Bitcoin's unique contribution. Governance by architecture
- **Meritocracy:** Apache formalized this. Best ideas win, but power dynamics persist
- **Foundation-led:** Linux Foundation, Apache, Ethereum. Adds legitimacy and bureaucracy
- **Rough consensus and running code:** IETF principle. "We reject kings, presidents, and voting."
- **Corporate-backed:** React, Angular. Well-funded but creates dependency on sponsor interests

### Philosophical Currents
- **Ethical (Stallman):** software freedom is a moral imperative
- **Pragmatic (Raymond):** open source is superior development methodology
- **Cypherpunk (Hughes, May):** code is speech, cryptography is a human right
- **Commons (Ostrom):** shared resource governed by community norms

## Part 2: Best Practices for Repository Management

### Community Standards Files
- **README.md:** front door — what, why, how to use, how to contribute
- **CONTRIBUTING.md:** development environment, submission process, standards
- **CODE_OF_CONDUCT.md:** behavioral expectations (Contributor Covenant is de facto standard)
- **SECURITY.md:** vulnerability reporting process and disclosure policy
- **LICENSE:** non-negotiable. MIT/Apache for adoption; GPL for copyleft
- **SUPPORT.md:** where to get help (distinguishes bugs from questions)
- **FUNDING.yml:** GitHub Sponsors integration

### Issue and PR Templates
- Bug report: steps to reproduce, expected vs. actual, environment
- Feature request: problem statement, proposed solution, alternatives
- Blank issue: always include an escape hatch
- YAML-based issue forms provide validation and required fields

### Branch Protection and Review
- Require PR reviews before merging
- Require status checks to pass
- Require linear history
- Restrict direct pushes
- Automated checks: linting, formatting, type checking, security scanning

### CI/CD Pipeline
1. On every PR: lint, format check, type check, tests
2. On merge to main: build, test, deploy
3. On schedule: dependency updates, security scanning

### Release Management
- Semantic Versioning (SemVer): MAJOR.MINOR.PATCH
- Automated changelog generation from conventional commits
- Tools: `release-please`, `standard-version`

### Documentation Hierarchy
1. Inline comments (why, not what)
2. README.md (quick orientation)
3. docs/ directory (architecture, guides)
4. External docs site (when project outgrows directory)

## Part 3: Case Studies

### GNU: The Manifesto as Architecture
Stallman led with moral authority, not corporate. Every technical decision filtered through ethics: does this increase user freedom? Proved a manifesto can be a founding document. Warned that the leader's vision must be separable from the leader's person.

### Bitcoin: Governance by Disappearance
Satoshi's vanishing ensured Bitcoin could never be "Satoshi's project." Governance by architecture: the protocol's rules constrain behavior more effectively than any human leader. The CONTRIBUTING.md states: "there is no particular concept of 'Bitcoin Core developers' in the sense of privileged people."

### Ethereum: The World Computer and the EIP Process
EIP process provides structured deliberation: numbered proposals with clear statuses and lifecycles. Seven stakeholder groups with no single veto. The DAO fork proved governance is ultimately social, not technical.

## Recommendations

**Immediate:** CODE_OF_CONDUCT.md, SECURITY.md, LICENSE, YAML issue templates
**Short term:** automated CI checks, GOVERNANCE.md, project vision document, automated changelog
**Medium term:** formal proposal process, stale issue management, document human-AI workflow, publish iteration plans

**Principles:** automate the routine, humanize the exceptions; document decisions not just outcomes; values first, process second; start simple, add complexity only when you feel the pain; governance is transparency, not bureaucracy; the founder must be separable from the project.
