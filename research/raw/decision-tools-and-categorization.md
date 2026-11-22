# Decision Tools and Categorization: The 2026 Landscape

Raw research file. Single-topic deep dive produced 2026-11-22 on the tools and techniques for making small, fast, typed decisions inside software: routing, classifying, gating, verifying, and deferring. Source material for later synthesis, not a finished essay.

Companion file: [[jev-system-one-models]] covers the product (TypeSafe AI's Jev) that prompted this survey and supplies the concrete case at the centre of it.

Related Substrate nodes: [[jev-system-one-models]] (the product at the centre of the survey), [[agent-tool-permissions]] (gating as the permission problem), [[agent-orchestrator-pattern]] (routing between agents is the same problem as routing between models), [[decision-provenance]] (a decision with a recorded confidence and outcome), [[conscience]] (calibrated uncertainty as the deferral mechanism), [[principal-agent-theory]] (deference as the tractable form of the alignment gap), [[agent-platform-2027]] (the blueprint that used a decision model as a pipeline component), [[multi-agent-coordination]] (coordination by typed decision rather than by protocol).

## 1. The problem

An LLM call is the wrong shape for most of the decisions software needs to make. A decision inside a running system has four requirements that text generation satisfies badly:

1. **Fast.** It sits in a request path. A user waiting on a classification will not wait three seconds.
2. **Cheap.** It runs per item. Classifying a million documents at chat-model prices is not a product, it is a research budget.
3. **Typed.** Its output has to branch code. Free text has to be parsed and validated before software can act on it, and parsing is where the failure modes live.
4. **Honest about uncertainty.** If the decision might be wrong, the system needs a signal that says so, in time to route the case somewhere safer.

INTERPRETATION: those four requirements define a category, and the category is old. Guardrail classifiers, spam filters, intent classifiers, rules engines, and semantic caches have all been making fast typed decisions inside request paths for years or decades. What is new in 2026 is not the idea but the economics and the fidelity: the decisions now come from models that approach frontier reasoning, at a price measured in fractions of a cent, and with an explicit probability attached. So the useful question is not "which product wins" but "what are the actual primitives, and what is genuinely new versus old wine in a new price structure".

This file answers that in three layers: the science of calibrated decisions and deferral, the product landscape, and the practice of categorization itself, which is the thing all of this is doing.

## 2. The science of calibrated decisions and deferral

FACT: the product claim under examination has two independent parts, a probability that is calibrated, and a mechanism that acts on it. The literature treats these as separate problems with separate guarantees, and no single method delivers both.

INTERPRETATION: "RLCD" (the training method TypeSafe names) is not a named method in the literature. The nearest named lineages are calibration, selective prediction, and learning to defer. The product is best read as an application of those rather than as a new theoretical object.

### 2.1 Calibration: methods, metrics, and what it does not buy

BACKGROUND: Platt scaling (Platt, 1999) and isotonic regression (Zadrozny and Elkan, 2002) are the two classic post-hoc calibrators; Niculescu-Mizil and Caruana (2005) compared them across model families.

FACT: Guo, Pleiss, Sun, and Weinberger, "On Calibration of Modern Neural Networks" (ICML 2017, arXiv:1706.04599). Core finding: modern deep networks, unlike those "from a decade ago", are poorly calibrated and systematically overconfident. The same paper finds that temperature scaling, a single scalar applied to the logits, outperforms vector scaling and matrix scaling on both negative log likelihood and expected calibration error, and recommends it as the simple default.

BACKGROUND: the standard metrics are Expected Calibration Error and Maximum Calibration Error, which bin predictions and compare mean confidence to empirical accuracy; the Brier score (Brier, 1950), which is a strictly proper scoring rule; and reliability diagrams as the visual diagnostic. ECE and MCE are binning artifacts, sensitive to the number of bins and to the samples per bin.

BACKGROUND: what calibration guarantees is a marginal property. Over a bin, among inputs assigned confidence p, the fraction correct is approximately p. What it does not guarantee is per-input correctness, or even the right confidence for a specific input. A model can be overconfident in one region of input space and underconfident in another while remaining calibrated on average.

### 2.2 Conformal prediction, which is the stronger guarantee nobody is shipping

FACT: conformal prediction was founded by Vladimir Vovk with collaborators from the late 1990s; the canonical reference is Vovk, Gammerman, and Shafer, "Algorithmic Learning in a Random World" (Springer, 2005). Lei et al. (2018) formalized split conformal. The modern entry point is Angelopoulos and Bates, "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification" (arXiv:2107.07511).

FACT: the split conformal guarantee, for exchangeable data and any nonconformity score, is that the true label lies in the prediction set with probability at least 1 minus alpha, in finite samples, with an upper bound of 1 minus alpha plus 1 over (n plus 1) under distinct residuals. It is model-agnostic and distribution-free.

FACT: the guarantee is marginal, not conditional. No distribution-free method achieves meaningful conditional coverage, as shown by Lei and Wasserman (2014), Vovk (2012), and Barber et al. (2021); the price of conditional coverage is infinite expected set width. Empirically a constant-width band over-covers easy inputs and under-covers hard ones.

FACT: Conformal Risk Control (arXiv:2208.02814, Angelopoulos, Bates, Fisch, Lei, Schuster) extends conformal prediction from bounding miscoverage to bounding the expectation of any monotone loss, including false negative rate and token-level F1. BACKGROUND on the venue: ICLR 2023.

INTERPRETATION: the difference between calibration and conformal coverage matters and is usually elided in product marketing. A calibrated probability says nothing about whether a threshold rule will hit a target error rate on the next sample. Conformal coverage says nothing about the probability attached to any particular class. For a model whose output space is a fixed typed choice set, split conformal applies directly and yields prediction sets that are subsets of the label set with the coverage guarantee, which is the honest way to put a bound on a typed-choice model. It does not hand you a calibrated probability per choice for free. No product in this survey was found offering a conformal guarantee, which is a real gap given that it is the guarantee an automation gate actually wants.

FACT: the conformal guarantee requires exchangeability and decays under distribution shift, though the distribution-shift case is an active area rather than a solved one.

### 2.3 Selective prediction and the reject option

FACT: Chow, "On Optimum Recognition Error and Reject Tradeoff" (IEEE Transactions on Information Theory 16(1):41-46, 1970; also MIT AIM-175, 1969) defines the optimum rejection rule and the error-reject tradeoff. Chow's rule rejects when the loss of deciding exceeds the cost of abstaining; under zero-one loss that reduces to a threshold on the maximum posterior.

FACT: risk-coverage curves are the canonical object. Abstaining lowers risk at the cost of coverage, and selective classification trades coverage for accuracy.

FACT: Geifman and El-Yaniv, "Selective Classification for Deep Neural Networks" (NeurIPS 2017, arXiv:1705.08500) establishes that rejection grants a target risk with high probability while maximizing coverage, for example reaching 2 percent top-5 ImageNet error at 99.9 percent probability with about 60 percent coverage. BACKGROUND lineage: El-Yaniv and Wiener, "On the Foundations of Noise-Free Selective Classification" (JMLR, 2010).

INTERPRETATION: choosing the threshold from a cost model rather than by hand is the difference between a guess and a policy. The decision-theoretic rule is to abstain when the cost of the error times the probability of error exceeds the cost of abstaining or referring. Under a constant cost ratio that is exactly a fixed confidence threshold, so a hand-picked threshold is the special case of the cost rule where the two costs are constant.

### 2.4 Learning to defer, the closest academic analogue to the product's real use

FACT: Madras, Pitassi, and Zemel, "Predict Responsibly: Improving Fairness and Accuracy by Learning to Defer" (NeurIPS 2018, arXiv:1711.06664) generalizes rejection learning to a setting with another decision-making agent, and reports that deferral can improve accuracy and reduce bias, including with inconsistent or biased users.

FACT: Mozannar and Sontag, "Consistent Estimators for Learning to Defer to an Expert" (ICML 2020, PMLR 119:7076-7087, arXiv:2006.01862) designs a predictor plus a rejector and gives a reduction to cost-sensitive learning with a consistent surrogate loss generalizing cross entropy, framed for the case where only the expert's decisions are observed.

INTERPRETATION: the published framing is that naive deferral training is a consistency problem, in which the naive plug-in surrogate does not recover the Bayes-optimal deferral policy. Read as an engineering warning: optimizing a heuristic deferral loss, such as training a confidence head and thresholding it, is not a consistent estimator of the best deferral rule for that loss. The distinction that matters between human and model experts is whether the expert's output is observable on all inputs (defer to a model) or only when you hand off the decision (defer to a human), and whether the expert signal is noisy. INTERPRETATION: this lineage, not calibration, is the academically correct home for "defer when unsure", because learning to defer is trained against the cost of deferring while calibration is not.

### 2.5 The decision-theoretic layer

BACKGROUND: the rule that maximizes expected utility is to ask when the expected loss of deciding exceeds the expected loss of asking. That is a policy, a function of the input, and Chow (1970) is its recognition-specific instance. BACKGROUND: asking has a value bounded by the expected improvement in the decision, which is the classic Value of Information framing (Howard, 1966).

FACT: Hadfield-Menell, Dragan, Abbeel, and Russell, "The Off-Switch Game" (arXiv:1611.08219). An agent that is uncertain about the human's objective prefers to let the human correct it, because the correction is informative and the action is otherwise uninformed.

INTERPRETATION: that is the formal argument for "an uncertain agent has an incentive to defer", and it is worth being precise about what the uncertainty is over. It is uncertainty about the reward, not about the agent's own perception. An agent that is confident about its own prediction but uncertain about what the human wants still defers. That distinction separates the off-switch result from the calibration question, and the two are frequently conflated in product framing.

INTERPRETATION (which the literature supports): the cost-based policy is the supported object, and "defer when confidence is below X" is its threshold special case, exact only under a constant cost ratio and correct calibration. A confidence threshold is a valid policy only if calibration holds; the cost rule degrades gracefully when calibration is off.

### 2.6 Uncertainty elicitation from language models

FACT: Zhou, Jurafsky, and Hashimoto, "Navigating the Grey Area: How Expressions of Uncertainty and Overconfidence Affect Language Models" (EMNLP 2023). Language models are highly sensitive to epistemic markers in prompts, with accuracy varying by more than 80 percent across 50 injected markers; high-certainty wording reduces accuracy by about 7 percent relative to low certainty; factive verbs hurt and evidentials help. The paper reads this as mimicking observed language use rather than reflecting genuine internal uncertainty.

FACT: "Are Large Language Models More Honest in Their Probabilistic or Verbalized Confidence?" (arXiv:2408.09773, 2024) finds probabilistic (token) confidence better aligned with correctness than verbalized confidence; verbalized confidence is not well calibrated and tends to be overconfident, while probabilistic confidence still needs an in-domain validation set to pick a threshold.

FACT: Kuhn, Gal, and Farquhar, "Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation" (arXiv:2302.09664, ICLR 2023) introduces semantic entropy, entropy over meanings (clusters of semantically equivalent generations), unsupervised and single-model with no retraining.

FACT: Farquhar, Kossen, Kuhn, and Gal, "Detecting hallucinations in large language models using semantic entropy" (Nature, 2024, s41586-024-07421-0). Semantic entropy detects confabulations across datasets and tasks with no task-specific data; averaged over 30 task-model combinations it reaches about 0.790 AUROC against 0.691 for naive entropy, 0.698 for P(True), and 0.687 for embedding regression. It does not help when outputs are systematically wrong.

INTERPRETATION: raw token log probabilities are not calibrated probabilities. They become usable only after post-hoc calibration, and only in distribution. The honest statement of the state of the art is that uncertainty in generative models is an active research problem with partial solutions, and that a model which sidesteps the problem by not generating text has a genuine architectural advantage on this axis.

### 2.7 Calibrated LLM-as-judge

BACKGROUND: the judge and verifier pattern is established. Zheng et al. (2023, NeurIPS Datasets and Benchmarks) introduced and analyzed the LLM-as-judge setup including known position and verbosity biases. Kadavath et al. (2022, Anthropic) showed models can partly self-assess correctness through P(True)-style elicitation, degrading out of distribution.

INTERPRETATION: whether judge confidence can be calibrated well enough to gate automation is open. The verified evidence supports using semantic-entropy-style signals as an overseer signal and supports treating verbalized judge confidence as overconfident. No verified paper was found establishing a calibrated automation gate built from judge confidence, so no such claim should be made.

### 2.8 The open problems

- FACT: calibration decays under distribution shift. A calibrator fit on the training distribution does not transfer, and conformal's guarantee needs exchangeability. BACKGROUND for the general decay, with Ovadia et al. (2019) on uncertainty under dataset shift as the standard reference.
- FACT: confidence can stay high while accuracy collapses out of distribution; the Nature 2024 result shows embedding-regression uncertainty estimators degrade under shift. INTERPRETATION: high confidence out of distribution is not evidence of correctness.
- BACKGROUND: calibration does not imply that the model knows what it does not know. A calibrated head can be confidently wrong on inputs it has never seen, and Kadavath et al. (2022) is the optimistic case, explicitly distribution-limited.
- INTERPRETATION: the deferral failure modes are rubber-stamping (the human accepts the model's suggestion without independent review, so no real deferral happens), threshold drift (the cost ratio that set the threshold changes in deployment while the threshold does not), and feedback loops (the human's overrides become training labels, so the model converges on the human's biases). The Madras (2018) bias result is a measured instance of a human-agent interaction effect, in the opposite direction.

INTERPRETATION: the sharpest gap for any product claim of the "calibrated decision plus threshold" shape is that the combination is a valid policy only under two conditions the literature treats as fragile: the calibration must hold on the deployment distribution, and the cost ratio must be known and stationary. The learning-to-defer literature exists precisely because training a confidence head and thresholding it is not a consistent estimator of the optimal deferral rule.

## 3. The product landscape

BACKGROUND: the mature version of "a typed decision inside software" already exists, as classifier-in-the-request-path. Guardrail models, semantic routers, semantic caches, mixture-of-experts gates, and rules engines are all this pattern. The distinguishing claim of a decision model is not that it makes decisions but that its decision space is typed by construction.

### 3.1 Semantic model routers

BACKGROUND: a layer in front of multiple LLMs that picks which model handles a request.

FACT: RouteLLM (LMSYS, repository lm-sys/routellm) describes itself as "A framework for serving and evaluating LLM routers", with a cost threshold on each routing request controlling the cost-quality tradeoff. Open source. The decision signal is learned from preference data.

BACKGROUND: Martian and NotDiamond are commercial routers positioned on quality-per-dollar routing via learned preference models. OpenRouter's auto path selects among hosted models on cost and availability heuristics. Portkey is a commercial gateway with conditional routing and fallbacks. LiteLLM is an open-source proxy whose routing is rule and config based (fallbacks, load balancing, tag routing) rather than a learned semantic classifier. Cloudflare AI Gateway is a commercial edge gateway with caching, rate limiting, and fallback routing.

INTERPRETATION: all of these optimize cost, quality, and latency at the request level. The learned ones (RouteLLM, NotDiamond, Martian) decide by a classifier over the prompt and are the closest analogy to a decision model. The rule-based ones decide by configuration, keys, or health. Unverified this session: the exact routing mathematics for Martian, NotDiamond, and OpenRouter auto.

### 3.2 Cascades

FACT: FrugalGPT (arXiv:2305.05176, submitted 2023-05-09, Lingjiao Chen, Matei Zaharia, James Zou, Stanford) names three cost strategies, prompt adaptation, LLM approximation, and LLM cascade, and claims the cascade can match the best LLM while cutting cost by up to 98 percent.

BACKGROUND: the mechanism has a cheap model answer, then a scoring function (learned, or a confidence threshold) decides whether to escalate to a stronger model. The gate is the decision point.

INTERPRETATION: no dominant standalone "cascade as a product" was verified under that name. Cascade logic has been absorbed into routers and gateways as fallback chains and vendor escalation features, so the cascade should be read as a technique rather than a product category.

### 3.3 Guardrail and safety classifiers, the most mature category

BACKGROUND: Llama Guard (Meta) is an open-weight input and output safety classifier (versions 1, 2, and 3) that classifies a prompt or response against a taxonomy, returning a label, which is to say a typed decision. Prompt Guard (Meta) is an open-weight classifier focused on prompt injection and jailbreak detection.

FACT: NVIDIA NeMo Guardrails exists and is active, now at repository NVIDIA-NeMo/Guardrails, v0.25.0, with commits in November 2026, open source. BACKGROUND: it provides a DSL (Colang) for programmable rails and can call classifiers as rails.

BACKGROUND: Guardrails AI is an open-source Python framework whose validators enforce output structure and safety, with a validator hub. Azure AI Content Safety is a commercial API returning categories plus severity scores, with Prompt Shields for injection. Lakera is a commercial real-time prompt-injection and guardrail API that sells on low latency.

INTERPRETATION: these are the most mature typed-decision products in the industry. They output a label and often a score or threshold, so they are genuinely typed decisions, but they are trained offline and frozen rather than composed per call, which is the structural difference from a general decision model. Latency design targets are single-digit to low-double-digit milliseconds for small classifiers and tens of milliseconds for small-LLM guards; specific latency and accuracy tables were not verified this session and should not be cited without a source.

### 3.4 Structured output and constrained decoding, the crux

FACT: XGrammar (repository mlc-ai/xgrammar) describes itself as "Fast, Flexible and Portable Structured Generation" and "leverages constrained decoding to ensure 100% structural correctness". FACT: Outlines exists (repository dottxt-ai/outlines). BACKGROUND: guidance, Instructor, BAML, and provider JSON modes are further instances.

BACKGROUND: these force a generative model's token sampling to conform to a grammar, regex, or schema (JSON Schema, Pydantic, a context-free grammar). XGrammar, guidance, Outlines, and provider JSON mode are the pattern itself; Instructor and BAML are developer-ergonomics layers that generate schemas and validate or retry.

INTERPRETATION (the crux, and the single most important distinction in this file): constrained decoding constrains the syntax of a still-generative model. The model remains a free-text model wearing a shape, and it can be semantically wrong while syntactically valid. A model whose output space is typed by construction has the decision itself as its native emission, not a constrained string that is parsed into a decision. That is where a "typed decision model" claim lives, and it is a real distinction against XGrammar, Outlines, Instructor, and BAML. It is also a narrow one: the guarantee is about the shape of the answer, not its truth. A typed model cannot emit a malformed answer; it can emit a well-formed wrong one.

### 3.5 Mixture-of-experts routing as learned categorization

BACKGROUND: mixture-of-experts layers use a gating network that computes a softmax over experts and routes each token to the top-k experts. The lineage is Shazeer et al. (2017) on sparsely-gated mixture of experts; the Switch Transformer uses top-1 routing; Mixtral and DeepSeek-V3 use top-k with load balancing. Sparse upcycling is the practice of converting dense checkpoints into mixture-of-experts models. Named-model detail is from search snippets and is name-level only.

INTERPRETATION: the analogy is useful for the mechanism and misleading for the economics. Mechanically, a mixture-of-experts gate is a learned classifier deciding which expert receives a token, which is categorization inside the forward pass. Economically, the gate is trained end-to-end for next-token quality and is not an inspectable, addressable decision surface. A decision model exposes its gate; a mixture-of-experts model hides it. So the analogy illuminates why learned routing works and not why anyone would buy it as a product.

### 3.6 Semantic caching and deduplication

BACKGROUND: GPTCache (Zilliz) is an open-source semantic cache that embeds a request, does a vector-similarity lookup, and returns a cached response on a hit. Redis semantic cache does vector similarity search over cached prompts and responses.

INTERPRETATION: "is this request basically one I have seen before" is a fast categorization decision made in the serving path by an embedding threshold, and it is the cheapest decision surface in the stack today. It is also the clearest case where a wrong categorization is silent: a false cache hit returns a plausible answer to a different question.

### 3.7 Decision tables, rule engines, and DMN, the incumbent

BACKGROUND: the OMG's Decision Model and Notation standard provides decision tables and FEEL expressions and is the standard for shareable business decisions. Drools is Red Hat's rule engine (with KIE and DMN support), deterministic and forward chaining. The broader field includes IBM ODM, Camunda's DMN engine, and the CLIPS lineage.

INTERPRETATION: this is the incumbent a typed probabilistic decision product replaces or augments, and the tradeoff should be stated precisely. Rules are auditable, deterministic, explainable, cheap, and they freeze a human's judgement; they are brittle at the boundary of the unanticipated and cannot generalize. Models generalize but are opaque and probabilistic. A typed probabilistic decision product does not replace rules wholesale. It occupies the cases rules cannot enumerate, which is fuzzy intent and unanticipated input, while rules keep the hard, regulated, high-stakes cases. Framing it as a replacement rather than a boundary negotiation is a category error and a sales tactic.

### 3.8 Weak supervision and programmatic labeling

BACKGROUND: Snorkel combines labeling functions (heuristics, throwaway models, knowledge bases) through a label model into probabilistic training labels, which is the cheapest route to a custom classifier without hand-labeling.

INTERPRETATION: this is the cheapest path to a bespoke categorizer and it is the prior art a decision-model product must beat on ergonomics, since it requires no label model and no training run and returns a typed output directly. Where the labeling functions are cheap and the domain is stable, weak supervision remains the better engineering answer, and that is worth saying because the product marketing implies otherwise.

## 4. Categorization as a practice

### 4.1 The thesis that classification has consequences

FACT: Bowker and Star, "Sorting Things Out: Classification and Its Consequences" (MIT Press, 1999). The book's opening moral claim, in their own words: "Each standard and each category valorizes some point of view and silences another. This is not inherently a bad thing; indeed it is inescapable. But it is an ethical choice, and as such it is dangerous, not bad, but dangerous." That sentence is the whole thesis, and it is the sentence the rest of this section is about.

FACT (their definitions): "A classification is a spatial, temporal or spatio-temporal segmentation of the world." A classification system is "a set of boxes (metaphorical or literal) into which things can be put in order to then do some kind of work, bureaucratic or knowledge production." The ideal type assumes consistent and unique classificatory principles, mutually exclusive categories, and completeness. Real systems fail all three, and the failures are where the story lives.

FACT (torque, their own term): "a twisting of timelines that pull at each other, and bend or twist both patient biography and the process of metrication. When all are aligned, there is no sense of torque or stress; when they pull against each other over a long period, a nightmare texture emerges." Torque is what a person feels when the formal category and the lived trajectory disagree, and it is the bridge between the book's structural analysis and its ethical one.

FACT (residual categories): the "other", "not elsewhere classified", "none of the above" bucket. Their finding: "Others are everywhere, structuring social order." One design finding from the International Classification of Diseases: "not elsewhere classified" appears throughout but "nowhere as a top-level category", so that uncertainty is inevitable but its impact "will not hit a single disease or location disproportionately." The residual absorbs what the scheme cannot name, and where you put it decides who is invisible.

FACT (classification as infrastructure): they treat classification systems as information infrastructure, drawing on Star and Ruhleder's properties, embeddedness, transparency (visible "only upon breakdown"), reach or scope, learned as part of membership in a community of practice, linked to conventions of practice, embodying standards, and built on an installed base. The operative claim: "These standards and classifications, however imbricated in our lives, are ordinarily invisible." This is why the consequences are easy to miss. Naturalized infrastructure feels like nature.

FACT (boundary objects): classifications as "objects for cooperation across social worlds" (from Star and Griesemer, 1989), objects that "both inhabit several communities of practice and satisfy the informational requirements of each of them", that can travel while maintaining "some sort of constant identity", being "both ambiguous and constant", weakly structured in common use and more strongly structured in local use. Where such shared objects cannot be built, the book's word for the outcome is violence.

FACT (case studies): three clusters, the International Classification of Diseases as information infrastructure and the tuberculosis trajectories it shapes; race classification and reclassification under apartheid, where South Africans were sorted into four groups (White or European, Bantu or Black, Asian, and Colored or Mixed Race), with reclassification applications exposing "the underlying architecture of apartheid" as "a mixture of brute power, confused eugenics and appropriations of anthropological theories of race"; and the classification of nursing work through the Nursing Interventions Classification, where naming determines whether labour is visible or "forgotten".

FACT (their closing normative proposal, verbatim): "The only good classification is a living classification." Their call is for classifications that "explicitly retain traces of their construction", are tunable to "new institutional arrangements or personal trajectories", and can "reconfigure the world on the fly".

INTERPRETATION (the engineering brief hidden in the book): read as a design document, Bowker and Star are making four demands of any classification system. The residual category is a design decision with political content, so "other" must be first class rather than a dumping ground. Invisibility is a feature of adoption and a hazard of accountability, so the system should keep a trace of why a category exists and who chose it. The same label can mean different things to different communities (the boundary object problem), so a flat label set will be misread across teams. And user-visible disagreement with the classification (torque) is signal rather than error, and should have a route back into the schema.

BACKGROUND (Foucault as companion): "The Order of Things" ("Les mots et les choses", 1966) opens on Borges's invented Chinese encyclopedia and its impossible taxonomy, animals that "belong to the Emperor", that are "embalmed", "tame", "suckling pigs", "sirens". Foucault's point is not that the taxonomy is wrong but that it destroys the possibility of ordering at all, and he names the resulting unease heterotopia. Knowledge, on this account, is made possible by an episteme, a historical a priori deciding what can be said and seen together. INTERPRETATION: this is the right companion because it supplies the layer Bowker and Star deliberately leave thinner, the claim that the order of things precedes and enables knowledge about them. It is a different kind of book: Foucault works at the level of the epoch and a totalizing episteme, Bowker and Star at the level of the built artefact and the institutional negotiation, and they are careful not to stand outside these systems or to pronounce on a "real" versus "constructed" nature, asking instead only what the classifications do. Use Foucault for the philosophical claim that ordering precedes knowing; use Bowker and Star for the empirical case that specific orderings, once built, are consequential and contestable.

BACKGROUND (modern restatement): the critique of automated classification in machine learning is Bowker and Star's argument in a new substrate. Kate Crawford, "The Atlas of AI" (2021), on classification as extraction; Safiya Noble, "Algorithms of Oppression" (2018), and Ruha Benjamin, "Race After Technology" (2019), on the reproduction of social categories; Buolamwini and Gebru, "Gender Shades" (2018), on demographic error disparities in face classification; Crawford and Paglen, "Excavating AI" (2019), on the politics baked into the categories of a major image dataset.

INTERPRETATION: the continuity is exact. A training label is a draw from a taxonomy, and the taxonomy inherits the ethics of whoever built the box list. The new twist is that the box list is now often generated rather than curated, which is section 4.3.

### 4.2 The technical state of the art

FACT: Tunstall et al., "Efficient Few-Shot Learning Without Prompts" (SetFit, arXiv:2209.11055, 2022, Hugging Face). SetFit fine-tunes a pretrained sentence transformer on a small number of text pairs in a contrastive siamese manner, then trains a classification head on the resulting embeddings. The abstract reports no prompts or verbalizers, results comparable to prompt-based and pattern-exploiting methods, an order of magnitude faster training, and multilingual support by swapping the encoder. This is the current practical default for small labeled sets.

BACKGROUND (zero-shot classification with LLMs, two lineages): the natural-language-inference trick (Yin et al., "Benchmarking Zero-shot Text Classification", 2019) recasts the label as a hypothesis and asks an entailment model, and it shipped as the default zero-shot pipeline in a major open-source library. The generative lineage casts labels as options in a prompt or reads next-token logits over label strings; few-shot prompting was established by GPT-3 (Brown et al., 2020), and instruction-tuned and chat models made the prompt form dominant. Zero-shot is cheap and brittle, sensitive to label wording, ordering, and the model's priors about the label's semantics.

BACKGROUND (embedding-based classification and nearest neighbor): Sentence-BERT (Reimers and Gurevych, 2019) made sentence embeddings usable for similarity, turning classification into either a shallow probe (embeddings into logistic regression) or nearest-neighbor over labeled examples or one prototype vector per label. INTERPRETATION: the nearest-neighbor form is the most legible to a category-theorist, because adding a category is adding a prototype and a few examples, and it degrades gracefully, since a query near no prototype returns a low-similarity, high-abstention result.

BACKGROUND (contrastive learning): learn the embedding space so same-class items cluster and different-class items separate. SimCLR (Chen et al., 2020) for self-supervision, SupCon (Khosla et al., 2020) for supervised contrastive learning, CLIP (Radford et al., 2021) for joint image-text, which is the engine behind modern zero-shot classification by comparing an input embedding to per-label text embeddings. INTERPRETATION: contrastive objectives make the taxonomy's geometry explicit, since category boundaries become distances in a learned space, and two near-synonymous labels will fight over the same region unless the training pairs separate them.

BACKGROUND (hierarchical and multi-label): real taxonomies are trees or directed acyclic graphs, and real items carry several labels. Hierarchical classifiers exploit the tree, coarse to fine or one classifier per node, often with label smoothing down the path; multi-label classifiers emit a set. INTERPRETATION: hierarchy buys two things, a cheaper high-cardinality problem since you decide level by level, and an interpretable failure mode since the parent is often right when the leaf is wrong, which is exactly the "torque" of section 4.1 expressed as an error decomposition.

FACT (high-cardinality classification, the hard case): the formal name is eXtreme Multi-label Classification, predicting relevant labels from a universe of thousands to millions. The review (arXiv:2302.05971) and the Extreme Classification Repository are the standard references. BACKGROUND on the standard tricks: one-vs-all with a linear head and negative sampling, tree or label-clustering structures (Parabel, PECOS, XR-Transformer), and two-tower retrieval where the label set is indexed and the input is the query. Metrics are ranking metrics such as precision at k and nDCG, because exact recall over a million labels is hopeless.

INTERPRETATION: a ceiling of 255 is the maximum value of an unsigned eight-bit integer, so a bound stated in exactly that shape reads as a fixed-width encoding decision, with the category dimension living in one byte. The theoretical point the bound gestures at is real regardless: past a few hundred categories, flat softmax stops being the right tool and the problem becomes retrieval and ranking, where recall at k, calibration, and the long tail decide whether the system works at all. The product's own claim about the 255 bound could not be verified beyond its marketing page, so the byte-width reading is an inference from the number, not a documented design fact.

### 4.3 Dynamic and generated taxonomies

INTERPRETATION (the shift): classically the taxonomy is fixed and the classifier is learned. The emerging pattern is the reverse, with the classifier (an LLM) fixed and the taxonomy generated per tenant, per corpus, or per run. Two consequences follow immediately: cheapness and non-reproducibility.

BACKGROUND (taxonomies generated at runtime): prompt the model to name and structure the categories for a corpus, for example "here are 500 support tickets, propose the label set and the hierarchy", then classify into it. Variants iterate, classifying, inspecting the residual and the confusions, renaming or splitting a node, and re-running. Useful when no schema exists, dangerous when the schema is then treated as stable.

FACT: Grootendorst, "BERTopic: Neural topic modeling with a class-based TF-IDF procedure" (arXiv:2203.05794, 2022). The pipeline embeds documents with a transformer, clusters the embeddings (UMAP plus HDBSCAN by default), then derives a topic representation with a class-based variation of TF-IDF. BACKGROUND: latent Dirichlet allocation (Blei et al., 2003) is the ancestor and Top2Vec is a sibling. INTERPRETATION: BERTopic is topic modeling rebuilt as clustering, which is exactly the move: the "category" becomes a cluster plus a generated label rather than a curated concept.

BACKGROUND (clustering as categorization): k-means, HDBSCAN, agglomerative. The labels are indices, and the indices are not stable, since re-running with a different seed, a different neighborhood parameter, or a different embedding checkpoint renumbers the clusters and re-partitions the boundary cases. Cluster identifiers are not concepts.

INTERPRETATION (taxonomy drift, a third kind): concept drift (surveyed by Gama et al., 2014) is when the mapping from input to label changes over time; label shift is when the prior over labels changes. Taxonomy drift is specific to generated categories: the referent itself is regenerated, so "the taxonomy used in March" and "the taxonomy used in April" are not comparable, and any longitudinal aggregate silently compares apples to oranges. This is where the technical argument loops back to section 4.1. Bowker and Star asked for classifications that explicitly retain traces of their construction. A generated taxonomy discarded and re-derived each run is the exact opposite, maximum recency with zero provenance and no route for a user to contest a category that will not exist next week. The engineering response is to version the taxonomy as you version the model, or you cannot audit either.

### 4.4 How categorization is evaluated

BACKGROUND (precision, recall, and the confusion matrix): precision is the fraction of predicted positives that are correct, recall is the fraction of true positives found, and F1 is their harmonic mean. The confusion matrix decomposes errors into false positives and false negatives, and per-class matrices expose the classes being sacrificed. Averaging matters: micro-averaging is dominated by common classes, macro-averaging weights every class equally and exposes rare-class failure, which is usually the one that matters for equity and for the long tail.

BACKGROUND (the cost asymmetry is the whole game): the threshold is a policy choice, not a default. A threshold of 0.5 assumes equal cost for a false positive and a false negative, which is almost never true. Cost-sensitive learning (Elkan, 2001; Provost and Fawcett) formalizes the move: choose the threshold from the ratio of costs, not from accuracy. INTERPRETATION: a decision system is a cost function wearing a model's clothes. Accuracy is a proxy that flatters the model; the cost matrix is what the operator actually cares about and should be written down before the model is built, because it is the only object in the pipeline that cannot be learned from data.

BACKGROUND (inter-annotator agreement as the ceiling): Cohen's kappa (Cohen, 1960) corrects observed agreement for chance; Fleiss's kappa extends it to more than two raters; Krippendorff's alpha handles missing data and several scales. INTERPRETATION: two uses. As a ceiling, since a classifier cannot outperform the label set it was trained on, and if two humans agree only 70 percent of the time beyond chance then 70 percent is the taxonomy's own reliability rather than the model's failure. Low kappa is a diagnosis of the schema, not of the annotators, which is the empirical form of the Bowker and Star claim that categories are negotiated rather than discovered. As a warning, because chance-corrected agreement is sensitive to prevalence, and low-prevalence categories can show paradoxically low kappa even with high raw agreement.

BACKGROUND (coverage and abstention as a first-class outcome): Chow's rule is the classical selective classifier, abstaining when the posterior is too close to the decision boundary; Geifman and El-Yaniv (2017) revived it for deep models, trading coverage for accuracy; conformal prediction gives distribution-free coverage guarantees. INTERPRETATION: abstention is the engineering form of the residual category. It is the system saying "the scheme does not name this", and a system that cannot say that is lying about its completeness. An evaluation that reports only accuracy and not coverage has hidden its residual in the false-positive column, where it does its damage unseen.

### 4.5 Ontologies and knowledge organization

BACKGROUND (the stack): RDF is the data model (subject, predicate, object triples, with IRIs as names). RDFS adds lightweight class and property hierarchies. OWL is the Web Ontology Language, grounded in description logic, adding cardinality, disjointness, and logical axioms a reasoner can use to infer entailments and check consistency. SKOS is the deliberately lighter layer for thesauri and controlled vocabularies, with preferred and alternate labels and broader, narrower, and related relations. SPARQL queries all of it.

FACT: Hogan et al., "Knowledge Graphs" (arXiv:2003.02320, 2020, revised 2021) is the standard survey. INTERPRETATION: a knowledge graph is the pragmatic descendant of the ontology project, with less insistence on a single axiomatized upper ontology and more acceptance of heterogeneous, partial, dynamically updated schemas.

BACKGROUND (enterprise taxonomy practice): controlled vocabularies, thesauri, facet analysis (Ranganathan's colon classification is the intellectual ancestor of faceted search), shared metadata vocabularies such as Dublin Core and schema.org, and the discipline of taxonomy governance in large organizations. This is where categorization is a managed asset with owners and change control.

INTERPRETATION (what formal ontology buys over a flat label set): inheritance and reasoning (state that heart failure is a cardiovascular disease once and the reasoner propagates it), consistency checking (contradictions surface at authoring time rather than query time), disambiguation (IRIs make "bank" two things), relational structure a flat label cannot express (part-of, caused-by), and federation across systems that agree on identifiers. That is a genuinely larger expressive budget than a softmax head.

INTERPRETATION (why it failed to spread to applied ML, in rough order of weight): the knowledge acquisition bottleneck, since hand-curating an ontology is expensive and maintaining it against a moving world is worse; the semantic web's overpromise and its open-world assumption, which sits badly against the closed-world statistical framing most machine learning assumes; staleness, since an ontology nobody edits is a museum and the incentive to edit it rarely lands on the team that depends on it; and the culture gap, since the ontology community optimized for logical guarantees while the machine learning community optimized for generalization from examples, and the two did not share a metric. The pragmatic reconciliation is visible now in ontology-aware LLM classification and in retrieval over knowledge graphs, where the ontology is a soft prior rather than a hard constraint. Where ontology did stick, it stuck because curation was funded and the stakes were clinical: the Gene Ontology, SNOMED CT, and UMLS are the standing counterexamples.

### 4.6 Where categorization surfaces in products

BACKGROUND (named systems): intent classification in assistants (Alexa, Google Assistant) and their shipping toolchains (Dialogflow, Rasa); ticket triage and routing in Zendesk, ServiceNow, and Jira automation; document and email routing in enterprise capture and records systems; content moderation classifiers including the Perspective API and OpenAI's moderation endpoints; and product-category assignment in commerce catalogs.

INTERPRETATION (the agent-facing surface is the newer one): an LLM agent classifying an incoming request to choose a tool, a memory index, or a sub-agent is doing intent classification under another name. The router pattern in retrieval (pick the index, pick the retrieval strategy, or decide to answer directly), self-querying retrieval, and LLM tool selection are all categorization decisions made at runtime by the same model that then acts on them. Retrieval routing is the case where a classification error is not merely a wrong label but a wrong evidence set, which is why abstention and coverage matter more here than raw accuracy does.

### 4.7 The cost argument, and a skeptical reading

INTERPRETATION (categorization as the reduction of decision cost): a category is a compressed prior. It lets an actor skip a fresh evaluation and reuse a decision. Sorting is worth doing exactly to the degree it lowers the cost of the decisions that follow. That is the honest answer to why categorize at all: not knowledge for its own sake, but the amortization of judgement.

FACT (the Jevons paradox): Jevons (1865, "The Coal Question") observed that improvements in the efficiency of coal use increased rather than decreased total coal consumption. The modern statement is that the paradox occurs when a technological improvement in the efficiency of a resource's use leads to a rise in total consumption, that is, when the rebound effect exceeds 100 percent. The mechanism: greater efficiency reduces the resource needed per application and lowers its effective cost, and if demand is sufficiently price elastic the lower cost induces demand, frequently resulting in a net increase in total consumption.

INTERPRETATION (the applied claim, and why it is only suggestive): the TypeSafe-style move is that a fall in the cost of a decision unlocks more decisions. That is Jevons with classification in the coal slot. It has real force where classification is a bottleneck on a genuinely elastic activity, such as the number of documents you would survey or the number of tickets you would triage if each were nearly free. But the paradox's conditions are specific and several do not obviously hold for machine classification:

1. Jevons needs the efficiency gain to lower the effective price of the service and the demand to be price elastic. The elasticity of demand for "decisions" is not a market quantity: nobody has a demand curve for being classified, so the rebound is not measurable in the same currency as the efficiency gain.
2. Jevons needs the savings to be respent on the same service. Machine classification is more often a substitute for a human judgement than an input that scales it. Substitution can reduce decision volume rather than multiply it, which is the opposite of the paradox.
3. The binding constraint is usually downstream, not at the classifier. You can classify a thousand tickets you cannot fix. Classification volume exceeding the capacity to act does not unlock decisions; it relocates them into a review queue. The rebound, where it exists, lands on the false-positive review burden, and it is paid in human attention, which is the resource that did not get cheaper. This is Bowker and Star's work of the people who adjust classifications to make organizations run smoothly, recreated as an ML operations queue.
4. The accounting unit is undefined. "More decisions" is not a well-formed total when the system also manufactures the decisions it counts. A classifier that sorts every email into twelve folders has not created twelve decisions per email; it has created one labeling event per email, which is a different and cheaper thing.

INTERPRETATION (verdict): apply Jevons here as a prompt for questions, not as a law. The version that survives skeptical reading is narrow: cheap classification reliably increases the volume of classification events, trivially, and can increase net decision value only where the elasticity is real, the output feeds an action with slack capacity, and the false-positive cost does not consume the savings. Where those conditions fail, cheaper classification is best understood as the automation paradox, moving the hard judgement from the classifier to the reviewer and calling the move efficiency. The design response is not to reject the category but to instrument its cost honestly, which means the cost matrix of section 4.4 and the abstention rate from the same section are the two numbers that decide whether any of this is progress.

## 5. What is actually new

INTERPRETATION: sorting the genuinely new from the repackaged, the honest ledger is short.

**Not new.** The mathematics of deciding when to abstain is from 1970 (Chow). The guarantee that would actually let you automate on a classifier's confidence is from 2005 (conformal prediction). Consistent training for deferral to an expert is from 2018 and 2020 (Madras; Mozannar and Sontag). Calibration methods are from 1999 to 2017. Guardrail classifiers and semantic routers have been in production for years. Rules engines have been in production for decades. The argument that categories have consequences is from 1999 and the argument that ordering precedes knowing is from 1966.

**New in 2026, genuinely.** First, the decision as the native unit of inference rather than a parsed string, which is an architectural change with a real consequence: the failure mode of malformed output disappears by construction, and with it a whole class of integration bugs and prompt-injection surfaces. Second, the price. A decision at fractions of a cent per case, with free output and sub-second latency, changes what is worth automating, which is the actual commercial claim and the one worth taking seriously. Third, the placement. A frontier-adjacent decision inside a request path at 100 milliseconds moves classification from the batch layer to the interactive layer, which is where most of the value in the existing categorization products already lives but where the models were not previously good enough or cheap enough to sit.

**New and unowned.** The taxonomy problem has inverted. When taxonomies were curated by hand, the failure mode was the knowledge acquisition bottleneck and the fix was governance. When taxonomies are generated per run, the failure mode is provenance loss and incomparability over time, and there is no established practice for it. Section 4.3's proposal, version the taxonomy like the model, is not implemented in any product surveyed here.

**The gap between the two literatures.** The decision-tools literature optimizes for accuracy, cost, latency, and calibration. The categorization literature asks about consequences, residuals, and the route by which a person can contest a category. No product in this survey serves both, and no evaluation framework measures both. A system that classifies cheaply, confidently, and inaccurately about people is exactly what Bowker and Star described, at a lower price and a higher volume, and the tools have not changed their shape to account for it.

## 6. Where the mapping breaks

- **The theory predates the products by decades, and only the price is new.** Nothing in section 2 was discovered in 2026. The honest framing of the whole category is that the mathematics of abstention, coverage, and deferral has been available for years and the missing ingredient was a model good enough and cheap enough to make the primitives worth wiring up. Read the products as the commercialization of an old idea, not the invention of a new one.
- **Confidence thresholds are shipped; the policy that justifies them is left to the integrator.** The literature's object is a cost-based deferral rule. The products ship a probability and a suggested threshold, and the integrator implements the bands. That means the hard part, the cost matrix and its stationarity, lands on the customer, usually with no instrumentation to notice when it drifts.
- **No product offers the guarantee the use case actually wants.** For an automation gate you want coverage, conformal gives it distribution-free, and no surveyed product offers it. Nobody has measured a conformal bound on a commercial decision model. That is the single most useful experiment missing from this landscape.
- **Calibration is marginal, and every product's marketing treats it as if it were per-input.** The vendor's own docs sometimes say this plainly, and the marketing still implies otherwise. A group-level property cannot license a per-case decision without an assumption the product does not state.
- **The generated-taxonomy case has no practice, only a risk.** Section 4.3's drift problem is real, unnamed in any product, and likely to appear as an audit failure rather than a model failure. The engineering fix is cheap (version the taxonomy) and nobody is doing it because the taxonomy is treated as a prompt detail rather than a governed artefact.
- **The categorization consequences literature is entirely absent from the products.** Not one surveyed design treats the residual as a first-class category, retains the trace of a category's construction, or gives a user a route to contest a classification. Bowker and Star's four design demands from section 4.1 are 25 years old and unaddressed. This is not a small omission in systems that will route people's benefits claims, medical records, and job applications.
- **Evaluation is split down the middle and neither half is sufficient.** Decision tools get evaluated on accuracy, cost, and latency. Categorizers get evaluated on precision, recall, and agreement. Neither reports the coverage curve alongside the accuracy and neither reports the cost matrix that explains the threshold. A system can pass both evaluations and still be misclassifying the rare case that carries the consequence, which is the macro-averaging failure dressed as a success.
- **The Jevons argument, as deployed, is rhetoric rather than economics.** Section 4.7 gives four reasons the conditions do not obviously hold for classification. The rebound, where it exists, is paid in human review attention, which is the resource that did not get cheaper. A company named after Jevons is making a bet about demand, and the bet is untested.
- **The mixture-of-experts analogy is attractive and misleading.** Learned gating is categorization, and it is hidden inside the forward pass rather than exposed as an inspectable surface. Anyone using the analogy to argue that decision models are inevitable should note that the industry has had learned categorization inside models for a decade without any of the governance questions being asked.
- **Weak supervision is the honest competitor and it gets less attention.** Where labeling functions are cheap and the domain is stable, composing them into a label model is a better and cheaper answer than buying a decision model, and it is auditable in a way a learned classifier is not. The ergonomics gap, not the capability gap, is the argument for the new products, and it is worth naming as such.
- **The funding numbers say the market believes this is infrastructure.** A large valuation for a decision-model company implies the category is expected to sit underneath everything, which raises the stakes of section 4.1 rather than lowering them. Infrastructure that classifies people and has no route for them to contest the classification is precisely the hazard Bowker and Star named, and the current products have not answered it.

## 7. Compression points for synthesis

1. The category is "small, fast, typed decisions inside software", and it is old: guardrail classifiers, routers, rules engines, and semantic caches have been doing it for years or decades. What changed in 2026 is that decisions now come from frontier-adjacent models at fractions of a cent with explicit probabilities.
2. The mathematics of deciding when to abstain is from Chow (1970); selective prediction and risk-coverage curves formalize it; Geifman and El-Yaniv (2017) revived it for deep models.
3. Conformal prediction (Vovk, Gammerman, and Shafer, 2005; Angelopoulos and Bates, arXiv:2107.07511) provides a distribution-free finite-sample coverage guarantee, and it is the guarantee an automation gate actually wants. It is not offered by any product in this survey, and no independent conformal bound has been measured on a commercial decision model. That is the sharpest missing experiment.
4. Calibration (Platt 1999, Guo et al. 2017, temperature scaling) is a marginal property: it says that among inputs assigned confidence p, about p are correct, and it guarantees nothing about a specific input. Calibration of a probability and coverage of a set are different objects, and product marketing elides the difference.
5. Learning to defer (Madras et al. 2018; Mozannar and Sontag 2020) is the academically correct home for "defer when unsure", and its central result is that training a confidence head and thresholding it is not a consistent estimator of the optimal deferral rule.
6. The correct decision rule is a policy, ask when the expected loss of deciding exceeds the expected loss of asking, and a confidence threshold is its special case under a constant cost ratio and correct calibration. The off-switch game (Hadfield-Menell et al., arXiv:1611.08219) is the theoretical reason an uncertain agent defers, and the uncertainty it concerns is over the reward, not over the model's own perception.
7. Constrained decoding (XGrammar, Outlines, Instructor, BAML) constrains the syntax of a still-generative model, which can be wrong while valid. A model whose output space is typed by construction has the decision as its native emission. That distinction is real and narrower than it sounds: it guarantees the shape of the answer, not its truth.
8. The product landscape's components are semantic routers (RouteLLM, Martian, NotDiamond, OpenRouter, Portkey, LiteLLM, Cloudflare AI Gateway), cascades (FrugalGPT, absorbed into routers rather than sold as products), guardrail classifiers (Llama Guard, Prompt Guard, NeMo Guardrails, Guardrails AI, Azure AI Content Safety, Lakera), structured output tools, mixture-of-experts gates, semantic caches (GPTCache, Redis), rules engines (DMN, Drools), and weak supervision (Snorkel). Rules are the incumbent, and a typed probabilistic decision product negotiates a boundary with them rather than replacing them.
9. Categorization is not neutral. Bowker and Star, "Sorting Things Out" (1999): each standard and category valorizes some point of view and silences another, and that is "dangerous, not bad, but dangerous". Their concepts, torque, residual categories, classification as infrastructure, and boundary objects, are the vocabulary for what happens when a system sorts people or work. Their closing demand is that the only good classification is a living one, retaining traces of its construction and tunable to new arrangements.
10. The taxonomy problem has inverted: curated taxonomies had a knowledge-acquisition bottleneck, generated taxonomies have a provenance and comparability failure. Version the taxonomy as you version the model. No surveyed product does this, and the categorization consequences literature's four design demands (first-class residual, retained construction traces, cross-community legibility, a route to contest) are 25 years old and unimplemented.
11. Evaluation is split and insufficient: decision tools are scored on accuracy, cost, and latency; categorizers on precision, recall, and agreement; neither on consequences or coverage. Macro-averaging reveals rare-class failure and is usually omitted, which hides exactly the category error that carries the cost.
12. The Jevons argument for cheap decisions is a demand bet, not an economic result. The paradox needs price-elastic demand, respending on the same service, and slack downstream capacity, and several of those do not obviously hold for classification. The rebound, where it exists, is paid in human review attention.

## Sources

### Verified live this session

- Chow, C. K. (1970), "On Optimum Recognition Error and Reject Tradeoff", IEEE Transactions on Information Theory 16(1):41-46. For the reject rule and the error-reject tradeoff.
- Guo, Pleiss, Sun, and Weinberger (2017), "On Calibration of Modern Neural Networks", ICML, arXiv:1706.04599. Miscalibration of modern networks; temperature scaling.
- Angelopoulos and Bates, "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification", arXiv:2107.07511. For the split conformal guarantee and its marginal character.
- Angelopoulos, Bates, Fisch, Lei, and Schuster, "Conformal Risk Control", arXiv:2208.02814. Coverage extended to monotone losses.
- Geifman and El-Yaniv (2017), "Selective Classification for Deep Neural Networks", NeurIPS, arXiv:1705.08500.
- Madras, Pitassi, and Zemel (2018), "Predict Responsibly: Improving Fairness and Accuracy by Learning to Defer", NeurIPS, arXiv:1711.06664.
- Mozannar and Sontag (2020), "Consistent Estimators for Learning to Defer to an Expert", ICML, PMLR 119:7076-7087, arXiv:2006.01862.
- Hadfield-Menell, Dragan, Abbeel, and Russell, "The Off-Switch Game", arXiv:1611.08219.
- Zhou, Jurafsky, and Hashimoto (2023), "Navigating the Grey Area", EMNLP 2023.
- "Are Large Language Models More Honest in Their Probabilistic or Verbalized Confidence?", arXiv:2408.09773 (2024).
- Kuhn, Gal, and Farquhar (2023), "Semantic Uncertainty", ICLR, arXiv:2302.09664.
- Farquhar, Kossen, Kuhn, and Gal (2024), "Detecting hallucinations in large language models using semantic entropy", Nature, s41586-024-07421-0.
- Chen, Zaharia, and Zou, "FrugalGPT", arXiv:2305.05176 (2023-05-09).
- RouteLLM, repository lm-sys/routellm. Cost-threshold routing, learned from preference data.
- XGrammar, repository mlc-ai/xgrammar. Constrained decoding and the structural-correctness claim.
- Outlines, repository dottxt-ai/outlines. Existence verified.
- NVIDIA NeMo Guardrails, repository NVIDIA-NeMo/Guardrails, v0.25.0, active November 2026.
- Bowker and Star (1999), "Sorting Things Out: Classification and Its Consequences", MIT Press. Introduction and chapters 1, 2, 9, and 10, full text published by the author at ics.uci.edu/~gbowker/classification/. All section 4.1 quotations verified against that text.
- Tunstall et al. (2022), "Efficient Few-Shot Learning Without Prompts" (SetFit), arXiv:2209.11055.
- Grootendorst (2022), "BERTopic", arXiv:2203.05794.
- Hogan et al. (2020, revised 2021), "Knowledge Graphs", arXiv:2003.02320.
- "Review of Extreme Multi-label Classification", arXiv:2302.05971, and the Extreme Classification Repository, manikvarma.org.
- Jevons paradox, definition and mechanism, with W. S. Jevons, "The Coal Question" (1865), as the underlying source.

### Established record cited but not re-verified (verify before direct quotation)

- Platt (1999) and Zadrozny and Elkan (2002) on post-hoc calibration; Niculescu-Mizil and Caruana (2005) on comparing calibrators; Brier (1950) on the proper scoring rule.
- Vovk, Gammerman, and Shafer (2005), "Algorithmic Learning in a Random World", Springer; Lei et al. (2018) on split conformal; Lei and Wasserman (2014), Vovk (2012), and Barber et al. (2021) on the impossibility of distribution-free conditional coverage.
- El-Yaniv and Wiener (2010), JMLR, on noise-free selective classification; Howard (1966) on value of information; Ovadia et al. (2019) on uncertainty under dataset shift.
- Zheng et al. (2023), NeurIPS Datasets and Benchmarks, on LLM-as-judge and its biases; Kadavath et al. (2022), Anthropic, on models knowing what they know.
- Shazeer et al. (2017) on sparsely-gated mixture of experts; the Switch Transformer, Mixtral, and DeepSeek-V3 architectures (name-level only); sparse upcycling.
- Llama Guard, Prompt Guard, Guardrails AI, Azure AI Content Safety, Lakera, GPTCache, Redis semantic cache, Snorkel and labeling functions, DMN, Drools, IBM ODM, Camunda, CLIPS. Positioned from established record; documentation bodies were not opened this session and latency or accuracy figures for these are not cited.
- Yin et al. (2019) on NLI-based zero-shot classification; Brown et al. (2020) on few-shot prompting; Reimers and Gurevych (2019) on Sentence-BERT; Chen et al. (2020), Khosla et al. (2020), and Radford et al. (2021) on contrastive learning; Blei et al. (2003) on latent Dirichlet allocation; Gama et al. (2014) on concept drift; Cohen (1960), Fleiss, and Krippendorff on agreement; Elkan (2001) and Provost and Fawcett on cost-sensitive learning; Ranganathan on facet analysis; the Gene Ontology, SNOMED CT, and UMLS as funded clinical ontologies.
- Michel Foucault, "The Order of Things" (1966), the Borges taxonomy, heterotopia, and the episteme; Crawford, "The Atlas of AI" (2021); Noble, "Algorithms of Oppression" (2018); Benjamin, "Race After Technology" (2019); Buolamwini and Gebru (2018); Crawford and Paglen (2019).
- Martian, NotDiamond, Portkey, LiteLLM, Cloudflare AI Gateway, OpenRouter auto-routing. Categories and positioning only; routing mathematics and documentation not opened this session.

### Open questions a later pass should close

- No independent conformal measurement or coverage curve exists for any commercial decision model. This is the most valuable missing artifact in the file.
- The mixture-of-experts architecture details (Switch Transformer, Mixtral, DeepSeek-V3) were name-level only and should be sourced properly before any synthesis leans on them.
- Several product docs (Martian, NotDiamond, Portkey, LiteLLM, Cloudflare AI Gateway, Azure AI Content Safety, Lakera, GPTCache, Snorkel, DMN, Drools) were rate-limited and are cited at the name and positioning level only. A second pass with working fetches should verify their actual mechanisms.
- No product was found implementing any of Bowker and Star's four design demands. If one exists, it belongs in this file.
- The claim that generated taxonomies cause audit failure is an INTERPRETATION here. A case study, if one exists, would convert it to evidence.
