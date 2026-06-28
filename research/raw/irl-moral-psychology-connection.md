---
title: Inverse Reinforcement Learning Connection to Moral Psychology
created: 2026-06-28
updated: 2026-06-28
type: research
tags: [inverse-reinforcement-learning, moral-psychology, value-learning, ai-alignment, moral-foundations, rationality]
related:
  - conscience
  - principal-agent-theory
  - agent-identity
source: original
---

# Inverse Reinforcement Learning: Connection to Moral Psychology

## The Core Tension

IRL makes a critical assumption: **humans are approximately rational optimizers of some stable reward function.**

Moral psychology tells us this assumption is false.

This is not a technical detail. It is the fundamental problem at the intersection of value learning and moral psychology. If you apply IRL to human behavior, you are inferring the reward function that would produce the observed behavior IF the agent were a rational optimizer. But humans are not rational optimizers. So what does the inferred reward function actually mean?

---

## Problem 1: The Rationality Assumption

### What IRL Assumes

Standard IRL (Ng & Russell, MaxEnt IRL) assumes:
- The expert has a stable reward function R(s)
- The expert (approximately) maximizes expected cumulative reward
- Observed behavior reveals this reward function

### What Moral Psychology Shows

**Dual-Process Theory (Kahneman, Greene):**
- System 1: Fast, automatic, affective, heuristic-driven
- System 2: Slow, deliberative, effortful, controlled

Human moral judgment is dominated by System 1. People make rapid intuitive judgments, then use System 2 to rationalize them. The "reward function" driving System 1 is not the same as the "reward function" System 2 would endorse upon reflection.

**Implication for IRL:** Which system's reward function should you infer? If you watch someone make a snap moral judgment, you're observing System 1. If you ask them to deliberate about a trolley problem, you're observing System 2. These may produce different behaviors, hence different inferred reward functions.

**Moral Foundations Theory (Haidt):**
Moral judgment is driven by evolved "taste buds":
- Care/Harm
- Fairness/Cheating
- Loyalty/Betrayal
- Authority/Subversion
- Sanctity/Degradation
- Liberty/Oppression

These foundations are not learned through optimization. They are evolved priors. IRL assumes the reward function is learned from behavior, but moral foundations suggest some "rewards" are hardwired.

**Implication for IRL:** If moral foundations are innate, then the reward function is not purely learned. It is a combination of innate priors and learned features. Standard IRL does not account for this.

**Bounded Rationality and Biases:**
Humans exhibit:
- Loss aversion (prospect theory)
- Framing effects (same outcome, different description → different choice)
- Status quo bias
- Anchoring
- Availability heuristic

These are not noise around a rational optimum. They are systematic deviations. If you apply IRL to biased behavior, you infer a reward function that encodes the bias.

**Implication for IRL:** The inferred reward function R_inferred = R_true + Bias. You cannot separate the "true" values from the cognitive biases without additional assumptions.

---

## Problem 2: Stated vs. Revealed Preferences

### The Gap

**Stated preferences:** What people say they value (survey responses, explicit principles)
**Revealed preferences:** What people's behavior shows they value (choices, actions)

IRL infers revealed preferences. But in moral domains, stated and revealed preferences often diverge:

- People say they value honesty but lie when it's convenient
- People say they value equality but exhibit implicit bias
- People say they value long-term health but eat junk food
- Organizations say they value patient safety but optimize for throughput

### Why This Matters for Values Middleware

Your roadmap is about building a values middleware for AI systems. The hard problem is not "how do we encode stated values." The hard problem is "how do we reconcile stated values with revealed values."

IRL gives you the revealed values. But organizations will push back: "That's not what we believe. That's just what we do."

**The normative question:** Should the AI optimize for what the organization says it values, or what it actually does?

Moral psychology does not answer this. But it shows you the gap exists, and that the gap is systematic, not random.

---

## Problem 3: Moral Particularism

### The Challenge to Stable Reward Functions

