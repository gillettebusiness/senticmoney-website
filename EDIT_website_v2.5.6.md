# Website Page Edits for v2.5.6

**Run from:** `C:\dev\senticmoney-website`
**Prereqs confirmed:**
- Pull-rebase complete — local ahead of origin by 1 commit (`edb412a Ship Windows installer v2.5.6`)
- Both artifacts present: `SenticMoney-Setup-v2.5.6.exe` and `SenticMoney-v2.5.6-mac.dmg`
- Uncommitted PDF (`resources/senticmoney-quick-start.pdf`) in working tree, ready to stage
- Untracked `week15_v33_capsule_rewrite.py` is intentional, leave alone
- Audit complete: `tasks/audit_v2.5.6_website.md`

Execute the 13 edits approved from the audit, stage the full v2.5.6 website bundle, commit, and push. Result: one Render deploy takes v2.5.6 fully live end-to-end.

---

## Edit 1 — download.html (11 line edits)

Apply each of these. Line numbers are from the audit — verify each by reading the file around the line first; if content has drifted, grep for the pattern instead.

```
L657 — "softwareVersion": "2.5.5"  →  "softwareVersion": "2.5.6"
L658 — "fileSize": "~100MB"  →  "fileSize": "~110MB"
L753 — Windows download anchor:
       href="...SenticMoney-Setup-v2.5.5.exe"  →  "...SenticMoney-Setup-v2.5.6.exe"
       AND trackDownload('windows', '2.5.5')  →  trackDownload('windows', '2.5.6')
L758 — <span>Version 2.5.5</span>  →  <span>Version 2.5.6</span>
L770 — Mac download anchor:
       href="...SenticMoney-v2.5.5-mac.dmg"  →  "...SenticMoney-v2.5.6-mac.dmg"
       AND trackDownload('mac', '2.5.5')  →  trackDownload('mac', '2.5.6')
L775 — <span>Version 2.5.5</span>  →  <span>Version 2.5.6</span>
L844 — <code>SenticMoney-Setup-v2.5.5.exe</code>  →  <code>SenticMoney-Setup-v2.5.6.exe</code>
L881 — <code>SenticMoney-v2.5.5-mac.dmg</code>  →  <code>SenticMoney-v2.5.6-mac.dmg</code>
L1005 — const MAC_DMG_URL: replace "SenticMoney-v2.5.5-mac.dmg" with "SenticMoney-v2.5.6-mac.dmg"
L1066 — JS innerHTML text: "Version 2.5.5"  →  "Version 2.5.6"
L1070 — trackDownload('mac', '2.5.5')  →  trackDownload('mac', '2.5.6')
```

After all download.html edits, verify:

```powershell
findstr /n "2.5.5" download.html
```

Expected: zero hits. If any remain, report them and stop before moving on.

## Edit 2 — features.html Mobile Receipt Capture card (L901-906)

First read lines 895-915 of the current file to see the exact HTML structure (icons, div classes, header pattern, list vs paragraph style) used by the Mobile Receipt Capture card and the cards around it.

Replace the body of the Mobile Receipt Capture card with the following content, **preserving the card's outer HTML structure (div class, icon, header tag, etc.) exactly as found**:

> **Mobile Receipt Capture**
>
> Snap a receipt on your phone — SenticMoney extracts the amount, date, and category and drops it in your Receipts & Bills inbox. Works on home WiFi and away from home: when you're on cellular or an unfamiliar network, captures queue securely on our relay and sync the next time you open the app. Tap Sync Mobile to pull pending captures on demand. Yellow highlighting on the inbox shows which items still need your review.

Adapt paragraph structure to match the surrounding cards. If other cards use a single `<p>`, use a single `<p>`. If they use a headline + sub-paragraph structure, split accordingly. Preserve whatever icon/emoji/SVG sits at the top of the card.

After editing, report the actual final HTML of the card so Dennis can verify.

## Edit 3 — update.html new v2.5.6 release block

Insert a new block ABOVE line 594 (above the existing v2.5.5 entry). DO NOT modify the v2.5.5 entry.

Read lines 590-600 of the current file to see the exact wrapper div style, heading level (h2/h3/h4), and structural pattern used by the v2.5.5 block. Match the new v2.5.6 block to that pattern.

Content to insert:

```html
<div style="padding: 1rem 0; border-bottom: 1px solid #f3f4f6;">
  <h?>v2.5.6 — April 2026</h?>
  <p><strong>Changed</strong></p>
  <ul>
    <li>Mobile receipt capture now works from anywhere — cellular, unfamiliar WiFi, any connection. Captures queue on the secure relay and sync to your inbox next time you open SenticMoney.</li>
    <li>New "Sync Mobile" button on the Receipts &amp; Bills page pulls any pending captures on demand.</li>
    <li>Receipts awaiting your review now show with a yellow highlight in the inbox.</li>
    <li>Dashboard transaction list shows a "Split" badge for transactions divided across multiple categories.</li>
    <li>The Genie now factors year-to-date spending by category into its answers about budgets and habits.</li>
  </ul>
  <p><strong>Fixed</strong></p>
  <ul>
    <li>Category searches now include transactions where a split allocation matches — and show the correct split amount, not the full transaction total.</li>
    <li>About page version number now displays correctly (was rendering blank).</li>
    <li>Purchase confirmation emails now show the correct support address (support@senticmoney.com).</li>
    <li>Consolidated duplicate Receipts help page into a single comprehensive guide.</li>
  </ul>
</div>
```

