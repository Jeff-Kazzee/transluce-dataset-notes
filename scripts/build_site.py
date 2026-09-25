"""Build docs/index.html from README.md so the site and the README never drift apart.

Usage: python scripts/build_site.py   (needs the `markdown` package)
"""

from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent

STYLE = """
:root{--bg:#fbfaf7;--fg:#1d1e20;--muted:#5b5f65;--line:#e2ded5;--accent:#1d5bb8;--code:#f0ede6}
@media (prefers-color-scheme:dark){:root{--bg:#131416;--fg:#e7e5e0;--muted:#a1a4a9;--line:#2b2d31;--accent:#7ea8ff;--code:#222428}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.7 Charter,"Iowan Old Style",Georgia,serif}
main{max-width:680px;margin:0 auto;padding:64px 16px 96px}
.kicker{font:600 .78rem/1 ui-sans-serif,-apple-system,"Segoe UI",sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 14px}
h1{font:700 2rem/1.2 ui-sans-serif,-apple-system,"Segoe UI",sans-serif;margin:0 0 24px;letter-spacing:-.01em}
h2{font:700 1.2rem/1.35 ui-sans-serif,-apple-system,"Segoe UI",sans-serif;margin:52px 0 10px}
p{margin:0 0 16px}
a{color:var(--accent);text-underline-offset:3px}
code{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:.8em;background:var(--code);border-radius:5px;padding:1px 5px;overflow-wrap:anywhere}
ol{padding-left:1.3em}
li{margin:6px 0}
"""


def main():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    # The README's site link points at this page, so drop it here.
    text = "\n".join(line for line in text.splitlines() if not line.startswith("Site: "))
    body = markdown.markdown(text, extensions=["toc"])
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Transluce Dataset Notes</title>
<meta name="description" content="What Transluce's AI agent data shows that its report doesn't: a US budget portal hit 586 times, 57 days of nonstop activity, and more.">
<style>{STYLE}</style>
</head>
<body>
<main>
<p class="kicker">Notes on a public dataset</p>
{body}
</main>
</body>
</html>
"""
    (ROOT / "docs/index.html").write_text(page, encoding="utf-8")
    print("wrote docs/index.html")


if __name__ == "__main__":
    main()
