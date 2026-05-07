---
title: Local-First Software Architecture
tags:
- local-first
- crdt
- architecture
- privacy
- data-ownership
- collaboration
related:
- github-as-knowledge-graph
- rag-vs-wiki
- agent-native-operations
- context-persistence
source: Ink and Switch, Automerge, Yjs. Compiled 2026-02-03
---




# Local-First Software Architecture

Local-first software treats the user's local device as the primary source of truth, rather than a cloud server. This enables instant responsiveness (no network round-trips for basic operations), offline functionality (full editing capability without connectivity), data ownership (users control their data, not service providers), and real-time collaboration (multiple users edit simultaneously without conflicts).

The movement emerged from research at Ink and Switch, a lab exploring "the future of tools for thought." Their 2019 essay "Local-First Software: You Own Your Data, in Spite of the Cloud" established the foundational principles.

Key enabling technology: CRDTs (Conflict-free Replicated Data Types), data structures that can be modified independently on multiple devices and merged automatically without conflicts.

## The Problem with Cloud Apps

Cloud applications offer collaboration and cross-device access, but at a cost:

- Service dependency: if the service is unavailable, you cannot access your work.
- Longevity risk: companies shut down, products get discontinued.
- Performance: every action requires a network round-trip.
- Privacy: centralized databases are attractive targets for attackers.
- Ownership: the cloud provider, not you, controls your data.

## The Local-First Manifesto: Seven Ideals

1. No spinners: your work at your fingertips. Operations handled by reading and writing local files. Data synchronization happens in the background.
2. Your work is not trapped on one device. Sync across all devices seamlessly.
3. The network is optional. Full functionality offline. Sync when connectivity returns.
4. Seamless collaboration with your colleagues. Real-time collaboration on par with Google Docs. No merge conflicts for users to resolve.
5. The Long Now. Data remains accessible indefinitely. Not dependent on company survival.
6. Security and privacy by default. Local devices store only your data. End-to-end encryption possible.
7. You retain ultimate ownership and control. All data stored on your device. Freedom to process, copy, modify, or delete.

## Technical Foundations

### CRDTs (Conflict-free Replicated Data Types)

A CRDT is a data structure replicated across multiple computers with three features: the application can update any replica independently, concurrently, and without coordinating with other replicas; an algorithm automatically resolves any inconsistencies; although replicas may have different state at any time, they are guaranteed to eventually converge.

Key properties: no coordination required, automatic conflict resolution, eventual consistency, decentralized (peer-to-peer sync works).

Two approaches: strong consistency (replicas coordinate before applying changes, cannot work offline) versus optimistic replication (modify any replica independently, resolve conflicts on sync). CRDTs handle optimistic replication automatically.

Basic CRDTs: Grow-only Set (elements added never removed), Last-Write-Wins Register (stores single value, resolved by timestamp), Multi-Value Register (preserves all concurrent values), Unique Set or Add-Wins Set (supports add and delete, add wins over concurrent delete), List CRDT (ordered sequence with insert and delete, foundation for collaborative text editing).

### Logical Clocks and Causality

CRDTs need to reason about "what happened before what" without relying on system clocks. Problems with system time: clock drift (0.001 percent error equals 1 second per day), users can change system time, leap seconds can make time go backwards, different CPU cores can have different times.

Solution: logical clocks. Each node maintains an integer counter. Increment on every event. When nodes sync, set clock to max(peer_clock, my_clock) plus 1. If event A has lower clock than event B, A could not have caused B.

### Sync Protocols

Automerge's approach: network-agnostic. Works with any connection-oriented network protocol (client-server like WebSocket, peer-to-peer like WebRTC, or entirely local like Bluetooth). You can even send an Automerge file as email attachment or on a USB drive in the mail.

Common sync architectures: client-server (central server relays changes, simpler but less resilient), peer-to-peer (direct device-to-device sync, fully decentralized), hybrid (optional server for convenience, peer sync when available).

## Key Players

Ink and Switch: independent research lab. Contributions include the Local-First Manifesto (2019), Automerge CRDT library, Muse (local-first workspace app), Keyhive (local-first access control), Patchwork (version control for everything).

Martin Kleppmann: Cambridge professor, co-creator of Automerge. Academic research on JSON CRDTs, formal verification using Isabelle, "Designing Data-Intensive Applications" (O'Reilly).

Other key researchers: Alex Good (lead maintainer of Automerge), Kevin Jahns (creator of Yjs), Nuno Preguica, Carlos Baquero, Marc Shapiro (CRDT foundational researchers), Peter van Hardenberg (Ink and Switch, Muse developer).

## Tools and Libraries

Automerge: library for building collaborative applications using CRDTs. JSON-like data model, immutable state snapshots, works with any network protocol, JavaScript, Rust, and WebAssembly implementations, C API for iOS. Backed by Ink and Switch, Fly.io, Prisma, GoodNotes, NLNet, ARIA, Endless Foundation.

Yjs: the most popular CRDT library with 900,000-plus weekly npm downloads. Automatic syncing with shared types, offline support with IndexedDB storage, network agnostic, decentralized. Editor integrations: ProseMirror, Quill, Monaco, CodeMirror, TipTap. Sponsors: Athena Intel, Cargo.site, TipTap, Evernote, GitBook, Liveblocks.

Comparison: Automerge has JSON-like documents, built-in history and versioning, compact binary format, multi-language support (JS, Rust, WASM, C), academic rigor philosophy. Yjs has shared types, requires extension for history, very compact binary format, primarily JS, production pragmatism philosophy, largest user base.

Other notable tools: ElectricSQL (sync engine for Postgres, local SQLite plus cloud Postgres), Replicache (sync framework for web apps, optimistic updates with server reconciliation), Evolu (React hooks for local-first, SQLite-based), CR-SQLite or vlcn.io (CRDTs directly in SQLite, merge tables like Git merges files), Gun.js (decentralized database, real-time sync).

## Real-World Applications

Muse (Ink and Switch spin-off): digital workspace for brainstorming, canvas for notes, sketches, PDFs.

Figma (partial local-first): uses CRDTs for multiplayer, server-centric for storage. Demonstrates real-time collaboration at scale.

Linear (partial): offline support, optimistic updates.

GoodNotes: note-taking app using Automerge, cross-device sync.

Excalidraw: collaborative whiteboard, end-to-end encryption, uses Yjs.

## Relevance to Agent Infrastructure

Opportunities: agent memory could be CRDT-based, multiple agent instances could sync state, offline agents could continue working and merge later. Human plus AI editing same documents with no conflict between user edits and AI suggestions. Agents running on user devices, syncing to cloud when available. Agents as peers in a CRDT network with no central coordinator required. Users own their agent interaction history, portable between services.

Challenges: CRDTs are designed for human-speed collaboration, not high-frequency agent updates. Large state (LLM context) may not fit CRDT models well. Agent actions may need stronger consistency than CRDTs provide.

Promising patterns: event sourcing with CRDT-based event logs, local-first memory with selective cloud sync, hybrid architecture (local-first for UI, server for compute).

Riffle Systems proposes storing all app state, including UI state, in a reactive relational database. Instead of imperatively fetching data, the user writes reactive queries that update with fresh results whenever dependencies change. This could apply to agent systems: agent state as reactive queries, UI automatically updates as agent processes, clear data dependencies for debugging.
