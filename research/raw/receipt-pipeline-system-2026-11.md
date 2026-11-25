# Receipts: The System, Decided

Status: answer document for the root card, ready for Operator review
Date: 2026-11-25
Card: t_1b443ef8 (closes t_cd15565a, t_5f445382, t_07ec92a8, t_0c33c0a1)
Evidence: inventory (`receipt-inventory-2026-05.md`), decision (`t_5f445382`),
prototype (`t_07ec92a8`, code preserved at `/home/sivart/code/receiptpipe`,
commit `d8f5d30`), rollout plan (`receipt-pipeline-rollout-plan-2026-11.md`).

---

## The answer in one page

A receipt arrives, becomes a validated row in a private git ledger within the
hour, and the tax year stops being an event. That is the whole design.

Five decisions, each argued below:

| Question | Decision |
|---|---|
| Where does receipt data live? | Append-only JSONL plus content-addressed PDFs in the private repo `agent-sivart/ledger`. Git history is the audit trail. The Substrate holds architecture, never transaction rows. |
| What gets extracted? | The `receipt-v1` record, upgraded to v1.1 with `entity`, `direction`, `document_type`, and normalized vendor. Money as decimal strings, provenance mandatory. |
| Attachments: separate or with the email? | Both, in a strict order. The blob is content-addressed and stored with the ledger; the record points back to the email as chain of custody. |
| Accounting destination? | Annual CSV plus reconciliation sheet for the CPA, signed webhook for anything downstream. QBO stays deferred until volume clears 50 transactions a month (now about 33). CoinTracker is cost basis, not a receipt store. |
| Skill or standalone pipeline? | A standalone deterministic pipeline with a thin agent skill wrapped around it. The LLM is a fallback and an auditor, never the write path for money. |

One sentence on why: **the core has to run correctly at 3 a.m. with nobody
watching, and be auditable a year later by a human who does not trust it.** That
rules out an agent in the hot path and rules in deterministic parsing, git, and
hashes.

---

## 1. Where the data lives

The ledger is a private GitHub repository, `agent-sivart/ledger`. One JSON
object per receipt, one line, append only. Attachments live beside it,
content-addressed by sha256. Every receipt is a commit:
`feat(receipts): <record_id> <vendor> <amount>`.

Why this and not a database:

- Diffable. A wrong row is visible in a review, not buried in a table.
- Portable. No vendor, no migration, no subscription. A folder of text outlives
  every SaaS startup that ever promised to file your taxes.
- Verifiable. `receiptpipe verify` walks every hash and every required field in
  one command, offline.
- Free, and already live. The remote is 19,219 bytes, byte-identical to local.

What it costs: no query language and no UI. That is acceptable because the
consumers are a CSV export and a monthly reconciliation report, not an analyst.
If volume ever justifies a real accounting system, the JSONL is the migration
source, not the destination.

The Substrate boundary is explicit. Architecture documents like this one live in
the Substrate. Transaction rows do not, ever. Mixing them would make every
receipt commit a knowledge graph event and every knowledge graph change a
bookkeeping change. Neither system wants that.

### Schema: receipt-v1, and the v1.1 upgrade

v1 fields, all validated before write:

| Field | Contents |
|---|---|
| `record_id` | `rcpt_` plus 16 hex of the idempotency key |
| `idempotency_key` | sha256(message-id + sorted attachment hashes) |
| `vendor` | name, domain, sender address |
| `receipt_number`, `invoice_number` | vendor identifiers |
| `paid_on` | settlement date, ISO 8601 |
| `billing_period` | start and end when stated |
| `currency` | from the source, else USD with `currency_source: default` |
| `amount` | subtotal, tax, tax_rate, total, amount_paid as decimal strings |
| `payment_method` | brand and last4; Stripe Link has no last4 |
| `line_items` | description, quantity, unit price, tax rate, amount |
| `category` | accounting bucket from a conservative keyword taxonomy |
| `source` | account, folder, UID, Message-ID, subject, received_at |
| `attachments` | filename, sha256, content type, role, bytes, stored path |
| `extraction` | method, version, confidence, cross-check verdicts, notes |
| `status` | `posted` |

v1.1 must add, before Phase 1 rather than after 900 rows:

1. `entity: business | personal`. Without it, business and personal spend mix
   in one ledger and every report needs a manual split. This is the highest
   leverage change in the whole plan. Retrofitting costs a day plus errors.
2. `direction: expense | revenue` and `document_type: receipt | invoice |
   credit_note | statement`. QuickBooks invoices are revenue. Refunds are
   credit notes. Today the schema rejects negative amounts, so a refund cannot
   even be represented.
3. A normalized `vendor_id`. The live ledger already contains both `Anthropic`
   and `Anthropic, PBC` for one vendor. Reporting splits it in two. That is not
   hypothetical, it is in the nine records.

Validation rules that stay: missing provenance rejects, malformed money rejects,
bad attachment hash rejects, unknown category rejects. A rejected record is
quarantined to `failures.jsonl`, never written. **Quarantine over guessing** is
the core safety property.

