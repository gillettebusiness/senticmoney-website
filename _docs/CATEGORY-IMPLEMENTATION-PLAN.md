# Blog Category Implementation Plan

> **Status:** Draft - Implement when blog reaches 50+ articles
> **Created:** February 4, 2026
> **Target:** Week 12-14 (late March 2026)

---

## Why Categories?

At 50+ articles, a flat blog index becomes hard to navigate. Categories provide:
- **User experience:** Readers find related content faster
- **SEO benefit:** Topic clusters signal expertise to search engines
- **Internal linking:** Natural opportunities for cross-linking
- **Content gaps:** Easier to see which topics need more coverage

---

## Proposed Category Structure

Based on existing content and content calendar:

| Category | Slug | Description | Current Articles |
|----------|------|-------------|------------------|
| **Budgeting Methods** | `methods` | How-to guides for budgeting approaches | 50/30/20, zero-based, envelope, paycheck, monthly budget |
| **App Comparisons** | `comparisons` | Competitor reviews and alternatives | YNAB, Mint, EveryDollar, Quicken, GoodBudget |
| **Privacy & Security** | `privacy` | Plaid risks, local-first, data protection | budget-apps-without-plaid, is-plaid-safe |
| **Couples & Family** | `couples` | Shared finances, family budgeting | couples-budgeting, budget-software-for-couples, best-budget-apps-for-couples |
| **Teen Finance** | `teens` | Young adult money management | how-to-budget-as-a-teenager, budget-advice-for-young-adults, money-management-for-youth, financial-management-for-teens |
| **Christian Finance** | `christian` | Faith-based budgeting | biblical-money-management, christian-budgeting-apps, how-to-budget-for-tithing |
| **Saving & Goals** | `saving` | Emergency funds, financial goals, saving strategies | how-to-build-emergency-fund, how-to-set-financial-goals, pay-yourself-first |
| **Expense Tracking** | `tracking` | Spending tracking guides | how-to-track-your-spending, expense tracker articles |
| **Debt** | `debt` | Debt payoff strategies | debt-payoff-strategies |

**Note:** Some articles may fit multiple categories. Use primary category for URL, add secondary as tags.

---

## URL Structure

### Option A: Flat with Filter (Recommended)
```
/blog                          → All articles (default)
/blog?category=methods         → Filtered view
/blog?category=comparisons     → Filtered view
```

**Pros:** No URL changes, simple implementation, no duplicate content risk
**Cons:** Less SEO value than dedicated pages

### Option B: Category Landing Pages
```
/blog                          → All articles
/blog/category/methods         → Category page with filtered articles
/blog/category/comparisons     → Category page with filtered articles
```

**Pros:** Dedicated pages can rank for category keywords, better for pillar content
**Cons:** More pages to maintain, need unique content per category page

### Option C: Hybrid (Best of Both)
```
/blog                          → All articles with category filter UI
/blog/category/methods         → SEO-optimized landing page + filtered articles
```

**Pros:** Filter UI for users, landing pages for SEO
**Cons:** Most development work

**Recommendation:** Start with **Option A** (quick win), add **Option C** landing pages for top 3 categories later.

---

## Article URL Policy

**CRITICAL: Do NOT change existing article URLs.**

Current: `/blog/best-ynab-alternatives-2026`
Keep as: `/blog/best-ynab-alternatives-2026`

NOT: `/blog/comparisons/best-ynab-alternatives-2026` ❌

Changing URLs breaks:
- Existing Google rankings
- Backlinks
- Internal links
- Bookmarks

Categories are metadata, not URL paths.

---

## Implementation Steps

### Phase 1: Data Layer (Week 12)

1. **Add category field to each article's JSON-LD schema:**
```json
{
  "@type": "BlogPosting",
  "articleSection": "Budgeting Methods",
  ...
}
```

2. **Create category mapping file** (`_data/categories.json` or in JS):
```json
{
  "methods": {
    "name": "Budgeting Methods",
    "description": "Step-by-step guides to popular budgeting approaches",
    "articles": ["50-30-20-budget-rule-guide", "zero-based-budgeting-guide", ...]
  },
  ...
}
```

3. **Add category tag to each article HTML** (visible to users):
```html
<span class="category-tag">Budgeting Methods</span>
```

