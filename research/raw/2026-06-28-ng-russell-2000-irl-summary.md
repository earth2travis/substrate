# Ng & Russell (2000): Algorithms for Inverse Reinforcement Learning — A Comprehensive Summary

**Citation:** Ng, A. Y., & Russell, S. J. (2000). Algorithms for inverse reinforcement learning. In *Proceedings of the Seventeenth International Conference on Machine Learning (ICML 2000)* (pp. 663–670). Morgan Kaufmann Publishers Inc.

---

## 1. Core Problem Formulation

### 1.1 The MDP Setting
The paper is situated within the standard Markov Decision Process (MDP) framework. An MDP is defined by the tuple $M = (\mathcal{S}, \mathcal{A}, P, \gamma, R)$, where:
- $\mathcal{S}$ is the state space (finite or continuous),
- $\mathcal{A}$ is the action space,
- $P(s' \mid s, a)$ is the transition dynamics,
- $\gamma \in [0, 1)$ is the discount factor,
- $R: \mathcal{S} \to \mathbb{R}$ is the reward function (state-dependent in the basic formulation).

In the *forward* reinforcement learning problem, the agent is given $R$ and must compute a policy $\pi^*$ maximizing the expected discounted cumulative reward:

$$V^\pi(s) = \mathbb{E}\left[ \sum_{t=0}^{\infty} \gamma^t R(s_t) \;\bigg|\; \pi, s_0 = s \right]$$

The Bellman equation for a fixed policy $\pi$ is:

$$V^\pi(s) = R(s) + \gamma \sum_{s' \in \mathcal{S}} P(s' \mid s, \pi(s)) V^\pi(s')$$

In vector form, this becomes $V^\pi = R + \gamma P^\pi V^\pi$, which yields the closed-form expression:

$$V^\pi = (I - \gamma P^\pi)^{-1} R$$

This linear relationship between the reward vector $R$ and the value vector $V^\pi$ under a *fixed* policy is the crucial algebraic fact that makes the entire LP-based approach possible.

### 1.2 The Inverse RL Problem
Ng and Russell invert the standard problem. Instead of optimizing a policy given a reward, they ask: **given an optimal policy $\pi^*$ (or trajectories sampled from it), recover the reward function $R$ that makes $\pi^*$ optimal.**

Why recover $R$ rather than simply imitate the policy? The authors argue that a reward function is often more **portable, interpretable, and robust** than a policy. If dynamics change, a policy may fail catastrophically, whereas a recovered reward can be re-optimized under the new dynamics. A reward also captures the *intent* or *objective* of the expert, generalizing beyond the demonstrated trajectories.

### 1.3 The Ambiguity Problem
The paper’s first theoretical insight is that this inversion is fundamentally ill-posed. There is a severe **non-uniqueness** (ambiguity) in the reward function consistent with a given policy. If $\pi^*$ is optimal under $R$, it is also optimal under:
- $cR$ for any constant $c > 0$ (positive scaling preserves the ordering of actions),
- $R + \Phi$, where $\Phi$ is a *potential-based shaping reward* (as shown in prior work by Ng, Harada, and Russell 1999), and
- more generally, any reward that merely preserves the ordinal ranking of action values at each state.

A policy reveals *which* action is best, but not *by how much*. Consequently, the set of reward functions for which a given policy is optimal forms a **non-empty convex cone** (or a polyhedral region under normalization). Exact recovery of the "true" reward is therefore impossible without additional assumptions. This observation frames the rest of the paper not as a search for the unique $R$, but as an algorithmic procedure for finding a *reasonable* $R$ from the feasible set.

---

## 2. Key Algorithms

### 2.1 Linear Programming for Small State Spaces
For finite MDPs where the transition matrix $P$ is known and the observed expert policy $\pi^*$ is deterministic, Ng and Russell derive a linear program (LP) over the reward variables $R(s)$.

Define the action-value function for taking action $a$ in state $s$ and thereafter following $\pi^*$ as:

$$Q^{\pi^*}(s, a) = R(s) + \gamma \sum_{s'} P(s' \mid s, a) V^{\pi^*}(s')$$

Because $V^{\pi^*} = (I - \gamma P^{\pi^*})^{-1} R$, both $V^{\pi^*}$ and $Q^{\pi^*}$ are **linear in $R$**. The optimality of $\pi^*$ implies that for every state $s$ and every alternative action $a \neq \pi^*(s)$:

$$Q^{\pi^*}(s, \pi^*(s)) \geq Q^{\pi^*}(s, a)$$

These are linear inequalities in the unknown reward vector $R$. To select a unique reward from the feasible polytope, the authors propose maximizing the margin by which the expert action outperforms all alternatives. Introducing slack variables $d_{s,a}$, the LP formulation is approximately:

$$\max_{R, \, d} \; \sum_{s \in \mathcal{S}} \sum_{a \neq \pi^*(s)} d_{s,a}$$

subject to:

$$Q^{\pi^*}(s, \pi^*(s)) - Q^{\pi^*}(s, a) \geq d_{s,a}, \quad \forall s \in \mathcal{S}, \; a \neq \pi^*(s)$$

$$d_{s,a} \geq 0, \quad \forall s, a$$

$$|R(s)| \leq R_{\max}, \quad \forall s \in \mathcal{S}$$

(The bound $|R(s)| \leq R_{\max}$ is a normalization constraint preventing the trivial infinite scaling of rewards.)

This LP finds the reward function that makes the demonstrated policy not merely optimal, but *uniquely* optimal by the widest possible margin. It is a primal contribution: the first tractable, polynomial-time algorithm for reward recovery in finite MDPs.

### 2.2 Feature-Based Approach for Large and Continuous Spaces
Tabular reward functions are impossible to specify when $\mathcal{S}$ is large or continuous. Ng and Russell extend the LP by assuming the reward is a linear combination of known basis features:

$$R(s) = w^T \phi(s) = \sum_{i=1}^{k} w_i \phi_i(s)$$

where $\phi(s) \in \mathbb{R}^k$ is a fixed feature vector and $w \in \mathbb{R}^k$ is the unknown weight vector. Because $V^{\pi^*}$ is linear in $R$, and $R$ is now linear in $w$, the value function under the expert policy is also linear in $w$:

$$V^{\pi^*}(s) = \sum_{s'} (I - \gamma P^{\pi^*})^{-1}_{s,s'} w^T \phi(s') = w^T \psi(s)$$

where $\psi(s)$ is an effective feature vector at state $s$ induced by the policy dynamics. Substituting into the optimality constraints yields linear inequalities in $w$ rather than $R$. The LP is now over the $k$-dimensional weight space, making the method scalable to high-dimensional and continuous domains provided the basis functions are chosen appropriately.

This formulation foreshadows the **feature expectation** perspective later formalized by Abbeel and Ng (2004). The discounted cumulative feature count under a policy is:

$$\mu(\pi) = \mathbb{E}\left[ \sum_{t=0}^{\infty} \gamma^t \phi(s_t) \;\bigg|\; \pi \right]$$

and the value of any policy can be expressed as $V^\pi = w^T \mu(\pi)$. In this view, the IRL problem reduces to finding a weight vector $w$ such that the expert policy achieves a higher feature-expectation inner product than competing policies.

### 2.3 Bayesian Formulation
Recognizing that a point estimate of $R$ discards valuable uncertainty information, the authors sketch a Bayesian framework. They place a prior $P(R)$ over reward functions and model the likelihood $P(\pi^* \mid R)$ as an indicator function that is $1$ when $\pi^*$ is optimal under $R$ and $0$ otherwise. The posterior is:

$$P(R \mid \pi^*) \propto P(\pi^* \mid R) \, P(R)$$

Because the likelihood is a step function (the policy is either optimal or not), the posterior is simply the prior restricted to the feasible polytope of rewards consistent with the demonstrations. Although exact posterior computation is intractable for arbitrary priors, this formulation was conceptually important: it treats the reward as a latent variable to be inferred, and it naturally accommodates regularization via the prior (e.g., preferring sparse or smooth rewards). This Bayesian perspective directly influenced later work by Ramachandran and Amir (2007) on Bayesian IRL.

---

## 3. Theoretical Contributions

### 3.1 Exact Recovery is Impossible in General
The paper provides a formal proof that the reward function cannot be uniquely determined from an optimal policy alone. The set of reward functions consistent with a given optimal policy $\pi^*$ is a **convex polyhedral cone** (after accounting for the trivial degree of freedom $cR$). Because the feasible set has dimensionality greater than zero, exact recovery is impossible without additional constraints.

### 3.2 Conditions Under Which Recovery is Possible
Despite the general impossibility result, the authors discuss restricted conditions under which uniqueness can be achieved:
- **Restricting the reward class:** If the reward is known to lie in a specific low-dimensional subspace (e.g., a linear combination of a small, known feature set), the policy constraints may become full-rank in the reduced space, allowing unique recovery of the weights.
- **Structural assumptions:** If the reward is known to be sparse (non-zero only in a small subset of states) or if the dynamics are sufficiently rich, the feasible polytope may shrink to a single point.
- **Observing the value function:** If one observes not only the policy but the *actual numerical values* of $V^{\pi^*}(s)$, the reward becomes identifiable (up to a constant) because the Bellman equations are linear and invertible. In practice, however, one rarely observes values, only actions.

### 3.3 Optimality and Reward Uniqueness
The authors formalize the relationship between policy optimality and reward uniqueness. A policy encodes only *ordinal* information about the underlying utility: it tells us that $\pi^*(s)$ is preferred to every other action $a$, but not the cardinal strength of that preference. Any reward function that preserves this ordering is a valid solution. This insight explains why the LP formulation requires an auxiliary objective (margin maximization) to break the symmetry of the feasible set. The choice of objective function is not merely a computational convenience; it is an epistemological necessity.

---

## 4. Experimental Results

The experiments are conducted in a **discrete grid world** (e.g., a $5 \times 5$ grid), where an agent navigates to a goal state. The true reward is typically positive at the goal and zero elsewhere (or negative in obstacle states), and the transition dynamics are known to the learner.

**What was demonstrated:**
- **Reward Recovery:** The LP algorithm successfully recovers *a* reward function that rationalizes the expert policy. Importantly, the recovered reward is not necessarily identical to the true reward used to generate the demonstrations—confirming the theoretical ambiguity result. For instance, the LP may assign non-zero rewards to intermediate states that are informationally equivalent to the goal under the specific dynamics.
- **Policy Reconstruction:** The recovered reward, when plugged into a standard MDP solver, yields a policy that matches the expert demonstrations. This validates the functional utility of the method even when the true reward is not recovered.
- **Feature-Based Scaling:** The authors demonstrate that the feature-based extension can recover weights in spaces where a tabular representation would be infeasible.
- **Sensitivity:** The experiments illustrate that without the margin-maximization objective, the LP may return degenerate or uninformative reward functions (e.g., near-zero rewards everywhere). The margin objective acts as a crucial regularizer.

---

## 5. Limitations and Assumptions

The paper is explicit about its assumptions, many of which have motivated subsequent research:

- **Known Transition Dynamics:** The LP requires full knowledge of $P(s' \mid s, a)$. This is a strong limitation; many real-world domains have unknown or partially known dynamics. Later work (e.g., apprenticeship learning by Abbeel & Ng, 2004) addresses this by working directly from trajectories without an explicit model.
- **Exactly Optimal Demonstrations:** The constraints assume that the observed policy is strictly optimal. Human or real-world demonstrations are rarely exactly optimal; they are noisy, stochastic, and context-dependent. This limitation was later addressed by probabilistic IRL frameworks, notably **Maximum Entropy IRL** (Ziebart et al., 2008), which models suboptimal behavior via a Boltzmann distribution over actions.
- **Deterministic Expert Policy:** The basic LP assumes a deterministic expert. While the formulation can be extended, stochastic policies complicate the linear constraint structure.
- **Finite Action Spaces:** The LP scales with $|\mathcal{S}| \times |\mathcal{A}|$ constraints. For very large action spaces, enumeration becomes intractable.
- **State-Only Rewards:** The basic formulation assumes $R(s)$ rather than $R(s, a)$. While the extension to state-action rewards is conceptually straightforward, it increases the number of parameters.
- **Hand-Engineered Features:** The feature-based method requires a human to specify the basis functions $\phi(s)$. Poor feature choices lead to poor reward approximations, a limitation that persists until the advent of deep IRL methods (e.g., Wulfmeier et al., 2015), which learn features end-to-end.
- **Computational Complexity:** Inverting $(I - \gamma P^{\pi^*})$ requires $O(|\mathcal{S}|^3)$ time in the worst case, limiting the tabular LP to moderate-sized MDPs.

---

## 6. Impact on the Field

Ng & Russell (2000) is a foundational paper that established the algorithmic and conceptual framework for modern inverse reinforcement learning. Its impact can be traced along several lines:

- **Formalization of the IRL Problem:** By casting reward recovery as a computational problem within the MDP framework, the paper moved beyond the earlier economics and control-theory literature (where similar problems were called "inverse optimal control" or "structural estimation"). It provided the vocabulary and notation that the field still uses today.
- **Apprenticeship and Imitation Learning:** The paper directly enabled the apprenticeship learning paradigm. Abbeel and Ng (2004) built on the feature-based formulation to show that an agent could learn from demonstrations by matching feature expectations, without ever recovering an explicit reward. This lineage continues through modern imitation learning and GAIL (Ho & Ermon, 2016).
- **Maximum Entropy and Probabilistic IRL:** The awareness of reward ambiguity in Ng & Russell (2000) motivated later work to resolve ambiguity via probabilistic models. Ziebart et al. (2008) introduced MaxEnt IRL, which selects the reward that maximizes the entropy of the trajectory distribution subject to feature matching. This became the dominant approach for structured prediction and trajectory forecasting.
- **Deep Inverse RL:** The feature-based extension prefigures deep IRL, where neural networks replace the hand-specified basis functions $\phi(s)$. The linearity of the value function in the reward (and thus in the weights) remains a useful structural property in certain deep formulations.
- **AI Alignment and Reward Modeling:** The paper’s central premise—that rewards are latent variables to be inferred from behavior—resonates deeply with modern AI alignment. Techniques like **RLHF (Reinforcement Learning from Human Feedback)** and reward modeling (Christiano et al., 2017) are conceptual descendants of inverse RL. They infer a reward function from human preferences (a form of demonstrated optimality) and then optimize a policy against it.
- **Inverse Optimal Control in Robotics:** The LP and feature-based methods were adapted for robotics and autonomous driving, where recovering a cost function from expert demonstrations is often more robust than cloning a control policy.

In retrospect, the paper’s most enduring contribution is the **formal articulation of the ambiguity problem**. By proving that the reward is underdetermined by the policy, Ng and Russell shifted the community’s focus from naive reward recovery to principled ways of selecting among feasible rewards—whether through margin maximization, Bayesian priors, maximum entropy, or feature expectation matching. These algorithmic strategies remain the pillars of the field today.

---

**Summary for the Knowledge Base:** Ng & Russell (2000) is the seminal algorithmic paper on inverse reinforcement learning. It formalizes the problem within finite MDPs, proves that exact reward recovery is impossible due to a fundamental ambiguity (the feasible reward set is a convex cone), and provides three practical algorithmic responses: a linear program for finite spaces, a feature-based linear extension for large/continuous spaces, and a Bayesian framework for representing uncertainty. Experiments in grid-world domains confirm that while the true reward may not be recovered, a functionally equivalent reward can be found. The paper’s assumptions—known dynamics, optimal demonstrations, and finite actions—set the agenda for two decades of subsequent research, from apprenticeship learning and MaxEnt IRL to deep inverse RL and reward modeling in AI alignment.
