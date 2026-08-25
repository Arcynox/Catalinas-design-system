#!/usr/bin/env python3
"""Catalinas Design System — build compiler.

Single source:
  tokens/tokens.json   design tokens (W3C-style)
  spec/*.json          widget specs with per-target templates

Outputs:
  web/catalinas.css    all widget css (token vars resolved as var())
  web/catalinas.js     behaviors collected from specs + core helpers
  qt/catalinas.qss     Qt stylesheet ({$path$} placeholders -> literal values)
  qt/theme.py          tokens as Python dict + accessor
  docs/widgets.js      manifest for the living styleguide

Pure stdlib. Run: python3 build.py [--check]
"""
import argparse
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_extra import emit_wc, emit_swift, emit_compose, emit_tokens_md
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_extra import emit_wc, emit_swift, emit_compose, emit_tokens_md

ALL_TARGETS = ["css", "js", "qss", "py", "react", "flutter", "tailwind",
               "flat", "docs", "tokens-css", "scss", "mjs", "dtcg", "snippets", "api", "rtl", "vue", "wc", "swift", "compose", "tokens-md"]
TARGETS_ORDER = ["Web CSS", "Web JS", "React", "Vue 3", "Web Components", "Qt",
                 "Flutter", "SwiftUI", "Compose", "Tailwind", "Figma DTCG", "Flat JSON"]
argp = argparse.ArgumentParser()
argp.add_argument("--targets", default="all",
                  help="coma-separado: " + ",".join(ALL_TARGETS))
argp.add_argument("--watch", action="store_true",
                  help="recompila cuando cambian tokens/ o spec/")
args_cli = argp.parse_args()

def _latest_mtime():
    latest = 0
    for d in ("tokens", "spec"):
        dd = Path(__file__).resolve().parent.parent / d
        for f in dd.glob("*.*"):
            latest = max(latest, f.stat().st_mtime)
    return latest
SELECTED = ALL_TARGETS if args_cli.targets == "all" else [x.strip() for x in args_cli.targets.split(",")]
wants = lambda name: name in SELECTED

ROOT = Path(__file__).resolve().parent.parent
T = json.loads((ROOT / "tokens" / "tokens.json").read_text())

# ---------- token resolution ----------

def resolve(node):
    if isinstance(node, dict):
        return {k: resolve(v) for k, v in node.items() if not k.startswith("$")}
    if isinstance(node, str):
        m = re.fullmatch(r"\{([\w.\-]+)\}", node.strip())
        if m:
            cur = T
            for part in m.group(1).split("."):
                cur = cur[part]
            return resolve(cur)
        return node
    return node

R = resolve(T)

def flat(prefix, node, out):
    for k, v in node.items():
        key = f"{prefix}-{k}" if prefix else k
        if isinstance(v, dict):
            flat(key, v, out)
        else:
            out[key] = v

FLAT = {}
flat("", R, FLAT)

def var_name(path):  # color.ink.hi -> --cat-color-ink-hi
    return "--cat-" + path.replace(".", "-")

def get(path):
    cur = R
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            raise KeyError(f"token not found: {path}")
        cur = cur[part]
    return cur

# ---------- placeholder substitution for non-css targets ----------
PLACEHOLDER = re.compile(r"\{\$([\w.\-]+)\$\}")

def sub_qss(text):
    def repl(m):
        return str(get(m.group(1)))
    return PLACEHOLDER.sub(repl, text)

# validate var(--cat-*) references used in web css actually exist
VARREF = re.compile(r"var\((--cat-[\w\-]+)")

# ---------- load specs ----------
specs = []
for f in sorted((ROOT / "spec").glob("*.json")):
    specs.append(json.loads(f.read_text()))

# ---------- emit CSS ----------
css_parts = [
    "/* Catalinas Design System — generated, do not edit",
    "   source: tokens/tokens.json + spec/*.json */",
    ":root {"]
for k, v in FLAT.items():
    css_parts.append(f"  {var_name(k)}: {v};")
css_parts.append("}")
css_parts.append("")

errors = []
VARSET = {var_name(k) for k in FLAT}
for sp in specs:
    w = sp["targets"].get("web", {})
    for rule in w.get("css", []):
        for ref in VARREF.findall(rule):
            if ref not in VARSET:
                errors.append(f"[{sp['name']}] unknown token in: {ref}")
        css_parts.append(rule.strip())
    css_parts.append("")

if errors:
    print("\n".join(errors))
    sys.exit(1)

(ROOT / "web" / "catalinas.css").write_text("\n".join(css_parts) + "\n")

# ---------- themes ----------
theme_css = []
for tname, overrides in (T.get("$themes") or {}).items():
    theme_css.append(f'[data-theme="{tname}"] {{')
    for path, val in sorted(overrides.items()):
        cur = T
        try:
            for part in path.split("."):
                cur = cur[part]
        except (KeyError, TypeError):
            errors.append(f"[theme {tname}] unknown token path: {path}")
            continue
        theme_css.append(f"  {var_name(path)}: {val};")
    theme_css.append("}")
    theme_css.append("")

# ---------- utilities (estándar DS: escala de tokens -> helpers) ----------
util = ["/* utilities */"]
SPACE = R["size"]["space"]
RAD = R["size"]["radius"]
FS = R["font"]["size"]
FW = R["font"]["weight"]
for k, v in SPACE.items():
    util += [
        f".cat-p-{k}{{padding:{v}}}", f".cat-px-{k}{{padding-left:{v};padding-right:{v}}}",
        f".cat-py-{k}{{padding-top:{v};padding-bottom:{v}}}",
        f".cat-m-{k}{{margin:{v}}}", f".cat-mt-{k}{{margin-top:{v}}}", f".cat-mb-{k}{{margin-bottom:{v}}}",
        f".cat-gap-{k}{{gap:{v}}}"]
