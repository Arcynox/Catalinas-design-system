---
name: catalinas-motion-a11y
description: Skill de motion, accesibilidad y microinteracciones del design system Catalinas (by Arcynox). Cubre tokens de motion y easings, la regla prefers-reduced-motion, focus-visible rings, aria-labels en iconos solos, navegacion por teclado (command palette, menus), jerarquia de severidad accesible y el checklist de calidad HIG. Usar al animar cualquier componente Catalinas o al auditar accesibilidad de una UI construida con el sistema.
---

# Catalinas Motion & Accessibility

> El sistema se siente premium por su MOTION contenido y por no excluir a nadie.
> Este skill cubre como mover cosas (poco y bien) y como garantizar que todo
> sea operable por teclado y lectores de pantalla.

---

## 1. TOKENS DE MOTION

```css
--cat-motion-fast:120ms;   /* hovers, color changes, chips */
--cat-motion-med:180ms;    /* dropdowns, gliders cortos */
--cat-motion-slow:260ms;   /* panels, switch knob, glider largo */
--cat-motion-ease-out:cubic-bezier(.2,.7,.3,1);   /* default: entra rapido sale suave */
--cat-motion-spring:cubic-bezier(.25,.8,.3,1.2);  /* knobs, gliders: leve overshoot */
```

### Reglas de uso

| Interaccion | Duracion | Easing |
|---|---|---|
| hover bg/color | fast | ease-out |
| press scale (.97) | fast | ease-out |
| menu open/close | fast | ease-out + translateY(-4px) |
| switch knob | slow | spring |
| tab/segmented glider | med-slow (240ms) | spring |
| toast auto-dismiss | med | ease-out + translateY(6px) |
| progress fill width | slow | ease-out |

PROHIBIDO:
- Duraciones > 400ms en UI chrome.
- bounce/elastic exagerado (spring maximo overshoot 1.2).
- Animar layout properties (top/left/width sin transform) — usa transform.

### Glider deslizante (patron firma)

La seleccion NUNCA aparece/desaparece: SE DESPLAZA del item viejo al nuevo.

```js
function move(anim){
  const act = container.querySelector(sel+'.'+activeCls)||container.querySelector(sel);
  if(!act)return;
  gl.style.width=act.offsetWidth+'px';
  gl.style.transform=`translateX(${act.offsetLeft}px)`;
  if(!anim){const t=gl.style.transition;gl.style.transition='none';
    void gl.offsetWidth;gl.style.transition=t;} // primer paint sin animar
}
requestAnimationFrame(()=>move(false));
```

Aplica a: tabs, segmented. El gliver es fondo z-0; items z-1 sin background propio.

---

## 2. REDUCED MOTION

Bloque obligatorio en todo proyecto (el compilador lo inyecta):

```css
@media (prefers-reduced-motion: reduce){
  *,*::before,*::after{animation-duration:.01ms!important;
    animation-iteration-count:1!important;
    transition-duration:.01ms!important;
    scroll-behavior:auto!important}}
```

Efecto: gliders/toasts/spinners aparecen en estado final instantaneo.
Nada se rompe funcionalmente.

---

## 3. FOCUS VISIBLE (teclado primero)

Todo interactivo recibe ring accent al navegar con teclado:

```css
:focus{outline:none} /* mouse click NO muestra ring */
button:focus-visible,[tabindex]:focus-visible{
  outline:2px solid var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base));
  outline-offset:2px}
.cat-switch input:focus-visible+.track,
.chip:has(input:focus-visible){
  box-shadow:0 0 0 3px var(--cat-semantic-accent-ring)}
```

Reglas:
- `focus-visible` (no `:focus`): el ring no debe aparecer al hacer clic.
- Ring = accent al 15% alpha, 3px, radius heredado.
- Inputs usan border-color accent + ring combinados.

---

## 4. ARIA: LO MINIMO OBLIGATORIO

### Icon-only buttons
TODO boton cuyo contenido sea solo svg REQUIERE aria-label:

```html
<button class="win-btn" aria-label="Minimize">[svg]</button>
<button class="star" aria-label="4 estrellas">[svg]</button>
```

### Roles de composicion
| Patron | Atributos |
|---|---|
| Tabs | container `role=tablist`; cada tab `role=tab` + `aria-selected`; paneles `role=tabpanel` |
| Menu | container `role=menu`; items `role=menuitem` |
| Command palette | dialog `role=dialog` `aria-modal=true`; lista `role=listbox`; items `role=option` |
| Switch | input checkbox nativo (heredado gratis) |
| Segmented | container `role=radiogroup`; botones `aria-pressed` |

### Formularios
- Label visible SIEMPRE (placeholder no es label).
- Errores inline bajo el campo (`role=alert` opcional para anunciarlo).
- Submit invalido previene default y enfoca el primer campo con error.

---

## 5. TECLADO

Patrones ya implementados en el core (no reinventar):

**Menus:** ESC cierra. Click fuera cierra. Trigger alterna aria-expanded.
**Command palette:** Ctrl+K/Cmd+K abre; ArrowDown/Up ciclan is-active con
scrollIntoView nearest; Enter ejecuta el activo; ESC cierra.
**Tabs:** click cambia; (extensible: flechas mueven foco entre tabs).
**Filas seleccionables:** click selecciona; Ctrl/Meta multi-seleccion;
status bar contextual se actualiza siempre.
**Dialog nativo:** ESC y foco trapped automaticamente.

Al agregar un widget interactivo nuevo, definí su teclado ANTES que su mouse.

---

## 6. SEVERIDAD ACCESIBLE

Color JAMAS es el unico carrier:

```html
<div class="cat-alert danger">
  <span class="a-icon" style="background:var(--cat-color-danger-base)">
    <svg><!-- X icon --></svg></span>
  <div class="a-body"><b>Titulo accionable</b><span>Descripcion clara</span></div>
</div>
```

- Icono lider (forma distinta por severidad: info=circle-i, success=check,
  warning=triangle, danger=x).
- Texto explicito ("Backup completo", "Espacio bajo").
- Tinte de fondo sutil como refuerzo terciario.
- PROHIBIDO franjas laterales de color como unico carrier (regla del sistema).

---

## 7. CONTRASTE Y HAIRLINES

- Hairlines sobre claro: rgba oscura translucida (stroke-input .14).
- Hairlines sobre vidrio/wallpaper: blanca translucida (.55).
- Ink hi (#1c2436) sobre content (.87 blanco) = ratio > 12:1.
- Placeholder/metadata nunca por debajo de ink-low (#59627a ≈ 5:1).
- Texto sobre accent fill: blanco puro; iconos del row iluminados via filter.

Si un componente nuevo necesita un color que no existe en tokens, es señal
de que falta un token — agregalo, no hardcodees.

---

## 8. CHECKLIST FINAL (auditoria express)

- [ ] prefers-reduced-motion bloqueando todo
- [ ] Ningun transition > 400ms
- [ ] focus-visible con ring accent en 100% de interactivo
- [ ] Botones icon-only: aria-label presente
- [ ] img con alt
- [ ] Inputs con label visible o aria-label
- [ ] Menus: ESC + click-outside + aria-expanded
- [ ] Palette: flechas + Enter + ESC + role option/listbox
- [ ] Severidad: icono lider + texto, color como refuerzo
- [ ] Gliders respetan reduced-motion
- [ ] Status bar refleja seleccion por texto (no solo color)
