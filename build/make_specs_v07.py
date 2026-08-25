#!/usr/bin/env python3
import json, pathlib

OUT = pathlib.Path("spec")
SPECS = []
def add(**kw): SPECS.append(kw)

X_SVG = ('<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>')
MIN_SVG = ('<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
           'stroke-width="2.4" stroke-linecap="round"><path d="M5 12h14"/></svg>')
MAX_SVG = ('<svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
           'stroke-width="2.4"><rect x="5" y="5" width="14" height="14" rx="1.5"/></svg>')

CONTROLS = ('<div class="w-ctl">'
            '<button class="w-btn" aria-label="Minimize">' + MIN_SVG + '</button>'
            '<button class="w-btn" aria-label="Maximize">' + MAX_SVG + '</button>'
            '<button class="w-btn close" aria-label="Close">' + X_SVG + '</button></div>')

DOTS = '<span class="w-dots"><i></i><i></i><i class="dim"></i></span>'

# ---------------- WINDOWS ----------------
add(
name="windows",
description="Ventanas de nivel app en dos materiales: Desktop (vidrio acrilico) y Normal (solida). Ambas con barra de control.",
anatomy=["frame", "bar(title + controls)", "body"],
states=["desktop-glass", "standard-solid"],
rules=[
  "Glass para apps de escritorio que viven sobre el wallpaper.",
  "Solid para documentos y ventanas hijas: maxima legibilidad.",
  "El contenido interno siempre es mas opaco que el marco (legibilidad > transparencia)."
],
targets={"web":{
"markup":
'<section class="cat-window glass" style="width:320px">' +
'<header class="w-bar"><b>Desktop</b>' + CONTROLS + '</header>' +
'<div class="w-body">Contenido sobre vidrio acrilico.</div></section>',
"css":[
".cat-window{display:flex;flex-direction:column;border-radius:var(--cat-size-radius-xl);"
"overflow:hidden;font-family:var(--cat-font-family-ui);color:var(--cat-color-ink-hi)}"
".cat-window.glass{background:var(--cat-color-surface-glass-window);"
"backdrop-filter:blur(var(--cat-blur-window)) saturate(var(--cat-blur-saturate-window));"
"-webkit-backdrop-filter:blur(var(--cat-blur-window)) saturate(var(--cat-blur-saturate-window));"
"border:1px solid var(--cat-color-stroke-light);box-shadow:var(--cat-elevation-window),inset 0 1px 0 rgba(255,255,255,.6)}"
".cat-window.solid{background:var(--cat-color-white);border:1px solid var(--cat-color-stroke-input);box-shadow:var(--cat-elevation-window)}",
".w-bar{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:9px 12px}"
".cat-window.glass .w-bar{border-bottom:1px solid var(--cat-color-stroke-light)}"
".cat-window.solid .w-bar{border-bottom:1px solid var(--cat-color-stroke-dark);background:var(--cat-color-surface-hover)}"
".w-bar b{font-size:var(--cat-font-size-base);font-weight:600}"
".w-body{padding:14px;font-size:var(--cat-font-size-base);line-height:1.5}",
".w-ctl{display:flex;gap:2px}"
".w-btn{display:grid;place-items:center;width:28px;height:24px;border:none;border-radius:var(--cat-size-radius-xs);background:none;color:var(--cat-color-ink-hi);cursor:pointer;transition:background var(--cat-motion-fast),transform var(--cat-motion-fast)}"
".w-btn:hover{background:var(--cat-color-surface-hover)}"
".w-btn.close:hover{background:var(--cat-color-danger-base);color:#fff}"
".w-btn.close:active,.w-btn:active{transform:scale(.92)}"]},
"qt":{"widget":"QMainWindow","qss":[
'QWidget[cat="windowGlass"]{background:{$color.surface.glass-window$};border:1px solid {$color.stroke.light$};border-radius:{$size.radius.xl$}}',
'QWidget[cat="windowSolid"]{background:white;border:1px solid {$color.stroke.input$};border-radius:{$size.radius.xl$}}']}},
docs={"demos":[
'<div style="display:flex;gap:18px;flex-wrap:wrap;justify-content:center;width:100%">'
'<section class="cat-window glass" style="width:290px">'
'<header class="w-bar"><b>KittyDrive</b>' + CONTROLS + '</header>'
'<div class="w-body" style="min-height:96px">Vidrio acrilico: el fondo se percibe a traves del marco.</div></section>'
'<section class="cat-window solid" style="width:290px">'
'<header class="w-bar"><b>Documento.txt</b>' + CONTROLS + '</header>'
'<div class="w-body" style="min-height:96px">Ventana solida: legibilidad maxima para contenido.</div></section></div>'],
"note":"Ejemplo completo armado: examples/kittydrive.html"}
)

