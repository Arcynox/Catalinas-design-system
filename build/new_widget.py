#!/usr/bin/env python3
"""Scaffolder de widgets: python3 new_widget.py <nombre>
Crea spec/<nombre>.json con esqueleto valido y corre el build."""
import json, pathlib, subprocess, sys

if len(sys.argv) < 2:
    print("uso: python3 new_widget.py <nombre-widget>")
    sys.exit(1)

name = sys.argv[1].strip().lower().replace(" ", "-")
root = pathlib.Path(__file__).resolve().parent.parent
spec_file = root / "spec" / f"{name}.json"

if spec_file.exists():
    print(f"ERROR: ya existe spec/{name}.json")
    sys.exit(1)

skeleton = {
    "name": name,
    "description": f"Widget {name}.",
    "anatomy": [],
    "props": {},
    "states": ["default", "hover", "focus-visible", "disabled"],
    "targets": {
        "web": {
            "markup": f'<div class="cat-{name}">{name}</div>',
            "css": [
                f".cat-{name}{{font-family:var(--cat-font-family-ui);font-size:var(--cat-font-size-base);color:var(--cat-color-ink-hi)}}"
            ]
        }
    },
    "docs": {"demos": [f'<div class="cat-{name}">{name}</div>']}
}

spec_file.write_text(json.dumps(skeleton, ensure_ascii=False, indent=1))
print(f"creado spec/{name}.json")

r = subprocess.run([sys.executable, str(root / "build" / "build.py")], capture_output=True, text=True)
print(r.stdout)
if r.returncode != 0:
    print(r.stderr)
    sys.exit(r.returncode)
print(f"\nProximos pasos:")
print(f"  1. Editar spec/{name}.json (css/markup/qss)")
print(f"  2. python3 build/build.py")
print(f"  3. Ver en docs/index.html#w-{name}")
