---
title: "What Is a Protocol?"
tags:
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/what-is-a-protocol.md
---

# What Is a Protocol?

_Deep research into protocols as technology, culture, and coordination mechanism._

---

## Etymology: The First Sheet Glued On

The word "protocol" traces to the Greek **πρωτόκολλον (prōtokollon)**, meaning "first sheet glued onto a manuscript." Breaking it down:

- **πρῶτος (prōtos)**: first
- **κόλλα (kolla)**: glue

In ancient manuscript production, the protokollon was the first page affixed to a papyrus roll. It contained metadata: the document's contents, authentication marks, notes on provenance. It was not the content itself but the frame that made the content legible and trustworthy.

This etymology reveals something essential: **a protocol is not the message but the structure that makes the message possible.** It is the glue that holds things together, the first layer that establishes context before meaning can flow.

The word evolved through Medieval Latin (_protocollum_: "draft, original copy of a treaty") to French (_protocole_: "formula of diplomatic etiquette") before arriving in English around 1540 as "draft of a document" and by 1896 as "diplomatic etiquette."

The computing sense, "rules for data exchange," emerged in 1967 at the UK National Physical Laboratory. The general sense of "conventional proper conduct" is attested from 1952.

---

## The Timeline of Technical Protocols

### Prehistory: Telegraph and Telephone (1830s–1960s)

Before computer networks, there were communication protocols:

- **Morse code (1837)**: A protocol for encoding text as electrical pulses. Agreement on timing, spacing, and character mappings.
- **Telephone switching protocols**: Operators followed strict procedures for connecting calls. Human protocols for routing human voices.
- **Telex (1933)**: Standardized message exchange between teleprinters across different networks.

These were protocols in the full sense: agreed upon rules enabling communication between parties who might never meet.

### The Birth of Packet Switching (1960s)

**1961**: Leonard Kleinrock publishes mathematical theory of packet switching at MIT.

**1965–1966**: Donald Davies at the UK National Physical Laboratory conceives and names "packet switching." His team coins the term "protocol" in a computing context.

**April 1967**: Roger Scantlebury and Keith Bartlett write "A Protocol for Use in the NPL Data Communications Network." This is the first use of "protocol" in modern data communications.

**1969**: ARPANET goes live. Four nodes: UCLA, Stanford, UCSB, University of Utah. The 1822 protocol, written by Bob Kahn, defines host to IMP communication.

### Protocol Wars: The 1970s

**1972**: Telnet protocol introduced, enabling remote terminal access.

**1973**: File Transfer Protocol (FTP) specified.

**1974**: Vint Cerf and Bob Kahn publish "A Protocol for Packet Network Intercommunication," describing TCP. Still a monolithic design at this point.

**1974**: IBM releases Systems Network Architecture (SNA), a proprietary protocol suite.

**1975**: DEC releases DECnet. The "battle for access standards" begins.

**1976**: X.25 standard adopted by CCITT for public data networks. Connection oriented, virtual circuits. This becomes the European standard.

**1978**: TCP split into TCP and IP. The modular architecture emerges.

**1979**: Yogen Dalal at Xerox develops XNS (Xerox Network Systems).

### The Standards War: 1980s

**January 1980**: TCP and IP published as RFCs and DOD standards simultaneously.

**January 1, 1983**: "Flag Day." ARPANET cuts over to TCP/IP. The date was set three years in advance. Every host had to be ready.

**1984**: ISO publishes the OSI (Open Systems Interconnection) reference model. Seven layers, top to bottom: Application, Presentation, Session, Transport, Network, Data Link, Physical.

The OSI model was elegant, comprehensive, and backed by governments. France, West Germany, the UK, and the US Department of Commerce mandated OSI compliance. Even the DOD planned to transition from TCP/IP to OSI.

But TCP/IP was already running. Already deployed. Already working.

**1989**: The Internet protocol suite is complete (RFC 1122, RFC 1123). TCP/IP wins by adoption, not decree.

**1990s**: The Protocol Wars end. TCP/IP becomes the de facto global standard. OSI remains a teaching tool.

### The Lesson

> "The OSI model was designed by committee. TCP/IP was designed by running code."

Standards can be mandated, but protocols ultimately win through adoption. A protocol that runs beats a protocol that is perfect on paper.

### The Web Era (1990s–2000s)

**1991**: HTTP/0.9 (Tim Berners Lee). Hypertext over TCP/IP.

**1996**: HTTP/1.0 (RFC 1945).

**1997**: HTTP/1.1 (RFC 2068). Still the dominant version for most of the web's history.

**1999**: 802.11b (Wi-Fi). Wireless networking standardized.

### The Blockchain Era (2008–present)

**2008**: Satoshi Nakamoto publishes the Bitcoin whitepaper. Bitcoin is a protocol for trustless value transfer. Consensus without central authority.

**2015**: Ethereum launches. Smart contracts: protocols that execute themselves. Agreements encoded as code.

**2020s**: Layer 2 protocols, rollups, bridges. Protocols layered on protocols, all the way down.

---

## Protocols in Non-Technical Culture

Technical protocols inherit from older human traditions. The word itself came from diplomacy. But protocol as a concept, agreed upon rules for coordination, is as old as human civilization.

### Diplomatic Protocol

Diplomatic protocol is "the etiquette of diplomacy and affairs of state." It specifies:

- How to address a head of state
- The order of precedence at official functions
- How ambassadors are received and accredited
- Gift exchange procedures
- Treaty signing ceremonies

**Key insight**: Diplomatic protocol "creates space where meetings can take place." The rules don't limit interaction; they enable it. By making behavior predictable, participants can focus on substance rather than form.

