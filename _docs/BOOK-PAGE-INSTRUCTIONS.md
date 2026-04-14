# Book Page Instructions (AEO 2026) - SenticMoney

## Philosophy: Topic Authority Hub, Not Sales Page

Book pages should be "Answer Hubs" that Google can summarize in AI Overviews. The goal is to be THE answer when someone asks "How do I learn [topic]?"

---

## Required Page Structure (Top to Bottom)

### 1. Answer Capsule (CRITICAL)
Immediately after the H1 title, add a 40-60 word summary block. This is what AI extracts.

```html
<div class="answer-capsule">
    <p><strong>Quick Summary:</strong> [Book Title] is a comprehensive guide to [topic], covering [key areas]. This [year] edition helps [target audience] master [skill/outcome] with practical strategies and real-world examples.</p>
</div>
```

**Formula:**
1. What it is (comprehensive guide to X)
2. What it covers (from A to B)
3. Who it's for (beginners AND professionals)
4. What outcome they'll achieve

---

### 2. Buy Buttons
Place immediately after the answer capsule for conversion.

```html
<div class="buy-buttons">
    <a href="[AMAZON_PAPERBACK_URL]" class="btn btn-primary" target="_blank" rel="noopener">
        <i class="fab fa-amazon"></i> Paperback
    </a>
    <a href="[AMAZON_KINDLE_URL]" class="btn btn-secondary" target="_blank" rel="noopener">
        <i class="fab fa-amazon"></i> Kindle
    </a>
</div>
```

---

### 3. What You'll Learn (Bulleted)
Use checkmark icons for visual appeal:

```html
<ul class="learn-list">
    <li><i class="fas fa-check"></i> <strong>Topic 1</strong> - Brief explanation</li>
    <li><i class="fas fa-check"></i> <strong>Topic 2</strong> - Brief explanation</li>
</ul>
```

**2026 Entity Requirements (Personal Finance):**
Include these high-growth search terms where relevant:
- AI-powered budgeting
- Financial privacy & data security
- Subscription management
- Receipt tracking & OCR
- Zero-based budgeting
- FIRE (Financial Independence, Retire Early)
- Emergency fund strategies
- Debt avalanche vs. snowball

---

### 4. Who This Book Is For
Expand to multiple audiences:
- **Complete Beginners** - No finance experience required
- **Young Professionals** - Building first budget
- **Families** - Household expense management
- **Small Business Owners** - Separating personal/business finances
- **Privacy-Conscious Users** - Local-first financial tracking

---

### 5. Table of Contents
Grid format for visual appeal and topical depth signals.

---

### 6. Continue Your Learning (Internal Links)
Link to related product pages and future content:
- Link to SenticMoney features
- Link to pricing/download
- Link to support/FAQ

---

### 7. Book Metadata Footer
Add structured metadata block before footer:

```html
<div class="book-metadata">
    <h3>Book Details</h3>
    <ul>
        <li><strong>ISBN-13:</strong> 979-XXXXXXXXXX</li>
        <li><strong>ASIN:</strong> BXXXXXXXXXX</li>
        <li><strong>Pages:</strong> XXX</li>
        <li><strong>Publisher:</strong> [Publisher Name]</li>
        <li><strong>Publication Date:</strong> [Date]</li>
        <li><strong>Language:</strong> English</li>
    </ul>
</div>
```

---

## JSON-LD Schema Requirements

**CRITICAL:** Create separate Book schemas for Paperback and Kindle editions. Use full schema.org URLs for `bookFormat`.

### Book Schema - Paperback Edition
```json
{
    "@context": "https://schema.org",
    "@type": "Book",
    "name": "Book Title: Subtitle",
    "author": {
        "@type": "Person",
        "name": "Author Name",
        "url": "https://senticmoney.com/about.html"
    },
    "datePublished": "2024-XX-XX",
    "publisher": {
        "@type": "Organization",
        "name": "Publisher Name"
    },
    "isbn": "979-XXXXXXXXXX",
    "numberOfPages": XXX,
    "inLanguage": "en",
    "bookFormat": "https://schema.org/Paperback",
    "description": "A comprehensive guide to [topic] for [audience].",
    "genre": ["Personal Finance", "Budgeting", "Money Management"],
    "offers": {
        "@type": "Offer",
        "availability": "https://schema.org/InStock",
        "price": "XX.XX",
        "priceCurrency": "USD",
        "url": "https://www.amazon.com/dp/XXXXXXXXXX",
        "itemCondition": "https://schema.org/NewCondition"
    }
}
```

