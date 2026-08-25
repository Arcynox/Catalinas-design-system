---
name: catalinas-web
description: Master skill para implementar el design system Catalinas (by Arcynox) en cualquier proyecto web. Look macOS HIG plano con ventanas de vidrio acrilico, hairlines, un solo accent, superficies planas y contenido casi opaco. Usar cuando el usuario pida "estilo Catalinas", "glass estilo macOS", "design system Arcynox", o una UI de escritorio web (file manager, dashboard, app shell). Cubre layout shell, chrome, toolbar, sidebar, listas, status bar, cards y ventanas.
---

# Catalinas Web: Design System Implementation

> Sistema disenado por Arcynox. Este skill implementa el LOOK COMPLETO en web.
> Filosofia central: superficies planas + hairlines + un solo accent + glass solo donde corresponde.
> Si el proyecto ya tiene `catalinas.css`, usalo directo. Si no, este skill te ensena a reproducir
> el lenguaje desde cero con CSS puro.

---

## 0. DECISION DE RUTA

Antes de escribir CSS, decidí:

1. **¿Existe `catalinas.css` en el proyecto?** → linkealo y usa las clases `cat-*`. No reinventes.
2. **¿Proyecto sin la libreria?** → implementá el lenguaje con CSS propio siguiendo este skill al pie de la letra.
3. **¿App de escritorio web?** (file manager, IDE, dashboard con sidebar) → usa el patron APP SHELL completo (seccion 3).
4. **¿Landing/marketing?** → este skill NO aplica para hero sections llamativas; aplican los componentes internos (botones, inputs) pero el layout es libre.

---

## 1. FILOSOFIA (no negociable)

Estas reglas definen si algo "se siente Catalinas" o no. Violaciones = rechazo.

1. **Superficies PLANAS.** Cero gradientes decorativos. Los unicos gradientes permitidos son:
   - skeleton shimmer (funcional)
   - artwork/cover de media (es contenido, no decoracion)
   Todo lo demas: color solido o rgba translucido.

2. **Hairlines, no cajas.** Los bordes son `1px` con alpha bajo. Un borde nunca debe "gritar".
   - Sobre fondo claro: `rgba(20,30,60,.08)` (oscura translucida)
   - Sobre vidrio/wallpaper: `rgba(255,255,255,.55)` (clara)
   - Regla: el borde debe ser apenas perceptible.

3. **Un solo accent.** Todo el sistema gira alrededor de UN color (`--cat-semantic-accent-dynamic`).
   - Hover = tono mas oscuro del accent (no filter brightness en produccion real).
   - Active = todavia mas oscuro.
   - Seleccion, focus ring, item activo de sidebar, botones primary: TODOS usan ese accent.
   - Nunca dos colores compitiendo por atencion.

4. **Legibilidad > transparencia.** El contenido interno es MAS opaco que el chrome.
   - Chrome de ventana: ~68% opaco
   - Contenido: ~87% opaco
   - El usuario jamas pelea con contraste para leer informacion primaria.

5. **Glass es material por capa, no decoracion global.**
   | Capa | Material |
   |---|---|
   | Wallpaper | foto con blur 46px saturate(1.7) |
   | Ventana raiz | glass: blur(46px) + rgba blanca .68 |
   | Toolbar/banda | tinte accent al ~10% + blur chip |
   | Dropdowns/menus | surface menu .88 + blur float |
   | Cards flotantes | chip translucido + blur |
   | CONTENIDO | casi opaco (.87-.90) SIN blur |

6. **Severidad con icono lider.** Alerts/toasts/banners comunican severidad con un ICONO
   en circulo solid + tinte sutil del contenedor. PROHIBIDO franjas o bordes laterales
   de color como carrier unico de significado.

7. **Sombras cortas y neutras.** Nada de glows de color ni sombras gigantes de 90px.
   ```css
   /* ventana */ box-shadow: 0 18px 60px rgba(0,0,0,.26), 0 6px 18px rgba(0,0,0,.12);
   /* menu    */ box-shadow: 0 14px 40px rgba(0,0,0,.22), 0 2px 8px rgba(0,0,0,.10);
   /* boton raised */ box-shadow: 0 1px 2px rgba(0,0,0,.14);
   ```

8. **Zona interactiva > elemento visual.** Thumb de slider 15px sobre track de 4px.
   Hit areas generosas via padding invisible.

9. **prefers-reduced-motion respeta todo.** Inclui siempre:
   ```css
   @media (prefers-reduced-motion: reduce){
     *,*::before,*::after{animation-duration:.01ms!important;
       transition-duration:.01ms!important}
   }
   ```

---

## 2. TOKENS (los 147)

Si no hay catalinas.css, definí estos tokens en `:root`. Son el contrato.

