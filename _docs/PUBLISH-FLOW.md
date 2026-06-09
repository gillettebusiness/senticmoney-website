# Publish Flow — Standing Process

This is the durable, reusable procedure for shipping a batch of articles to the live repo.
It is separate from ARTICLE-WRITING-GUIDE.md: that guide covers *how to write* an article;
this covers *how to ship* one. Keep the two concerns in their own files.

Established and proven on the Week 18 batch (May 29, 2026).

---

## The two jobs

Every batch is two distinct jobs. Do not conflate them.

1. **Write + verify** (this chat / the article-authoring session). Capsules, Win Throughout,
   Crown Test, link verification, the full gate. The hard judgment lives here.
2. **Ship** (Claude Code / the CLI). Mechanical execution of the publish ripple — reading
   existing files, matching patterns, appending entries, updating trackers, commit, verify.
   No new judgment; the thinking already happened in job 1.

## The paste-avoidance pattern (the core lesson)

The CLI is finicky about long multi-line pastes (bracketed-paste quirks, premature newline
execution, em-dash/smart-quote re-encoding). Do NOT paste the ripple instructions or the
literal content blocks into the terminal.

Instead, for every batch:

1. The authoring session produces a single self-contained instruction file:
   `PUBLISH-<batch>.md` (e.g. PUBLISH-WEEK18.md). It contains the full ripple, every literal
   content block (llms entries, card data, commit message), and all constraints — written
   exactly as they should land.
2. Drop that file into the repo root (`C:\dev\senticmoney-website\`) alongside the new
   article files in /blog. File drops are not subject to paste mangling.
3. Kick off the CLI with ONE short, plain-ASCII line:
   `Read PUBLISH-<batch>.md in the repo root and execute it. One step at a time, confirm
   with me before each next step, show the diff after each edit.`
4. The instruction file tells the CLI not to commit itself. Delete or exclude it before the
   final commit.

Why it works: the literal content sits on disk and is *read*, not *pasted*, so encoding and
line endings survive intact, and the human's only paste is one trivial line.

## One task at a time — non-negotiable

Batching ripple steps has historically caused skipped checklist steps and misdirected file
ops. The instruction file enforces step-by-step execution with confirmation between steps and
a diff after each edit. Keep that discipline regardless of which model runs it.

## Model

Run the ripple on **Sonnet 4.6** (`claude --model sonnet`, or `/model sonnet`; explicit string
`claude-sonnet-4-6`). It is the documented daily driver for mechanical execution and ~40%
cheaper on tokens than Opus. Escalate a single step to Opus only if it turns into real
judgment (an unexpected reference to repoint, genuinely ambiguous markup to match), then drop
back to Sonnet.

## Start-of-session inventory reconciliation

Before planning or writing, reconcile inventory across ALL count-bearing files AND the live
site — they drift independently. In the Week 18 session the count disagreed file-to-file:
marketing CLAUDE.md said 64, ARTICLE-STATUS.txt said 67, and live was 67. No single file is
authoritative on its own. Fast check: union the homepage blog-card slugs with the llms.txt
slugs, diff against ARTICLE-STATUS.txt, and cross-check the count in marketing CLAUDE.md.
Reconcile any gap as part of the next publish. The lesson is not "the tracker lags reality"
— it is "every count-bearing file can sit at a different number, so verify against disk."

## The 12-step ripple (template)

Each `PUBLISH-<batch>.md` instantiates these steps with the batch's specifics:

1. Verify new files — ends in `</html>`, dates match in meta + JSON-LD, canonical matches slug,
   and run `npx html-validate blog/[slug].html` (the validation step the repo per-publish
   checklists also require — keep this template and those checklists in agreement).
2. blog/index.html — read an existing card, replicate per new article (bare slugs, no target=_blank).
3. author/frank-d-campbell.html — add new articles, newest first, matching existing format.
4. sitemap.xml — add <url> entries, bare slugs, lastmod = each article's date.
5. llms.txt — add blog entries in correct topical sections (.html suffix, preserve CRLF).
6. (one-time / as needed) retire or reconcile auxiliary files safely — grep for references
   before any deletion; never blind-delete.
7. ARTICLE-STATUS.txt — add new + any reconcile slugs; update total.
8. INDEXING-TRACKER.md — add new URLs to Pending Indexing (Submitted date left blank).
9. CONTENT-CALENDAR.md — mark the batch complete.
10. marketing_CLAUDE.md — update state (count, notable decisions).
11. Commit + push to main (confirm the instruction file is not staged).
12. Verify live after Render deploy — poll with cache-buster, cap at 3 minutes, then escalate
    to the dashboard (see "Deploy verification" below). Checks per URL:
    `curl -sL -o /dev/null -w "%{http_code}" -A "Mozilla/5.0" https://senticmoney.com/blog/<slug>`
    and `curl -sL ... | tail -c 20` (expect `</html>`).

## Deploy verification (lessons from 2026-06-09)

- **Poll the origin with a cache-buster, and cap the wait.**
  `curl -s "https://senticmoney-website.onrender.com/<path>?cb=$(date +%s)"`
  Render serves static sites through its own CDN, so un-busted polls can return stale
  content even after a successful deploy. If the origin still serves old content after
  ~3 minutes of polling, stop polling and check the Render dashboard (Events tab).
  Manual Deploy → Deploy latest commit is the fallback. Render deploys normally take
  1-3 minutes but have been observed taking 30+.
- **Cloudflare purge is usually unnecessary.** Site files are served with `s-maxage=300`,
  so the edge refreshes itself within 5 minutes. For non-urgent changes, wait out the
  TTL instead of purging.
- **The CLI has no Render or Cloudflare credentials.** It can push to GitHub and poll
  URLs, nothing more. Forcing a deploy or a purge is a manual dashboard action unless
  the operator later creates a Render Deploy Hook and/or Cloudflare API token (operator
  decision; secrets must live outside the repos).
- **Wording for future runbooks:** deploy-verification steps should say "poll with
  cache-buster, cap at 3 minutes, then escalate to the dashboard" rather than
  open-ended polling.

## Standing constraints (carry into every PUBLISH-<batch>.md)

- **Two URL conventions, never mixed:** llms.txt uses `.html` suffixes; blog cards, sitemap,
  and internal article links use BARE slugs with no `.html` and no `target="_blank"`.
- **llms.txt is CRLF.** Preserve line endings on any edit.
- **Single llms file.** llms-full.txt was retired on May 29, 2026; maintain only llms.txt.
  (Use this exact date wherever the retirement is referenced — marketing CLAUDE.md and any
  checklist must read "May 29, 2026", not a vaguer "May 2026", so the docs do not disagree.)
- Pricing always `$39/year`. No old branding (CognitoMoney/CognitoFi/cognitofi). Never cite
  mint.intuit.com.
- Date-staggering for multi-article batches is set at draft time (most evergreen earliest,
  weekdays only) — a writing-side rule, applied before files reach the CLI.

## Keep follow-ups out of the publish commit

Content corrections and optional enhancements (e.g. competitor-fact updates, reciprocal
cross-links) ship as their own commits, never folded into the publish ripple. The instruction
file lists them under a "NOT part of this commit" heading so the CLI doesn't absorb them.
