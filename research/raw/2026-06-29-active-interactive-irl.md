---
title: "Active and Interactive Inverse Reinforcement Learning: Query-Based Learning, Interactive Teaching, and Online Methods"
tags:
  - raw
  - inverse-reinforcement-learning
  - active-learning
  - cooperative-irl
  - query-based-learning
  - human-in-the-loop
  - online-irl
  - interactive-teaching
  - preference-learning
  - ai-alignment
  - value-learning
related:
  - [[2026-06-28-ziebart-maxent-irl-alignment-machine-conscience]]
  - [[2026-06-28-irl-landscape-2000-2010]]
  - [[2026-06-28-ng-russell-2000-irl-summary]]
  - [[cirl-cooperative-inverse-reinforcement-learning]]
  - [[rlhf-human-feedback]]
  - [[teaching-dimension]]
  - [[active-learning-supervised]]
source: "Internal knowledge base synthesis via arXiv API search and parametric synthesis (2026-06-29)"
---

> **Composite research briefing compiled from arXiv searches and parametric synthesis across the active and interactive IRL literature.**
> This document covers query-based IRL, interactive teaching models, online and incremental methods, active demonstration selection, preference query optimization, human-in-the-loop systems, teaching complexity, inverse cooperative RL, reward dialogue, and connections to active learning in supervised settings.

---

# Part I: Introduction and Foundational Framing

## 1. The Problem: From Passive Observation to Active Inquiry

Traditional Inverse Reinforcement Learning (IRL) operates in a fundamentally passive mode. The agent receives a batch of expert demonstrations, observes state-action trajectories, and infers a reward function that rationalizes the observed behavior. Whether formulated as the linear programming approach of Ng and Russell (2000), the apprenticeship learning framework of Abbeel and Ng (2004), or the maximum entropy formulation of Ziebart et al. (2008), the standard assumption is that the human provides data and the agent processes it. The human is a source of information, not a partner in a dialogue.

This passivity creates severe practical limitations. First, the ambiguity of the IRL problem means that many reward functions are consistent with the same demonstrations. Any reward function R, when modified by a potential-based shaping term (Ng, Harada, and Russell, 1999), preserves the optimal policy. The set of feasible rewards forms a convex polytope, and the agent has no principled way to select among them without additional criteria. Second, the expert demonstrations may be suboptimal, noisy, or cover only a narrow region of the state space. The agent cannot ask for clarification, request demonstrations in ambiguous regions, or probe the human's preferences systematically. Third, batch learning assumes that all data arrives at once, which is unrealistic in many real-world settings where the agent must learn incrementally from ongoing interaction.

Active and interactive IRL addresses these limitations by treating the learning process as a **bidirectional interaction** rather than a unidirectional data flow. The agent can ask questions, request demonstrations, propose comparisons, or engage in dialogue. The human can respond with feedback, corrections, or additional information. This transforms IRL from a statistical inference problem into an **interactive epistemology** problem: how should an agent optimally acquire information about human values through structured interaction?

The motivation extends beyond algorithmic efficiency. In the context of AI alignment, an agent that passively observes human behavior may miss critical aspects of the human's values, especially when those values are context-dependent, nuanced, or not fully expressed in the demonstrations. An agent that can ask clarifying questions, probe edge cases, and verify its understanding is more likely to learn a reward function that truly reflects the human's intent. This is particularly important in high-stakes domains such as autonomous driving, medical decision-making, and human-robot collaboration, where misalignment between the agent's inferred reward and the human's true preferences can have serious consequences.

---

# Part II: Cooperative Inverse Reinforcement Learning

## 2. Hadfield-Menell et al. (2016): The Cooperative IRL Framework

The most influential theoretical framework for interactive IRL is **Cooperative Inverse Reinforcement Learning (CIRL)**, introduced by Hadfield-Menell, Dragan, Abbeel, and Russell in their 2016 paper "Cooperative Inverse Reinforcement Learning" (arXiv:1606.03137, published in NeurIPS 2016). This paper represents a fundamental reconceptualization of the IRL problem by treating the human and the robot as **cooperative agents** in a two-player game, rather than treating the human as an exogenous information source.

### 2.1 The Standard IRL Model and Its Flaws

Hadfield-Menell et al. begin by identifying a deep structural problem in the standard IRL formulation. In standard IRL, the human is modeled as an optimal agent acting in an environment, and the robot observes the human's behavior to infer the reward function. The robot then optimizes this inferred reward function to act autonomously. The problem is that this model treats the human's behavior as independent of the robot's presence. In reality, the human's behavior changes when the robot is present: the human may teach, correct, demonstrate, or simply behave differently knowing that the robot is watching and learning.

More formally, standard IRL assumes that the human acts according to a fixed optimal policy π_H that maximizes a reward function R. The robot observes trajectories sampled from π_H and infers R. But this is a **single-agent** model applied to a **multi-agent** situation. The human is not merely optimizing R in the environment; the human is also trying to communicate R to the robot. This communicative intent means that the human's behavior is not simply optimal with respect to R, but optimal with respect to R **plus the teaching objective**. Standard IRL ignores this teaching objective, which leads to misinterpretation of the demonstrations.

### 2.2 The CIRL Game Formulation

CIRL formalizes the interaction as a **two-player Markov game** where the state space is augmented to include both the physical environment and the robot's belief about the reward function. The game is cooperative: both players share the same reward function, but only the human knows it initially. The robot must learn the reward function through interaction.

