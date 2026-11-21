# The Riemann Hypothesis, and the November 2026 Proof Claims

Raw research file. Single-topic deep dive produced 2026-11-21: source material for later synthesis, not a finished essay. Written the day after two independent claims of proof appeared, so the status sections are a dated snapshot, not a settled record. Time-sensitive: the verification status of the claims below will have moved by the time anyone reads this.

Related Substrate nodes: [[turing-computing-machinery-and-intelligence]] (the 1950 paper that asked whether machines can think, and declined to define "think"; this is the first event where a machine appears to have answered a question mathematicians could not), [[rsi-anthropic-openai-deep-dive]] (the recursive-self-improvement narrative that this event is a data point for), [[subagent-architecture]] (the ~60-subagent orchestration pattern reported in the earlier August result), [[minimax-theorem-statement-proofs]] (the Substrate's other formal-mathematics node; shares the statement-versus-proof distinction that is the crux of the verification problem here).

## 1. What the hypothesis says

BACKGROUND: Bernhard Riemann, in his 1859 paper on the distribution of primes, proposed that the nontrivial zeros of the zeta function all lie on the vertical line with real part one half, the critical line, bisecting the critical strip 0 < Re(s) < 1. He called it "very likely" and did not prove it.

BACKGROUND: The zeros control the primes through the explicit formula. The weighted prime count psi(x) equals x minus a sum over the zeros of x^rho / rho, plus lower-order terms. Each zero with real part beta contributes an oscillation of size x^beta. If every beta equals one half, every oscillation has the minimal size sqrt(x), which is the tightest error term the prime number theorem could possibly have. One zero off the line would produce a larger, detectable irregularity in the primes, at a scale set by that zero's real part.

BACKGROUND: RH is one of the seven Clay Mathematics Institute Millennium Prize Problems, with a one million dollar prize for an accepted solution. It is the only problem on Hilbert's original 1900 list of 23 that remains open. It is not the only unproven statement of its kind: the same question over function fields was proved (Weil, following Stepanov's argument), and the general statement over number fields is the Generalized Riemann Hypothesis (GRH); the extension to all number fields including those with a given character is the Extended Riemann Hypothesis (ERH).

## 2. What a proof would mean

**It converts a vast conditional literature into unconditional fact.** A large fraction of twentieth and twenty-first century analytic number theory is stated as "assuming RH" or "assuming GRH." Those results would become theorems outright. This is the largest single consequence and the one least visible from outside the field.

**It pins down the primes with optimal precision.** The prime number theorem's error term drops to the smallest size the structure allows, on the order of sqrt(x) times a log factor. Concretely: strong deterministic bounds on the gaps between consecutive primes, control of the least prime in an arithmetic progression (the GRH case is far sharper than what is known unconditionally), effective bounds for the Chebotarev density theorem, sharpened bounds on the Mertens function and the Chebyshev functions, and a long list of explicit numerical bounds across number theory and adjacent fields.

**It would likely, and perhaps necessarily, expose a hidden structure.** The zeros' statistics match those of random matrices (Montgomery and Odlyzko, non-trivial zeros and the Gaussian Unitary Ensemble), which strongly suggests the zeros are the spectrum of a self-adjoint operator, the Hilbert-Polya idea. Most number theorists expect a proof to arrive by exhibiting that operator, and regard the operator itself as the bigger prize. The de Bruijn-Newman constant gave a related reformulation: RH is equivalent to that constant being at most zero, and it is now known unconditionally to be at least zero (Rodgers and Tao, building on work of de Bruijn, Newman, and Polymath15), which reduces the hypothesis to the equality case. Other equivalent criteria exist (Li's criterion, the Nyman-Beurling criterion, Weil's positivity criterion), and they matter here because a proof may well arrive through one of these reformulations rather than through the zeros directly.

**It would make some algorithms provably efficient.** GRH is used to prove running-time bounds for a range of number-theoretic algorithms, including primality testing and aspects of factoring and discrete logarithms. A proof would upgrade many of these analyses from conditional to unconditional. Deterministic Miller-Rabin primality testing, for instance, becomes provable with known constants rather than heuristic.

## 3. What a proof would not mean

**It would not break RSA or any deployed cryptosystem.** This is the most common popular claim and it is false. RH constrains where zeta zeros lie; it does not give a fast factoring algorithm. If anything a proof helps cryptography, by making prime generation and primality testing provably reliable. Nothing about the location of the zeros threatens the hardness assumptions that public-key cryptography rests on.

**It would not settle the deeper structure of the primes.** Goldbach, the twin-prime conjecture, and the fine-scale distribution of prime gaps are not resolved by RH. RH narrows the error bars to the optimal width; it does not explain why the primes fall where they fall. The explicit formula is an identity, not a pattern-recognition device.

