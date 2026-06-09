# AUDIT-SCHEDULE.md

**Purpose:** Track pending GSC re-pulls, CTR diagnostics, content audits, and conversion-flow reviews for senticmoney.com. This file is the canonical schedule. Every session that produces a "revisit in N weeks" decision must add a row to Section 1. Every audit cycle that ships changes must add an entry to Section 3.

**How to use this file (read this every session):**

1. Open this file at the start of any session involving SEO, content strategy, GSC data, or article performance.
2. Check Section 1 — if any trigger date has passed, that's the work for this session (or surface it to the user if not in scope).
3. Check Section 2 for any audits whose release condition has been met by recent events; promote them into Section 1 with a trigger date.
4. At session end, if any decision was made to "revisit in N weeks" or "wait for [outcome]," add the row before closing the session.
5. After any audit-driven change ships, add an entry to Section 3.

**Maintenance rule:** Stale rows are worse than missing rows. If a trigger date passes and the check-in isn't run, either run it, defer it explicitly (update the date with a note explaining why), or move it to Section 3 with "deferred" as the outcome. Never silently skip.

**File location:** Canonical docs only. This file lives in `C:\dev\senticmoney-website\_docs\` alongside INDEXING-TRACKER.md, ARTICLE-STATUS.txt, and other working docs. Files in `_docs/` are not part of the public deploy surface.

---

## Section 1 — Pending check-ins (dated)

Active scheduled work. When a trigger date passes, the row either gets executed (then moves to Section 3) or its date gets pushed forward with a note explaining why.

| Trigger date | URL or target | Action | Decision this informs |
|---|---|---|---|
| 2026-06-02 | `/blog/is-ynab-worth-it` | Pull 14-day GSC data (clicks, impressions, CTR, position) for the URL. Compare to 28-day baseline pulled 2026-05-19 (1 click, 993 impr, 0.1% CTR, pos 12.8). Specifically check: did "is ynab worth it" position improve from 21.6? Did "ynab pricing 2026 monthly annual" (pos 10.3) earn its first click? Did "ynab pricing official 2026" (pos 4.2) start converting? | If pricing queries remain 0% CTR while worth-it improves → build `/blog/ynab-pricing-2026` next cycle. If both improve → snippet fix sufficient; move to next audit target. |
| 2026-06-18 | `/blog/is-ynab-worth-it` | Pull 30-day GSC data for the URL as second confirmation point. | Confirms or disconfirms the 14-day signal. Lower noise than the 14-day pull alone. This is the more important of the two pulls. |
| 2026-06-23 | `/blog/christian-budgeting-apps` | Pull 14-day GSC data (clicks, impressions, CTR, position) for the URL. Compare to 28-day baseline pulled for window ending 2026-06-06 (avg position 6.8, 23 impressions, 0 clicks, 0% CTR). | Success signal: CTR above 3% on the christian budgeting apps query cluster at comparable position. If CTR stays 0% at comparable position, the snippet hook is not the bottleneck for this page. |
| 2026-07-09 | `/blog/christian-budgeting-apps` | Pull 30-day GSC data for the URL as second confirmation point. | Confirms or disconfirms the 14-day signal. Lower noise than the 14-day pull alone. |

---

## Section 2 — Audit backlog (condition-triggered)

Queued audits with no fixed trigger date. Released into Section 1 when the listed condition is met.

| Target | Release condition | Notes |
|---|---|---|
| `/blog/best-personal-finance-app-2026` and `/blog/best-personal-finance-apps-privacy-2026` snippet audit | After is-ynab-worth-it snippet fix shows positive signal at 14-day or 30-day mark | Both URLs already rank page 1 (pos 10.2 and 7.7) with 864 and 785 impressions and 0 clicks in 28 days as of 2026-05-19. Same CTR pathology as is-ynab-worth-it, larger volume. Highest-priority follow-on. |
| Portfolio-wide CTR audit (all 61 articles) | After is-ynab-worth-it snippet fix confirmed at 30-day mark | Pull GSC data for every blog URL: clicks, impressions, CTR, position. Sort into four quadrants by position and CTR. Snippet-fix candidates are page-1, low-CTR URLs. Strategy chat will plan execution batches of 3-5 URLs per cycle. Pre-condition: bulk CSV export from GSC Performance is the data source. |
| Article → download conversion audit | After portfolio CTR audit produces measurable CTR lift | Different bottleneck from snippet conversion. Measures click-to-download rate per landing page. Out of scope until SEO traffic is actually arriving. |
| Download → paid conversion audit | After download volume becomes statistically meaningful | Product-side audit, not SEO. Free → Standard upgrade flow, in-app prompts, email nurture. Last in the sequence by design. |
| URL-CONVENTIONS.md standardization | When LFS bandwidth permanent fix is shipped | Documented tech debt from week 16. Not audit-related but lives here because the work is queued and condition-triggered. Pre-condition: installer migration from LFS to GitHub Releases. |
| Possible keyword cannibalization: `/blog/ynab-alternative` vs `/blog/best-ynab-alternatives-2026` | Resolve during the portfolio-wide CTR audit | Both pages target the ynab alternative(s) query cluster. Rank tracker 2026-06-06: "ynab alternative" position 51.4, "ynab alternatives" position 50.7, 0 clicks each — two pages splitting one query's signals, neither winning. Options: differentiate intent or consolidate with a 301. |
| Priority optimization candidate: `/blog/budget-management-software-guide` | Next optimization session | GSC 28-day window ending 2026-06-06: "budget management software" 776 impressions (62% of site total), avg position 33.8, 0 clicks. First confirm in GSC that this page is the one ranking, then internal-linking pass and snippet review. |

---

## Section 3 — Audit log (append-only, newest at top)

| Date | Target | Finding | Action shipped | Outcome |
|---|---|---|---|---|
| 2026-06-09 | `/blog/christian-budgeting-apps` | 28-day GSC baseline (window ending 2026-06-06): avg position 6.8, 23 impressions, 0 clicks, 0% CTR. Spot-checked at position 4 on 2026-06-09, listed between two FaithFi app-store results with star ratings. Description was a generic compare-style snippet with no verdict, price, or hook. Google is displaying the authored meta description (confirmed via live SERP screenshot 2026-06-09), so meta-level fix applies; capsule sync gates do not. | Meta description rewrite following the is-ynab-worth-it snippet playbook (commit `22d33ce`): description, og:description, and twitter:description set to verdict-led copy (SenticMoney pick, free or $39/yr, on-device privacy hook). Freshness bump: article:modified_time and JSON-LD dateModified to 2026-06-09. Title tag, capsule, FAQ, and body untouched. Commit "Rewrite christian-budgeting-apps meta description for SERP CTR and log GSC check-ins". | Pending. Check-ins scheduled 2026-06-23 (14-day) and 2026-07-09 (30-day). |
| 2026-05-19 | `/blog/is-ynab-worth-it` | 28-day GSC pull revealed intent drift: 80% of 993 impressions came from YNAB pricing queries despite article framed as worth-it verdict. Position 4.2 on "ynab pricing official 2026" with 0 clicks. Capsule asked the question instead of answering it (v3.4 rule misexecution). | Snippet rewrite: title, meta description, H1, and all four capsule sync locations updated. New capsule leads with verdict ("YNAB is worth $109/year if...") and places SenticMoney at word 32. Commit `22d33ce` to website repo. INDEXING-TRACKER.md updated. URL re-submitted to GSC and Bing for re-crawl. | Pending. Diagnostic re-pull scheduled 2026-06-02 (14-day) and 2026-06-18 (30-day). |

---

## Appendix — How rows get added

**Section 1 row template:**

```
| YYYY-MM-DD | [URL or audit name] | [What to pull/measure/do] | [What decision the data informs] |
```

**Section 2 row template:**

```
| [Target] | [Release condition — be specific about what event releases this audit] | [Context, prerequisites, scope notes] |
```

**Section 3 row template:**

```
| YYYY-MM-DD | [Target] | [What the data revealed] | [What shipped — link to commit SHA where relevant] | [Outcome if known, "pending" if not yet measured] |
```
