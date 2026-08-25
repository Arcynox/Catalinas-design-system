---
name: catalinas-components
description: Guia completa de implementacion de los 45 componentes del design system Catalinas (by Arcynox) en web. Cubre convenciones cat-*, markup y CSS de cada componente por categoria (acciones, entrada, navegacion, datos, feedback, superficies), la seleccion deslizante (glider), menus con flip automatico, behaviors data-cat-* y el checklist para agregar widgets nuevos. Usar al construir o extender cualquier UI Catalinas en web.
---

# Catalinas Components: Library Implementation

> 45 componentes, convencion unica: clases `cat-*`, behaviors declarativos `data-cat-*`,
> tokens semanticos para todo color/altura. Cada seccion = markup + css clave + estados.

---

## 0. CONVENCIONES

- Prefijo de clase: `cat-` kebab-case (`cat-btn`, `cat-menu-item`).
- Modificador de estado: `is-active`, `is-selected`, `is-error`, `cat-leaving`.
- Behaviors declarativos (core JS los engancha solo):
  | Attr | Efecto |
  |---|---|
  | `data-cat-tabs` + `data-cat-tab` | tabs con glider + paneles |
  | `data-cat-segmented` | segmented con glider |
  | `data-cat-rating` + `.star` | rating hover/click |
  | `data-cat-selectable` + `data-cat-statusbar` | multi-seleccion filas -> status bar |
  | `data-cat-chips` | chips toggle .active |
  | `data-cat-colors` | swatches de accent |
  | `data-cat-command` + `data-cat-cmd` | items del Ctrl+K |
  | `data-cat-dismiss=".sel"` | cierra el ancestro |
  | `data-cat-validate` | validacion de form |
  | `data-cat-spark="1,2,3"` | sparkline SVG |
  | `data-cat-tooltip="txt"` | tooltip CSS-only |
- Colores SIEMPRE via `var(--cat-semantic-*)` o `var(--cat-color-*)`.
- Alturas via `var(--cat-size-control-h-{sm,md,lg})`.

---

## 1. ACCIONES

### Button
```css
.cat-btn{height:var(--h-md);padding:0 14px;border-radius:var(--r-sm);
  font:500 var(--fs-base)/1 ui;border:1px solid transparent;cursor:pointer;
  display:inline-flex;align-items:center;justify-content:center;gap:7px;
  transition:background fast,transform fast}
.cat-btn:active{transform:scale(.97)}
```
| Variante | Estilo | Hover |
|---|---|---|
| primary | bg accent solid, texto blanco | accent-hover token |
| secondary | chip translucido + hairline input | chip-hover |
| ghost | transparente, texto mid | surface-hover + ink-hi |
| danger | danger solid | danger-hover |
| link | sin padding/bg, color accent | underline |

Estados transversales: `:disabled{opacity:.45;pointer-events:none}`,
`.loading{color:transparent!important}+::after spinner`,
`:focus-visible{box-shadow:0 0 0 3px ring}`.
Sizes sm/lg cambian height+padding+font.

### Segmented (glider)
```html
<div class="cat-segmented" data-cat-segmented role="radiogroup">
  <button class="seg-btn is-active" aria-pressed="true">Icons</button>
  <button class="seg-btn" aria-pressed="false">List</button>
</div>
```
Contenedor relative, padding 2px. Glider absoluto top/bottom 2px que se MUEVE:
```css
.seg-btn.is-active{background:none;color:ink-hi;font-weight:600}
[data-cat-segmented]>.glider{transition:transform 240ms spring,width 240ms spring}
```
JS del core mide offsetLeft/offsetWidth del activo y anima translateX.
NUNCA aparece/desaparece: SE DESPLAZA.

### Menu
Trigger `[data-cat-menu-trigger]` dentro de `[data-cat-menu]`. Panel absolute.
**Flip automatico:** al abrir, JS mide espacio inferior; si `< menuHeight+12`,
agrega `.up` (bottom:calc(100%+6px)). Items 27px; **hover = accent fill + texto blanco**
(HIG macOS); checked muestra check svg; kbd a la derecha en low.

