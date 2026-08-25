---
name: catalinas-tokens-theming
description: Skill de arquitectura de tokens y theming runtime del design system Catalinas (by Arcynox). Cubre las 3 capas de tokens, la regla de derivacion accent-desde-wallpaper, density modes, theming de fuentes e iconos con CDNs, reduced motion y como agregar un dark theme sin romper nada. Usar cuando se necesite rethemear un UI Catalinas, cambiar accent en runtime, agregar densidades, fuentes o packs de iconos.
---

# Catalinas Tokens & Runtime Theming

> El sistema tiene 147 tokens en 3 capas + semanticos que son OVERRIDE POINTS.
> Todo el theming ocurre a traves de los semanticos. Los componentes jamas
> tocan primitivos directamente.

---

## 1. LAS TRES CAPAS

```
PRIMITIVOS      color.accent.base = #5e9eff        (valores crudos, nunca cambian)
     ↓
SEMANTICOS      --cat-semantic-accent-dynamic      (override points del tema)
     ↓
COMPONENTES     background: var(--cat-semantic-accent-dynamic)
```

**Regla de oro:** un componente CSS jamas escribe `var(--cat-color-accent-base)`.
Siempre el semantico. Asi un tema/cambio de accent propaga a todo sin tocar componentes.

Semanticos disponibles:

| Token | Uso |
|---|---|
| `--cat-semantic-accent-dynamic` | color de accion unico del sistema |
| `--cat-semantic-accent-ring` | focus ring rgba |
| `--cat-semantic-chip-a/b` | fondos translucidos de chips/controles |
| `--cat-semantic-tab-a/b` | tab activo |
| `--cat-semantic-input-a/b` | fondo de inputs |
| `--cat-semantic-seg-checked` | segmented/switch checked bg |
| `--cat-semantic-statusbar-bg` | status bar |
| `--cat-semantic-sidebar-bg` | sidebar |
| `--cat-semantic-panel-tint` | accordions/paneles suaves |
| `--cat-semantic-float-a/b` | cards flotantes glass |
| `--cat-semantic-dropzone-bg` | dropzones |
| `--cat-semantic-toolbar-bg` | banda toolbar |
| `--cat-semantic-row-height` | altura de filas (density) |
| `--cat-semantic-glass-window` | vidrio de ventana raiz |

---

## 2. DERIVACION ACCENT DESDE WALLPAPER

El signature move del sistema: **el UI toma el hue dominante del wallpaper.**

```js
function deriveAccentFromImage(imgEl){
  const c = document.createElement('canvas');
  c.width = 48; c.height = 48;
  const ctx = c.getContext('2d', { willReadFrequently:true });
  ctx.drawImage(imgEl, 0, 0, 48, 48);
  const data = ctx.getImageData(0,0,48,48).data;

  // 24 bins de hue, peso por saturacion y distancia a luminosidad ideal
  const BINS=24, bins=Array.from({length:BINS},()=>({w:0,h:0,s:0}));
  for(let i=0;i<data.length;i+=4){
    const [h,s,l] = rgbToHsl(data[i],data[i+1],data[i+2]);
    if(l<.2||l>.96||s<.06) continue;
    const b=bins[Math.min(BINS-1,(h/360*BINS)|0)];
    const w=s*(1-Math.abs(l-.72));
    b.w+=w; b.h=h; b.s+=s*w;
  }
  // hue dominante + secundario lejano (>28deg) para gradientes duales
  ...
}
```

Reglas de la derivacion:
- Peso `s * (1 - abs(l - .72))`: favorece colores vivos pero claros.
- Descarta grises (`s<.06`) y extremos de luminosidad.
- Hue secundario debe estar a mas de 28deg del dominante; si no existe, dominante+42.
- El resultado pinta: `accent`, `ring`, `sel-a/b`, `glass-window`, `surface-content`,
  `toolbar-bg` (3 stops), `wall-hue-1/2`.

**Cache:** pedir la imagen con query param unico (`wallpaper.jpg?v=${Date.now()}`)
para no heredar el placeholder cacheado.

**CORS:** la imagen necesita `crossorigin="anonymous"` para getImageData.
Si falla (tainted canvas), catch silencioso mantiene defaults.

---

## 3. OVERRIDE EN RUNTIME

Tres niveles, en orden de precedencia:

```js
// nivel 1: accent manual puntual
document.documentElement.style.setProperty(
  '--cat-semantic-accent-dynamic', 'hsl(215 85% 60%)');

// nivel 2: swatches (color-picker widget)
// setea accent + ring juntos:
rs.setProperty('--cat-semantic-accent-dynamic', '#5e9eff');
rs.setProperty('--cat-semantic-accent-ring',   '#5e9eff29'); // alpha hex

// nivel 3: auto (derivar del wallpaper)
rootEl.removeProperty('--cat-semantic-accent-dynamic');
rootEl.removeProperty('--cat-semantic-accent-ring');
// -> vuelve al valor del :root o a la derivacion activa
```