**Moral particularism (Jonathan Dancy):** Moral reasoning is context-dependent. There are no stable principles that apply across all situations. What is right in one context may be wrong in another, even if the "features" of the situation are identical.

Example: Lying is generally wrong. But lying to protect someone from harm may be right. The "feature" of lying does not have a stable moral weight.

**Implication for IRL:** IRL assumes R(s) = wᵀφ(s), where the weight vector w is stable across all states. Moral particularism says this assumption is false. The weight vector itself is state-dependent: w = w(s).

This breaks the linear IRL framework. You would need a non-stationary reward function, which is much harder to learn from limited demonstrations.

---

## Problem 4: The Normative vs. Descriptive Problem

### What IRL Gives You (Descriptive)

IRL is a descriptive tool. It tells you what people actually optimize, not what they should optimize.

If you apply IRL to a society that practices slavery, you will infer a reward function that assigns positive value to slave ownership. This is descriptively accurate (it predicts behavior) but normatively monstrous.

### What Alignment Needs (Normative)

AI alignment is a normative project. We want to specify what AI systems SHOULD optimize, not just what humans happen to optimize.

**The is-ought gap (Hume):** You cannot derive an "ought" from an "is." You cannot derive normative values from descriptive observations of behavior.

**Implication for IRL:** IRL alone cannot solve the value alignment problem. It can tell you what people value, but it cannot tell you whether those values are good. You need a normative framework to evaluate the inferred reward function.

### Where Moral Philosophy Enters

Moral philosophy provides normative frameworks:
- **Utilitarianism:** Maximize aggregate welfare
- **Deontology:** Follow universalizable rules
- **Virtue ethics:** Cultivate moral character
- **Contractualism:** Act on principles no one could reasonably reject

These frameworks can be used to evaluate the reward functions inferred by IRL. But they do not emerge from IRL itself.

---

## Problem 5: Multi-Stakeholder Alignment

### When Humans Disagree

IRL assumes a single expert. But in the real world, different humans have different values:
- Doctors and patients disagree on treatment priorities
- Managers and employees disagree on workplace values
- Different cultures have different moral foundations

**Implication for IRL:** You cannot infer a single reward function. You infer a distribution over reward functions, one per stakeholder group.

**The aggregation problem:** How do you combine these into a single reward function for the AI? This is a social choice problem, and Arrow's impossibility theorem shows there is no perfect solution.

**Moral psychology insight:** Moral Foundations Theory shows that different groups weight the six foundations differently. Liberals emphasize Care and Fairness. Conservatives weight all six more evenly. These are not errors. They are stable differences in moral taste.

**Implication for values middleware:** You cannot build a "neutral" values layer. You must make normative choices about whose values to prioritize. IRL can reveal the landscape, but it cannot navigate it.

---

## Problem 6: Moral Uncertainty

### The Problem

**Moral uncertainty (MacAskill, Bykvist, Ord):** We do not know which moral theory is correct. Should we maximize utility? Follow rules? Cultivate virtues?

**Implication for IRL:** Even if you could perfectly infer human values, you would not know how to act on them under moral uncertainty. Should the AI optimize for what humans would want under utilitarianism? Deontology? Some weighted combination?

**Moral psychology insight:** People are not consistent moral theorists. They use different frameworks in different contexts. A doctor may be utilitarian about triage but deontological about lying.

**Implication for IRL:** The inferred "reward function" is not a coherent moral theory. It is a patchwork of context-dependent intuitions. You cannot directly use it as a guide for action under moral uncertainty.

---

## Problem 7: The Interpretability of Inferred Values

### The Black Box Problem

Deep IRL infers reward functions parameterized by neural networks. These are not interpretable. You cannot look at the network and say "this is what it values."

**Moral psychology insight:** Humans cannot introspect on their own value functions. When asked why they made a moral judgment, they confabulate reasons (Nisbett & Wilson, 1977). The "reasons" people give are post-hoc rationalizations, not the actual causes of their behavior.

