---
title: "The Child Machine: Turing's Learning-Machine Section as the Field's Real Ancestor"
tags: [finding, turing, ai, machine-learning, reinforcement-learning, history, philosophy]
related:
- turing-1950-imitation-game
- turing-1950-reception-and-llm-afterlife
- subagent-architecture
- accelerando-minds-as-software
source: research/raw/turing-computing-machinery-and-intelligence.md
ingested: 2026-11-21
---
# The Child Machine: Turing's Learning-Machine Section as the Field's Real Ancestor

## Key Points

**Section 7 opens with a confession.** Turing introduces Learning Machines, the paper's final section, by admitting he has no positive case: "I have no very convincing arguments of a positive nature to support my views. If I had I should not have taken such pains to point out the fallacies in contrary views." INTERPRETATION: the paper's most consequential section is the one he rates lowest.

**The child machine is the proposal.** Instead of programming an adult mind, simulate a child's and educate it: "Instead of trying to produce a programme to simulate the adult mind, why not rather try to produce one which simulates the child's? If this were then subjected to an appropriate course of education one would obtain the adult brain." The child brain is "something like a notebook as one buys it from the stationer's. Rather little mechanism, and lots of blank sheets."

**The evolutionary mapping is explicit, and it is the ancestor of machine learning as search.** Structure of the child machine is hereditary material; changes of the child machine are mutation; natural selection is the judgment of the experimenter. The advantage over biology is that the experimenter "is not restricted to random mutations. If he can trace a cause for some weakness he can probably think of the kind of mutation which will improve it." Learning itself is framed as search: it "may be regarded as a search for a form of behaviour which will satisfy the teacher."

**Reward and punishment are stated operationally, without any machinery of feeling.** "The machine has to be so constructed that events which shortly preceded the occurrence of a punishment signal are unlikely to be repeated, whereas a reward signal increased the probability of repetition of the events which led up to it. These definitions do not presuppose any feelings on the part of the machine." He reports an experiment: "I have done some experiments with one such child machine, and succeeded in teaching it a few things, but the teaching method was too unorthodox for the experiment to be considered really successful." INTERPRETATION: the reinforcement-learning formulation precedes the term by decades.

**He also sees the bandwidth problem in reward-only teaching.** If reward and punishment are the only channel, the information transferred cannot exceed their count. The illustration is a child learning "Casabianca" by Twenty Questions with a blow for every no. The fix is the one the field adopted: additional "unemotional" channels, a symbolic language through which orders travel, which "will diminish greatly the number of punishments and rewards required."

**The randomness argument is a search argument.** A random element belongs in a learning machine because with many satisfactory solutions the random method beats the systematic one. Evolution uses the same trick, and there "the systematic method is not possible. How could one keep track of the different genetical combinations that had been tried, so as to avoid trying them again?"

**Opacity is named as a property, not a defect.** The teacher of a learning machine "will often be very largely ignorant of quite what is going on inside, although he may still be able to some extent to predict his pupil's behavior," and most programmes "will result in its doing something that we cannot make sense of, or which we regard as completely random behaviour." Intelligent behaviour "presumably consists in a departure from the completely disciplined behaviour involved in computation, but a rather slight one, which does not give rise to random behaviour, or to pointless repetitive loops." Human fallibility comes for free: a machine educated by teaching acquires it "in a rather natural way, i.e., without special 'coaching'." INTERPRETATION: the observation held; the valuation flipped. The field now spends substantial effort trying to reverse exactly this condition under the name interpretability. His Manchester demonstration agrees: a 1,000-unit programme whose replies he defies anyone to predict from prior outputs.

**The learning paradox is resolved by ephemerality, not by hierarchy.** A machine whose rules change looks paradoxical, since rules of operation should describe completely how it reacts whatever its history. Turing's answer: the rules that change "are of a rather less pretentious kind, claiming only an ephemeral validity," with the Constitution of the United States as the analogy.

**The piano string and the atomic pile.** Against Lady Lovelace, an injected idea either dies away (the piano string) or, in a supercritical mind, becomes "a whole 'theory' consisting of secondary, tertiary and more remote ideas." The question becomes "Can a machine be made to be supercritical?" The skin-of-an-onion analogy follows: strip the mechanically explicable functions and you reach either the real mind or "the skin which has nothing in it," in which case "the whole mind is mechanical." Turing flags both paragraphs honestly as "recitations tending to produce belief."

**The close is the field's unfinished-work statement.** He declines to pick the starting domain, whether abstract activity like chess or sense organs plus English, and says both should be tried: "We can only see a short distance ahead, but we can see plenty there that needs to be done."

**The blank-slate premise is where the section is empirically thin.** INTERPRETATION: the architecture Turing sketched, learn rather than hand-code, was right; the cognitive premise he rested it on, an infant mind as "rather little mechanism, and lots of blank sheets," is the opposite of how the systems that actually work are built. Pretraining on vast corpora bakes priors in by scale.

**The 1948 report is the sibling document, not the same paper.** "Intelligent Machinery" (National Physical Laboratory, judged too speculative to publish in his lifetime, first published 1969 in Meltzer and Michie's *Machine Intelligence 5*) proposes the "unorganised machine," A-type and B-type randomly connected networks of simple units with modifiable connections, plus training by genetical search and by reward and punishment. Copeland's 1996 paper "On Alan Turing's Anticipation of Connectionism" treats it as the first explicit proposal of connectionist machine learning. INTERPRETATION: 1948 is an engineering-programme document arguing for connectionist learning; 1950 is a philosophy paper that replaces a question with a test and answers nine objections. The child machine is the thread through both.

## Open Questions

- The child machine's education problem is stated, not solved. Turing names reward and punishment, unemotional channels, and randomness, and reports only that his own teaching experiments were too unorthodox to count.
- The blank-slate assumption and the learning-from-data conclusion point in opposite directions. The section is right that capability would come from learning and wrong about what the learner starts with.

## Source

`research/raw/turing-computing-machinery-and-intelligence.md` (section 1.6; sections 2-3 for the 1936 and 1948 antecedents; compression points 7-8). All quotations line-anchored to the Mind reprint extraction read this session; the 1948 report and Copeland 1996 are cited in the raw file from the established record. Related Substrate nodes: [[subagent-architecture]] (learning and teaching as delegated processes), [[accelerando-minds-as-software]] (minds as software).
