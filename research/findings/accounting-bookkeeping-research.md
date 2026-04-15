---
title: "Accounting & Bookkeeping Research for Sivart"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/accounting-bookkeeping-research.md
---

# Accounting & Bookkeeping Research for Sivart

**Date:** 2026-02-25
**Context:** Human+AI partnership (sivart.wtf), ~$50-100/mo expenses, US-based (Texas), growing operation

---

## 1. Tool Comparison for Our Scale

### Wave Financial (Free tier / Pro $16/mo)

- **Cost:** Starter plan is free (unlimited invoices, estimates, bills, bookkeeping records). Pro plan ~$16/mo adds bank auto-import, receipt capture, auto-categorization.
- **Automation:** Pro plan auto-imports bank transactions and auto-categorizes. Free tier is manual entry only.
- **Receipt capture:** Pro plan only. Mobile app for scanning.
- **Tax categorization:** Basic. Maps to common categories but not specifically Schedule C lines.
- **API access:** None. No public API. Zero automation potential for an AI agent.
- **Verdict:** Good free option for humans who want a GUI. Useless for AI-native workflows. The lack of API is a dealbreaker for us.

### QuickBooks Solopreneur (formerly Self-Employed, ~$20/mo)

- **Cost:** ~$20/mo (frequently discounted to $10/mo for first months). QuickBooks Self-Employed was discontinued; replaced by Solopreneur.
- **Automation:** Bank feed auto-import, auto-categorization, mileage tracking, TurboTax integration.
- **Receipt capture:** Yes, mobile app with OCR.
- **Tax categorization:** Excellent. Maps directly to Schedule C categories. Estimates quarterly taxes automatically.
- **API access:** QuickBooks has an API but it's designed for third-party integrations, not personal automation. OAuth setup is heavy. Not practical for a micro operation.
- **Verdict:** Best traditional option for tax prep. Overkill and expensive for $100/mo in expenses. The TurboTax integration is its killer feature.

### Hurdlr (Free / Premium ~$10/mo)