**Implication for IRL:** Even if you perfectly infer the reward function, you cannot validate it by asking the expert "is this what you value?" The expert does not know.

This creates a verification problem. How do you know the inferred reward function is "correct" if the expert cannot introspect on their own values?

---

## Synthesis: What IRL Can and Cannot Do

### What IRL Can Do

1. **Reveal revealed preferences:** Show what behavior actually optimizes, as opposed to what people say they value
2. **Detect value drift:** Identify when an organization's behavior diverges from its stated values
3. **Quantify trade-offs:** Estimate how much weight people implicitly place on competing values
4. **Generate hypotheses:** Suggest candidate reward functions that can be evaluated normatively

### What IRL Cannot Do

1. **Distinguish true values from biases:** The inferred reward function conflates values and cognitive biases
2. **Resolve normative questions:** IRL is descriptive, not prescriptive
3. **Handle moral particularism:** IRL assumes stable reward functions, but morality may be context-dependent
4. **Aggregate conflicting values:** IRL cannot solve the social choice problem
5. **Provide interpretability:** Deep IRL produces black-box reward functions

### The Path Forward

IRL is a necessary but insufficient tool for value alignment. It must be combined with:

1. **Moral philosophy:** To provide normative evaluation of inferred values
2. **Moral psychology:** To understand the gap between revealed and stated preferences
3. **Deliberative democracy:** To aggregate conflicting values across stakeholders
4. **Interpretability research:** To make inferred reward functions auditable
5. **Moral uncertainty frameworks:** To act under uncertainty about the "right" values

---

## Concrete Implications for Values Middleware

### Design Principle 1: Separate Description from Prescription

The middleware should not conflate "what people do" with "what people should do." It should:
- Use IRL to infer revealed preferences (descriptive)
- Allow stakeholders to explicitly state normative principles (prescriptive)
- Make the gap between the two visible and auditable

### Design Principle 2: Model Moral Foundations as Features

Use Haidt's six foundations as the feature set φ(s) in IRL. Then:
- Infer the weight vector w for different stakeholder groups
- Visualize the moral profile of the organization
- Detect when AI behavior diverges from the inferred moral profile

### Design Principle 3: Support Multiple Reward Functions

Do not assume a single "true" reward function. Instead:
- Infer a distribution over reward functions (Bayesian IRL)
- Allow stakeholders to specify which reward function to optimize
- Provide tools for negotiating between conflicting values

### Design Principle 4: Build in Moral Uncertainty

The middleware should not assume moral certainty. It should:
- Support multiple moral frameworks (utilitarian, deontological, virtue-based)
- Allow stakeholders to specify their degree of moral uncertainty
- Implement decision procedures for acting under moral uncertainty (e.g., maximize expected choice-worthiness)

### Design Principle 5: Make Values Interpretable

The middleware should not produce black-box reward functions. It should:
- Use interpretable feature representations (moral foundations, organizational principles)
- Provide explanations for why certain behaviors are rewarded
- Allow stakeholders to audit and modify the inferred reward function

---

## References

### Moral Psychology
- Kahneman, D. (2011). *Thinking, Fast and Slow*
- Haidt, J. (2012). *The Righteous Mind*
- Greene, J. (2013). *Moral Tribes*
- Dancy, J. (2004). *Ethics Without Principles* (moral particularism)

### Moral Uncertainty
- MacAskill, W., Bykvist, K., & Ord, T. (2020). *Moral Uncertainty*

### IRL and Value Learning
- Russell, S. (2019). *Human Compatible*
- Ng, A. Y., & Russell, S. (2000). Algorithms for inverse reinforcement learning
- Ziebart, B. D., et al. (2008). Maximum entropy inverse reinforcement learning

### Social Choice and Aggregation
- Arrow, K. (1951). *Social Choice and Individual Values*
- Sen, A. (1970). *Collective Choice and Social Welfare*
