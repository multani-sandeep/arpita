#!/usr/bin/env python3
"""
CV Markdown to single-page PDF converter.
Uses pandoc for MD->HTML and Chrome headless for HTML->PDF.
No pip dependencies required.

Usage:
    python3 cv_to_pdf.py input.md [output.pdf]
    python3 cv_to_pdf.py input.md --preview     # open HTML in browser to check layout
"""

import sys
import os
import tempfile
import subprocess
import shutil
import webbrowser

# ── CONFIGURATION ─────────────────────────────────────────────────────────────
# Tweak these to fit content on one page.
# Workflow: run with --preview to check in browser, adjust, repeat, then generate PDF.

FONT_SIZE       = 9   # pt  — main body text (reduce to fit more)
NAME_SIZE       = 14    # pt  — H1 candidate name
SECTION_SIZE    = 10   # pt  — section header bold labels
ROLE_SPACING    = 18     # px  — space above each role title block
SECTION_SPACING = 10    # px  — space above section headers (SUMMARY, SKILLS, etc.)
LINE_HEIGHT     = 1.28  # —   — tighter = more content per page
MARGIN_TOP      = 9     # mm  — page margins
MARGIN_BOTTOM   = 9     # mm
MARGIN_LEFT     = 13    # mm
MARGIN_RIGHT    = 13    # mm
PAGE_SIZE       = "A4"  # A4 or Letter
# ─────────────────────────────────────────────────────────────────────────────