### Dialog
`<dialog class="cat-dialog">` nativo: foco, ESC y ::backdrop gratis.
Backdrop rgba(10,12,24,.38)+blur(6px). Actions alineadas derecha,
primary a la derecha, UNO solo por dialog.

---

## 2. ENTRADA

### Input / Field
```css
.cat-field{width:100%;max-width:320px;display:flex;flex-direction:column;gap:4px}
.cat-input>.el{height:30px;padding:0 12px;border-radius:10px;
  border:1px solid stroke-input;background:var(--input-a)}
.cat-input:focus-within>.el{
  background:var(--input-focus-a);border-color:accent-dynamic;
  box-shadow:0 0 0 3px accent-ring}
```
- Icono lider solo cuando ayuda scanning (busqueda). padding-left 32.
- Error: wrapper `.is-error` + `.field-msg` debajo. NUNCA alerts.
- Select: appearance none + chevron svg data-uri derecha.
- Textarea: min-height 84, resize vertical.

### Switch / Checkbox / Radio
Switch: label > input oculto + span.track. Checked = accent fill, knob 18px
translateX(16) spring. Focus-visible ring en track. Checkbox: box 17px radius 4,
check via borders rotados. Radio: circle + dot interior scale.

### Slider
Track 4px, thumb 15px blanco (HIG: zona interactiva mayor que visual).
Accent variant pinta sub-track.

### Rating
5 botones `.star` con SVG star fill currentColor. Estado `.on` = warning color.
JS core maneja hover preview y click (data-value inicial).

### Dropzone
Dashed border input-color; hover/dragover = accent border + subtle-a bg.

### File-chip
Icono tipo + nombre truncate + peso + X. `.uploading` agrega "..." animado.

### Color picker
Swatches circulares 22px; `.active` ring doble blanco+color; auto = arcoíris conic.
Click setea accent+ring semanticos en documentElement.

---

## 3. NAVEGACION

### Tabs (GLIDER — firma del sistema)
```css
.cat-tabs{position:relative;display:inline-flex;gap:5px}
[data-cat-tabs]>.glider{position:absolute;top:0;bottom:0;left:0;width:max-content;
  border-radius:7px;background:var(--tab-a);border:1px solid stroke-dark;
  box-shadow:0 1px 2px rgba(25,35,65,.10);
  transition:transform 240ms spring,width 240ms spring;opacity:0;z-index:0}
.cat-tab{position:relative;z-index:1;background:none!important}
```
El glider ES el tab activo visualmente. Los tabs solo cambian peso/color.
JS mide y anima translateX. Paneles sincronizados via `data-cat-panel-for`.

### Mobile tabbar
Pill glass horizontal, item activo accent (icono+label). Fixed bottom bajo 520px.

### Breadcrumb + Toolbar
Crumb actual weight 600 ink-hi; anteriores low con chevron sep.
Toolbar banda accent 10% conectada al body (radius arriba solo).

### Sidebar-nav
Ver skill catalinas-web seccion 6. Active LLENO accent.

### Pagination / Stepper / Tree-view / App-header
Pagination: botones 28px, active accent fill. Stepper: circles 24px conectados
por lineas, done=accent. Tree: indent 22px + linea vertical softer.
App-header: brand + nav links (active weight) + spacer + accion primaria.

---

## 4. DATOS

### List agrupada + Status bar
Ver skill catalinas-web secciones 7-8. Comportamiento:
`data-cat-selectable` en contenedor de rows + `data-cat-statusbar="#sb"`.
Ctrl/Meta = multi. Un click limpia las demas. Status refleja icono+nombre o count.

### Table
Header uppercase xs low; td border-bottom softer; hover negro 4%;
selected = accent fill blanco. Sin zebra (scanning por whitespace).

