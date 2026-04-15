---
title: "Feature Flags: Best Practices and Opportunities"
tags:
  - research
related:
  - [[actual-occasions]]
  - [[ai-career-convergence]]
  - [[alfred-north-whitehead]]
  - [[api-first-interfaces]]
source: research/raw/feature-flags-best-practices.md
---

# Feature Flags: Best Practices and Opportunities

_Research completed February 12, 2026_

## Executive Summary

Feature flags (also called feature toggles or feature switches) are a software development technique that allows toggling features on or off at runtime without redeploying code. Now that PostHog is implemented, we have access to a powerful feature management and experimentation platform. This research documents best practices and identifies strategic opportunities for the partnership.

## Core Concepts

### What Feature Flags Enable

1. **Decoupling deploy from release**: Code can exist in production without being executed (dark launching)
2. **Phased rollouts**: Ship to 5% of users, monitor, gradually increase
3. **Kill switches**: Instantly disable broken features without redeploying
4. **User targeting**: Show features to specific users, teams, or segments
5. **A/B testing**: Run experiments with multivariate flags and measure results
6. **Remote configuration**: Send JSON payloads to configure behavior server side
7. **Beta programs**: Let users opt in to early access features
8. **Infrastructure migrations**: Gradually shift traffic between systems

### Flag Types by Lifecycle

| Type             | Duration        | Examples                                            |
| ---------------- | --------------- | --------------------------------------------------- |
| Release flags    | Days to weeks   | New feature rollouts, dark launches                 |
| Experiment flags | Weeks to months | A/B tests, multivariate experiments                 |
| Ops flags        | Permanent       | Kill switches, circuit breakers, log level controls |
| Permission flags | Permanent       | Entitlements, beta access, feature tiers            |

---

## Best Practices (The 12 Commandments)

### 1. Establish Clear Naming Conventions

Names should describe purpose and intent. Include:

- What the flag does
- When it was added
- Who owns it
- When it should be removed

**Bad**: `new_feature_v2_temp_DO_NOT_REMOVE`
**Good**: `checkout_flow_v2_2026Q1_@travis`

Avoid using "on" in flag names (e.g., "Tiles on") as it creates confusing double negatives when toggled off.

### 2. Use Centralized Management

PostHog provides this. Benefits:

- Single source of truth for flag states
- Visibility across environments
- Audit logs for compliance
- Integration with analytics

### 3. Keep Flags Short Lived

Treat flags like milk, not wine: they don't get better with age.

- Set expiration dates at creation time
- Default lifecycle: 30 days for release flags
- Block builds containing expired flags
- Budget time for flag cleanup in sprint planning

**Flag Friday**: One team dedicates the last hour of Friday to cleaning up old flags. Simple, consistent, visible.

### 4. Document Thoroughly

Every flag needs:

- Purpose (what problem does it solve?)
- Owner (a person, not "the team")
- User impact
- Expiration date
- Removal plan

### 5. Implement Access Controls

- Define roles and permissions
- Production environment changes should require approval (four eyes principle)
- Integrate with SSO for enterprise security
- Audit access permissions regularly

### 6. Monitor and Log Usage

- Track which flags are evaluated and how often
- Correlate flag changes with production metrics
- Alert on stale flags (no evaluation in 30 days)
- Detect flag combinations causing issues

### 7. Integrate with CI/CD

- Test all flag combinations in staging
- Automate flag cleanup tickets
- Include flag state in deployment manifests
- Run integration tests with flags in both states

### 8. Test Before Deployment

- Functional testing: does the flag do what it should?
- Regression testing: does toggling break other things?
- Combinatorial testing: what happens with other active flags?

### 9. Use Flags for Rollbacks

Feature flags enable instant rollback without code changes. A toggle flip is faster than a deployment rollback.

- Include kill switch flags for risky features
- Document rollback procedures per flag
- Test rollback paths before launch

### 10. A/B Testing and Experimentation

PostHog's experiments feature enables:

- Test different variations
- Measure statistical significance
- Run on new user flows (signup, onboarding)
- Validate hypotheses before full rollout

### 11. Canary Releases

Gradual rollouts minimize blast radius:

1. Internal users (dogfooding)
2. 1% of production traffic
3. 10% of production traffic
4. 50% of production traffic
5. General availability

Monitor metrics at each stage before expanding.

### 12. Target User Segments

PostHog supports targeting by:

- User properties (plan, role, signup date)
- Geographic location
- Device type
- Custom attributes

---

## The Seven Deadly Mistakes

### 1. The "And" Problem

If you describe a flag with "and," you've already failed. One flag = one function. Multi-function flags become impossible to understand or remove safely.

### 2. Placeholder Names

Never use temporary names like `foobar` or `test_flag`. You will forget to rename them.

### 3. Abandoned Ownership

"The developer who wrote it owns it forever" doesn't work. Transfer ownership to product or ops when the feature stabilizes.

### 4. Dumping on Ops

Don't make operations responsible for flags they don't understand. Context matters at every stage.

### 5. Technical Debt Accumulation (The Chest Freezer Problem)

Every temporary flag left in place adds debt. Like a chest freezer: easy to add things, hard to find them later, and eventually everything gets freezer burned.

### 6. Not Distinguishing Permanent Flags

