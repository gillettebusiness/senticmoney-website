# Website Pages Audit for v2.5.6

**Repo:** `C:\dev\senticmoney-website`
**Target files:** `download.html`, `features.html`, `update.html`
**Scope:** Read-only audit. Identifies what Step 4 of the Version Bump Ripple will need to change. No source edits made.
**Audit date:** 2026-04-16
**Context:** Windows installer swap committed locally (`1806fb6`) but not pushed. Mac DMG not yet landed — no `github-actions[bot]` commits observed during audit. Recent commits:

```
1806fb6 Ship Windows installer v2.5.6
ac1a7b9 docs: add llms-full.txt step to publishing checklist
b30fcd9 Add Week 15 articles to llms.txt and llms-full.txt
```

---

## 1. download.html

### Version strings

| Line | Context | Current value |
|------|---------|---------------|
| 657 | JSON-LD SoftwareApplication schema | `"softwareVersion": "2.5.5"` |
| 658 | JSON-LD `fileSize` | `"fileSize": "~100MB"` |
| 758 | Windows panel version badge | `<span>Version 2.5.5</span>` |
| 775 | Mac panel version badge | `<span>Version 2.5.5</span>` |
| 1066 | JS innerHTML — post-click Mac panel | `Version 2.5.5` |
| 1070 | JS innerHTML — `trackDownload('mac', '2.5.5')` | `'2.5.5'` |

### Download-filename references

| Line | Context | Current filename |
|------|---------|------------------|
| 753 | Windows download anchor `href` + `trackDownload('windows', '2.5.5')` | `SenticMoney-Setup-v2.5.5.exe` |
| 770 | Mac download anchor `href` + `trackDownload('mac', '2.5.5')` | `SenticMoney-v2.5.5-mac.dmg` |
| 844 | Windows help text `<code>` | `SenticMoney-Setup-v2.5.5.exe` |
| 881 | Mac help text `<code>` | `SenticMoney-v2.5.5-mac.dmg` |
| 1005 | JS constant `MAC_DMG_URL` | `https://senticmoney.com/senticmoney-download/SenticMoney-v2.5.5-mac.dmg` |

All links point into `/senticmoney-download/`. No broken `/resources/*.pdf` references seen on this page.

### "Latest version" / "What's new" / banner sections

No dedicated "What's new" banner on download.html — version reveals only through panel badges (L758, L775), help-text filename callouts, and JSON-LD. Release-notes copy lives on `update.html`.

### Hardcoded dates / download counts / file sizes

- L658 `fileSize: "~100MB"` — approximate, likely drift. Current installer on disk is `~110MB` (actual `SenticMoney-Setup-v2.5.6.exe` is 115,737,844 bytes ≈ 110 MB).
- No hardcoded release date on this page.
- No download counters rendered.

### System requirements

Windows: Windows 10 or later (64-bit). Mac: macOS 12+ (Monterey). No changes needed — v2.5.6 did not change platform floors.

---

## 2. features.html

### Version strings

None found. Page is version-agnostic — nothing to bump.

### Download-filename references

None. Page does not link installers directly.

### Section headings (outline)

```
H2 L673  SenticMoney Genie — Your AI Financial Advisor
H2 L698  Smart Budgeting That Adapts to Your Life
H2 L716  Your Financial Health at a Glance
H2 L734  Never Miss a Bill Again
H2 L752  Transaction Management Made Simple
H2 L775  Goals That Keep You Motivated
H2 L792  AI-Powered Document Processing
H2 L814  Runway — See How Long Your Money Lasts
H2 L835  Multi-Device & Accessibility
```

### v2.5.6 feature coverage check

| Feature | Covered on features.html? | Notes |
|---------|---------------------------|-------|
| PWA mobile capture (v2.5 original) | Yes — L901-906 Mobile Receipt Capture card | Describes "queued on phone until home WiFi" — accurate for v2.5, out of date for v2.5.6 |
| Away-from-home capture (v2.5.6) | No | Card still implies phone queues locally; proxy-relay path is not mentioned |
| Sync Mobile button | No | Not surfaced anywhere on features.html |
| Needs Review highlighting | No | No mention of the Receipts & Bills inbox / Needs Review workflow |
| Split badge on Dashboard | No | Not mentioned |
| Genie YTD awareness | No | Genie section (L673) does not call out YTD context |

**Location to patch:** L901-906 "Mobile Receipt Capture" card is the natural anchor for a v2.5.6 refresh — rewrite to cover cellular/proxy capture, Sync Mobile button, and Needs Review inbox. Other v2.5.6 items (Split badge, Genie YTD) are minor polish and can stay in update.html release notes only.

### AI model references

- L793: `Gemini 3.1 Pro or 3.1 Flash-Lite` — correct. Matches current model stack.

---

## 3. update.html

### Version strings

