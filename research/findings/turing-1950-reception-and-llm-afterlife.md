---
title: "Reception and Afterlife: From Mind to the LLM Turing-Test Headlines"
tags: [finding, turing, ai, philosophy, history, reception, benchmarks]
related:
- turing-1950-imitation-game
- turing-1950-nine-objections
- ai-machine-soul
- rsi-anthropic-openai-deep-dive
source: research/raw/turing-computing-machinery-and-intelligence.md
ingested: 2026-11-21
---
# Reception and Afterlife: From Mind to the LLM Turing-Test Headlines

## Key Points

**The venue shaped the reception.** *Mind* is a philosophy journal, not a computing venue, so the paper entered the philosophy-of-mind literature first and the computing literature second. That is why it reads as much as a philosophical taxonomy (theological, consciousness, Lovelace) as an engineering programme, and why uptake was slow: "Turing test" was not coined until later, gaining currency in the 1960s and 1970s. Turing returned to the theme in a 1952 BBC radio discussion with Newman, Braithwaite, and Jefferson, "Can Automatic Calculating Machines Be Said to Think?"

**The paper did not name the field.** The phrase "artificial intelligence" does not appear in it, verified this session by count: zero occurrences. Turing's vocabulary is "thinking machines," "digital computers," "machines," and, for the human counterpart, "human computer." The term arrives with McCarthy's coinage in the September 2, 1955 Dartmouth proposal for the 1956 summer workshop organised by McCarthy, Minsky, Rochester, and Shannon. INTERPRETATION: Dartmouth did not name the field in response to this paper; the coinage was also chosen partly to distance the project from Wiener's "cybernetics." The 1950 paper is a canonical antecedent, not the proximate trigger.

**The institutionalization of the test was a prize nobody won.** The Loebner Prize launched in 1990 by Hugh Loebner with the Cambridge Center for Behavioral Studies in Massachusetts, in standard Turing-test format, first contest at the Computer Museum in Boston, with a $100,000 prize (plus a smaller $25,000 one) offered for a program passing the full test. It was never awarded. The contest ran annually until 2019, when the format changed.

**The critiques that stuck target sufficiency, not possibility.** Searle's Chinese Room ("Minds, Brains, and Programs," *Behavioral and Brain Sciences*, 1980) attacks the strong-AI hypothesis: a correctly programmed computer with the right inputs and outputs thereby has a mind. Note the shape of the claim: Searle does not say the test cannot be passed; he says passing it would not establish understanding, because syntax is not sufficient for semantics. Block's Blockhead ("Psychologism and Behaviorism," *Philosophical Review*, 1981) is the sharpest form of the same family, a giant lookup table of all possible conversations passing the test with no intelligence behind it. Dreyfus (*What Computers Can't Do*, 1972) attacks the paper's central methodological choice head-on: behaviourism that misses embodiment, context, and know-how. Weizenbaum's ELIZA (1966) and the "ELIZA effect" is the standing demonstration of how cheaply superficial text behaviour is mistaken for understanding.

**The standard defenses are equally settled, and they are Turing's own.** The test is an operational criterion, a workable substitute for a question he judged meaningless, not a definition of mind. Passing is a sufficient condition for attributing thought, not a necessary one. And the "polite convention that everyone thinks" that he names in the consciousness objection is simply extended to machines. Later variants add channels rather than arguments: Harnad's Total Turing Test adds perception and action to the text channel.

**The modern headline proves less than it looks.** The LLM era renewed the "does it pass?" question sharply. Microsoft Research's 2023 "Sparks of Artificial General Intelligence" argued early GPT-4 shows sparks of general intelligence, and a 2023-24 study by Jones and Bergen found human judges could not reliably distinguish GPT-4 from a human in a five-minute two-player imitation game, widely reported as a quasi-pass. INTERPRETATION: passing was always a low bar, and Turing never equated passing with thinking. He replaced the original question precisely because he found it meaningless. The headlines show that the operational substitute has been satisfied, which is what he said would eventually happen, and settle nothing about "Can machines think?" Both the headline and the shrug were priced into the paper.

**The paper's most consequential legacy is not the test.** Section 7 anticipates machine learning and reinforcement learning: a child programme plus an education process, the evolutionary mapping, the operational reward-and-punishment rule, the random element in search, and the teacher's ignorance of the machine's internals. INTERPRETATION: for the field that actually arrived, the learning section matters more than the game.

**Where the mapping breaks, the failures are specific and useful.** The universality argument proves machines can mimic machines, not that a mimicking machine thinks, and the joint between theorem and test is asserted rather than argued. The behaviourism is deliberate: objection 4 answers the consciousness objection well and answers Blockhead not at all. The anthropocentrism is built in, since the machine must imitate a man, so nothing in the paper asks whether a mind that thinks in ways no human shares would be detectable. The diagnosis of the bottleneck was wrong: Turing believed the problem was "mainly one of programming" and estimated about sixty workers for fifty years at his own rate of a thousand digits of programme a day. Progress came instead from learning from data at scale, which is the child machine's other half. The clearest place where his forecast of how the work would go was beaten by his own better idea.

**The famous quotations are less stable than they look.** The Lovelace line circulates with a word ("whatever") that this text does not contain, and the paper dates her memoir 1842 where the standard date is 1843. The year-2000 prediction is routinely quoted as an unqualified 30 percent when the text prints a 70 percent correct-identification rate over five minutes. The extraction has no superscripts, so every exponent had to be reconstructed. INTERPRETATION: quotations from this paper should be checked against a clean print, not against summaries, including this one.

**What the paper does not contain is as telling as what it does.** No definition of intelligence. No engagement with embodiment, grounding, or the source of meaning in symbols, all later loci of critique. No consideration of data or scale as the engine of capability. And no theory of why the imitation game, of all possible operational tests, should be the one that tracks what we care about. INTERPRETATION: a superb piece of philosophical hygiene built around a criterion never argued for at the level its mathematics is argued at.

## Open Questions

- The question of which critique family survives a system that is trained rather than programmed is unresolved: Searle and Block target symbol manipulation, and neither addresses learned representations directly.
- Whether any operational test can carry the weight the imitation game was asked to carry remains open, and the paper's own answer (the alternative is solipsism) is a reply about humans, not about tests.
- The Jones and Bergen figure carried in the sibling node [[accelerando-minds-as-software]] (GPT-4.5 judged human 73 percent of the time in five-minute text Turing tests) is UNVERIFIED there and carried forward here with the same flag. Re-check the study before any hard claim rests on it.

## Source

`research/raw/turing-computing-machinery-and-intelligence.md` (sections 2-5; compression points 9-10). Searle 1980 and the phrase count verified this session; Block 1981, Dreyfus 1972, Weizenbaum 1966, Harnad's Total Turing Test, Loebner Prize details, and the Jones and Bergen study are cited from the established record in the raw file and flagged for re-verification. Related Substrate nodes: [[ai-machine-soul]] (Chinese Room and replies), [[rsi-anthropic-openai-deep-dive]] (the capability-progress narrative the LLM passes feed).
