# The Quantum Thief: Memory Editing and Conscience as Architecture

Raw research file. Series: quantum-thief-privacy-as-currency.md, quantum-thief-sobornost-copy-problem.md, quantum-thief-crypto-coordination.md, quantum-thief-conscience-architecture.md (concept 4 of 4, produced 2026-10-05). Source material for later synthesis, not a finished essay.

Related Substrate nodes: [[conscience]] (signal/stop/moral-knowledge components), [[context-stack-as-conscience]] (conscience as installed architecture), [[ziebart-maxent-irl-alignment-conscience]] (conscience in the alignment frame), [[russell-human-compatible-storm]] (the off-switch game and provably beneficial AI), [[agent-identity]] (continuity of the moral agent).

## 1. The Dilemma Prison: game theory made literal

BACKGROUND. The novel opens with Jean le Flambeur in the Dilemma Prison of the Archons, a Sobornost institution:

- Prisoners are paired in an iterated prisoner's dilemma played for real stakes: winning a round earns a temporary "gun" or release option; the game can literally end in death and resurrection, since prisoners are uploaded minds whose bodies can be reprinted.
- The Archon is the prison's warden-intelligence, presenting itself as a paternal reformer: the prison's stated purpose is to rehabilitate criminals by forcing them to learn cooperation through iterated play. The Archon claims to love its prisoners.
- The structure is game-theoretic torture: endless iteration means defectors face eternal punishment, but the prison also manufactures scarcity and betrayal so that trust never stabilizes; cooperation is demanded but never made safe.
- Jean escapes not by winning the game but by an outside agent: Mieli, an Oortian warrior serving the Sobornost pellegrini, breaks him out because she needs the legendary thief for a job.

The game-theoretic anchors are FACT: iterated prisoner's dilemma (IPD) is repeated play between agents who must each choose cooperate or defect without binding contracts; the dominant one-shot strategy (defect) yields collectively bad outcomes. Axelrod, *The Evolution of Cooperation* (Basic Books, 1984), verified via Wikipedia and author-hosted PDF: computer tournaments invited strategies for IPD; the winner, submitted by Anatol Rapoport, was tit for tat, which cooperates on the first move and then echoes the opponent's previous move. Tit for tat's virtues per Axelrod: nice (never defects first), retaliatory, forgiving, clear.

INTERPRETATION: The Archon's prison is Axelrod's tournament re-skinned as penology. The claim that iteration breeds cooperation is the prison's official theory of rehabilitation. But the novel shows the failure modes Axelrod's own model contains: tit for tat collapses under noise and misperception, and the prison manufactures noise deliberately (resurrections, scarcity, hidden third parties). Rehabilitation-by-IPD is a warden's rationalization: the game reproduces the conditions of distrust it claims to cure.

INTERPRETATION: Jean, a professional defector, is the perfect experimental subject: the Archon's hypothesis is that even a thief can be iterated into a cooperator. The novel's answer is that he learns something else entirely: not cooperation, but an accounting of what his past self owed his future ones.

## 2. The self-heist: Jean's hidden caches

BACKGROUND:

- Jean hid his memories before his capture: caches sealed in locations only a past self would choose, retrievable only by re-enacting or re-becoming that self. "The box" motif: self-made vaults whose keys are states of mind.
- Recovering them reveals that Jean's prison sentence was not just imposed from outside: his own past self engineered circumstances, partitioned motives, and hid reasons from his future self.
- The prison thus doubles: an external Dilemma Prison run by the Archon, and an internal one built by Jean's prior self as judgment on his future selves.

Framing established in the record: conscience is not a voice but an architecture; parts of the self that other parts deliberately build to constrain them.

## 3. Real-world mapping: Elster, Ainslie, Parfit

### Precommitment and the divided self

