#!/usr/bin/env python3
import json, pathlib

OUT = pathlib.Path("spec")
SPECS = []
def add(**kw): SPECS.append(kw)

# ---------------- APP SHELL ----------------
add(
name="app-shell", description="Layout de aplicacion completa: chrome + toolbar + sidebar + contenido + statusbar. Grid unico.",
targets={"web":{
"markup":'<div class="cat-appshell"><header class="cat-shell-chrome"></header><div class="cat-shell-toolbar"></div><div class="cat-shell-body"><aside class="cat-sidebar"></aside><main class="cat-shell-main"></main></div><footer class="cat-statusbar"></footer></div>',
"css":["""
.cat-appshell{display:flex;flex-direction:column;width:min(1040px,96vw);height:min(680px,92vh);border-radius:var(--cat-size-radius-window);background:var(--cat-semantic-glass-window,var(--cat-color-surface-glass-window));backdrop-filter:blur(var(--cat-blur-window)) saturate(var(--cat-blur-saturate-window));-webkit-backdrop-filter:blur(var(--cat-blur-window)) saturate(var(--cat-blur-saturate-window));border:1px solid var(--cat-color-stroke-light);box-shadow:var(--cat-elevation-window),inset 0 1px 0 rgba(255,255,255,.65);overflow:hidden;font-family:var(--cat-font-family-ui)}
.cat-shell-chrome{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 12px 4px 14px}
.cat-shell-toolbar{display:flex;align-items:center;gap:2px;margin:2px 14px 0;padding:5px 8px;border-radius:14px 14px 0 0;background:var(--cat-semantic-grad-toolbar);border:1px solid rgba(255,255,255,.42);border-bottom:none;box-shadow:inset 0 1px 0 rgba(255,255,255,.55)}
.cat-shell-body{flex:1;min-height:0;display:grid;grid-template-columns:216px 1fr;margin:0 14px;border-radius:0 0 var(--cat-size-radius-lg) var(--cat-size-radius-lg);background:var(--cat-color-surface-content);border:1px solid var(--cat-color-stroke-light);border-top:none;box-shadow:var(--cat-elevation-panel)}
.cat-shell-body>.cat-sidebar{border-radius:0}
.cat-shell-main{display:flex;flex-direction:column;min-width:0;background:transparent}
.cat-appshell>.cat-statusbar{margin:0 14px 12px;border-radius:0 0 var(--cat-size-radius-md) var(--cat-size-radius-md)}"""]},
"qt":{"widget":"QMainWindow + QSplitter","qss":[]}},
docs={"demos":['<div class="cat-appshell" style="height:auto;min-height:300px"><header class="cat-shell-chrome"><div class="cat-tabs"><button class="cat-tab is-active">Documents</button><button class="cat-tab">Music</button></div></header><div class="cat-shell-toolbar"><span style="font-size:12px;font-weight:600;padding-left:4px">Add New</span></div><div class="cat-shell-body"><aside class="cat-sidebar"><div class="cat-nav-item active">Documents</div><div class="cat-nav-item">Music</div></aside><main class="cat-shell-main"><div class="file-scroll" style="padding:10px 20px;font-size:13px;color:var(--cat-color-ink-mid)">Contenido</div></main></div><footer class="cat-statusbar"><span class="cat-status-title">No file selected</span><span class="cat-status-count">4 folders, 67 files</span></footer></div>']}
)

