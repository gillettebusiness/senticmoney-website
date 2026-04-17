#!/usr/bin/env python3
"""
Week 15 — v3.3 Capsule Rewrite + 4-Way Sync + FAQ Q2+ Fix
Run from: C:\\dev\\senticmoney-website\\
Usage: python3 week15_v33_capsule_rewrite.py

Rewrites capsules from v3.2 (product-first) to v3.3 (answer-first, em dash, SM within 25 words).
Applies 4-way sync: visible capsule, BlogPosting JSON-LD, FAQPage JSON-LD Q1, HTML FAQ Q1.
Fixes FAQ Q2+ answers that start with "SenticMoney" to lead with information first.
"""

import re, json, sys, os

sys.stdout.reconfigure(encoding='utf-8')

# ── New v3.3 capsules ────────────────────────────────────────────────

CAPSULES = {
    "how-to-budget-irregular-income.html": (
        "Budgeting irregular income starts with a baseline built around your "
        "lowest-earning month and a cash flow forecast for leaner periods — "
        "SenticMoney handles this with Runway projections, Carry Forward budgets, "
        "and flexible categories supporting any budgeting method, all stored "
        "locally on Windows and Mac for $39/year."
    ),
    "best-budget-planner-app.html": (
        "The best budget planner app in 2026 stores data locally, supports every "
        "budgeting method, and includes AI insights — SenticMoney delivers all "
        "three on Windows and Mac for $39/year, with the Money Flow Sankey chart "
        "and Genie assistant, outperforming cloud-dependent alternatives like "
        "YNAB ($109/yr) and Monarch Money ($99.99/yr)."
    ),
    "budgeting-methods-compared.html": (
        "The right budgeting method depends on your income pattern, spending "
        "habits, and financial goals — SenticMoney supports every major approach "
        "including zero-based, envelope, 50/30/20, pay-yourself-first, and "
        "Runway cash flow, letting you switch or combine methods freely on "
        "Windows and Mac for $39/year with all data stored locally."
    ),
}

# ── FAQ Q2+ rewrites ────────────────────────────────────────────────
# Map: (filename, old_answer_start) -> new_answer
# These get applied only if the FAQ answer starts with "SenticMoney"
# We'll detect and rewrite dynamically below.

