# Harness Engineering Evaluation: Synthweave

Evaluation against OpenAI's agent-first development methodology.

---

## 1. AGENTS.md as Table of Contents

**Score: 2/5** - Minimal

### What Exists

- **Root CLAUDE.md** (128 lines): Core principles, repo layout, workflow, Hasura development guidance
- **UI CLAUDE.md** (217 lines): UI-specific standards (styling, theming, z-index, icons)
- **Chat AGENTS.md** (139 lines): Single BC-specific agent guidance (React key mechanism rules)
- **22 context.md files**: Comprehensive bounded context documentation with ubiquitous language
- **docs/architecture/**: 10 files, 7,519 lines of implementation plans

### Critical Gaps

- **No top-level AGENTS.md**: No agent-facing entry point explaining how to navigate the codebase
- **No docs/INDEX.md**: No navigation document mapping what documentation exists where
- **No ADRs**: Architectural decisions embedded in plan documents, not indexed separately
- **No tech debt tracking**: No KNOWN_ISSUES.md or tracked technical debt
- **Monolithic plans**: Architecture docs are comprehensive but scattered (7,500+ lines across 10 files)

### Quick Wins

1. Create `/AGENTS.md` with structured navigation to CLAUDE.md, context.md files, and architecture docs
2. Add `/docs/INDEX.md` listing all documentation with reading order
3. Extract ADR-style summaries from existing plan documents

### Recommendations

- Create `/docs/decisions/` with ADR format for major architectural choices
- Add `AGENTS.md` to each bounded context (currently only Chat has one)
- Version active plans vs completed plans in `/docs/plans/active/` and `/docs/plans/completed/`

---

## 2. Repository as System of Record

**Score: 3.5/5** - Partial with good foundation

### What Exists

- **22 context.md files**: Complete ubiquitous language per bounded context
- **DDD architecture**: Clear bounded contexts with domain/application/infrastructure/ui layers
- **CLAUDE.md**: Coding standards, conventions, workflow documented
- **TECHNICAL_SUMMARY.md**: Comprehensive API surface documentation
- **docs/features/**: 11 feature-specific documentation files
- **hasura/migrations/**: Complete database schema history

### Critical Gaps

- **External context dependencies**:
  - No link to product roadmap or feature prioritization
  - Design decisions may live in external systems (Notion, Google Docs, Slack)
  - User research and product requirements not in-repo
- **Tribal knowledge**:
  - Why certain patterns were chosen over alternatives not documented
  - Historical context for tech debt not captured
  - Integration gotchas (Auth0, Hasura quirks) learned through experience

### Quick Wins

1. Add "Why" sections to context.md files explaining design rationale
2. Create `/docs/GOTCHAS.md` for integration-specific pitfalls
3. Link external documentation sources in a `/docs/EXTERNAL_REFERENCES.md`

### Recommendations

- Establish convention: any significant decision discussed in Slack gets ADR in-repo
- Add "Last updated" dates to all documentation files
- Create `/docs/domain/` with business domain explanations for non-developer context

---

## 3. Mechanical Enforcement

**Score: 3/5** - Partial enforcement

### What Exists

**Linting (ESLint + Stylelint + Prettier)**:
```javascript
// ESLint: typescript-eslint strictTypeChecked + stylisticTypeChecked
// GraphQL: @graphql-eslint/no-duplicate-fields, no-unused-variables (error)
// Stylelint: color-no-hex (enforces design tokens)
// Prettier: Tailwind plugin for class ordering
```

**Pre-commit hooks** (.husky/pre-commit):
- Prettier formatting enforcement

**CI Enforcement** (.github/workflows/pr-build.yml):
- `npm run build` - Must pass
- `npm run typecheck` - TypeScript checking
- `npm run test:coverage` - Unit tests with coverage reporting

**Custom Validation** (scripts/validate-hasura-inserts.ts):
- Validates GraphQL mutations include all NOT NULL columns
- Catches schema/mutation mismatches

**Zod Schemas**:
- Runtime validation at HTTP boundaries
- Template schemas for sample data

### Critical Gaps

- **No dependency boundary enforcement**: No dependency-cruiser or eslint-plugin-boundaries
- **No import cycle detection**: Circular dependencies not mechanically prevented
- **No file size limits**: Large files not flagged
- **No commit message linting**: No commitlint or conventional commits
- **Lint errors lack remediation**: Standard ESLint messages, not agent-friendly instructions
- **No schema drift detection**: GraphQL schema changes don't auto-validate against code

### Quick Wins

1. Add eslint-plugin-boundaries for BC import restrictions
2. Create custom ESLint rule with remediation instructions in messages
3. Add commitlint for conventional commit enforcement

### Recommendations

- Implement dependency-cruiser with BC boundary rules
- Add structural tests that validate bounded context isolation
- Create `/scripts/lint-architecture.ts` for custom architectural validation

---

## 4. Application Legibility for Agents

**Score: 4/5** - Strong

### What Exists

**Headless Boot** (scripts/dev-start.ts):
```bash
npm run dev:start         # Start all services (Docker, Hasura, UI, Server)
npm run dev:start stop    # Stop all services
npm run dev:start --cleanup  # Cleanup on error
```
- Prerequisite checking (Docker, npm)
- Health polling for Hasura (30 retries)
- Graceful shutdown handling

**MCP Tools for Agent Automation** (22 tools):
- Navigation: `ls`
- Search: `snip_search` (hybrid semantic + full-text)
- CRUD: `snip_reader`, `create-snip`, `snip_rewrite`, `manage_snip`
- Projects: `create_project`, `task_creator`, `task_updater`
- Version control: `checkpoint`

**Observability**:
- Laminar (OpenTelemetry tracing)
- PostHog (event analytics)
- Morgan HTTP logging with custom tokens
- BullBoard queue dashboard (`/admin/queues`)

**Docker Compose**:
- PostgreSQL 16 + pgvector
- Valkey (Redis-compatible)
- Hasura with healthchecks
- All services have health endpoints

### Critical Gaps

- **No Playwright/UI automation**: Agent cannot drive the UI programmatically
- **No per-worktree isolation**: Single Docker environment, not per-branch
- **No test database factory**: Manual database reset required
- **Logs not centralized**: Console-based, no log aggregation service

### Quick Wins

1. Add Playwright configuration for basic smoke tests
2. Create `docker-compose.test.yml` for isolated test environment
3. Add correlation IDs to all log messages

### Recommendations

- Implement database factory for isolated test runs
- Add screenshot capability to MCP tools for visual verification
- Create `/scripts/reset-test-db.ts` for agent-driven database reset

---

## 5. Testing and Verification

**Score: 3/5** - Partial

### What Exists

**Test Coverage**:
- 153 test files total (106 server, 45 UI, 2 scripts)
- Vitest with v8 coverage provider
- Coverage reports: text-summary, JSON, HTML, Cobertura
- CI posts coverage metrics to PR comments

**Test Organization**:
- Unit tests per bounded context
- Integration tests (`.integration.test.ts`)
- Contract tests (`.contract.test.ts`)
- E2E tests (`.e2e.test.ts` suffix)

**E2E Testing**:
- Checksum AI-powered E2E tests on PRs to main
- 1 Playwright spec for collaboration features
- 120-minute timeout for E2E suite

**Conditional Execution**:
- `describe.skipIf()` for integration tests
- Environment-based test skipping

### Critical Gaps

- **Minimal E2E coverage**: Only 1 Playwright spec file
- **No visual regression testing**: No Percy, Chromatic, or screenshot comparison
- **No proof-of-work capability**: Agent cannot demonstrate fix with screenshots/video
- **No acceptance criteria framework**: Tests don't map to user stories or acceptance criteria
- **Flaky test management**: No vitest retry configuration, only application-level retries
- **Test/coverage ratio**: UI has 2.4x fewer tests than server

### Quick Wins

1. Add vitest retry configuration for known flaky tests
2. Create `/tests/acceptance/` with criteria-driven tests
3. Add screenshot capture to E2E tests

### Recommendations

- Implement visual regression testing with Percy or Chromatic
- Create evaluation harness that agents can query for pass/fail status
- Add `/scripts/proof-of-work.ts` for agent demonstration capability
- Centralize test utilities in `/packages/test-utils/`

---

## 6. CI/CD and Merge Pipeline

**Score: 3/5** - Partial

### What Exists

**GitHub Workflows** (.github/workflows/):
1. `pr-build.yml`: Build + typecheck + unit tests with coverage
2. `checksum-tests.yml`: E2E tests on main PRs
3. `checksum-test-cases.yml`: AI-powered CI guard
4. `pr-summary.yml`: CodeRabbit AI code review

**Blocking Gates**:
- Build must pass
- TypeScript must pass
- Unit tests must pass
- Coverage report generated (informational)

**Automation**:
- Pre-commit: Prettier formatting
- PR: Automated code review summary
- E2E: AI-assisted test assertion (disabled in CI)

### Critical Gaps

- **No release automation**: No semantic-release, changesets, or versioning
- **No production deploy pipeline**: No Vercel/Railway/AWS deployment
- **No branch protection config in-repo**: Likely configured in GitHub UI
- **No automated changelog**: Version history not generated
- **CI feedback not agent-friendly**: Standard GitHub Actions output

### Quick Wins

1. Add changesets for version management
2. Create deploy workflow for staging environment
3. Add CI timing metrics to track iteration speed

### Recommendations

- Implement semantic-release with conventional commits
- Add deployment previews for PRs
- Create `/scripts/merge-check.ts` for agent-queryable merge status
- Add MCP tool for agent to check CI status programmatically

---

## 7. Entropy and Quality Control

**Score: 2.5/5** - Minimal

### What Exists

**Quality Standards**:
- CLAUDE.md documents coding standards
- DDD principles enforced by convention
- Stylelint enforces design token usage (no raw hex colors)
- TypeScript strict mode

**Pattern Enforcement**:
- Bounded context structure is consistent
- GraphQL operation validation script
- Zod schemas at boundaries

### Critical Gaps

- **No tech debt tracking**: No TECHNICAL_DEBT.md or tracked issues
- **No quality grades**: No scoring system for code health
- **No stale documentation detection**: context.md files may drift from implementation
- **No pattern drift scanning**: Deviations from DDD patterns not detected
- **No cleanup agent capability**: No automated code quality improvement tools
- **No deprecation tracking**: Removed/deprecated code not documented

### Quick Wins

1. Create `/TECHNICAL_DEBT.md` with categorized issues
2. Add "Last verified" dates to context.md files
3. Create `/scripts/quality-scan.ts` for pattern drift detection

### Recommendations

- Implement code quality scoring (maintainability index, complexity)
- Create recurring cleanup checklist for agent execution
- Add `/docs/DEPRECATIONS.md` for tracked removals
- Integrate SonarQube or CodeClimate for automated quality tracking

---

## 8. Progressive Disclosure and Navigation

**Score: 3.5/5** - Partial

### What Exists

**Entry Points**:
- `README.md` (230 lines): Architecture overview, quick start
- `CLAUDE.md` (128 lines): Core principles, workflow
- `TECHNICAL_SUMMARY.md` (430 lines): API deep dive

**Structured Paths**:
```
README.md → CLAUDE.md → context.md (per BC) → domain/models/ → implementation
```

**Cross-References**:
- CLAUDE.md links to apps/ui/CLAUDE.md
- Context.md files reference domain models
- Architecture plans reference each other

**Self-Documenting Structure**:
```
src/bounded-contexts/[BCName]/
├── context.md          # Entry point for BC
├── domain/models/      # Core entities
├── application/events/ # Use cases
├── infrastructure/     # Adapters
└── ui/                 # Components
```

### Critical Gaps

- **File count for feature understanding**: Agent needs to read 10-15 files to understand a typical feature
- **No "recommended reading order"**: Agent must discover dependencies themselves
- **Inconsistent BC documentation**: Only 1 of 13 server BCs has README
- **Missing cross-references**: Tests don't link to specs, specs don't link to implementation
- **No dependency graph visualization**: Agent cannot see BC relationships

### Quick Wins

1. Add README.md to each server bounded context
2. Create `/docs/READING_ORDER.md` with suggested exploration paths
3. Add "Related files" section to context.md files

### Recommendations

- Generate dependency graph (mermaid diagram) of bounded contexts
- Create `/scripts/find-related.ts` for agent to discover related files
- Add "See also" sections linking tests ↔ implementation ↔ docs
- Implement file tagging system for easier navigation

---

## Overall Assessment

### Harness Engineering Readiness Score: 3.1/5

| Category | Score | Weight | Weighted |
|----------|-------|--------|----------|
| 1. AGENTS.md as ToC | 2.0 | 1.0 | 2.0 |
| 2. Repo as System of Record | 3.5 | 1.2 | 4.2 |
| 3. Mechanical Enforcement | 3.0 | 1.3 | 3.9 |
| 4. Application Legibility | 4.0 | 1.5 | 6.0 |
| 5. Testing and Verification | 3.0 | 1.3 | 3.9 |
| 6. CI/CD Pipeline | 3.0 | 1.0 | 3.0 |
| 7. Entropy and Quality | 2.5 | 1.2 | 3.0 |
| 8. Progressive Disclosure | 3.5 | 1.0 | 3.5 |
| **Total** | | **9.5** | **29.5** |
| **Weighted Average** | | | **3.1** |

### Strengths

1. **Excellent MCP tooling**: 22 tools for programmatic workspace manipulation
2. **Strong DDD foundation**: Consistent bounded context structure with context.md
3. **Comprehensive documentation**: 7,500+ lines of architecture docs
4. **Good headless operation**: dev-start.ts handles full environment orchestration
5. **Multi-tier observability**: Laminar + PostHog + Morgan logging

### Critical Weaknesses

1. **No agent-facing entry point**: Missing AGENTS.md navigation guide
2. **No dependency boundary enforcement**: BC isolation is convention-only
3. **No tech debt tracking**: Historical context and known issues undocumented
4. **No proof-of-work capability**: Agent cannot demonstrate fixes visually
5. **No release automation**: Manual deployment process

---

## Top 5 Investments for Agent Effectiveness

### 1. Create AGENTS.md Navigation System (Impact: High, Effort: Low)

**What**: Top-level AGENTS.md with structured paths to all documentation

```markdown
# AGENTS.md
## Quick Start
- For new features: Start with `/apps/ui/src/bounded-contexts/{BC}/context.md`
- For API work: See `/TECHNICAL_SUMMARY.md`
- For architecture: See `/docs/architecture/INDEX.md`

## Bounded Context Map
[Mermaid diagram of BC relationships]

## Documentation Index
[Links to all context.md, CLAUDE.md, and architecture docs]
```

**Why**: Reduces agent exploration time from 15+ files to 3-4 targeted reads.

---

### 2. Add Dependency Boundary Enforcement (Impact: High, Effort: Medium)

**What**: eslint-plugin-boundaries + dependency-cruiser configuration

```javascript
// .dependency-cruiser.js
{
  forbidden: [{
    name: 'bc-isolation',
    from: { path: '^src/bounded-contexts/([^/]+)/' },
    to: { path: '^src/bounded-contexts/(?!$1/)' },
    message: 'Cross-BC imports must go through ports'
  }]
}
```

**Why**: Prevents architectural drift, gives agents clear "what can import what" rules.

---

### 3. Implement Proof-of-Work Capability (Impact: High, Effort: Medium)

**What**: MCP tool for screenshot capture + test execution + result reporting

```typescript
// New MCP tools
verify_fix: {
  runTests: ['apps/server/src/.../*.test.ts'],
  captureScreenshot: '/snips/:id',
  generateReport: 'markdown'
}
```

**Why**: Agent can demonstrate that changes work, not just that they compile.

---

### 4. Create Tech Debt Registry (Impact: Medium, Effort: Low)

**What**: `/TECHNICAL_DEBT.md` with categorized, prioritized issues

```markdown
# Technical Debt Registry

## Critical (blocks agent work)
- [ ] TD-001: No test database isolation - affects all integration tests

## High (should fix soon)
- [ ] TD-002: UI test coverage gap - 2.4x fewer tests than server

## Medium (nice to have)
- [ ] TD-003: No visual regression tests
```

**Why**: Agents can prioritize cleanup work and avoid known pitfalls.

---

### 5. Add Agent-Queryable CI/Merge Status (Impact: Medium, Effort: Low)

**What**: MCP tool or script that returns structured CI status

```typescript
// scripts/check-ci-status.ts
{
  branch: 'feature/foo',
  checks: {
    build: 'passing',
    typecheck: 'passing',
    tests: 'failing',
    coverage: { statements: 78.5, branches: 65.2 }
  },
  blockers: ['unit-tests'],
  mergeable: false
}
```

**Why**: Agent can self-diagnose merge failures and iterate without human intervention.

---

## Conclusion

Synthweave has a **strong foundation** for agent-first development, particularly in MCP tooling and DDD structure. The main gaps are in **documentation navigation**, **mechanical enforcement of boundaries**, and **proof-of-work capabilities**. The top 5 investments above would move the harness engineering score from **3.1 to approximately 4.0**, making the codebase significantly more autonomous-agent-friendly.