---

## 2. Attachments

Save them, separately, and never lose the thread back to the mailbox.

An attachment is written to a content-addressed path (`attachments/<sha256>/`)
before the JSONL line is appended. A crash between the two leaves an orphan blob,
never a record pointing at nothing. The record carries the sha256, the original
filename, the message id, the IMAP UID, and the account. So the PDF can be
proved to be the bytes that arrived, and the email can be found again without
trusting a mail client's local state.

Duplicate attachments collapse by hash. Duplicate messages collapse by
`message_id` index. Re-running a batch of nine returns nine duplicates and
writes nothing, which was verified twice.

Retention: hot in the repo for two years, then cold private archive, with the
JSONL row remaining forever. The ledger should stay small enough to clone in a
second. Seven years of PDFs in git is a slow-motion repo bloat problem.

---

## 3. Where it lands

Three consumers, in order of what exists today:

1. **Annual CSV plus reconciliation sheet, handed to the CPA.** This is the
   real destination for the 2026 close. It needs no integration, no API, and no
   trust from an accounting system. It is a file a human can open.
2. **HMAC-signed webhook** (`receipt.posted`) for whatever becomes the
   accounting endpoint. Best effort with retries and a `redeliver` replay. The
   receiving side dedupes on `record_id`.
3. **QBO, deferred.** Roughly 33 transactions a month against a 50 threshold.
   Below the threshold, sync is maintenance without payoff.

CoinTracker deserves its own sentence because it is a different animal. It
computes crypto cost basis from exchange and wallet data. The receipt ledger is
*evidence* for those transactions, not a parallel basis. Feed it CSV or PDFs
when a lot needs support; never let two systems compute the same gain.

Unresolved and honest: whether the return is self-filed with CPA review or
fully CPA-prepared. The artifact serves both. Phase 5 confirms the exact format
with the CPA before December, so the answer is a one hour conversation, not a
design decision.

---

## 4. Skill or pipeline

Both, with a hard boundary between them.

**The pipeline** (`receiptpipe`) is Python, stdlib only, no daemon. IMAP
read-only, MIME walk, deterministic parser per family, cross-check, validate,
store, notify, export. It exits 0 on success and 2 on quarantine so cron can
alert. It is boring on purpose.

**The skill** is the Operator interface: `scan` a sender, `run` a window,
`verify` the ledger, show the quarantine digest, add a sender from the registry,
export for the CPA. It calls the CLI. It does not reimplement it.

**The LLM** is the fallback when required fields are missing or the PDF, body,
and invoice disagree, and an auditor in `--extractor llm` mode where the
deterministic parse checks the model. In the prototype run, Claude returned the
same fields as the parser. That is the correct role: expensive, occasional,
checked.

Why not agent-first: an agent that reads a receipt and writes a ledger row is
unrepeatable. The same input can produce two answers, and the audit trail is a
transcript instead of a hash. At nine receipts a month nobody notices. At tax
time, the difference between "the parser is wrong and here is the fixture that
proves it" and "the model said so" is the difference between a fix and an
argument with the IRS.

---

## 5. The inventory, corrected

The inventory scanned 12 months across two accounts and found 987 receipt-like
emails, roughly 105 vendor domains. Those numbers are a floor, not a census.

| Account | Emails scanned | Receipt-like | Vendors |
|---|---|---|---|
| earth2travis@gmail.com | 1,348 | 72 | ~25 |
| travis.mccutcheon@gmail.com | 3,912 | 915 | ~80 |
| email@earth2travis.com | inaccessible | unknown | unknown |

**The correction that matters:** the keyword scan counted seven Anthropic
*failed payment notices* in earth2travis and concluded Anthropic had no usable
receipts. The prototype then found 34 real Anthropic receipts from
`invoice+statements@mail.anthropic.com`, eleven of them in 2026, every one with
machine-readable PDFs. The scan missed them because the subject line says
"Invoice" or the sender was not in its heuristic list.

Lesson, and it is the design lesson of this whole card: **a sender registry
beats a keyword scan.** Keyword filters find noise and miss signal. An explicit
list of senders, each with a subject pattern and a parser family, is auditable,
extensible, and tells you what it does not cover.

Format families, and what each is worth:

| Family | Examples | Data in email | Treatment |
|---|---|---|---|
| Stripe HTML + PDF | Anthropic, CoinTracker, Loom, Neynar, Midjourney | Yes, authoritative PDF | Phase 1, reuse parser |
| Plain text structured | Google Payments, PrintWithMe, YouTube | Yes | Phase 2, regex |
| HTML itemized table | H-E-B, Toast, Airbnb, Amazon order, Square, eBay | Yes | Phase 2, table parser |
| Notification or portal link | Capital One, Discover, Chase, HCTRA, Texas Gas, Venmo, PayPal | No | Phase 4, Plaid or portal |
| Shipment tracking | Amazon shipped/delivered, Nike, Shopify | Order numbers only | Out of scope |
| Bilingual HTML | City of Austin Utilities | Partial | Phase 4 |

