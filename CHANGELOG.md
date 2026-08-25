# Changelog — Catalinas Design System by Arcynox

Historia completa del sistema. Formato inspirado en Keep a Changelog, versionado semantico.
El playground previo (`fluent-glass-demo/`) es el laboratorio donde se probaron visualmente
todas las decisiones antes de convertirse en tokens.

---

## 0.8.0

### Widgets nuevos (4) -> 45
- command-palette: overlay Ctrl+K con filtrado, flechas, Enter, ESC. API Catalinas.palette(items).
- toast-queue: API Catalinas.toast({tone,title,message,timeout}) con cola fija y auto-dismiss.
- sparkline: SVG line/bars desde data-values, cero dependencias.
- form-validation: required/email/minLength declarativos, errores inline + evento cat:valid.

### Compatibilidades
- Vue 3 adapter: web/catalinas-vue.js (CatButton/CatSwitch/CatBadge/CatAvatar/CatCard/CatToast) con install() automatico.
- QSS completado: timeline, key-value-list, mobile-tabbar, rating, carousel ahora tienen estilos Qt.

### Innovaciones
- Density modes: data-density compact|cozy|comfortable via tokens de altura (controles + filas).
- RTL generator: web/catalinas.rtl.css (flip experimental de direcciones).
- A11y static check: build/a11y_check.py (aria-labels icon-only, alt, inputs sin label). Reporte actual: OK.
- CLI scaffolder: build/new_widget.py <nombre> crea spec esqueleto + buildea.

## 0.7.1

- NEW exports (6): tokens-only CSS, SCSS variables, ESM tokens module, Figma W3C DTCG,
  VS Code snippets (41, generados desde los markups reales), API JSON maquina-legible.
- NEW CLI: `--targets css,js,...` para compilacion selectiva.

## 0.7.0

- NEW widget `windows`: dos materiales de ventana de nivel app.
  - `Desktop` (vidrio acrilico): blur real del wallpaper, hairline blanca, para apps raiz.
  - `Normal` (solida): blanco opaco + hairline oscura, para documentos y ventanas hijas.
  - Ambas con barra titulo + controles minimizar/maximizar/cerrar (hover rojo).
- NEW widget `carousel`: scroll-snap horizontal + flechas prev/next generadas por runtime.
- CHANGELOG reescrito con historia completa (0.1.0 -> presente) incluyendo el trabajo del playground.

## 0.6.0

- NEW widgets (4):
  - `color-picker`: swatches de accent con estado "auto" (derivado del wallpaper). Cambia todo el UI en vivo.
  - `radius-scale`: escala visual xs->pill sobre gris neutro para elegir radio por superficie.
  - `mobile-tabbar`: bottom nav glass; bajo 520px se fija al borde inferior.
  - `typography`: escala H1-H3/body/caption + estados muted/low/faint/accent/success/danger/code/link.
- NEW `.cat-mark`: resaltado tipo seleccion de texto con `box-decoration-break: clone`. Variantes success/danger.
- DOCS: recipe "Quick find" eliminada a pedido; categorias de sidebar actualizadas.

## 0.5.x

### 0.5.2
- FIX critico: `docs/widgets.js` no se escribia desde 0.3.0 (stale v0.1.0 rompia todo el styleguide).
- NEW seleccion deslizante: glider animado para tabs y segmented (spring 240ms).
- FIX segmented reescrito a botones accesibles (aria-pressed) con glider compartido.
- FIX rating reescrito: botones SVG con hover preview y data-value inicial (clip-path+radios era fragil).
- FIX hairlines invisibles: controles sobre fondo claro usan `stroke-input` (oscura), no `stroke-light`.
  Migrados: button secondary, input, nav-seg, toolbar border, empty-orb.
- FIX recipes rotas: Quick find (grid incompleto), cards chip sobre dot-grid, Share menu sin altura.
- DOCS sidebar categorizada: Acciones / Entrada / Navegacion / Datos / Feedback / Superficies.
- EXAMPLE KittyDrive: tercer tab, sidebar real con Favorites + Locations, cache-bust ?v=052.