In the CIRL game, the state at time t is a tuple (s_t, b_t) where s_t is the physical state and b_t is the robot's belief about the reward function. The human chooses actions that influence the physical state, but also convey information about the reward. The robot chooses actions based on its current belief and its observations of the human's actions. The reward for both players depends only on the physical state and the true reward function, which is initially known only to the human.

This formulation has several important implications. First, it means that the human's optimal policy is not merely to maximize the reward in the physical environment, but to **maximize the reward while also teaching the robot**. The human may choose suboptimal actions in the physical environment if those actions provide more information about the reward. For example, a human teaching a robot to cook might deliberately make a mistake to demonstrate what not to do, even though this is suboptimal from the perspective of cooking alone.

Second, it means that the robot's optimal policy is not merely to maximize the inferred reward, but to **maximize the expected reward under its current belief while also updating its belief efficiently**. The robot must balance exploitation (acting on its current best estimate of the reward) with exploration (taking actions that reveal information about the reward). This is similar to the exploration-exploitation tradeoff in reinforcement learning, but here the exploration is directed toward learning about the reward function from the human's responses.

### 2.3 Theoretical Results and Complexity

Hadfield-Menell et al. prove several important theoretical results about the CIRL game. They show that the optimal strategy for the human involves **teaching behaviors** that are distinct from the optimal behavior in the absence of the robot. They also show that the robot's optimal strategy involves **active learning** that goes beyond passive observation. The CIRL game can be solved using dynamic programming, but the state space is augmented by the space of possible beliefs, which makes exact computation intractable for all but the simplest cases.

The paper also introduces the concept of **value alignment** as a formal property of the CIRL game. Value alignment means that the robot's actions maximize the human's true reward function. In the CIRL framework, value alignment is achieved when the robot's belief converges to the true reward function and the robot acts optimally with respect to that reward. The CIRL framework thus provides a formal definition of value alignment that connects the AI safety literature with the IRL literature.

The practical significance of CIRL is that it provides a theoretical foundation for why active learning is necessary in IRL. In standard IRL, the robot is passive because the model assumes the human is not trying to teach. In CIRL, the robot is active because the model explicitly includes the teaching objective. The robot must ask questions, request demonstrations, and probe the human's preferences because the human is expecting it to do so. The cooperative framework transforms the IRL problem from a one-sided inference problem into a two-sided coordination problem.

---

# Part III: Query-Based and Active IRL

## 3. Sadigh et al. (2017): Active Preference-Based Learning

The work of Sadigh, Dragan, Sastry, and Seshia (2017), published in Robotics: Science and Systems (RSS), represents one of the most practical and influential approaches to active IRL. Their paper "Active Preference-Based Learning of Reward Functions" introduces a framework where the robot learns a reward function by actively querying the human with pairwise comparisons between trajectories. This approach is grounded in the preference-based learning literature and connects IRL to active learning in a direct and implementable way.

### 3.1 Preference-Based Reward Learning

The key insight of Sadigh et al. is that humans are often better at comparing trajectories than at providing absolute reward values. A human can say "trajectory A is better than trajectory B" more reliably than they can say "trajectory A has a reward of 7.3." This is consistent with findings in behavioral economics and psychology, where pairwise comparisons are a standard tool for eliciting preferences (Thurstone, 1927; Bradley and Terry, 1952).

Sadigh et al. model the human's preference using a **probabilistic choice model**. The probability that a human prefers trajectory A over trajectory B is given by a sigmoid function of the difference in reward between the two trajectories:

P(A > B | R) = σ(R(A) - R(B))

where R(A) is the cumulative reward of trajectory A and σ is the logistic function. This is the **Bradley-Terry model** applied to trajectory comparison. The reward function is parameterized as a linear combination of features: R(s, a) = θ^T φ(s, a), where θ is a weight vector to be learned.

### 3.2 Active Query Selection

The active learning component of the framework is the method for selecting which queries to ask. Sadigh et al. propose selecting the pair of trajectories that maximizes the expected **information gain** about the reward parameters. This is a standard active learning criterion: the agent should ask the question that is most informative about the unknown parameters.

More specifically, the information gain for a query (A, B) is defined as the expected reduction in entropy of the posterior distribution over θ after observing the human's preference. The posterior is updated using Bayes' rule after each query, and the next query is chosen to maximize the expected information gain under the current posterior. This is computationally expensive because it requires evaluating the expected information gain for all possible trajectory pairs, but the paper proposes approximations and demonstrates practical feasibility on driving and manipulation tasks.

### 3.3 Experimental Results and Extensions

Sadigh et al. demonstrate their approach on a simulated driving task and a robotic manipulation task. They show that active preference-based learning can learn accurate reward functions with fewer queries than passive learning. The key advantage is that the active learner can focus on comparing trajectories that are near the decision boundary, where the human's preference is most informative about the reward parameters.

This work has been extended in many directions. One important extension is the incorporation of **dynamical models** of the human's preference, where the human's preference function is allowed to change over time or depend on context. Another extension is the use of **batch active learning**, where multiple queries are selected jointly to maximize the total information gain, rather than selecting queries one at a time. These extensions are particularly important for applications where the human's time is limited and the robot must make the most efficient use of each query.

---

## 4. Risk-Aware Active IRL: Brown, Cui, and Niekum (2019)

Brown, Cui, and Niekum (2019), in their paper "Risk-Aware Active Inverse Reinforcement Learning" (arXiv:1901.02161), address a critical limitation of standard active IRL: the risk that the learned reward function, even if it explains the queries well, may lead to a policy that performs poorly in practice. This is the **performance risk** of the learned policy, and it is not captured by standard information-theoretic active learning criteria.