# ---------------- CAROUSEL ----------------
SLIDES = "".join(
f'<div class="slide"><b>{n}</b><span>{sub}</span></div>'
for n, sub in [("Favoritos","12 items"),("Recientes","67 items"),("Compartidos","8 items"),("Papelera","3 items"),("Descargas","21 items")])

add(
name="carousel", description="Carrusel horizontal con scroll-snap y flechas prev/next.",
targets={"web":{
"markup":
'<div class="car-wrap"><div class="car-head"><b>Galeria</b><span class="car-nav">'
'<button data-cat-car-prev aria-label="Anterior">&#8249;</button>'
'<button data-cat-car-next aria-label="Siguiente">&#8250;</button></span></div>'
'<div class="cat-carousel">' + SLIDES + '</div></div>',
"css":[
".car-wrap{width:min(480px,100%);font-family:var(--cat-font-family-ui)}"
".car-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}"
".car-head b{font-size:var(--cat-font-size-base);color:var(--cat-color-ink-hi)}"
".car-nav button{width:26px;height:26px;margin-left:4px;border:1px solid var(--cat-color-stroke-input);border-radius:50%;background:var(--cat-color-surface-card);color:var(--cat-color-ink-mid);cursor:pointer;font-size:14px;line-height:1;transition:all var(--cat-motion-fast)}"
".car-nav button:hover{background:#fff;color:var(--cat-color-ink-hi)}"
".cat-carousel{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;padding:2px;"
"scrollbar-width:none}"
".cat-carousel::-webkit-scrollbar{display:none}"
".cat-carousel .slide{flex:0 0 150px;height:104px;scroll-snap-align:start;border-radius:var(--cat-size-radius-md);"
"background:var(--cat-color-surface-card);border:1px solid var(--cat-color-stroke-dark);"
"display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px}"
".cat-carousel .slide b{font-size:var(--cat-font-size-sm);font-weight:600;color:var(--cat-color-ink-hi)}"
".cat-carousel .slide span{font-size:var(--cat-font-size-xs);color:var(--cat-color-ink-low)}"],
"js":"""document.addEventListener("click", e => {
  const btn = e.target.closest("[data-cat-car-next],[data-cat-car-prev]");
  if (!btn) return;
  const wrap = btn.closest(".car-wrap");
  const car = wrap && wrap.querySelector(".cat-carousel");
  if (!car) return;
  const first = car.firstElementChild;
  const step = first ? (first.getBoundingClientRect().width + 12) : 162;
  car.scrollBy({ left: btn.hasAttribute("data-cat-car-next") ? step : -step, behavior: "smooth" });
});"""}},
docs={"demos":[
'<div class="car-wrap"><div class="car-head"><b>Favoritos</b><span class="car-nav">'
'<button data-cat-car-prev aria-label="Anterior">&#8249;</button>'
'<button data-cat-car-next aria-label="Siguiente">&#8250;</button></span></div>'
'<div class="cat-carousel">' + SLIDES + '</div></div>']}
)

for s in SPECS:
    (OUT / (s["name"] + ".json")).write_text(json.dumps(s, ensure_ascii=False, indent=1))
print(len(SPECS), "specs nuevas")
