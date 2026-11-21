---
title: "Turing's Imitation Game: The 1950 Paper's Core Move"
tags: [finding, turing, ai, philosophy, computation, history]
related:
- ai-machine-soul
- accelerando-minds-as-software
- minimax-beyond-game-theory
- turing-1950-nine-objections
- turing-1950-child-machine-and-learning
source: research/raw/turing-computing-machinery-and-intelligence.md
ingested: 2026-11-21
---
# Turing's Imitation Game: The 1950 Paper's Core Move

## Key Points

**The original question is replaced, not answered.** Turing opens by proposing to consider "Can machines think?" and refuses to answer it. Defined to match normal use, the words would force the answer to come from "a statistical survey such as a Gallup poll. But this is absurd." So he substitutes the imitation game: three players, a man (A), a woman (B), an interrogator (C) who knows them only as X and Y, communicating by teleprinter so tone cannot help. The machine takes A's part, and the standard of success is comparative, not absolute: will the interrogator decide wrongly as often as with a human pair? The line usually quoted as the paper's opening, "The original question, 'Can machines think?' I believe to be too meaningless to deserve discussion," in fact sits in Section 6, after four sections of setup.

**The famous prediction is misquoted in a specific, checkable way.** Turing's stated belief is that in about fifty years it will be possible to program computers with storage of about 10^9 to play the game so well that "an average interrogator will not have more than 70 per cent chance of making the right identification after five minutes of questioning." The number is the interrogator's chance of being right; the machine's pass rate is the unprinted complement, roughly 30 percent. The string "30 per cent" does not occur anywhere in the text. The popular compression, "Turing predicted machines would pass the test by 2000," flattens a calibrated claim about a five-minute exchange into a binary. He also predicted that by century's end "one will be able to speak of machines thinking without expecting to be contradicted."

**The paper is about a possibility space, and says so.** Turing declines to test the machines of his day: "we are not asking whether all digital computers would do well in the game nor whether the computers at present available would do well, but whether there are imaginable computers which would do well."

**The load-bearing section is a theorem, not a conjecture.** Section 5 restates the universality argument of the 1936 paper for readers who had never heard of a Turing machine. Digital computers are discrete-state machines ("Strictly speaking, there are no such machines. Everything really moves continuously"), storage capacity is the base-2 logarithm of state count (the Manchester machine: about 2^165,000 states, capacity about 165,000 bits), and a digital computer "could mimic the behavior of any discrete-state machine." The consequence Turing draws is the collapse of machine diversity as a design problem ("it is unnecessary to design various new machines to do various computing processes"), which lets him fold the question onto one fixed machine C. INTERPRETATION: the philosophical test is bolted onto a mathematical theorem from 1936, and that joint is asserted rather than argued. Section 5 establishes that a computer can simulate a machine that behaves like a human; it does not establish that such simulation is thinking.

**The physical is deliberately excluded.** The interrogator cannot see, touch, or hear the competitors, which "draws a fairly sharp line between the physical and the intellectual capacities of a man" and makes "artificial flesh" pointless. The paper's method is equally indifferent to the machine's substance: that modern computers and nervous systems are both electrical is "only a very superficial similarity," and since "all digital computers are in a sense equivalent," electricity "cannot be of theoretical importance." What to look for instead: "mathematical analogies of function."

**Two concessions in Section 1.2 are the paper's weak joints.** First, the odds are weighted against the machine because a man pretending to be a machine "would be given away at once by slowness and inaccuracy in arithmetic," which Turing calls "a very strong one" and answers only by noting that if a machine can play anyway the objection need not trouble us. Second, the machine's best strategy might not be imitation of a man at all: Turing grants "this may be," says he thinks it unlikely, and assumes it away for the paper. If he is wrong, the test measures conformity to an arbitrary target rather than intelligence. Most later objections that the test measures deception rather than thought are descendants of this concession.

**The three-part machine vocabulary survives.** The store (the human computer's paper and memory), the executive unit (the individual operations), and the control (obedience to the "table of instructions" in the right order) are still the architecture. The two instruction types that make programs possible arrive with the cobbler's-mother analogy: unconditional jump and conditional branch, a notice stuck up once and destroyed when its purpose is served. Babbage's Analytical Engine is named the ancestor ("he had all the essential ideas," never completed, about 100 times slower than the Manchester machine), and a machine with unbounded store is an "infinitive capacity" machine, with "no theoretical difficulty."

## Open Questions

- The universal-machine license covers mimicking discrete-state machines. No argument in the paper bridges from "can simulate" to "can think," and the bridge is the paper's central unstated premise rather than a defended claim.
- The game's comparative standard inherits its reference class from human pairs. Nothing in the paper asks whether a mind that thinks in ways no human shares would be detectable at all.
- The paper is explicitly about imaginable machines. Every later dispute about whether a particular system "passes" is arguing about a question the paper declined to pose.

## Source

`research/raw/turing-computing-machinery-and-intelligence.md` (sections 1.1-1.4; compression points 1-3). Primary text: A. M. Turing, "Computing Machinery and Intelligence," *Mind* 49(236): 433-460, October 1950, read this session as a pdftotext extraction of the Mind reprint; all quotations line-anchored, OCR corruptions catalogued and corrected in the raw file. Related Substrate nodes: [[ai-machine-soul]] (Chinese Room and machine consciousness), [[accelerando-minds-as-software]] (minds as software, modern LLM Turing-test evidence), [[minimax-beyond-game-theory]] (Turing's Turochamp and the game-tree lineage the paper sits inside).