Some flags are meant to be permanent (kill switches, entitlements). Mark them explicitly so they don't get removed accidentally.

### 7. Flag Reuse

Never reuse a flag name. Knight Capital lost $440 million in 45 minutes due to reusing a flag that triggered dormant code. Create new flags instead.

---

## Technical Architecture Principles

### 1. Enable Runtime Control

Flags must be dynamic, not static. If you need to restart to change a flag, that's configuration, not a feature flag.

Components needed:

- Feature Flag Control Service
- Database/data store
- API layer
- Client SDKs
- Continuous update mechanism

### 2. Prioritize Availability Over Consistency

Your application should not depend on the availability of your flag system.

- Bootstrap SDKs with cached data
- Evaluate flags locally when possible
- Graceful degradation when flag service is unavailable
- Eventually consistent is acceptable

### 3. Unique Flag Names

Ensure uniqueness across your entire system. This:

- Prevents accidental reactivation of old flags
- Makes search across codebases easier
- Enables reorganization as architecture evolves

### 4. Open by Default

Flag states should be visible to engineers, product, and support. Transparency enables collaboration and faster debugging.

### 5. Protect PII Server Side

Never send sensitive user data to a third party flag service. Evaluate flags server side where PII lives. For client side apps, use a proxy pattern.

### 6. Evaluate Close to the User

Minimize latency by:

- Local SDK evaluation
- Edge caching
- CDN distribution

### 7. Scale Horizontally

Decouple reads from writes. SDKs should read from cache; admin UI writes to control plane.

### 8. Keep Payloads Small

Use segments instead of embedding large targeting lists in flag definitions.

### 9. Consistent User Experience

Same user should see same flag state across sessions (sticky bucketing). Use consistent hashing on user ID.

### 10. Optimize Developer Experience

Make the right thing easy:

- Clear SDK APIs
- Good local development tools
- Easy to test both flag states
- Clear documentation

---

## Strategic Opportunities for [[Sivart]]/[[Ξ2T]]

### 1. Agent Behavior Flags

Use feature flags to control AI agent behavior:

- **Model selection**: Flag which model handles which tasks
- **Tool access**: Toggle tool availability per environment
- **Response styles**: Experiment with different personas
- **Safety levels**: Adjust caution levels for different contexts

### 2. Progressive Autonomy

Feature flags enable graduated trust:

- Start with flags requiring human approval
- Gradually expand autonomous actions based on success metrics
- Instant rollback if autonomy goes wrong

### 3. Multi-Agent Coordination

Flags can control:

- Which agent handles which domain
- Handoff protocols between agents
- Fallback chains when primary agent fails

### 4. Experimentation on Process

Run experiments on:

- Different commit workflows
- Documentation styles
- Memory management strategies
- Communication patterns

Measure which processes actually improve outcomes.

### 5. User Facing Features (Blog/Public)

When we ship user facing products:

- Beta features for early adopters
- A/B test content formats
- Personalize based on reader preferences
- Canary roll new designs

### 6. Kill Switches for Safety

Critical for AI systems:

- Instant disable of any agent capability
- Emergency stop without code deployment
- Gradual restoration after incidents

### 7. Infrastructure Migration

When moving to new:

- Model providers
- Hosting platforms
- Database systems

Feature flags enable gradual, reversible migration.

---

## PostHog Specific Features to Leverage

### Feature Flags

- Boolean and multivariate flags
- Percentage rollouts
- User targeting with properties
- Cohort targeting
- Local evaluation for speed
- Bootstrapping for initial page loads

### Experiments

- Built on feature flags
- Statistical significance calculation
- Goal metrics and secondary metrics
- Experiment results dashboard
- Bayesian and frequentist analysis

### Integration Points

- Web, mobile, and server SDKs
- Session replay correlation
- Funnel analysis with flag variants
- Retention analysis by flag exposure

---

## Implementation Checklist

### Immediate (This Week)

- [ ] Define naming convention for flags
- [ ] Create first operational kill switch
- [ ] Document flag ownership model
- [ ] Set up flag review in weekly process

### Short Term (This Month)

- [ ] Create first A/B experiment
- [ ] Implement agent behavior flag
- [ ] Set up stale flag alerts
- [ ] Document flag cleanup process

### Medium Term (This Quarter)

- [ ] Build progressive autonomy framework with flags
- [ ] Experiment on process improvements
- [ ] Create multi-agent coordination flags
- [ ] Establish flag debt metrics

---

## Sources

1. PostHog Feature Flags Documentation: https://posthog.com/docs/feature-flags
2. LaunchDarkly Feature Flags 101: https://launchdarkly.com/blog/what-are-feature-flags/
3. Unleash 11 Principles: https://docs.getunleash.io/guides/feature-flag-best-practices
4. Octopus 12 Commandments: https://octopus.com/devops/feature-flags/feature-flag-best-practices/
5. Statsig Technical Debt Management: https://www.statsig.com/perspectives/feature-flag-debt-management
6. LaunchDarkly 7 Mistakes: https://launchdarkly.com/blog/feature-flag-mistakes/
7. Martin Fowler on Feature Toggles: https://martinfowler.com/bliki/FeatureFlag.html

---

_Researched and compiled by [[Sivart]]. Issue #158._
