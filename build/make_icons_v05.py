#!/usr/bin/env python3
"""v0.5: icons runtime nuevo (lucide default, sin bootstrap/system) + specs extra."""
import json, pathlib

# ---------------- ICONS ----------------
ICONS_JS = r"""window.CatalinasIcons = (() => {
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
})();"""

spec = {
"name":"icons",
"description":"Iconos themable con runtime CatalinasIcons. Default: Lucide (SVG). Alternativas por CDN webfont.",
"props":{"provider":"lucide|remix|tabler|fa|phosphor","name":"folder|doc|ppt|music|img|home|cloud|desktop|cat|net"},
"targets":{"web":{
"markup":'<span data-cat-icon="folder"></span>',
"css":["""
[data-cat-icon]{display:inline-grid;place-items:center;width:17px;height:17px}
[data-cat-icon] svg,[data-cat-icon] i{width:100%;height:100%;font-size:16px;line-height:1}""",
"""
.cat-icon-picker{display:inline-flex;gap:4px;flex-wrap:wrap}
.cat-icon-picker button{height:26px;padding:0 10px;border-radius:var(--cat-size-radius-sm);border:1px solid var(--cat-color-stroke-input);background:var(--cat-color-surface-card);font:500 var(--cat-font-size-xs) var(--cat-font-family-ui);color:var(--cat-color-ink-mid);cursor:pointer;transition:all var(--cat-motion-fast)}
.cat-icon-picker button:hover{color:var(--cat-color-ink-hi)}
.cat-icon-picker button.is-active{background:var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base));border-color:transparent;color:#fff;font-weight:600}
.cat-icons-grid{display:flex;flex-wrap:wrap;gap:14px;font-size:13px;color:var(--cat-color-ink-mid)}
.cat-icons-grid .icell{display:flex;flex-direction:column;align-items:center;gap:5px;width:64px;padding:10px 4px;border-radius:var(--cat-size-radius-md);background:var(--cat-color-surface-card)}"""],
"js":ICONS_JS}},
"docs": {"demos": [
'<div style="width:100%"><div class="cat-icon-picker" id="packPicker"><button type="button" data-pack="lucide" class="is-active">Lucide</button><button type="button" data-pack="remix">Remix</button><button type="button" data-pack="tabler">Tabler</button><button type="button" data-pack="fa">Font Awesome</button><button type="button" data-pack="phosphor">Phosphor</button></div></div>',
'<div class="cat-icons-grid">' + "".join(f'<div class="icell"><span data-cat-icon="{k}"></span><small>{k}</small></div>' for k in ["folder","doc","ppt","music","img","home","cloud","desktop","cat","net"]) + '</div>'],
"note":"Default Lucide. Cambio en vivo via CatalinasIcons.use(provider)."}
}

pathlib.Path("spec/icons.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1))
print("icons.json reescrito (lucide default, sin bootstrap/system)")
