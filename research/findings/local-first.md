---
title: Local-First Software Architecture
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/local-first.md
---

# Local-First Software Architecture

_Research compiled: 2026-02-03_

## Executive Summary

Local-first software is a paradigm that treats the user's local device as the primary source of truth, rather than a cloud server. This architecture enables:

- **Instant responsiveness** — No network round-trips for basic operations
- **Offline functionality** — Full editing capability without connectivity
- **Data ownership** — Users control their data, not service providers
- **Real-time collaboration** — Multiple users can edit simultaneously without conflicts

The movement emerged from research at Ink & Switch, a lab exploring "the future of tools for thought." Their 2019 essay "Local-First Software: You Own Your Data, in Spite of the Cloud" established the foundational principles.

Key enabling technology: **CRDTs (Conflict-free Replicated Data Types)** — data structures that can be modified independently on multiple devices and merged automatically without conflicts.

---

## 1. Philosophy & Principles

### The Problem with Cloud Apps

Cloud applications offer collaboration and cross-device access, but at a cost:

> "There is no cloud, it's just someone else's computer."
> — Popular bumper sticker quoted in the Local-First Manifesto

**Issues with cloud-centric architecture:**

- **Service dependency**: If the service is unavailable, you cannot access your work
- **Longevity risk**: Companies shut down, products get discontinued (see: [Killed by Google](https://killedbygoogle.com))
- **Performance**: Every action requires a network round-trip
- **Privacy**: Centralized databases are attractive targets for attackers
- **Ownership**: The cloud provider, not you, controls your data

_Source: [Ink & Switch Local-First Essay](https://www.inkandswitch.com/local-first/)_

### The Local-First Manifesto: Seven Ideals

Ink & Switch defines seven ideals for local-first software:

1. **No spinners: your work at your fingertips**
   - Operations handled by reading/writing local files
   - Data synchronization happens in the background
   - Near-instantaneous response to user input

2. **Your work is not trapped on one device**
   - Sync across all devices seamlessly
   - Cross-device sync with background replication

3. **The network is optional**
   - Full functionality offline
   - Sync when connectivity returns
   - Can use Bluetooth or local WiFi, not just Internet

4. **Seamless collaboration with your colleagues**
   - Real-time collaboration on par with Google Docs
   - Support for both synchronous and asynchronous workflows
   - No merge conflicts for users to resolve

5. **The Long Now**
   - Data remains accessible indefinitely
   - Not dependent on company survival
   - Files can be preserved in standard formats

6. **Security and privacy by default**
   - Local devices store only your data
   - End-to-end encryption possible
   - No centralized honeypot of user data

7. **You retain ultimate ownership and control**
   - All data stored on your device
   - Freedom to process, copy, modify, or delete
   - No arbitrary access restrictions

_Source: [Ink & Switch Local-First Essay](https://www.inkandswitch.com/local-first/)_

### Why Local-First Now?

The confluence of several trends makes local-first increasingly viable:

- **Mobile devices with significant storage and compute**
- **Mature CRDT algorithms** proven correct through formal verification
- **Developer tools** like Automerge and Yjs reaching production quality
- **User awareness** of privacy and data ownership issues
- **Remote work** increasing need for offline-capable tools

---

## 2. Technical Foundations

### CRDTs (Conflict-free Replicated Data Types)

CRDTs are the core technical innovation enabling local-first software.

**Definition from crdt.tech:**

> "A CRDT is a data structure that simplifies distributed data storage systems and multi-user applications. It is replicated across multiple computers in a network, with the following features:
>
> - The application can update any replica independently, concurrently and without coordinating with other replicas
> - An algorithm automatically resolves any inconsistencies
> - Although replicas may have different state at any time, they are guaranteed to eventually converge"

_Source: [crdt.tech](https://crdt.tech/)_

**Key properties:**

- **No coordination required**: Devices can modify data without checking with others
- **Automatic conflict resolution**: Built into the data structure itself
- **Eventual consistency**: All replicas converge to the same state
- **Decentralized**: No single server needed, peer-to-peer sync works

**Two approaches to conflict-free replication:**

| Approach                   | Description                                                                                                         |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Strongly consistent**    | Replicas coordinate before applying changes. Provides strong guarantees but requires consensus, can't work offline. |
| **Optimistic replication** | Modify any replica independently, resolve conflicts on sync. CRDTs handle the resolution automatically.             |

_Source: [crdt.tech](https://crdt.tech/)_

### Types of CRDTs

**Basic CRDTs:**

1. **Grow-only Set (G-Set)**
   - Elements can only be added, never removed
   - Trivially mergeable: union of all sets

2. **Last-Write-Wins Register (LWW)**
   - Stores a single value
   - Concurrent writes resolved by timestamp
   - Simple but can lose data

3. **Multi-Value Register (MVR)**
   - Preserves all concurrent values
   - Application or user decides which to keep

4. **Unique Set (Add-Wins Set)**
   - Supports both add and delete
   - Each element has unique tag
   - Add operation wins over concurrent delete

5. **List CRDT**
   - Ordered sequence with insert/delete
   - Uses "immutable positions" rather than indices
   - Foundation for collaborative text editing

_Source: [Matt Weidner - Designing Data Structures for Collaborative Apps](https://mattweidner.com/2022/02/10/collaborative-data-design.html)_

### Logical Clocks and Causality

CRDTs need to reason about "what happened before what" without relying on unreliable system clocks.

**Problems with system time:**

- Clock drift (0.001% error = 1 second/day)
- Users can change system time
- Leap seconds can make time go backwards
- Different CPU cores can have different times

**Solution: Logical clocks**

- Each node maintains an integer counter
- Increment on every event
- When nodes sync, set clock to `max(peer_clock, my_clock) + 1`
- If event A has lower clock than event B, A could not have caused B

_Source: [vlcn.io - Gentle Introduction to CRDTs](https://vlcn.io/blog/intro-to-crdts)_

### Sync Protocols

**Automerge's approach:**

> "Network-agnostic. Automerge is a pure data structure library that does not care about what kind of network you use. It works with any connection-oriented network protocol, which could be client/server (e.g. WebSocket), peer-to-peer (e.g. WebRTC), or entirely local (e.g. Bluetooth). You can even send an Automerge file as email attachment, or on a USB drive in the mail."

_Source: [Automerge Docs](https://automerge.org/docs/hello/)_

**Common sync architectures:**

- **Client-server**: Central server relays changes, simpler but less resilient
- **Peer-to-peer**: Direct device-to-device sync, fully decentralized
- **Hybrid**: Optional server for convenience, peer sync when available

---

## 3. Key Players

### Ink & Switch

An independent research lab exploring "the future of tools for thought."

**Research areas:**

- Local-first software architecture
- Malleable software (user customization)
- Programmable ink (dynamic sketching)
- Universal version control

**Key contributions:**

- The Local-First Manifesto (2019 essay)
- Automerge CRDT library
- Muse (local-first workspace app)
- Keyhive (local-first access control)
- Patchwork (version control for everything)

_Source: [inkandswitch.com](https://www.inkandswitch.com/)_

### Martin Kleppmann

Cambridge professor and computer scientist, co-creator of Automerge.

**Contributions:**

- Academic research on JSON CRDTs
- Formal verification of CRDT algorithms using Isabelle
- "Designing Data-Intensive Applications" (O'Reilly book)
- Talks on "Convergence vs Consensus"

_Source: [Automerge Team Page](https://automerge.org/)_

### Other Key Researchers

- **Alex Good**: Lead maintainer of Automerge
- **Kevin Jahns**: Creator of Yjs
- **Nuno Preguiça, Carlos Baquero, Marc Shapiro**: CRDT foundational researchers
- **Peter van Hardenberg**: Ink & Switch member, Muse developer

---

## 4. Tools & Libraries

### Automerge

**Description:** A library for building collaborative applications that automatically sync changes across devices, even offline, using CRDTs.

**Key features:**

- JSON-like data model
- Immutable state snapshots
- Works with any network protocol
- JavaScript, Rust, and WebAssembly implementations
- C API for iOS and other platforms

**Supporters:** Ink & Switch (engineering staff), Fly.io, Prisma, GoodNotes, NLNet, ARIA, Endless Foundation

**Philosophy:**

> "We are driven to build high performance, reliable software you can bet your project on. We develop rigorous academic proofs of our designs using theorem proving tools like Isabelle."

_Source: [automerge.org](https://automerge.org/)_

### Yjs

**Description:** The most popular CRDT library with 900k+ weekly npm downloads.

**Key features:**

- Automatic syncing with shared types
- Offline support with IndexedDB storage
- Network agnostic, decentralized
- Rich ecosystem of integrations

**Editor integrations:** ProseMirror, Quill, Monaco, CodeMirror, TipTap, and more

**Notable sponsors:** Athena Intel, Cargo.site, TipTap, Evernote, GitBook, Liveblocks

_Source: [yjs.dev](https://yjs.dev/)_

### Comparison: Automerge vs Yjs

| Feature            | Automerge           | Yjs                   |
| ------------------ | ------------------- | --------------------- |
| Data model         | JSON-like documents | Shared types          |
| History/versioning | Built-in            | Requires extension    |
| Binary format      | Compact, efficient  | Very compact          |
| Multi-language     | JS, Rust, WASM, C   | Primarily JS          |
| Philosophy         | Academic rigor      | Production pragmatism |
| Adoption           | Growing             | Largest user base     |

### Other Notable Tools

**ElectricSQL:**

- Sync engine for Postgres
- Local SQLite + cloud Postgres
- Shape-based dynamic partial replication

**Replicache:**

- Sync framework for web apps
- Optimistic updates with server reconciliation

**Evolu:**

- React hooks for local-first
- SQLite-based

**CR-SQLite (vlcn.io):**

- CRDTs directly in SQLite
- Merge tables like Git merges files

**Gun.js:**

- Decentralized database
- Real-time sync

_Sources: [ElectricSQL Blog](https://electric-sql.com/blog/2023/02/09/developing-local-first-software), [lofi.so/learn](https://lofi.so/learn)_

---

## 5. Real-World Applications

### Production Applications

**Muse** (Ink & Switch spin-off)

- Digital workspace for brainstorming
- Canvas for notes, sketches, PDFs
- Local-first architecture

**Figma** (partial local-first)

- Uses CRDTs for multiplayer
- Server-centric for storage
- Demonstrates real-time collaboration at scale

**Linear** (partial)

- Offline support
- Optimistic updates

**GoodNotes**

- Note-taking app using Automerge
- Cross-device sync

**Excalidraw**

- Collaborative whiteboard
- End-to-end encryption
- Uses Yjs

_Sources: [Automerge supporters](https://automerge.org/), various product pages_

### Research Prototypes

**Pixelpusher** (Ink & Switch)

- Collaborative pixel art editor
- Demonstrates multi-value register for color conflicts

**Pushpin** (Ink & Switch)

- Collaborative corkboard
- Document functional reactive programming

---

## 6. Relevance to Agent Infrastructure

### Opportunities for Local-First in Agent Systems

**1. Agent Memory and State**

- Agent memory could be CRDT-based
- Multiple agent instances could sync state
- Offline agents could continue working and merge later

**2. Collaborative AI Workflows**

- Human + AI editing same documents
- No conflict between user edits and AI suggestions
- History/versioning built in for audit trails

**3. Edge Deployment**

- Agents running on user devices (local-first)
- Sync to cloud when available
- Better privacy for sensitive agent interactions

**4. Multi-Agent Coordination**

- Agents as peers in a CRDT network
- No central coordinator required
- Fault-tolerant by design

**5. User Data Ownership**

- Users own their agent interaction history
- Portable between services
- Long-term preservation

### Technical Considerations

**Challenges:**

- CRDTs are designed for human-speed collaboration, not high-frequency agent updates
- Large state (LLM context) may not fit CRDT models well
- Agent actions may need stronger consistency than CRDTs provide

**Promising patterns:**

- Event sourcing with CRDT-based event logs
- Local-first memory with selective cloud sync
- Hybrid architecture: local-first for UI, server for compute

### Riffle's Vision

Riffle Systems proposes storing all app state, including UI state, in a reactive relational database:

> "Instead of imperatively fetching data from the database, the user writes reactive queries that update with fresh results whenever their dependencies change."

This could apply to agent systems:

- Agent state as reactive queries
- UI automatically updates as agent processes
- Clear data dependencies for debugging

_Source: [Riffle Systems Essay](https://riffle.systems/essays/prelude/)_

---

## 7. Gaps in This Research

### Content We Could Not Access

1. **YouTube Video** (<https://www.youtube.com/watch?v=10d8HxS4y_g>)
   - Unable to extract transcript
   - Related Issue: #80 (YouTube transcript extraction)
   - May contain valuable presentation content

2. **Local-First Conf 2025 Talks**
   - Playlist available but not processed
   - <https://youtube.com/playlist?list=PL4isNRKAwz2MabH6AMhUz1yS3j1DqGdtT>

3. **Some Linked Articles**
   - bricolage.io notes on local-first (fetch failed)
   - Some Automerge quickstart pages (404)

### Areas Needing Deeper Research

- **Performance benchmarks** comparing CRDT implementations
- **Security models** for end-to-end encrypted local-first apps
- **Migration patterns** from cloud-first to local-first
- **Mobile-specific considerations** (battery, storage limits)
- **Enterprise adoption** case studies

---

## Further Reading

### Essential

- [Local-First Software Essay](https://www.inkandswitch.com/local-first/) — Ink & Switch (2019)
- [crdt.tech](https://crdt.tech/) — CRDT overview and papers
- [Automerge Documentation](https://automerge.org/docs/hello/)
- [Yjs Documentation](https://docs.yjs.dev/)

### Technical Deep-Dives

- [Designing Data Structures for Collaborative Apps](https://mattweidner.com/2022/02/10/collaborative-data-design.html) — Matthew Weidner
- [A Gentle Introduction to CRDTs](https://vlcn.io/blog/intro-to-crdts) — vlcn.io
- [Developing Local-First Software](https://electric-sql.com/blog/2023/02/09/developing-local-first-software) — ElectricSQL

### Academic Papers

- "Conflict-free Replicated Data Types" — Preguiça, Baquero, Shapiro (2018)
- "A Comprehensive Study of CRDTs" — Shapiro et al. (2011)
- JSON CRDT paper — Kleppmann (2017)

### Community

- [Local-First Conf](https://www.localfirstconf.com/) — Annual conference (Berlin, July 2026)
- [lofi.so/learn](https://lofi.so/learn) — Curated learning resources
- Automerge Discord/Community
- Local-First Newsletter (via Buttondown)

---

## Summary

Local-first software represents a fundamental shift in how we think about application architecture. By treating the user's device as the primary data source and using CRDTs for conflict-free synchronization, we can build applications that are:

- **Faster** (no network latency for operations)
- **More reliable** (work offline, survive service outages)
- **More private** (data stays on device, E2E encryption)
- **More durable** (user owns data, not dependent on service survival)

For agent infrastructure, local-first principles offer intriguing possibilities for memory management, multi-agent coordination, and user data ownership. The technology is mature enough for production use, with tools like Yjs and Automerge powering real applications.

The main trade-off is complexity: local-first requires different mental models and careful consideration of sync semantics. But for applications where the seven ideals matter, it's an increasingly viable and attractive approach.
