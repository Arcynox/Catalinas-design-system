#!/usr/bin/env python3
import json, pathlib

OUT = pathlib.Path("spec")
SPECS = []
def add(**kw): SPECS.append(kw)

# ---------------- AVATAR GROUP ----------------
add(
name="avatar-group", description="Stack de avatares con overlap y contador restante.",
targets={"web":{
"markup":'<div class="cat-avgroup"><span class="cat-avatar">LU</span><span class="cat-avatar">MI</span><span class="cat-avatar">CO</span><span class="cat-avatar more">+5</span></div>',
"css":["""
.cat-avgroup{display:flex}
.cat-avgroup .cat-avatar{width:32px;height:32px;border-radius:50%;background:var(--cat-color-ink-low);color:#fff;display:grid;place-items:center;font:600 var(--cat-font-size-sm) var(--cat-font-family-ui);border:2px solid var(--cat-color-surface-content);margin-left:-8px}
.cat-avgroup .cat-avatar:first-child{margin-left:0}
.cat-avgroup .cat-avatar:nth-child(1){background:var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base))}
.cat-avgroup .cat-avatar:nth-child(2){background:var(--cat-color-violet)}
.cat-avgroup .cat-avatar:nth-child(3){background:var(--cat-color-ppt)}
.cat-avgroup .more{background:var(--cat-color-surface-hover);color:var(--cat-color-ink-mid);font-size:10px}"""]},
"qt":{"widget":"QLabel row","qss":[]}},
docs={"demos":['<div class="cat-avgroup"><span class="cat-avatar">LU</span><span class="cat-avatar">MI</span><span class="cat-avatar">CO</span><span class="cat-avatar more">+5</span></div>']}
)

# ---------------- TIMELINE ----------------
add(
name="timeline", description="Feed de actividad vertical con puntos y linea conectora.",
targets={"web":{
"markup":'<ul class="cat-timeline"><li><span class="dot"></span><div><b>Sincronizacion</b> iniciada<span class="t">hace 2 min</span></div></li><li><span class="dot done"></span><div><b>Backup</b> completado<span class="t">hace 1 h</span></div></li></ul>',
"css":["""
.cat-timeline{list-style:none;margin:0;padding:0;font-size:var(--cat-font-size-base);color:var(--cat-color-ink-mid)}
.cat-timeline li{position:relative;display:flex;gap:12px;padding:0 0 18px 4px}
.cat-timeline li:last-child{padding-bottom:0}
.cat-timeline li::before{content:"";position:absolute;left:8.5px;top:16px;bottom:-2px;width:1.5px;background:var(--cat-color-stroke-dark)}
.cat-timeline li:last-child::before{display:none}
.cat-timeline .dot{flex:none;width:11px;height:11px;margin-top:5px;border-radius:50%;background:var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base));box-shadow:0 0 0 3px var(--cat-color-accent-subtle-b)}
.cat-timeline .dot.done{background:var(--cat-color-success);box-shadow:0 0 0 3px rgba(52,199,89,.15)}
.cat-timeline b{font-weight:600;color:var(--cat-color-ink-hi)}
.cat-timeline .t{display:block;font-size:var(--cat-font-size-xs);color:var(--cat-color-ink-faint);margin-top:1px}"""]},
"qt":{"widget":"(custom)","qss":[]}},
docs={"demos":['<ul class="cat-timeline" style="width:300px"><li><span class="dot"></span><div><b>Sincronizacion iniciada</b> — 12 archivos<span class="t">hace 2 min</span></div></li><li><span class="dot done"></span><div><b>Backup completado</b> — 4.33 GB<span class="t">hace 1 h</span></div></li><li><span class="dot done"></span><div><b>Nuevo device vinculado</b><span class="t">ayer</span></div></li></ul>']}
)

