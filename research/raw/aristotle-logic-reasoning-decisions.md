# Aristotle: Logic, Reasoning, and Rational Decision-Making

Raw research file. Deep dive on Aristotle as the origin point of formal logic, the theory of demonstrative reasoning, and the account of practical rationality. This file is source material for later synthesis, not a finished essay.

Stance: report what the texts and the scholarship say, mark the boundary between them. FACT tags apply to claims verified live this session with source; BACKGROUND marks established record not re-verified this session; INTERPRETATION marks readings and connections.

Related Substrate nodes: [[5-whys]] (Aristotle's four causes as the ancient formalization of "why"), [[critical-rationalism]] (Popper's break with the demonstrative ideal Aristotle founded), [[decision-provenance]] (chains of reasons as first-class artifacts; the practical syllogism is the original chain), [[agent-identity]] (character and choice as the seat of practical reason).

---

## 1. The claim

Framing claim (INTERPRETATION): Aristotle invented logic as a discipline by separating the form of an argument from its content, and he drew the boundary that decision science keeps rediscovering: formal logic guarantees validity, not wisdom. Sound decisions need true premises, correct perception of particulars, and character that wants the right ends in the first place.

---

## 2. The Organon: logic as instrument

Aristotle's logical writings were never conceived by him as a single book. The grouping into a corpus called the Organon ("instrument" or "tool") was the work of later commentators, the Peripatetic school and especially the Alexandrian/Neoplatonic tradition, who argued that logic is not a part of philosophy but the instrument of all philosophy and science. Hence the name: organon, instrument. (BACKGROUND)

The six treatises, in the traditional order (terms to propositions to syllogisms to demonstration to dialectic to fallacies): (BACKGROUND)

- **Categories**: classification of terms and the ten categories (substance, quantity, quality, relation, place, time, position, state, action, passion); homonymy, synonymy, paronymy.
- **De Interpretatione**: from terms to propositions; affirmation and negation; the raw materials of the square of opposition (A/E/I/O forms). Chapter 9 contains the sea-battle discussion of future contingents, the locus classicus for debates about excluded middle and fatalism.
- **Prior Analytics**: the theory of the syllogism proper. Book I opens with the definition (see below), develops the three figures, and determines which premise-pairs yield valid conclusions, reducing imperfect figures to the perfect first figure. FACT: the definition opens Prior Analytics I.1 at 24b18-20.
- **Posterior Analytics**: the theory of demonstration (apodeixis), scientific inference whose premises are true, primary, immediate, better known than, prior to, and explanatory of the conclusion. Aristotle's philosophy of science; the model Euclid later instantiated.
- **Topics**: the art of dialectic, reasoning from endoxa (reputable opinions) rather than from true first principles. A handbook for argumentative debate.
- **Sophistical Refutations**: a catalogue of thirteen fallacies, divided into fallacies in dictione (equivocation, amphiboly, composition, division, accent, form of expression) and extra dictionem (accident, secundum quid, ignoratio elenchi, petitio principii, consequent, non-cause, many questions). The first systematic treatise on how arguments go wrong.

Why "the instrument" (INTERPRETATION): the six books form a complete toolkit for rational discourse itself, prior to any particular subject matter. The name Organon encodes a philosophical thesis: logic is the organon of thought, not a branch of it.

---

## 3. The syllogism and the laws of thought

### 3.1 Definition and structure

Aristotle defines the syllogism at the start of the Prior Analytics: "A syllogism is a discourse in which, certain things being posited, something other than what was laid down results of necessity because these things are so." FACT: Prior Analytics I.1, 24b18-20; wording confirmed via secondary sources quoting the passage.

A categorical syllogism has exactly three terms and two premises sharing a common term. (BACKGROUND)

- **Middle term**: appears in both premises, not in the conclusion; the hinge that links the extremes.
- **Major term**: predicate of the conclusion; its premise is the major premise.
- **Minor term**: subject of the conclusion; its premise is the minor premise.
- Propositions come in the four categorical forms A/E/I/O, possibly modalized.