Al usar override manual, SIEMPRE actualizar ring junto al accent
(ring = mismo color con alpha .16-.29).

---

## 4. DENSITY MODES

```css
[data-density="compact"]{--cat-size-control-h-sm:22px;--cat-size-control-h-md:26px;
  --cat-size-control-h-lg:30px;--cat-semantic-row-height:32px}
[data-density="cozy"]{...defaults...}
[data-density="comfortable"]{sm:28 md:34 lg:40 row:44}
```

Funciona porque TODOS los controles usan `var(--cat-size-control-h-*)`.
Si agregas un componente nuevo, sus alturas DEBEN usar estos tokens.

Activacion: `document.documentElement.dataset.density = 'compact'`.

---

## 5. FUENTES

Token unico que gobierna todo:

```css
--cat-font-family-ui:-apple-system,BlinkMacSystemFont,'SF Pro Text',
  'Segoe UI',system-ui,sans-serif;
```

Swap en runtime:

```js
// cargar webfont externa una sola vez
const link=document.createElement('link');
link.rel='stylesheet';
link.href='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap';
document.head.appendChild(link);
document.documentElement.style.setProperty(
  '--cat-font-family-ui', "'Inter', sans-serif");
```

Reglas:
- La familia custom SIEMPRE con fallback al stack del sistema.
- Los componentes declaran `font-family:var(--cat-font-family-ui)` — nunca font names fijos.
- Mono aparte: `--cat-font-family-mono` para kbd/code.

---

## 6. ICONOS THEABLE

Markup: `<span data-cat-icon="folder"></span>` (span VACIO, el runtime llena).

Providers (webfont CDN salvo lucide):

| Provider | Tipo | Prefijo ejemplo |
|---|---|---|
| **lucide** (default) | UMD JS + createIcons | `<i data-lucide="folder">` |
| remix | font css | `ri-folder-line` |
| tabler | font css | `ti-folder` |
| fa | font css | `fa-solid fa-folder` |
| phosphor | font css | `ph-folder` |

Runtime API:

```js
window.CatalinasIcons.use('tabler');   // cambia TODOS los iconos en vivo
window.CatalinasIcons.providers;       // lista disponible
window.CatalinasIcons.current;         // actual
```

Detalles criticos:
- Al aplicar por primera vez, snapshot del innerHTML original en `dataset.orig`
  (lazy: tambien para nodos insertados dinamicamente).
- Lucide via UMD: inyectar `<i data-lucide="name">` y llamar `lucide.createIcons()`.
- Iconos semanticos: folder/doc/ppt/music/img/home/cloud/desktop/cat/net.
- Color heredado via currentColor; sizing via `[data-cat-icon] svg,i{width:100%}`.

Agregar provider nuevo = entrada en PROVIDERS con {type,css|src,map}.

---

## 7. REDUCED MOTION

Obligatorio en todo proyecto:

```css
@media (prefers-reduced-motion: reduce){
  *,*::before,*::after{
    animation-duration:.01ms!important;
    animation-iteration-count:1!important;
    transition-duration:.01ms!important;
    scroll-behavior:auto!important}}
```

---

## 8. DARK THEME (como hacerlo BIEN si algun dia vuelve)

Fue removido en v0.4 porque estaba roto. Reglas para reintroducirlo:

1. Solo overrides SEMANTICOS bajo `[data-theme="dark"]`, jamas duplicar componentes.
2. Migrar TODOS los blancos hardcodeados a semanticos primero
   (chip/tab/input/statusbar/sidebar/float/dropzone/panel). Si queda UN rgba(255,255,255)
   decorativo fuera de token, dark quedara parchado.
3. Ink invertido: hi→claro, low/faint ajustados, strokes oscuras → claras translucidas.
4. Glass window oscuro: rgba(26,30,44,.66).
5. QA visual POR COMPONENTE antes de publicar (fue la razon del removal).

---

## 9. CHECKLIST DE THEMING

- [ ] Ningun componente referencia primitivos directo
- [ ] Accent + ring se setean JUNTOS siempre
- [ ] Derivacion con cache-bust en la imagen fuente
- [ ] Density usa tokens de altura, no heights fijas nuevas
- [ ] Fuentes con fallback stack incluido
- [ ] Icon picker dispara CatalinasIcons.use, nunca innerHTML manual
- [ ] prefers-reduced-motion presente