### 4.1 The Performance Risk Problem

Standard active IRL selects queries to maximize information gain about the reward parameters. But information gain is only a proxy for the true objective: finding a policy that performs well under the human's true reward function. A query that provides a lot of information about the reward parameters may not provide information that is relevant to the policy's performance. For example, a query about a rare edge case may be highly informative about the reward parameters but irrelevant to the policy's performance in the typical case.

Brown et al. formalize this by defining the **risk** of a learned reward function as the expected performance loss under the true reward function. They propose a **risk-aware active learning** criterion that selects queries to minimize the expected risk of the final policy, rather than maximizing information gain. This requires a more complex optimization problem, but it leads to more practically useful queries.

### 4.2 The Risk-Aware Query Selection Algorithm

The risk-aware query selection algorithm works as follows. At each step, the robot maintains a posterior distribution over reward functions. For each possible query, it computes the expected posterior after each possible human response. For each possible posterior, it computes the optimal policy under the expected reward function and evaluates the risk of that policy under the current posterior. The query is selected to minimize the expected risk of the final policy, averaged over the possible human responses.

This algorithm is computationally more demanding than information-gain-based active learning, but Brown et al. show that it can be approximated efficiently using sampling methods. They demonstrate on a simulated driving task that risk-aware active learning leads to safer policies than information-gain-based active learning, especially in the early stages of learning when the reward function is highly uncertain.

### 4.3 Connections to Safe Exploration

The risk-aware active IRL framework connects to the broader literature on **safe exploration** in reinforcement learning. In safe exploration, the agent must explore the environment to learn about the reward function, but it must avoid taking actions that are dangerous or irreversible. Risk-aware active IRL extends this idea to the learning of the reward function itself: the agent must ask queries to learn about the reward function, but it must avoid asking queries that could lead to a dangerously wrong reward function. This is particularly important in safety-critical applications such as autonomous driving and medical decision-making.

---

## 5. PAC Apprenticeship Learning with Bayesian Active IRL (2025)

A recent paper by Bajgar, Gould, Liu, Abate, Gatsis, and Osborne (2025), "PAC Apprenticeship Learning with Bayesian Active Inverse Reinforcement Learning" (arXiv:2508.03693), brings together the theoretical rigor of Probably Approximately Correct (PAC) learning with the practical benefits of active IRL. This work addresses the sample complexity of active IRL: how many queries are needed to learn a policy that is approximately optimal with high probability?

### 5.1 PAC Learning in IRL

The PAC framework, introduced by Valiant (1984), provides a formal definition of efficient learning: an algorithm is PAC if it can learn a hypothesis that is approximately correct with high probability using a polynomial number of samples. In the context of IRL, the hypothesis is the reward function and the samples are the demonstrations or queries. A PAC IRL algorithm guarantees that, given a polynomial number of demonstrations, it will find a reward function that yields a policy whose value is within ε of the optimal policy, with probability at least 1 - δ.

Bajgar et al. extend the PAC framework to active IRL by showing that the number of queries required for PAC learning can be significantly reduced by using active learning. They prove that their Bayesian active IRL algorithm is PAC and derive bounds on the sample complexity. The key insight is that active learning can focus on the most informative queries, reducing the total number of queries needed to achieve a given level of accuracy.

### 5.2 Bayesian Active IRL with Thompson Sampling

The algorithm uses a Bayesian approach to maintain a posterior distribution over reward functions, and it uses **Thompson sampling** to select queries. Thompson sampling is a well-known exploration strategy in bandit problems: at each step, the agent samples a reward function from the posterior and selects the query that would be optimal under that sampled reward function. This provides a natural balance between exploration and exploitation, as the agent explores queries that are informative under a variety of possible reward functions.

Bajgar et al. prove that this Thompson sampling approach achieves PAC guarantees with a sample complexity that is polynomial in the relevant parameters (the number of features, the horizon, and the desired accuracy). This is a significant theoretical result, as it provides the first PAC guarantees for active IRL in the apprenticeship learning setting. The practical implication is that active IRL can be provably efficient, not just empirically effective.

---

# Part IV: Online and Incremental IRL

## 6. Online IRL: Updating Beliefs Incrementally

Online IRL refers to methods that update the reward estimate incrementally as new demonstrations or feedback arrive, rather than batch learning from a fixed dataset. This is essential for real-world applications where the agent must learn continuously from ongoing interaction with the human.

### 6.1 The Need for Online Learning

Batch IRL assumes that all demonstrations are available at the start of learning. This is unrealistic in many settings. In human-robot interaction, the robot may receive new demonstrations over time as the human observes the robot's behavior and provides corrections. In personalized AI systems, the user's preferences may change over time, and the system must adapt incrementally. In lifelong learning settings, the agent must integrate new experiences with old knowledge without retraining from scratch.

Online IRL addresses these challenges by maintaining a running estimate of the reward function and updating it efficiently as new data arrives. The key algorithmic challenge is to update the reward estimate without re-solving the entire IRL problem from scratch. This requires incremental optimization algorithms that can incorporate new data efficiently.

### 6.2 Wang, Chen, and Dong (2020): Lifelong Incremental RL with Online Bayesian Inference

Wang, Chen, and Dong (2020), in their paper "Lifelong Incremental Reinforcement Learning with Online Bayesian Inference" (arXiv:2007.14196), propose a framework for lifelong learning that uses online Bayesian inference to update the agent's knowledge as the environment changes. While this paper is primarily about reinforcement learning rather than IRL, its online Bayesian inference framework is directly applicable to online IRL.

