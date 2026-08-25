#!/usr/bin/env python3
"""v0.5.2: gliders css, segmented/rating a botones, hairlines visibles, demos consolidadas."""
import json, pathlib

def load(n): return json.loads((pathlib.Path("spec")/n).read_text())
def save(n,d): (pathlib.Path("spec")/n).write_text(json.dumps(d,ensure_ascii=False,indent=1))

# ---------- TABS: glider ----------
d=load("tabs.json")
d["targets"]["web"]["css"][0]+="""
[data-cat-tabs]{position:relative}
.cat-tabs>.cat-glider{top:0;bottom:0;left:0;border-radius:7px;background:var(--cat-semantic-tab-a);border:1px solid var(--cat-color-stroke-dark);box-shadow:0 1px 2px rgba(25,35,65,.10);transition:transform 240ms var(--cat-motion-spring),width 240ms var(--cat-motion-spring),opacity 150ms ease;opacity:0;z-index:0;width:max-content}
.cat-tab{position:relative;z-index:1;background:none!important;border-color:transparent!important;box-shadow:none!important}
.cat-tab.is-active{color:var(--cat-color-ink-hi);font-weight:var(--cat-font-weight-semibold)}
.cat-tab:not(.is-active):hover{background:rgba(255,255,255,.35)!important}"""
save("tabs.json",d)

# ---------- SEGMENTED: botones + glider ----------
d=load("segmented.json")
d["targets"]["web"]={
"markup":'<div class="cat-segmented" data-cat-segmented role="radiogroup" aria-label="Vista"><button type="button" class="seg-btn is-active" aria-pressed="true">Icons</button><button type="button" class="seg-btn" aria-pressed="false">List</button><button type="button" class="seg-btn" aria-pressed="false">Gallery</button></div>',
"css":["""
.cat-segmented{position:relative;display:inline-flex;padding:2px;border-radius:9px;background:rgba(120,120,128,.14);gap:2px;font-family:var(--cat-font-family-ui)}
.cat-segmented>.cat-glider{top:2px;bottom:2px;left:0;border-radius:7px;background:var(--cat-semantic-seg-checked);box-shadow:0 1px 3px rgba(0,0,0,.14),0 0 0 .5px rgba(0,0,0,.04);transition:transform 240ms var(--cat-motion-spring),width 240ms var(--cat-motion-spring),opacity 150ms ease;opacity:0;z-index:0;width:max-content}
.seg-btn{position:relative;z-index:1;display:inline-flex;align-items:center;height:26px;padding:0 13px;border-radius:7px;border:none;background:none;font:500 var(--cat-font-size-sm) var(--cat-font-family-ui);color:var(--cat-color-ink-mid);cursor:pointer;user-select:none;transition:color var(--cat-motion-fast) ease}
.seg-btn:hover{color:var(--cat-color-ink-hi)}
.seg-btn.is-active{color:var(--cat-color-ink-hi);font-weight:600}
.seg-btn:focus-visible{outline:2px solid var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base));outline-offset:-2px;border-radius:7px}"""]}
d["docs"]={"demos":[
'<div class="cat-segmented" data-cat-segmented role="radiogroup"><button type="button" class="seg-btn is-active" aria-pressed="true">Icons</button><button type="button" class="seg-btn" aria-pressed="false">List</button><button type="button" class="seg-btn" aria-pressed="false">Gallery</button></div>']}
save("segmented.json",d)

# ---------- RATING: estrellas svg + js ----------
star='<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z"/></svg>'
stars="".join(f'<button type="button" class="star" aria-label="{i} estrellas">{star}</button>' for i in range(1,6))
d=load("rating.json")
d["targets"]["web"]={
"markup":f'<div class="cat-rating" data-cat-rating data-value="3" role="radiogroup" aria-label="Puntaje">{stars}</div>',
"css":["""
.cat-rating{display:inline-flex;gap:3px}
.star{width:21px;height:21px;padding:0;border:none;background:none;color:var(--cat-color-stroke-input);cursor:pointer;transition:transform 120ms var(--cat-motion-ease-out),color 120ms ease}
.star:hover{transform:scale(1.18)}
.star.on{color:var(--cat-color-warning)}
.star svg{width:100%;height:100%;display:block}"""]}
d["docs"]={"demos":[f'<div class="cat-rating" data-cat-rating data-value="4" role="radiogroup">{stars}</div>',
f'<div class="cat-rating" data-cat-rating data-value="2" role="radiogroup">{stars}</div>'],
"note":"Hover preview y click para fijar. Valor inicial via data-value."}
save("rating.json",d)

# ---------- BUTTON: demos consolidados ----------
d=load("button.json")
d["docs"]={"demos":[
'<button class="cat-btn primary">Primary</button>'
'<button class="cat-btn secondary">Secondary</button>'
'<button class="cat-btn ghost">Ghost</button>'
'<button class="cat-btn danger">Danger</button>'
'<button class="cat-btn link">Link</button>'
'<span style="width:12px"></span>'
'<button class="cat-btn primary sm">Small</button>'
'<button class="cat-btn primary loading">Loading</button>'
'<button class="cat-btn primary disabled">Disabled</button>']}
save("button.json",d)

# ---------- ICONS: quitar picker duplicado del demo ----------
d=load("icons.json")
d["docs"]["demos"]=d["docs"]["demos"][1:]   # queda solo la grilla
save("icons.json",d)

# ---------- HAIRLINES visibles en superficies claras ----------
SWAPS=[("border:1px solid var(--cat-color-stroke-light)","border:1px solid var(--cat-color-stroke-input)")]
for name in ["button.json","input.json","breadcrumb-toolbar.json","empty-state.json","breadcrumb-toolbar.json"]:
    p=pathlib.Path("spec")/name
    if not p.exists(): continue
    s=p.read_text()
    for a,b in SWAPS:
        if a in s:
            s=s.replace(a,b)
            # nav-seg / input / btn-secondary / empty-orb / toolbar border
            json.loads(s)
            p.write_text(s)
print("hairlines ok")

# toolbar border blanco especifico
p=pathlib.Path("spec/breadcrumb-toolbar.json"); s=p.read_text()
s=s.replace("border:1px solid rgba(255,255,255,.42)","border:1px solid var(--cat-color-stroke-dark)")
p.write_text(s)
print("toolbar border ok")

# tabs activo border ya transparente ✓ ; window-chrome conserva stroke-light (vidrio sobre wallpaper) intencional