### 3.2 Figures, moods, completeness

The figure is determined by the position of the middle term: first figure (middle is subject of major, predicate of minor; "perfect"), second figure (middle predicate of both), third figure (middle subject of both). Imperfect figures must be reduced to the first by conversion or reductio. The mood is the triple of proposition types (AAA, EAE, ...). (BACKGROUND)

Aristotle's method was exhaustive and eliminative: for each figure he went through possible premise-pairs and either produced a deduction or gave a counterexample with concrete terms. This is a genuine decision procedure for the fragment, arguably the first completeness result in the history of logic. (BACKGROUND; visible in An. Pr. I.4-6)

The medievals named the valid moods with mnemonic verses: Barbara, Celarent, Darii, Ferio (first figure); Cesare, Camestres, Festino, Baroco (second); Darapti, Disamis, Datisi, Felapton, Bocardo, Ferison (third). The vowels give the mood; consonants encode reduction rules. (BACKGROUND)

The famous "All men are mortal / Socrates is a man / therefore Socrates is mortal" is not Aristotle's own stock example; it is a later textbook standardization, and the singular minor premise fits his term logic awkwardly. (BACKGROUND)

Within his stated fragment (categorical, non-modal, three figures), Aristotle did enumerate the premise-pairs, prove the valid ones, and refute the rest by counterexample: a complete classification. The claim weakens for the modal syllogistic, which has gaps commentators from Theophrastus onward have tried to repair. (BACKGROUND)