for k, v in RAD.items():
    if k == "pill":
        continue
    util.append(f".cat-rounded-{k}{{border-radius:{v}}}")
util.append(f".cat-rounded-full{{border-radius:{RAD['pill']}}}")
for k, v in FS.items():
    util.append(f".cat-text-{k}{{font-size:{v}}}")
for k, v in FW.items():
    util.append(f".cat-weight-{k}{{font-weight:{v}}}")
for tone in ("hi", "mid", "low", "faint"):
    util.append(f".cat-ink-{tone}{{color:var(--cat-color-ink-{tone})}}")
util += [".cat-flex{display:flex}", ".cat-items-center{align-items:center}",
         ".cat-justify-between{justify-content:space-between}", ".cat-w-full{width:100%}",
         ".cat-truncate{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}"]

util += [
 '[data-density="compact"]{--cat-size-control-h-sm:22px;--cat-size-control-h-md:26px;--cat-size-control-h-lg:30px;--cat-semantic-row-height:32px}',
 '[data-density="cozy"]{--cat-size-control-h-sm:24px;--cat-size-control-h-md:30px;--cat-size-control-h-lg:36px;--cat-semantic-row-height:38px}',
 '[data-density="comfortable"]{--cat-size-control-h-sm:28px;--cat-size-control-h-md:34px;--cat-size-control-h-lg:40px;--cat-semantic-row-height:44px}']

util += ["@media (prefers-reduced-motion: reduce){*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important;scroll-behavior:auto!important}}"]

with open(ROOT / "web" / "catalinas.css", "a") as f:
    f.write("\n".join(theme_css + util) + "\n")