Scope is the 43 senders that carry a dollar amount and parse without scraping.
The remaining ~62 domains average four emails a year and are mostly shipment
noise. Onboarding them on demand costs 1.5 hours each. Brute-forcing all 105
costs about 93 hours and buys almost nothing.

The third account was re-checked today. 1Password Operations holds exactly two
Gmail IMAP items, earth2travis and travis.mccutcheon. `email@earth2travis.com`
still needs its own app password. Phase 5 stays blocked on that credential, and
nothing else.

---

## 6. What actually ran

Not a sketch, not a mock. The numbers below were re-verified while writing this
document:

- 12/12 unit tests pass from the preserved copy at `/home/sivart/code/receiptpipe`.
- 9 real Anthropic receipts stored: 2024-12-19 through 2026-09-09, $708.89
  total, all categorized `ai_services`.
- `verify` returns `records=9 problems=0` with attachment hashes intact.
- A second identical pass returns 9 duplicates and appends nothing.
- Webhook delivered 9/9 with valid HMAC signatures.
- Live IMAP scan found 11/11 Anthropic receipts for 2026, all extracting clean
  in dry-run.
- Ledger remote `agent-sivart/ledger` is private, on `main`, 19,219 bytes,
  byte-identical to local.

The code previously existed only in a disposable scratch workspace. It is now a
local git repository at `/home/sivart/code/receiptpipe` (29 files, one commit).
Publishing it to a private GitHub repo is a Phase 0 item, because pushing to
GitHub is an external action and belongs behind the Operator's GO.

---

## 7. Cost to finish

257 engineer-hours over 11 calendar weeks, then 4 hours a month to operate.

| Phase | Hours | What it buys |
|---|---|---|
| 0 Foundation | 62 | sender registry, IMAP cursor, schema v1.1, ledger lock and push, ops surface |
| 1 Stripe tier | 20 | every Stripe PDF sender, reusing the parser |
| 2 Body-parsed | 58 | plain text and HTML table families |
| 3 Long tail | 45 | the remaining machine-parseable senders |
| 4 Statements | 44 | Plaid or portal, decision gated |
| 5 Close and handoff | 28 | third account, 2026 close, CPA format |
| Operate | 48/year | digest, quarantine, reconciliation, restore drills |

Note a document inconsistency: the Phase 0 heading says 56 hours, the roll-up
says 62, and the 257 total uses 62. The phase body supports 62. The heading is
stale and should be corrected before the plan is quoted to anyone.

Wall clock is set by review bandwidth, not keyboard speed. At 25 to 30 agent
hours a week and about 3 Operator hours a week, the CPA handoff lands 2027-02-09,
eight weeks before the filing deadline. If Phase 4 is deferred, the 2026 close
still lands, because statements are reconciliation and receipts are the deduction.

Marginal cost per sender is fixture capture plus a mapping table, not a project.
That estimate assumes no sender changes format mid-rollout. Historically that
fails once or twice a year. Golden fixtures and quarantine alerts exist for
exactly that.

---

## 8. Six decisions that are yours

1. **Statements: Plaid, scraping, or defer?** Recommendation: Plaid for four
   business institutions, defer the rest. Cheapest path to reconciliation.
2. **Entity split now?** Recommendation: yes, before Phase 1. Six hours now,
   a day plus errors later.
3. **Direction and document type?** Recommendation: yes. Refunds and outbound
   invoices are otherwise unrepresentable.
4. **Blob retention?** Recommendation: two years hot, then cold private archive.
5. **CPA delivery?** Recommendation: immutable shared folder, one annual artifact.
6. **QBO threshold?** Recommendation: stays at 50 transactions a month.

If 2 and 3 land before Phase 0 ends they cost six hours. If they land after
Phase 2 they cost a day and a migration.

---

## 9. What could make this wrong

- **Gmail app passwords.** The whole ingest assumes IMAP with app passwords
  stays available on these accounts. If Google forces OAuth only, the source
  layer needs a rewrite; the ledger does not.
- **Cross-sender double counting.** A Stripe receipt and the matching card
  statement line will both look like expenses. The message-id key cannot catch
  that. Phase 0 needs a cross-record match on amount, date window, and last4,
  or the books overstate deductions.
- **Sender drift.** Vendors redesign receipts. Deterministic parsers fail loudly
  into quarantine, which is the right failure, but somebody has to clear it.
- **PII in fixtures.** The nine `.eml` files contain a billing address, masked
  card digits, and an email address. Private repos only until a scrubbing path
  exists.
- **The 987 number.** It is a floor from a keyword scan that demonstrably
  missed a major sender. Any effort estimate inherits that uncertainty.

---

## 10. Next

On GO: Phase 0, starting with the sender registry and schema v1.1. Publish the
code to a private repo. Wire the nightly timer. Then Phase 1, which is mostly
data entry and fixtures because the hard parser already exists.

The measure of success is unglamorous: in February, nobody opens a mailbox
looking for a receipt.
