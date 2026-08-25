# Catalinas Design System

Design system multi-plataforma con un unico source de verdad: `tokens/tokens.json` + `spec/*.json` compilan a Web (CSS/JS), React, Vue 3, Qt (QSS/Python), Flutter, Tailwind y Figma.

**Autor:** Arcynox · **Version:** 0.8.1 · **Licencia:** MIT con atribucion (ver LICENSE)

---

## Como funciona

```
tokens/tokens.json     147 tokens W3C-style (color/spacing/radius/type/elevation/motion/depth)
spec/*.json            45 widgets: anatomia, props, estados, guidance HIG y templates por target
        |
        v
build/build.py         compilador stdlib Python puro (cero dependencias)
        |
        +-- web/catalinas.css            vars + temas + utilities + componentes
        +-- web/catalinas.js             behaviors (menus, tabs deslizantes, seleccion, toasts, palette)
        +-- web/catalinas.jsx            bindings React
        +-- web/catalinas-vue.js         bindings Vue 3
        +-- qt/catalinas.qss             stylesheet Qt (tokens resueltos)
        +-- qt/theme.py                  TOKENS dict + load_qss(app)
        +-- flutter/catalinas_theme.dart CatColors / CatRadius / catLightTheme()
        +-- tailwind/catalinas.tw.js     preset Tailwind
        +-- figma/tokens.tokens.json     W3C DTCG para Tokens Studio
        +-- snippets/catalinas.json      VS Code snippets (uno por widget)
        +-- api/api.json                 manifest maquina-legible
        +-- docs/index.html              styleguide vivo
```

Un cambio en un spec JSON regenera todos los targets. Los componentes nunca hardcodean valores: solo `var(--cat-*)` en web y `{$token.path$}` en Qt.

## Quick start

```bash
python3 build/build.py                        # compilar todo
python3 build/build.py --targets css,docs    # compilacion selectiva
python3 build/a11y_check.py                   # auditoria estatica accesibilidad
python3 build/new_widget.py mi-widget         # scaffolder de widget nuevo
```

### Web

```html
<link rel="stylesheet" href="web/catalinas.css">
<script src="web/catalinas.js"></script>
<button class="cat-btn primary">Aceptar</button>
```

React: `import { CatButton } from './web/catalinas.jsx'` · Vue: registrar `CatalinasVue`.

### Qt / PySide6

```python
from qt import theme
theme.load_qss(app)
color = theme.get("color.accent.base")
```

### APIs de runtime (web)

| API | Descripcion |
|---|---|
| `Catalinas.toast({tone,title,message,timeout})` | cola de notificaciones |
| `Catalinas.palette(items)` | command palette global (Ctrl+K) |
| `CatalinasIcons.use('lucide')` | cambia el pack de iconos en vivo |

Iconos: `<span data-cat-icon="folder"></span>` — providers: lucide (default), remix, tabler, fa, phosphor.

## Exports completos

| Target | Archivo |
|---|---|
| Web CSS completo / tokens only | `web/catalinas.css` / `web/catalinas.tokens.css` |
| Web behaviors JS | `web/catalinas.js` |
| React bindings | `web/catalinas.jsx` |
| Vue 3 bindings | `web/catalinas-vue.js` |
| SCSS variables | `web/_catalinas.scss` |
| ESM tokens | `web/catalinas.tokens.mjs` |
| RTL experimental | `web/catalinas.rtl.css` |
| Qt stylesheet + theme | `qt/catalinas.qss` + `qt/theme.py` |
| Flutter theme | `flutter/catalinas_theme.dart` |
| Tailwind preset | `tailwind/catalinas.tw.js` |
| Figma DTCG | `figma/tokens.tokens.json` |
| VS Code snippets | `snippets/catalinas.json` |
| API manifest | `api/api.json` |
| Flat interop | `tokens/tokens.flat.json` |

CLI selectivo: `--targets css,js,qss,py,react,vue,flutter,tailwind,tokens-css,scss,mjs,dtcg,snippets,api,rtl,docs`

## Widgets (45)

- **Acciones:** button (5 variantes x 3 sizes + loading), segmented (glider animado), menu, dialog
- **Entrada:** input/select/textarea, checkbox/radio, switch, slider, rating, dropzone, file-chip, color-picker, form-validation
- **Navegacion:** tabs (deslizantes), mobile-tabbar, breadcrumb/toolbar, sidebar-nav, app-header, pagination, tree-view, stepper
- **Datos:** list-statusbar, table, key-value-list, meter, filter-chips, sparkline
- **Feedback:** progress/spinner/skeleton, alert-banner, card/toast-queue, empty-state, timeline, stat-card
- **Superficies:** windows (desktop glass + normal solida), carousel, icons-runtime, window-chrome, app-shell

## Principios

1. Un solo source. Todos los targets derivan.
2. Severidad con icono lider + tinte sutil. Nunca franjas laterales de color.
3. Legibilidad sobre transparencia: el contenido es mas opaco que el chrome.
4. Glass es material por capa, no decoracion global. Superficies planas + hairlines.
5. Zona interactiva mayor que el elemento visual.
6. `prefers-reduced-motion` apaga todas las animaciones.
7. Widget nuevo = spec primero, codigo despues (`new_widget.py`).

## Theming

```js
// accent en runtime (en produccion viene del hue del wallpaper)
document.documentElement.style.setProperty('--cat-semantic-accent-dynamic', 'hsl(215 85% 60%)');

// densidad
document.documentElement.dataset.density = 'compact'; // compact | cozy | comfortable

// iconos
window.CatalinasIcons.use('tabler');
```

Fuentes: overridear `--cat-font-family-ui`. El sistema completo sigue la familia elegida.

## Documentacion

- Styleguide vivo con demos, guidance HIG y use cases: abrir `docs/index.html`
- Ejemplo real armado solo con el sistema: `examples/kittydrive.html`

## Roadmap

Pendientes: visual regression screenshots por demo, plugin interactivo de Figma, virtualized list, date picker, chart primitives avanzados.

## Licencia

MIT con atribucion — libre para usar, modificar y distribuir manteniendo el credito **"Design System: Catalinas by Arcynox"**. Ver archivo [LICENSE](LICENSE).
