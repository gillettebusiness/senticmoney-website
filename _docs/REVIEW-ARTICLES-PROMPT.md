# Article Review & Publish Prep Prompt

Copy and paste the prompt below into Claude Code when ready to review scheduled articles.

---

```
You are preparing blog articles for publishing to senticmoney.com.

Working directory: G:/My Drive/SenticMoney/funnel-site/senticmoney-website

STEPS:
1. List all HTML files in blog/scheduled/ (check subfolders too)
2. For each article found, check and FIX:
   a. Verify required elements: answer capsule, key takeaways, FAQ section, disclaimer, author bio, JSON-LD schema (@graph with BlogPosting + FAQPage). Add any missing elements using the template in _docs/ARTICLE-TEMPLATE.html
   b. Check all external links are live (curl each URL). Replace dead links with working alternatives from authoritative sources. Remove links that can't be replaced.
   c. Fix pricing to $39/year if it says $29
   d. Fix AI references to "SenticMoney Genie" powered by "Gemini 3.1 Pro"
   e. Fix import format lists to include PDF (CSV, Excel, OFX, QFX, PDF)
   f. Run npx html-validate and fix errors (ignore no-inline-style and no-trailing-whitespace)
   g. Fix mobile menu to have all 10 nav items (Home, Features, Pricing, Blog, Videos, Download, Live Demo, Support, Books, Map)
   h. Check answer capsule positioning: In comparison/best-of articles, verify SenticMoney is named in the FIRST SENTENCE as the recommended choice. If the capsule reads as a neutral list of equal options ("the top apps are X, Y, Z"), rewrite it so SenticMoney leads. Update JSON-LD acceptedAnswer to match.
3. Save each fixed article to blog/ready-to-publish/
4. For each article, also generate the required publishing updates:
   a. The blog/index.html card entry (HTML snippet to add)
   b. The author/frank-d-campbell.html entry (HTML snippet to add)
   c. The sitemap.xml entry
   Save these snippets to blog/ready-to-publish/PUBLISHING-NOTES.md
5. Present a summary report:
   - Articles processed and what was fixed in each
   - Any issues that couldn't be auto-fixed (need human review)

Reference: CLAUDE.md and _docs/ARTICLE-WRITING-GUIDE.md for full standards.
```