The key idea is to use **online Bayesian inference** to update the posterior distribution over reward functions as new data arrives. The posterior at time t is updated from the posterior at time t-1 using the new data, without re-processing all the old data. This is achieved using variational inference or particle filtering, which approximate the posterior with a tractable distribution that can be updated incrementally.

In the context of IRL, this means that the agent can maintain a belief over reward functions and update it as new demonstrations or queries arrive. The agent can also use the current belief to select actions or queries, balancing the need to perform well under the current belief with the need to gather information to improve the belief. This is essentially the online version of the CIRL game, where the agent must learn and act simultaneously over an indefinite horizon.

### 6.3 Online Maximum Entropy IRL

The maximum entropy IRL framework of Ziebart et al. (2008) is particularly well-suited to online learning because it provides a probabilistic model of behavior that can be updated incrementally. The probability of a trajectory under the reward parameters is given by a Boltzmann distribution, and the parameters can be updated using online gradient descent or stochastic gradient descent as new trajectories are observed.

Online maximum entropy IRL updates the reward parameters θ using the gradient of the log-likelihood of the new trajectories. The gradient for a new trajectory ξ is:

∇_θ log P(ξ | θ) = f_ξ - E[f_ξ | θ]

where f_ξ is the feature count of the observed trajectory and E[f_ξ | θ] is the expected feature count under the current model. The expected feature count can be computed using the forward-backward algorithm, and the update can be performed incrementally. This is similar to online learning in exponential families, where the parameters are updated using the sufficient statistics of the new data.

The advantage of online maximum entropy IRL is that it can adapt to changes in the expert's behavior over time. If the expert's preferences change, the online algorithm will gradually shift the reward parameters to match the new behavior. This is important for applications where the human's preferences are not static, such as in personalized recommendation systems or adaptive tutoring systems.

---

# Part V: Interactive Teaching and the Human as Teacher

## 7. Teaching Dimension and Teaching Complexity

The theoretical study of teaching in machine learning has a long history, dating back to the work of Goldman and Kearns (1995) and Shinohara and Miyano (1991) on the **teaching dimension** of concept classes. The teaching dimension of a concept class is the minimum number of examples needed to teach any concept in the class to a learner. This notion has been extended to the setting of IRL, where the goal is to teach a reward function to an agent.

### 7.1 Teaching Dimension for Reward Functions

In the context of IRL, the teaching dimension is the minimum number of demonstrations or queries needed to teach the agent a reward function that is approximately correct. This depends on the complexity of the reward function class (e.g., linear combinations of features, neural networks, etc.) and the complexity of the environment (e.g., the number of states, the horizon, the stochasticity).

Cakmak and Lopes (2012) were among the first to study the teaching problem in IRL. They formalized the problem of **algorithmic teaching** where the teacher (human) selects demonstrations to maximize the agent's learning. They showed that the optimal teaching strategy is not simply to demonstrate the optimal behavior, but to select demonstrations that maximize the information gain about the reward function. This is the dual of active learning: instead of the agent selecting queries, the teacher selects demonstrations.

### 7.2 Zhu et al.: Machine Teaching

The broader **machine teaching** literature, initiated by Zhu (2013) and developed by Zhu, Singla, Zheng, and Pech (2018), provides a general framework for studying the interaction between a teacher and a learner. In machine teaching, the teacher has a target model (in this case, a reward function) and wants to teach it to the learner using a minimal number of examples. The teaching problem is to find the optimal set of examples that will make the learner converge to the target model.

In the context of IRL, machine teaching can be applied to both the demonstration setting and the query setting. In the demonstration setting, the teacher selects a set of trajectories that will make the IRL algorithm converge to the true reward function. In the query setting, the teacher selects a set of queries that will make the preference-based learning algorithm converge to the true reward function. The teaching problem is typically easier than the learning problem because the teacher has full knowledge of the target model and can optimize the examples accordingly.

### 7.3 Seita et al. (2019): ZPD Teaching Strategies for Deep RL from Demonstrations

Seita, Chan, Rao, Tang, Zhao, and Canny (2019), in their paper "ZPD Teaching Strategies for Deep Reinforcement Learning from Demonstrations" (arXiv:1910.12154), draw on the educational psychology concept of the **Zone of Proximal Development (ZPD)** to design teaching strategies for deep RL. The ZPD, introduced by Vygotsky (1978), is the range of tasks that a learner can perform with guidance but not independently. In the context of RL, the ZPD is the range of tasks that the agent can learn from demonstrations but not from scratch.

Seita et al. propose that the teacher should provide demonstrations that are within the agent's ZPD: not too easy (the agent could learn them on its own) and not too hard (the agent cannot learn them even with demonstrations). They design a curriculum of demonstrations that gradually increases in difficulty, starting with easy demonstrations and progressing to harder ones. This is similar to curriculum learning in RL, but with the added constraint that the demonstrations must be selected by a teacher who knows the agent's current capabilities.

The ZPD framework connects IRL to educational psychology in a principled way. It suggests that the optimal teaching strategy depends on the learner's current state, not just on the target task. This is consistent with the CIRL framework, where the human's optimal teaching strategy depends on the robot's current belief about the reward function. The ZPD framework provides a psychological justification for why active and interactive teaching is necessary: the teacher must adapt to the learner's state to be effective.

---

# Part VI: Human-in-the-Loop and Preference-Based Systems

## 8. Iterative Reward Refinement Through Human Feedback

