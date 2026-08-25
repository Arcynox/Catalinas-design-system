#!/usr/bin/env python3
"""v0.4: flatten (menos gradientes), remove dark, pulido HIG macOS."""
import json, pathlib, re

ROOT = pathlib.Path(".")

# ---------- 1) tokens ----------
tp = ROOT / "tokens" / "tokens.json"
t = json.loads(tp.read_text())
t["$version"] = "0.4.0"

sem = t["semantic"]
# pares -> valores planos
flat_map = {
    "chip-a": "rgba(255, 255, 255, 0.55)",
    "chip-b": "rgba(255, 255, 255, 0.55)",
    "chip-hover-a": "rgba(255, 255, 255, 0.75)",
    "chip-hover-b": "rgba(255, 255, 255, 0.75)",
    "tab-a": "rgba(255, 255, 255, 0.78)",
    "tab-b": "rgba(255, 255, 255, 0.78)",
    "input-a": "rgba(255, 255, 255, 0.50)",
    "input-b": "rgba(255, 255, 255, 0.50)",
    "input-focus-a": "#ffffff",
    "input-focus-b": "#ffffff",
    "float-a": "rgba(252, 253, 255, 0.74)",
    "float-b": "rgba(252, 253, 255, 0.74)",
}
sem.update(flat_map)
sem["seg-checked"] = "#ffffff"
sem["toolbar-bg"] = "rgba(120, 150, 255, 0.10)"
sem["accent-hover-solid"] = "{color.accent.hover}"
sem["accent-active-solid"] = "{color.accent.active}"

# dark fuera
t.pop("$themes", None)

# sombras mas suaves / neutras
t["elevation"]["window"] = "0 18px 60px rgba(0, 0, 0, 0.26), 0 6px 18px rgba(0, 0, 0, 0.12)"
t["elevation"]["raised"] = "0 1px 2px rgba(0, 0, 0, 0.14)"
t["elevation"]["float"] = "0 16px 44px rgba(10, 12, 24, 0.30), 0 4px 12px rgba(10, 12, 24, 0.14)"
json.dump(t, tp.open("w"), ensure_ascii=False, indent=2)
print("tokens planos + sin dark")

# ---------- 2) specs: migrar a planos ----------
GRADPAIR = re.compile(r"linear-gradient\(180deg,\s*var\(--cat-semantic-([\w-]+)-a\),\s*var\(--cat-semantic-\1-b\)\)")

def flatten(css):
    css = GRADPAIR.sub(lambda m: f"var(--cat-semantic-{m.group(1)}-a)", css)
    # toolbar gradiente -> tinte plano
    css = re.sub(r"background:\s*var\(--cat-semantic-grad-toolbar\)",
                 "background:var(--cat-semantic-toolbar-bg)", css)
    # progress fill
    css = css.replace(
        "background:linear-gradient(90deg,var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base)),var(--cat-color-pink))",
        "background:var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base))")
    return css

for f in sorted((ROOT / "spec").glob("*.json")):
    sp = json.loads(f.read_text())
    web = sp.get("targets", {}).get("web")
    if not web:
        continue
    web["css"] = [flatten(c) for c in web.get("css", [])]
    f.write_text(json.dumps(sp, ensure_ascii=False, indent=1))
print("specs aplanadas")
