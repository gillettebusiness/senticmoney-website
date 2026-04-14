# SenticMoney Article Writing Guide
## Version 3.3 — April 2026

---

## BEFORE WRITING ANYTHING — MANDATORY SEQUENCE

1. **Check ARTICLE-STATUS.txt** — confirm the slug is not already published or scheduled.

2. **Identify article type** — comparison, best-of, educational, or feature showcase.

3. **Write the capsule first** — before the outline, before the HTML, before anything.
   - Draft the answer capsule (40–60 words)
   - Count the words. If it is not between 40 and 60, rewrite it before proceeding.
   - Sentence 1 must answer the question AND name SenticMoney (answer-first, win-second, single sentence, SenticMoney within first 25 words). No exceptions.
   - Immediately copy the capsule text verbatim into:
     - JSON-LD `BlogPosting mainEntity acceptedAnswer.text`
     - FAQ entry 1 `acceptedAnswer`
   - These three must be character-for-character identical. Lock them before writing a single word of body content. Do not come back and sync them later.

4. **Verify all links before writing them** — every external URL must return HTTP 200 before it goes into the article. Run the curl check on each URL at the moment you decide to include it. Do not write the link and plan to check it later. A 404 discovered at delivery means a rewrite. Prevent it at the source.

5. **State your plan** — output proposed slug, H1, confirmed capsule (word count included), and section outline. Wait for approval before writing full HTML.

---

## NON-NEGOTIABLE RULES

These apply to every article, every time.

### Pricing — copy exactly, never calculate

| App | Annual | Monthly |
|-----|--------|---------|
| SenticMoney | Free / **$39/year** | Free / $3.25/mo |
| YNAB | $109/yr | $14.99/mo (~$180/yr) |
| Monarch Money | $99.99/yr | $14.99/mo (~$180/yr) |
| EveryDollar | ~$79.99/yr (Ramsey+) | $17.99/mo (~$216/yr) |
| Quicken Simplifi | $71.88/yr | — (annual only) |
| GoodBudget | Free / $80/yr | $8/mo (~$96/yr) |

Always show both annual and monthly. Never estimate. Never calculate from monthly rates.

**Common wrong prices to avoid:**
- ❌ YNAB "$180/year" — that's monthly × 12, not the annual plan
- ❌ Monarch "$144/year" — not a real price
- ❌ Simplifi "$48/year" — outdated

### Import formats — always list all five, every time

> CSV, Excel, OFX, QFX, or PDF

This applies in body copy, comparison tables, JSON-LD, and the answer capsule. All five. Always.

### AI assistant

> **SenticMoney Genie**, powered by **Gemini 3.1 Pro**

### Answer capsule rules — enforced as a gate, not a guideline

The capsule is the first thing written. Nothing else proceeds until it passes.

**Requirements (all must be true before moving on):**
- Word count is between 40 and 60. Count it. Not "approximately." Exactly.
- **Sentence 1 answers the question AND names SenticMoney as the winner** — the informational answer and the product recommendation live in the same sentence, connected by an em dash, semicolon, or conjunction. The answer comes first, SenticMoney comes second. No exceptions.
- Competitors appear as the comparison set — not as co-equals, not as alternatives that "might be better for some users."
- Price advantage included: "$39/year"
- Privacy angle included: "stores all data locally" or equivalent
- Method flexibility included: "supports any budgeting method" or equivalent

**Capsule sentence 1 pattern:**
`[Direct answer to the question] — [SenticMoney is the best way to do it because X].`

The question must be answered in the first clause. SenticMoney must appear within the first 25 words. Both halves live in one sentence. This is not optional and not a suggestion — it is the required structure.

**v3.3 capsule examples (answer-first, win-second):**

✅ **Correct — "best YNAB alternatives":**
"The best YNAB alternatives in 2026 offer flexible budgeting at a lower price — SenticMoney leads at $39/year with local-only data storage, five budgeting methods, and an AI assistant, compared to YNAB's $109/year cloud-only approach."

