---
title: "Receipts as Deterministic Infrastructure: The Receipt Pipeline System, Decided"
tags: [finding, operations, finance, tooling, agents, workflow]
related:
- accounting-bookkeeping-research
- agent-provenance-graph
- workflow-as-contract
- decision-provenance
- proof-of-work
source: research/raw/receipt-pipeline-system-2026-11.md
ingested: 2026-11-25
---

# Receipts as Deterministic Infrastructure: The Receipt Pipeline System, Decided

## Key Points

**The design answer is one sentence: a receipt becomes a validated row in a private git ledger within the hour, and the tax year stops being an event.** Everything else in the source is an argument for that sentence and a set of constraints that follow from it. The stated success measure is equally plain: in February, nobody opens a mailbox looking for a receipt.

**Storage is append-only JSONL plus content-addressed blobs in a private repo (`agent-sivart/ledger`), and the Substrate holds architecture, never transaction rows.** One JSON object per line, one commit per receipt. The argument is diffability (a wrong row shows up in review), portability (a folder of text outlives every SaaS vendor), offline verification (`receiptpipe verify` walks every hash), and zero cost. The admitted cost is no query language and no UI, acceptable because the consumers are a CSV export and a monthly reconciliation, not an analyst. The boundary is the interesting part: mixing transaction rows into the knowledge graph would make every receipt commit a graph event and every graph edit a bookkeeping change.

**The v1.1 schema additions are the highest-leverage decisions in the document, precisely because they are boring.** `entity: business | personal` prevents business and personal spend from mixing in one ledger, which otherwise forces a manual split in every report. `direction` and `document_type` make refunds and outbound invoices representable at all; v1 rejects negative amounts, so a credit note cannot exist. A normalized `vendor_id` fixes a defect already present in the live nine records, where `Anthropic` and `Anthropic, PBC` appear as two vendors. Cost of doing this before Phase 1: six hours. Cost after Phase 2: a day plus a migration.

**Quarantine over guessing is the core safety property.** Missing provenance rejects, malformed money rejects, a bad attachment hash rejects, an unknown category rejects. Rejected records land in `failures.jsonl` and are never written to the ledger. This is the same instinct as `workflow-as-contract`: the failure mode is loud and inspectable rather than silently plausible.

**Attachments are written before the record, so a crash leaves an orphan blob rather than a record pointing at nothing.** Provenance is carried in the record itself: sha256, original filename, message id, IMAP UID, account. The PDF can be proved to be the bytes that arrived, and the email can be found again without trusting a mail client's local state. Duplicate attachments collapse by hash, duplicate messages collapse by message id; re-running a batch of nine returns nine duplicates and writes nothing, verified twice.

**The pipeline/skill/LLM split is the architectural crux.** `receiptpipe` is stdlib Python, no daemon, deterministic parser per sender family, exit 0 on success and 2 on quarantine so cron can alert. The skill is the operator interface that calls the CLI without reimplementing it. The LLM is fallback when required fields are missing or sources disagree, and an auditor in `--extractor llm` mode. The argument against agent-first is auditability: an agent writing a ledger row is unrepeatable, the same input can produce two answers, and the audit trail becomes a transcript instead of a hash. At nine receipts a month nobody notices; at tax time, "the parser is wrong and here is the fixture" is a fix, "the model said so" is an argument.

**The inventory correction is the design lesson of the whole card: a sender registry beats a keyword scan.** The keyword scan counted seven Anthropic failed-payment notices and concluded Anthropic had no usable receipts. The prototype found 34 real Anthropic receipts, eleven in 2026, every one with a machine-readable PDF, because the subject line says "Invoice" and the sender was not in the heuristic list. The corrected inventory is 987 receipt-like emails across two accounts and roughly 105 vendor domains, a floor rather than a census. Scope settles at the 43 senders that carry a dollar amount and parse without scraping; onboarding the long tail on demand costs about 1.5 hours each against roughly 93 hours to brute-force all 105.

**The format-family table is a cost model in disguise.** Stripe HTML plus PDF is authoritative and parser-reusable (Phase 1). Plain text and HTML itemized tables are Phase 2 regex and table parsers. Notification-only senders (Capital One, Chase, Venmo, PayPal) carry no amount and need Plaid or portal access in Phase 4. Shipment tracking is out of scope. Marginal cost per sender is fixture capture plus a mapping table.

**What actually ran, not a mock:** 12 of 12 unit tests pass from the preserved copy, 9 real Anthropic receipts stored (2024-12-19 through 2026-09-09, $708.89, all `ai_services`), `verify` returns `records=9 problems=0`, a second identical pass appends nothing, the webhook delivered 9 of 9 with valid HMAC signatures, and the private ledger remote is byte-identical to local at 19,219 bytes.

**Cost to finish is 257 engineer-hours over 11 calendar weeks, then 4 hours a month.** Wall clock is set by review bandwidth rather than typing speed; at 25 to 30 agent hours and about 3 operator hours a week, the CPA handoff lands 2027-02-09, eight weeks before the deadline. Deferring Phase 4 statements still lets the 2026 close land, because statements are reconciliation and receipts are the deduction. The document flags its own inconsistency here: the Phase 0 heading says 56 hours, the roll-up and the total use 62, and the phase body supports 62.

**The failure list is unusually honest and includes the one that would corrupt the books.** Gmail app passwords could disappear, forcing a rewrite of the source layer but not the ledger. Sender drift fails into quarantine, which is correct but requires someone to clear it. Fixtures contain PII (billing address, masked card digits, email address), so private repos only until a scrubbing path exists. The 987 count inherits the keyword scan's known miss. And cross-sender double counting is unsolved: a Stripe receipt and the matching card statement line both look like expenses, message-id dedupe cannot catch it, and Phase 0 needs an amount/date-window/last4 match or the books overstate deductions.

**QBO stays deferred at roughly 33 transactions a month against a 50 threshold.** CoinTracker is cost basis, not a receipt store; the ledger is evidence for transactions, and two systems must never compute the same gain. The near-term destination is a CSV plus reconciliation sheet a human can open, with an HMAC-signed `receipt.posted` webhook for whatever becomes the accounting endpoint.

## Open Questions

- Whether the 2026 return is self-filed with CPA review or fully CPA-prepared; the artifact serves both and Phase 5 resolves it in an hour with the CPA.
- Whether the cross-record matcher for double counting is simple enough to trust, or whether it needs its own quarantine lane.
- The third account (`email@earth2travis.com`) is still blocked on an app password; Phase 5 depends on that credential and nothing else.

## Relations

- Extends `accounting-bookkeeping-research.md`, which chose plain text accounting over SaaS; this document chooses an append-only JSONL ledger inside the same plain-text philosophy, with the tax form as the output rather than the source of truth.
- An instance of [[workflow-as-contract]]: sender registry, schema, validation rules, and exit codes are versioned policy, not vibes.
- Depends on the [[agent-provenance-graph]] instinct: every row carries its own chain of custody instead of trusting an upstream system's word.
- Sibling of [[decision-provenance]]: the same question, "who decided this and can you prove it," asked of money instead of models.
- Shares [[proof-of-work]]'s test: the artifact is a hash that either verifies offline or does not.
