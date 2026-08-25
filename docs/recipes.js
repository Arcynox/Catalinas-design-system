/* generated — casos de uso compuestos solo con clases cat- */
window.CATALINAS_RECIPES = [
{
  name: "Login",
  description: "Card de acceso: campos con icono, primaria y enlace de recovery.",
  tags: ["input", "button", "card"],
  markup:
'<div class="cat-card" style="width:340px;display:flex;flex-direction:column;gap:12px">' +
'<div style="text-align:center;margin-bottom:4px">' +
'<div style="font-size:17px;font-weight:650">Ingresar a KittyDrive</div>' +
'<div style="font-size:12px;color:var(--cat-color-ink-mid);margin-top:2px">Sincronizacion segura entre dispositivos</div></div>' +
'<div class="cat-field"><label class="cat-label">Email</label><div class="cat-input has-icon">' +
'<span class="cat-icon"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></span>' +
'<input class="el" placeholder="tu@email.com"></div></div>' +
'<div class="cat-field"><label class="cat-label">Password</label><div class="cat-input"><input class="el" type="password" value="............"></div></div>' +
'<button class="cat-btn primary" style="width:100%;justify-content:center">Ingresar</button>' +
'<button class="cat-btn link" style="align-self:center;font-size:12px">Olvide mi password</button></div>'
},
{
  name: "Settings panel",
  description: "Panel de ajustes con filas de switch, patron System Settings.",
  tags: ["switch", "card"],
  markup:
'<div class="cat-card" style="width:360px;padding:8px">' +
(function(){
  var rows = [
    ["#34c759", '<path d="M5 12.5a10 10 0 0 1 14 0"/><path d="M8.5 15.5a5 5 0 0 1 7 0"/><circle cx="12" cy="18.5" r="1.4" fill="currentColor" stroke="none"/>', "Wi-Fi", true],
    ["#5e9eff", '<path d="M7 7l10 10-5 4V3l5 4L7 17"/>', "Bluetooth", false],
    ["#ff9f0a", '<circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.9 4.9l1.4 1.4m11.4 11.4l1.4 1.4M2 12h2m16 0h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>', "Brightness", true]
  ];
  var out = "";
  rows.forEach(function(r, i){
    out += '<div style="display:flex;align-items:center;gap:10px;padding:9px 10px;' + (i>0 ? 'border-top:1px solid var(--cat-color-stroke-softer);' : '') + '">'
      + '<span style="display:grid;place-items:center;width:26px;height:26px;border-radius:6px;background:' + r[0] + ';color:#fff">'
      + '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">' + r[1] + '</svg></span>'
      + '<span style="flex:1;font-size:13px">' + r[2] + '</span>'
      + '<label class="cat-switch"><input type="checkbox"' + (r[3] ? " checked" : "") + '><span class="track"></span></label></div>';
  });
  return out;
})() +
'</div>'
},
{
  name: "Upload flow",
  description: "Dropzone + chips de archivo + progreso + banner informativo.",
  tags: ["dropzone", "file-chip", "progress", "alert"],
  markup:
'<div style="width:420px;display:flex;flex-direction:column;gap:12px">' +
'<label class="cat-dropzone"><input type="file" multiple hidden><b>Solta archivos aca</b><span>o hace clic para elegir</span></label>' +
'<span class="cat-filechip"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#5f8af5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></svg><span class="fc-name">informe-q4.pdf</span><span class="fc-size">2.4 MB</span><button class="fc-x" aria-label="Quitar">x</button></span>' +
'<div class="cat-progress indeterminate"><div class="fill"></div></div>' +
'<div class="cat-alert info"><span class="a-icon" style="background:var(--cat-semantic-accent-dynamic,var(--cat-color-accent-base))"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M12 11v5"/></svg></span><div class="a-body"><b>Subiendo 3 archivos</b><span>No cierres la ventana.</span></div><button class="t-close" data-cat-dismiss=".cat-alert">x</button></div></div>'
},
{
  name: "Data page",
  description: "App header + tabla con seleccion + paginado + status bar contextual.",
  tags: ["app-header", "table", "pagination"],
  markup:
'<div style="width:520px;display:flex;flex-direction:column;gap:12px">' +
'<header class="cat-appheader"><span class="brand">KittySync</span><nav><a class="is-active">Backups</a><a>Devices</a><a>Activity</a></nav><span class="spacer"></span><button class="cat-btn primary sm">New backup</button></header>' +
'<table class="cat-table"><thead><tr><th>Name</th><th>Status</th><th>Size</th></tr></thead><tbody>' +
'<tr class="is-selected"><td>backup.zip</td><td>Done</td><td>1.2 GB</td></tr>' +
'<tr><td>fotos.tar</td><td>Running</td><td>860 MB</td></tr>' +
'<tr><td>db.sqlite</td><td>Queued</td><td>44 MB</td></tr></tbody></table>' +
'<nav class="cat-pagination"><button class="page prev" disabled>&lt;</button><button class="page is-active">1</button><button class="page">2</button><span class="ellip">&hellip;</span><button class="page next">&gt;</button></nav></div>'
},
{
  name: "Onboarding stepper",
  description: "Flujo guiado: stepper + campos en grilla + acciones al pie.",
  tags: ["stepper", "input", "button"],
  markup:
'<div class="cat-card" style="width:430px;padding:20px">' +
'<ol class="cat-stepper" style="margin-bottom:18px"><li class="done"><span>1</span>Cuenta</li><li class="active"><span>2</span>Perfil</li><li><span>3</span>Listo</li></ol>' +
'<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px">' +
'<div class="cat-field"><label class="cat-label">Nombre</label><div class="cat-input"><input class="el" placeholder="Luigi"></div></div>' +
'<div class="cat-field"><label class="cat-label">Apellido</label><div class="cat-input"><input class="el" placeholder="Gonzalez"></div></div></div>' +
'<div style="display:flex;justify-content:flex-end;gap:8px">' +
'<button class="cat-btn secondary">Atras</button><button class="cat-btn primary">Continuar</button></div></div>'
},
{
  name: "Share menu",
  description: "Menu contextual HIG disparado desde un boton secundario.",
  tags: ["menu", "button", "kbd"],
  markup:
'<div style="min-height:150px;display:flex;align-items:flex-start"><div data-cat-menu><button class="cat-btn secondary" data-cat-menu-trigger aria-expanded="false">Compartir ▾</button>' +
'<div class="cat-menu" role="menu">' +
'<button class="cat-menu-item" role="menuitem">Copiar enlace<span class="menu-kbd">Ctrl+L</span></button>' +
'<button class="cat-menu-item" role="menuitem">Enviar por mail<span class="menu-kbd">Ctrl+E</span></button>' +
'<div class="cat-menu-sep"></div>' +
'<button class="cat-menu-item checked" role="menuitem">Acceso: solo yo<span class="mi-check"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 13l4 4 10-10"/></svg></span></button>' +
'</div></div>'
}
];