CSS = f"""
@page {{
    size: {PAGE_SIZE};
    margin: {MARGIN_TOP}mm {MARGIN_RIGHT}mm {MARGIN_BOTTOM}mm {MARGIN_LEFT}mm;
}}

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}

body {{
    font-family: Calibri, 'Segoe UI', Arial, sans-serif;
    font-size: {FONT_SIZE}pt;
    line-height: {LINE_HEIGHT};
    color: #111;
}}

h1 {{
    font-size: {NAME_SIZE}pt;
    text-align: left;
    letter-spacing: 0.8px;
    font-weight: 700;
    margin-bottom: 2px;
}}

/* Contact line immediately after name */
h1 + p {{
    text-align: left;
    font-size: {round(FONT_SIZE - 0.8, 1)}pt;
    color: #444;
    margin-bottom: 4px;
}}

p {{
    margin-bottom: 2px;
}}

/* Section label paragraphs — added via post-processing in md_to_html_body */
p.section-header {{
    font-size: {SECTION_SIZE}pt;
    font-weight: 700;
    margin-top: {SECTION_SPACING}px;
    margin-bottom: 1px;
    padding-bottom: 1px;
}}

/* Role title lines — bold paragraphs containing | e.g. "Role | Company | Dates" */
p.role-header {{
    margin-top: {ROLE_SPACING}px;
    margin-bottom: 1px;
}}

/* Footer section headers (Education, Certifications, Thought Leadership, Community) */
p.section-header.footer-section {{
    margin-top: {ROLE_SPACING}px;
}}

ul {{
    margin: 1px 0 2px 0;
    padding-left: 14px;
    list-style-type: disc;
}}

li {{
    margin-bottom: 1px;
}}

/* Nested bullet lists (Highlights sub-points) */
li > ul {{
    margin-top: 1px;
    margin-bottom: 0;
    padding-left: 12px;
    list-style-type: circle;
}}

li > ul > li {{
    margin-bottom: 1px;
}}

strong {{
    font-weight: 600;
}}

em {{
    font-style: italic;
    color: #444;
}}

a {{
    color: #111;
    text-decoration: none;
}}

hr {{
    display: none;
}}

.page-break {{
    break-before: page;
    page-break-before: always;
}}
"""

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
{css}
</style>
</head>
<body>
{body}
</body>
</html>
"""


def find_chrome():
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
    ]
    for c in candidates:
        if c and os.path.exists(c):
            return c
    return None


def find_pandoc():
    path = shutil.which("pandoc")
    if path:
        return path
    # Homebrew default
    homebrew_pandoc = "/opt/homebrew/bin/pandoc"
    if os.path.exists(homebrew_pandoc):
        return homebrew_pandoc
    return None


def md_to_html_body(md_path, pandoc_path):
    import re
    result = subprocess.run(
        [pandoc_path, md_path, "-f", "markdown", "-t", "html", "--no-highlight"],
        capture_output=True,
        text=True,
        check=True,
    )
    # Tag paragraphs that contain ONLY a <strong> (no surrounding text).
    # :only-child in CSS cannot distinguish these from <strong> followed by text.
    html = re.sub(
        r'<p>(<strong>(?:[A-Z /]|&amp;)+</strong>)</p>',
        r'<p class="section-header">\1</p>',
        result.stdout,
    )
    # Tag role title lines — bold paragraphs whose <strong> content contains | (pipe),
    # e.g. "Delivery Lead | Worldpay | Domain | Dates" (may include trailing <em> note).
    # Uses a lambda so we can check for | after matching across newlines.
    html = re.sub(
        r'<p>(<strong>[\s\S]*?</strong>(?:\s*<em>[\s\S]*?</em>)?)\s*</p>',
        lambda m: '<p class="role-header">' + m.group(1) + '</p>'
                  if '|' in m.group(1) else m.group(0),
        html,
    )
    # Add extra top spacing to footer section headers.
    _FOOTER = {'EDUCATION', 'CERTIFICATIONS', 'THOUGHT LEADERSHIP', 'COMMUNITY', 'INTERESTS'}
    html = re.sub(
        r'<p class="section-header">(<strong>([^<]+)</strong>)</p>',
        lambda m: '<p class="section-header footer-section">' + m.group(1) + '</p>'
                  if any(s in m.group(2) for s in _FOOTER)
                  else m.group(0),
        html,
    )
    return html


def render_pdf(html_path, pdf_path, chrome_path):
    abs_html = os.path.abspath(html_path)
    abs_pdf  = os.path.abspath(pdf_path)
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={abs_pdf}",
        f"file://{abs_html}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if not os.path.exists(abs_pdf):
        # Fallback: older --headless flag
        cmd[1] = "--headless"
        result = subprocess.run(cmd, capture_output=True, text=True)
    if not os.path.exists(abs_pdf):
        print("Chrome PDF generation failed:")
        print(result.stderr[-1000:])
        sys.exit(1)


def write_temp_html(html):
    tmp = tempfile.NamedTemporaryFile(
        suffix=".html", mode="w", delete=False, encoding="utf-8"
    )
    tmp.write(html)
    tmp.close()
    return tmp.name


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    input_md  = args[0]
    preview   = "--preview" in args
    remaining = [a for a in args[1:] if not a.startswith("--")]
    output_pdf = remaining[0] if remaining else "/tmp/ArpitaNarula.pdf"

    if not os.path.exists(input_md):
        print(f"File not found: {input_md}")
        sys.exit(1)

    pandoc = find_pandoc()
    if not pandoc:
        print("pandoc not found. Install with: brew install pandoc")
        sys.exit(1)

    body    = md_to_html_body(input_md, pandoc)
    html    = HTML_TEMPLATE.format(css=CSS, body=body)
    tmp_html = write_temp_html(html)

    if preview:
        print(f"Preview: {tmp_html}")
        webbrowser.open(f"file://{os.path.abspath(tmp_html)}")
        print("Adjust constants at the top of cv_to_pdf.py, then re-run without --preview.")
        return

    chrome = find_chrome()
    if not chrome:
        print("Google Chrome not found. Install Chrome and try again.")
        sys.exit(1)

    print(f"Input:   {input_md}")
    print(f"Output:  {output_pdf}")

    try:
        render_pdf(tmp_html, output_pdf, chrome)
        print("Done.")
    finally:
        os.unlink(tmp_html)


if __name__ == "__main__":
    main()