- **Cost:** Free tier with basic tracking. Premium ~$10/mo for full features.
- **Automation:** Auto-tracks mileage, expenses, income. Bank connections.
- **Receipt capture:** Yes, mobile OCR.
- **Tax categorization:** Good. Real-time tax estimate updates. Designed for gig workers/freelancers.
- **API access:** None.
- **Verdict:** Mobile-first, good for gig workers who drive. Not aligned with our use case (we're a server-based operation, not driving for Uber). Skip.

### Google Sheets with Templates

- **Cost:** Free (already have Google Workspace).
- **Automation:** Can build Apps Script automations. Full API access. An AI agent can read/write via Google Sheets API.
- **Receipt capture:** Manual (link to Google Drive files).
- **Tax categorization:** Whatever you build. No built-in intelligence.
- **API access:** Full. Google Sheets API is robust and well-documented.
- **Verdict:** Flexible, free, API-accessible. But reinventing the wheel. No double-entry validation, easy to make mistakes. Fine as a supplementary reporting layer but not as a primary ledger.

### Plain Text Accounting (hledger / beancount)

- **Cost:** Free and open source.
- **Automation:** Total. Files are plain text. An AI agent reads and writes them natively. Git-versioned. Scriptable.
- **Receipt capture:** Manual (link to files or scan directories). Can build wrappers.
- **Tax categorization:** You define your own chart of accounts, mapped to Schedule C.
- **API access:** Not applicable; the file IS the API. Both tools have CLI interfaces for querying.
- **Verdict:** **Best fit for an AI-native operation.** Version-controlled, auditable, scriptable, zero cost. The agent can maintain the books directly.

### Summary Matrix

| Tool | Cost | AI-Writable | Git-Friendly | Tax Mapping | Our Fit |
|------|------|-------------|--------------|-------------|---------|
| Wave Free | $0 | No | No | Basic | Poor |
| Wave Pro | $16/mo | No | No | Basic | Poor |
| QB Solopreneur | $20/mo | Limited | No | Excellent | Okay |
| Hurdlr | $0-10/mo | No | No | Good | Poor |
| Google Sheets | $0 | Yes | No | Manual | Fair |
| hledger | $0 | Yes | Yes | Manual | Excellent |
| beancount | $0 | Yes | Yes | Manual | Excellent |

---

## 2. Plain Text Accounting: hledger vs beancount

### Overview

Both are mature tools that store financial data as plain text files. Both support double-entry bookkeeping and produce standard financial reports (balance sheet, income statement, etc.).

### hledger

- **Language:** Haskell
- **Install:** `apt install hledger` or `brew install hledger`
- **File format:** `.journal` (compatible with Ledger format)
- **Web UI:** Built-in (`hledger-web`), basic but functional
- **Strengths:** Flexible date formats, partial data entry (can omit one amount), forgiving parser, excellent CLI, great documentation
- **Community:** Active, good docs at hledger.org

**Example hledger journal:**
```
; sivart.journal - Sivart Operations Ledger

2026-02-01 Hetzner Cloud - CPX11 Server
    expenses:cloud:compute          $4.35
    liabilities:mercury-debit

2026-02-01 Google Workspace - Business Standard
    expenses:saas:productivity      $10.92
    liabilities:mercury-debit

2026-02-01 1Password Teams
    expenses:saas:security          $10.65
    liabilities:mercury-debit

2026-02-15 Anthropic API
    expenses:ai:api                 $25.00
    liabilities:mercury-debit

2026-02-15 OpenAI API
    expenses:ai:api                 $5.00
    liabilities:mercury-debit

2026-02-20 ElevenLabs TTS
    expenses:ai:tts                 $5.00
    liabilities:mercury-debit
```

**Querying:**
```bash
hledger -f sivart.journal balance expenses    # expense breakdown
hledger -f sivart.journal register expenses   # transaction list
hledger -f sivart.journal balance -M          # monthly summary
hledger -f sivart.journal incomestatement     # P&L
```

### beancount

- **Language:** Python (v3 rewritten in C++ core with Python API)
- **Install:** `pip install beancount` (v2) or `pip install beancount-v3` (v3, newer)
- **File format:** `.beancount`
- **Web UI:** Fava (`pip install fava`) — beautiful, full-featured web dashboard
- **Strengths:** Strict validation (catches errors), plugin system (Python), structured metadata, explicit account opening/closing
- **Community:** Active, beancount.io forum

**Example beancount file:**
```beancount
option "title" "Sivart Operations"
option "operating_currency" "USD"

; Account declarations (required in beancount)
2026-01-01 open Assets:Mercury:Checking
2026-01-01 open Liabilities:Mercury:Debit
2026-01-01 open Expenses:Cloud:Compute
2026-01-01 open Expenses:SaaS:Productivity
2026-01-01 open Expenses:SaaS:Security
2026-01-01 open Expenses:AI:API
2026-01-01 open Expenses:AI:TTS
2026-01-01 open Expenses:Domain
2026-01-01 open Expenses:Hosting
2026-01-01 open Income:Revenue

2026-02-01 * "Hetzner" "CPX11 Cloud Server - Ashburn"
  Expenses:Cloud:Compute          4.35 USD
  Liabilities:Mercury:Debit

2026-02-01 * "Google" "Workspace Business Standard"
  Expenses:SaaS:Productivity     10.92 USD
  Liabilities:Mercury:Debit

2026-02-01 * "1Password" "Teams Plan"
  Expenses:SaaS:Security         10.65 USD
  Liabilities:Mercury:Debit

2026-02-15 * "Anthropic" "Claude API Usage"
  Expenses:AI:API                25.00 USD
  Liabilities:Mercury:Debit

2026-02-15 * "OpenAI" "API Usage"
  Expenses:AI:API                 5.00 USD
  Liabilities:Mercury:Debit

2026-02-20 * "ElevenLabs" "TTS API"
  Expenses:AI:TTS                 5.00 USD
  Liabilities:Mercury:Debit
```

### Head-to-Head Comparison

| Feature | hledger | beancount |
|---------|---------|-----------|
| Validation strictness | Lenient (flexible) | Strict (catches errors) |
| Account declaration | Optional | Required (good for discipline) |
| Web UI | hledger-web (basic) | Fava (excellent) |
| Plugin system | Limited | Python plugins (powerful) |
| AI writability | Easy (simpler format) | Easy (structured, explicit) |
| Learning curve | Lower | Slightly higher |
| Error messages | Good | Excellent (line numbers, specific) |
| Import tools | hledger-import, csv rules | bean-import framework |
| Currency handling | Good | Excellent (cost basis tracking) |

### Recommendation: beancount

**Why beancount wins for us:**
1. **Strict validation** catches errors before they propagate. An AI agent generating entries benefits from a tool that rejects bad data.
2. **Fava** is a genuinely excellent web UI for visual review.
3. **Python ecosystem** means we can write custom importers and plugins easily.
4. **Required account declarations** enforce a clean chart of accounts.
5. **Beancount v3** has strong performance improvements.

The strict validation is the key differentiator. When an AI agent is writing accounting entries, you want the tool to reject mistakes, not silently accept them.

---

## 3. Expense Categorization

### Chart of Accounts for Sivart (mapped to Schedule C)

```
Expenses:
├── AI/                          → Schedule C Line 27a (Other: AI Services)
│   ├── API                      Anthropic, OpenAI API usage
│   ├── TTS                      ElevenLabs
│   └── ML                       Runway ML, other ML tools
├── Cloud/                       → Schedule C Line 27a (Other: Cloud Computing)
│   ├── Compute                  Hetzner server
│   ├── Hosting                  Orbiter, other hosting
│   └── Storage                  Any cloud storage
├── SaaS/                        → Schedule C Line 27a (Other: Software/Subscriptions)
│   ├── Productivity             Google Workspace
│   ├── Security                 1Password
│   ├── DevTools                 GitHub, other dev tools
│   └── Other                    Misc subscriptions
├── Domain/                      → Schedule C Line 27a (Other: Internet/Web)
│   └── Registration             Hover domain renewals
├── Internet/                    → Schedule C Line 25 (Utilities) [if home office]
│   └── Service                  Business portion of internet
├── BankFees/                    → Schedule C Line 27a (Other: Bank Charges)
│   └── Monthly                  Mercury fees if any
├── Tax/                         → Not deductible on Schedule C
│   ├── Federal                  
│   └── StateLocal               
├── Legal/                       → Schedule C Line 17 (Legal & Professional)
│   └── Formation                LLC formation costs
└── Education/                   → Schedule C Line 27a (Other: Education)
    └── Training                 Courses, books related to business
```

### Schedule C Line Mapping

| Schedule C Line | Category | Our Expenses |
|----------------|----------|-------------|
| Line 8 - Advertising | Marketing | (none currently) |
| Line 17 - Legal & Professional | CPA, lawyer, formation | LLC formation if applicable |
| Line 18 - Office Expense | Office supplies, small software | Could put SaaS here |
| Line 22 - Supplies | General supplies | Minimal |
| Line 25 - Utilities | Internet, phone (biz portion) | Internet service |
| Line 27a - Other Expenses | **Most of our stuff** | AI APIs, cloud, SaaS, domains |

**Key insight:** Most tech/AI expenses land on Line 27a "Other Expenses" with itemized descriptions. The IRS doesn't have specific lines for cloud computing or AI APIs. You describe them on the supplemental page. This is completely normal and expected for modern tech businesses.

### Subscription-Based Software (SaaS) Deduction Rule

SaaS subscriptions (monthly recurring) are expensed in the year incurred. They are NOT capitalized. This is straightforward: $10.92/mo for Google Workspace = $131.04 annual deduction.

---

## 4. Best Practices

### Monthly Close Process (for a micro operation)

This should take 15 minutes max:

1. **Reconcile:** Compare Mercury statement to ledger entries. Every transaction should be recorded.
2. **Categorize:** Ensure all expenses have correct account codes.
3. **Receipt check:** Verify receipts exist for any expense over $75 (IRS requirement). For recurring SaaS under $75, the bank/card statement suffices.
4. **Run reports:** Generate monthly P&L. Compare to prior month. Flag anomalies.
5. **Commit:** `git add . && git commit -m "close: february 2026"` — the books are now locked for the month.

### Receipt Retention

- **IRS requirement:** Keep records for 3 years from filing date (or 6 years if >25% underreporting suspected).
- **What counts as a receipt:** Bank/card statements suffice for recurring charges. For one-off purchases, keep the actual receipt/invoice.
- **Digital is fine:** IRS accepts digital records. A `receipts/` folder in the repo with PDFs/images works.
- **Under $75 rule:** For expenses under $75, a bank statement entry is sufficient. You don't need a separate receipt. Most of our expenses fall here.
- **Practical approach:** Set up email forwarding rules to auto-save invoices from Hetzner, Google, Anthropic, etc. to a receipts folder.

### Separating Business/Personal

- **Dedicated bank account:** Mercury is already dedicated. This is the single most important thing. ✅ Already done.
- **Dedicated card:** Mercury debit card for all business expenses. ✅ Already done.
- **No mixing:** Never pay personal expenses from Mercury. Never pay business expenses from personal accounts.
- **If you slip:** Record it as an owner draw/contribution to keep the books clean.

### Quarterly Tax Estimates

- **Who:** Anyone expecting to owe >$1,000 in tax for the year.
- **When:** April 15, June 15, September 15, January 15 (of following year).
- **How much:** Self-employment tax (15.3%) + federal income tax on net profit. For ~$1,200/yr in expenses with minimal revenue, this may not apply yet. Once revenue exceeds expenses consistently, start paying quarterly.
- **Form:** IRS Form 1040-ES.
- **Safe harbor:** Pay at least 100% of prior year's tax liability (or 110% if AGI >$150k) to avoid underpayment penalties.
- **Texas:** No state income tax = no state quarterly estimates needed. ✅

### When to Get a CPA

- When annual revenue exceeds $10,000-20,000
- When forming an LLC (one-time consultation, ~$200-500)
- When first filing Schedule C (one-time consultation to set up correctly)
- At tax time if you're unsure about anything
- **Right now?** Probably not needed yet. At $50-100/mo expenses and minimal revenue, you can handle this with TurboTax or FreeTaxUSA. Get a CPA consult when revenue picks up.

---

## 5. AI-Native Bookkeeping

This is where our setup gets interesting. An AI agent can handle most bookkeeping tasks natively with plain text accounting.

### What the AI Agent Can Do

**Daily/Ongoing:**
- Parse Mercury transaction notifications or bank feed CSVs
- Auto-categorize transactions based on vendor name (Hetzner → Expenses:Cloud:Compute, Anthropic → Expenses:AI:API)
- Write beancount entries directly to the journal file
- Run `bean-check` to validate entries
- Commit changes to git

**Monthly:**
- Run the monthly close process
- Generate reports via beancount CLI
- Compare month-over-month spending
- Flag unusual transactions or budget overruns
- Produce a summary for the human

**Quarterly:**
- Calculate estimated tax liability
- Remind human about quarterly payment deadlines
- Generate year-to-date P&L

**Tax Time:**
- Generate Schedule C category totals
- Produce a tax preparation summary
- Export data in formats a CPA can use

### Auto-Categorization Rules

A simple mapping table the agent maintains:

```python
VENDOR_CATEGORIES = {
    "hetzner": "Expenses:Cloud:Compute",
    "google workspace": "Expenses:SaaS:Productivity",
    "1password": "Expenses:SaaS:Security",
    "anthropic": "Expenses:AI:API",
    "openai": "Expenses:AI:API",
    "elevenlabs": "Expenses:AI:TTS",
    "runway": "Expenses:AI:ML",
    "orbiter": "Expenses:Cloud:Hosting",
    "hover": "Expenses:Domain:Registration",
}
```

### Receipt OCR Pipeline

1. Receipt arrives (email PDF or photo)
2. Agent extracts text (built-in vision capability or Google Document AI)
3. Agent parses vendor, amount, date
4. Agent writes beancount entry
5. Agent moves receipt to `receipts/YYYY/MM/vendor-date.pdf`
6. Agent links receipt in beancount metadata: `document: "receipts/2026/02/hetzner-20260201.pdf"`

### Mercury Integration

Mercury offers CSV exports and potentially webhook notifications. The agent can:
1. Download monthly CSV from Mercury (or human forwards it)
2. Parse transactions
3. Auto-categorize and write beancount entries
4. Flag any unrecognized transactions for human review

### Implementation Plan

```
bookkeeping/
├── main.beancount          # Main ledger (includes other files)
├── accounts.beancount      # Chart of accounts
├── 2026/
│   ├── 01.beancount        # January transactions
│   ├── 02.beancount        # February transactions
│   └── ...
├── receipts/
│   └── 2026/
│       └── 02/
├── reports/                # Generated reports
├── importers/              # Mercury CSV importer
└── rules.py                # Auto-categorization rules
```

---

## 6. Tax Implications

### Texas LLC vs Sole Proprietorship

**Sole Proprietorship (current state):**
- Cost: $0 to form, $0 ongoing
- Taxes: Report on Schedule C of personal 1040
- Liability: No protection (personal assets at risk)
- Texas: No franchise tax filing required
- Complexity: Minimal

**Texas Single-Member LLC:**
- Cost: $300 filing fee with Texas Secretary of State
- Annual: Must file Texas franchise tax report annually (but exempt if revenue under $2.47M threshold for 2024-2025, recently raised to $2.65M for 2026-2027). File a "no tax due" report: $0.
- Taxes: Same as sole prop for federal (disregarded entity, still Schedule C). Could elect S-Corp taxation later if revenue grows.
- Liability: Personal assets protected from business debts/lawsuits
- Complexity: Slightly more (annual franchise tax filing, registered agent)

**Recommendation:** Form the LLC. $300 one-time cost is cheap liability protection. The annual franchise tax report is a simple no-tax-due form at our revenue level. If you ever get sued (unlikely but possible), your personal assets are protected.

### Self-Employment Tax

- **Rate:** 15.3% (12.4% Social Security + 2.9% Medicare) on net self-employment income
- **Applies to:** Net profit (revenue minus expenses) on Schedule C
- **Deduction:** You deduct 50% of SE tax from adjusted gross income
- **At our scale:** If net profit is $0 (expenses equal revenue), SE tax is $0. Once profitable, budget 15.3% of net profit for SE tax plus your marginal income tax rate.
- **$400 threshold:** If net SE income is under $400, no SE tax is due.

### Deductibility of Our Expenses

| Expense | Deductible? | Category | Notes |
|---------|-------------|----------|-------|
| Anthropic API | Yes, 100% | Other expenses | Ordinary and necessary business expense |
| OpenAI API | Yes, 100% | Other expenses | Same |
| ElevenLabs TTS | Yes, 100% | Other expenses | Same |
| Runway ML | Yes, 100% | Other expenses | Same |
| Hetzner server | Yes, 100% | Other expenses | Cloud computing infrastructure |
| Google Workspace | Yes, 100% | Other expenses | Business productivity suite |
| 1Password | Yes, 100% | Other expenses | Business security tool |
| Domain registration | Yes, 100% | Other expenses | Web presence |
| Orbiter hosting | Yes, 100% | Other expenses | Web hosting |
| Mercury bank fees | Yes, 100% | Other expenses | Business banking |
| Home internet | Partial | Utilities | Business-use percentage only (e.g., 50%) |

**All of our current expenses are fully deductible** as ordinary and necessary business expenses. AI API costs are no different from any other software/service subscription from the IRS's perspective. There's no special treatment or limitation.

### QBI Deduction (Section 199A)

As a sole prop or single-member LLC, you may qualify for the Qualified Business Income deduction: 20% of qualified business income. For income under $191,950 (single, 2025), no limitations apply. This effectively reduces your tax rate on business income by 20%.

---

## 7. Recommendations

### Primary Recommendation: Beancount + Git + AI Agent

**Start with beancount as the primary ledger.** Here's why this is the right choice for sivart.wtf:

1. **Zero cost.** We're already running on a tight budget.
2. **AI-native.** I (the AI agent) can read, write, validate, and report on beancount files without any API integration. The file format IS the interface.
3. **Git-versioned.** Every change is tracked, reversible, and auditable. This is better than any accounting software's audit trail.
4. **Strict validation.** `bean-check` catches errors. This matters when an AI is writing entries.
5. **Fava web UI.** Beautiful reporting dashboard for when you want to see charts and graphs.
6. **Scales up.** If we grow to $10k/mo, beancount still works. If we need a CPA, we can export to standard formats.

### Implementation Steps

1. **Now:** Install beancount and fava on the server (`pip install beancount fava`)
2. **Now:** Create initial chart of accounts based on our actual services
3. **Now:** Backfill January and February 2026 transactions from Mercury statements
4. **Ongoing:** Agent records transactions as they occur
5. **Monthly:** Agent runs close process, generates report
6. **Q2 2026:** Evaluate if quarterly tax estimates are needed
7. **When revenue reaches ~$5k/yr:** Consider forming Texas LLC ($300)
8. **When revenue reaches ~$20k/yr:** Get a CPA consultation

### What NOT to Do

- Don't pay for QuickBooks or Wave Pro. Our volume doesn't justify it.
- Don't use Google Sheets as the primary ledger (no validation).
- Don't mix business and personal (already handled with Mercury).
- Don't wait until tax time to start tracking. Start now.

### Cost of This Setup

**$0/month.** Beancount is free. Git is free. The agent's time is already allocated. Fava runs on the existing Hetzner server.

---

*This document should be reviewed and updated as the operation grows. Tax information is for reference; consult a CPA for specific tax advice.*