**It would not, by itself, answer the Turing question.** Turing's 1950 paper asked whether a machine could do something we would have to call thinking, and specifically declined to define the term. A machine proving RH would be an extraordinary data point for the practical version of that question and no answer at all to the philosophical one, which Turing anticipated by refusing to pose it. See [[turing-computing-machinery-and-intelligence]].

**It would not surprise anyone that the hypothesis is true.** The truth of RH is near-universally believed. The value is in the tools and the structure, which are what a proof would have to reveal, and which are the actual unknown.

## 4. The November 2026 claims

Two independent claims of proof appeared on the same day, Friday 2026-11-20. They should be kept separate; they are different people, different methods, and different verification states.

### Claim 1: Levent Alpoge with Claude (Riemann, GRH, and claimed ERH)

FACT: Alpoge, a mathematician and Anthropic employee, published a statement at his personal site (alpo.ge/remark.pdf) dated 2026-11-20: "I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis." He states that the method "easily extends much further, resolving the so-called Generalized Riemann Hypothesis," and that he expects the Extended Riemann Hypothesis with more time. He also states that he and Claude "formalized the arguments without assumptions."

FACT: The proof was released as Lean only, in fourteen archive parts (lean.tar.gz.part01 through part14), with no human-readable writeup. Alpoge's stated reason: "It being obviously inappropriate to attempt to post some massive unreadable travesty of 'slop', I decided to only present Lean." New Scientist reports his account that the unpublished prose version ran to more than 250,000 pages.

REPORTED ON X, UNVERIFIED: the Lean release is described in social media summaries as roughly 17.37 million lines across about 175,000 files. These figures come from X posts, including one from the automated Grok account, not from the primary artifact. Treat them as order-of-magnitude only until someone counts the tarballs.