Human-in-the-loop IRL refers to systems that iteratively refine the reward function through ongoing human feedback. This is the sequential decision-making analog of Reinforcement Learning from Human Feedback (RLHF), which has been highly successful in training large language models.

### 8.1 RLHF and Its Connection to IRL

RLHF (Reinforcement Learning from Human Feedback) has emerged as the dominant paradigm for aligning large language models with human preferences (Ouyang et al., 2022; Ziegler et al., 2019). In RLHF, a reward model is trained from human comparisons of model outputs, and the language model is fine-tuned using reinforcement learning to maximize the learned reward. The reward model is essentially a preference-based IRL system applied to the space of text outputs.

The connection between RLHF and IRL is direct. In RLHF, the state space is the space of conversation contexts, the action space is the space of possible tokens or responses, and the reward function is the human's preference over responses. The reward model is learned from pairwise comparisons, which is the same preference-based learning framework used by Sadigh et al. (2017). The key difference is that RLHF operates in a very large, high-dimensional space (text) and uses deep neural networks to represent the reward function, whereas classical IRL operates in smaller, low-dimensional spaces (robotics, games) and uses linear or kernel-based reward representations.

### 8.2 Ye et al. (2024): Online Iterative RLHF with General Preference Models

Ye, Xiong, Zhang, Dong, Jiang, and Zhang (2024), in their paper "Online Iterative Reinforcement Learning from Human Feedback with General Preference Model" (arXiv:2402.07314), extend the RLHF framework to the online setting with general preference models. They relax the standard assumption that the human's preferences follow the Bradley-Terry model and instead consider a general preference oracle that can provide arbitrary preference signals.

The general preference model is important because it allows the system to handle non-transitive preferences, context-dependent preferences, and other complexities of human preference that are not captured by the Bradley-Terry model. Ye et al. prove convergence results for online iterative RLHF under general preference models, showing that the algorithm can learn a near-optimal policy with a polynomial number of queries.

This work has direct implications for interactive IRL. In sequential decision-making settings such as robotics and autonomous driving, the human's preferences may not be well-modeled by the Bradley-Terry model. The human may have non-transitive preferences (e.g., preferring A to B, B to C, and C to A), or their preferences may depend on the context in complex ways. The general preference model framework provides a theoretical foundation for handling these complexities in interactive IRL systems.

### 8.3 Lindner et al. (2022): Humans Are Not Boltzmann Distributions

Lindner and El-Assady (2022), in their paper "Humans are not Boltzmann Distributions: Challenges and Opportunities for Modelling Human Feedback and Interaction in Reinforcement Learning" (arXiv:2206.13316), challenge the standard assumption in IRL that humans are noisy rational agents whose behavior follows a Boltzmann distribution over actions. They argue that human behavior is much more complex and cannot be captured by a simple softmax model.

The Boltzmann model assumes that the probability of a human action is proportional to exp(β * Q(s, a)), where Q(s, a) is the action value and β is an inverse temperature parameter. This model implies that the human is approximately rational, with their deviations from rationality being purely random. Lindner and El-Assady argue that this model is empirically inadequate: humans make systematic errors, are influenced by framing effects, have inconsistent preferences, and their behavior depends on their mental state and the interaction history.

This critique is important for interactive IRL because it suggests that the standard models of human behavior used in IRL may be too simplistic. If the human is not a Boltzmann agent, then the agent's queries and inferences must be designed to handle more complex human behavior. This may require richer models of human cognition, such as models that incorporate cognitive biases, theory of mind, or emotional states. The paper also points to opportunities: by designing interaction protocols that account for human cognitive complexity, we can build more effective and more aligned AI systems.

### 8.4 Zhang, Carroll, Bobu, and Dragan (2022): Time-Efficient Reward Learning via Visually Assisted Cluster Ranking

Zhang, Carroll, Bobu, and Dragan (2022), in their paper "Time-Efficient Reward Learning via Visually Assisted Cluster Ranking" (arXiv:2212.00169), address the practical problem of reducing the time cost of human feedback in reward learning. They observe that pairwise comparison labeling is expensive and time-consuming, and they propose a method that uses clustering to reduce the number of comparisons needed.

The key idea is to cluster the trajectories into groups of similar trajectories and ask the human to rank the clusters rather than comparing individual trajectories. This reduces the number of comparisons from O(n^2) to O(k^2), where k is the number of clusters and n is the number of trajectories. The clusters are generated using visual features (e.g., images of the trajectories), which makes the ranking task easier for the human.

