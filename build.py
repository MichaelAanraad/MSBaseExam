"""Validate all questions and write docs/index.html (self-contained, GitHub Pages ready)."""
import json
import os
import sys

from objectives import DOMAINS, GROUPS, objectives
from validate import check, load, load_cases

partial = "--partial" in sys.argv  # preview with whatever groups exist so far
qs = load(list(GROUPS))
err = [] if partial else check(qs, list(GROUPS))
if not partial and (err or len(qs) != 500):
    sys.exit(f"not building: {len(err)} validation errors, {len(qs)} questions (run validate.py)")

data = {
    "domains": {k: {"title": t, "weight": w} for k, (t, w) in DOMAINS.items()},
    "objectives": {k: t for k, (t, _) in objectives().items()},
    "questions": qs,
    "cases": {c["id"]: c for c in load_cases()},
}
# "</" would close the <script> tag early.
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
with open("template.html", encoding="utf-8") as f:
    html = f.read().replace("/*__DATA__*/", blob)
os.makedirs("docs", exist_ok=True)
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"docs/index.html: {len(qs)} questions, {len(html) // 1024} KB")
