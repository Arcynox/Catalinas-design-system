#!/usr/bin/env python3
"""Migra gradientes/bgs blancos hardcodeados a tokens semanticos."""
import json, re, pathlib

GRAD = re.compile(r"linear-gradient\(180deg,\s*rgba\(255,\s?255,\s?255,\s*([\d.]+)\)\s*,\s*rgba\(255,\s?255,\s?255,\s*([\d.]+)\s*\)\)")

def grad_sem(a, b):
    key = (float(a), float(b))
    m = {
        (.62,.34):"chip", (.62,.36):"chip",
        (.55,.32):"chip", (.55,.30):"input",
        (.66,.42):"float",
    }
    for (x,y),name in m.items():
        if abs(key[0]-x)<.001 and abs(key[1]-y)<.001:
            return name
    return None

SPECIFIC = [
    ("button.json",      "linear-gradient(180deg,#fff,rgba(248,250,255,.85))",          "linear-gradient(180deg,var(--cat-semantic-chip-hover-a),var(--cat-semantic-chip-hover-b))"),
    ("button.json",      "linear-gradient(180deg,#ffffff,rgba(248, 250, 255, 0.85))",   "linear-gradient(180deg,var(--cat-semantic-chip-hover-a),var(--cat-semantic-chip-hover-b))"),
    ("input.json",       "linear-gradient(180deg, #ffffff, rgba(248, 250, 255, 0.92))", "linear-gradient(180deg,var(--cat-semantic-input-focus-a),var(--cat-semantic-input-focus-b))"),
    ("segmented.json",   ".cat-segmented input:checked+span{background:#fff;",          ".cat-segmented input:checked+span{background:var(--cat-semantic-seg-checked);"),
    ("list-statusbar.json","background:rgba(255, 255, 255, 0.5);backdrop-filter",       "background:var(--cat-semantic-statusbar-bg);backdrop-filter"),
    ("sidebar-nav.json", "background:rgba(250,250,253,.45)",                            "background:var(--cat-semantic-sidebar-bg)"),
    ("accordion.json",   "background:rgba(255,255,255,.35);overflow:hidden",            "background:var(--cat-semantic-panel-tint);overflow:hidden"),
    ("dropzone.json",    "background:rgba(255,255,255,.25);cursor:pointer",             "background:var(--cat-semantic-dropzone-bg);cursor:pointer"),
]

changed = []
for f in sorted(pathlib.Path("spec").glob("*.json")):
    sp = json.loads(f.read_text())
    web = sp.get("targets", {}).get("web")
    if not web:
        continue
    def fix_css(css):
        def grad_repl(m):
            name = grad_sem(m.group(1), m.group(2))
            if not name:
                return m.group(0)
            return f"linear-gradient(180deg,var(--cat-semantic-{name}-a),var(--cat-semantic-{name}-b))"
        return GRAD.sub(grad_repl, css)
    web["css"] = [fix_css(c) for c in web.get("css", [])]
    s = f.read_text()
    for fname, old, new in SPECIFIC:
        if fname == f.name and old in s:
            s = s.replace(old, new)
    if s != f.read_text() or True:
        f.write_text(json.dumps(sp, ensure_ascii=False, indent=1))
    changed.append(f.name)

print("procesados:", len(changed))
