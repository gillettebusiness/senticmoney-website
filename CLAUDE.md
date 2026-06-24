# senticmoney-website — CLAUDE.md

This repo is the live marketing site for senticmoney.com. It auto-deploys to Render on push to `main`.

---

## Current State

- Index recovery launched 2026-06-09 (commits `d0a34b5`, `63200a2`) - 17 unindexed articles got an internal linking pass (25 links across 20 source articles). GSC URL Inspection submissions due manually: never-crawled 8 on 2026-06-10, crawled-not-indexed 10 on 2026-06-11 (lists in `C:\dev\INDEX-RECOVERY.md` Phase 2). Check-ins logged 2026-06-23 and 2026-07-09 in `_docs/AUDIT-SCHEDULE.md`.

---

## AEO (Answer Engine Optimization) — Added 2026-04-14

### Root-Level AI Files
- `llms.txt` — AI-optimized content index following the llms.txt spec (llmstxt.org). Curated summary, inline FAQ, comparison table, feature tiers, and the full blog catalog (every published article). This is the "recommended reading list" for AI crawlers.
- `llms-full.txt` — Retired May 29, 2026. Maintain only `llms.txt`.
- `robots.txt` — Allows all crawlers (including GPTBot, ClaudeBot, PerplexityBot, Google-Extended). Comments reference llms.txt files.

### Maintenance Rules
- When features change, pricing changes, or new comparison blog posts are published: update `llms.txt` in the same commit.
- The FAQ section in `llms.txt` should mirror the most common questions from the support page.
- Blog list in `llms.txt` is the FULL published catalog — every published article appears exactly once (currently 75). The earlier "curate to top ~25" rule was evaluated and deliberately rejected: for a catalog of distinct articles, full coverage maximizes AI-crawler discovery, which is the file's purpose. Do not prune to a subset. (Parallels the May 29 2026 llms-full.txt retirement: one canonical, complete index.) Add every new article to llms.txt in the publish commit.
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
- `PUBLISH-FLOW.md` — full publish procedure for shipping article batches

Full publish procedure: see `_docs/PUBLISH-FLOW.md`.