### 0.5.1
- NEW guidance HIG en 15 widgets clave: bloques "Usalo para / Evitalo si / Reglas".
- NEW recipes (4): Activity dashboard, File inspector, Notifications stack, Onboarding stepper ya existia -> total 10.
- FIX anti-estiramiento en previews: max-widths por componente (fields 320px, timeline/kv/statusbar/dropzone fijos).

### 0.5.0
- ICONS runtime v2: Bootstrap y System fuera. **Lucide default** via UMD async + createIcons.
  Quedan: Lucide / Remix / Tabler / Font Awesome / Phosphor. Warning si provider desconocido.
- NEW widgets (5): avatar-group, timeline, stat-card, rating, key-value-list.
- DOCS: navbar topbar eliminado; sidebar estatica con brand/version/targets; main con scroll propio.
- EXAMPLE KittyDrive pulido.
- ACCESIBILIDAD: regla global prefers-reduced-motion en el CSS generado.

## 0.4.x

### 0.4.0
- REMOVED dark theme completo (vuelve cuando haya QA visual real por componente).
- FLATTEN pass estilo HIG macOS: gradientes decorativos eliminados. Solo quedan 2 funcionales
  (skeleton shimmer). Afectados: secondary/ghost buttons, tabs activos, inputs, segmented checked,
  nav-seg, toolbar tri-tono -> tinte accent plano, progress fill, slider track, empty orb,
  app-header, plus-badge, sidebar overlay gloss, input inner highlights.
- Sombras reducidas y neutras: window 18px/60 @26%; raised = 1px.
- Primary/danger: hover/active por tokens accent-hover/accent-active en vez de filter brightness.
- RULES README: superficies planas + hairlines; gradientes decorativos prohibidos;
  severidad por icono lider; nunca franjas laterales.
- EXAMPLE KittyDrive alineado al lenguaje plano.

### 0.3.x
- 0.3.1:
  - FIX icon runtime snapshot lazy (contenido dinamico).
  - FIX font picker feedback + Google Fonts correcto.
  - DOCS quick find fuera; guidance HIG planificado.
- 0.3.0:
  - NEW targets: React bindings (`catalinas.jsx`), Flutter theme (`catalinas_theme.dart`),
    Tailwind preset (`catalinas.tw.js`), flat tokens (`tokens.flat.json`).
  - NEW dark theme experimental (deprecado en 0.4.0).
  - NEW utilities layer (spacing/radius/text/weight/flex).
  - NEW behaviors core: seleccion multiple filas + status bar contextual (`data-cat-selectable`),
    chips toggle (`data-cat-chips`), dropzone drag states.
  - NEW widgets (11): dialog, accordion, segmented, alert-banner, pagination, table,
    empty-state, app-header, dropzone, stepper, icons-runtime.
  - EXAMPLE `examples/kittydrive.html`: app completa solo con catalinas.css/js.
  - REGRESION conocida resuelta en 0.5.2: manifest docs stale.

## 0.2.0

- Multi-target decision: un source -> CSS web + QSS Qt + theme.py.
- Compilador Python stdlib puro (sin Node): resuelve tokens, valida vars, emite todos los targets.
- Specs JSON por widget con estados, variantes y templates por target.
- Styleguide vivo autogenerado desde las mismas specs (imposible que mienta).
- Primeros widgets dual-target: button, input/select/textarea, switch, menu, progress.

## 0.1.0

- Nacimiento: tokens W3C-style extraidos del playground fluent-glass-demo (122 iniciales).
- Decision fundacional: componentes nunca hardcodean valores; solo var(--cat-*).
- Depth system codificado (wallpaper < window < toolbar < dropdown < float < toast).
- Motion tokens (fast/med/slow + easings) y blur levels como tokens.
- Derivation rule: hue dominante del wallpaper -> accent/glass/toolbar/seleccion.

---

## Principios estables (no negociables)

1. Un solo source: `tokens.json` + `spec/*.json`.
2. Severidad con icono lider + tinte sutil. Jamas franjas laterales.
3. Legibilidad > transparencia: contenido mas opaco que chrome.
4. Glass es material por capa, no decoracion global.
5. Superficies planas + hairlines. Gradientes decorativos prohibidos (solo skeleton).
6. Zona interactiva mayor que el elemento visual (sliders, switches).
7. prefers-reduced-motion respeta todas las animaciones.