### Book Schema - Kindle Edition
```json
{
    "@context": "https://schema.org",
    "@type": "Book",
    "name": "Book Title: Subtitle (Kindle Edition)",
    "author": {
        "@type": "Person",
        "name": "Author Name"
    },
    "datePublished": "2024-XX-XX",
    "publisher": {
        "@type": "Organization",
        "name": "Publisher Name"
    },
    "bookFormat": "https://schema.org/EBook",
    "description": "A comprehensive guide to [topic] for [audience].",
    "offers": {
        "@type": "Offer",
        "availability": "https://schema.org/InStock",
        "price": "X.XX",
        "priceCurrency": "USD",
        "url": "https://www.amazon.com/dp/XXXXXXXXXX",
        "itemCondition": "https://schema.org/NewCondition"
    }
}
```

### Key Schema Rules:
- Use `"https://schema.org/Paperback"` or `"https://schema.org/EBook"` (NOT plain text)
- Use `description` (NOT `about`) for the book summary
- Create separate `<script type="application/ld+json">` blocks for each format
- Include `itemCondition` in offers
- ISBN only required for Paperback (Kindle uses ASIN in URL)

---

### FAQ Schema
```json
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "Who is this book for?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "This book is written for [target audiences]."
            }
        },
        {
            "@type": "Question",
            "name": "Do I need [prerequisite]?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "No prior experience is required. [Explanation]."
            }
        }
    ]
}
```

---

## Styling (Match SenticMoney Brand)

```css
:root {
    --primary-color: #10B981;
    --secondary-color: #059669;
    --text-dark: #1F2937;
    --text-light: #6B7280;
}

.answer-capsule {
    background: #f0fdf4;
    border-left: 4px solid var(--primary-color);
    padding: 1.5rem;
    margin: 1.5rem 0 2rem;
    border-radius: 0 8px 8px 0;
}

.answer-capsule p {
    margin: 0;
    color: var(--text-dark);
    font-size: 1.1rem;
    line-height: 1.6;
}

.book-metadata {
    background: #f9fafb;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    padding: 1.5rem;
    margin-top: 2rem;
}

.book-metadata ul {
    list-style: none;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.5rem;
}

.buy-buttons {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    margin: 1.5rem 0;
}

.btn {
    padding: 0.875rem 1.5rem;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.3s;
}

.btn-primary {
    background: #ff9900;
    color: #000;
}

.btn-primary:hover {
    background: #e68a00;
}

.btn-secondary {
    background: white;
    color: var(--text-dark);
    border: 1px solid #e5e7eb;
}

.btn-secondary:hover {
    border-color: var(--primary-color);
    color: var(--primary-color);
}
```

---

## Technical Requirements

### External Links
All external links must include `rel="noopener"`:
```html
<a href="https://amazon.com/..." target="_blank" rel="noopener">
```

### Accessibility
- Skip link: `<a href="#main-content" class="skip-link">Skip to main content</a>`
- Main wrapper: `<main id="main-content">`
- Image alt text with book title

---

## Checklist Before Publishing

- [ ] Answer capsule present (40-60 words)
- [ ] Buy buttons immediately after capsule
- [ ] 2026 entities mentioned in "What You'll Learn"
- [ ] Multiple audience types in "Who This Is For"
- [ ] Book metadata footer with ISBN/pages/publisher
- [ ] Paperback Book JSON-LD schema
- [ ] Kindle Book JSON-LD schema
- [ ] FAQ schema for common questions
- [ ] All external links have `rel="noopener"`
- [ ] Skip link and `<main id="main-content">` present
- [ ] Internal links to product pages

---

## Integration with SenticMoney

When the book relates to personal finance, include:
- Link to SenticMoney download page
- Mention how the software complements the book
- "Try It" CTA for the free edition

---

*Last Updated: January 4, 2026*
*Format Version: 1.0*