# ---------------- TREE VIEW ----------------
add(
name="tree-view", description="Arbol jerarquico en contenido (no sidebar). Expand/collapse nativo via details-like con JS minimo opcional.",
targets={"web":{
"markup":'<ul class="cat-tree"><li class="branch open"><div class="t-row"><span class="tw">-</span> Projects</div><ul><li><div class="t-row leaf">catalinas</div></li><li><div class="t-row leaf">kittydrive</div></li></ul></li></ul>',
"css":["""
.cat-tree,.cat-tree ul{list-style:none;margin:0;padding:0;font-size:var(--cat-font-size-base);color:var(--cat-color-ink-hi)}
.cat-tree ul{padding-left:22px;border-left:1px solid var(--cat-color-stroke-softer);margin-left:9px;display:none}
.cat-tree .branch.open>ul{display:block}
.t-row{display:flex;align-items:center;gap:7px;height:28px;padding:0 8px;border-radius:var(--cat-size-radius-xs);cursor:pointer;transition:background var(--cat-motion-fast)}
.t-row:hover{background:var(--cat-color-surface-hover)}
.t-row.leaf{cursor:default}
.tw{width:14px;text-align:center;color:var(--cat-color-ink-faint);font-family:var(--cat-font-family-mono);font-size:11px;user-select:none}
.branch.open>.t-row .tw{transform:none}"""]},
"qt":{"widget":"QTreeView","qss":[
'QTreeView::branch:has-children:closed{image:none}',
'QTreeView::item{height:26px;border-radius:{$size.radius.xs$};padding:2px 6px}',
'QTreeView::item:hover{background:rgba(0,0,0,14)}',
'QTreeView::item:selected{background:{$color.accent.base$};color:white}']}},
docs={"demos":['<ul class="cat-tree" id="tvDemo" style="width:280px" data-cat-tree><li class="branch open"><div class="t-row"><span class="tw">-</span>KittyDrive</div><ul><li><div class="t-row leaf">Projects</div></li><li><div class="t-row leaf">Backups</div></li></ul></li><li class="branch"><div class="t-row"><span class="tw">+</span>Cats</div><ul><li><div class="t-row leaf">michi.jpg</div></li></ul></li></ul>'],
"note":"Toggle con JS del host: click en .branch > .t-row alterna clase open y el signo."}
)

# ---------------- FILTER CHIPS ----------------
add(
name="filter-chips", description="Chips de filtro multi-seleccion con estado activo accent.",
targets={"web":{
"markup":'<div class="cat-chips"><label class="chip active">Documentos<input type="checkbox" checked hidden></label><label class="chip">Presentaciones<input type="checkbox" hidden></label><label class="chip">Carpetas<input type="checkbox" hidden></label></div>',
"css":["""
.cat-chips{display:inline-flex;flex-wrap:wrap;gap:6px;font-family:var(--cat-font-family-ui)}
.chip{position:relative;display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 12px;border-radius:var(--cat-size-radius-pill);border:1px solid var(--cat-color-stroke-input);background:rgba(255,255,255,.45);font:500 var(--cat-font-size-sm) var(--cat-font-family-ui);color:var(--cat-color-ink-mid);cursor:pointer;user-select:none;transition:all var(--cat-motion-fast) var(--cat-motion-ease-out)}
.chip:hover{background:#fff;color:var(--cat-color-ink-hi)}
.chip input{position:absolute;inset:0;opacity:0;margin:0;cursor:pointer}
.chip.active{background:var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base));border-color:transparent;color:#fff;font-weight:600}
.chip input:focus-visible~nothing{}"""]},
"qt":{"widget":"QPushButton checkable","qss":[
'QPushButton[cat="chip"]{border-radius:{$size.radius.pill$};border:1px solid {$color.stroke.input$};background:rgba(255,255,255,120);padding:4px 12px;font-size:{$font.size.sm$};color:{$color.ink.mid$}}',
'QPushButton[cat="chip"]:checked{background:{$color.accent.base$};border-color:transparent;color:white;font-weight:600}']}},
docs={"demos":['<div class="cat-chips" data-cat-chips><label class="chip active">Documentos<input type="checkbox" checked hidden></label><label class="chip">Presentaciones<input type="checkbox" hidden></label><label class="chip">Carpetas<input type="checkbox" hidden></label><label class="chip">Imagenes<input type="checkbox" hidden></label></div>'],
"note":"data-cat-chips activa toggle automatico de .active en catalinas.js"}
)