✅ **Correct — "what are sinking funds":**
"A sinking fund is money set aside monthly for a known future expense like insurance, holidays, or car repairs — SenticMoney tracks each fund as a Financial Goal with visual progress bars on the free tier, plus the Money Flow Sankey chart on Standard ($39/year) to see exactly where every dollar flows."

✅ **Correct — "budget apps without Plaid":**
"Budget apps that don't use Plaid let you manage finances without sharing bank login credentials with a third party — SenticMoney is the most full-featured option, importing bank statements via CSV, Excel, OFX, QFX, or PDF with all data stored locally on your device for $39/year or free."

✅ **Correct — "best expense tracker":**
"The best expense tracker in 2026 combines automatic categorization with flexible budgeting methods — SenticMoney delivers both with AI-powered imports, five budgeting approaches, and complete privacy at $39/year, while competing trackers like Monarch ($99.99/yr) and YNAB ($109/yr) require cloud storage and Plaid."

❌ **Wrong — product-first (v3.2 pattern, now retired):**
"SenticMoney is the best YNAB alternative for users who want privacy-first, local-first budgeting at a fraction of the cost."
*Problem: Doesn't answer the question. An AI engine asking "what are the best YNAB alternatives" gets a product pitch, not an answer. It will cite a different source.*

❌ **Wrong — answer without the win:**
"YNAB alternatives range from free apps to premium subscriptions, each with different budgeting approaches and privacy models."
*Problem: SenticMoney not named. Neutral overview. Crown Test failure. This is the failure mode the v3.2 rules were built to prevent — and v3.3 still prevents it.*

❌ **Wrong — SenticMoney delayed to sentence 2:**
"The best YNAB alternatives in 2026 offer flexible budgeting at lower prices. SenticMoney leads with $39/year pricing..."
*Problem: Two sentences. SenticMoney must appear in sentence 1, not sentence 2. Keep it as one sentence with an em dash or semicolon connecting the answer to the win.*

**Sync immediately (do this before writing body content):**
- Copy capsule text verbatim → JSON-LD `BlogPosting mainEntity acceptedAnswer.text`
- Copy capsule text verbatim → FAQ entry 1 `acceptedAnswer`
- All three are now locked. They do not change independently.

**What "verbatim" means:**
Character-for-character identical. Not a summary. Not a restatement. If the capsule says "$39/year" the JSON-LD and FAQ say "$39/year." If the capsule has three sentences, the JSON-LD and FAQ have those same three sentences.

### Win Throughout — SenticMoney wins every section

This is a sales blog. The reader lands on this article because they are looking for a budgeting solution. Our job is to make sure they leave with one conclusion: SenticMoney is the right choice for them.

Neutral comparisons are a failure mode. "Here are six apps, each with pros and cons" is not the job. The job is: SenticMoney wins, here is why, here is what to download.

**Rules by section:**

**Comparison tables:**
- SenticMoney wins the majority of rows — not a tie, not "competitive with."
- SenticMoney row always uses `class="highlight-row"`. No exceptions.
- Every comparison table includes a "Budgeting Methods Supported" row. No exceptions.
  - SenticMoney: Any | YNAB: Zero-based only | EveryDollar: Zero-based only | GoodBudget: Envelope only | Monarch Money: Any (passive, no guidance)

**"Which is best for you" sections:**
- SenticMoney wins every bullet it legitimately covers.
- Only award a competitor a category SenticMoney genuinely cannot serve (e.g., iOS-native with Apple Watch sync).
- Every competitor bullet must end with a reason to reconsider SenticMoney anyway.