# ---------- emit JS ----------
CORE_JS = r"""(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];

  function closeAllMenus(except) {
    $$("[data-cat-menu-open]").forEach(m => {
      if (m !== except) {
        delete m.dataset.catMenuOpen;
        $(".cat-menu", m).classList.remove("open");
        const b = $("[data-cat-menu-trigger]", m);
        if (b) b.setAttribute("aria-expanded", "false");
      }
    });
  }

  document.addEventListener("click", e => {
    const trg = e.target.closest("[data-cat-menu-trigger]");
    const wrap = trg && trg.closest("[data-cat-menu]");
    closeAllMenus(wrap);
    if (trg && wrap) {
      const menu = $(".cat-menu", wrap);
      const open = menu.classList.toggle("open");
      if (open) wrap.dataset.catMenuOpen = "1";
      else delete wrap.dataset.catMenuOpen;
      trg.setAttribute("aria-expanded", String(open));
    } else {
      closeAllMenus();
    }
  });

  document.addEventListener("keydown", e => { if (e.key === "Escape") closeAllMenus(); });

  $$("[data-cat-tabs]").forEach(tabs => {
    tabs.addEventListener("click", e => {
      const tab = e.target.closest("[data-cat-tab]");
      if (!tab || !tabs.contains(tab)) return;
      $$("[data-cat-tab]", tabs).forEach(t => {
        t.classList.toggle("is-active", t === tab);
        t.setAttribute("aria-selected", String(t === tab));
      });
      tabs._moveGlider && tabs._moveGlider();
      const group = tabs.dataset.catTabs;
      if (group) {
        $$(`[data-cat-panel-for="${group}"]`).forEach(p =>
          p.hidden = p.getAttribute("data-cat-panel") !== tab.dataset.catTab);
      }
    });
  });

  $$("[data-cat-dismiss]").forEach(btn => {
    btn.addEventListener("click", () => {
      const target = btn.closest(btn.dataset.catDismiss);
      if (target) target.classList.add("cat-leaving");
    });
  });

  document.addEventListener("transitionend", e => {
    if (e.target.classList && e.target.classList.contains("cat-leaving")) e.target.remove();
  });

  $$("[data-cat-selectable]").forEach(list => {
    list.addEventListener("click", e => {
      const row = e.target.closest(".cat-row");
      if (!row || !list.contains(row)) return;
      if (!e.ctrlKey && !e.metaKey) $$(".is-selected", list).forEach(r => r.classList.remove("is-selected"));
      row.classList.toggle("is-selected", !row.classList.contains("is-selected") || e.ctrlKey || e.metaKey);
      const sel = $$(".is-selected", list);
      const bar = document.querySelector(list.dataset.catStatusbar || ".cat-statusbar");
      if (!bar) return;
      const t = $(".cat-status-title", bar), m = $(".cat-status-meta", bar);
      if (!t) return;
      if (sel.length === 0) { t.textContent = "No file selected"; m.textContent = ""; }
      else if (sel.length === 1) { t.textContent = sel[0].dataset.name || ""; m.textContent = sel[0].dataset.meta || ""; }
      else { t.textContent = sel.length + " items selected"; m.textContent = ""; }
    });
  });

  // sliding selection: tabs + segmented
  function attachGlider(container, itemSel, activeCls) {
    const gl = document.createElement("span");
    gl.className = "cat-glider";
    container.appendChild(gl);
    function move(anim) {
      const act = container.querySelector(itemSel + "." + activeCls) || container.querySelector(itemSel);
      if (!act) return;
      gl.style.width = act.offsetWidth + "px";
      gl.style.transform = "translateX(" + act.offsetLeft + "px)";
      gl.style.opacity = "1";
      if (!anim) { const t = gl.style.transition; gl.style.transition = "none"; void gl.offsetWidth; gl.style.transition = t; }
    }
    requestAnimationFrame(() => move(false));
    container._moveGlider = () => move(true);
    addEventListener("resize", () => move(false));
  }

  $$("[data-cat-tabs]").forEach(t => attachGlider(t, "[data-cat-tab]", "is-active"));

  $$("[data-cat-segmented]").forEach(seg => {
    attachGlider(seg, ".seg-btn", "is-active");
    seg.addEventListener("click", e => {
      const b = e.target.closest(".seg-btn");
      if (!b || !seg.contains(b)) return;
      $$(".seg-btn", seg).forEach(x => {
        x.classList.toggle("is-active", x === b);
        x.setAttribute("aria-pressed", String(x === b));
      });
      seg._moveGlider && seg._moveGlider();
    });
  });

  $$("[data-cat-rating]").forEach(r => {
    const btns = $$(".star", r);
    let val = +(r.dataset.value || 0);
    const paint = () => btns.forEach((b, i) => b.classList.toggle("on", i < val));
    btns.forEach((b, i) => {
      b.addEventListener("mouseenter", () => btns.forEach((x, j) => x.classList.toggle("on", j <= i)));
      b.addEventListener("mouseleave", paint);
      b.addEventListener("click", () => { val = i + 1; r.dataset.value = val; paint(); });
    });
    paint();
  });

  document.addEventListener("click", e => {
    const b = e.target.closest(".cat-swatch");
    if (!b) return;
    const root = b.closest("[data-cat-colors]");
    if (!root) return;
    const rs = document.documentElement.style;
    $$(".cat-swatch", root).forEach(x => x.classList.toggle("active", x === b));
    if (b.dataset.color){
      rs.setProperty("--cat-semantic-accent-dynamic", b.dataset.color);
      rs.setProperty("--cat-semantic-accent-ring", b.dataset.color + "29");
    } else {
      rs.removeProperty("--cat-semantic-accent-dynamic");
      rs.removeProperty("--cat-semantic-accent-ring");
    }
  });

  $$("[data-cat-chips]").forEach(group => {
    group.addEventListener("change", e => {
      const chip = e.target.closest(".chip");
      if (chip) chip.classList.toggle("active", e.target.checked);
    });
  });

  $$("label.cat-dropzone input[type=file]").forEach(inp => {
    inp.addEventListener("change", () => {
      const n = inp.files.length;
      const b = $("b", inp.closest(".cat-dropzone"));
      if (b && n) b.textContent = n === 1 ? "1 archivo listo" : n + " archivos listos";
    });
    const zone = inp.closest(".cat-dropzone");
    ["dragover","dragenter"].forEach(ev => zone.addEventListener(ev, e => { e.preventDefault(); zone.classList.add("over"); }));
    ["dragleave","drop"].forEach(ev => zone.addEventListener(ev, () => zone.classList.remove("over")));
  });

  // ---------- toast queue ----------
  let toastZone = $(".cat-toasts");
  if (!toastZone) {
    toastZone = document.createElement("div");
    toastZone.className = "cat-toasts";
    document.body.appendChild(toastZone);
  }
  function toast(opts) {
    const o = typeof opts === "string" ? { title: opts } : (opts || {});
    const el = document.createElement("div");
    el.className = "cat-toast " + (o.tone && o.tone !== "info" ? o.tone : "");
    el.innerHTML = '<span class="t-icon"></span><div style="flex:1;min-width:0">'
      + '<b style="font-size:12.5px;display:block">' + (o.title || "") + '</b>'
      + (o.message ? '<div style="font-size:11px;color:var(--cat-color-ink-mid)">' + o.message + '</div>' : "")
      + '</div><button class="t-close" aria-label="Cerrar">x</button>';
    el.querySelector(".t-close").addEventListener("click", () => dismiss(el));
    toastZone.appendChild(el);
    if (o.timeout !== 0) setTimeout(() => dismiss(el), o.timeout || 4200);
    return el;
  }
  function dismiss(el){ el.classList.add("cat-leaving"); }

  // ---------- command palette (Ctrl+K) ----------
  function palette(items, opts) {
    const o = opts || {};
    let overlay = $(".cat-cmdk-overlay");
    if (!overlay) {
      overlay = document.createElement("div");
      overlay.className = "cat-cmdk-overlay";
      overlay.innerHTML = '<div class="cat-cmdk" role="dialog" aria-modal="true">'
        + '<input class="cmdk-input" placeholder="' + (o.placeholder || "Buscar...") + '">'
        + '<div class="cmdk-list" role="listbox"></div>'
        + '<div class="cmdk-foot"><span class="menu-kbd">ESC cerrar</span></div></div>';
      document.body.appendChild(overlay);
      overlay.addEventListener("click", e => { if (e.target === overlay) close(); });
      const inp = $(".cmdk-input", overlay);
      inp.addEventListener("input", () => render(inp.value.toLowerCase()));
      document.addEventListener("keydown", ev => {
        if (!overlay.open) return;
        if (ev.key === "Escape") close();
        if (ev.key === "ArrowDown" || ev.key === "ArrowUp") {
          ev.preventDefault();
          const rows = $$(".cmdk-item:not([hidden])", overlay);
          if (!rows.length) return;
          let i = rows.findIndex(r => r.classList.contains("is-active"));
          i = ev.key === "ArrowDown" ? (i + 1) % rows.length : (i - 1 + rows.length) % rows.length;
          rows.forEach((r, j) => r.classList.toggle("is-active", j === i));
          rows[i].scrollIntoView({ block: "nearest" });
        }
        if (ev.key === "Enter") {
          const act = $(".cmdk-item.is-active", overlay);
          if (act) { close(); act.dataset.onSelect && eval(act.dataset.onSelect); }
        }
      });
      function render(q) {
        $$(".cmdk-item", overlay).forEach(it => {
          const hit = !q || it.textContent.toLowerCase().includes(q);
          it.hidden = !hit;
        });
        const vis = $$(".cmdk-item:not([hidden])", overlay);
        vis.forEach((r, j) => r.classList.toggle("is-active", j === 0));
      }
      overlay._render = render;
    }
    const list = $(".cmdk-list", overlay);
    list.innerHTML = "";
    items.forEach(it => {
      const b = document.createElement("button");
      b.type = "button"; b.className = "cat-menu-item cmdk-item"; b.setAttribute("role","option");
      b.innerHTML = '<span>' + it.label + '</span>' + (it.kbd ? '<span class="menu-kbd">' + it.kbd + '</span>' : '');
      b.addEventListener("click", () => { close(); it.onSelect && it.onSelect(); });
      list.appendChild(b);
    });
    overlay.classList.add("open"); overlay.open = true;
    setTimeout(() => $(".cmdk-input", overlay).focus(), 20);
    overlay._render("");
    function close(){ overlay.classList.remove("open"); overlay.open = false; }
    return { close };
  }

  document.addEventListener("keydown", e => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      const host = $("[data-cat-command]");
      if (host) {
        const items = $$("[data-cat-cmd]", host).map(b => ({
          label: b.dataset.catCmd,
          kbd: b.dataset.kbd,
          onSelect: () => b.click()
        }));
        window.Catalinas.palette(items, { placeholder: host.dataset.catCommand });
      } else {
        window.Catalinas.palette([{ label: "Sin comandos registrados" }]);
      }
    }
  });

  // ---------- sparklines ----------
  $$("[data-cat-spark]").forEach(el => {
    const values = (el.dataset.catSpark || "").split(",").map(Number).filter(v => !isNaN(v));
    if (values.length < 2) return;
    const kind = el.dataset.sparkType || "line";
    const w = +(el.dataset.width || 120), h = +(el.dataset.height || 32);
    const max = Math.max(...values), min = Math.min(...values);
    const rng = max - min || 1;
    const pts = values.map((v, i) => [(i / (values.length - 1)) * w, h - ((v - min) / rng) * (h - 4) - 2]);
    let shape = "";
    if (kind === "bars") {
      const bw = w / values.length * 0.6, gap = w / values.length * 0.4;
      shape = pts.map((p, i) =>
        `<rect x="${(i * w / values.length + gap / 2).toFixed(1)}" y="${p[1]}" width="${bw.toFixed(1)}" height="${(h - p[1]).toFixed(1)}" rx="1.5"/>`).join("");
    } else {
      shape = `<polyline points="${pts.map(p => p[0].toFixed(1) + "," + p[1].toFixed(1)).join(" ")}"/>`;
    }
    const stroke = 'stroke="currentColor" fill="' + (kind === "bars" ? "currentColor" : "none") + '"';
    el.innerHTML = `<svg width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" ${stroke} stroke-width="2" stroke-linecap="round" stroke-linejoin="round">${shape}</svg>`;
  });

  // ---------- form validation ----------
  $$("[data-cat-validate]").forEach(form => {
    form.setAttribute("novalidate", "");
    form.addEventListener("submit", e => {
      let bad = 0;
      $$("[required], [data-cat-type]", form).forEach(f => {
        const wrap = f.closest(".cat-field");
        const msgEl = wrap && wrap.querySelector(".field-msg");
        let err = "";
        const v = f.value.trim();
        if (f.required && !v) err = f.dataset.msgRequired || "Campo requerido";
        else if (v && f.dataset.catType === "email" && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v)) err = f.dataset.msgInvalid || "Formato invalido";
        else if (v && f.minLength > 0 && v.length < f.minLength) err = "Minimo " + f.minLength + " caracteres";
        if (wrap) wrap.classList.toggle("is-error", !!err);
        if (msgEl) msgEl.textContent = err;
        else if (err && wrap) { const m = document.createElement("span"); m.className = "field-msg"; m.textContent = err; wrap.appendChild(m); }
        if (err) bad++;
      });
      if (bad) e.preventDefault();
      form.dispatchEvent(new CustomEvent("cat:valid", { detail: { valid: !bad }, cancelable: true }));
    });
  });

  window.Catalinas = { $, $$, toast, palette };
})();"""