### Color
```css
:root{
  /* ink */
  --cat-color-ink-hi:#1c2436; --cat-color-ink-mid:#59627a;
  --cat-color-ink-low:#8d95a8; --cat-color-ink-faint:#aab1c2;

  /* accent (semantic override point) */
  --cat-color-accent-base:#5e9eff;
  --cat-color-accent-hover:#4a8df2;
  --cat-color-accent-active:#3d7ce0;
  --cat-color-accent-on:#ffffff;
  --cat-semantic-accent-dynamic:var(--cat-color-accent-base);
  --cat-semantic-accent-ring:rgba(94,158,255,.16);

  /* estados */
  --cat-color-success:#34c759; --cat-color-warning:#ff9f0a;
  --cat-color-danger-base:#e8382d; --cat-color-danger-hover:#c22b21;

  /* superficies */
  --cat-color-surface-glass-window:rgba(247,249,253,.68);
  --cat-color-surface-content:rgba(255,255,255,.87);
  --cat-color-surface-card:rgba(255,255,255,.72);
  --cat-color-surface-menu:rgba(246,246,250,.88);
  --cat-color-surface-glass-chip:rgba(255,255,255,.45);
  --cat-color-surface-hover:rgba(0,0,0,.05);
  --cat-color-surface-active:rgba(0,0,0,.09);

  /* strokes */
  --cat-color-stroke-light:rgba(255,255,255,.55);  /* solo sobre wallpaper/vidrio */
  --cat-color-stroke-input:rgba(20,30,60,.14);     /* controles sobre claro */
  --cat-color-stroke-dark:rgba(20,30,60,.08);
  --cat-color-stroke-softer:rgba(20,30,60,.05);

  /* dark player (superficie funcional oscura) */
  --cat-color-dark-player-bg:rgba(24,28,42,.74);
}
```

### Escalas
```css
--cat-size-radius-xs:4px; sm:6px; md:8px; lg:12px; xl:16px; window:12px; pill:999px;
--cat-size-space-1..20: 2,4,6,8,10,12,14,16,20,24,32,40 px
--cat-size-control-h-sm/md/lg: 26/30/36px
--cat-font-size-2xs..2xl: 10,11,12,12.5,13,15,17,20,24,32px
--cat-motion-fast/med/slow: 120/180/260ms
--cat-motion-ease-out: cubic-bezier(.2,.7,.3,1)
--cat-motion-spring: cubic-bezier(.25,.8,.3,1.2)
```

### Regla de nombres
Todo token = `--cat-<categoria>-<sub>-<nombre>` kebab-case. Los semanticos son
override points: un tema cambia SOLO semanticos, nunca primitivos.

---

## 3. APP SHELL (layout maestro)

Estructura de toda app de escritorio web:

```html
<div class="appshell">
  <header class="shell-chrome">
    <!-- tabs deslizantes + controles de ventana -->
  </header>
  <nav class="shell-navbar">
    <!-- nav-segmented + breadcrumb + search -->
  </nav>
  <div class="shell-toolbar"><!-- banda de acciones --></div>
  <div class="shell-body">
    <aside class="sidebar"><!-- navegacion --></aside>
    <main class="shell-main"><!-- contenido --></main>
  </div>
  <footer class="statusbar"><!-- estado contextual --></footer>
</div>
```

```css
.appshell{
  display:flex;flex-direction:column;
  width:min(1040px,96vw);height:min(680px,92vh);
  border-radius:var(--cat-size-radius-window);
  background:var(--cat-color-surface-glass-window);
  backdrop-filter:blur(46px) saturate(1.7);
  -webkit-backdrop-filter:blur(46px) saturate(1.7);
  border:1px solid var(--cat-color-stroke-light);
  box-shadow:0 18px 60px rgba(0,0,0,.26),inset 0 1px 0 rgba(255,255,255,.65);
  overflow:hidden;
}
.shell-body{flex:1;min-height:0;display:grid;grid-template-columns:216px 1fr;
  margin:0 14px;border-radius:0 0 var(--cat-size-radius-lg) var(--cat-size-radius-lg);
  background:var(--cat-color-surface-content);
  border:1px solid var(--cat-color-stroke-light);border-top:none;}
```

**Clave:** toolbar y body se CONECTAN visualmente. Toolbar radius arriba solamente,
body radius abajo solamente. Parecen una sola unidad.

### Wallpaper detras

```css
body{background:linear-gradient(180deg,#f5f7fb,#e9ecf5)} /* fallback */
.wallpaper{position:fixed;inset:-140px;width:calc(100%+280px);height:calc(100%+280px);
  object-fit:cover;filter:blur(46px) saturate(1.7) brightness(1.06);
  transform:scale(1.02)}
```
El inset negativo evita bordes fantasma del blur. La MISMA formula de blur que la ventana:
todo el escritorio es un material continuo.

---

## 4. WINDOW CHROME

Tabs integrados al chrome + controles − □ X a la derecha.

```html
<header class="chrome">
  <div class="tabs" data-cat-tabs role="tablist">...</div>
  <div class="win-controls">
    <button class="win-btn" aria-label="Minimize">[svg minus]</button>
    <button class="win-btn" aria-label="Maximize">[svg square]</button>
    <button class="win-btn close" aria-label="Close">[svg x]</button>
  </div>
</header>
```