window.CATALINAS_RECIPES.push(
{
  name: "Activity dashboard",
  description: "KPIs en fila + timeline de actividad: el patron resumen de cualquier app.",
  tags: ["stat-card", "timeline", "card"],
  markup:
'<div style="width:520px;display:flex;flex-direction:column;gap:14px">' +
'<div style="display:flex;gap:10px">' +
'<div class="cat-stat"><span class="label">Archivos</span><span class="value">67</span><span class="delta up">+4</span></div>' +
'<div class="cat-stat"><span class="label">En nube</span><span class="value">98%</span><span class="delta up">+1%</span></div>' +
'<div class="cat-stat"><span class="label">Espacio</span><span class="value">12 GB</span><span class="delta down">-3 GB</span></div></div>' +
'<div class="cat-card" style="padding:14px 16px"><ul class="cat-timeline" style="padding:4px 6px">' +
'<li><span class="dot"></span><div><b>Sincronizacion iniciada</b> — 12 archivos<span class="t">hace 2 min</span></div></li>' +
'<li><span class="dot done"></span><div><b>Backup completado</b> — 4.33 GB<span class="t">hace 1 h</span></div></li></ul></div></div>'
},
{
  name: "File inspector",
  description: "Panel de detalles: preview, metadata clave/valor y acciones.",
  tags: ["key-value-list", "avatar-group", "button"],
  markup:
'<div class="cat-card" style="width:300px;padding:16px;display:flex;flex-direction:column;gap:12px">' +
'<div style="display:flex;align-items:center;gap:10px">' +
'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#5f8af5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6M9 16h6"/></svg>' +
'<div><div style="font-size:13px;font-weight:600">design-spec.docx</div><div style="font-size:11px;color:var(--cat-color-ink-low)">1.4 MB</div></div></div>' +
'<dl class="cat-kv">' +
'<div><dt>Tipo</dt><dd>Word document</dd></div><div><dt>Modificado</dt><dd>Ayer</dd></div>' +
'<div><dt>Compartido con</dt><dd><span class="cat-avgroup" style="margin-left:auto"><span class="cat-avatar" style="width:22px;height:22px;font-size:9px;border:none;margin-left:-6px">LU</span><span class="cat-avatar" style="width:22px;height:22px;font-size:9px;border:none;margin-left:-6px;background:var(--cat-color-violet)">MI</span></span></dd></div></dl>' +
'<div style="display:flex;justify-content:flex-end;gap:8px"><button class="cat-btn secondary sm">Abrir</button><button class="cat-btn primary sm">Compartir</button></div></div>'
},
{
  name: "Notifications stack",
  description: "Cola de toasts apilados con dismiss independiente.",
  tags: ["toast"],
  markup:
'<div style="display:flex;flex-direction:column;gap:8px;width:320px">' +
'<div class="cat-toast success"><span class="t-icon"></span><div style="flex:1"><b style="font-size:12.5px">Backup completo</b><div style="font-size:11px;color:var(--cat-color-ink-mid)">4.33 GB sincronizados</div></div><button class="t-close" data-cat-dismiss=".cat-toast">x</button></div>' +
'<div class="cat-toast"><span class="t-icon"></span><div style="flex:1"><b style="font-size:12.5px">Nuevo dispositivo</b><div style="font-size:11px;color:var(--cat-color-ink-mid)">Laptop de Luigi</div></div><button class="t-close" data-cat-dismiss=".cat-toast">x</button></div>' +
'</div>'
},
);