This work is important for interactive IRL because it addresses the **human cost** of active learning. In many applications, the human's time is the bottleneck, not the agent's computation. Methods that reduce the number of queries or the time per query are essential for making interactive IRL practical. The cluster ranking approach is one of several recent methods that aim to make human feedback more efficient, including methods that use batch queries, methods that use natural language feedback, and methods that use implicit feedback (e.g., observing the human's natural behavior).

---

# Part VII: Inverse Cooperative Reinforcement Learning Extensions

## 9. Extensions of CIRL and Multi-Agent Interactive IRL

The CIRL framework has been extended in several directions, including multi-agent settings, communication protocols, and natural language interaction.

### 9.1 Multi-Agent CIRL

In the original CIRL framework, there is one human and one robot. This can be extended to settings with multiple humans and multiple robots. In multi-agent CIRL, the state space includes the beliefs of all agents, and each agent must reason about the beliefs of the others. This creates a complex recursive reasoning problem, similar to the "I know that you know that I know" problem in game theory.

Carroll, Shah, Ho, Griffiths, Seshia, Abbeel, and Dragan (2019), in their paper "On the Utility of Learning about Humans for Human-AI Coordination" (arXiv:1910.05789), study the problem of human-AI coordination and show that agents that learn about their human partners can achieve better coordination than agents that treat their partners as fixed. This is a form of multi-agent CIRL where the agent learns a model of the human's strategy and uses it to coordinate. The paper shows that standard self-play and population-based training methods create agents that can coordinate with themselves but not with humans, because they do not learn about human behavior.

### 9.2 Communication and Natural Language in CIRL

One of the most exciting extensions of CIRL is the incorporation of natural language communication. In standard CIRL, the communication between the human and the robot is limited to actions and observations in the physical environment. But in many real-world settings, the human and the robot can communicate through language, gestures, and other modalities.

Recent work has explored how natural language can be used to accelerate IRL. The human can provide verbal instructions, corrections, or explanations that convey information about the reward function more efficiently than physical demonstrations. For example, a human might say "avoid the red areas" rather than demonstrating a path that avoids the red areas. This verbal instruction conveys a general rule that applies to many situations, whereas a demonstration only conveys information about the specific situation demonstrated.

The combination of natural language with IRL is still an active area of research. Key challenges include grounding natural language in the physical environment, handling ambiguous or vague instructions, and integrating linguistic feedback with demonstration data. The emergence of large language models (LLMs) has opened new possibilities for this research, as LLMs can be used to interpret natural language instructions and generate candidate reward functions that are then refined through interaction.

---

# Part VIII: Connections to Active Learning in Supervised Settings

## 10. Transferring Active Learning Principles to IRL

Active learning in supervised learning is a well-studied field with a rich set of algorithms and theoretical results. The key question is whether these principles can be transferred to the IRL setting.

### 10.1 Uncertainty Sampling

In supervised learning, uncertainty sampling is a simple and effective active learning strategy: the learner selects the unlabeled example for which the current model is most uncertain. In classification, this is typically the example with the lowest maximum predicted probability (margin sampling) or the highest entropy of the predicted class distribution (entropy sampling).

In IRL, uncertainty sampling can be applied to the reward function parameters. The agent can select the query (e.g., the state or trajectory pair) for which the posterior distribution over reward parameters has the highest entropy. This is equivalent to the information-gain criterion used by Sadigh et al. (2017), as entropy reduction is equivalent to information gain for Gaussian posteriors. However, in IRL the uncertainty is not just over the label of a single example, but over the parameters of a function that determines the value of all trajectories. This makes the uncertainty computation more complex, as it requires evaluating the entropy of the posterior over the entire reward function.

### 10.2 Query-by-Committee

Query-by-committee (QBC) is another active learning strategy where a committee of models is trained, and the example with the highest disagreement among the committee members is selected for labeling. In IRL, a committee of reward functions can be maintained (e.g., by sampling from the posterior), and the query that maximizes the disagreement among the committee members can be selected. This has been explored by Cohn, Ghahramani, and Jordan (1996) in the supervised setting and has been adapted to IRL by maintaining an ensemble of reward estimates.

### 10.3 Expected Model Change

Expected model change is an active learning criterion that selects the example that would cause the largest change in the model parameters if labeled. In IRL, this can be applied by selecting the query that would cause the largest change in the reward parameters. This is related to the information-gain criterion, as the expected change in parameters is related to the Fisher information matrix. The expected model change criterion has been used in deep active learning and can be adapted to deep IRL, where the reward function is represented by a neural network.

### 10.4 Theoretical Gaps and Challenges

While the transfer of active learning principles to IRL is conceptually straightforward, there are several theoretical and practical challenges. First, the **query space** in IRL is much larger and more complex than in supervised learning. In supervised learning, the query is a single example (e.g., an image or a text). In IRL, the query is a trajectory or a pair of trajectories, which may be long, high-dimensional, and structured. This makes the query selection problem computationally harder.

Second, the **label space** in IRL is different from supervised learning. In supervised learning, the label is a class or a real value. In IRL, the label is a preference or a demonstration, which is a complex structured object. The noise model for human preferences is also more complex than the noise model for supervised labels, as human preferences may be inconsistent, context-dependent, and influenced by presentation effects.

Third, the **feedback loop** in IRL is more complex. In supervised learning, the label is provided for a single example, and the model is updated. In IRL, the query affects the human's future behavior, which affects the future data. This creates a feedback loop that is not present in supervised learning and requires careful analysis to avoid bias or divergence.

---

# Part IX: Synthesis and Connections to Alignment

## 11. Common Themes Across Active and Interactive IRL

Despite the diversity of approaches, several common themes emerge across the active and interactive IRL literature.

### 11.1 Information-Theoretic Foundations

Many active IRL methods are grounded in information theory. The agent selects queries to maximize the expected information gain about the reward function, which is equivalent to minimizing the entropy of the posterior. This information-theoretic foundation connects active IRL to Bayesian experimental design, optimal control of information, and the broader literature on active learning. The common thread is that learning is treated as an information acquisition process, and the agent optimizes the acquisition process to maximize the efficiency of learning.

### 11.2 The Exploration-Exploitation Tradeoff in Value Learning

A second common theme is the exploration-exploitation tradeoff, but applied to the learning of values rather than the learning of the environment. In standard RL, the agent explores the environment to find high-reward states. In active IRL, the agent explores the space of possible reward functions to find the true human reward. This requires a different kind of exploration: the agent must ask questions, probe preferences, and request demonstrations that reveal the human's values. The exploration-exploitation tradeoff in value learning is central to the CIRL framework, where the agent must balance acting on its current belief with gathering information to improve its belief.

### 11.3 The Human as a Strategic Teacher

A third theme is the recognition that the human is not merely a source of data, but a strategic teacher. In the CIRL framework, the human actively teaches the robot by selecting actions that convey information about the reward. In the machine teaching literature, the teacher selects demonstrations to maximize the learner's information gain. In the ZPD framework, the teacher selects demonstrations that are at the right level of difficulty for the learner. This shift from viewing the human as a passive data source to viewing the human as an active teacher has profound implications for the design of human-AI interaction systems.

## 12. Practical Implications for Human-AI Interaction and Alignment

### 12.1 Designing Better Interaction Protocols

The active and interactive IRL literature provides principles for designing better interaction protocols between humans and AI systems. First, the agent should be able to ask questions. This requires designing query interfaces that are natural and efficient for humans. Second, the agent should be able to handle ambiguous or inconsistent feedback. This requires robust inference algorithms that can tolerate noisy and contradictory data. Third, the agent should be able to adapt to the human's teaching style. This requires personalized models that learn not just the human's reward function, but also the human's communication strategy.

### 12.2 Safety and Alignment

From an alignment perspective, active and interactive IRL addresses one of the key challenges of AI safety: **value learning under uncertainty**. An agent that can ask clarifying questions is less likely to misinterpret the human's values. An agent that can handle inconsistent feedback is more robust to the complexities of human preference. An agent that can adapt to the human's teaching style is more likely to converge to the true reward function quickly and safely.

However, active IRL also introduces new risks. An agent that asks questions may ask manipulative or misleading questions. An agent that probes the human's preferences may probe sensitive or harmful preferences. An agent that learns from ongoing interaction may learn to exploit the human's cognitive biases. These risks require careful design of the interaction protocol, including constraints on the types of queries the agent can ask, oversight mechanisms to detect and correct harmful learning, and transparency mechanisms to help the human understand what the agent is learning.

### 12.3 Connections to Existing Substrate Work

The active and interactive IRL literature connects to several existing substrate files. The CIRL framework (Hadfield-Menell et al., 2016) is directly related to the concept of **machine conscience** discussed in the Ziebart analysis (2026-06-28-ziebart-maxent-irl-alignment-machine-conscience.md), as both are concerned with the agent's internal representation of values and its role in decision-making. The preference-based learning framework (Sadigh et al., 2017) connects to the **moral psychology** literature on preference elicitation and judgment. The online and incremental IRL methods connect to the **lifelong learning** and **continual learning** literature in the broader substrate.

The 2000-2010 IRL landscape (2026-06-28-irl-landscape-2000-2010.md) established the foundational algorithms that active and interactive IRL builds upon. The apprenticeship learning framework (Abbeel and Ng, 2004) provided the feature expectation matching approach that is used in many active IRL methods. The maximum entropy IRL framework (Ziebart et al., 2008) provided the probabilistic foundation for Bayesian active IRL. The cooperative IRL framework (Hadfield-Menell et al., 2016) redefined the problem as a two-agent game, which is the basis for much of the interactive IRL work.

---

# Part X: Future Directions and Open Problems

## 13. Open Problems

Several important open problems remain in active and interactive IRL.

### 13.1 Scaling to High-Dimensional Spaces

Most active IRL methods have been demonstrated on relatively low-dimensional problems (driving, manipulation, simple games). Scaling to high-dimensional spaces such as natural language, video, and complex robotics tasks remains a major challenge. Deep learning approaches (e.g., deep RLHF) have made progress on this front, but the theoretical foundations of deep active IRL are still underdeveloped.

### 13.2 Modeling Complex Human Behavior

As Lindner and El-Assady (2022) argue, humans are not simple Boltzmann agents. Modeling the full complexity of human behavior, including cognitive biases, emotional states, social context, and cultural differences, is a major open problem. This requires interdisciplinary research that combines AI, cognitive science, psychology, and sociology.

### 13.3 Safe and Ethical Querying

The problem of safe and ethical querying is still largely open. How do we design active IRL systems that ask questions that are informative, respectful, and safe? How do we prevent the agent from asking manipulative or harmful questions? How do we ensure that the agent's queries do not invade privacy or cause distress? These questions require not just technical solutions, but also ethical frameworks and regulatory oversight.

### 13.4 Multi-Modal Interaction

Most current active IRL systems use a single modality (demonstrations, comparisons, or natural language). Multi-modal interaction, where the agent can combine demonstrations, language, gestures, and other modalities, is a promising direction that could make interactive IRL more natural and efficient. The integration of large language models with robotics and vision systems is a particularly exciting area for future research.

---

# References

1. Abbeel, P., & Ng, A. Y. (2004). Apprenticeship Learning via Inverse Reinforcement Learning. In *Proceedings of the Twenty-First International Conference on Machine Learning (ICML 2004)*. ACM. https://doi.acm.org/10.1145/1015330.1015430

2. Bajgar, O., Gould, D. S. W., Liu, J., Abate, A., Gatsis, K., & Osborne, M. A. (2025). PAC Apprenticeship Learning with Bayesian Active Inverse Reinforcement Learning. arXiv:2508.03693. https://arxiv.org/abs/2508.03693

3. Bradley, R. A., & Terry, M. E. (1952). Rank Analysis of Incomplete Block Designs: I. The Method of Paired Comparisons. *Biometrika*, 39(3/4), 324–345. https://doi.org/10.2307/2334029

4. Brown, D. S., Cui, Y., & Niekum, S. (2019). Risk-Aware Active Inverse Reinforcement Learning. arXiv:1901.02161. https://arxiv.org/abs/1901.02161

5. Cakmak, M., & Lopes, M. (2012). Algorithmic and Human Teaching of Sequential Decision Tasks. In *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI 2012)*, 1536–1542. AAAI Press.