Reglas:
- Controles son ICONOS directos negros, 28x24, hover gris, **close hover ROJO #e8382d + icono blanco**.
- Tabs: chips flotantes de 30px. El activo se distingue con un GLIDER deslizante
  (ver skill catalinas-components, seccion Sliding Selection).
- Chrome SIN border-bottom: chrome y navbar comparten la misma superficie de vidrio.

---

## 5. NAVBAR + TOOLBAR

```html
<nav class="navbar">
  <div class="nav-seg"> <!-- rectangulo unico blanco segmentado --> </div>
  <breadcrumb/>
  <search/> <!-- pill 30px radius 10 -->
</nav>
<div class="toolbar">
  <button class="tool-btn primary">Add New</button>
  <span class="sep"></span>
  <button class="tool-btn">Organize ▾</button>
</div>
```

- `.nav-seg`: back/forward/refresh en UN rectangulo blanco (mismo tratamiento que search).
  Sin divisores entre segmentos. Radius 10px igual que search.
- `.toolbar`: banda con `background:rgba(accent,.10)`, border-top-radius 14,
  conectada al body debajo. Add New = filled accent (unico botón lleno).
- Tool-btn hover: `rgba(0,0,0,.05)` — gris sutil, JAMAS blanco brillante.

---

## 6. SIDEBAR

Item activo = accent LLENO con texto blanco (patron Finder de macOS):

```css
.side-item{display:flex;align-items:center;gap:9px;height:var(--row-h,30px);
  padding:0 9px;border-radius:var(--r-sm,6px);color:var(--ink-mid);cursor:pointer}
.side-item:hover{background:rgba(255,255,255,.5);color:var(--ink-hi)}
.side-item.active{background:var(--accent);color:#fff;font-weight:500;
  box-shadow:0 1px 2px rgba(0,0,0,.12)}
.side-item.active .icon{color:#fff}
```

Arbol expandible: chevron rota 180deg al abrir, children con padding-left indentado.
Secciones con label uppercase tracking amplio color faint entre grupos.
Ancho fijo 216-224px. Fondo: tint neutro muy suave + border-right hairline.

---

## 7. LISTA AGRUPADA (editorial scanning)

```html
<div class="list-header"><span>Name</span><span>Type</span><span>Date</span></div>
<div class="group-head">File folders</div>
<div class="rows" data-cat-selectable data-cat-statusbar="#sb">
  <div class="row" tabindex="0" data-name="Design" data-meta="Folder · Aug 22">
    <span class="cell-name">Design</span><span class="cell-type">Folder</span>
    <span class="cell-date">Aug 22</span></div>
</div>
```

- Headers de columna: uppercase, 11px, weight 500, color low, tracking .04em.
- Group heads separan por tipo: estructura editorial que mejora el scanning.
- Rows: height 38px, grid 1.6fr/1fr/1fr, radius 6, hover negro 4%.
- Seleccion: **fila completa accent fill, texto blanco**, iconos iluminados.
- Multi-select con Ctrl/Meta via comportamiento `data-cat-selectable`.

## 8. STATUS BAR CONTEXTUAL

Refleja el estado actual. Con seleccion muestra icono + nombre + metadata;
sin seleccion: "No file selected". Count a la derecha SIEMPRE visible
(`4 folders and 67 files · 4.33 GB`). Sentence case, no uppercase gritado.

```css
.statusbar{display:flex;justify-content:space-between;padding:9px 18px;
  border-top:1px solid stroke-dark;background:rgba(255,255,255,.5);
  backdrop-filter:blur(12px)}
.status-title{font-size:12.5px;font-weight:550;color:ink-hi}
.status-meta{font-size:11px;color:ink-low;margin-top:1px}
```

---

## 9. CARDS (niveles de superficie)

| Clase | Uso | Estilo |
|---|---|---|
| `.card content` | contenedor estandar | bg content .87 + border light + shadow panel |
| `.card chip` | translucida sobre dot-grid | bg glass-chip + blur chip |
| `.card float` | widget flotante (player, dock) | bg .74 + blur float + shadow float |
| `.card dark` | superficie funcional oscura | bg player-bg + ink claro |

Padding 16, radius lg(12). Las cards dark permiten contenido claro invertido.

---

## 10. CHECKLIST FINAL (antes de entregar)

- [ ] Cero gradientes decorativos (solo skeleton/artwork)
- [ ] Hairlines: ningun borde mas opaco que rgba(x,x,x,.55) sobre claro
- [ ] Un solo accent; hover/active derivados
- [ ] Contenido mas opaco que chrome
- [] Severidad con icono lider, sin franjas laterales
- [ ] Todos los botones icon-only tienen aria-label
- [ ] Focus-visible ring accent en todo interactivo
- [ ] prefers-reduced-motion incluido
- [ ] Sombras cortas neutras (max 60px blur)
- [ ] Sentence case en status bar; uppercase solo headers/columnas