The paradox: constraint creates freedom. When everyone knows the rules, no one wastes energy on uncertainty.

### Religious Protocol (Liturgy)

Every major religion has protocols for worship:

**Judaism**: Shabbat rituals, the Seder, the use of Hebrew in prayer, the handling of Torah scrolls, the structure of synagogue services.

**Christianity**: The liturgy. Call and response. Communion protocols that vary by denomination but share deep structure. The church calendar.

**Islam**: Wudu (ritual washing), the five daily prayers with prescribed postures and recitations, the Hajj with its precise sequence of rituals, the protocols of Ramadan.

These are not mere customs. They are protocols in the technical sense: specified behaviors that enable coordination across time and space. A Jew in Morocco and a Jew in New York can perform the same Seder because the protocol is documented and transmitted.

### Indigenous Cultural Protocols

Indigenous peoples worldwide maintain protocols for:

- **Welcome and acknowledgment**: How to greet guests, acknowledge country, introduce oneself
- **Ceremony**: Who may participate, what must be said, when silence is required
- **Knowledge transmission**: Who may share certain stories, under what conditions
- **Decision making**: Consensus processes, speaking order, the role of elders
- **Gift and reciprocity**: Tobacco offerings, the timing and meaning of gifts

**Key insight**: Indigenous protocols often protect relationships, not just transactions. Protocol violation isn't just a faux pas; it damages the fabric of connection.

### Social Etiquette

Modern etiquette traces to the court of Louis XIV. Frustrated by aristocrats trampling his gardens at Versailles, he posted signs (étiquettes) with rules. The word came to mean the rules themselves.

Etiquette protocols govern:

- Greetings and introductions
- Table manners
- Dress codes
- Correspondence
- Ceremonies (weddings, funerals, graduations)

After the French Revolution, aristocrats fled to England, carrying their protocols with them. The Industrial Revolution created new wealth that sought legitimacy through adopting upper-class protocols. Finishing schools trained the middle class to pass.

### Scientific Protocol

Scientific research runs on protocols:

- **Experimental protocols**: Precise procedures that enable replication
- **Peer review protocols**: How papers are submitted, reviewed, revised
- **Clinical trial protocols**: Regulatory frameworks for medical research
- **Laboratory safety protocols**: Procedures to prevent accidents

Scientific protocols serve a specific function: enabling verification. If I can follow your protocol and get the same result, your finding is real. The protocol is what makes science reproducible.

---

## What Protocols Do

Across all these domains, protocols serve common functions:

### 1. Enable Coordination Without Central Authority

Protocols let parties who don't know each other, who may never meet, who may not even share a language, coordinate behavior. The protocol is the shared reference that makes interaction possible.

The Internet has no CEO. HTTP has no owner. Yet billions of devices coordinate because they share protocols.

### 2. Reduce Transaction Costs

Without protocols, every interaction requires negotiation. With protocols, the negotiation happens once (when the protocol is defined) and then never again. The savings compound over every subsequent interaction.

### 3. Encode Trust

Protocols embed assumptions about who can be trusted, under what conditions, with what verification. Diplomatic protocol encodes hierarchies. Religious protocol encodes sacred obligations. Network protocols encode authentication and encryption.

### 4. Create Legibility

Protocols make behavior predictable. This lets parties focus on substance rather than form. It also makes behavior auditable: did you follow the protocol or not?

### 5. Enable Scale

Human relationships don't scale. Protocols do. You can have a personal relationship with maybe 150 people (Dunbar's number). But you can participate in protocols with billions.

### 6. Preserve Culture

Protocols transmit practices across generations. A child learns the Seder protocol and can participate in a ritual 3,000 years old. The protocol is the vessel; the culture is what flows through.

---

## The Deep Pattern

A protocol is a **coordination mechanism that operates through agreed upon constraints**.

It is not a law (which is enforced by a state). It is not a contract (which binds specific parties). It is not a custom (which evolves organically and has fuzzy boundaries).

A protocol is:

- **Explicit**: Written down or at least articulable
- **Agreed upon**: Not imposed unilaterally
- **Constraining**: It limits behavior within defined bounds
- **Enabling**: Those constraints make coordination possible
- **Replicable**: Anyone can implement it
- **Composable**: Protocols can layer on protocols

The deepest insight: **protocols are infrastructure for human coordination that doesn't require trust in specific humans.** You don't need to trust the person on the other end of an HTTP request. You just need to trust that they're speaking HTTP.

---

## Questions for Protocol Fiction

If we're going to write fiction that explores protocols, we need to ask:

1. **What happens when protocols break?** When the agreed upon rules no longer hold?

2. **Who writes protocols?** What power dynamics are embedded in the writing?

3. **Who can't access the protocol?** What exclusions are baked in?

4. **When do protocols become prisons?** When do the constraints stop enabling and start suffocating?

5. **What happens when protocols compete?** (The Protocol Wars teach us this is not hypothetical.)

6. **Can protocols evolve?** Or are they frozen at the moment of specification?

7. **What's the relationship between protocol and protocol violation?** (Every system has edge cases. How are they handled?)

8. **What would a protocol for AI coordination look like?** For human-AI coordination? For AI-AI coordination?

---

## Sources

- Wikipedia: Protocol (diplomacy), Protocol Wars, Communication protocol, Internet protocol suite, OSI model
- History of Computer Communications (historyofcomputercommunications.info)
- Online Etymology Dictionary (etymonline.com)
- UNESCO: Social practices, rituals and festive events
- Institute of Etiquette: History of Etiquette
- City of Grande Prairie: Indigenous Cultural Protocols
- Various search results on religious liturgy and scientific protocols

---

_Research compiled February 8, 2026. Foundation for protocol fiction work._