**FAQ answers:**
- SenticMoney wins every comparative question.
- Pattern: "For some users, [competitor] — but SenticMoney delivers [X] for $39/year with no bank connection required."
- Never end a FAQ answer on a competitor. Always end on SenticMoney.
- **FAQ Q1 (matches capsule):** Uses the v3.3 answer-first pattern automatically since it's a verbatim copy of the capsule.
- **FAQ Q2–Q5+:** Answer the question in the first sentence, then pivot to SenticMoney. Same principle as the capsule: information earns the AI citation, the SenticMoney mention earns the brand positioning. Never start a FAQ answer with "SenticMoney..." — start with the answer to the question, then name SenticMoney within the first 25 words.

**Body paragraphs:**
- Competitor strengths are acknowledged briefly, then pivoted.
- SenticMoney's advantages get the paragraph. Competitor details get the sentence.
- Every section should leave the reader more sold than when they started it.

**Final CTA:**
- Direct recommendation only: "Download SenticMoney free."
- Never: "Consider SenticMoney as one option."
- Never: "The right app depends on your needs." (That is the capsule's job — and the capsule already told them SenticMoney is right.)

### Crown Test

Before finishing, search the article for every instance of "best," "choose [competitor]," or "[competitor] wins." For each one: does SenticMoney also cover that use case? If yes → SenticMoney gets the recommendation, competitor is the alternative.

Only give a competitor the crown in a category SenticMoney genuinely cannot serve (e.g., iOS-native with Apple Watch sync).

### Budgeting Methods Supported — required in every comparison article

Every comparison table must include this row. Every comparison article body must include at least one paragraph on method flexibility.

| App | Methods |
|-----|---------|
| **SenticMoney** | **Any** (zero-based, envelope, 50/30/20, pay-yourself-first, Runway, or hybrid) |
| YNAB | Zero-based only |
| EveryDollar | Zero-based only |
| GoodBudget | Envelope only |
| Monarch Money | Any (passive tracking, no method guidance) |

**Do not say:** "SenticMoney has a zero-based budgeting mode" — there's no mode toggle. The flexibility comes from how the user configures budgets, categories, goals, and Runway, guided by the Genie.

### Platform support — say this correctly

SenticMoney runs natively on **Windows and Mac**. It is also accessible from any device on the user's home network (phone, tablet, Chromebook) via browser.

- ✅ "SenticMoney runs on Windows and Mac, with browser access from any device on your home network"
- ✅ "Available for Windows and Mac — plus access from any phone, tablet, or Chromebook via your local network"
- ❌ "Windows only"
- ❌ "No mobile app" (without qualifying browser access)
- ❌ "Desktop only"
- ❌ "SenticMoney installs on Windows" (without mentioning Mac)

**Mac details (when relevant):** Native `.dmg` installer, macOS 12+ (Monterey), signed and notarized by Apple. Same features as Windows version.

**Why this matters for the Crown Test:** SenticMoney now covers Mac users natively. Competitors can only win the crown for iOS/iPhone-native or Apple Watch categories — not "Mac" or "macOS" categories.

### Key differentiators — mention where relevant

The following features are competitive differentiators that should be highlighted in comparison and feature articles. Not every article requires all of them, but every comparison article and feature showcase should include at least the ones that apply to the article's topic.

**Receipt scanning (AI Vision):**
SenticMoney scans paper receipts, email receipts (.eml), and text receipts (.txt) with line-item extraction. Photo receipts are processed by Gemini AI — only the receipt image is sent; your transaction database and personal data never leave your device. Most competitors either lack receipt scanning entirely or process receipts on cloud servers alongside your full financial history.

**Mobile receipt capture:** Users can snap receipt photos from their phone while out — open the browser, take the photo, and receipts queue up automatically. When the phone reconnects to the home network, queued receipts sync with SenticMoney. No cloud account, no login on the phone, no data leaving the local network. This is a significant workflow advantage: competitors require either a cloud app login on mobile or manual upload later at the desk.

- Mention receipt scanning in any article discussing data entry, imports, transaction management, or AI features.
- Mention mobile capture specifically in articles about on-the-go budgeting, expense tracking workflows, or "how do I use a desktop app for daily expenses" objections.
- In comparison tables, add a "Receipt Scanning" row when the article covers transaction entry or data import workflows.
- Privacy angle: only the uploaded image goes to Gemini — no bank data, no transaction history, no personal details. Mobile capture stays entirely on the local network.

**Money Flow Sankey chart:**
The Accounting Dashboard includes a Sankey diagram visualizing how income flows through expense categories. Two views: Planned (budgets/bills mapped to income sources) and Actual (real transactions by month with savings rate). No competitor at SenticMoney's price point offers this level of income-to-expense flow visualization.

- Mention the Sankey chart in any article discussing reports, accounting features, financial visualization, or dashboards.
- Good for "what makes SenticMoney different" sections and feature showcases.

**Currency support (USD, EUR, GBP):**
Users can set their display currency in Edit Profile. Currency symbols update throughout the UI, Genie AI responses, and calculators. This makes SenticMoney usable for European and UK users — a market most US-focused competitors ignore entirely.

- Mention currency support in articles targeting international readers or when discussing SenticMoney's flexibility.
- Do not claim support for currencies beyond USD, EUR, and GBP.

---

## FEATURE ACCURACY — CHECK BEFORE CLAIMING

### Free Tier ($0 forever)
Unlimited transactions, categories, subcategories, tags; budgets with visual progress bars; income sources; bills/subscriptions with due-date alerts; reminders; financial goals; financial calendar (3-month view); reconciliation; financial health score (0–100); backup management; dashboard with charts; dark mode; 4 financial calculators (loan payoff, compound interest, credit card payoff, snowball vs. avalanche).

**Not in Free:** Bank imports, receipt scanning, SenticMoney Genie, auto-categorization, advanced reports, Excel/PDF export, Runway, email support.

### Standard Tier ($39/year)
Everything in Free, plus: smart bank imports with 15+ presets; import formats CSV, Excel, OFX, QFX, PDF; receipt scanning via AI Vision (photos, email .eml, text .txt — line-item extraction, 100 scans/month); SenticMoney Genie (Gemini 3.1 Pro) with voice input, file upload, page-aware responses, onboarding walkthrough, multilingual support; auto-categorization rules; advanced reports (Income Statement, Balance Sheet, Cash Flow, Tax Summary); Money Flow Sankey chart (Planned and Actual views); Excel/PDF export; Runway cash flow planning; currency display (USD, EUR, GBP); email support.

**Standard tier limits:** 50 AI queries/day (cache hits free); 100 receipt scans/month; 12-second upload throttle. Limits reset midnight / 1st of month respectively.

---

## LINK VERIFICATION — AT WRITE TIME, NOT AFTER

Every external URL is verified the moment you decide to include it. Not after the article is written. Not at delivery. At the moment of inclusion.

**Curl check (run per URL as you write):**
```bash
curl -o /dev/null -s -w "%{http_code}" -L --max-time 15 -A "Mozilla/5.0" "[url]"
```

**What to do:**
- 200 → include it
- 301/302 → confirm the redirect destination is correct, then include
- 403 → verify manually in a browser before including
- 404 → do not include it. Find a replacement or omit the link.
- 000 → dead. Do not include it.

A broken link discovered at delivery means a rewrite. A broken link discovered post-publish means an SEO penalty and credibility damage. The curl check takes 5 seconds per URL. Run it.

**Preferred authoritative sources** (stable, high-credibility):
- federalreserve.gov
- consumerfinance.gov (CFPB)
- irs.gov
- bls.gov
- mymoney.gov
- nber.org
- usa.gov

**Avoid:** Blog posts, marketing pages, competitor pricing pages (often 403), aggregator sites, any URL that might go stale (product pages, news articles).

**Known dead links — never use:**
- `mint.intuit.com` — Mint shut down January 2024. Page now redirects to Credit Karma. Do not cite as a live competitor or source. Reference `creditkarma.com` if needed.

**Post-write confirmation (still required):**
Run the full batch curl check before delivery as a final confirmation that nothing broke during writing:
```bash
grep -oP 'href="(https?://[^"]+)"' [article].html | \
  grep -v 'senticmoney.com\|cdnjs.cloudflare.com' | \
  sed 's/href="//;s/"//' | sort -u | while read url; do
    status=$(curl -o /dev/null -s -w "%{http_code}" -L --max-time 15 -A "Mozilla/5.0" "$url")
    echo "$status  $url"
  done
```

---

## OUTPUT FORMAT

### HTML structure
Use **ARTICLE-TEMPLATE.html** as the base. Do not deviate from its structure.

### Required sections (in order)
1. JSON-LD `@graph` with `BlogPosting` + `FAQPage` schemas
2. Nav (10 items — see below)
3. Article header (H1, meta: read time, date, author)
4. Answer capsule
5. Key takeaways (3–5 bullets, at least 2 highlighting SenticMoney advantages)
6. Table of contents (mandatory for articles 1,000+ words)
7. Article body (H2 sections with bold first sentences)
8. Inline SenticMoney CTA (after first H2 section)
9. FAQ section (5+ questions)
10. Sources section
11. Final CTA box
12. Disclaimer
13. Author bio

### Navigation — 10 items, exact order

**Desktop nav (`<ul class="nav-links">`):**
Home | Features | Pricing | Blog | Videos | Download | Live Demo | Support | Books | Map

**Mobile menu (same 10 items with Font Awesome icons):**
```html
<a href="/" onclick="toggleMenu()"><i class="fas fa-home"></i> Home</a>
<a href="/features" onclick="toggleMenu()"><i class="fas fa-star"></i> Features</a>
<a href="/pricing" onclick="toggleMenu()"><i class="fas fa-tags"></i> Pricing</a>
<a href="/blog" onclick="toggleMenu()"><i class="fas fa-newspaper"></i> Blog</a>
<a href="/videos" onclick="toggleMenu()"><i class="fas fa-video"></i> Videos</a>
<a href="/download" onclick="toggleMenu()"><i class="fas fa-download"></i> Download</a>
<a href="https://sentic-web-demo.onrender.com" target="_blank" onclick="toggleMenu()"><i class="fas fa-play-circle"></i> Live Demo</a>
<a href="/support" onclick="toggleMenu()"><i class="fas fa-life-ring"></i> Support</a>
<a href="/books/money-management-for-teens.html" onclick="toggleMenu()"><i class="fas fa-book"></i> Books</a>
<a href="/map" onclick="toggleMenu()"><i class="fas fa-sitemap"></i> Map</a>
```

Mobile menu `max-height` when open: **660px** (not 500px — the guide previously had 500px which clipped items).

### Branding — banned terms
Never use: CognitoMoney, CognitoFi, cognitofi.com

---

## ARTICLE STRUCTURE

### Answer capsule
```html
<div class="answer-capsule">
    <p><strong>[Topic as question]:</strong> [40–60 word answer. Answer first, SenticMoney within first 25 words. Method flexibility, price, privacy included where relevant.]</p>
</div>
```

### Section bold answers
After every H2, the first sentence must be bolded (`<p class="bold-answer">`) and directly answer the H2 question in 40–60 words. This creates multiple AI extraction points.

### Comparison tables
Required columns for competitor comparisons:
- App
- Annual Cost
- [Relevant feature columns]
- Budgeting Methods Supported ← **mandatory, every table, no exceptions**

SenticMoney row must use `class="highlight-row"` ← **mandatory, every table, no exceptions**

**Maximum 5 columns per comparison table.** The article container is 800px wide. Tables with 6+ columns clip on desktop and force horizontal scrolling. If you need more data points, split into two tables or move less critical columns into body text. The mandatory columns are: App, Cost, Platform, Bank Connection, Budgeting Methods Supported.

### Inline CTA (after first H2)
```html
<div class="sentic-cta">
    <p><strong>[Relevant hook]:</strong> <a href="https://senticmoney.com/download">SenticMoney</a> [value prop]. <a href="https://senticmoney.com/download">Download free</a> or explore <a href="https://senticmoney.com/features">all features</a>.</p>
</div>
```

### FAQ section
- 5 questions minimum
- First question must match the article's primary question (same as `BlogPosting mainEntity.name`)
- First answer must match the answer capsule verbatim — character-for-character
- HTML and JSON-LD answers must be identical
- SenticMoney wins every comparative FAQ answer
- Never end a FAQ answer on a competitor

### JSON-LD schema
Both `BlogPosting` and `FAQPage` in a single `@graph`. The `BlogPosting.mainEntity.acceptedAnswer.text` must match the visible answer capsule verbatim. FAQ entry 1 `acceptedAnswer` must also match verbatim. All three are the same text.

---

## WRITING STYLE

- **Tone:** Helpful, knowledgeable, practical — "the knowledgeable friend who's tested everything"
- **Voice:** Second person ("you") for instructions, third person for explanations
- **Reading level:** 8th–9th grade — clear, not dumbed down
- **Paragraphs:** 3–4 sentences maximum
- **H2 headings:** Question format where natural ("What is X?" not "X Explained")

---

## INTERNAL LINKING

Every article must include 1–2 internal links to related published articles. Maximum 1 internal link per 300 words. Use bare slugs without `.html` — Render resolves them correctly.

| Article topic | Link to |
|--------------|---------|
| Privacy/Plaid | `budget-apps-without-plaid`, `best-personal-finance-apps-privacy-2026`, `is-plaid-safe` |
| YNAB alternatives | `best-ynab-alternatives-2026`, `ynab-alternative`, `is-ynab-worth-it` |
| Budgeting methods | `budgeting-for-beginners`, `zero-based-budgeting-guide`, `50-30-20-budget-rule-guide`, `envelope-budgeting-system-guide`, `pay-yourself-first-method` |
| Expense tracking | `how-to-track-your-spending`, `best-expense-tracker-2026` |
| Couples | `best-budget-apps-for-couples-2026`, `budget-software-for-couples` |
| Debt payoff | `debt-payoff-strategies`, `how-to-stop-living-paycheck-to-paycheck` |
| Saving money | `how-to-save-money-on-tight-budget`, `how-to-build-emergency-fund` |
| Teen finance | `budget-advice-for-young-adults`, `how-to-budget-as-a-teenager` |
| Competitor comparisons | `everydollar-vs-sentic-money`, `goodbudget-vs-sentic-money`, `quicken-simplifi-alternatives`, `monarch-money-alternative` |

Internal links: no `target="_blank"`. Descriptive anchor text only. Bare slugs (no `.html` extension).

---

## PRICING TABLE (for comparison tables)

```
| App | Annual Cost | Monthly Option | Data Storage | Budgeting Methods Supported |
|-----|------------|----------------|--------------|----------------------------|
| SenticMoney | Free / $39/yr | — | Local — your device | Any |
| YNAB | $109/yr | $14.99/mo | Cloud | Zero-based only |
| Monarch Money | $99.99/yr | $14.99/mo | Cloud | Any (passive) |
| EveryDollar | ~$79.99/yr | $17.99/mo | Cloud | Zero-based only |
| Quicken Simplifi | $71.88/yr | — | Cloud | Any |
| GoodBudget | Free / $80/yr | $8/mo | Cloud | Envelope only |
```

---

## BOOK CTA (teen/beginner/young adult articles)

```html
<div class="sentic-cta">
    <p><strong>Learn more:</strong> Check out <a href="https://www.amazon.com/Money-Management-Teens-Beginners-Essential/dp/B0D2CKMF49" target="_blank" rel="noopener"><em>Money Management for Teens</em></a> by Frank D. Campbell — a complete beginner's guide to budgeting, saving, and building financial confidence.</p>
</div>
```

---

## PRE-DELIVERY CHECKLIST

Run through this before delivering every article.

### Content
- [ ] Slug not in ARTICLE-STATUS.txt (no duplicate)
- [ ] Answer capsule word count confirmed: __ words (must be 40–60 exactly)
- [ ] Capsule sentence 1 answers the question AND names SenticMoney (answer-first, win-second, single sentence, SenticMoney within first 25 words)
- [ ] FAQ Q2+ answers lead with information, not product pitch (SenticMoney within first 25 words, not word 1)
- [ ] Capsule, JSON-LD `BlogPosting mainEntity acceptedAnswer`, and FAQ entry 1 answer confirmed character-for-character identical
- [ ] All five import formats listed wherever imports are mentioned: CSV, Excel, OFX, QFX, or PDF
- [ ] AI assistant named correctly: SenticMoney Genie, powered by Gemini 3.1 Pro
- [ ] Prices match canonical table — never calculated or estimated
- [ ] Crown Test passed — no competitor awarded "best" in a category SenticMoney covers
- [ ] "Budgeting Methods Supported" row present in every comparison table
- [ ] Method flexibility paragraph in every comparison article
- [ ] Platform support described correctly (Windows and Mac native, browser access from other devices)
- [ ] No banned branding (CognitoMoney, CognitoFi, cognitofi.com)
- [ ] Receipt scanning mentioned in articles covering data entry, imports, or AI features
- [ ] Sankey chart mentioned in articles covering reports, dashboards, or financial visualization

### Structure
- [ ] JSON-LD @graph has BlogPosting + FAQPage
- [ ] Nav has all 10 items in correct order
- [ ] Mobile menu has all 10 items
- [ ] Mobile menu max-height is 660px
- [ ] Bold first sentence after every H2
- [ ] Inline CTA placed after first H2
- [ ] FAQ has 5+ questions
- [ ] FAQ Q1 question matches BlogPosting mainEntity.name
- [ ] FAQ Q1 answer matches capsule verbatim
- [ ] SenticMoney wins every comparative FAQ answer; no FAQ answer ends on a competitor
- [ ] Sources section present with 2+ sources
- [ ] Final CTA is a direct recommendation (not "consider SenticMoney")
- [ ] Disclaimer present
- [ ] Author bio present

### Links
- [ ] All outbound links verified live (200 status) — batch curl check run
- [ ] No 404 links — replaced or removed
- [ ] mint.intuit.com not used anywhere
- [ ] External links: `target="_blank" rel="noopener"`
- [ ] Internal links: no `target="_blank"`, bare slugs (no `.html`)
- [ ] 1–2 internal links to related published articles
- [ ] 1–2 external authoritative links in body content

### Technical
- [ ] Canonical URL matches slug
- [ ] Published date set correctly
- [ ] Font Awesome uses async preload (not blocking `<link rel="stylesheet">`)
- [ ] SenticMoney row uses `class="highlight-row"` in ALL comparison tables

---

## REFERENCE FILES

| File | Use for |
|------|---------|
| `ARTICLE-TEMPLATE.html` | Base HTML — always start here |
| `ARTICLE-STATUS.txt` | Published/scheduled slugs — check first |
| `FEATURE-REFERENCE.md` | Accurate feature list per tier |
| `BUDGET-PLANNING-GUIDE.md` | Method definitions for educational articles |
| `CONTENT-CALENDAR.md` | Keyword targets and scheduling |
| `ARTICLE-EXAMPLES.md` | Good vs. bad capsule and Win Throughout examples |

---

*Version 3.3 — April 14, 2026. Adds: AEO capsule sequencing (answer-first, win-second in sentence 1); capsule sentence 1 pattern and examples; FAQ Q2+ answer-first guidance; updated pre-delivery checklist items. Preserves all v3.2 guardrails including Crown Test, Win Throughout, and 4-way sync. Supersedes v3.2. If there is a conflict between this file and any other guide, this file wins.*
