#!/usr/bin/env python3
import json, pathlib

OUT = pathlib.Path("spec")
SPECS = []
def add(**kw): SPECS.append(kw)

ACC = "var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base))"
RING = "var(--cat-semantic-accent-ring)"
CHIP_A = "var(--cat-semantic-chip-a)"
CHIP_B = "var(--cat-semantic-chip-b)"

STAR = ('<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.6l2.8 5.9 6.4.8-4.7 4.4 '
        '1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z"/></svg>')
DOCICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
           'stroke-linecap="round" stroke-linejoin="round">'
           '<path d="M13 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V9z"/>'
           '<path d="M13 3v6h6"/><path d="M12 12v6m-3-3h6"/></svg>')

# ---------------- COLOR PICKER ----------------
cp_css1 = (
"[data-cat-colors]{display:inline-flex;align-items:center;gap:8px}"
".cat-swatch{width:22px;height:22px;border-radius:50%;border:none;cursor:pointer;"
"box-shadow:inset 0 0 0 1px rgba(0,0,0,.12);"
"transition:transform var(--cat-motion-fast) var(--cat-motion-ease-out),box-shadow var(--cat-motion-fast)}"
".cat-swatch:hover{transform:scale(1.12)}"
".cat-swatch.auto{background:conic-gradient(red,yellow,lime,cyan,blue,magenta,red)}"
".cat-swatch.active{box-shadow:0 0 0 2px var(--cat-color-surface-content),0 0 0 4px " + ACC + "}"
".cat-label-side{font-size:var(--cat-font-size-xs);color:var(--cat-color-ink-low);margin-left:4px}")
cp_css2 = (
"@media (prefers-reduced-motion: reduce){.cat-swatch{transition:none}}")
cp_js = (
'(() => {'
' function init(root){'
'  root.addEventListener("click", e => {'
'   const b = e.target.closest(".cat-swatch");'
'   if (!b || !root.contains(b)) return;'
'   const rs = document.documentElement.style;'
'   root.querySelectorAll(".cat-swatch").forEach(x => x.classList.toggle("active", x === b));'
'   if (b.dataset.color){'
'    rs.setProperty("--cat-semantic-accent-dynamic", b.dataset.color);'
'    rs.setProperty("--cat-semantic-accent-ring", b.dataset.color + "29");'
'   } else {'
'    rs.removeProperty("--cat-semantic-accent-dynamic");'
'    rs.removeProperty("--cat-semantic-accent-ring");'
'   }'
'  });'
' }'
' document.addEventListener("DOMContentLoaded", () => {'
'  document.querySelectorAll("[data-cat-colors]").forEach(init);'
' });'
'})();')
swatches = (
'<button class="cat-swatch auto active" data-auto aria-label="Auto"></button>'
'<button class="cat-swatch" style="background:#5e9eff" data-color="#5e9eff" aria-label="Azul"></button>'
'<button class="cat-swatch" style="background:#a78bfa" data-color="#a78bfa" aria-label="Violeta"></button>'
'<button class="cat-swatch" style="background:#f2a2c6" data-color="#f2a2c6" aria-label="Rosa"></button>'
'<button class="cat-swatch" style="background:#ef5a76" data-color="#ef5a76" aria-label="Rojo"></button>'
'<button class="cat-swatch" style="background:#34c759" data-color="#34c759" aria-label="Verde"></button>')
add(
name="color-picker",
description="Seleccion de accent para todo el sistema: swatches + auto (derivado del wallpaper).",
states=["default","hover","active"],
targets={"web":{
"markup":'<div class="cat-colors" data-cat-colors>' + swatches + '<span class="cat-label-side">cambia todo el UI</span></div>',
"css":[cp_css1, cp_css2],
"js":cp_js}},
docs={"demos":[
'<div class="cat-colors" data-cat-colors>' + swatches + '<span class="cat-label-side">cambia todo el UI</span></div>',
'<div class="cat-alert info"><span class="a-icon" style="background:' + ACC + '">'
'<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M12 11v5"/></svg></span>'
'<div class="a-body"><b>Mira este banner</b><span>El icono sigue el accent elegido arriba.</span></div></div>'],
"note":"Auto = hue derivado del wallpaper en produccion."}
)