js_parts = ["/* Catalinas Design System — generated behaviors, do not edit */", CORE_JS]
for sp in specs:
    code = sp["targets"].get("web", {}).get("js", "").strip()
    if code:
        js_parts.append(f"/* {sp['name']} */")
        js_parts.append(code)

(ROOT / "web" / "catalinas.js").write_text("\n\n".join(js_parts) + "\n")

# ---------- emit QSS ----------
qss_parts = ["/* Catalinas Design System — generated Qt stylesheet, do not edit */", ""]
qt_meta = []
for sp in specs:
    qt = sp["targets"].get("qt", {})
    if not qt:
        continue
    qt_meta.append({"name": sp["name"], **{k: v for k, v in qt.items() if k != "qss"}})
    for rule in qt.get("qss", []):
        qss_parts.append(sub_qss(rule.strip()))
        qss_parts.append("")

(ROOT / "qt" / "catalinas.qss").write_text("\n".join(qss_parts))

# ---------- emit theme.py ----------
def py_value(v):
    if isinstance(v, bool):
        return "True" if v else "False"
    if isinstance(v, (int, float)):
        return repr(v)
    return repr(str(v))

lines = [
    '"""Catalinas Design System — generated Qt theme module, do not edit."""',
    "", "TOKENS = {"]