### Key-value list
dl/div flex space-between, separadores softer, dt mid / dd hi weight 500.

### Meter semantico
Barra 5px; color chunk segun valor: <60 success, <85 warning, >=85 danger.

### Filter chips
Multi-toggle real (checkbox oculto). `.active` = accent fill. Cambio dispara
evento para filtrar lista externa.

### Sparkline
`data-cat-spark="4,9,6"` + type line/bars. SVG generado por core: polyline
stroke accent 2px round, o bars violeta rx 1.5.

---

## 5. FEEDBACK

### Progress / Spinner / Skeleton
Progress 4-5px radius pill, fill accent SOLID (sin gradiente).
Indeterminado: range(0,0) + chunk animado translateX.
Spinner: border 2px accent top transparente, spin .7s linear.
Skeleton: gradiente gris 400% animado; variantes text/av.

### Alert banner (REGLA CRITICA)
```html
<div class="cat-alert info"><span class="a-icon">[svg]</span>
  <div class="a-body"><b>Titulo</b><span>Mensaje</span></div>
  <button class="t-close" data-cat-dismiss=".cat-alert">x</button></div>
```
Severidad = ICONO lider en circulo solid + tinte sutil de fondo.
**PROHIBIDO franjas/bordes laterales de color como carrier.**

### Toast queue
API: `Catalinas.toast({tone,title,message,timeout})`. Contenedor fijo
top-right 320px pointer-events none; toasts auto. Dismiss con data-cat-dismiss.

### Empty state
Orbe 64px radius 20 chip-bg + svg accent, titulo lg, mensaje max-w 300,
UNA accion primary sm.

---

## 6. SUPERFICIES

### Cards niveles
content (.87) / chip (blur chip) / float (blur float + shadow float) /
dark (player-bg + ink claro). Padding 16, radius lg.

### Windows (2 materiales)
```css
.cat-window.glass{background:surface-glass-window;backdrop-filter blur window;
  border:stroke-light;box-shadow:elevation-window+inset white}
.cat-window.solid{background:#fff;border:stroke-input}
```
Barra: title weight 600 + controles − □ X (close hover ROJO #e8382d blanco).

### Command palette
Overlay fixed + panel menu-surface 520px. Input 44px sin borde con border-bottom.
Items = menu-items (hover accent fill). Flechas mueven is-active, Enter ejecuta,
ESC cierra. Abrir con Ctrl+K si existe `[data-cat-command]`.

---

## 7. SLIDING SELECTION (patron generic reutilizable)

Cualquier grupo single-select puede tener glider:

```js
function attachGlider(container, itemSel, activeCls){
  const gl=container.appendChild(document.createElement('span'));
  gl.className='glider';
  function move(anim){
    const act=container.querySelector(itemSel+'.'+activeCls)||container.querySelector(itemSel);
    if(!act)return;
    gl.style.width=act.offsetWidth+'px';
    gl.style.transform=`translateX(${act.offsetLeft}px)`;
    gl.style.opacity='1';
    if(!anim){const t=gl.style.transition;gl.style.transition='none';
      void gl.offsetWidth;gl.style.transition=t;}
  }
  requestAnimationFrame(()=>move(false));
}
```

Reglas: el glider es el FONDO del activo (z-index 0, items z-index 1);
el item activo quita su propio background; transicion spring 240ms;
primer paint sin animacion.

---

## 8. AGREGAR WIDGET NUEVO (checklist)

1. `python3 build/new_widget.py nombre` → spec skeleton
2. Editar spec: description, anatomy, props, states COMPLETOS
   (default/hover/active/focus-visible/disabled como minimo)
3. Markup + css web usando SOLO tokens semanticos
4. QSS Qt equivalente (si aplica)
5. Docs demos: minimo 2 casos de uso reales
6. Guidance HIG: use / avoid / rules
7. `python3 build/build.py` -> verificar en docs + example
8. Si tiene behavior: agregar a CORE_JS, no inline
9. Correr build/a11y_check.py
