#!/usr/bin/env python3
import json, pathlib

STAR = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
        'stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M13 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V9z"/>'
        '<path d="M13 3v6h6"/><path d="M12 12v6m-3-3h6"/></svg>')

ACC = 'var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base))'

CSS = """
.cat-empty{display:flex;flex-direction:column;align-items:center;text-align:center;padding:44px 28px;font-family:var(--cat-font-family-ui)}
.cat-empty-orb{width:64px;height:64px;border-radius:20px;display:grid;place-items:center;margin-bottom:16px;color:ACC;background:linear-gradient(135deg,var(--cat-semantic-chip-a),var(--cat-semantic-chip-b));border:1px solid var(--cat-color-stroke-light);box-shadow:var(--cat-elevation-panel)}
.cat-empty-orb svg{width:26px;height:26px}
.cat-empty-title{margin:0;font-size:var(--cat-font-size-lg);font-weight:600;color:var(--cat-color-ink-hi)}
.cat-empty-msg{margin:5px 0 18px;font-size:var(--cat-font-size-base);color:var(--cat-color-ink-mid);max-width:300px;line-height:1.55}
""".replace("ACC", ACC)

def empty_demo(title, msg, btn_text, btn_cls):
    return ('<div class="cat-empty"><div class="cat-empty-orb">' + STAR + '</div>'
            + '<h4 class="cat-empty-title">' + title + '</h4>'
            + '<p class="cat-empty-msg">' + msg + '</p>'
            + '<button class="' + btn_cls + '">' + btn_text + '</button></div>')

spec = {
    "name": "empty-state",
    "description": "Estado vacio: orbe con icono, titulo, descripcion y accion primaria.",
    "anatomy": ["orb", "title", "message", "action"],
    "states": ["default", "hover(action)"],
    "targets": {
        "web": {
            "markup": '<div class="cat-empty"><div class="cat-empty-orb">' + STAR + '</div><h4 class="cat-empty-title">Sin resultados</h4><p class="cat-empty-msg">Proba con otros terminos o crea algo nuevo.</p><button class="cat-btn primary sm">Crear</button></div>',
            "css": [CSS],
        },
        "qt": {"widget": "QLabel stack", "qss": []},
    },
    "docs": {
        "demos": [
            empty_demo("Sin resultados", "Proba con otros terminos o crea algo nuevo.", "Crear", "cat-btn primary sm"),
            empty_demo("KittyDrive vacio", "Arrastra archivos para empezar a sincronizar con la nube.", "Ver planes", "cat-btn secondary sm"),
        ]
    },
}

pathlib.Path("spec/empty-state.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1))

# targets globales en manifest
b = pathlib.Path("build/build.py")
s = b.read_text()
old = '"widgets": manifest}, ensure_ascii=False, indent=1))'
new = '"widgets": manifest, "targets": ["Web CSS", "React", "Qt", "Flutter", "Tailwind", "Flat JSON"]}, ensure_ascii=False, indent=1))'
if old in s:
    s = s.replace(old, new)
    b.write_text(s)
    print("manifest targets ok")
else:
    print("WARN: anchor manifest no encontrado")
