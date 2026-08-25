#!/usr/bin/env python3
"""Generadores extra de Catalinas: Web Components, SwiftUI, Compose, tokens.md."""
import json, re
from pathlib import Path


def emit_wc(ROOT, written):
    """Runtime de Web Components light-DOM (agnosticos de framework).
    Estilado por catalinas.css via clases cat-* — sin Shadow DOM."""
    js = r"""/* Catalinas Design System - Web Components runtime (generated)
   Elementos light-DOM estilados por catalinas.css. Agnosticos de framework.

   <cat-button variant="primary|secondary|ghost|danger" size="sm|md|lg">Texto</cat-button>
   <cat-badge tone="success" dot>Beta</cat-badge>
   <cat-avatar initials="LU" online></cat-avatar>
   <cat-card level="content|chip|float|dark"><h3>...</h3></cat-card>
   <cat-alert tone="info|success|warning|danger" title="..." message="..." dismissible></cat-alert>
   <cat-switch checked></cat-switch>
   <cat-segmented options="Icons,List,Gallery"></cat-segmented>
*/
(() => {
  const STAR = '<svg viewBox="0 0 24 24" width="11" height="11" fill="currentColor"><path d="M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z"/></svg>';
  const X = '<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>';

  function base(tag, cls, render) {
    class C extends HTMLElement {
      connectedCallback() { this.render(); }
      attributeChangedCallback() { if (this.isConnected) this.render(); }
      static get observedAttributes() { return ["*"]; }
      render() { this.className = cls; this.innerHTML = render(this); }
    }
    customElements.define(tag, C);
    return C;
  }

  base("cat-button", "", el => {
    const v = el.getAttribute("variant") || "primary";
    const size = el.getAttribute("size");
    const b = document.createElement("button");
    b.type = "button";
    b.className = ["cat-btn", v, size && size !== "md" ? size : ""].filter(Boolean).join(" ");
    b.append(...Array.from(el.childNodes));
    el.replaceChildren(b);
    return b;
  });

  base("cat-badge", "", el => {
    const tone = el.getAttribute("tone");
    const s = document.createElement("span");
    s.className = "cat-badge" + (tone ? " " + tone : "");
    if (el.hasAttribute("dot")) s.appendChild(Object.assign(document.createElement("span"), { className: "dot" }));
    s.append(el.textContent.trim());
    el.replaceChildren(s);
  });

  base("cat-avatar", "", el => {
    const s = document.createElement("span");
    s.className = "cat-avatar";
    const src = el.getAttribute("src");
    if (src) { const i = document.createElement("img"); i.src = src; s.appendChild(i); }
    else s.append((el.getAttribute("initials") || "").slice(0, 2));
    if (el.hasAttribute("online")) s.appendChild(Object.assign(document.createElement("i"), { className: "presence" }));
    el.replaceChildren(s);
  });

  base("cat-card", "", el => {
    const lvl = el.getAttribute("level");
    const d = document.createElement("div");
    d.className = "cat-card " + (lvl || "");
    d.append(...Array.from(el.childNodes));
    el.replaceChildren(d);
  });

  base("cat-alert", "", el => {
    const tone = el.getAttribute("tone") || "info";
    const w = document.createElement("div");
    w.className = "cat-alert " + tone;
    const ic = document.createElement("span");
    ic.className = "a-icon";
    ic.style.background = tone === "success" ? "var(--cat-color-success)"
      : tone === "warning" ? "var(--cat-color-warning)"
      : tone === "danger" ? "var(--cat-color-danger-base)"
      : "var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base))";
    ic.innerHTML = STAR;
    const body = document.createElement("div");
    body.className = "a-body";
    body.innerHTML = '<b>' + (el.getAttribute("title") || "") + '</b><span>'
      + (el.getAttribute("message") || "") + '</span>';
    w.append(ic, body);
    if (el.hasAttribute("dismissible")) {
      const x = document.createElement("button");
      x.className = "t-close"; x.innerHTML = X;
      x.addEventListener("click", () => el.remove());
      w.appendChild(x);
    }
    el.replaceChildren(w);
  });

  base("cat-switch", "", el => {
    const l = document.createElement("label");
    l.className = "cat-switch";
    const i = document.createElement("input");
    i.type = "checkbox";
    i.checked = el.hasAttribute("checked");
    i.addEventListener("change", () => {
      i.checked ? el.setAttribute("checked", "") : el.removeAttribute("checked");
      el.dispatchEvent(new Event("change", { bubbles: true }));
    });
    const t = document.createElement("span");
    t.className = "track";
    l.append(i, t);
    el.replaceChildren(l);
  });

  base("cat-segmented", "", el => {
    const opts = (el.getAttribute("options") || "").split(",").map(s => s.trim()).filter(Boolean);
    el.className = "cat-segmented";
    el.setAttribute("data-cat-segmented", "");
    opts.forEach((o, i) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "seg-btn" + (i === 0 ? " is-active" : "");
      b.setAttribute("aria-pressed", String(i === 0));
      b.textContent = o;
      b.addEventListener("click", () => {
        el.querySelectorAll(".seg-btn").forEach(x => {
          x.classList.toggle("is-active", x === b);
          x.setAttribute("aria-pressed", String(x === b));
        });
        el.dispatchEvent(new CustomEvent("change", { detail: o, bubbles: true }));
        el.dispatchEvent(new Event("segment-change"));
        el.dispatchEvent(new Event("input", { bubbles: true }));
      });
      el.appendChild(b);
    });
    // glider del core se engancha si catalinas.js esta presente
    document.addEventListener("DOMContentLoaded", () => {
      el.querySelectorAll(".seg-btn").forEach(b =>
        b.addEventListener("click", () => el.dispatchEvent(new Event("cat:move"))));
    });
  });

  // integracion con behaviors del core (glider)
  document.addEventListener("cat:move", e => {
    const seg = e.target.closest("[data-cat-segmented]");
    if (seg && seg._moveGlider) seg._moveGlider();
  });

  window.CatalinasWC = { version: "0.10.0" };
})();
"""
    out = ROOT / "web" / "catalinas-wc.js"
    out.write_text(js)
    written.append("web/catalinas-wc.js")