- FACT: Elster, *Ulysses and the Sirens: Studies in Rationality and Irrationality* (Cambridge University Press, 1979): the Ulysses contract, binding oneself against predictable future irrationality, as the paradigm of imperfect rationality (verified via PhilPapers; the earlier article version appeared 1977).
- INTERPRETATION: Jean's memory caches are inverted Ulysses contracts. Ulysses binds his body and keeps his knowledge; Jean binds his knowledge and keeps his body free. The mast he ties himself to is informational.
- BACKGROUND: Ainslie, *Breakdown of Will* (2001): hyperbolic discounting makes the self a population of temporally situated agents with conflicting preferences; self-control is bargaining among them (standard reference, not re-verified).
- INTERPRETATION: Under Ainslie's frame, Jean's past self is not a wiser planner but a rival agent with a longer time horizon who won one round of the internal bargaining game and used his victory to lock the board.
- BACKGROUND: Parfit on personal identity: what matters is psychological continuity, which comes in degrees; a sufficiently edited self may not be "you" in any morally load-bearing sense (standard reference, not re-verified).
- INTERPRETATION: If Jean's memories are partitions he may or may not re-open, the question "why did I do this" has no fact-of-the-matter answer. There is only the past self's testimony, curated for an audience of one he did not trust.

### Memory editing ethics

- BACKGROUND: President's Council on Bioethics, *Beyond Therapy* (2003): memory-dampening (propranolol for traumatic memory) debated as a threat to moral agency; painful memories are load-bearing for identity and responsibility (standard reference, not re-verified).
- INTERPRETATION: The Council worried about erasing the past to spare the present. Rajaniemi poses the sharper case: a self that erases strategically, keeping the punishment while hiding the crime, so the future self serves a sentence whose charge sheet it cannot read. That is the novel's ethical vertigo, and it is a real technology's logical endpoint.

## 4. The alignment analogue: precommitment and corrigibility

