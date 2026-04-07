"""
Add Google Ads tag to all HTML files in the current directory.
Run from your senticmoney-website folder:
    python add-gtag.py
"""
import os
import glob

GTAG_SNIPPET = '''    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=AW-1065282227"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'AW-1065282227');
    </script>
'''

MARKER = 'AW-1065282227'

html_files = glob.glob('*.html')
if not html_files:
    print("No HTML files found in current directory. Are you in the right folder?")
    exit(1)

modified = []
skipped = []

for filepath in sorted(html_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if MARKER in content:
        skipped.append(filepath)
        continue

    # Insert after <head> tag (with optional attributes)
    import re
    new_content, count = re.subn(r'(<head[^>]*>)\n', r'\1\n' + GTAG_SNIPPET, content, count=1)

    if count == 1:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified.append(filepath)
    else:
        print(f"  WARNING: Could not find <head> tag in {filepath}")

print(f"\nGoogle Ads tag (AW-1065282227) added to {len(modified)} files:")
for f in modified:
    print(f"  ✓ {f}")

if skipped:
    print(f"\nSkipped {len(skipped)} files (tag already present):")
    for f in skipped:
        print(f"  - {f}")