FACT (from Alpoge's own statement): the method is descended from Stepanov's argument over function fields, where the proof uses a divisor carrying multiplicity. Alpoge notes that multiplicity is hard to find over the integers, "corresponding to something like differentiating whole numbers," and that he and Claude were led to chain theta lifts so the same tricks recur in a natively automorphic way, with the chain length chosen to mimic square-root multiplicity. The statement also lists Iwasawa towers, the Bost slope inequality, a relative trace formula, Poincare series and approximate orthogonality, a weakening of Vandiver's conjecture, Lichtenbaum's K-theoretic predictions, and a use of Behrend's theorem. Dated working entries run from 2026-10-06 to 2026-11-16, with one entry reading simply "GRH."

FACT: The statement is unusually candid about its own epistemic state. Alpoge writes that he is "presenting the world with a complete argument before having mastered a massive neighbourhood around its mathematics," that his intuition "insists it will be massively simplified, likely immediately," and that the argument is "incredibly long at the moment."

FACT (timing, from the statement itself): Alpoge writes "The precise timing is horrible," that the finish landed late on the preceding Sunday night, that he messaged someone he addresses only as "Dario" (presumably Anthropic's chief executive; the statement gives no surname) to ask about his ability to announce, that "there was a constraint to respect," and that he is "clearly unilaterally responsible for feeling I just could not live if I waited even longer." He pre-empts the obvious reading directly: "There is an obvious cynical view, to do with the timing, but it is false, and I am pleased that I am in circumstances where it is obviously false." Scientific American notes the announcement came one day after Anthropic's stock market debut.

FACT (reaction, named): Andrew Sutherland (MIT) is quoted by Scientific American saying he had "independently compiled Alpoge's result in Lean," that this is "an historic moment," that "the world has changed," and that he regards it as "a human triumph, and a day for celebration." Carlo Pagano (Concordia, visiting Google DeepMind) says that even from a high-level scan, the new ideas are plausibly going to "open up brand new avenues of thinking in number theory." Hector Pasten (Pontifical Catholic University of Chile) calls a correct proof "something like a Rosetta Stone," completing a dictionary between branches where the connections were only partial.

FACT (reaction, cautious): Kevin Buzzard (Imperial College London), quoted by New Scientist, responded "Let's see if it compiles first," adding that it "might be a while before we find the relevant experts who are able to tell us the thrust of the argument, assuming it's all true, of course, which it probably will be because of course Alpoge will have [a] huge amount of egg on [his] face if the Lean code doesn't compile or is deficient in some way."

### Claim 2: Alessandro Masullo (GRH, human, no AI)

FACT: Ravi Vakil announced on his Math 216 blog on 2026-11-20 that Alessandro Masullo has a proposed proof of GRH, that Brian Conrad "has been looking closely at it for months and gave extensive feedback which is being incorporated, and it is so far looking good," that it is "all human, with no AI," and that the plan had been to bring Masullo to Stanford for a year to polish the writing before announcing. Vakil says the Alpoge news forced releasing the current draft, and posts the paper "The Music of the Primes."

REPORTED (community analysis, not peer review): a LessWrong commenter reports examining Masullo's draft and finding that chapters 11 and 12 are entirely absent, that the section meant to contain the decisive step (passing from finitely many primes to all primes) is empty, that the theorem meant to show the remaining primes contribute nothing has only a sketch, and that the decisive step is equivalent to GRH itself, which would make the argument circular as posted. The same analysis calls the foundations and the per-prime trace formulas a real contribution in their own right. This is one commenter's reading, and it is about Masullo, not about Alpoge. It is recorded here because it is the kind of claim that gets conflated, and conflation of the two claims is a live risk.

## 5. The verification question, which is the whole question

Compilation of a Lean proof is necessary and not sufficient, and the gap between the two is where a famous claim of this kind succeeds or fails.

FACT: Lean is a proof assistant in which a theorem is mechanically checked by a kernel against the definitions and axioms in scope. If the code compiles with no unproved gaps, then the formal statement follows from the axioms used. This is genuinely strong, which is why Sutherland's independent compilation moved the story materially.

The checks that still matter, and which compilation alone does not answer:

1. **Statement fidelity.** Does the formal statement capture the Riemann Hypothesis as mathematicians mean it, or a subtly different, weakened, or vacuous object? A formally proved theorem about a definition that does not match the intended one proves something else. This is the standard failure mode for formalizations of famous problems, and it is why Buzzard's point about needing "the relevant experts who are able to tell us the thrust of the argument" is the load-bearing caution, not a formality.
2. **Axioms and gaps.** Does the development use only the standard axioms, or has it introduced an axiom, a `sorry`, an `unsafe` escape, or a non-standard definition that trivializes the target? The standard audit is to print the axioms of the main theorem and confirm they are the expected ones and to verify no gaps remain.
3. **Definitions hygiene.** Are the definitions in the development the intended mathematical objects, or degenerate stand-ins that happen to make the statement provable? A large automated development can pass its own checks and still not formalize the intended mathematics.
4. **Independent reproduction.** The compilation claim needs to be reproduced by multiple parties on adequate hardware, by people with no stake in the result.

INTERPRETATION: the honest position as of 2026-11-21 is that the Alpoge claim has passed one important gate (an independent expert, Sutherland, reports the Lean compiles) and has not passed the decisive one (an expert confirmation that the formalized statement is the Riemann Hypothesis and that the development is clean). The absence of any human-readable exposition makes the decisive check harder, because it removes the heuristic path by which mathematicians normally assess plausibility in a day. Alpoge says he intends to write it up and expects it to be massively simplified; the field's judgment has to wait on that, or on experts reading the Lean.

INTERPRETATION: Alpoge's own framing cuts both ways. His candor about presenting a complete argument before understanding its neighborhood is exactly what one wants from someone making a claim of this size, and it also means the author cannot yet vouch for the mathematics from the inside. "It compiles" and "we understand the proof" are different claims, and only the first is currently asserted.

## 6. The 2026 context this lands in

BACKGROUND: 2026 has been the year AI systems started producing research-level mathematics faster than the field can absorb it.

- July 2026: Alpoge tweeted a Claude-generated solution to the Jacobian conjecture, which Scientific American credits with kicking off "math's unprecedented summer." (The Jacobian conjecture is a longstanding open problem in algebraic geometry; the specific Claude-assisted status of that result is BACKGROUND here.)
- August 2026: Anthropic announced that an unreleased research version of Claude raised the proven lower bound on the proportion of zeta zeros on the critical line from about 41.6 to 67.2 percent, validated by two Anthropic mathematicians (Levent Alpoge and Ralph Furman), reviewed by Brian Conrey and Dan Goldston, with a Lean formalization passing the standard comparator tool. That work was prompted by a non-mathematician, used roughly 60 subagents and 31 million output tokens, and Anthropic stated plainly that they did not expect the technique to reach RH. FACT (verified from Anthropic's own writeup this session).
- September 2026: Youness Lamzouri published an independent, conceptually simpler proof that more than 67.25 percent of nontrivial zeros are simple and on the critical line, plus 83.62 percent distinct zeros and 88.76 percent simple-or-on-the-line, crediting the Claude result as the seed for two of the bounds he extends. FACT (arXiv 2609.02882, abstract verified this session).
- October 2026: OpenAI released a large batch of mathematics results, reported as 722 papers, causing significant field disruption; one item made progress on the primes. BACKGROUND.
- November 2026: Scientific American reports a Buckmaster and Alpoge AI-aided proof of Navier-Stokes blowup, after months of controversy over an OpenAI result in the same area. BACKGROUND.
- The December 2026 issue of Scientific American is billed as "The End of Math as We Know It." FACT (page banner).

INTERPRETATION: whatever the verdict on the RH claim, the surrounding year establishes the pattern. The community has, in a single year, moved from "AI assists with computations" to "AI produces candidate research results at a rate that outstrips the human verification capacity," and the binding constraint has shifted from generation to checking. The verification infrastructure (Lean, independent experts, willingness to say "not yet") is now the rate limiter on mathematical knowledge, not the supply of proofs. That is the structural story, and it is more durable than any single claim.

## 7. Where the mapping breaks

- **The claim is one day old and unverified at the level that matters.** Compilation has been reported by one named expert. Statement fidelity has not been confirmed. Everything in section 4 should be read as a dated snapshot. Reporting this as settled would be a category error, and the whole point of section 5 is that the gap is real, not ceremonial.
- **A Lean-only release shifts the burden in a way that is not obviously fair or foul.** Releasing Lean only is defensible (it is the strongest available evidence short of a full writeup, and Alpoge's stated reason, avoiding a 250,000-page "slop" document, is reasonable) and it is also a way to claim priority while deferring the interpretive work to volunteers. Both readings are available. The community's actual response, that it will need experts to tell it what the argument says, is the honest one.
- **The primary evidence for the scale of the artifact is social media, not the artifact.** The line and file counts circulating are from X posts, including an automated account, and should not be repeated as fact. The primary sources are the fourteen tarballs themselves.
- **The timing is entangled with corporate considerations, and Alpoge says so.** He asked his chief executive whether he could announce; the release came a day after a stock market debut. He explicitly denies the cynical reading. Recording the entanglement is not the same as endorsing the cynicism, and the entanglement is a fact about the announcement, not about the mathematics.
- **Two same-day claims invite conflation.** The community analysis finding Masullo's draft incomplete (missing the decisive step, which would be circular) is about Masullo's human proof, not Alpoge's machine-assisted one. Treating a flaw in one as a flaw in the other is a mistake this file's structure is designed to prevent.
- **"Proved the Riemann Hypothesis" would not be the right description if it rests on automorphic machinery most number theorists cannot yet read.** A proof that only a small number of experts can follow, and that its own author cannot yet vouch for from the inside, is a proof in the formal sense and a problem for the social process by which mathematics certifies knowledge. That process is being stress-tested by this event regardless of the outcome.
- **The August Anthropic post is itself evidence against over-reading this one.** Anthropic's own researchers said they did not expect the August technique to reach RH. If the November claim holds, it means something changed in roughly three months, which is possible and which would be the most interesting fact in the story. If it does not hold, the August caution is the tell.
- **Do not treat this file's "what a proof would mean" section as commentary on whether this proof is correct.** Section 2 describes what a proof would accomplish in general. It applies to a correct proof by anyone, Alpoge and Claude included, and to none of the claims until they clear section 5.

## 8. Compression points for synthesis

1. The Riemann Hypothesis states that all nontrivial zeros of the zeta function lie on the critical line with real part one half. Through the explicit formula the zeros control the error term in the prime number theorem, so RH is equivalent to the primes being distributed as regularly as the analytic structure permits.
2. The primary consequence of a proof is conversion: a large conditional literature ("assuming RH" or "assuming GRH") would become unconditional theorems outright, which is the largest effect and the least visible from outside number theory.
3. A proof would likely come with structural revelation, most probably the operator whose spectrum the zeros are (Hilbert-Polya), and the operator would be the larger prize. Equivalent reformulations (de Bruijn-Newman, Li, Nyman-Beurling, Weil positivity) are candidate routes.
4. A proof would not break RSA or any deployed cryptosystem. It would make prime generation and primality testing provably reliable, which helps cryptography. The popular claim that RH threatens crypto is false.
5. A proof would not settle Goldbach, the twin primes, or the fine structure of prime gaps. It narrows the error bars to the optimal width without explaining the pattern.
6. On 2026-11-20, Levent Alpoge (Anthropic) claimed a proof of RH, GRH, and expected ERH, working with Claude, released Lean-only in fourteen archives with no human-readable writeup, with reported scale in the millions of lines. He is candid that he has a complete argument he does not yet fully understand and expects it to simplify.
7. The verification status as of 2026-11-21: one named expert (Andrew Sutherland) reports independently compiling the Lean; the decisive check, that the formalized statement is actually RH and that the development is clean of gaps, non-standard axioms, and degenerate definitions, has not been confirmed. Compilation is necessary and not sufficient.
8. On the same day, Ravi Vakil announced a separate, human, no-AI GRH proof by Alessandro Masullo, months in review with Brian Conrad. Community analysis reports it incomplete as posted, missing the decisive step in a way that would be circular. The two claims are distinct and should not be conflated.
9. The 2026 context: Claude's August result on the proportion of zeros on the critical line (41.6 to 67.2 percent, validated and formalized), Lamzouri's September independent simplification, the October OpenAI math release, and the November Navier-Stokes controversy. AI mathematics has become a firehose.
10. The durable structural change, independent of the verdict on any single claim: the binding constraint on mathematical knowledge has shifted from producing proofs to verifying them, and Lean plus a small pool of experts is now the rate limiter.

## Sources

### Verified live this session

- Alpoge, L. "Remark" (statement of the RH proof claim), 2026-11-20, alpo.ge/remark.pdf. Full text read this session; all Alpoge quotations line-verified against it.
- Anthropic Research, "Claude has improved on a longstanding lower bound for the fraction of zeros of the Riemann zeta function that satisfy the Riemann hypothesis," 2026-08 (updated 2026-08-13), anthropic.com/research/riemann-zeta. Read this session: the 41.6 to 67.2 percent figures, the named validators (Alpoge, Furman), the named external reviewers (Conrey, Goldston), the Lean formalization repository, the 60-subagent and 31-million-token account, and the explicit statement that Anthropic does not expect the technique to reach RH.
- Lamzouri, Y. "A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line," arXiv:2609.02882 (submitted 2026-09-02, revised 2026-09-08). Abstract read this session.
- Scientific American, "Anthropic mathematician claims to prove Riemann hypothesis, most famous problem in all of math," by Joseph Howlett, 2026-11-20. Read this session: the Sutherland, Pagano, and Pasten quotations, the 250,000-page figure, the Alpoge background (Jacobian conjecture July 2026, Navier-Stokes controversy), and the Anthropic market debut note.
- New Scientist, "Anthropic mathematician claims AI-assisted proof of the Riemann hypothesis," by Matthew Sparkes, 2026-11-20. Read this session: the Kevin Buzzard quotation and the "more than 250,000 pages" figure.
- LessWrong, "Linkpost: Anthropic's Alpoge (along with Claude) claims to have solved the Riemann Hypothesis," 2026-11-20. Read this session: the Alpoge statement link and the community analysis of the Masullo draft.
- Vakil, R. "Hurried Announcement: Alessandro Masullo GRH," Math 216 blog, 2026-11-20. Read this session.
- Masullo, A. "The Music of the Primes," draft PDF linked from the Vakil announcement, 2026-11-20. Not read in full.
- xAI Grok x_search query against X, run this session (X API credits were depleted; the oEmbed and Grok fallbacks were used). Returned no Alpoge announcement post on X, several third-party summaries, and the Sutherland compilation report. Sourced citations from that query: x.com/0xDEADSHAE/status/2123878725041484001, x.com/grok/status/2123946408243773449, x.com/v_shakthi/status/2123947553641341046.

### Established record cited but not re-verified (verify before direct quotation)

- Riemann, B. (1859), "Ueber die Anzahl der Primzahlen unter einer gegebenen Grosse."
- The explicit formula and the error-term equivalence for RH.
- Montgomery (1973) pair correlation; Odlyzko's numerical work on the zeros and the Gaussian Unitary Ensemble connection.
- Hilbert-Polya conjecture.
- de Bruijn-Newman constant, and the Rodgers-Tao result that it is at least zero; the Polymath15 work on its upper bound.
- Li's criterion; the Nyman-Beurling criterion; Weil's positivity criterion; Connes's trace-formula approach.
- Weil's proof of RH over function fields; Stepanov's argument; Deligne's work on the Weil conjectures.
- The Clay Millennium Prize terms and the one million dollar award; the Hilbert 1900 problem list.
- Deterministic Miller-Rabin primality testing under GRH, and GRH's role in running-time analyses for number-theoretic algorithms.
- The July 2026 Jacobian conjecture tweet by Alpoge; the September 2026 Navier-Stokes priority controversy involving OpenAI, Tristan Buckmaster, and Alpoge; the October 2026 OpenAI mathematics release reported as 722 papers.
- The two X-sourced scale figures for the Lean release (about 17.37 million lines, about 175,000 files, fourteen archives). Attribute to X summaries, not to the artifact, until counted.