def _hex_only(v):
    s = str(v).strip()
    return s if re.match(r"^#[0-9a-fA-F]{6}$", s) else None


def emit_swift(ROOT, FLAT, written):
    colors = []
    for k, v in sorted(FLAT.items()):
        hx = _hex_only(v)
        if hx and k.startswith("color"):
            name = "".join(p.capitalize() for p in k.split("-"))
            colors.append(f"    public static let {name} = Color(catalinaHex: \"{hx}\")")
    radii = []
    for k, v in sorted(FLAT.items()):
        if k.startswith("size-radius-"):
            num = float(str(v).replace("px", ""))
            radii.append(f'    public static let ' + k.replace("size-radius-", "").replace("-", "_")
                         + f' = CGFloat({num})')
    swift = f"""// Catalinas Design System - SwiftUI theme (generated)

import SwiftUI

public extension Color {{
    init(catalinaHex hex: String) {{
        let h = hex.replacingOccurrences(of: "#", with: "")
        var rgb: UInt64 = 0
        Scanner(string: h).scanHexInt64(&rgb)
        self.init(.sRGB,
                  red: Double((rgb >> 16) & 0xFF) / 255,
                  green: Double((rgb >> 8) & 0xFF) / 255,
                  blue: Double(rgb & 0xFF) / 255,
                  opacity: 1)
    }}
}}

public enum CatColors {{
{chr(10).join(colors)}
}}

public enum CatRadius {{
{chr(10).join(radii)}
}}

public extension Font {{
    static let catBody = Font.system(size: 13, weight: .regular)
    static let catCaption = Font.system(size: 11, weight: .medium)
    static let catTitle = Font.system(size: 17, weight: .semibold)
}}
"""
    d = ROOT / "swiftui"
    d.mkdir(exist_ok=True)
    (d / "CatalinasTheme.swift").write_text(swift)
    written.append("swiftui/CatalinasTheme.swift")


def emit_compose(ROOT, FLAT, written):
    def kt_color(v):
        s = str(v).strip()
        m = re.match(r"^#([0-9a-fA-F]{6})$", s)
        if m:
            return "Color(0xFF" + m.group(1).upper() + ")"
        m = re.match(r"^rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([\d.]+)\s*\)", s)
        if m:
            a = int(round(float(m.group(4)) * 255))
            argb = (a << 24) | (int(m.group(1)) << 16) | (int(m.group(2)) << 8) | int(m.group(3))
            return f"Color(0x{argb & 0xFFFFFFFF:08X})"
        return None

    lines = [
        "// Catalinas Design System - Compose Multiplatform theme (generated)",
        "package dev.arcynox.catalinas",
        "",
        "import androidx.compose.ui.graphics.Color",
        "import androidx.compose.material3.Typography",
        "",
        "object CatColors {",
    ]
    for k, v in sorted(FLAT.items()):
        if not k.startswith("color"):
            continue
        c = kt_color(v)
        if c:
            name = "Cat" + "".join(p.capitalize() for p in k.split("-")[1:])
            lines.append(f"    val {name} = {c}")
    lines += ["}", "", "object CatRadius {"]
    for k, v in sorted(FLAT.items()):
        if k.startswith("size-radius-"):
            num = float(str(v).replace("px", ""))
            name = k.replace("size-radius-", "").replace("-", "_")
            lines.append(f"    val {name} = {num}.dp")
    lines += ["}"]
    d = ROOT / "compose"
    d.mkdir(exist_ok=True)
    (d / "CatalinasTheme.kt").write_text("\n".join(lines) + "\n")
    written.append("compose/CatalinasTheme.kt")


def emit_tokens_md(ROOT, FLAT, written):
    groups = {}
    for k, v in sorted(FLAT.items()):
        g = k.split("-")[0]
        groups.setdefault(g, []).append((k, v))
    names = {"color": "Color", "size": "Tamanio y radios", "font": "Tipografia",
             "elevation": "Elevacion / sombras", "blur": "Blur / materiales",
             "motion": "Motion", "depth": "Profundidad (z-index)",
             "semantic": "Semanticos (runtime)"}
    md = ["<!-- generated -->", "# Referencia de tokens", ""]
    for g, items in groups.items():
        md += [f"## {names.get(g, g.capitalize())}", "",
               "| Token | Valor |", "|---|---|"]
        for k, v in items:
            md.append(f"| `{k}` | `{v}` |")
        md.append("")
    (ROOT / "docs" / "tokens.md").write_text("\n".join(md) + "\n")
    written.append("docs/tokens.md")
