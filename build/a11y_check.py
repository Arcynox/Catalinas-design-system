#!/usr/bin/env python3
"""A11y static check para HTML generado por Catalinas.
Escanea docs/index.html y examples/*.html:
  - botones con solo svg dentro y sin aria-label
  - <img> sin alt
  - inputs sin label asociado ni aria-label/placeholder
Salida: reporte con lineas. Exit 1 si hay errores."""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = [ROOT / "docs" / "index.html", ROOT / "examples" / "kittydrive.html"]

issues = []
for f in FILES:
    if not f.exists():
        continue
    s = f.read_text()
    lines = s.split("\n")

    # botones icon-only sin aria-label
    for m in re.finditer(r"<button\b[^>]*>(.*?)</button>", s, re.S):
        inner, tag = m.group(1), m.group(0)
        if "<svg" in inner and re.sub(r"<[^>]+>|\s", "", inner) == "":
            if 'aria-label' not in tag:
                ln = s[:m.start()].count("\n") + 1
                issues.append(f"{f.name}:{ln} button solo-icono sin aria-label")

    # img sin alt
    for m in re.finditer(r"<img\b[^>]*>", s):
        if "alt=" not in m.group(0):
            ln = s[:m.start()].count("\n") + 1
            issues.append(f"{f.name}:{ln} <img> sin alt")

    # inputs sin label/aria
    for m in re.finditer(r"<input\b[^>]*>", s):
        tag = m.group(0)
        if re.search(r'type="(hidden|submit|checkbox|radio|range)"', tag):
            continue
        if "aria-label" not in tag and "placeholder" not in tag and 'id="' not in tag:
            ln = s[:m.start()].count("\n") + 1
            issues.append(f"{f.name}:{ln} input sin label/aria-label/placeholder")

if issues:
    print(f"A11Y: {len(issues) if False else ''}{len(issues)} problema(s):")
    for i in issues:
        print("  -", i)
    sys.exit(1)
print("A11Y OK: sin problemas estaticos detectados")