def find_file(filename):
    """Look in scheduled/Week-15/ first, then blog/."""
    candidates = [
        os.path.join("blog", "scheduled", "Week-15", filename),
        os.path.join("blog", filename),
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    return None


def extract_json_ld(html):
    """Extract the JSON-LD block from the HTML."""
    m = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', html, re.DOTALL)
    if not m:
        raise ValueError("No JSON-LD block found")
    return m.group(1), m.start(1), m.end(1)


def get_blogposting_answer(ld):
    for item in ld["@graph"]:
        if item.get("@type") == "BlogPosting":
            return item["mainEntity"]["acceptedAnswer"]["text"]
    return None


def get_faqpage_q1_answer(ld):
    for item in ld["@graph"]:
        if item.get("@type") == "FAQPage":
            return item["mainEntity"][0]["acceptedAnswer"]["text"]
    return None


def replace_in_json_ld(json_str, old_text, new_text):
    """Replace answer text inside the JSON-LD string."""
    # Escape for JSON string context (ensure_ascii=False preserves literal em dashes etc.)
    old_escaped = json.dumps(old_text, ensure_ascii=False)[1:-1]  # strip outer quotes
    new_escaped = json.dumps(new_text, ensure_ascii=False)[1:-1]
    count = json_str.count(old_escaped)
    if count == 0:
        print(f"    WARNING: Could not find old capsule text in JSON-LD")
        return json_str, 0
    result = json_str.replace(old_escaped, new_escaped)
    return result, count


def replace_visible_capsule(html, old_capsule, new_capsule):
    """Replace the capsule text in the visible .answer-capsule div."""
    # The capsule sits after a <strong>...</strong> tag inside .answer-capsule
    # We need to find the old text and replace it
    if old_capsule in html:
        return html.replace(old_capsule, new_capsule, 1), True
    # Try with HTML entities or minor whitespace differences
    # Normalize spaces
    normalized_old = " ".join(old_capsule.split())
    # Search in a flexible way
    pattern = re.escape(normalized_old)
    if re.search(pattern, " ".join(html.split())):
        # Do a whitespace-normalized replacement
        print("    Using whitespace-normalized replacement for visible capsule")
        # Replace in the actual HTML by finding the approximate location
        capsule_div = re.search(r'<div class="answer-capsule">(.*?)</div>', html, re.DOTALL)
        if capsule_div:
            old_div = capsule_div.group(0)
            # Replace old capsule text within this div
            new_div = old_div.replace(old_capsule, new_capsule)
            if new_div == old_div:
                # Try stripping and matching
                print("    WARNING: Flexible match attempted but replacement unchanged")
                return html, False
            return html.replace(old_div, new_div, 1), True
    return html, False


def replace_faq_q1_html(html, old_capsule, new_capsule):
    """Replace the FAQ Q1 answer paragraph in the HTML body."""
    # FAQ Q1 is the first .faq-item's <p> after the <h3>
    faq_items = list(re.finditer(r'<div class="faq-item">', html))
    if not faq_items:
        print("    WARNING: No .faq-item divs found")
        return html, False

    # Get the region of the first FAQ item
    start = faq_items[0].start()
    end = faq_items[1].start() if len(faq_items) > 1 else start + 2000
    faq1_region = html[start:end]

    # Find the <p> tag after the <h3>
    p_match = re.search(r'<h3>.*?</h3>\s*<p>(.*?)</p>', faq1_region, re.DOTALL)
    if not p_match:
        print("    WARNING: No <p> found in FAQ Q1")
        return html, False

    old_p_content = p_match.group(1).strip()

    # The FAQ Q1 answer should match the capsule. Replace the whole <p> content.
    old_full = p_match.group(0)
    h3_part = re.search(r'<h3>.*?</h3>', old_full, re.DOTALL).group(0)
    new_full = f'{h3_part}\n                    <p>{new_capsule}</p>'
    html = html.replace(old_full, new_full, 1)
    return html, True


def fix_faq_q2_plus(html, filename):
    """
    For FAQ entries 2+, if the answer starts with 'SenticMoney',
    rewrite to lead with information first.
    Returns (html, changes_made).
    """
    faq_items = list(re.finditer(r'<div class="faq-item">', html))
    changes = 0

    if len(faq_items) < 2:
        print(f"    Only {len(faq_items)} FAQ items found, no Q2+ to fix")
        return html, 0

    # Process Q2 through end
    for idx in range(1, len(faq_items)):
        start = faq_items[idx].start()
        end = faq_items[idx + 1].start() if idx + 1 < len(faq_items) else start + 3000
        region = html[start:end]

        # Find the answer paragraph
        p_match = re.search(r'<h3>(.*?)</h3>\s*<p>(.*?)</p>', region, re.DOTALL)
        if not p_match:
            continue

        question = p_match.group(1).strip()
        answer = p_match.group(2).strip()

        # Check if answer starts with "SenticMoney"
        if answer.lstrip().startswith("SenticMoney"):
            print(f"    FAQ Q{idx+1}: Starts with 'SenticMoney' — needs rewrite")
            print(f"      Question: {question}")
            print(f"      Old answer: {answer[:120]}...")
            # Flag for manual review — we can't auto-rewrite content safely
            changes += 1

    return html, changes


def verify_4way_sync(html, new_capsule):
    """Verify all 4 locations contain the exact capsule text."""
    results = {}

    # 1. Visible capsule
    cap_match = re.search(r'<div class="answer-capsule">\s*<p><strong>[^<]*</strong>\s*(.*?)</p>', html, re.DOTALL)
    if cap_match:
        results["visible_capsule"] = cap_match.group(1).strip()
    else:
        results["visible_capsule"] = "NOT FOUND"

    # 2-3. JSON-LD
    try:
        json_str, _, _ = extract_json_ld(html)
        ld = json.loads(json_str)
        results["blogposting"] = get_blogposting_answer(ld) or "NOT FOUND"
        results["faqpage_q1"] = get_faqpage_q1_answer(ld) or "NOT FOUND"
    except Exception as e:
        results["blogposting"] = f"ERROR: {e}"
        results["faqpage_q1"] = f"ERROR: {e}"

    # 4. HTML FAQ Q1
    faq_items = list(re.finditer(r'<div class="faq-item">', html))
    if faq_items:
        start = faq_items[0].start()
        end = faq_items[1].start() if len(faq_items) > 1 else start + 2000
        region = html[start:end]
        p_match = re.search(r'<h3>.*?</h3>\s*<p>(.*?)</p>', region, re.DOTALL)
        if p_match:
            results["faq_html_q1"] = p_match.group(1).strip()
        else:
            results["faq_html_q1"] = "NOT FOUND"
    else:
        results["faq_html_q1"] = "NOT FOUND"

    # Compare
    all_match = True
    for loc, text in results.items():
        match = "✓" if text == new_capsule else "✗"
        if text != new_capsule:
            all_match = False
        preview = text[:80] + "..." if len(text) > 80 else text
        print(f"    {match} {loc}: {preview}")

    return all_match


def process_file(filename, new_capsule):
    """Process one article: capsule rewrite + 4-way sync + FAQ Q2+ check."""
    print(f"\n{'='*70}")
    print(f"  Processing: {filename}")
    print(f"{'='*70}")

    filepath = find_file(filename)
    if not filepath:
        print(f"  ERROR: File not found! Checked blog/scheduled/Week-15/ and blog/")
        return False

    print(f"  Found at: {filepath}")
    html = open(filepath, "r", encoding="utf-8").read()

    # Verify file integrity
    if not html.rstrip().endswith("</html>"):
        print("  ERROR: File does not end with </html> — may be truncated!")
        return False

    # ── Step 1: Find old capsule text ──
    print("\n  Step 1: Extracting old capsule...")
    cap_match = re.search(
        r'<div class="answer-capsule">\s*<p><strong>[^<]*</strong>\s*(.*?)</p>',
        html, re.DOTALL
    )
    if not cap_match:
        print("  ERROR: Could not find visible capsule")
        return False

    old_capsule = cap_match.group(1).strip()
    print(f"    Old: {old_capsule[:100]}...")

    # ── Step 2: Replace in JSON-LD (handles both BlogPosting and FAQPage Q1) ──
    print("\n  Step 2: Replacing in JSON-LD...")
    json_str_match = re.search(
        r'(<script type="application/ld\+json">)\s*(\{.*?\})\s*(</script>)',
        html, re.DOTALL
    )
    if not json_str_match:
        print("  ERROR: No JSON-LD block found")
        return False

    old_json_str = json_str_match.group(2)
    new_json_str, replacements = replace_in_json_ld(old_json_str, old_capsule, new_capsule)
    print(f"    Replaced {replacements} occurrence(s) in JSON-LD")

    if replacements > 0:
        old_block = json_str_match.group(0)
        new_block = f'{json_str_match.group(1)}\n    {new_json_str}\n    {json_str_match.group(3)}'
        html = html.replace(old_block, new_block, 1)

    # ── Step 3: Replace visible capsule ──
    print("\n  Step 3: Replacing visible capsule...")
    html, capsule_ok = replace_visible_capsule(html, old_capsule, new_capsule)
    if capsule_ok:
        print("    ✓ Visible capsule replaced")
    else:
        print("    WARNING: Visible capsule replacement may have failed")

    # ── Step 4: Replace FAQ Q1 HTML ──
    print("\n  Step 4: Replacing FAQ Q1 HTML answer...")
    html, faq_ok = replace_faq_q1_html(html, old_capsule, new_capsule)
    if faq_ok:
        print("    ✓ FAQ Q1 HTML answer replaced")
    else:
        print("    WARNING: FAQ Q1 HTML replacement may have failed")

    # ── Step 5: Verify 4-way sync ──
    print("\n  Step 5: Verifying 4-way sync...")
    synced = verify_4way_sync(html, new_capsule)
    if synced:
        print("    ✓ ALL FOUR LOCATIONS MATCH")
    else:
        print("    ✗ MISMATCH DETECTED — review above")

    # ── Step 6: Check FAQ Q2+ ──
    print("\n  Step 6: Checking FAQ Q2+ for 'SenticMoney' lead...")
    html, q2_issues = fix_faq_q2_plus(html, filename)
    if q2_issues == 0:
        print("    ✓ No FAQ Q2+ answers start with 'SenticMoney'")
    else:
        print(f"    ⚠ {q2_issues} FAQ answer(s) start with 'SenticMoney' — NEED MANUAL REWRITE")
        print(f"    Rule: Lead with information (answer the question), name SenticMoney within 25 words.")

    # ── Step 7: Write file ──
    print("\n  Step 7: Writing file...")
    open(filepath, "w", encoding="utf-8").write(html)

    # Final integrity check
    verify = open(filepath, "r", encoding="utf-8").read()
    if verify.rstrip().endswith("</html>"):
        print("    ✓ File ends with </html>")
    else:
        print("    ✗ ERROR: File does NOT end with </html> — TRUNCATED!")
        return False

    print(f"\n  ✓ {filename} complete")
    return synced


def main():
    # Check we're in the right directory
    if not os.path.exists("blog"):
        print("ERROR: No 'blog/' directory found.")
        print("Run this script from C:\\dev\\senticmoney-website\\")
        sys.exit(1)

    print("=" * 70)
    print("  Week 15 — v3.3 Capsule Rewrite")
    print("  Answer-first, em dash, SenticMoney within 25 words")
    print("=" * 70)

    results = {}
    for filename, capsule in CAPSULES.items():
        word_count = len(capsule.split())
        print(f"\n  Capsule for {filename}: {word_count} words")
        success = process_file(filename, capsule)
        results[filename] = success

    # ── Summary ──
    print("\n" + "=" * 70)
    print("  SUMMARY")
    print("=" * 70)
    for filename, success in results.items():
        status = "✓ SYNCED" if success else "✗ NEEDS REVIEW"
        print(f"  {status}  {filename}")

    if all(results.values()):
        print("\n  All 3 articles updated. Ready for FAQ Q2+ manual review if flagged above.")
    else:
        print("\n  Some files need review — check output above.")

    print("\n  Next: Publish checklist (move to blog/, cards, author, sitemap, llms.txt)")


if __name__ == "__main__":
    main()
