# senticmoney-website — CLAUDE.md

This repo is the live marketing site for senticmoney.com. It auto-deploys to Render on push to `main`.

---

## AEO (Answer Engine Optimization) — Added 2026-04-14

### Root-Level AI Files
- `llms.txt` — AI-optimized content index following the llms.txt spec (llmstxt.org). Curated summary, inline FAQ, comparison table, feature tiers, and top blog links. This is the "recommended reading list" for AI crawlers.
- `llms-full.txt` — Companion file that inlines all key content in a single markdown document. AI agents load this for full context in one request.
- `robots.txt` — Allows all crawlers (including GPTBot, ClaudeBot, PerplexityBot, Google-Extended). Comments reference llms.txt files.

### Maintenance Rules
- When features change, pricing changes, or new comparison blog posts are published: update `llms.txt` and `llms-full.txt` in the same commit.
- Keep `llms-full.txt` content in sync with `llms.txt` — they should contain the same core content.
- The FAQ section in `llms.txt` should mirror the most common questions from the support page.
- Blog list in `llms.txt` is curated to top ~25 highest-AEO-value articles. Not every blog post belongs here — prioritize comparison guides, privacy articles, and budgeting method guides over niche topic posts.
- The comparison table in `llms.txt` is a primary citation source — keep competitor pricing and feature data current.

### Schema Markup (JSON-LD)
- Homepage: `WebSite` + `Organization` + `SoftwareApplication` with offers and featureList
- Download: `SoftwareApplication` with downloadUrl and operatingSystem
- Pricing: `SoftwareApplication` with detailed offers + `FAQPage` with pricing FAQ
- Features: `SoftwareApplication` with full featureList
- Support: `FAQPage` matching visible FAQ content on the page

When the app version changes: update `softwareVersion` in the homepage and download page schema.
When pricing changes: update all `Offer` blocks across homepage, download, and pricing schemas.
When features change: update `featureList` in homepage and features schemas.

---

## _docs Folder — Article Writing System

The `_docs/` folder in this repo is the single source of truth for all article writing guides, templates, and content planning. Previously duplicated in `senticmoney-marketing` — consolidated here April 2026.

Key files:
- `ARTICLE-WRITING-GUIDE.md` (v3.3) — mandatory rules for every blog article, including AEO capsule sequencing
- `ARTICLE-TEMPLATE.html` — base HTML template for all blog posts
- `ARTICLE-STATUS.txt` — published/scheduled slug tracking
- `FEATURE-REFERENCE.md` — accurate feature list per tier
- `CONTENT-CALENDAR.md` — keyword targets and scheduling
- `ARTICLE-EXAMPLES.md` — good vs bad capsule and Win Throughout examples