### Phase 2: Blog Index Filter (Week 13)

1. **Add filter UI to blog/index.html:**
```html
<div class="category-filter">
  <button class="filter-btn active" data-category="all">All</button>
  <button class="filter-btn" data-category="methods">Methods</button>
  <button class="filter-btn" data-category="comparisons">Comparisons</button>
  ...
</div>
```

2. **Add JavaScript for filtering:**
```javascript
// Filter articles by category on click
// Update URL with ?category= parameter
// Persist filter state
```

3. **Add `data-category` attribute to each article card:**
```html
<article class="article-card" data-category="methods">
```

### Phase 3: Category Landing Pages (Week 14, Optional)

Create dedicated pages for top 3 categories:
- `/blog/category/comparisons` - High search intent
- `/blog/category/methods` - Educational authority
- `/blog/category/privacy` - Core differentiator

Each page includes:
- Category-specific H1 and meta description
- Introduction paragraph (unique content, 100-200 words)
- Filtered article grid
- Internal links to related categories
- Category-specific CTA

### Phase 4: Navigation Updates

1. **Add "Topics" dropdown to main nav** (optional):
```html
<li class="dropdown">
  <a href="/blog">Blog</a>
  <ul class="dropdown-menu">
    <li><a href="/blog?category=methods">Budgeting Methods</a></li>
    <li><a href="/blog?category=comparisons">App Comparisons</a></li>
    ...
  </ul>
</li>
```

2. **Add category links to article footers:**
```html
<p>More in <a href="/blog?category=methods">Budgeting Methods</a></p>
```

---

## Schema Markup Updates

### Article Schema Addition
Add `articleSection` to each BlogPosting:
```json
{
  "@type": "BlogPosting",
  "headline": "...",
  "articleSection": "Budgeting Methods",
  ...
}
```

### Category Page Schema (if using Option B/C)
```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Budgeting Methods - SenticMoney Blog",
  "description": "Step-by-step guides to popular budgeting methods...",
  "url": "https://senticmoney.com/blog/category/methods",
  "isPartOf": {
    "@type": "Blog",
    "name": "SenticMoney Blog",
    "url": "https://senticmoney.com/blog"
  }
}
```

---

## Sitemap Updates

If using category landing pages (Option B/C), add to sitemap.xml:
```xml
<url>
  <loc>https://senticmoney.com/blog/category/methods</loc>
  <lastmod>2026-03-15</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.7</priority>
</url>
```

---

## Internal Linking Strategy

When categories are live, update articles with cross-links:

1. **End of article:** "More in [Category Name]" link
2. **Related articles section:** Show 2-3 articles from same category
3. **Pillar content:** Link from category page to cornerstone article

Example for YNAB article:
```html
<p>For more app comparisons, see our guides to
<a href="/blog/best-mint-alternatives-2026">Mint alternatives</a> and
<a href="/blog/everydollar-vs-sentic-money">EveryDollar vs SenticMoney</a>.</p>
```

---

## Migration Checklist

When ready to implement:

- [ ] Finalize category list (review with current article count)
- [ ] Create category mapping (article → category)
- [ ] Add `articleSection` to all article schemas
- [ ] Add `data-category` to all article cards in blog index
- [ ] Add category tag display to all articles
- [ ] Build filter UI on blog index
- [ ] Add filter JavaScript
- [ ] Test filter functionality
- [ ] Update sitemap (if adding category pages)
- [ ] Submit new category pages to Google/Bing (if applicable)
- [ ] Update CLAUDE.md with category guidelines for new articles

---

## New Article Workflow (Post-Implementation)

When creating new articles after categories are live:

1. Assign primary category during writing
2. Add `articleSection` to JSON-LD schema
3. Add `data-category` attribute to blog index card
4. Add category tag to article HTML
5. Include cross-links to 1-2 related articles in same category

---

## Future Enhancements (50+ articles)

- **Tag system:** Secondary categorization (e.g., "beginner", "advanced")
- **Search:** Full-text search across articles
- **Popular/Trending:** Highlight high-traffic articles
- **Series:** Multi-part article sequences
- **Author filter:** If multiple authors added

---

*Plan created February 4, 2026. Review and update when approaching 50 articles.*
