# Lessons Learned — SenticMoney Website

---

### 2026-05-18 — HTTP 200 ≠ live content (CFPB blog archive-shell)
- **Tried:** Verified an external link with `curl -o /dev/null -s -w "%{http_code}"` per the writing guide's link-check procedure. URL returned 200.
- **Outcome:** The URL was https://www.consumerfinance.gov/about-us/blog/budgeting-how-to-create-a-budget-and-stick-with-it/ — the CFPB blog was archived May 14, 2026, but the URL shell still resolves. The page now displays "There are no results to display." Curl saw 200; the actual content was gone.
- **Lesson:** Status-code checks are necessary but not sufficient. For any external link, fetch the body and scan for archive-shell markers: "no results to display", "was archived on", "page has moved", "page no longer", "content not found", "page not found". A URL can be a 200 archive shell with no real content behind it. Also: the entire CFPB blog being archived means existing articles may link to specific CFPB blog posts that are now dead-but-200. Run `grep -r "consumerfinance.gov/about-us/blog" blog/` to find and fix exposures before the June 1 citation re-test.

---

### 2026-06-24 — Internal-link integrity: forward + inverse + brand checks (count ≠ identity)
- **Tried:** Two new comparison articles (rocket-money, caleb-hammer) shipped, then spot-checked. Found in-body blog-to-blog links written as `/<slug>` (root) instead of `/blog/<slug>`, 404ing. Root cause: the guide's "bare slugs" rule read as "strip to the slug," dropping the required `/blog/` prefix.
- **Outcome:** Fixed 11 links across the 2 files (commit 1f42fa1). A forward grep (root-form links to existing slugs) confirmed the bug was isolated to those two files. An INVERSE grep (every `/blog/<slug>` link resolving to a real file) then surfaced 3 OTHER pre-existing dead links the forward check structurally could not see: a truncated `50-30-20-budget-rule` and two `everydollar-vs-cognito-money` rebrand leftovers (file renamed COG→SNT, inbound links never updated). Fixed those (commit 6473525). A final case-insensitive brand sweep (`cognito(money|fi)?`) across all .html/.txt/.xml came back empty — rebrand clean in rendered content; survivors had been slug-path-only, invisible to a brand-name grep.
- **Lesson:** A count reconciles totals; a diff reconciles identity. Same pattern recurred with llms.txt (75=75 line-count vs a true 1:1 slug diff) and the rank-tracker reconcile. Run BOTH link directions plus a brand-name sweep — each catches a class the others cannot. Guardrail added to ARTICLE-WRITING-GUIDE: blog-to-blog hrefs use `/blog/<slug>`, plus a pre-publish internal-link grep gate.

---

### 2026-06-24 — Rank-tracker slug count ≠ published-article count
- **Tried:** Rank tracker reported 81 tracked slugs while ARTICLE-STATUS.txt and llms.txt both showed 75 published. Spent time questioning whether the canonical docs were stale.
- **Outcome:** Disk was ground truth: `ls blog/*.html` (minus index) = 75, and ARTICLE-STATUS vs llms.txt diffed to zero against each other. The tracker's 81 = 75 real articles + 6 non-article tracked URLs (alternate-canonical duplicates such as the www/features host-dupe, plus main site pages). No phantom articles, nothing stale in canon.
- **Lesson:** Reconcile published count against DISK (`ls blog/*.html` excluding index.html), never against the rank tracker or GSC "known pages" (which also counts redirects, 404s, and canonical dupes). Tracker reconciliation is post-publish hygiene, not a publishing blocker.

---

## External link durability - federal sites are archiving content (June 2026)

A write-time HTTP 200 is NOT durable. The CFPB archived its entire blog
(consumerfinance.gov/about-us/blog) on May 14, 2026; a specific post that returned 200
with full content earlier in a session was later serving the archived index shell
byte-for-byte (identical response size). In the same June verification pass, FDIC and
Investor.gov budgeting pages 404'd, and usa.gov/budget is about the federal budget, not
personal finance. Lessons:
1. Content-body check is mandatory - grep the response for "archived" / "no results to
   display", not just the HTTP status code.
2. Prefer durable, ad-free sources - MyMoney.gov and FTC consumer pages (consumer.ftc.gov)
   held up; CFPB did not.
3. Re-verify external links at the moment of inclusion, even ones verified earlier in the
   same session.
Fix applied: household-budget-app's CFPB blog link was replaced with mymoney.gov/spend
before publish.
