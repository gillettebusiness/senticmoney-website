Folder URL:   C:\Users\gille\OneDrive\Desktop\CoWork Scheduled Tasks


# Scheduled Task Prompts for Claude Code

Save these as scheduled tasks in Claude Code. All tasks work from the home directory (web-based, no Google Drive access needed).

---

## 1. Live Site Health Check (Weekly)

**Name:** Site health check
**Frequency:** Weekly

```
Check the health of senticmoney.com by visiting every page and reporting issues.

PAGES TO CHECK:
- https://senticmoney.com/
- https://senticmoney.com/features
- https://senticmoney.com/pricing
- https://senticmoney.com/download
- https://senticmoney.com/support
- https://senticmoney.com/privacy
- https://senticmoney.com/terms
- https://senticmoney.com/refund
- https://senticmoney.com/cookies
- https://senticmoney.com/videos
- https://senticmoney.com/blog
- https://senticmoney.com/author/frank-d-campbell
- https://senticmoney.com/books/money-management-for-teens.html
- https://sentic-web-demo.onrender.com (Live Demo)

FOR EACH PAGE:
1. Confirm it returns HTTP 200
2. Check for broken internal links (any link to senticmoney.com that 404s)
3. Verify page has a <title> tag and <meta name="description">

ALSO CHECK:
- https://sentic-web-demo.onrender.com — Render web demo is responding
- Confirm SSL certificate is valid on senticmoney.com

REPORT:
- Pages with issues (status code, missing elements)
- Broken internal links found
- Service status (web demo up/down)
- All clear confirmation if everything passes
```

---

## 2. Competitor Price Monitor (Weekly)

**Name:** Competitor price check
**Frequency:** Weekly

```
Check competitor pricing pages for changes. Compare against known prices below.

COMPETITORS TO CHECK:
1. YNAB — https://www.ynab.com/pricing (known: $14.99/month or $109/year)
2. Monarch Money — https://www.monarchmoney.com/pricing (known: $14.99/month or $99.99/year)
3. EveryDollar — https://www.ramseysolutions.com/ramseyplus/everydollar (known: ~$80/year with Ramsey+)
4. Quicken Simplifi — https://www.quicken.com/simplifi (known: $71.88/year ($5.99/month billed annually — note: promotional first-year rates of 40-50% off are frequently offered))
5. GoodBudget — https://goodbudget.com/pricing (known: $80/year)

FOR EACH:
- Fetch the pricing page
- Extract current pricing
- Compare against the known prices above
- Flag any changes

REPORT:
- Any price changes detected (old price vs new price)
- "No changes" if everything matches
- Note: If a competitor raised prices, this is content opportunity — mention which blog articles could be updated

SenticMoney current pricing for reference: Free tier + $39/year Standard
```

---

## 3. SEO Audit (Weekly)

**Name:** SEO audit
**Frequency:** Weekly

```
Audit senticmoney.com pages for SEO issues, old branding, and meta tag problems.

PAGES TO AUDIT:
- https://senticmoney.com/
- https://senticmoney.com/features
- https://senticmoney.com/pricing
- https://senticmoney.com/download
- https://senticmoney.com/support
- https://senticmoney.com/privacy
- https://senticmoney.com/terms
- https://senticmoney.com/refund
- https://senticmoney.com/cookies
- https://senticmoney.com/videos
- https://senticmoney.com/blog
- https://senticmoney.com/author/frank-d-campbell
- https://senticmoney.com/books/money-management-for-teens.html

FOR EACH PAGE CHECK:
1. <title> exists and is under 60 characters
2. <meta name="description"> exists and is 150-160 characters
3. <meta property="og:title"> and og:description exist
4. <link rel="canonical"> exists and points to correct URL
5. No references to old branding: "CognitoMoney", "CognitoFi", "cognitomoney.com", "cognitofi.com"
6. No references to old pricing: "$29/year"
7. No references to old AI: "Gemini 2.5 Flash", "Gemini 3 Flash", "AI Financial Assistant"
8. Pricing mentions say "$39/year"
9. AI mentions say "SenticMoney Genie" and "Gemini 3.1 Pro"

REPORT:
- Pages with meta tag issues
- Any old branding references found (URGENT — these need immediate fixing)
- Any outdated pricing or AI references
- All clear confirmation if everything passes
```

---

## 4. Blog Link Rot Checker (Weekly)

**Name:** Blog link checker
**Frequency:** Weekly

```
Check all published blog articles on senticmoney.com for dead outbound links.

STEPS:
1. Fetch https://senticmoney.com/blog to get the list of all published articles
2. Visit each article page
3. Extract all external links (href starting with http/https, excluding senticmoney.com)
4. Check each external URL returns HTTP 200 (follow redirects, 10 second timeout)
5. Flag any non-200 responses

REPORT FORMAT:
For each article with issues:
- Article title and URL
- Broken link URL and status code (404, 403, 500, timeout, etc.)
- Suggested action (remove link, find replacement, update URL)

Summary:
- Total articles checked
- Total external links checked
- Total broken links found
- Articles with no issues: list

If all links are healthy, report "All clear — no broken links found across X articles."
```

---

## 5. Render Uptime Ping (Daily)

**Name:** Render uptime ping
**Frequency:** Daily

```
Quick health check on SenticMoney's Render-hosted services.

CHECK THESE ENDPOINTS:
1. https://sentic-web-demo.onrender.com — Web demo (should return 200)
2. https://senticmoney.com — Main site (should return 200)

FOR EACH:
- Record HTTP status code
- Record response time
- Flag if status is not 200 or response time exceeds 5 seconds

REPORT:
- Status and response time for each service
- Flag any issues
- If Render web demo is down, note that free-tier Render services sleep after inactivity and may take 30-60 seconds to cold start — a single slow response is normal, but a non-200 after retrying is a real issue
```

---

## Notes

- All tasks use web requests only — no local file access needed
- Competitor prices were last verified February 2026 — update known prices in the prompts if competitors change pricing
- If the SEO audit finds old branding, fix it immediately in the source files on Google Drive