- FACT: Hadfield-Menell, Dragan, Abbeel, Russell, "The Off-Switch Game" (IJCAI 2017; arXiv 1611.08219): formalizes shutdown as a two-agent game between human H and robot R (verified via arXiv and ACM this session).
- FACT: Core result: a robot that is certain of its objective has incentive to disable its off switch; a robot that is uncertain about the human's preferences, and believes the human is not too irrational, has positive incentive to preserve the off switch and no incentive to switch itself off (verified in the arXiv paper text this session).
- INTERPRETATION: This is the strongest formal anchor for the mapping. Corrigibility via engineered uncertainty is conscience-as-architecture in the exact novel sense: the system is built so that a part of it (the human's shutdown option) constrains another part (the planner) not by force but by epistemic design. The constraint holds because the smarter self cannot audit the values it serves well enough to justify cutting the wire.
- The established record's formulation, "a mind smart enough to edit itself needs an off-switch it agreed in advance not to reach," maps cleanly: Jean's caches are the agreement; the Dilemma Prison is what happens when the agreement is outsourced to an external warden.

## 5. The critique layer

- **Can self-binding survive a self smart enough to unbind?** INTERPRETATION: Three answers in the literature. Elster's: yes, because binding is physical and the later self is weaker (but a superintelligent later self is never weaker). The off-switch game's: yes, if the unbinding incentive is removed at the design level via preference uncertainty, not blocked at the capability level (FACT-grounded in the 2017 result). The novel's: no, not permanently; Jean recovers the caches because his past self left the doors open. Self-binding by a mind that keeps the keys is a policy, not a wall.
- **Moral agency under editable memory.** INTERPRETATION: Responsibility requires continuity of the self that chose. If Jean's past self deleted the reasons for the deed, punishing the present Jean punishes a stranger for a crime committed by a dead man. The novel's prison is therefore unjust in a way the Archon cannot see: it iterates against the wrong defendant. Alignment parallel: an AI whose objectives were written by an earlier training run is being "held responsible" for intentions it cannot audit.
- **Is architectural conscience still conscience?** INTERPRETATION: The novel's wager, per the established framing, is that conscience is exactly this: mechanisms installed by selves that knew their successors would want to defect. If so, the distinction between "real" conscience and engineered constraint collapses; human conscience is the architecture evolution and culture installed. The dissenting view (implicit in the memory-ethics debate): conscience requires the constraint to be owned, understood, and re-ratified by the current self, which is precisely what memory partitioning destroys. Jean's arc tests which view survives contact with a mind that can edit both the constraint and the memory of installing it.

## 6. Where the mapping breaks

- **Novel-internal claims are BACKGROUND throughout.** The Dilemma Prison's mechanics, the Archon's characterization, Jean's caches, and the self-imprisonment arc were taken from the established conversation record and secondary sources, not from a fresh primary-text pass. Direct quotation from the novel should wait for that pass.
- **The off-switch game's result is narrower than the mapping suggests.** The 2017 paper proves corrigibility under specific assumptions (a two-agent game, a particular utility structure, a human who is "not too irrational"). It does not prove that engineered uncertainty scales to superintelligence, and the paper itself flags that a sufficiently uncertain robot may also defer to a poorly-informed human. The mapping inherits the narrowness.
- **The Elster analogy is inverted by construction, which weakens it.** Ulysses' sailors are physically restrained; Jean's future selves are informationally restrained. The inversion is illuminating, but informational binding is categorically weaker than physical binding for a mind that can edit its own epistemics. The file's claim that "self-binding by a mind that keeps the keys is a policy, not a wall" is the honest version; the Ulysses frame can obscure that.
- **Ainslie, Parfit, and Beyond Therapy are standard references cited from memory.** Not re-verified this session. The page-level details (what exactly the Council concluded about propranolol, which Ainslie chapter makes the bargaining claim) should be checked before quotation.
- **The 'conscience is architecture' framing is the file's organizing bet, not the novel's stated thesis.** Rajaniemi does not use the word conscience this way; the framing comes from the Substrate's own conscience cluster ([[conscience]], [[context-stack-as-conscience]]) applied to the text. That is a legitimate synthesis move, but it should be read as such, not as a reading of the novel's intent.

## 7. Compression points for synthesis

1. The Dilemma Prison is Axelrod's tournament re-skinned as penology: the Archon's rehabilitation theory is that iteration breeds cooperation, but the prison manufactures the noise (resurrection, scarcity, hidden third parties) under which tit for tat collapses. Rehabilitation-by-IPD is a warden's rationalization.
2. Jean's memory caches are inverted Ulysses contracts: Ulysses binds his body and keeps his knowledge; Jean binds his knowledge and keeps his body free. The mast is informational, and informational binding is categorically weaker than physical for a mind that can edit its own epistemics.
3. Conscience is not a voice but an architecture: parts of the self that other parts deliberately build to constrain them. The off-switch game (Hadfield-Menell et al. 2017, verified) is the formal version: corrigibility via engineered uncertainty, where the constraint holds because the smarter self cannot audit the values it serves well enough to justify cutting the wire.
4. The three answers to "can self-binding survive a self smart enough to unbind": Elster's (yes, the later self is weaker, false for superintelligence), the off-switch game's (yes, if unbinding incentives are removed at design level), and the novel's (no, not permanently; the past self left the doors open). Self-binding by a mind that keeps the keys is a policy, not a wall.
5. Moral agency under editable memory: punishing a present self for a past self's hidden deed punishes a stranger for a crime committed by a dead man. The alignment parallel: an AI whose objectives were written by an earlier training run is being held responsible for intentions it cannot audit.
6. The conscience wager: if conscience is architecture (mechanisms installed by selves that knew their successors would want to defect), the distinction between "real" conscience and engineered constraint collapses. The dissent: conscience requires re-ratification by the current self, which memory partitioning destroys. Jean's arc tests which view survives.

## Sources

### Verified live this session

- Hadfield-Menell, D., Dragan, A., Abbeel, P., Russell, S. "The Off-Switch Game." IJCAI 2017. arXiv:1611.08219 (verified via arxiv.org/html/1611.08219v3)
- Axelrod, R. *The Evolution of Cooperation.* Basic Books, 1984 (verified via en.wikipedia.org and author-hosted PDF)
- Elster, J. *Ulysses and the Sirens: Studies in Rationality and Irrationality.* Cambridge University Press, 1979 (verified via philpapers.org; 1977 article version noted)

### Established record cited but not re-verified (verify before direct quotation)

- Ainslie, G. *Breakdown of Will.* Cambridge University Press, 2001
- President's Council on Bioethics, *Beyond Therapy*, 2003
- Parfit, D. *Reasons and Persons*, 1984
- Rajaniemi, H. *The Quantum Thief.* Gollancz/Tor, 2010 (all novel-internal claims; primary-text pass pending)