# ---------------- METER ----------------
add(
name="meter", description="Medidor semantico (disco, RAM): verde/amarillo/rojo segun umbral.",
targets={"web":{
"markup":'<div class="cat-meter warn" data-value="78%"><div class="fill" style="width:78%"></div></div>',
"css":["""
.cat-meter{width:200px;height:5px;border-radius:var(--cat-size-radius-pill);background:rgba(0,0,0,.10);overflow:hidden}
.cat-meter>.fill{height:100%;border-radius:inherit;background:var(--cat-color-success);transition:width var(--cat-motion-slow) var(--cat-motion-ease-out),background var(--cat-motion-med)}
.cat-meter.warn>.fill{background:var(--cat-color-warning)}
.cat-meter.danger>.fill{background:var(--cat-color-danger-base)}
.cat-meter.labeled{position:relative}
.cat-meter-label{display:flex;justify-content:space-between;font-size:var(--cat-font-size-xs);color:var(--cat-color-ink-low);margin-top:4px}"""]},
"qt":{"widget":"QProgressBar","qss":[
'QProgressBar[cat="meterWarn"]::chunk{background:{$color.warning$}}',
'QProgressBar[cat="meterDanger"]::chunk{background:{$color.danger.base$}}']}},
docs={"demos":['<div><div class="cat-meter"><div class="fill" style="width:34%"></div></div><div class="cat-meter-label"><span>Disco</span><span>34%</span></div></div>','<div><div class="cat-meter danger"><div class="fill" style="width:91%"></div></div><div class="cat-meter-label"><span>RAM</span><span>91%</span></div></div>']}
)

# ---------------- FILE CHIP ----------------
add(
name="file-chip", description="Chip de archivo adjunto/subido: icono, nombre, peso, remover.",
targets={"web":{
"markup":'<span class="cat-filechip"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#5f8af5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></svg><span class="fc-name">informe.pdf</span><span class="fc-size">2.4 MB</span><button class="fc-x" aria-label="Quitar">x</button></span>',
"css":["""
.cat-filechip{display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 8px 0 10px;border-radius:var(--cat-size-radius-sm);background:var(--cat-color-surface-card);border:1px solid var(--cat-color-stroke-dark);font-family:var(--cat-font-family-ui)}
.fc-name{font-size:var(--cat-font-size-sm);font-weight:550;color:var(--cat-color-ink-hi);max-width:160px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.fc-size{font-size:var(--cat-font-size-xs);color:var(--cat-color-ink-low)}
.fc-x{background:none;border:none;color:var(--cat-color-ink-low);cursor:pointer;font-size:11px;line-height:1;padding:4px;border-radius:4px}
.fc-x:hover{background:var(--cat-color-surface-hover);color:var(--cat-color-ink-hi)}
.cat-filechip.uploading .fc-name::after{content:" ...";color:var(--cat-color-ink-faint)}"""]},
"qt":{"widget":"QFrame","qss":['QFrame[cat="fileChip"]{background:{$color.surface.card$};border:1px solid {$color.stroke.dark$};border-radius:{$size.radius.sm$}']}},
docs={"demos":['<span class="cat-filechip"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#5f8af5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></svg><span class="fc-name">informe-q4.pdf</span><span class="fc-size">2.4 MB</span><button class="fc-x" aria-label="Quitar">x</button></span> <span class="cat-filechip uploading"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#e8776f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 14h6M9 17h4"/></svg><span class="fc-name">deck-final.pptx</span><span class="fc-size">18 MB</span><button class="fc-x" aria-label="Quitar">x</button></span>']}
)

for s in SPECS:
    (OUT / f"{s['name']}.json").write_text(json.dumps(s, ensure_ascii=False, indent=1))
print(f"{len(SPECS)} specs nuevas")
