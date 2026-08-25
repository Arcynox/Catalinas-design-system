#!/usr/bin/env python3
"""Instala las skills de Catalinas en el directorio de skills del agente.

Uso:
  python3 skills/install.py                     # instala en ~/.agents/skills
  python3 skills/install.py --dest /otro/path   # destino custom (debe contener SKILL.md por carpeta)
"""
import argparse, pathlib, shutil, sys

SRC = pathlib.Path(__file__).resolve().parent
SKILLS = ["catalinas-web", "catalinas-tokens-theming",
          "catalinas-components", "catalinas-motion-a11y"]

ap = argparse.ArgumentParser()
ap.add_argument("--dest", default=str(pathlib.Path.home() / ".agents" / "skills"))
args = ap.parse_args()

dest = pathlib.Path(args.dest)
if not dest.exists():
    print(f"ERROR: destino inexistente: {dest}")
    sys.exit(1)

installed = []
for name in SKILLS:
    src = SRC / name
    if not (src / "SKILL.md").exists():
        print(f"skip {name} (falta SKILL.md)")
        continue
    dst = dest / name
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    installed.append(str(dst))

print(f"Instaladas {len(installed)} skills:")
for i in installed:
    print("  +", i)
print("\nReinicia la sesion del agente para que se detecten.")
