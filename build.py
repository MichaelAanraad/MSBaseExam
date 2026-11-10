"""Validate all questions and write docs/<exam>/index.html (self-contained, GitHub Pages ready),
plus docs/index.html that links to every built exam."""
import json
import os
import re
import sys

import exam  # python build.py <exam>; must come before objectives

from objectives import DOMAINS, EXAM, EXAM_TITLE, GROUPS, TOTAL, objectives
from validate import check, load, load_cases

partial = "--partial" in sys.argv  # preview with whatever groups exist so far
qs = load(list(GROUPS))
err = [] if partial else check(qs, list(GROUPS))
if not partial and (err or len(qs) != TOTAL):
    sys.exit(f"not building: {len(err)} validation errors, {len(qs)} questions (run validate.py)")

data = {
    "exam": {"id": EXAM, "title": EXAM_TITLE},
    "domains": {k: {"title": t, "weight": w} for k, (t, w) in DOMAINS.items()},
    "objectives": {k: t for k, (t, _) in objectives().items()},
    "questions": qs,
    "cases": {c["id"]: c for c in load_cases()},
}
# "</" would close the <script> tag early.
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
with open(os.path.join(exam.ROOT, "template.html"), encoding="utf-8") as f:
    html = f.read().replace("/*__DATA__*/", blob).replace("__EXAM_TITLE__", EXAM_TITLE).replace("__EXAM__", EXAM)
out = os.path.join(exam.ROOT, "docs", exam.KEY)
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print(f"docs/{exam.KEY}/index.html: {len(qs)} questions, {len(html) // 1024} KB")

# landing page: one link per exam that has been built
links = []
for k in exam.EXAMS:
    if os.path.isfile(os.path.join(exam.ROOT, "docs", k, "index.html")):
        with open(os.path.join(exam.ROOT, "exams", k, "objectives.py"), encoding="utf-8") as f:
            src = f.read()
        eid, title = (re.search(rf'^{v} = "(.*)"', src, re.M).group(1) for v in ("EXAM", "EXAM_TITLE"))
        links.append(f'<li><a href="{k}/"><b>{eid}</b> {title}</a></li>')
with open(os.path.join(exam.ROOT, "docs", "index.html"), "w", encoding="utf-8") as f:
    f.write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Exam Buddy</title>
<style>
:root {{ color-scheme: light dark; --bg: #f6f7f9; --card: #fff; --text: #1b1f24; --accent: #2563eb; --line: #d8dde3; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg: #111418; --card: #1a1e24; --text: #e6e9ee; --accent: #6ea8ff; --line: #2c323a; }} }}
body {{ margin: 0; background: var(--bg); color: var(--text); font: 16px/1.55 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }}
main {{ max-width: 860px; margin: 0 auto; padding: 24px 16px 64px; overflow-wrap: anywhere; }}
ul {{ list-style: none; padding: 0; }}
a {{ display: block; padding: 16px; margin: 0 0 12px; background: var(--card); border: 1px solid var(--line); border-radius: 12px; color: var(--text); text-decoration: none; }}
a:hover, a:focus-visible {{ border-color: var(--accent); }}
b {{ color: var(--accent); margin-right: 6px; }}
</style></head>
<body><main><h1>Exam Buddy</h1><p>Practice exams for Microsoft certifications. Original questions, not real exam questions.</p>
<ul>{"".join(links)}</ul></main></body></html>
""")