# ---------------- RADIUS SCALE ----------------
rr = lambda r, extra="": '<div class="rr"><i style="border-radius:' + r + ';' + extra + '"></i>' + r.replace("999px","pill") + '</div>'
radii_demo = ('<div class="cat-radii">' + rr("4px") + rr("6px") + rr("8px") + rr("12px") + rr("16px")
              + '<div class="rr"><i style="border-radius:999px;width:64px;height:36px"></i>pill</div></div>')
add(
name="radius-scale",
description="Escala de radios sobre gris neutro, para elegir el correcto por superficie.",
targets={"web":{
"markup": radii_demo,
"css":[
".cat-radii{display:inline-flex;flex-wrap:wrap;gap:16px}"
".cat-radii .rr{display:flex;flex-direction:column;align-items:center;gap:6px;font-size:10px;font-weight:500;color:var(--cat-color-ink-low);font-family:var(--cat-font-family-mono)}"
".cat-radii i{display:block;width:56px;height:56px;background:#d7dce6;border:1px solid rgba(0,0,0,.08)}"]},
"qt":{"widget":"n/a","qss":[]}},
docs={"demos":[radii_demo],
"note":"Regla HIG: controles sm, contenedores md-lg, ventanas xl-window."}
)

# ---------------- MOBILE TABBAR ----------------
BAR_ICONS = [
 ("home", "Inicio", '<path d="M3 11l9-8 9 8"/><path d="M5 10v10a1 1 0 0 0 1 1h4v-6h4v6h4a1 1 0 0 0 1-1V10"/>'),
 ("search", "Buscar", '<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>'),
 ("plus", "Crear", '<path d="M12 5v14M5 12h14"/>'),
 ("heart", "Favs", '<path d="M12 21C7 16.5 3 13.2 3 9.5A4.5 4.5 0 0 1 12 6a4.5 4.5 0 0 1 9 3.5c0 3.7-4 7-9 11.5z"/>'),
 ("user", "Perfil", '<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 5-6 8-6s6.5 2 8 6"/>'),
]
def bar_items(with_labels):
    out = ""
    for i, (k, lbl, pth) in enumerate(BAR_ICONS):
        act = " is-active" if i == 0 else ""
        svg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + pth + '</svg>'
        label = "<span>" + lbl + "</span>" if with_labels else ""
        out += ('<button type="button" class="tb-item' + act + '" data-cat-tab role="tab" aria-selected="'
                + str(i == 0).lower() + '">' + svg + label + '</button>')
    return out
tabbar_css1 = (
".cat-tabbar{display:flex;width:min(400px,100%);padding:6px;border-radius:22px;"
"background:var(--cat-color-surface-glass-chip);"
"backdrop-filter:blur(var(--cat-blur-chip)) saturate(var(--cat-blur-saturate-chip));"
"-webkit-backdrop-filter:blur(var(--cat-blur-chip)) saturate(var(--cat-blur-saturate-chip));"
"border:1px solid var(--cat-color-stroke-input);box-shadow:var(--cat-elevation-menu)}"
".tb-item{flex:1;display:flex;flex-direction:column;align-items:center;gap:2px;padding:7px 0 5px;"
"border:none;border-radius:14px;background:none;color:var(--cat-color-ink-low);"
"font:500 10px var(--cat-font-family-ui);cursor:pointer;transition:color var(--cat-motion-fast)}"
".tb-item svg{width:20px;height:20px}"
".tb-item:hover{color:var(--cat-color-ink-mid)}"
".tb-item.is-active{color:" + ACC + "}")
tabbar_css2 = (
"@media (max-width:520px){.cat-tabbar{position:fixed;left:12px;right:12px;bottom:12px;z-index:var(--cat-depth-z-float)}}")
add(
name="mobile-tabbar",
description="Barra de navegacion inferior para movil: glass con blur, item activo accent.",
targets={"web":{
"markup":'<nav class="cat-tabbar" data-cat-tabs role="tablist">' + bar_items(True) + '</nav>',
"css":[tabbar_css1, tabbar_css2]},
"qt":{"widget":"QToolBar (bottom)","qss":[]}},
docs={"demos":[
'<nav class="cat-tabbar" data-cat-tabs role="tablist">' + bar_items(True) + '</nav>',
'<nav class="cat-tabbar" data-cat-tabs role="tablist" style="width:300px">' + bar_items(False) + '</nav>'],
"note":"En pantallas chicas se fija abajo automaticamente."}
)

