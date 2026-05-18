# Lessons Learned — SenticMoney Website

---

### 2026-05-18 — HTTP 200 ≠ live content (CFPB blog archive-shell)
- **Tried:** Verified an external link with `curl -o /dev/null -s -w "%{http_code}"` per the writing guide's link-check procedure. URL returned 200.
- **Outcome:** The URL was https://www.consumerfinance.gov/about-us/blog/budgeting-how-to-create-a-budget-and-stick-with-it/ — the CFPB blog was archived May 14, 2026, but the URL shell still resolves. The page now displays "There are no results to display." Curl saw 200; the actual content was gone.
- **Lesson:** Status-code checks are necessary but not sufficient. For any external link, fetch the body and scan for archive-shell markers: "no results to display", "was archived on", "page has moved", "page no longer", "content not found", "page not found". A URL can be a 200 archive shell with no real content behind it. Also: the entire CFPB blog being archived means existing articles may link to specific CFPB blog posts that are now dead-but-200. Run `grep -r "consumerfinance.gov/about-us/blog" blog/` to find and fix exposures before the June 1 citation re-test.