def py_dict(node, indent=1):
    pad = "    " * indent
    for k, v in node.items():
        key = k.replace("-", "_")
        if isinstance(v, dict):
            lines.append(f'{pad}"{key}": {{')
            py_dict(v, indent + 1)
            lines.append(f"{pad}}},")
        else:
            lines.append(f'{pad}"{key}": {py_value(v)},')
py_dict(R)
lines += ["}", "",
          "QSS_FILE = __file__.replace('theme.py', 'catalinas.qss')", "",
          "def get(path, default=None):",
          '    """TOKENS.get("color.accent.base") -> value"""',
          "    cur = TOKENS",
          "    for part in path.split('.'):",
          "        if not isinstance(cur, dict) or part not in cur:",
          "            return default",
          "        cur = cur[part]",
          "    return cur", "",
          "def load_qss(app):",
          '    """app.setStyleSheet(open(QSS_FILE).read()) helper"""',
          "    from pathlib import Path",
          "    app.setStyleSheet(Path(QSS_FILE).read_text())"]
(ROOT / "qt" / "theme.py").write_text("\n".join(lines) + "\n")

# ---------- emit docs manifest ----------
manifest = []
for sp in specs:
    entry = {k: v for k, v in sp.items() if k != "targets"}
    entry["has_js"] = bool(sp["targets"].get("web", {}).get("js", "").strip())
    docs = sp.get("docs", {})
    entry["demos"] = docs.get("demos", [sp["targets"].get("web", {}).get("markup", "")])
    manifest.append(entry)

docs_js = ("/* generated */\nwindow.CATALINAS = "
           + json.dumps({"version": T["$version"],
                         "widgets": manifest, "targets": ["Web CSS", "React", "Qt", "Flutter", "Tailwind", "Flat JSON"]}, ensure_ascii=False, indent=1))
(ROOT / "docs" / "widgets.js").write_text(docs_js + "\n")
(ROOT / "qt" / "theme.py").write_text("\n".join(lines) + "\n")

# ---------- React adapters ----------
REACT_HEADER = '''/* Catalinas Design System — React bindings (generated)
   Uso: <CatButton variant="danger">Eliminar</CatButton>
   Requiere catalinas.css en la app. *''' + "/\n\n"

REACT = {
"button": '''export function CatButton({ variant = "primary", size, icon, loading, className = "", children, ...p }) {
  const cls = ["cat-btn", variant, size && size !== "md" ? size : "", loading ? "loading" : "", className].filter(Boolean).join(" ");
  return <button {...p} className={cls}>{icon}{children}</button>;
}''',
"input": '''export function CatField({ label, icon, error, textarea, select, options = [], className = "", ...p }) {
  return (
    <div className={"cat-field" + (error ? " is-error" : "") + " " + className}>
      {label && <label className="cat-label">{label}</label>}
      <div className={"cat-input" + (icon ? " has-icon" : "")}>
        {icon && <span className="cat-icon">{icon}</span>}
        {textarea ? <textarea className="el" {...p} />
          : select ? <select className="el" {...p}>{options.map(o => <option key={o}>{o}</option>)}</select>
          : <input className="el" {...p} />}
      </div>
      {error && <span className="field-msg">{error}</span>}
    </div>
  );
}''',
"switch": '''export function CatSwitch({ defaultChecked, disabled, onChange }) {
  return (
    <label className="cat-switch">
      <input type="checkbox" defaultChecked={defaultChecked} disabled={disabled} onChange={onChange} />
      <span className="track" />
    </label>
  );
}''',
"checkbox-radio": '''export function CatCheck({ children, ...p }) {
  return <label className="cat-check"><input type="checkbox" {...p} /><span className="box" />{children}</label>;
}
export function CatRadio({ name, children, ...p }) {
  return <label className="cat-radio"><input type="radio" name={name} {...p} /><span className="box" />{children}</label>;
}''',
"slider": '''export function CatSlider({ accent, ...p }) {
  return <input type="range" className={"cat-slider" + (accent ? " accent" : "")} {...p} />;
}''',
"tabs": '''export function CatTabs({ tabs, groupId }) {
  return (
    <div className="cat-tabs" data-cat-tabs={groupId || undefined} role="tablist">
      {tabs.map((t, i) => (
        <button key={i} role="tab" aria-selected={i === 0}
          data-cat-tab={t.id}
          className={"cat-tab" + (i === 0 ? " is-active" : "")}>{t.label}</button>
      ))}
    </div>
  );
}''',
"badge-tooltip-kbd-avatar": [
  '''export function CatBadge({ tone, dot, children }) {
  return <span className={"cat-badge" + (tone ? " " + tone : "")}>{dot && <span className="dot" />}{children}</span>;
}''',
  '''export function CatTooltip({ label, children }) {
  return <span data-cat-tooltip={label}>{children}</span>;
}''',
  '''export function Kbd({ children }) { return <kbd className="cat-kbd">{children}</kbd>; }''',
  '''export function CatAvatar({ initials, src, online }) {
  return (
    <span className="cat-avatar">
      {src ? <img src={src} alt="" /> : initials}
      {online && <span className="presence" />}
    </span>
  );
}''',
],
"card-toast": [
  '''export function CatCard({ level = "content", className = "", children, ...p }) {
  return <div {...p} className={"cat-card " + level + " " + className}>{children}</div>;
}''',
  '''export function CatToasts({ children }) { return <div className="cat-toasts">{children}</div>; }
export function CatToast({ tone = "info", title, onClose }) {
  return (
    <div className={"cat-toast " + (tone === "info" ? "" : tone)}>
      <span className="t-icon" />
      <div style={{ flex: 1 }}><b>{title}</b></div>
      {onClose && <button className="t-close" data-cat-dismiss=".cat-toast" onClick={onClose}>x</button>}
    </div>
  );
}''',
],
"alert-banner": [
  '''const I = {
  info: <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4"><circle cx="12" cy="12" r="9" /><path d="M12 8h.01M12 11v5" strokeLinecap="round" /></svg>,
  success: <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.8" strokeLinecap="round"><path d="M5 13l4 4 10-10" /></svg>,
  warning: <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round"><path d="M12 4L2 20h20z" /><path d="M12 10v4m0 3h.01" /></svg>,
  danger: <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4" strokeLinecap="round"><path d="M6 6l12 12M18 6L6 18" /></svg>,
};
export function CatAlert({ tone = "info", title, message, onClose }) {
  return (
    <div className={"cat-alert " + tone}>
      <span className="a-icon" aria-hidden>{I[tone] || I.info}</span>
      <div className="a-body"><b>{title}</b><span>{message}</span></div>
      {onClose && <button className="t-close" data-cat-dismiss=".cat-alert" onClick={onClose}>x</button>}
    </div>
  );
}''',
],
"segmented": [
  '''export function CatSegmented({ name, options }) {
  return (
    <div className="cat-segmented">
      {options.map((o, i) => (
        <label key={i}><input type="radio" name={name} defaultChecked={i === 0} /><span>{o}</span></label>
      ))}
    </div>
  );
}''',
],
}