# ---------------- TYPOGRAPHY ----------------
typo_css = (
".cat-h1,.cat-h2,.cat-h3,.cat-body,.caption,.cat-code,.cat-link{font-family:var(--cat-font-family-ui);margin:0}"
".cat-h1{font-size:24px;font-weight:700;letter-spacing:-.02em;color:var(--cat-color-ink-hi)}"
".cat-h2{font-size:17px;font-weight:600;color:var(--cat-color-ink-hi)}"
".cat-h3{font-size:15px;font-weight:600;color:var(--cat-color-ink-hi)}"
".cat-body{font-size:13px;line-height:1.55;color:var(--cat-color-ink-hi)}"
".caption{font-size:11px;color:var(--cat-color-ink-low)}"
".cat-text-muted{color:var(--cat-color-ink-mid)}"
".cat-text-low{color:var(--cat-color-ink-low)}"
".cat-text-faint{color:var(--cat-color-ink-faint)}"
".cat-text-accent{color:" + ACC + ";font-weight:550}"
".cat-text-success{color:var(--cat-color-success);font-weight:550}"
".cat-text-danger{color:var(--cat-color-danger-base);font-weight:550}"
".cat-mark{background:var(--cat-color-accent-subtle-a);color:inherit;border-radius:3px;padding:1px 4px;"
"-webkit-box-decoration-break:clone;box-decoration-break:clone}"
".cat-mark.success{background:rgba(52,199,89,.18)}"
".cat-mark.danger{background:rgba(232,56,45,.10)}"
".cat-code{font:500 12px var(--cat-font-family-mono);background:rgba(0,0,0,.05);border:1px solid var(--cat-color-stroke-dark);"
"border-radius:4px;padding:1px 5px;color:var(--cat-color-ink-hi)}"
".cat-link{color:" + ACC + ";text-decoration:none}"
".cat-link:hover{text-decoration:underline}")

def tag(lbl): return '<span class="tag">' + lbl + '</span>'
typo_demo = (
'<div class="cat-typography-list">'
'<div class="trow">' + tag("H1") + '<h1 class="cat-h1">Titulo de vista</h1></div>'
'<div class="trow">' + tag("H2") + '<h2 class="cat-h2">Seccion destacada</h2></div>'
'<div class="trow">' + tag("Body") + '<p class="cat-body">Texto con <span class="cat-mark">resaltado accent</span> dentro.</p></div>'
'<div class="trow">' + tag("Mark") + '<p class="cat-body">Variantes: <span class="cat-mark success">ok</span> <span class="cat-mark danger">error</span> <code class="cat-code">codigo</code></p></div>'
'<div class="trow">' + tag("Estados") + '<p class="cat-body">muted <span class="cat-text-muted">medio</span>, <span class="cat-text-low">bajo</span>, <span class="cat-text-accent">accent</span>, <span class="cat-text-success">exito</span>, <span class="cat-text-danger">error</span></p></div>'
'<div class="trow">' + tag("Caption") + '<span class="caption">Metadata secundaria - Aug 25, 2026</span></div>'
'</div>')

typo_css_list_style = (
".cat-typography-list{display:flex;flex-direction:column;gap:10px;width:100%;max-width:600px}"
".cat-typography-list .trow{display:flex;align-items:center;gap:12px}"
".cat-typography-list .tag{flex:none;width:64px;font-size:9px;font-weight:700;letter-spacing:.06em;"
"text-transform:uppercase;color:var(--cat-color-ink-faint)}")

add(
name="typography",
description="Escala textual, estados y resaltado tipo seleccion (.cat-mark).",
targets={"web":{"markup": typo_demo,
"css":[typo_css, typo_css_list_style]}},
docs={"demos":[typo_demo],
"note":".cat-mark usa box-decoration-break:clone: sobrevive saltos de linea."}
)

for s in SPECS:
    (OUT / (s["name"] + ".json")).write_text(json.dumps(s, ensure_ascii=False, indent=1))
print(len(SPECS), "specs nuevas")
