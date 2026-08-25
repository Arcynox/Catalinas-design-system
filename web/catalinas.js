/* Catalinas Design System — generated behaviors, do not edit */

(() => {
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
})();

/* carousel */

document.addEventListener("click", e => {
  const btn = e.target.closest("[data-cat-car-next],[data-cat-car-prev]");
  if (!btn) return;
  const wrap = btn.closest(".car-wrap");
  const car = wrap && wrap.querySelector(".cat-carousel");
  if (!car) return;
  const first = car.firstElementChild;
  const step = first ? (first.getBoundingClientRect().width + 12) : 162;
  car.scrollBy({ left: btn.hasAttribute("data-cat-car-next") ? step : -step, behavior: "smooth" });
});

/* color-picker */

(() => { function init(root){  root.addEventListener("click", e => {   const b = e.target.closest(".cat-swatch");   if (!b || !root.contains(b)) return;   const rs = document.documentElement.style;   root.querySelectorAll(".cat-swatch").forEach(x => x.classList.toggle("active", x === b));   if (b.dataset.color){    rs.setProperty("--cat-semantic-accent-dynamic", b.dataset.color);    rs.setProperty("--cat-semantic-accent-ring", b.dataset.color + "29");   } else {    rs.removeProperty("--cat-semantic-accent-dynamic");    rs.removeProperty("--cat-semantic-accent-ring");   }  }); } document.addEventListener("DOMContentLoaded", () => {  document.querySelectorAll("[data-cat-colors]").forEach(init); });})();

/* icons */

window.CatalinasIcons = (() => {
  const PROVIDERS = {
    lucide:{type:"umd",src:"https://unpkg.com/lucide@0.469.0/dist/umd/lucide.min.js",
      map:{folder:"folder",doc:"file-text",ppt:"presentation",music:"music",img:"image",home:"house",cloud:"cloud",desktop:"monitor",cat:"cat",net:"globe"}},
    remix:{type:"font",css:"https://cdn.jsdelivr.net/npm/remixicon@4.5.0/fonts/remixicon.css",pre:"ri-",
      map:{folder:"folder-line",doc:"file-word-line",ppt:"file-ppt-2-line",music:"music-2-line",img:"image-line",home:"home-5-line",cloud:"cloud-line",desktop:"computer-line",cat:"star-line",net:"global-line"}},
    tabler:{type:"font",css:"https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.31.0/dist/tabler-icons.min.css",pre:"ti ti-",
      map:{folder:"folder",doc:"file-text",ppt:"presentation",music:"music",img:"photo",home:"home",cloud:"cloud",desktop:"device-desktop",cat:"paw",net:"world"}},
    fa:{type:"font",css:"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css",pre:"fa-solid ",
      map:{folder:"fa-folder",doc:"fa-file-lines",ppt:"fa-file-powerpoint",music:"fa-music",img:"fa-image",home:"fa-house",cloud:"fa-cloud",desktop:"fa-desktop",cat:"fa-paw",net:"fa-globe"}},
    phosphor:{type:"font",css:"https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1/src/regular/style.css",pre:"ph ph-",
      map:{folder:"folder",doc:"file-doc",ppt:"file-ppt",music:"music-notes",img:"image",home:"house",cloud:"cloud",desktop:"monitor",cat:"paw-print",net:"globe"}}
  };
  const DEFAULT="lucide";
  let current=null;
  let umdPromise=null;

  function loadUmd(src){
    if(umdPromise)return umdPromise;
    umdPromise=new Promise((res,rej)=>{
      const s=document.createElement("script");
      s.src=src;s.onload=res;s.onerror=()=>rej(new Error("UMD load fail"));
      document.head.appendChild(s);
    });
    return umdPromise;
  }
  function ensureFont(p){
    let l=document.querySelector('link[data-cat-icons-font]');
    if(!l){l=document.createElement("link");l.rel="stylesheet";l.setAttribute("data-cat-icons-font","");document.head.appendChild(l);}
    l.href=p.css;
  }
  function paintFont(p){
    [...document.querySelectorAll("[data-cat-icon]")].forEach(n=>{
      const name=p.map[n.dataset.catIcon];
      if(name)n.innerHTML='<i class="'+p.pre+name+'"></i>';
    });
  }
  async function paintUmd(p){
    try{await loadUmd(p.src);}catch(e){console.warn("[catalinas-icons]",e.message);return;}
    [...document.querySelectorAll("[data-cat-icon]")].forEach(n=>{
      const name=p.map[n.dataset.catIcon];
      if(name)n.innerHTML='<i data-lucide="'+name+'"></i>';
    });
    window.lucide&&window.lucide.createIcons();
  }

  function use(key){
    key=key||DEFAULT;
    const p=PROVIDERS[key];
    if(!p){console.warn("[catalinas-icons] provider desconocido:",key);return;}
    current=key;
    return p.type==="umd"?paintUmd(p):(ensureFont(p),paintFont(p));
  }

  document.addEventListener("DOMContentLoaded",()=>use(DEFAULT));

  return {use,providers:Object.keys(PROVIDERS),default:DEFAULT,get current(){return current;}};
})();