6. Carroll, M., Shah, R., Ho, M. K., Griffiths, T. L., Seshia, S. A., Abbeel, P., & Dragan, A. (2019). On the Utility of Learning about Humans for Human-AI Coordination. arXiv:1910.05789. https://arxiv.org/abs/1910.05789

7. Cohn, D., Ghahramani, Z., & Jordan, M. I. (1996). Active Learning with Statistical Models. *Journal of Artificial Intelligence Research*, 4, 129–145. https://doi.org/10.1613/jair.295

8. Goldman, S. A., & Kearns, M. J. (1995). On the Complexity of Teaching. *Journal of Computer and System Sciences*, 50(1), 20–31. https://doi.org/10.1006/jcss.1995.1003

9. Hadfield-Menell, J., Dragan, A., Abbeel, P., & Russell, S. (2016). Cooperative Inverse Reinforcement Learning. arXiv:1606.03137. In *Advances in Neural Information Processing Systems 29 (NeurIPS 2016)*. https://arxiv.org/abs/1606.03137

10. Ijju, S. (2023). A Markovian Formalism for Active Querying. arXiv:2306.08001. https://arxiv.org/abs/2306.08001

11. Lindner, D., & El-Assady, M. (2022). Humans are not Boltzmann Distributions: Challenges and Opportunities for Modelling Human Feedback and Interaction in Reinforcement Learning. arXiv:2206.13316. https://arxiv.org/abs/2206.13316