# ---------------- STAT CARD ----------------
add(
name="stat-card", description="KPI card: label, valor grande, delta con direccion.",
targets={"web":{
"markup":'<div class="cat-stat"><span class="label">Ingresos</span><span class="value">$12.4K</span><span class="delta up">+8.2%</span></div>',
"css":["""
.cat-stat{display:flex;flex-direction:column;gap:2px;padding:14px 16px;border-radius:var(--cat-size-radius-md);background:var(--cat-color-surface-card);border:1px solid var(--cat-color-stroke-dark);min-width:130px;font-family:var(--cat-font-family-ui)}
.cat-stat .label{font-size:var(--cat-font-size-xs);font-weight:500;color:var(--cat-color-ink-low)}
.cat-stat .value{font-size:var(--cat-font-size-2xl);font-weight:650;color:var(--cat-color-ink-hi);letter-spacing:-.02em}
.cat-stat .delta{font-size:var(--cat-font-size-xs);font-weight:600}
.cat-stat .delta.up{color:var(--cat-color-success)}
.cat-stat .delta.down{color:var(--cat-color-danger-base)}"""]},
"qt":{"widget":"QFrame","qss":['QFrame[cat="stat"]{background:{$color.surface.card$};border:1px solid {$color.stroke.dark$};border-radius:{$size.radius.md$}}']}},
docs={"demos":['<div style="display:flex;gap:10px"><div class="cat-stat"><span class="label">Ingresos</span><span class="value">$12.4K</span><span class="delta up">+8.2%</span></div><div class="cat-stat"><span class="label">Churn</span><span class="value">2.1%</span><span class="delta down">+0.4%</span></div><div class="cat-stat"><span class="label">Activos</span><span class="value">324</span><span class="delta up">+12</span></div></div>']}
)

# ---------------- RATING ----------------
add(
name="rating", description="Estrellas interactivas CSS-only via radios.",
targets={"web":{
"markup":'<fieldset class="cat-rating"><input type="radio" name="rt" id="r1"><label for="r1"></label><input type="radio" name="rt" id="r2"><label for="r2"></label><input type="radio" name="rt" id="r3"><label for="r3"></label><input type="radio" name="rt" id="r4"><label for="r4"></label><input type="radio" name="rt" id="r5"><label for="r5"></label></fieldset>',
"css":["""
.cat-rating{display:inline-flex;flex-direction:row-reverse;gap:2px;border:none;margin:0;padding:0}
.cat-rating input{position:absolute;opacity:0;width:0;height:0}
.cat-rating label{width:20px;height:20px;cursor:pointer;color:var(--cat-color-stroke-input);transition:color var(--cat-motion-fast),transform var(--cat-motion-fast) var(--cat-motion-ease-out);clip-path:polygon(50% 0%,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%);background:currentColor}
.cat-rating label:hover,.cat-rating label:hover~label{transform:scale(1.15)}
.cat-rating input:checked~label{color:var(--cat-color-warning)}
.cat-rating input:checked+label:hover,.cat-rating label:hover,.cat-rating label:hover~label,
.cat-rating input:checked+label~label{color:var(--cat-color-warning)}
.cat-rating input:checked+label~label:not(:hover)~label:not(:hover){color:var(--cat-color-stroke-input)}
.cat-rating input:focus-visible+label{box-shadow:0 0 0 var(--cat-size-border-focus-ring) var(--cat-semantic-accent-ring)}"""]},
"qt":{"widget":"(custom)","qss":[]}},
docs={"demos":['<fieldset class="cat-rating"><input type="radio" name="rtD" id="rd1"><label for="rd1"></label><input type="radio" name="rtD" id="rd2" checked><label for="rd2"></label><input type="radio" name="rtD" id="rd3"><label for="rd3"></label><input type="radio" name="rtD" id="rd4"><label for="rd4"></label><input type="radio" name="rtD" id="rd5"><label for="rd5"></label></fieldset>'],
"note":"CSS-only: radios en orden inverso + sibling selectors."}
)

# ---------------- KEY-VALUE LIST ----------------
add(
name="key-value-list", description="Lista definicion clave/valor para metadata y propiedades.",
targets={"web":{
"markup":'<dl class="cat-kv"><div><dt>Size</dt><dd>4.33 GB</dd></div><div><dt>Items</dt><dd>67</dd></div><div><dt>Modified</dt><dd>Aug 25, 2026</dd></div></dl>',
"css":["""
.cat-kv{margin:0;display:flex;flex-direction:column;font-size:var(--cat-font-size-base)}
.cat-kv>div{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:7px 2px}
.cat-kv>div+div{border-top:1px solid var(--cat-color-stroke-softer)}
.cat-kv dt{color:var(--cat-color-ink-mid)}
.cat-kv dd{margin:0;color:var(--cat-color-ink-hi);font-weight:500;text-align:right}"""]},
"qt":{"widget":"QFormLayout","qss":[]}},
docs={"demos":['<dl class="cat-kv" style="width:260px"><div><dt>Tamano</dt><dd>4.33 GB</dd></div><div><dt>Elementos</dt><dd>67</dd></div><div><dt>Modificado</dt><dd>Aug 25, 2026</dd></div></dl>']}
)

for s in SPECS:
    (OUT / f"{s['name']}.json").write_text(json.dumps(s, ensure_ascii=False, indent=1))
print(f"{len(SPECS)} specs nuevas")
