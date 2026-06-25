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

### 2026-06-24 - Rank tracker is a hand-maintained keyword list, not an article/slug count
- **Tried:** Rank tracker reported 81 tracked entries while ARTICLE-STATUS.txt and llms.txt showed 75 published. Initially inferred "81 = 75 articles + 6 non-article URLs (canonical dupes + site pages)" without inspecting the tracker's source.
- **Outcome:** Inspecting `keywords.json` (in the separate `senticmoney-rank-tracker` repo) corrected that: the tracker is a HAND-MAINTAINED target-keyword list, not a slug list and not GSC-derived. It held 81 KEYWORDS mapped across the ~73-article pre-batch catalog - several articles carry multiple keywords (e.g. `50 30 20 rule` + `50/30/20 budget`, `emergency fund` + `how to build emergency fund`), and there are NO site-page rows. The two June-24 articles were absent simply because nothing auto-adds them; their keywords were added by hand (81 -> 87).
- **Lesson:** Two things. (1) Reconcile published count against DISK (`ls blog/*.html` minus index.html), never the rank tracker - it is a different unit (curated target keywords, many-to-one with articles). (2) CROSS-REPO GAP: the website publish ripple does not touch `senticmoney-rank-tracker`. Every new article needs its target keywords hand-added to `keywords.json` plus a fetch, as an explicit post-publish step. Codified in PUBLISH-FLOW.md. Earlier-session inference about the "+6" composition was wrong because it reasoned from counts instead of opening the source file - same count-vs-identity lesson, one level up.

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