react_parts = [REACT_HEADER]
for sp in specs:
    code = REACT.get(sp["name"])
    if not code:
        continue
    items = code if isinstance(code, list) else [code]
    react_parts.append(f"// {sp['name']}\n" + "\n\n".join(items))
react_parts.append("\nexport const tokens = window.CATALINAS_TOKENS; // si cargas docs/tokens.js")
(ROOT / "web" / "catalinas.jsx").write_text("\n\n".join(react_parts) + "\n")

# ---------- Vue 3 adapter ----------
VUE_HEADER = '''/* Catalinas Design System - Vue 3 bindings (generated)
   Requiere Vue 3 global. Uso:
   Object.assign(app.components, CatalinasVue) */

'''

VUE = {
    'button': [
        '''export const CatButton = (props, ctx) => h('button', {
  class: ['cat-btn', props.variant, props.size !== 'md' ? props.size : null,
          props.loading ? 'loading' : null],
  disabled: props.disabled,
  onClick: () => ctx.emit('click')
}, [props.icon, ctx.slots.default ? ctx.slots.default() : null]);''',
    ],
    'switch': [
        '''export const CatSwitch = (props, ctx) => h('label', { class: 'cat-switch' }, [
  h('input', { type: 'checkbox', checked: props.checked, disabled: props.disabled,
    onChange: e => ctx.emit('change', e.target.checked) }),
  h('span', { class: 'track' })
]);''',
    ],
    'badge-tooltip-kbd-avatar': [
        '''export const CatBadge = (props) => h('span', { class: 'cat-badge' + (props.tone ? ' ' + props.tone : '') },
  [props.dot ? h('span', { class: 'dot' }) : null], props.default);''',
        '''export const CatAvatar = (props) => h('span', { class: 'cat-avatar' },
  props.src ? h('img', { src: props.src }) : props.initials,
  props.online ? h('span', { class: 'presence' }) : null);''',
    ],
    'card-toast': [
        '''export const CatCard = (props) => h('div', { class: 'cat-card ' + (props.level || '') }, props.default);''',
        '''export const CatToast = (props, ctx) => h('div', { class: 'cat-toast ' + (props.tone === 'info' ? '' : props.tone) }, [
  h('span', { class: 't-icon' }),
  h('div', { style: 'flex:1' }, [h('b', props.title)]),
  h('button', { class: 't-close', onClick: () => ctx.emit('close') }, 'x')
]);''',
    ],
}

vue_parts = [VUE_HEADER]
for sp in specs:
    code = VUE.get(sp['name'])
    if not code: continue
    items = code if isinstance(code, list) else [code]
    vue_parts.append('// ' + sp['name'] + '\n\n' + '\n\n'.join(items))
(ROOT / 'web' / 'catalinas-vue.js').write_text('\n\n'.join(vue_parts) + '\n')
try: written.append('web/catalinas-vue.js')
except NameError: pass

# ---------- Flutter theme ----------
def dart_color(v):
    v = v.strip()
    if v.startswith("#"):
        h = v[1:]
        if len(h) == 3: h = "".join(c*2 for c in h)
        a = "FF" if len(h) <= 6 else h[6:8]
        rgb = h[:6]
        return f"Color(0x{a}{rgb})"
    import re as _re
    m = _re.match(r"rgba?\(([^)]+)\)", v)
    if m:
        parts = [float(x) for x in m.group(1).split(",")]
        r,g,b = [int(x) for x in parts[:3]]
        a = int(parts[3]*255) if len(parts) > 3 else 255
        return f"Color.fromARGB({a}, {r}, {g}, {b})"
    return None

