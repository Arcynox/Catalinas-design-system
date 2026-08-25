/* generated */
window.CATALINAS = {
 "version": "0.8.1",
 "widgets": [
  {
   "name": "accordion",
   "description": "Colapsable nativo <details>, sin JS.",
   "states": [
    "open",
    "closed",
    "hover"
   ],
   "docs": {
    "demos": [
     "<div style=\"width:340px\"><details class=\"cat-accordion\" open><summary>KittyDrive<svg class=\"chev\" width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M6 9l6 6 6-6\"/></svg></summary><div class=\"body\">Projects, Photos y Backups sincronizados.</div></details><details class=\"cat-accordion\"><summary>Red<svg class=\"chev\" width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M6 9l6 6 6-6\"/></svg></summary><div class=\"body\">2 equipos conectados.</div></details></div>"
    ]
   },
   "has_js": false,
   "demos": [
    "<div style=\"width:340px\"><details class=\"cat-accordion\" open><summary>KittyDrive<svg class=\"chev\" width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M6 9l6 6 6-6\"/></svg></summary><div class=\"body\">Projects, Photos y Backups sincronizados.</div></details><details class=\"cat-accordion\"><summary>Red<svg class=\"chev\" width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M6 9l6 6 6-6\"/></svg></summary><div class=\"body\">2 equipos conectados.</div></details></div>"
   ]
  },
  {
   "name": "alert-banner",
   "description": "Banner de estado con icono lider y tinte de fondo por severidad. Sin franjas laterales ni bordes semanticos.",
   "states": [
    "info",
    "success",
    "warning",
    "danger",
    "dismissed"
   ],
   "rules": [
    "Severidad se comunica con ICONO LIDER + tinte sutil del contenedor.",
    "Nunca usar barras o bordes laterales de color como unico carrier de severidad."
   ],
   "docs": {
    "demos": [
     "<div class=\"cat-alert info\" style=\"width:400px\"><span class=\"a-icon\" style=\"background:var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base))\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"M12 8h.01M12 11v5\"/></svg></span><div class=\"a-body\"><b>Nuevo dispositivo</b><span>KittyDrive se conecto a tu laptop.</span></div><button class=\"t-close\" data-cat-dismiss=\".cat-alert\">x</button></div>",
     "<div class=\"cat-alert success\" style=\"width:400px\"><span class=\"a-icon\" style=\"background:var(--cat-color-success)\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.6\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M5 13l4 4 10-10\"/></svg></span><div class=\"a-body\"><b>Backup completo</b><span>4.33 GB sincronizados.</span></div><button class=\"t-close\" data-cat-dismiss=\".cat-alert\">x</button></div>",
     "<div class=\"cat-alert warning\" style=\"width:400px\"><span class=\"a-icon\" style=\"background:var(--cat-color-warning)\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 4L2 20h20z\"/><path d=\"M12 10v4m0 3h.01\"/></svg></span><div class=\"a-body\"><b>Espacio bajo</b><span>Quedan 12 GB en KittyDrive.</span></div><button class=\"t-close\" data-cat-dismiss=\".cat-alert\">x</button></div>"
    ]
   },
   "guidance": {
    "use": [
     "Estado del sistema que el usuario debe notar sin bloquearlo."
    ],
    "avoid": [
     "Feedback de una accion del usuario: eso es toast."
    ],
    "rules": [
     "Severidad = icono lider + tinte sutil. Jamas franjas laterales."
    ]
   },
   "has_js": false,
   "demos": [
    "<div class=\"cat-alert info\" style=\"width:400px\"><span class=\"a-icon\" style=\"background:var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base))\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"M12 8h.01M12 11v5\"/></svg></span><div class=\"a-body\"><b>Nuevo dispositivo</b><span>KittyDrive se conecto a tu laptop.</span></div><button class=\"t-close\" data-cat-dismiss=\".cat-alert\">x</button></div>",
    "<div class=\"cat-alert success\" style=\"width:400px\"><span class=\"a-icon\" style=\"background:var(--cat-color-success)\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.6\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M5 13l4 4 10-10\"/></svg></span><div class=\"a-body\"><b>Backup completo</b><span>4.33 GB sincronizados.</span></div><button class=\"t-close\" data-cat-dismiss=\".cat-alert\">x</button></div>",
    "<div class=\"cat-alert warning\" style=\"width:400px\"><span class=\"a-icon\" style=\"background:var(--cat-color-warning)\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 4L2 20h20z\"/><path d=\"M12 10v4m0 3h.01\"/></svg></span><div class=\"a-body\"><b>Espacio bajo</b><span>Quedan 12 GB en KittyDrive.</span></div><button class=\"t-close\" data-cat-dismiss=\".cat-alert\">x</button></div>"
   ]
  },
  {
   "name": "app-header",
   "description": "Barra superior de aplicacion: marca, navegacion y acciones.",
   "docs": {
    "demos": [
     "<header class=\"cat-appheader\"><span class=\"brand\">KittyDrive</span><nav><a class=\"is-active\">Archivos</a><a>Compartido</a><a>Papelera</a></nav><span class=\"spacer\"></span><button class=\"cat-btn primary sm\">Subir</button></header>"
    ]
   },
   "has_js": false,
   "demos": [
    "<header class=\"cat-appheader\"><span class=\"brand\">KittyDrive</span><nav><a class=\"is-active\">Archivos</a><a>Compartido</a><a>Papelera</a></nav><span class=\"spacer\"></span><button class=\"cat-btn primary sm\">Subir</button></header>"
   ]
  },
  {
   "name": "app-shell",
   "description": "Layout de aplicacion completa: chrome + toolbar + sidebar + contenido + statusbar. Grid unico.",
   "docs": {
    "demos": [
     "<div class=\"cat-appshell\" style=\"height:auto;min-height:300px\"><header class=\"cat-shell-chrome\"><div class=\"cat-tabs\"><button class=\"cat-tab is-active\">Documents</button><button class=\"cat-tab\">Music</button></div></header><div class=\"cat-shell-toolbar\"><span style=\"font-size:12px;font-weight:600;padding-left:4px\">Add New</span></div><div class=\"cat-shell-body\"><aside class=\"cat-sidebar\"><div class=\"cat-nav-item active\">Documents</div><div class=\"cat-nav-item\">Music</div></aside><main class=\"cat-shell-main\"><div class=\"file-scroll\" style=\"padding:10px 20px;font-size:13px;color:var(--cat-color-ink-mid)\">Contenido</div></main></div><footer class=\"cat-statusbar\"><span class=\"cat-status-title\">No file selected</span><span class=\"cat-status-count\">4 folders, 67 files</span></footer></div>"
    ]
   },
   "has_js": false,
   "demos": [
    "<div class=\"cat-appshell\" style=\"height:auto;min-height:300px\"><header class=\"cat-shell-chrome\"><div class=\"cat-tabs\"><button class=\"cat-tab is-active\">Documents</button><button class=\"cat-tab\">Music</button></div></header><div class=\"cat-shell-toolbar\"><span style=\"font-size:12px;font-weight:600;padding-left:4px\">Add New</span></div><div class=\"cat-shell-body\"><aside class=\"cat-sidebar\"><div class=\"cat-nav-item active\">Documents</div><div class=\"cat-nav-item\">Music</div></aside><main class=\"cat-shell-main\"><div class=\"file-scroll\" style=\"padding:10px 20px;font-size:13px;color:var(--cat-color-ink-mid)\">Contenido</div></main></div><footer class=\"cat-statusbar\"><span class=\"cat-status-title\">No file selected</span><span class=\"cat-status-count\">4 folders, 67 files</span></footer></div>"
   ]
  },
  {
   "name": "avatar-group",
   "description": "Stack de avatares con overlap y contador restante.",
   "docs": {
    "demos": [
     "<div class=\"cat-avgroup\"><span class=\"cat-avatar\">LU</span><span class=\"cat-avatar\">MI</span><span class=\"cat-avatar\">CO</span><span class=\"cat-avatar more\">+5</span></div>"
    ]
   },
   "has_js": false,
   "demos": [
    "<div class=\"cat-avgroup\"><span class=\"cat-avatar\">LU</span><span class=\"cat-avatar\">MI</span><span class=\"cat-avatar\">CO</span><span class=\"cat-avatar more\">+5</span></div>"
   ]
  },
  {
   "name": "badge-tooltip-kbd-avatar",
   "description": "Micro-componentes: badge, tooltip CSS-only, tecla, divisor y avatar.",
   "docs": {
    "demos": [
     "<span class=\"cat-badge accent\">Beta</span> <span class=\"cat-badge success\"><span class=\"dot\"></span>Online</span> <span class=\"cat-badge\">v0.1</span>",
     "<button class=\"cat-btn secondary\" data-cat-tooltip=\"¡Hola! Soy un tooltip\">Hover me</button>",
     "<span class=\"cat-kbd\">Ctrl</span> <span class=\"cat-kbd\">K</span>",
     "<hr class=\"cat-divider\" style=\"width:200px\">",
     "<span class=\"cat-avatar\">LU<span class=\"presence\"></span></span>"
    ]
   },
   "has_js": false,
   "demos": [
    "<span class=\"cat-badge accent\">Beta</span> <span class=\"cat-badge success\"><span class=\"dot\"></span>Online</span> <span class=\"cat-badge\">v0.1</span>",
    "<button class=\"cat-btn secondary\" data-cat-tooltip=\"¡Hola! Soy un tooltip\">Hover me</button>",
    "<span class=\"cat-kbd\">Ctrl</span> <span class=\"cat-kbd\">K</span>",
    "<hr class=\"cat-divider\" style=\"width:200px\">",
    "<span class=\"cat-avatar\">LU<span class=\"presence\"></span></span>"
   ]
  },
  {
   "name": "breadcrumb-toolbar",
   "description": "Ruta jerárquica + banda de acciones con gradiente de identidad.",
   "docs": {
    "demos": [
     "<nav class=\"cat-breadcrumb\"><span class=\"crumb\">This PC</span><span class=\"sep\">›</span><span class=\"crumb current\">Documents</span></nav>",
     "<div class=\"cat-toolbar\"><button class=\"cat-tool-btn primary\"><span class=\"plus\">+</span>Add New</button><span class=\"cat-tool-sep\"></span><button class=\"cat-tool-btn\">Organize ▾</button><button class=\"cat-tool-btn\">View ▾</button></div>"
    ]
   },
   "has_js": false,
   "demos": [
    "<nav class=\"cat-breadcrumb\"><span class=\"crumb\">This PC</span><span class=\"sep\">›</span><span class=\"crumb current\">Documents</span></nav>",
    "<div class=\"cat-toolbar\"><button class=\"cat-tool-btn primary\"><span class=\"plus\">+</span>Add New</button><span class=\"cat-tool-sep\"></span><button class=\"cat-tool-btn\">Organize ▾</button><button class=\"cat-tool-btn\">View ▾</button></div>"
   ]
  },
  {
   "name": "button",
   "description": "Acción primaria, secundaria, fantasma, peligrosa o enlace.",
   "anatomy": [
    "container",
    "label",
    "icon"
   ],
   "props": {
    "variant": "primary|secondary|ghost|danger|link",
    "size": "sm|md|lg",
    "icon": "optional",
    "loading": "bool",
    "disabled": "bool"
   },
   "states": [
    "default",
    "hover",
    "active",
    "focus-visible",
    "disabled"
   ],
   "docs": {
    "demos": [
     "<button class=\"cat-btn primary\">Primary</button><button class=\"cat-btn secondary\">Secondary</button><button class=\"cat-btn ghost\">Ghost</button><button class=\"cat-btn danger\">Danger</button><button class=\"cat-btn link\">Link</button><span style=\"width:12px\"></span><button class=\"cat-btn primary sm\">Small</button><button class=\"cat-btn primary loading\">Loading</button><button class=\"cat-btn primary disabled\">Disabled</button>"
    ]
   },
   "guidance": {
    "use": [
     "Accion principal de una vista: una sola primary por pantalla.",
     "Danger solo para acciones destructivas e irreversibles."
    ],
    "avoid": [
     "Botones ghost para acciones criticas: poca affordance.",
     "Tres o mas botones en fila: convertilo en menu."
    ],
    "rules": [
     "Orden HIG: primario a la derecha en dialogos, a la izquierda en toolbars.",
     "Loading deshabilita el boton; nunca doble submit."
    ]
   },
   "has_js": false,
   "demos": [
    "<button class=\"cat-btn primary\">Primary</button><button class=\"cat-btn secondary\">Secondary</button><button class=\"cat-btn ghost\">Ghost</button><button class=\"cat-btn danger\">Danger</button><button class=\"cat-btn link\">Link</button><span style=\"width:12px\"></span><button class=\"cat-btn primary sm\">Small</button><button class=\"cat-btn primary loading\">Loading</button><button class=\"cat-btn primary disabled\">Disabled</button>"
   ]
  },
  {
   "name": "card-toast",
   "description": "Superficies por nivel de profundidad + notificaciones descartables.",
   "docs": {
    "demos": [
     "<div style=\"display:flex;gap:12px;flex-wrap:wrap\"><div class=\"cat-card\" style=\"width:170px\">Card L2 contenido casi opaco</div><div class=\"cat-card chip\" style=\"width:170px\">Card chip translúcida</div><div class=\"cat-card dark\" style=\"width:170px\">Card dark funcional</div><div class=\"cat-card float\" style=\"width:170px\">Card float glass</div></div>",
     "<div class=\"cat-toast\" style=\"position:static;margin-top:12px\"><span class=\"t-icon success\"></span><span>Backup completado</span><button class=\"t-close\" data-cat-dismiss=\".cat-toast\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><path d=\"M6 6l12 12M18 6L6 18\"/></svg></button></div>"
    ]
   },
   "has_js": false,
   "demos": [
    "<div style=\"display:flex;gap:12px;flex-wrap:wrap\"><div class=\"cat-card\" style=\"width:170px\">Card L2 contenido casi opaco</div><div class=\"cat-card chip\" style=\"width:170px\">Card chip translúcida</div><div class=\"cat-card dark\" style=\"width:170px\">Card dark funcional</div><div class=\"cat-card float\" style=\"width:170px\">Card float glass</div></div>",
    "<div class=\"cat-toast\" style=\"position:static;margin-top:12px\"><span class=\"t-icon success\"></span><span>Backup completado</span><button class=\"t-close\" data-cat-dismiss=\".cat-toast\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><path d=\"M6 6l12 12M18 6L6 18\"/></svg></button></div>"
   ]
  },
  {
   "name": "carousel",
   "description": "Carrusel horizontal con scroll-snap y flechas prev/next.",
   "docs": {
    "demos": [
     "<div class=\"car-wrap\"><div class=\"car-head\"><b>Favoritos</b><span class=\"car-nav\"><button data-cat-car-prev aria-label=\"Anterior\">&#8249;</button><button data-cat-car-next aria-label=\"Siguiente\">&#8250;</button></span></div><div class=\"cat-carousel\"><div class=\"slide\"><b>Favoritos</b><span>12 items</span></div><div class=\"slide\"><b>Recientes</b><span>67 items</span></div><div class=\"slide\"><b>Compartidos</b><span>8 items</span></div><div class=\"slide\"><b>Papelera</b><span>3 items</span></div><div class=\"slide\"><b>Descargas</b><span>21 items</span></div></div></div>"
    ]
   },
   "has_js": true,
   "demos": [
    "<div class=\"car-wrap\"><div class=\"car-head\"><b>Favoritos</b><span class=\"car-nav\"><button data-cat-car-prev aria-label=\"Anterior\">&#8249;</button><button data-cat-car-next aria-label=\"Siguiente\">&#8250;</button></span></div><div class=\"cat-carousel\"><div class=\"slide\"><b>Favoritos</b><span>12 items</span></div><div class=\"slide\"><b>Recientes</b><span>67 items</span></div><div class=\"slide\"><b>Compartidos</b><span>8 items</span></div><div class=\"slide\"><b>Papelera</b><span>3 items</span></div><div class=\"slide\"><b>Descargas</b><span>21 items</span></div></div></div>"
   ]
  },
  {
   "name": "checkbox-radio",
   "description": "Selección múltiple y exclusiva.",
   "states": [
    "checked",
    "focus-visible",
    "disabled"
   ],
   "docs": {
    "demos": [
     "<label class=\"cat-check\"><input type=\"checkbox\" checked><span class=\"box\"></span>Notificar</label>",
     "<label class=\"cat-radio\"><input type=\"radio\" name=\"r1\" checked><span class=\"box\"></span>Opción 1</label> <label class=\"cat-radio\"><input type=\"radio\" name=\"r1\"><span class=\"box\"></span>Opción 2</label>"
    ]
   },
   "guidance": {
    "use": [
     "Checkbox: seleccion multiple pendiente de confirmar.",
     "Radio: 2-5 opciones exclusivas visibles de una vez."
    ],
    "avoid": [
     "Radio con mas de 5 opciones: usa select o segmented."
    ],
    "rules": [
     "Un grupo de radios nunca empieza sin opcion marcada si la eleccion es requerida."
    ]
   },
   "has_js": false,
   "demos": [
    "<label class=\"cat-check\"><input type=\"checkbox\" checked><span class=\"box\"></span>Notificar</label>",
    "<label class=\"cat-radio\"><input type=\"radio\" name=\"r1\" checked><span class=\"box\"></span>Opción 1</label> <label class=\"cat-radio\"><input type=\"radio\" name=\"r1\"><span class=\"box\"></span>Opción 2</label>"
   ]
  },
  {
   "name": "color-picker",
   "description": "Seleccion de accent para todo el sistema: swatches + auto (derivado del wallpaper).",
   "states": [
    "default",
    "hover",
    "active"
   ],
   "docs": {
    "demos": [
     "<div class=\"cat-colors\" data-cat-colors><button class=\"cat-swatch auto active\" data-auto aria-label=\"Auto\"></button><button class=\"cat-swatch\" style=\"background:#5e9eff\" data-color=\"#5e9eff\" aria-label=\"Azul\"></button><button class=\"cat-swatch\" style=\"background:#a78bfa\" data-color=\"#a78bfa\" aria-label=\"Violeta\"></button><button class=\"cat-swatch\" style=\"background:#f2a2c6\" data-color=\"#f2a2c6\" aria-label=\"Rosa\"></button><button class=\"cat-swatch\" style=\"background:#ef5a76\" data-color=\"#ef5a76\" aria-label=\"Rojo\"></button><button class=\"cat-swatch\" style=\"background:#34c759\" data-color=\"#34c759\" aria-label=\"Verde\"></button><span class=\"cat-label-side\">cambia todo el UI</span></div>",
     "<div class=\"cat-alert info\"><span class=\"a-icon\" style=\"background:var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base))\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"M12 8h.01M12 11v5\"/></svg></span><div class=\"a-body\"><b>Mira este banner</b><span>El icono sigue el accent elegido arriba.</span></div></div>"
    ],
    "note": "Auto = hue derivado del wallpaper en produccion."
   },
   "has_js": true,
   "demos": [
    "<div class=\"cat-colors\" data-cat-colors><button class=\"cat-swatch auto active\" data-auto aria-label=\"Auto\"></button><button class=\"cat-swatch\" style=\"background:#5e9eff\" data-color=\"#5e9eff\" aria-label=\"Azul\"></button><button class=\"cat-swatch\" style=\"background:#a78bfa\" data-color=\"#a78bfa\" aria-label=\"Violeta\"></button><button class=\"cat-swatch\" style=\"background:#f2a2c6\" data-color=\"#f2a2c6\" aria-label=\"Rosa\"></button><button class=\"cat-swatch\" style=\"background:#ef5a76\" data-color=\"#ef5a76\" aria-label=\"Rojo\"></button><button class=\"cat-swatch\" style=\"background:#34c759\" data-color=\"#34c759\" aria-label=\"Verde\"></button><span class=\"cat-label-side\">cambia todo el UI</span></div>",
    "<div class=\"cat-alert info\"><span class=\"a-icon\" style=\"background:var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base))\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"M12 8h.01M12 11v5\"/></svg></span><div class=\"a-body\"><b>Mira este banner</b><span>El icono sigue el accent elegido arriba.</span></div></div>"
   ]
  },
  {
   "name": "command-palette",
   "description": "Palette de comandos global (Ctrl+K / Cmd+K). Busca, navega con flechas, ejecuta con Enter.",
   "anatomy": [
    "overlay",
    "panel",
    "input",
    "results",
    "foot"
   ],
   "states": [
    "closed",
    "open",
    "filtering",
    "active-item"
   ],
   "docs": {
    "demos": [
     "<button class=\"cat-btn primary\" id=\"demoCmdkBtn\">Abrir palette (o Ctrl+K)</button>",
     "<p class=\"caption\">Con un contenedor <code>data-cat-command</code>, Ctrl+K toma los items automaticamente.</p>"
    ],
    "note": "Flechas navegan, Enter ejecuta, ESC cierra. Filtrado instantaneo."
   },
   "has_js": false,
   "demos": [
    "<button class=\"cat-btn primary\" id=\"demoCmdkBtn\">Abrir palette (o Ctrl+K)</button>",
    "<p class=\"caption\">Con un contenedor <code>data-cat-command</code>, Ctrl+K toma los items automaticamente.</p>"
   ]
  },
  {
   "name": "dialog",
   "description": "Modal nativo <dialog> con backdrop blur. Foco y ESC gratis.",
   "docs": {
    "demos": [
     "<button class=\"cat-btn secondary\" onclick=\"dlgDemo.showModal()\">Abrir dialog</button><dialog class=\"cat-dialog\" id=\"dlgDemo\"><h3>Eliminar archivo</h3><p>Esta accion no se puede deshacer.</p><div class=\"actions\"><form method=\"dialog\"><button class=\"cat-btn ghost\">Cancelar</button></form><form method=\"dialog\"><button class=\"cat-btn danger\">Eliminar</button></form></div></dialog>"
    ]
   },
   "guidance": {
    "use": [
     "Decisiones irreversibles o informacion que bloquea la tarea."
    ],
    "avoid": [
     "Formularios largos: mejor una ventana propia."
    ],
    "rules": [
     "Un solo primary; cancelar siempre visible. ESC cierra."
    ]
   },
   "has_js": false,
   "demos": [
    "<button class=\"cat-btn secondary\" onclick=\"dlgDemo.showModal()\">Abrir dialog</button><dialog class=\"cat-dialog\" id=\"dlgDemo\"><h3>Eliminar archivo</h3><p>Esta accion no se puede deshacer.</p><div class=\"actions\"><form method=\"dialog\"><button class=\"cat-btn ghost\">Cancelar</button></form><form method=\"dialog\"><button class=\"cat-btn danger\">Eliminar</button></form></div></dialog>"
   ]
  },
  {
   "name": "dropzone",
   "description": "Zona de carga drag and drop. Visual puro; estado :drag-over via clase .over (JS del host).",
   "docs": {
    "demos": [
     "<label class=\"cat-dropzone\" style=\"width:380px\"><input type=\"file\" multiple hidden><b>Solta archivos aca</b><span>o hace clic para elegir</span></label>"
    ]
   },
   "has_js": false,
   "demos": [
    "<label class=\"cat-dropzone\" style=\"width:380px\"><input type=\"file\" multiple hidden><b>Solta archivos aca</b><span>o hace clic para elegir</span></label>"
   ]
  },
  {
   "name": "empty-state",
   "description": "Estado vacio: orbe con icono, titulo, descripcion y accion primaria.",
   "anatomy": [
    "orb",
    "title",
    "message",
    "action"
   ],
   "states": [
    "default",
    "hover(action)"
   ],
   "docs": {
    "demos": [
     "<div class=\"cat-empty\"><div class=\"cat-empty-orb\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M13 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V9z\"/><path d=\"M13 3v6h6\"/><path d=\"M12 12v6m-3-3h6\"/></svg></div><h4 class=\"cat-empty-title\">Sin resultados</h4><p class=\"cat-empty-msg\">Proba con otros terminos o crea algo nuevo.</p><button class=\"cat-btn primary sm\">Crear</button></div>",
     "<div class=\"cat-empty\"><div class=\"cat-empty-orb\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M13 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V9z\"/><path d=\"M13 3v6h6\"/><path d=\"M12 12v6m-3-3h6\"/></svg></div><h4 class=\"cat-empty-title\">KittyDrive vacio</h4><p class=\"cat-empty-msg\">Arrastra archivos para empezar a sincronizar con la nube.</p><button class=\"cat-btn secondary sm\">Ver planes</button></div>"
    ]
   },
   "guidance": {
    "use": [
     "Primer uso y resultados vacios: ensena el proximo paso."
    ],
    "avoid": [
     "Culpar al usuario; tono neutro y accion claro."
    ],
    "rules": [
     "Orbe + titulo corto + una sola accion primary."
    ]
   },
   "has_js": false,
   "demos": [
    "<div class=\"cat-empty\"><div class=\"cat-empty-orb\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M13 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V9z\"/><path d=\"M13 3v6h6\"/><path d=\"M12 12v6m-3-3h6\"/></svg></div><h4 class=\"cat-empty-title\">Sin resultados</h4><p class=\"cat-empty-msg\">Proba con otros terminos o crea algo nuevo.</p><button class=\"cat-btn primary sm\">Crear</button></div>",
    "<div class=\"cat-empty\"><div class=\"cat-empty-orb\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M13 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V9z\"/><path d=\"M13 3v6h6\"/><path d=\"M12 12v6m-3-3h6\"/></svg></div><h4 class=\"cat-empty-title\">KittyDrive vacio</h4><p class=\"cat-empty-msg\">Arrastra archivos para empezar a sincronizar con la nube.</p><button class=\"cat-btn secondary sm\">Ver planes</button></div>"
   ]
  },
  {
   "name": "file-chip",
   "description": "Chip de archivo adjunto/subido: icono, nombre, peso, remover.",
   "docs": {
    "demos": [
     "<span class=\"cat-filechip\"><svg width=\"15\" height=\"15\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#5f8af5\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z\"/><path d=\"M14 3v5h5\"/></svg><span class=\"fc-name\">informe-q4.pdf</span><span class=\"fc-size\">2.4 MB</span><button class=\"fc-x\" aria-label=\"Quitar\">x</button></span> <span class=\"cat-filechip uploading\"><svg width=\"15\" height=\"15\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#e8776f\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z\"/><path d=\"M14 3v5h5\"/><path d=\"M9 14h6M9 17h4\"/></svg><span class=\"fc-name\">deck-final.pptx</span><span class=\"fc-size\">18 MB</span><button class=\"fc-x\" aria-label=\"Quitar\">x</button></span>"
    ]
   },
   "has_js": false,
   "demos": [
    "<span class=\"cat-filechip\"><svg width=\"15\" height=\"15\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#5f8af5\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z\"/><path d=\"M14 3v5h5\"/></svg><span class=\"fc-name\">informe-q4.pdf</span><span class=\"fc-size\">2.4 MB</span><button class=\"fc-x\" aria-label=\"Quitar\">x</button></span> <span class=\"cat-filechip uploading\"><svg width=\"15\" height=\"15\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#e8776f\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z\"/><path d=\"M14 3v5h5\"/><path d=\"M9 14h6M9 17h4\"/></svg><span class=\"fc-name\">deck-final.pptx</span><span class=\"fc-size\">18 MB</span><button class=\"fc-x\" aria-label=\"Quitar\">x</button></span>"
   ]
  },
  {
   "name": "filter-chips",
   "description": "Chips de filtro multi-seleccion con estado activo accent.",
   "docs": {
    "demos": [
     "<div class=\"cat-chips\" data-cat-chips><label class=\"chip active\">Documentos<input type=\"checkbox\" checked hidden></label><label class=\"chip\">Presentaciones<input type=\"checkbox\" hidden></label><label class=\"chip\">Carpetas<input type=\"checkbox\" hidden></label><label class=\"chip\">Imagenes<input type=\"checkbox\" hidden></label></div>"
    ],
    "note": "data-cat-chips activa toggle automatico de .active en catalinas.js"
   },
   "has_js": false,
   "demos": [
    "<div class=\"cat-chips\" data-cat-chips><label class=\"chip active\">Documentos<input type=\"checkbox\" checked hidden></label><label class=\"chip\">Presentaciones<input type=\"checkbox\" hidden></label><label class=\"chip\">Carpetas<input type=\"checkbox\" hidden></label><label class=\"chip\">Imagenes<input type=\"checkbox\" hidden></label></div>"
   ]
  },
  {
   "name": "form-validation",
   "description": "Validacion declarativa: required/email/minLength via atributos. Errores inline y evento cat:valid.",
   "states": [
    "valid",
    "error-inline",
    "submitted-invalid"
   ],
   "docs": {
    "demos": [
     "<form class=\"cat-form\" data-cat-validate novalidate onsubmit=\"return false\"><div class=\"cat-field\"><label class=\"cat-label\">Email *</label><div class=\"cat-input has-icon\"><span class=\"cat-icon\"><svg width=\"13\" height=\"13\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"><rect x=\"3\" y=\"5\" width=\"18\" height=\"14\" rx=\"2\"/><path d=\"M3 7l9 6 9-6\"/></svg></span><input class=\"el\" required data-cat-type=\"email\" placeholder=\"tu@email.com\"></div></div><div class=\"cat-field\"><label class=\"cat-label\">Password *</label><div class=\"cat-input\"><input class=\"el\" type=\"password\" required minlength=\"6\" placeholder=\"min 6 caracteres\"></div></div><button class=\"cat-btn primary\" style=\"align-self:flex-end\">Enviar</button></form>"
    ],
    "note": "Submit invalido -> errores inline por campo + evento cat:valid para la logica de tu app. Sin alerts."
   },
   "has_js": false,
   "demos": [
    "<form class=\"cat-form\" data-cat-validate novalidate onsubmit=\"return false\"><div class=\"cat-field\"><label class=\"cat-label\">Email *</label><div class=\"cat-input has-icon\"><span class=\"cat-icon\"><svg width=\"13\" height=\"13\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"><rect x=\"3\" y=\"5\" width=\"18\" height=\"14\" rx=\"2\"/><path d=\"M3 7l9 6 9-6\"/></svg></span><input class=\"el\" required data-cat-type=\"email\" placeholder=\"tu@email.com\"></div></div><div class=\"cat-field\"><label class=\"cat-label\">Password *</label><div class=\"cat-input\"><input class=\"el\" type=\"password\" required minlength=\"6\" placeholder=\"min 6 caracteres\"></div></div><button class=\"cat-btn primary\" style=\"align-self:flex-end\">Enviar</button></form>"
   ]
  },
  {
   "name": "icons",
   "description": "Iconos themable con runtime CatalinasIcons. Default: Lucide (SVG). Alternativas por CDN webfont.",
   "props": {
    "provider": "lucide|remix|tabler|fa|phosphor",
    "name": "folder|doc|ppt|music|img|home|cloud|desktop|cat|net"
   },
   "docs": {
    "demos": [
     "<div class=\"cat-icons-grid\"><div class=\"icell\"><span data-cat-icon=\"folder\"></span><small>folder</small></div><div class=\"icell\"><span data-cat-icon=\"doc\"></span><small>doc</small></div><div class=\"icell\"><span data-cat-icon=\"ppt\"></span><small>ppt</small></div><div class=\"icell\"><span data-cat-icon=\"music\"></span><small>music</small></div><div class=\"icell\"><span data-cat-icon=\"img\"></span><small>img</small></div><div class=\"icell\"><span data-cat-icon=\"home\"></span><small>home</small></div><div class=\"icell\"><span data-cat-icon=\"cloud\"></span><small>cloud</small></div><div class=\"icell\"><span data-cat-icon=\"desktop\"></span><small>desktop</small></div><div class=\"icell\"><span data-cat-icon=\"cat\"></span><small>cat</small></div><div class=\"icell\"><span data-cat-icon=\"net\"></span><small>net</small></div></div>"
    ],
    "note": "Default Lucide. Cambio en vivo via CatalinasIcons.use(provider)."
   },
   "has_js": true,
   "demos": [
    "<div class=\"cat-icons-grid\"><div class=\"icell\"><span data-cat-icon=\"folder\"></span><small>folder</small></div><div class=\"icell\"><span data-cat-icon=\"doc\"></span><small>doc</small></div><div class=\"icell\"><span data-cat-icon=\"ppt\"></span><small>ppt</small></div><div class=\"icell\"><span data-cat-icon=\"music\"></span><small>music</small></div><div class=\"icell\"><span data-cat-icon=\"img\"></span><small>img</small></div><div class=\"icell\"><span data-cat-icon=\"home\"></span><small>home</small></div><div class=\"icell\"><span data-cat-icon=\"cloud\"></span><small>cloud</small></div><div class=\"icell\"><span data-cat-icon=\"desktop\"></span><small>desktop</small></div><div class=\"icell\"><span data-cat-icon=\"cat\"></span><small>cat</small></div><div class=\"icell\"><span data-cat-icon=\"net\"></span><small>net</small></div></div>"
   ]
  },
  {
   "name": "input",
   "description": "Campo de texto, con icono opcional y estado de error.",
   "anatomy": [
    "wrapper",
    "input",
    "icon",
    "label",
    "message"
   ],
   "states": [
    "default",
    "placeholder",
    "focus",
    "error",
    "disabled"
   ],
   "docs": {
    "demos": [
     "<div class=\"cat-field\"><label class=\"cat-label\">Nombre</label><div class=\"cat-input has-icon\"><span class=\"cat-icon\"><svg width=\"13\" height=\"13\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"><circle cx=\"11\" cy=\"11\" r=\"7\"/><path d=\"M20 20l-3.5-3.5\"/></svg></span><input class=\"el\" placeholder=\"Buscar…\"></div></div>",
     "<div class=\"cat-field is-error\"><label class=\"cat-label\">Email</label><div class=\"cat-input\"><input class=\"el\" value=\"no-es-un-email\"></div><span class=\"field-msg\">Formato inválido</span></div>",
     "<div class=\"cat-field\"><label class=\"cat-label\">Select</label><div class=\"cat-input\"><select class=\"el\"><option>Opción A</option><option>Opción B</option></select></div></div>",
     "<div class=\"cat-field\"><label class=\"cat-label\">Mensaje</label><div class=\"cat-input\"><textarea class=\"el\"></textarea></div></div>"
    ]
   },
   "guidance": {
    "use": [
     "Datos cortos con formato predecible (email, busqueda, nombre)."
    ],
    "avoid": [
     "Placeholders como unica etiqueta: desaparecen al escribir."
    ],
    "rules": [
     "Errores inline bajo el campo, nunca dialogs.",
     "Icono lider solo cuando ayuda al scanning (busqueda)."
    ]
   },
   "has_js": false,
   "demos": [
    "<div class=\"cat-field\"><label class=\"cat-label\">Nombre</label><div class=\"cat-input has-icon\"><span class=\"cat-icon\"><svg width=\"13\" height=\"13\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\"><circle cx=\"11\" cy=\"11\" r=\"7\"/><path d=\"M20 20l-3.5-3.5\"/></svg></span><input class=\"el\" placeholder=\"Buscar…\"></div></div>",
    "<div class=\"cat-field is-error\"><label class=\"cat-label\">Email</label><div class=\"cat-input\"><input class=\"el\" value=\"no-es-un-email\"></div><span class=\"field-msg\">Formato inválido</span></div>",
    "<div class=\"cat-field\"><label class=\"cat-label\">Select</label><div class=\"cat-input\"><select class=\"el\"><option>Opción A</option><option>Opción B</option></select></div></div>",
    "<div class=\"cat-field\"><label class=\"cat-label\">Mensaje</label><div class=\"cat-input\"><textarea class=\"el\"></textarea></div></div>"
   ]
  },
  {
   "name": "key-value-list",
   "description": "Lista definicion clave/valor para metadata y propiedades.",
   "docs": {
    "demos": [
     "<dl class=\"cat-kv\" style=\"width:260px\"><div><dt>Tamano</dt><dd>4.33 GB</dd></div><div><dt>Elementos</dt><dd>67</dd></div><div><dt>Modificado</dt><dd>Aug 25, 2026</dd></div></dl>"
    ]
   },
   "has_js": false,
   "demos": [
    "<dl class=\"cat-kv\" style=\"width:260px\"><div><dt>Tamano</dt><dd>4.33 GB</dd></div><div><dt>Elementos</dt><dd>67</dd></div><div><dt>Modificado</dt><dd>Aug 25, 2026</dd></div></dl>"
   ]
  },
  {
   "name": "list-statusbar",
   "description": "Lista agrupada editorial (headers + filas) y barra de estado contextual.",
   "states": [
    "row-default",
    "row-hover",
    "row-selected(accent fill)",
    "group-head",
    "statusbar-idle",
    "statusbar-selection"
   ],
   "docs": {
    "demos": [
     "<div class=\"cat-list\" style=\"max-width:520px\"><div class=\"cat-list-header\"><span>Name</span><span>Type</span><span>Date</span></div><div class=\"cat-group-head\">File Folders</div><div class=\"cat-row selected\"><span class=\"cell-name\">Design</span><span class=\"cell-type\">Folder</span><span class=\"cell-date\">Aug 22</span></div><div class=\"cat-row\"><span class=\"cell-name\">Fonts</span><span class=\"cell-type\">Folder</span><span class=\"cell-date\">Aug 19</span></div></div><hr class=\"cat-divider\"><footer class=\"cat-statusbar\" style=\"border-radius:10px\"><div><div class=\"cat-status-title\">Design</div><div class=\"cat-status-meta\">Folder · Aug 22, 2026</div></div><span class=\"cat-status-count\">1 selected</span></footer>"
    ]
   },
   "has_js": false,
   "demos": [
    "<div class=\"cat-list\" style=\"max-width:520px\"><div class=\"cat-list-header\"><span>Name</span><span>Type</span><span>Date</span></div><div class=\"cat-group-head\">File Folders</div><div class=\"cat-row selected\"><span class=\"cell-name\">Design</span><span class=\"cell-type\">Folder</span><span class=\"cell-date\">Aug 22</span></div><div class=\"cat-row\"><span class=\"cell-name\">Fonts</span><span class=\"cell-type\">Folder</span><span class=\"cell-date\">Aug 19</span></div></div><hr class=\"cat-divider\"><footer class=\"cat-statusbar\" style=\"border-radius:10px\"><div><div class=\"cat-status-title\">Design</div><div class=\"cat-status-meta\">Folder · Aug 22, 2026</div></div><span class=\"cat-status-count\">1 selected</span></footer>"
   ]
  },
  {
   "name": "menu",
   "description": "Dropdown flotante nivel depth.dropdown. Trigger por data-attr.",
   "states": [
    "open",
    "item-hover(accent fill HIG)",
    "item-checked",
    "kbd-hint"
   ],
   "docs": {
    "demos": [
     "<div data-cat-menu><button class=\"cat-btn secondary\" data-cat-menu-trigger aria-expanded=\"false\">Sort <svg class=\"chev\" width=\"10\" height=\"10\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.6\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M6 9l6 6 6-6\"/></svg></button><div class=\"cat-menu\" role=\"menu\"><button class=\"cat-menu-item checked\" role=\"menuitem\">Name<svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M5 13l4 4 10-10\"/></svg></button><button class=\"cat-menu-item\">Date Modified</button><div class=\"cat-menu-sep\"></div><button class=\"cat-menu-item\">Size<span class=\"menu-kbd\">Ctrl+S</span></button></div></div>"
    ]
   },
   "guidance": {
    "use": [
     "Acciones secundarias que no merecen espacio permanente."
    ],
    "avoid": [
     "Acciones frecuentes: quedan en toolbar."
    ],
    "rules": [
     "Abre hacia arriba automaticamente si falta espacio abajo.",
     "Items con shortcut muestran kbd a la derecha."
    ]
   },
   "has_js": false,
   "demos": [
    "<div data-cat-menu><button class=\"cat-btn secondary\" data-cat-menu-trigger aria-expanded=\"false\">Sort <svg class=\"chev\" width=\"10\" height=\"10\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.6\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M6 9l6 6 6-6\"/></svg></button><div class=\"cat-menu\" role=\"menu\"><button class=\"cat-menu-item checked\" role=\"menuitem\">Name<svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M5 13l4 4 10-10\"/></svg></button><button class=\"cat-menu-item\">Date Modified</button><div class=\"cat-menu-sep\"></div><button class=\"cat-menu-item\">Size<span class=\"menu-kbd\">Ctrl+S</span></button></div></div>"
   ]
  },
  {
   "name": "meter",
   "description": "Medidor semantico (disco, RAM): verde/amarillo/rojo segun umbral.",
   "docs": {
    "demos": [
     "<div><div class=\"cat-meter\"><div class=\"fill\" style=\"width:34%\"></div></div><div class=\"cat-meter-label\"><span>Disco</span><span>34%</span></div></div>",
     "<div><div class=\"cat-meter danger\"><div class=\"fill\" style=\"width:91%\"></div></div><div class=\"cat-meter-label\"><span>RAM</span><span>91%</span></div></div>"
    ]
   },
   "has_js": false,
   "demos": [
    "<div><div class=\"cat-meter\"><div class=\"fill\" style=\"width:34%\"></div></div><div class=\"cat-meter-label\"><span>Disco</span><span>34%</span></div></div>",
    "<div><div class=\"cat-meter danger\"><div class=\"fill\" style=\"width:91%\"></div></div><div class=\"cat-meter-label\"><span>RAM</span><span>91%</span></div></div>"
   ]
  },
  {
   "name": "mobile-tabbar",
   "description": "Barra de navegacion inferior para movil: glass con blur, item activo accent.",
   "docs": {
    "demos": [
     "<nav class=\"cat-tabbar\" data-cat-tabs role=\"tablist\"><button type=\"button\" class=\"tb-item is-active\" data-cat-tab role=\"tab\" aria-selected=\"true\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M3 11l9-8 9 8\"/><path d=\"M5 10v10a1 1 0 0 0 1 1h4v-6h4v6h4a1 1 0 0 0 1-1V10\"/></svg><span>Inicio</span></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"11\" cy=\"11\" r=\"7\"/><path d=\"M20 20l-3.5-3.5\"/></svg><span>Buscar</span></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 5v14M5 12h14\"/></svg><span>Crear</span></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 21C7 16.5 3 13.2 3 9.5A4.5 4.5 0 0 1 12 6a4.5 4.5 0 0 1 9 3.5c0 3.7-4 7-9 11.5z\"/></svg><span>Favs</span></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"12\" cy=\"8\" r=\"4\"/><path d=\"M4 21c1.5-4 5-6 8-6s6.5 2 8 6\"/></svg><span>Perfil</span></button></nav>",
     "<nav class=\"cat-tabbar\" data-cat-tabs role=\"tablist\" style=\"width:300px\"><button type=\"button\" class=\"tb-item is-active\" data-cat-tab role=\"tab\" aria-selected=\"true\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M3 11l9-8 9 8\"/><path d=\"M5 10v10a1 1 0 0 0 1 1h4v-6h4v6h4a1 1 0 0 0 1-1V10\"/></svg></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"11\" cy=\"11\" r=\"7\"/><path d=\"M20 20l-3.5-3.5\"/></svg></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 5v14M5 12h14\"/></svg></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 21C7 16.5 3 13.2 3 9.5A4.5 4.5 0 0 1 12 6a4.5 4.5 0 0 1 9 3.5c0 3.7-4 7-9 11.5z\"/></svg></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"12\" cy=\"8\" r=\"4\"/><path d=\"M4 21c1.5-4 5-6 8-6s6.5 2 8 6\"/></svg></button></nav>"
    ],
    "note": "En pantallas chicas se fija abajo automaticamente."
   },
   "has_js": false,
   "demos": [
    "<nav class=\"cat-tabbar\" data-cat-tabs role=\"tablist\"><button type=\"button\" class=\"tb-item is-active\" data-cat-tab role=\"tab\" aria-selected=\"true\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M3 11l9-8 9 8\"/><path d=\"M5 10v10a1 1 0 0 0 1 1h4v-6h4v6h4a1 1 0 0 0 1-1V10\"/></svg><span>Inicio</span></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"11\" cy=\"11\" r=\"7\"/><path d=\"M20 20l-3.5-3.5\"/></svg><span>Buscar</span></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 5v14M5 12h14\"/></svg><span>Crear</span></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 21C7 16.5 3 13.2 3 9.5A4.5 4.5 0 0 1 12 6a4.5 4.5 0 0 1 9 3.5c0 3.7-4 7-9 11.5z\"/></svg><span>Favs</span></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"12\" cy=\"8\" r=\"4\"/><path d=\"M4 21c1.5-4 5-6 8-6s6.5 2 8 6\"/></svg><span>Perfil</span></button></nav>",
    "<nav class=\"cat-tabbar\" data-cat-tabs role=\"tablist\" style=\"width:300px\"><button type=\"button\" class=\"tb-item is-active\" data-cat-tab role=\"tab\" aria-selected=\"true\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M3 11l9-8 9 8\"/><path d=\"M5 10v10a1 1 0 0 0 1 1h4v-6h4v6h4a1 1 0 0 0 1-1V10\"/></svg></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"11\" cy=\"11\" r=\"7\"/><path d=\"M20 20l-3.5-3.5\"/></svg></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 5v14M5 12h14\"/></svg></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 21C7 16.5 3 13.2 3 9.5A4.5 4.5 0 0 1 12 6a4.5 4.5 0 0 1 9 3.5c0 3.7-4 7-9 11.5z\"/></svg></button><button type=\"button\" class=\"tb-item\" data-cat-tab role=\"tab\" aria-selected=\"false\"><svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"12\" cy=\"8\" r=\"4\"/><path d=\"M4 21c1.5-4 5-6 8-6s6.5 2 8 6\"/></svg></button></nav>"
   ]
  },
  {
   "name": "pagination",
   "description": "Paginador compacto con estados activo/disabled.",
   "docs": {
    "demos": [
     "<nav class=\"cat-pagination\"><button class=\"page prev\" disabled>&lt;</button><button class=\"page is-active\">1</button><button class=\"page\">2</button><button class=\"page\">3</button><span class=\"ellip\">&hellip;</span><button class=\"page\">12</button><button class=\"page next\">&gt;</button></nav>"
    ]
   },
   "has_js": false,
   "demos": [
    "<nav class=\"cat-pagination\"><button class=\"page prev\" disabled>&lt;</button><button class=\"page is-active\">1</button><button class=\"page\">2</button><button class=\"page\">3</button><span class=\"ellip\">&hellip;</span><button class=\"page\">12</button><button class=\"page next\">&gt;</button></nav>"
   ]
  },
  {
   "name": "progress-spinner-skeleton",
   "description": "Indicadores de progreso determinado, indeterminado y carga.",
   "docs": {
    "demos": [
     "<div class=\"cat-progress\"><div class=\"fill\" style=\"width:64%\"></div></div>",
     "<div class=\"cat-progress indeterminate\"><div class=\"fill\"></div></div>",
     "<span class=\"cat-spinner\"></span>",
     "<div style=\"width:200px\"><div class=\"cat-skeleton av\"></div><div class=\"cat-skeleton text\" style=\"width:80%\"></div><div class=\"cat-skeleton text\" style=\"width:55%\"></div></div>"
    ]
   },
   "guidance": {
    "use": [
     "Progress bar: duracion conocida. Spinner: desconocida y corta. Skeleton: layout predecible."
    ],
    "avoid": [
     "Spinner para esperas mayores a 3s con progreso medible."
    ],
    "rules": [
     "Indeterminado comunica vida, no progreso real."
    ]
   },
   "has_js": false,
   "demos": [
    "<div class=\"cat-progress\"><div class=\"fill\" style=\"width:64%\"></div></div>",
    "<div class=\"cat-progress indeterminate\"><div class=\"fill\"></div></div>",
    "<span class=\"cat-spinner\"></span>",
    "<div style=\"width:200px\"><div class=\"cat-skeleton av\"></div><div class=\"cat-skeleton text\" style=\"width:80%\"></div><div class=\"cat-skeleton text\" style=\"width:55%\"></div></div>"
   ]
  },
  {
   "name": "radius-scale",
   "description": "Escala de radios sobre gris neutro, para elegir el correcto por superficie.",
   "docs": {
    "demos": [
     "<div class=\"cat-radii\"><div class=\"rr\"><i style=\"border-radius:4px;\"></i>4px</div><div class=\"rr\"><i style=\"border-radius:6px;\"></i>6px</div><div class=\"rr\"><i style=\"border-radius:8px;\"></i>8px</div><div class=\"rr\"><i style=\"border-radius:12px;\"></i>12px</div><div class=\"rr\"><i style=\"border-radius:16px;\"></i>16px</div><div class=\"rr\"><i style=\"border-radius:999px;width:64px;height:36px\"></i>pill</div></div>"
    ],
    "note": "Regla HIG: controles sm, contenedores md-lg, ventanas xl-window."
   },
   "has_js": false,
   "demos": [
    "<div class=\"cat-radii\"><div class=\"rr\"><i style=\"border-radius:4px;\"></i>4px</div><div class=\"rr\"><i style=\"border-radius:6px;\"></i>6px</div><div class=\"rr\"><i style=\"border-radius:8px;\"></i>8px</div><div class=\"rr\"><i style=\"border-radius:12px;\"></i>12px</div><div class=\"rr\"><i style=\"border-radius:16px;\"></i>16px</div><div class=\"rr\"><i style=\"border-radius:999px;width:64px;height:36px\"></i>pill</div></div>"
   ]
  },
  {
   "name": "rating",
   "description": "Estrellas interactivas CSS-only via radios.",
   "docs": {
    "demos": [
     "<div class=\"cat-rating\" data-cat-rating data-value=\"4\" role=\"radiogroup\"><button type=\"button\" class=\"star\" aria-label=\"1 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"2 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"3 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"4 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"5 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button></div>",
     "<div class=\"cat-rating\" data-cat-rating data-value=\"2\" role=\"radiogroup\"><button type=\"button\" class=\"star\" aria-label=\"1 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"2 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"3 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"4 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"5 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button></div>"
    ],
    "note": "Hover preview y click para fijar. Valor inicial via data-value."
   },
   "has_js": false,
   "demos": [
    "<div class=\"cat-rating\" data-cat-rating data-value=\"4\" role=\"radiogroup\"><button type=\"button\" class=\"star\" aria-label=\"1 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"2 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"3 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"4 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"5 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button></div>",
    "<div class=\"cat-rating\" data-cat-rating data-value=\"2\" role=\"radiogroup\"><button type=\"button\" class=\"star\" aria-label=\"1 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"2 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"3 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"4 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button><button type=\"button\" class=\"star\" aria-label=\"5 estrellas\"><svg viewBox=\"0 0 24 24\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.3L12 17l-5.7 3 1.2-6.3L2.8 9.3l6.4-.8z\"/></svg></button></div>"
   ]
  },
  {
   "name": "segmented",
   "description": "Control segmentado estilo macOS. CSS-only via radios (accesible).",
   "docs": {
    "demos": [
     "<div class=\"cat-segmented\" data-cat-segmented role=\"radiogroup\"><button type=\"button\" class=\"seg-btn is-active\" aria-pressed=\"true\">Icons</button><button type=\"button\" class=\"seg-btn\" aria-pressed=\"false\">List</button><button type=\"button\" class=\"seg-btn\" aria-pressed=\"false\">Gallery</button></div>"
    ]
   },
   "guidance": {
    "use": [
     "Cambiar modo de vista de un mismo contenido."
    ],
    "avoid": [
     "Destinos de navegacion distintos: tabs."
    ],
    "rules": [
     "2-5 segmentos; textos cortos, nunca iconos solos si son ambiguos."
    ]
   },
   "has_js": false,
   "demos": [
    "<div class=\"cat-segmented\" data-cat-segmented role=\"radiogroup\"><button type=\"button\" class=\"seg-btn is-active\" aria-pressed=\"true\">Icons</button><button type=\"button\" class=\"seg-btn\" aria-pressed=\"false\">List</button><button type=\"button\" class=\"seg-btn\" aria-pressed=\"false\">Gallery</button></div>"
   ]
  },
  {
   "name": "sidebar-nav",
   "description": "Navegación lateral con item activo lleno (Finder-style) y árbol expandible.",
   "docs": {
    "demos": [
     "<aside class=\"cat-sidebar\" style=\"border-radius:12px;border:1px solid rgba(255,255,255,.5)\"><div class=\"cat-nav-item\"><span class=\"ni-icon\">+</span>Home</div><div class=\"cat-nav-item active\"><span class=\"ni-icon\">#</span>Documents<span class=\"cat-chevron\">▾</span></div><div class=\"cat-sub\"><div class=\"cat-nav-item\">Projects</div><div class=\"cat-nav-item\">Backups</div></div><div class=\"cat-section\">Locations</div><div class=\"cat-nav-item\"><span class=\"ni-icon\">~</span>Network</div></aside>"
    ]
   },
   "guidance": {
    "use": [
     "Navegacion primaria persistente entre vistas."
    ],
    "avoid": [
     "Mas de ~8 items de primer nivel: agrupa en secciones."
    ],
    "rules": [
     "Item activo lleno con accent; icono hereda blanco."
    ]
   },
   "has_js": false,
   "demos": [
    "<aside class=\"cat-sidebar\" style=\"border-radius:12px;border:1px solid rgba(255,255,255,.5)\"><div class=\"cat-nav-item\"><span class=\"ni-icon\">+</span>Home</div><div class=\"cat-nav-item active\"><span class=\"ni-icon\">#</span>Documents<span class=\"cat-chevron\">▾</span></div><div class=\"cat-sub\"><div class=\"cat-nav-item\">Projects</div><div class=\"cat-nav-item\">Backups</div></div><div class=\"cat-section\">Locations</div><div class=\"cat-nav-item\"><span class=\"ni-icon\">~</span>Network</div></aside>"
   ]
  },
  {
   "name": "slider",
   "description": "Range nativo con thumb grande (zona táctil > visual, spec §40).",
   "docs": {
    "demos": [
     "<input class=\"cat-slider\" type=\"range\" value=\"40\">",
     "<input class=\"cat-slider accent\" type=\"range\" value=\"70\">"
    ]
   },
   "guidance": {
    "use": [
     "Valores continuos donde la precision exacta no es critica (volumen, brillo)."
    ],
    "avoid": [
     "Rangos discretos largos: mejor select."
    ],
    "rules": [
     "Thumb grande: la zona interactiva supera al elemento visual."
    ]
   },
   "has_js": false,
   "demos": [
    "<input class=\"cat-slider\" type=\"range\" value=\"40\">",
    "<input class=\"cat-slider accent\" type=\"range\" value=\"70\">"
   ]
  },
  {
   "name": "sparkline",
   "description": "Grafico SVG minimo: linea o barras desde data-values. Cero dependencias.",
   "props": {
    "data-cat-spark": "valores CSV",
    "data-spark-type": "line | bars",
    "data-width / data-height": "px"
   },
   "docs": {
    "demos": [
     "<span class=\"cat-sparkline\" data-cat-spark=\"4,9,6,12,8,14\" data-width=\"120\" data-height=\"32\"></span> <span class=\"cat-sparkline\" data-cat-spark=\"3,7,5,10,13\" data-spark-type=\"bars\" data-width=\"120\" data-height=\"32\"></span> <span class=\"cat-sparkline\" data-cat-spark=\"10,8,11,7,9,6,8\" data-width=\"120\" data-height=\"32\"></span>"
    ]
   },
   "has_js": false,
   "demos": [
    "<span class=\"cat-sparkline\" data-cat-spark=\"4,9,6,12,8,14\" data-width=\"120\" data-height=\"32\"></span> <span class=\"cat-sparkline\" data-cat-spark=\"3,7,5,10,13\" data-spark-type=\"bars\" data-width=\"120\" data-height=\"32\"></span> <span class=\"cat-sparkline\" data-cat-spark=\"10,8,11,7,9,6,8\" data-width=\"120\" data-height=\"32\"></span>"
   ]
  },
  {
   "name": "stat-card",
   "description": "KPI card: label, valor grande, delta con direccion.",
   "docs": {
    "demos": [
     "<div style=\"display:flex;gap:10px\"><div class=\"cat-stat\"><span class=\"label\">Ingresos</span><span class=\"value\">$12.4K</span><span class=\"delta up\">+8.2%</span></div><div class=\"cat-stat\"><span class=\"label\">Churn</span><span class=\"value\">2.1%</span><span class=\"delta down\">+0.4%</span></div><div class=\"cat-stat\"><span class=\"label\">Activos</span><span class=\"value\">324</span><span class=\"delta up\">+12</span></div></div>"
    ]
   },
   "has_js": false,
   "demos": [
    "<div style=\"display:flex;gap:10px\"><div class=\"cat-stat\"><span class=\"label\">Ingresos</span><span class=\"value\">$12.4K</span><span class=\"delta up\">+8.2%</span></div><div class=\"cat-stat\"><span class=\"label\">Churn</span><span class=\"value\">2.1%</span><span class=\"delta down\">+0.4%</span></div><div class=\"cat-stat\"><span class=\"label\">Activos</span><span class=\"value\">324</span><span class=\"delta up\">+12</span></div></div>"
   ]
  },
  {
   "name": "stepper",
   "description": "Pasos numerados conectados: done / active / pendiente.",
   "docs": {
    "demos": [
     "<ol class=\"cat-stepper\"><li class=\"done\"><span>1</span>Cuenta</li><li class=\"active\"><span>2</span>Datos</li><li><span>3</span>Confirmar</li></ol>"
    ]
   },
   "has_js": false,
   "demos": [
    "<ol class=\"cat-stepper\"><li class=\"done\"><span>1</span>Cuenta</li><li class=\"active\"><span>2</span>Datos</li><li><span>3</span>Confirmar</li></ol>"
   ]
  },
  {
   "name": "switch",
   "description": "Toggle binario estilo macOS. CSS puro sobre checkbox nativo (accesible).",
   "states": [
    "checked",
    "unchecked",
    "focus-visible",
    "disabled"
   ],
   "docs": {
    "demos": [
     "<label class=\"cat-switch\"><input type=\"checkbox\" checked><span class=\"track\"></span></label>",
     "<label class=\"cat-switch\"><input type=\"checkbox\"><span class=\"track\"></span></label>",
     "<label class=\"cat-switch\"><input type=\"checkbox\" disabled><span class=\"track\"></span></label>"
    ]
   },
   "guidance": {
    "use": [
     "Preferencias que aplican INMEDIATAMENTE al togglear."
    ],
    "avoid": [
     "Opciones que requieren confirmar con un boton: usa checkbox."
    ],
    "rules": [
     "Label siempre a la izquierda del control en listas de ajustes."
    ]
   },
   "has_js": false,
   "demos": [
    "<label class=\"cat-switch\"><input type=\"checkbox\" checked><span class=\"track\"></span></label>",
    "<label class=\"cat-switch\"><input type=\"checkbox\"><span class=\"track\"></span></label>",
    "<label class=\"cat-switch\"><input type=\"checkbox\" disabled><span class=\"track\"></span></label>"
   ]
  },
  {
   "name": "table",
   "description": "Tabla de datos: header secundario uppercase, hover suave, fila seleccionada en accent.",
   "docs": {
    "demos": [
     "<table class=\"cat-table\" style=\"max-width:480px\"><thead><tr><th>Nombre</th><th>Estado</th><th>Peso</th></tr></thead><tbody><tr class=\"is-selected\"><td>backup.zip</td><td>Listo</td><td>1.2 GB</td></tr><tr><td>fotos.tar</td><td>En curso</td><td>860 MB</td></tr><tr><td>db.sqlite</td><td>En cola</td><td>44 MB</td></tr></tbody></table>"
    ]
   },
   "guidance": {
    "use": [
     "Comparacion escaneable de muchos registros homogeneos."
    ],
    "avoid": [
     "Menos de 3 filas: lista simple."
    ],
    "rules": [
     "Header secundario uppercase; seleccion llena con accent."
    ]
   },
   "has_js": false,
   "demos": [
    "<table class=\"cat-table\" style=\"max-width:480px\"><thead><tr><th>Nombre</th><th>Estado</th><th>Peso</th></tr></thead><tbody><tr class=\"is-selected\"><td>backup.zip</td><td>Listo</td><td>1.2 GB</td></tr><tr><td>fotos.tar</td><td>En curso</td><td>860 MB</td></tr><tr><td>db.sqlite</td><td>En cola</td><td>44 MB</td></tr></tbody></table>"
   ]
  },
  {
   "name": "tabs",
   "description": "Pestañas chip aqua + paneles sincronizados por data-attrs.",
   "states": [
    "active(aqua chip)",
    "inactive",
    "hover"
   ],
   "docs": {
    "demos": [
     "<div class=\"cat-tabs\" data-cat-tabs=\"t1\"><button class=\"cat-tab is-active\" data-cat-tab=\"one\">Documents</button><button class=\"cat-tab\" data-cat-tab=\"two\">Music</button></div><div style=\"margin-top:12px;font-size:13px\" data-cat-panel-for=\"t1\" data-cat-panel=\"one\">Panel Documents</div><div style=\"margin-top:12px;font-size:13px\" data-cat-panel-for=\"t1\" data-cat-panel=\"two\" hidden>Panel Music</div>"
    ]
   },
   "guidance": {
    "use": [
     "Cambiar de contexto o documento sin perder el lugar."
    ],
    "avoid": [
     "Pasos secuenciales de un flujo: eso es stepper."
    ],
    "rules": [
     "Tab activo claramente elevado; nunca dos activos."
    ]
   },
   "has_js": false,
   "demos": [
    "<div class=\"cat-tabs\" data-cat-tabs=\"t1\"><button class=\"cat-tab is-active\" data-cat-tab=\"one\">Documents</button><button class=\"cat-tab\" data-cat-tab=\"two\">Music</button></div><div style=\"margin-top:12px;font-size:13px\" data-cat-panel-for=\"t1\" data-cat-panel=\"one\">Panel Documents</div><div style=\"margin-top:12px;font-size:13px\" data-cat-panel-for=\"t1\" data-cat-panel=\"two\" hidden>Panel Music</div>"
   ]
  },
  {
   "name": "timeline",
   "description": "Feed de actividad vertical con puntos y linea conectora.",
   "docs": {
    "demos": [
     "<ul class=\"cat-timeline\" style=\"width:300px\"><li><span class=\"dot\"></span><div><b>Sincronizacion iniciada</b> — 12 archivos<span class=\"t\">hace 2 min</span></div></li><li><span class=\"dot done\"></span><div><b>Backup completado</b> — 4.33 GB<span class=\"t\">hace 1 h</span></div></li><li><span class=\"dot done\"></span><div><b>Nuevo device vinculado</b><span class=\"t\">ayer</span></div></li></ul>"
    ]
   },
   "has_js": false,
   "demos": [
    "<ul class=\"cat-timeline\" style=\"width:300px\"><li><span class=\"dot\"></span><div><b>Sincronizacion iniciada</b> — 12 archivos<span class=\"t\">hace 2 min</span></div></li><li><span class=\"dot done\"></span><div><b>Backup completado</b> — 4.33 GB<span class=\"t\">hace 1 h</span></div></li><li><span class=\"dot done\"></span><div><b>Nuevo device vinculado</b><span class=\"t\">ayer</span></div></li></ul>"
   ]
  },
  {
   "name": "toast-queue",
   "description": "API JS para cola de notificaciones: Catalinas.toast({tone,title,message,timeout}).",
   "docs": {
    "demos": [
     "<button class=\"cat-btn secondary sm\" id=\"tgInfo\">Info</button> <button class=\"cat-btn success sm\" id=\"tgOk\">Exito</button> <button class=\"cat-btn danger sm\" id=\"tgErr\">Error</button>"
    ],
    "note": "Uso en app: Catalinas.toast({tone:'success', title:'Listo', message:'Backup completo', timeout:4000}). timeout:0 = sin auto-dismiss."
   },
   "has_js": false,
   "demos": [
    "<button class=\"cat-btn secondary sm\" id=\"tgInfo\">Info</button> <button class=\"cat-btn success sm\" id=\"tgOk\">Exito</button> <button class=\"cat-btn danger sm\" id=\"tgErr\">Error</button>"
   ]
  },
  {
   "name": "tree-view",
   "description": "Arbol jerarquico en contenido (no sidebar). Expand/collapse nativo via details-like con JS minimo opcional.",
   "docs": {
    "demos": [
     "<ul class=\"cat-tree\" id=\"tvDemo\" style=\"width:280px\" data-cat-tree><li class=\"branch open\"><div class=\"t-row\"><span class=\"tw\">-</span>KittyDrive</div><ul><li><div class=\"t-row leaf\">Projects</div></li><li><div class=\"t-row leaf\">Backups</div></li></ul></li><li class=\"branch\"><div class=\"t-row\"><span class=\"tw\">+</span>Cats</div><ul><li><div class=\"t-row leaf\">michi.jpg</div></li></ul></li></ul>"
    ],
    "note": "Toggle con JS del host: click en .branch > .t-row alterna clase open y el signo."
   },
   "has_js": false,
   "demos": [
    "<ul class=\"cat-tree\" id=\"tvDemo\" style=\"width:280px\" data-cat-tree><li class=\"branch open\"><div class=\"t-row\"><span class=\"tw\">-</span>KittyDrive</div><ul><li><div class=\"t-row leaf\">Projects</div></li><li><div class=\"t-row leaf\">Backups</div></li></ul></li><li class=\"branch\"><div class=\"t-row\"><span class=\"tw\">+</span>Cats</div><ul><li><div class=\"t-row leaf\">michi.jpg</div></li></ul></li></ul>"
   ]
  },
  {
   "name": "typography",
   "description": "Escala textual, estados y resaltado tipo seleccion (.cat-mark).",
   "docs": {
    "demos": [
     "<div class=\"cat-typography-list\"><div class=\"trow\"><span class=\"tag\">H1</span><h1 class=\"cat-h1\">Titulo de vista</h1></div><div class=\"trow\"><span class=\"tag\">H2</span><h2 class=\"cat-h2\">Seccion destacada</h2></div><div class=\"trow\"><span class=\"tag\">Body</span><p class=\"cat-body\">Texto con <span class=\"cat-mark\">resaltado accent</span> dentro.</p></div><div class=\"trow\"><span class=\"tag\">Mark</span><p class=\"cat-body\">Variantes: <span class=\"cat-mark success\">ok</span> <span class=\"cat-mark danger\">error</span> <code class=\"cat-code\">codigo</code></p></div><div class=\"trow\"><span class=\"tag\">Estados</span><p class=\"cat-body\">muted <span class=\"cat-text-muted\">medio</span>, <span class=\"cat-text-low\">bajo</span>, <span class=\"cat-text-accent\">accent</span>, <span class=\"cat-text-success\">exito</span>, <span class=\"cat-text-danger\">error</span></p></div><div class=\"trow\"><span class=\"tag\">Caption</span><span class=\"caption\">Metadata secundaria - Aug 25, 2026</span></div></div>"
    ],
    "note": ".cat-mark usa box-decoration-break:clone: sobrevive saltos de linea."
   },
   "has_js": false,
   "demos": [
    "<div class=\"cat-typography-list\"><div class=\"trow\"><span class=\"tag\">H1</span><h1 class=\"cat-h1\">Titulo de vista</h1></div><div class=\"trow\"><span class=\"tag\">H2</span><h2 class=\"cat-h2\">Seccion destacada</h2></div><div class=\"trow\"><span class=\"tag\">Body</span><p class=\"cat-body\">Texto con <span class=\"cat-mark\">resaltado accent</span> dentro.</p></div><div class=\"trow\"><span class=\"tag\">Mark</span><p class=\"cat-body\">Variantes: <span class=\"cat-mark success\">ok</span> <span class=\"cat-mark danger\">error</span> <code class=\"cat-code\">codigo</code></p></div><div class=\"trow\"><span class=\"tag\">Estados</span><p class=\"cat-body\">muted <span class=\"cat-text-muted\">medio</span>, <span class=\"cat-text-low\">bajo</span>, <span class=\"cat-text-accent\">accent</span>, <span class=\"cat-text-success\">exito</span>, <span class=\"cat-text-danger\">error</span></p></div><div class=\"trow\"><span class=\"tag\">Caption</span><span class=\"caption\">Metadata secundaria - Aug 25, 2026</span></div></div>"
   ]
  },
  {
   "name": "window-chrome",
   "description": "Ventana acrilica: tabs integrados + controles minimizar, maximizar y cerrar con hover rojo.",
   "docs": {
    "demos": [
     "<div style=\"border-radius:12px;background:rgba(247,249,253,.68);backdrop-filter:blur(46px) saturate(1.7);border:1px solid rgba(255,255,255,.55);box-shadow:0 24px 80px rgba(0,0,0,.34), inset 0 1px 0 rgba(255,255,255,.65)\" class=\"cat-window-demo\"><div class=\"cat-win-tabs\"><button class=\"cat-wtab is-active\">Documents</button><button class=\"cat-wtab\">Music</button><button class=\"cat-wtab add\">+</button></div><div class=\"cat-win-controls\"><button class=\"cat-win-btn\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><path d=\"M5 12h14\"/></svg></button><button class=\"cat-win-btn\"><svg width=\"9\" height=\"9\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\"><rect x=\"5\" y=\"5\" width=\"14\" height=\"14\" rx=\"1.5\"/></svg></button><button class=\"cat-win-btn close\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><path d=\"M6 6l12 12M18 6L6 18\"/></svg></button></div></div>"
    ]
   },
   "guidance": {
    "use": [
     "Ventanas de nivel app sobre el escritorio."
    ],
    "avoid": [
     "Controles dentro de cards embebidas."
    ],
    "rules": [
     "Cerrar con hover rojo: convencion de destruccion."
    ]
   },
   "has_js": false,
   "demos": [
    "<div style=\"border-radius:12px;background:rgba(247,249,253,.68);backdrop-filter:blur(46px) saturate(1.7);border:1px solid rgba(255,255,255,.55);box-shadow:0 24px 80px rgba(0,0,0,.34), inset 0 1px 0 rgba(255,255,255,.65)\" class=\"cat-window-demo\"><div class=\"cat-win-tabs\"><button class=\"cat-wtab is-active\">Documents</button><button class=\"cat-wtab\">Music</button><button class=\"cat-wtab add\">+</button></div><div class=\"cat-win-controls\"><button class=\"cat-win-btn\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><path d=\"M5 12h14\"/></svg></button><button class=\"cat-win-btn\"><svg width=\"9\" height=\"9\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\"><rect x=\"5\" y=\"5\" width=\"14\" height=\"14\" rx=\"1.5\"/></svg></button><button class=\"cat-win-btn close\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><path d=\"M6 6l12 12M18 6L6 18\"/></svg></button></div></div>"
   ]
  },
  {
   "name": "windows",
   "description": "Ventanas de nivel app en dos materiales: Desktop (vidrio acrilico) y Normal (solida). Ambas con barra de control.",
   "anatomy": [
    "frame",
    "bar(title + controls)",
    "body"
   ],
   "states": [
    "desktop-glass",
    "standard-solid"
   ],
   "rules": [
    "Glass para apps de escritorio que viven sobre el wallpaper.",
    "Solid para documentos y ventanas hijas: maxima legibilidad.",
    "El contenido interno siempre es mas opaco que el marco (legibilidad > transparencia)."
   ],
   "docs": {
    "demos": [
     "<div style=\"display:flex;gap:18px;flex-wrap:wrap;justify-content:center;width:100%\"><section class=\"cat-window glass\" style=\"width:290px\"><header class=\"w-bar\"><b>KittyDrive</b><div class=\"w-ctl\"><button class=\"w-btn\" aria-label=\"Minimize\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><path d=\"M5 12h14\"/></svg></button><button class=\"w-btn\" aria-label=\"Maximize\"><svg width=\"9\" height=\"9\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\"><rect x=\"5\" y=\"5\" width=\"14\" height=\"14\" rx=\"1.5\"/></svg></button><button class=\"w-btn close\" aria-label=\"Close\"><svg width=\"10\" height=\"10\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><path d=\"M6 6l12 12M18 6L6 18\"/></svg></button></div></header><div class=\"w-body\" style=\"min-height:96px\">Vidrio acrilico: el fondo se percibe a traves del marco.</div></section><section class=\"cat-window solid\" style=\"width:290px\"><header class=\"w-bar\"><b>Documento.txt</b><div class=\"w-ctl\"><button class=\"w-btn\" aria-label=\"Minimize\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><path d=\"M5 12h14\"/></svg></button><button class=\"w-btn\" aria-label=\"Maximize\"><svg width=\"9\" height=\"9\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\"><rect x=\"5\" y=\"5\" width=\"14\" height=\"14\" rx=\"1.5\"/></svg></button><button class=\"w-btn close\" aria-label=\"Close\"><svg width=\"10\" height=\"10\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><path d=\"M6 6l12 12M18 6L6 18\"/></svg></button></div></header><div class=\"w-body\" style=\"min-height:96px\">Ventana solida: legibilidad maxima para contenido.</div></section></div>"
    ],
    "note": "Ejemplo completo armado: examples/kittydrive.html"
   },
   "has_js": false,
   "demos": [
    "<div style=\"display:flex;gap:18px;flex-wrap:wrap;justify-content:center;width:100%\"><section class=\"cat-window glass\" style=\"width:290px\"><header class=\"w-bar\"><b>KittyDrive</b><div class=\"w-ctl\"><button class=\"w-btn\" aria-label=\"Minimize\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><path d=\"M5 12h14\"/></svg></button><button class=\"w-btn\" aria-label=\"Maximize\"><svg width=\"9\" height=\"9\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\"><rect x=\"5\" y=\"5\" width=\"14\" height=\"14\" rx=\"1.5\"/></svg></button><button class=\"w-btn close\" aria-label=\"Close\"><svg width=\"10\" height=\"10\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><path d=\"M6 6l12 12M18 6L6 18\"/></svg></button></div></header><div class=\"w-body\" style=\"min-height:96px\">Vidrio acrilico: el fondo se percibe a traves del marco.</div></section><section class=\"cat-window solid\" style=\"width:290px\"><header class=\"w-bar\"><b>Documento.txt</b><div class=\"w-ctl\"><button class=\"w-btn\" aria-label=\"Minimize\"><svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><path d=\"M5 12h14\"/></svg></button><button class=\"w-btn\" aria-label=\"Maximize\"><svg width=\"9\" height=\"9\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\"><rect x=\"5\" y=\"5\" width=\"14\" height=\"14\" rx=\"1.5\"/></svg></button><button class=\"w-btn close\" aria-label=\"Close\"><svg width=\"10\" height=\"10\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.4\" stroke-linecap=\"round\"><path d=\"M6 6l12 12M18 6L6 18\"/></svg></button></div></header><div class=\"w-body\" style=\"min-height:96px\">Ventana solida: legibilidad maxima para contenido.</div></section></div>"
   ]
  }
 ],
 "targets": [
  "Web CSS",
  "React",
  "Qt",
  "Flutter",
  "Tailwind",
  "Flat JSON"
 ]
}