| Line | Context | Current value |
|------|---------|---------------|
| 594 | Current release header | `v2.5.5 — April 2026` |
| 597 | Inside v2.5.5 "Changed" list | `Gemini 2.5 Flash to Gemini 3.1 Flash-Lite` — **historical fact, leave alone** |

### Page structure

Living changelog. Each release entry is wrapped in:

```html
<div style="padding: 1rem 0; border-bottom: 1px solid #f3f4f6;">
  <h? ...>vX.Y.Z — Month Year</h?>
  <p><strong>Changed</strong></p>
  <ul>...</ul>
  <p><strong>Fixed</strong></p>
  <ul>...</ul>
</div>
```

Entries are ordered newest-first. v2.5.5 currently holds the top slot.

### Version numbering

Hardcoded. Every release is its own `<div>` block with inline version + month. No templating, no data source.

### Last-updated timestamp

None rendered on the page.

### Insert location for v2.5.6

New block goes **above** L594 (above the v2.5.5 entry). v2.5.5 stays untouched as historical context.

---

## 4. Cross-cutting stale-content scan

Scanned all three files:

| Pattern | download.html | features.html | update.html | Verdict |
|---------|---------------|---------------|-------------|---------|
| `ecommsolutions@gmail.com` | 0 | 0 | 0 | Clean — all user-visible copy already uses `support@senticmoney.com` |
| `Cognito` / `cognitofi` | 0 | 0 | 0 | Clean |
| `Gemini 2.5 Flash` | 0 | 0 | 1 (L597, historical) | Leave — historical context inside a prior release note |
| Broken `/resources/*.pdf` links | none spotted | none spotted | none spotted | Clean |
| `/senticmoney-download/*` links | all present | none | none | All point at filenames listed above |

No cross-cutting cleanup needed — v2.5.6 work is purely version/filename bumps on download.html, a feature-card refresh on features.html, and a new release block on update.html.

---

## Mac DMG landing status

No `github-actions[bot]` commits present during this audit run. Mac build workflow is `workflow_dispatch`-only — push does not trigger it, so DMG won't land until the workflow is manually dispatched with `deploy_to_website=true`.

---

## Proposed edits for v2.5.6

Dennis to review and approve before any file is modified.

```
download.html:L657 — "softwareVersion": "2.5.5" → "2.5.6"
download.html:L658 — "fileSize": "~100MB" → "~110MB"
download.html:L753 — Windows download href: SenticMoney-Setup-v2.5.5.exe → SenticMoney-Setup-v2.5.6.exe; trackDownload('windows','2.5.5') → '2.5.6'
download.html:L758 — Windows panel badge: Version 2.5.5 → Version 2.5.6
download.html:L770 — Mac download href: SenticMoney-v2.5.5-mac.dmg → SenticMoney-v2.5.6-mac.dmg; trackDownload('mac','2.5.5') → '2.5.6'
download.html:L775 — Mac panel badge: Version 2.5.5 → Version 2.5.6
download.html:L844 — Help-text <code> filename: SenticMoney-Setup-v2.5.5.exe → SenticMoney-Setup-v2.5.6.exe
download.html:L881 — Help-text <code> filename: SenticMoney-v2.5.5-mac.dmg → SenticMoney-v2.5.6-mac.dmg
download.html:L1005 — MAC_DMG_URL: SenticMoney-v2.5.5-mac.dmg → SenticMoney-v2.5.6-mac.dmg
download.html:L1066 — JS innerHTML Mac panel text: Version 2.5.5 → Version 2.5.6
download.html:L1070 — JS innerHTML trackDownload('mac','2.5.5') → '2.5.6'
features.html:L901-906 — Rewrite Mobile Receipt Capture card: add v2.5.6 away-from-home capture (cellular + proxy relay), Sync Mobile button, Needs Review inbox workflow
update.html:L594 — Insert new v2.5.6 — April 2026 release block ABOVE existing v2.5.5 entry; DO NOT modify v2.5.5 entry
```

### Suggested v2.5.6 release-notes content for update.html

For reference when drafting the new block (not an edit instruction — Dennis picks final wording):

- **Changed** — Mobile receipt capture now works from anywhere: snap a receipt on cellular or any WiFi, it relays through the secure proxy and lands in your Receipts & Bills inbox on next app launch. New Sync Mobile button pulls pending captures on demand. Needs Review highlighting surfaces items waiting for categorization. Dashboard recent-transactions now shows a "Split" badge for multi-category items. Genie now considers year-to-date category spending when answering budget questions.
- **Fixed** — Category search now includes transactions whose split allocations match, with the correct split amount (was showing full transaction amount). About page version string (was rendering blank). Purchase-receipt emails now show `support@senticmoney.com` as the support address. Consolidated duplicate Receipts help page.

---

## Time spent

Within the 5-10 minute budget. No unexpected complexity — all three files are plain HTML with no templating, auto-generation, or build step.