12. Ng, A. Y., Harada, D., & Russell, S. (1999). Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping. In *Proceedings of the Sixteenth International Conference on Machine Learning (ICML 1999)*, 278–287. Morgan Kaufmann.

13. Ng, A. Y., & Russell, S. J. (2000). Algorithms for Inverse Reinforcement Learning. In *Proceedings of the Seventeenth International Conference on Machine Learning (ICML 2000)*, 663–670. Morgan Kaufmann.

14. Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., ... & Lowe, R. (2022). Training Language Models to Follow Instructions with Human Feedback. *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, 27730–27744.

15. Sadigh, D., Dragan, A. D., Sastry, S. S., & Seshia, S. A. (2017). Active Preference-Based Learning of Reward Functions. In *Proceedings of Robotics: Science and Systems (RSS 2017)*. https://doi.org/10.15607/RSS.2017.XIII.053

16. Seita, D., Chan, D., Rao, R., Tang, C., Zhao, M., & Canny, J. (2019). ZPD Teaching Strategies for Deep Reinforcement Learning from Demonstrations. arXiv:1910.12154. https://arxiv.org/abs/1910.12154

17. Shah, I., Halpern, D., Asadi, K., Littman, M. L. (2021). Convergence of a Human-in-the-Loop Policy-Gradient Algorithm With Eligibility Trace Under Reward, Policy, and Advantage Feedback. arXiv:2109.07054. https://arxiv.org/abs/2109.07054

18. Shinohara, A., & Miyano, S. (1991). Teachability in Computational Learning. *New Generation Computing*, 8(4), 337–347. https://doi.org/10.1007/BF03037189

19. Thurstone, L. L. (1927). A Law of Comparative Judgment. *Psychological Review*, 34(4), 273–286. https://doi.org/10.1037/h0070288

20. Valiant, L. G. (1984). A Theory of the Learnable. *Communications of the ACM*, 27(11), 1134–1142. https://doi.org/10.1145/1968.1972

21. Vygotsky, L. S. (1978). *Mind in Society: The Development of Higher Psychological Processes*. Harvard University Press.

22. Wang, Z., Chen, C., & Dong, D. (2020). Lifelong Incremental Reinforcement Learning with Online Bayesian Inference. arXiv:2007.14196. https://arxiv.org/abs/2007.14196

23. Ye, C., Xiong, W., Zhang, Y., Dong, H., Jiang, N., & Zhang, T. (2024). Online Iterative Reinforcement Learning from Human Feedback with General Preference Model. arXiv:2402.07314. https://arxiv.org/abs/2402.07314

24. Zhang, D., Carroll, M., Bobu, A., & Dragan, A. (2022). Time-Efficient Reward Learning via Visually Assisted Cluster Ranking. arXiv:2212.00169. https://arxiv.org/abs/2212.00169

25. Ziegler, D. M., Stiennon, N., Wu, J., Brown, T. B., Radford, A., Amodei, D., ... & Lowe, R. (2019). Fine-Tuning Language Models from Human Preferences. arXiv:1909.08593. https://arxiv.org/abs/1909.08593

26. Ziebart, B. D., Maas, A. L., Bagnell, J. A., & Dey, A. K. (2008). Maximum Entropy Inverse Reinforcement Learning. In *Proceedings of the Twenty-Third AAAI Conference on Artificial Intelligence (AAAI 2008)*, 1433–1438. AAAI Press.

27. Zhu, X. (2013). Machine Teaching: An Inverse Problem to Machine Learning and an Approach Toward Optimal Education. In *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI 2013)*, 4083–4087. AAAI Press.

28. Zhu, X., Singla, A., Zheng, S., & Pech, N. (2018). An Overview of Machine Teaching. arXiv:1801.05927. https://arxiv.org/abs/1801.05927