Replace `<h?>` / `</h?>` with whatever heading level the v2.5.5 block uses (check the source). Match inline styles on the wrapper div exactly if they differ from what's shown.

Adjust the outer div's inline style to match the v2.5.5 block's wrapper exactly — the border-bottom color, padding, anything else.

## Edit 4 — Sanity check before staging

```powershell
cd C:\dev\senticmoney-website

:: No stale v2.5.5 references remaining in download.html
findstr /c:"2.5.5" download.html

:: v2.5.6 references in expected places
findstr /c:"2.5.6" download.html
findstr /c:"v2.5.6" update.html

:: Mobile Receipt Capture card reflects v2.5.6 reality
findstr /c:"away from home" features.html

:: No accidental edits in update.html v2.5.5 block
findstr /c:"v2.5.5" update.html
```

Expected:
- `2.5.5` in download.html: zero hits
- `2.5.6` in download.html: many hits
- `v2.5.6` in update.html: at least one hit (the new block heading)
- `away from home` in features.html: at least one hit
- `v2.5.5` in update.html: still present (historical entry intact)

If any check fails, stop and report.

## Edit 5 — Stage the full v2.5.6 website bundle

Selective staging — do NOT run `git add -A` because of the untracked `week15_v33_capsule_rewrite.py`.

```powershell
git add download.html
git add features.html
git add update.html
git add resources\senticmoney-quick-start.pdf
git status
```

Expected staged:
- `modified:   download.html`
- `modified:   features.html`
- `modified:   update.html`
- `modified:   resources/senticmoney-quick-start.pdf`

Expected NOT staged:
- `week15_v33_capsule_rewrite.py` (untracked, intentional — Dennis knows)
- Any `tasks/audit_v2.5.6_*.md` files (these are internal audit artifacts — leave untracked OR commit to a separate commit, Dennis's call; default is leave untracked for this commit)

Before proceeding, if the `tasks/` audit files are untracked and Dennis would prefer them committed alongside, ask. Otherwise proceed.

If any unexpected file is staged, unstage it:
```powershell
git restore --staged <file>
```

Paste `git status` output for Dennis to confirm.

## Edit 6 — Commit

```powershell
git commit -m "Update website for v2.5.6 release" -m "- download.html: version bumps (11 edits) + filename swaps + file size refresh (~100MB -> ~110MB)" -m "- features.html: Mobile Receipt Capture card refreshed with v2.5.6 away-from-home, Sync Mobile, Needs Review coverage" -m "- update.html: new v2.5.6 release-notes block above v2.5.5 (historical v2.5.5 block preserved)" -m "- resources/senticmoney-quick-start.pdf: refreshed PDF (v2.5.6 content, regenerated earlier this release)" -m "Companions: installer swap (commit edb412a, already local) ships together. Mac DMG landed via workflow auto-commit (41c52f7)."
```

## Edit 7 — Verify the commit

```powershell
git log -1 --stat
git log --oneline -5
git log --oneline origin/main..HEAD
```

Expected:
- New commit at HEAD with 4 files changed
- Two commits ahead of origin (the installer swap and the page-edits commit)

## Edit 8 — Push

```powershell
git push origin main
```

This triggers Render auto-deploy. v2.5.6 goes fully live on senticmoney.com once Render finishes (~2-5 minutes after push).

Report push result and the Render deploy URL if git output includes it.

## Edit 9 — Final report to Dennis

Report:
- SHAs of both commits pushed (installer swap + page edits)
- Confirmation that `dir senticmoney-download\*.exe` and `dir senticmoney-download\*.dmg` show only v2.5.6 artifacts
- Confirmation that `findstr /c:"2.5.5" download.html` returns zero hits
- Current state of working tree (should still show the untracked `week15_v33_capsule_rewrite.py` and any untracked tasks/audit files)
- Next ripple step: Step 5 — proxy version bump (different repo: `senticmoney-proxy`)

---

## If anything goes sideways

- **Line numbers don't match content** → the audit was against a snapshot; if files shifted, grep for the string pattern and report before editing blind
- **features.html card structure is complex (custom components, JS rendering)** → stop and show Dennis the current HTML, he'll direct
- **update.html heading level is different from expected or has schema markup** → stop and show, he'll direct
- **Push rejected (divergence with origin)** → don't force, pull-rebase and retry; the only scenario that would cause this is if another Mac build fired during the edit window — unlikely
- **Anything else unexpected** → stop, report, wait