colors = {}
def walk_colors(node, pre):
    for k, v in node.items():
        kk = k.replace("-", "_")
        if isinstance(v, dict):
            walk_colors(v, pre + kk + "_")
        elif isinstance(v, str):
            c = dart_color(v)
            if c: colors[pre + kk] = c
walk_colors(R.get("color", {}), "")

dart_lines = [
    "// Catalinas Design System — generated Flutter theme (do not edit)",
    "import 'package:flutter/material.dart';", "",
    "class CatColors {",
]
for k, v in sorted(colors.items()):
    dart_lines.append(f"  static const {k} = {v};")
dart_lines += ["}", "",
    "class CatRadius {",
]
for k, v in R["size"]["radius"].items():
    num = float(v.replace("px","").replace("999","100"))
    dart_lines.append(f"  static double {k.replace('-','_')} = {num};")
dart_lines += ["}", "",
    "class CatText {",
    "  static TextTheme apply(BuildContext c) => Theme.of(c).textTheme.copyWith(",
    "    bodyMedium: TextStyle(fontSize: 13, fontFamily: 'SF Pro Text', color: CatColors.ink_hi),",
    "    labelSmall: TextStyle(fontSize: 11, letterSpacing: .4, color: CatColors.ink_low),",
    "    titleLarge: TextStyle(fontSize: 17, fontWeight: FontWeight.w600, color: CatColors.ink_hi),",
    "  );",
    "}", "",
    "ThemeData catLightTheme() => ThemeData(",
    "  useMaterial3: true,",
    "  scaffoldBackgroundColor: const Color(0xFFF2F4FA),",
    f"  colorScheme: ColorScheme.light(primary: {colors.get('accent_base','Color(0xFF5E9EFF)')}, secondary: {colors.get('violet','Color(0xFFA78BFA)')}, error: {colors.get('danger_base','Color(0xFFE8382D)')}),",
    "  fontFamily: 'SF Pro Text',",
    ");"]
(ROOT / "flutter").mkdir(exist_ok=True)
(ROOT / "flutter" / "catalinas_theme.dart").write_text("\n".join(dart_lines) + "\n")

# ---------- Tailwind preset ----------
tw = {
  "$schema": "https://cdn.tailwindcss.com",
  "theme": {
    "extend": {
      "colors": {"cat-" + k[len("color-"):]: "var(--cat-" + k + ")" for k in FLAT if k.startswith("color-")},
      "borderRadius": {"cat-" + k[len("radius-"):]: "var(--cat-size-radius-" + k[len("radius-"):] + ")" for k in FLAT if k.startswith("size-radius-")},
      "fontSize": {"cat-" + k[len("size-"):]: "var(--cat-font-size-" + k[len("size-"):] + ")" for k in FLAT if k.startswith("font-size-")},
      "fontFamily": {"catui": "var(--cat-font-family-ui)"},
      "boxShadow": {"cat-window": "var(--cat-elevation-window)", "cat-menu": "var(--cat-elevation-menu)", "cat-float": "var(--cat-elevation-float)"},
    }
  }
}
(ROOT / "tailwind").mkdir(exist_ok=True)
(ROOT / "tailwind" / "catalinas.tw.js").write_text(
    "/* Catalinas preset para Tailwind — usar como presets: [require('./catalinas.tw')] o ESM import */\n"
    + "window.CATALINAS_TW = " + json.dumps(tw, indent=1) + ";\n")

# ---------- flat tokens interop ----------
(ROOT / "tokens" / "tokens.flat.json").write_text(
    json.dumps({var_name(k): v for k, v in sorted(FLAT.items())}, ensure_ascii=False, indent=1))

tokens_js = ("/* generated */\nwindow.CATALINAS_TOKENS = "
             + json.dumps(FLAT, ensure_ascii=False, indent=1))
(ROOT / "docs" / "tokens.js").write_text(tokens_js + "\n")

# ================= EXTRA EXPORTS =================

written = []

if wants("tokens-css"):
    tok_css = ["/* Catalinas tokens-only — generated */", ":root {"]
    for k, v in sorted(FLAT.items()):
        tok_css.append(f"  {var_name(k)}: {v};")
    tok_css.append("}")
    (ROOT / "web" / "catalinas.tokens.css").write_text("\n".join(tok_css) + "\n")
    written.append("web/catalinas.tokens.css")

if wants("scss"):
    scss = ["// Catalinas Design System — generated SCSS variables", ""]
    for k, v in sorted(FLAT.items()):
        scss.append(f"$cat-{k}: {v};")
    scss += ["", "$cat-all: ("]
    for k, v in sorted(FLAT.items()):
        scss.append(f'  "{var_name(k)}": {json.dumps(v)},')
    scss.append(");")
    (ROOT / "web" / "_catalinas.scss").write_text("\n".join(scss) + "\n")
    written.append("web/_catalinas.scss")

if wants("mjs"):
    mjs = [
        "// Catalinas Design System — ESM tokens (generated)",
        "export const catTokens = " + json.dumps(FLAT, ensure_ascii=False, indent=1) + ";",
        "",
        "/** Lee un token por path: t('color.accent.base') -> var(--cat-color-accent-base) */",
        "export const t = path => `var(--cat-${path.replace('.', '-')})`;",
        "export default catTokens;",
    ]
    (ROOT / "web" / "catalinas.tokens.mjs").write_text("\n".join(mjs) + "\n")
    written.append("web/catalinas.tokens.mjs")

