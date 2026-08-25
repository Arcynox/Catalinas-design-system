/* Catalinas Design System - Web Components runtime (generated)
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