(INTERPRETATION) The deeper limitation is expressive: the system cannot represent relational inferences (De Morgan's "every horse is an animal; therefore every head of a horse is a head of an animal"), multiple generality, or singular terms cleanly. These gaps are exactly what 19th-century logic exposed.

### 3.3 Laws of thought

The phrase "laws of thought" is a later label, not Aristotle's, but he articulates the principles the label covers. (BACKGROUND)

**Non-contradiction (PNC)**: stated and defended in Metaphysics Gamma, chapters 3-6: "It is impossible for the same thing to belong and not to belong to the same thing at the same time and in the same respect" (1005b19-20). Aristotle calls it "the most certain of all principles." His argument is elenctic, not demonstrative: a principle this basic cannot be proved from anything more basic. Instead he shows that anyone who denies PNC refutes themselves the moment they say something significant; the opponent's own speech act presupposes PNC. He also argues PNC is presupposed by action and deliberation: nobody walks to the edge of a well believing falling in is both good and not good indifferently. (BACKGROUND, Met. Gamma 3-6)

**Excluded middle (PEM)**: also in Metaphysics Gamma (ch. 7): "there cannot be an intermediate between contradictories." The sea-battle chapter of De Interpretatione 9 is the tension point: Aristotle appears to restrict bivalence for future contingents while preserving the law that either p or not-p. Interpretations differ sharply on whether he abandons, restricts, or distinguishes PEM from bivalence. (BACKGROUND)

**Identity**: Aristotle has no canonical "A = A" formulation of the Leibnizian sort. The principle appears operationally: in the definition of the syllogism's terms, in PNC itself, and in Gamma's discussion of signification, where a name must signify one and the same thing throughout an argument. Crediting him with a stated third law is an anachronism imported from the post-Leibnizian tradition. (BACKGROUND / INTERPRETATION)

---

## 4. Demonstration and episteme: the reasoning machine

### 4.1 What episteme is

Aristotle defines unqualified scientific knowledge (episteme haplos) as knowing "the cause on which the fact depends, as the cause of that fact and of no other, and, further, that the fact could not be other than it is." FACT: Posterior Analytics I.2, Mure translation. The proper object of episteme is what is necessary; contingent facts are not, strictly speaking, objects of demonstration. (FACT, same source)

Episteme is a state produced by demonstration (apodeixis), "a syllogism productive of scientific knowledge." This makes episteme a justified and explanatory state, closer to "understanding why" than to modern "justified true belief": the knower possesses the cause (the middle term), not merely the conclusion. (FACT / BACKGROUND)

### 4.2 The six conditions on demonstrative premises

In I.2 Aristotle lays down that the premises of demonstrated knowledge must be: (FACT, Posterior Analytics I.2)

1. True
2. Primary and indemonstrable
3. Immediate (no middle term through which they could be proved)
4. Better known than the conclusion
5. Prior to the conclusion
6. Causes of the conclusion ("as effect to cause")

He immediately qualifies "prior" and "better known": what is prior in the order of being (universal causes) is the reverse of what is prior to us (particulars nearest to sense). This distinction is the hinge of the whole epistemology: demonstration moves top-down from what is prior by nature; learning moves bottom-up from what is prior to us. (FACT / INTERPRETATION)

### 4.3 The regress problem

If every premise of a demonstration had to be demonstrated, either the chain regresses to infinity or it loops in a circle. Aristotle argues in I.3 that circular demonstration collapses "prior and better known" into sameness, and in I.19-22 that the predicative chains must terminate finitely. This is Aristotle's answer to the dilemma still known as the Munchhausen trilemma: justification cannot be infinite, cannot be circular, and so must rest on something indemonstrable. His originality is to make the stopping point epistemically privileged rather than arbitrary. (BACKGROUND / INTERPRETATION)

### 4.4 Induction (epagoge) and nous

"Demonstration cannot be the originative source of demonstration." FACT: Posterior Analytics II.19. Something non-demonstrative must supply the first premises.

Aristotle's account in II.19: knowledge-states arise "from sense-perception." The famous military simile: "It is like a rout in battle stopped by first one man making a stand and then another, until the original formation has been restored." Perception gives memory; repeated memories give experience; from experience the universal comes to rest in the soul. FACT: II.19. The Callias passage: "though the act of sense-perception is of the particular, its content is universal, is man, for example, not the man Callias." FACT: II.19.

"Thus it is clear that we must get to know the primary premises by induction." FACT: II.19. And since "except intuition nothing can be truer than scientific knowledge, it will be intuition that apprehends the primary premises." FACT: II.19. "Intuition" here translates nous.

(INTERPRETATION) The division of labor is exact: epagoge supplies the content, nous registers it as principle, apodeixis unfolds its consequences. Deduction is dependent twice over, on induction for its starting points and on nous for their certification. Aristotelian "induction" is not probabilistic generalization; it is the cognitive passage from perceived particulars to a universal seen as necessary. Whether that passage is ever legitimate as described is exactly what Hume later denies.

---

## 5. The Euclidean legacy and where the model broke

### 5.1 Euclid and the rationalist career

Euclid's Elements (c. 300 BCE, roughly a generation after Aristotle) opens with definitions, postulates, and common notions and derives 465 propositions by deduction alone: the most influential implementation of the demonstrative structure Aristotle theorized. Whether Euclid read the Posterior Analytics directly is debated; the safer claim is that the Elements embodies the same demonstrative ideal. For over two millennia the Elements was the paradigm of certain knowledge. (BACKGROUND / INTERPRETATION)

Descartes's Meditations (1641) pursue an explicitly foundationalist project; his Rules for the Direction of the Mind distinguishes intuitus and deductio, a recognizable descendant of Aristotle's nous/episteme pair. Spinoza's Ethics (1677) is presented ordine geometrico, with definitions, axioms, propositions, proofs, corollaries: the most literal attempt to extend the Euclidean-Aristotelian demonstrative form to metaphysics and ethics. (BACKGROUND)

(INTERPRETATION) Spinoza's gamble exposes the weak joint in the whole tradition: the certainty of a geometrically ordered system can never exceed the warrant of its axioms, and the axioms of metaphysics do not command the assent that Euclid's postulates did. The form survives scrutiny; the premises do not, precisely the asymmetry Aristotle flagged with his requirement that premises be true, not merely assumed.

### 5.2 Bacon, Hume, Popper

Francis Bacon's Novum Organum (1620), its very title a rebuke to Aristotle's Organon, rejected both sterile syllogism and hasty generalization, proposing instead a disciplined, eliminative induction: tables of presence, absence, and degrees, rising by gradual steps from experiment to "middle axioms." Bacon keeps the direction of Aristotelian epagoge but changes its engine: controlled experiment and systematic elimination replace perception-and-memory. (BACKGROUND / INTERPRETATION)

The original source of the "problem of induction" is Book 1, Part iii, Section 6 of Hume's Treatise of Human Nature (1739); a shorter version appears in Section iv of the Enquiry (1748). FACT: Stanford Encyclopedia of Philosophy, "The Problem of Induction." Hume's dilemma: all reasoning is either demonstrative or probable. The inference from observed to unobserved presupposes a Uniformity Principle; demonstrative reasoning cannot establish it (its negation implies no contradiction); probable reasoning cannot establish it without circularity. FACT: SEP, same entry.

(INTERPRETATION) Hume's argument is the inversion of Aristotle's solution. Aristotle held that repeated perception inductively implants a universal that nous grasps as necessary; Hume shows no reasoning can certify that step. What Aristotle attributed to a truth-capacitating faculty, Hume reattributes to custom and habit: psychology replaces epistemology at the foundation.

Popper's Logik der Forschung (1934; English The Logic of Scientific Discovery, 1959) accepted Hume's negative result and re-founded scientific method on deduction alone: bold conjectures tested by deducing observable consequences and attempting to falsify them. Corroboration is never confirmation. (BACKGROUND) See [[critical-rationalism]] for the Substrate's existing Popper node: "There is no inductive foundation. Hume's problem of induction is accepted and bypassed: science grows through conjectures and refutations."

(INTERPRETATION) Popper's break is with the verificationist reading of the demonstrative ideal. His model keeps Aristotle's logic (modus tollens is a valid deductive form) while abandoning Aristotle's epistemic ambition for natural science: empirical claims are never episteme in the strict I.2 sense, because they can always be other than they are. Falsificationism is, structurally, demonstration turned against hypotheses instead of in their service.

### 5.3 What survives

The axiomatic method not only survived in mathematics but was radicalized: Hilbert's Grundlagen der Geometrie (1899), ZFC set theory, and the formalist program treat axioms as stipulated starting points. Aristotle's form retained, his demand that axioms be self-evidently true of the world dropped. Godel's incompleteness theorems (1931) showed any consistent formal system strong enough for arithmetic contains truths it cannot prove: a formal echo, within mathematics itself, of Aristotle's point that not everything true is demonstrable from a fixed basis. Formal verification in computer science (Coq, Lean, Isabelle; CompCert) is the living descendant of apodeixis. (BACKGROUND)

(INTERPRETATION) What survives of Aristotle is the architecture: the distinction between principles and consequences, the demand for immediate starting points, the regress argument. What did not survive is the epistemic optimism about empirical content. Modern science reversed the polarity: deduction is certain but only as strong as freely chosen axioms; induction is indispensable but never certain. Aristotle wanted both at once; the history from Euclid to Popper is the story of being forced to choose.

---

## 6. Practical reason: phronesis, deliberation, choice

### 6.1 Phronesis (NE Book VI)

Phronesis (practical wisdom) is an intellectual virtue: a truth-attaining rational state concerned with action (praxis), with "what is good or bad for a human being." (BACKGROUND, NE VI.5, 1140a24-b30)

In NE VI Aristotle distinguishes five states by which the soul attains truth: techne, episteme, phronesis, sophia, nous. Key contrasts: (BACKGROUND)

- Episteme is demonstrative knowledge of what is necessary and invariable; phronesis concerns the variable and contingent sphere of action, hence "cannot be a science."
- Techne aims at poiesis (making something distinct from the activity); in praxis the end is the doing well itself, hence phronesis "cannot be an art."
- Sophia contemplates what does not change; phronesis is subordinate in dignity but indispensable for life.

FACT: SEP confirms practical wisdom "cannot be acquired solely by learning general rules" and differs from theoretical science.

Actions are always particular and situated; no universal rule can dictate what to do here and now. Practical wisdom "is concerned with particulars as well as universals" and becomes "more a matter of particulars as it becomes more practical." The practically wise person is marked by experience of particular cases. FACT: SEP: "to apply that general understanding to particular cases, we must acquire, through proper upbringing and habits, the ability to see, on each occasion, which course of action is best supported by reasons."

The young may master mathematics (whose objects are grasped by abstraction) but not practical wisdom, whose objects come through experience. (BACKGROUND, NE VI.8)

### 6.2 Deliberation (bouleusis) (NE III.3)

We deliberate not about ends but about what promotes ends (ta pros to telos). We deliberate about what is in our power and achievable by action. (BACKGROUND, NE III.3, 1112a18-1113a2)

The backward-chain model: the agent posits an end, asks how and through what means it can be achieved, and works backward through intermediate steps until reaching a first cause, an action now within the agent's power. The analysis runs backward in thought; the action runs forward in execution. The last thing found in the analysis is the first thing done in the deed. Aristotle explicitly compares this to geometrical analysis. (BACKGROUND, NE III.3, 1112b11-27)

### 6.3 Prohairesis (choice) (NE VI.2)

Prohairesis is "deliberate desire of things in our own power," the origin (arche) of action. It is neither appetite alone nor reason alone but the fusion of both: "desiderative reason" (orektikos nous) or "reasoned desire" (orexis dianoetike). (BACKGROUND, NE VI.2, 1139a31-b5)

For action to occur, reason must affirm the good as end and desire must pursue it. Virtue of character (which rectifies desire) and practical wisdom (which rectifies reasoning) are mutually implicating: "we cannot be fully good without practical wisdom, nor practically wise without moral virtue." (BACKGROUND, NE VI.13) FACT: SEP confirms: "Ethical virtue is fully developed only when it is combined with practical wisdom."

### 6.4 The practical syllogism

A piece of practical reasoning in syllogistic shape: a major premise stating a universal rule of the practical good; a minor premise subsuming a particular under that rule; a conclusion that is not a proposition but an action. FACT: Wikipedia, "Practical syllogism."

Aristotle's stock illustration (De Motu Animalium 7, 701a-b; echoed in NE VII.3): Major: "Dry food is good for every man." Minor: "I am a man; this is dry food." Conclusion: the agent acts, eats, immediately, if not prevented. (BACKGROUND, De Motu Animalium 701a10-33; NE VII.3, 1147a24-b10)

His striking claim: in theoretical reasoning, when the two premises are united, the soul must affirm the conclusion; in practical reasoning, when the two premises are united, the soul must at once perform the action. The necessity is not logical compulsion of a proposition but the quasi-automatic translation of completed practical reasoning into bodily motion. (BACKGROUND, De Motu Animalium 701a13-16)

The minor premise is the crux: the particular premise is supplied by aisthesis (perception), and hence can fail, be absent, or be overridden by appetite. This is why the practical syllogism is the natural site for analyzing akrasia. (BACKGROUND, NE VII.3)

### 6.5 The mean, the irreducibility of rules, akrasia

Ethical virtue is a hexis concerned with choice, lying in a mean relative to us, determined by logos, "as the practically wise person would determine it." The mean is not arithmetical moderation but hitting the right target: at the right time, toward the right objects, for the right reason, in the right way. (BACKGROUND, NE II.6, 1106b36-1107a2)

Because the subject matter is variable and particular, ethical generalizations hold only "for the most part" (hos epi to poly); no algorithm can specify in advance the right action. The decision "rests with perception" (en aisthesei he krisis). FACT: SEP section "Ethical Theory Does Not Offer a Decision Procedure."

Akrasia (weakness of will) is acting against one's better judgment. Socrates, in Plato's Protagoras, denies akrasia is possible: no one willingly does what he knows to be bad; apparent weakness is really ignorance. Aristotle grants the puzzle "flatly contradicts the appearances." His solution deploys the practical syllogism: the akratic agent has the universal premise ("do not taste this") but either lacks, suppresses, or fails to activate the minor premise ("this is that") under the pressure of appetite. Knowledge is present but "not present in the way in which one who has it but is not using it has it," like a man asleep, mad, or drunk. Akrasia is a failure of the particular, perceptual link in the chain, not of the universal rule. (BACKGROUND, NE VII.2-3; FACT: SEP confirms the locus in NE VII)

---

## 7. The modern afterlife

### 7.1 Logic after Frege

FACT: In 1879 Gottlob Frege published the Begriffsschrift, the first system of logic with quantifiers and variables capable of expressing multiple generality and relations: the birth of modern predicate logic. Confirmed via Wikipedia, SEP ("Frege... is often credited with inventing modern quantificational logic in his Begriffsschrift"), and Cambridge University Press.

Preceded by Boole (1847, 1854) and De Morgan's relational logic; followed by Peirce, Peano, and Russell and Whitehead's Principia Mathematica (1910-13). Frege's motivation was mathematical (the logicist reduction of arithmetic), not anti-Aristotelian; the displacement of syllogistic was a side effect. (BACKGROUND)

FACT: In the Preface to the Second Edition (B viii, 1787) of the Critique of Pure Reason, Kant writes that logic "has not been able to advance a single step" since Aristotle "and is thus to all appearance a closed and completed body of doctrine." Confirmed via Stanford course page and University of Dayton faculty publication.

(INTERPRETATION) The rupture was expressive, not merely notational: where Aristotelian logic analyzes propositions into subject-predicate pairs of terms, Fregean logic analyzes them into function-argument structure with iterated quantification. The De Morgan counterexample (horse heads), unprovable in syllogistic and trivial in predicate logic, became the emblem of what 2,000 years of "complete" logic could not say.

Where Aristotelian logic still lives: (BACKGROUND)

- Lukasiewicz's Aristotle's Syllogistic (1951) axiomatized the syllogistic as a deductive system; later work reconstructed it as a sound and complete fragment of monadic predicate logic.
- "Syllogistic fragments" of natural language (Pratt-Hartmann, Moss) are an active research area in logic and computational semantics.
- Syllogisms remain the standard stimulus in the psychology of deduction (mental-models theory, believability bias); empirical results show systematic errors on exactly the moods Aristotle flagged as invalid.
- The durable residue is less the syllogism as a calculus than Aristotle's framing discoveries: validity is a matter of form, letters can stand for arbitrary terms, invalidity is shown by countermodel, fallacies can be taxonomized.

### 7.2 Virtue ethics revival

FACT: G. E. M. Anscombe, Intention (1957), revived the practical syllogism as the core structure of intentional action; "Modern Moral Philosophy" (1958) coined "consequentialism" and called for a return to Aristotle's categories, launching the contemporary virtue-ethics revival.

FACT: Alasdair MacIntyre, After Virtue (1981), argues the Enlightenment project failed because it abandoned Aristotelian teleology; he explicitly restores phronesis and the virtues, framing them within "practices" and narrative unity.

Martha Nussbaum develops Aristotle's particularism, the priority of aisthesis and phronesis over rule-following, in The Fragility of Goodness (1986). (BACKGROUND)

### 7.3 Phronetic social science

FACT: Bent Flyvbjerg, Making Social Science Matter (2001, Cambridge UP), argues social science must model itself on phronesis, not episteme: abandon the predictive-theory ideal, focus on values, power, and concrete case knowledge.

### 7.4 The limits-of-rules debate in AI

FACT: Hubert Dreyfus, What Computers Can't Do (1972), argued that expert human intelligence is intuitive and context-dependent, not rule-governed symbolic manipulation. Terry Winograd (with Fernando Flores), Understanding Computers and Cognition (1986), extended this critique into AI design: intelligent behavior is embedded in a background of practices. (BACKGROUND / FACT)

(INTERPRETATION) The practical syllogism is structurally a means-end, backward-chaining scheme: from a goal (end) and a belief about the world (the particular premise), derive an actionable step. This maps onto classical STRIPS-style planning (goal regression) and onto the Belief-Desire-Intention architecture (Rao and Georgeff, 1991), where desires play the role of ends, beliefs play the role of the minor premise, and intentions play the role of prohairesis.

(INTERPRETATION) The debate over whether AI alignment can be achieved by explicit rule-following versus whether it requires something like trained judgment, context-sensitivity, and virtue-like dispositions maps onto the Aristotle-vs-rules dialectic. The analogy is suggestive, not an established scholarly mapping.

---

## 8. Where the mapping breaks

Intellectual honesty section. The thesis "Aristotle invented logic and practical rationality" holds, but the mapping to the present fails at specific points:

1. **The syllogism's expressive poverty.** The system Aristotle proved complete is a small fragment. Relational inference, multiple generality, and singular terms are beyond it. The Fregean rupture was not a correction of detail but a change of subject. (BACKGROUND / FACT)

2. **The modal syllogistic is broken.** Aristotle's necessity/possibility rules have gaps and apparent inconsistencies that commentators from Theophrastus onward have tried and failed to repair. His most original contribution is also his least sound. (BACKGROUND)

3. **Epagoge does not deliver necessity.** Aristotle's solution to the regress problem, induction implanting universals that nous grasps as necessary, is precisely what Hume showed cannot be certified by reason. The most optimistic joint in the epistemic architecture is the one that failed. (FACT for Hume; INTERPRETATION for the diagnosis)

4. **The practical syllogism is not a logic.** The "necessity" with which the soul acts when premises unite is not logical validity; it is a psychological or physiological compulsion. Treating it as inference licenses the BDI mapping only by analogy, and the analogy hides how much of the action is in the perceptual minor premise, the part no calculus captures. (BACKGROUND / INTERPRETATION)

5. **Phronesis resists the very formalization Aristotle invented for theory.** He is explicit that ethics holds only "for the most part" and that judgment "rests with perception." Any attempt to operationalize phronesis as a decision procedure betrays the doctrine. The modern phronesis revival (Flyvbjerg) inherits this tension: it is a research program defined by what it refuses to be. (BACKGROUND / INTERPRETATION)

6. **Akrasia remains contested.** Aristotle's resolution (the akratic fails to activate the minor premise) is one of several readings of NE VII, and the phenomenon itself, weakness of will against better judgment, is still debated in action theory without consensus. (BACKGROUND)

---

## 9. Compression points for synthesis

1. Aristotle invented logic by separating the form of an argument from its content; the syllogism (Prior Analytics I.1, 24b18-20) is the first completeness result in the history of logic.
2. The Organon was named by later commentators who held logic is the instrument of all philosophy, not a branch of it.
3. Non-contradiction (Metaphysics Gamma) is defended elenctically, not demonstratively: the denier refutes themselves by speaking.
4. Episteme requires premises that are true, primary, immediate, better known than, prior to, and causes of the conclusion (Posterior Analytics I.2).
5. Deduction cannot ground its own axioms; induction (epagoge) and nous supply first principles (Posterior Analytics II.19).
6. Hume's problem of induction (Treatise 1739) inverts Aristotle's solution: no reasoning certifies the passage from particulars to necessary universals.
7. Popper's falsificationism (1934/1959) keeps Aristotle's logic while abandoning his epistemic ambition for empirical science; see [[critical-rationalism]].
8. Phronesis (NE VI) is practical wisdom about particulars, irreducible to rules; judgment "rests with perception."
9. The practical syllogism (De Motu Animalium 701a; NE VII.3) concludes in action, not a proposition; its structure anticipates BDI agent architectures by two millennia.
10. Akrasia is a failure of the perceptual minor premise, not of the universal rule; the practical syllogism is the natural site for analyzing weakness of will.
11. Frege's Begriffsschrift (1879) displaced syllogistic by solving expressive problems (relations, multiple generality) Aristotle's system could not state.
12. The modern virtue-ethics revival (Anscombe 1957/1958, MacIntyre 1981, Flyvbjerg 2001) restores phronesis against rule-based ethics and rule-based social science.

---

## Sources

Verified live this session:

- Posterior Analytics I.2 and II.19, Mure translation: https://classics.mit.edu/Aristotle/posterior.1.i.html and https://classics.mit.edu/Aristotle/posterior.2.ii.html
- Stanford Encyclopedia of Philosophy, "Aristotle's Ethics" (Kraut): https://plato.stanford.edu/entries/aristotle-ethics/
- Stanford Encyclopedia of Philosophy, "The Problem of Induction": https://plato.stanford.edu/entries/induction-problem/
- Stanford Encyclopedia of Philosophy, "Frege's Logic": https://plato.stanford.edu/entries/frege-logic/
- Wikipedia, "Begriffsschrift": https://en.wikipedia.org/wiki/Begriffsschrift
- Wikipedia, "G. E. M. Anscombe": https://en.wikipedia.org/wiki/G._E._M._Anscombe
- Wikipedia, "After Virtue": https://en.wikipedia.org/wiki/After_Virtue
- Wikipedia, "Making Social Science Matter": https://en.wikipedia.org/wiki/Making_Social_Science_Matter
- Wikipedia, "Hubert Dreyfus's views on artificial intelligence": https://en.wikipedia.org/wiki/Hubert_Dreyfus%27s_views_on_artificial_intelligence
- Wikipedia, "Practical syllogism": https://en.wikipedia.org/wiki/Practical_syllogism
- nLab, "syllogism": https://ncatlab.org/nlab/show/syllogism
- PhilArchive, "What is a Syllogism?": https://philarchive.org/archive/EBRWAT
- Stanford course page, Kant Critique of Pure Reason Preface: https://web.stanford.edu/class/history34q/readings/Kant/CritiquePreface.html
- University of Dayton faculty publication quoting Kant Bviii: https://ecommons.udayton.edu/phl_fac_pub/54/
- Cambridge University Press, Frege's Begriffsschrift (1879): https://www.cambridge.org/core/books/frege/freges-begriffsschrift-1879-an-ideal-logical-language/FA3818464C5DBF050FC82EC946BD7392

Established record cited but not re-verified (verify before direct quotation):

- Bekker numbers for all Nicomachean Ethics citations (III.3, VI.2-13, VII.2-3, II.2/6/9) and De Motu Animalium 701a wording of the dry-food example.
- Plato, Protagoras 352b-357e (Socrates on akrasia).
- Nussbaum, The Fragility of Goodness (1986).
- Winograd and Flores, Understanding Computers and Cognition (1986).
- Rao and Georgeff, BDI (1991).
- Davidson, "Actions, Reasons, and Causes" (1963).
- Lukasiewicz, Aristotle's Syllogistic (1951), and the Smiley/Corcoran reconstruction lineage.
- Galen/fourth-figure attribution and its disputed status.
- Medieval mnemonic consonant encoding details.
- Euclid's Elements date (~300 BCE), structure, and proposition count.
- Descartes Meditations (1641), Principles (1644), Rules; Spinoza Ethics (1677).
- Bacon Novum Organum (1620), tables of presence/absence/degrees.
- Popper Logik der Forschung (1934) / Logic of Scientific Discovery (1959).
- Hilbert Grundlagen der Geometrie (1899); Godel incompleteness (1931); proof assistants and CompCert.
- Cognitive-science specifics (Johnson-Laird mental models, believability bias).