def dtcg_type(v):
    import re as _re
    s = str(v).strip()
    if _re.match(r"^#([0-9a-f]{3}|[0-9a-f]{6}|[0-9a-f]{8})$", s, _re.I):
        return "color"
    if _re.match(r"^rgba?\(", s) or _re.match(r"^hsla?\(", s):
        return "color"
    if _re.match(r"^-?[\d.]+px$", s):
        return "dimension"
    if _re.match(r"^-?\d+$", s):
        return "number"
    return None

def dtcg(node):
    out = {}
    for k, v in node.items():
        key = k
        if isinstance(v, dict):
            out[key] = dtcg(v)
        else:
            tt = dtcg_type(v)
            if tt is None:
                out[key] = {"$value": str(v), "$type": "string"}
            else:
                out[key] = {"$value": str(v), "$type": tt}
    return out

if wants("dtcg"):
    figma_dir = ROOT / "figma"
    figma_dir.mkdir(exist_ok=True)
    doc = {"$name": T.get("$name", "Catalinas"), "$description": "Catalinas tokens (W3C DTCG)", **dtcg(R)}
    (figma_dir / "tokens.tokens.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1))
    written.append("figma/tokens.tokens.json")

if wants("snippets"):
    snip_dir = ROOT / "snippets"
    snip_dir.mkdir(exist_ok=True)
    snips = {}
    for sp in specs:
        markup = sp["targets"].get("web", {}).get("markup", "")
        if not markup:
            continue
        body = [line.strip() for line in markup.split(">") ]
        # reconstruir con saltos legibles
        rebuilt = []
        buf = ""
        for part in markup.split("<"):
            if part:
                rebuilt.append("<" + part)
        snips["cat-" + sp["name"]] = {
            "prefix": ["cat-" + sp["name"]],
            "description": f"Catalinas: {sp.get('description', sp['name'])}",
            "body": rebuilt,
        }
    (snip_dir / "catalinas.json").write_text(json.dumps(snips, ensure_ascii=False, indent=1))
    written.append("snippets/catalinas.json")

if wants("api"):
    api = {
        "$schema": "https://catalinas.dev/api.schema.json",
        "version": T["$version"],
        "counts": {"widgets": len(specs), "tokens": len(FLAT)},
        "targets": TARGETS_ORDER,
        "widgets": [
            {
                "name": sp["name"],
                "description": sp.get("description"),
                "anatomy": sp.get("anatomy"),
                "props": sp.get("props"),
                "states": sp.get("states"),
                "variants": sp.get("variants"),
                "guidance": sp.get("guidance"),
                "targets": sorted(sp.get("targets", {}).keys()),
            } for sp in specs
        ],
    }
    api_dir = ROOT / "api"
    api_dir.mkdir(exist_ok=True)
    (api_dir / "api.json").write_text(json.dumps(api, ensure_ascii=False, indent=1))
    written.append("api/api.json")

# ---------- Web Components ----------
if wants("wc"):
    emit_wc(ROOT, written)

if wants("swift"):
    emit_swift(ROOT, FLAT, written)

if wants("compose"):
    emit_compose(ROOT, FLAT, written)

if wants("tokens-md"):
    emit_tokens_md(ROOT, FLAT, written)

# ---------- RTL (experimental) ----------
if wants("rtl"):
    import re as _re
    css_src = (ROOT / "web" / "catalinas.css").read_text()
    def rtl_line(line):
        line = _re.sub(r"(padding-)left(:)", r"\1TMPR\2", line)
        line = _re.sub(r"(padding-)right(:)", r"\1left\2", line)
        line = _re.sub(r"(padding-)TMPR(:)", r"\1right\2", line)
        line = _re.sub(r"(margin-)left(:)", r"\1TMPR\2", line)
        line = _re.sub(r"(margin-)right(:)", r"\1left\2", line)
        line = _re.sub(r"(margin-)TMPR(:)", r"\1right\2", line)
        line = _re.sub(r"text-align:left", "text-align:TMPR", line)
        line = _re.sub(r"text-align:right", "text-align:left", line)
        line = _re.sub(r"text-align:TMPR", "text-align:right", line)
        line = _re.sub(r"([\s;{])left:", r"\1TMPR:", line)
        line = _re.sub(r"([\s;{])right:", r"\1left:", line)
        line = _re.sub(r"([\s;{])TMPR:", r"\1right:", line)
        line = _re.sub(r"border-top-left-radius", "BTLR", line)
        line = _re.sub(r"border-top-right-radius", "border-top-left-radius", line)
        line = _re.sub(r"BTLR", "border-top-right-radius", line)
        line = _re.sub(r"border-bottom-left-radius", "BBLR", line)
        line = _re.sub(r"border-bottom-right-radius", "border-bottom-left-radius", line)
        line = _re.sub(r"BBLR", "border-bottom-right-radius", line)
        return line
    body = "\n".join(rtl_line(l) for l in css_src.splitlines())
    hdr = "/* Catalinas RTL (experimental) - flip direccional generado */"
    (ROOT / "web" / "catalinas.rtl.css").write_text(hdr + "\n" + body + "\n")
    written.append("web/catalinas.rtl.css")

print(f"catalinas build ok — {len(specs)} widgets, {len(FLAT)} tokens")
for w in written:
    print("  +", w)

if args_cli.watch:
    import time
    last = _latest_mtime()
    print(f"watching tokens/ y spec/ (mtime {last:.0f})... Ctrl+C para salir")
    try:
        while True:
            time.sleep(1.2)
            now = _latest_mtime()
            if now != last:
                last = now
                print("-> cambio detectado, recompilando...")
                subprocess.run([sys.executable, __file__,
                                "--targets", args_cli.targets], check=False)
    except KeyboardInterrupt:
        print("watch detenido")
