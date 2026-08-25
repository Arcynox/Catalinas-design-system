#!/usr/bin/env python3
"""Agrega guidance estilo Apple HIG a los widgets clave."""
import json, pathlib

G = {
"button": {
  "use": ["Accion principal de una vista: una sola primary por pantalla.",
          "Danger solo para acciones destructivas e irreversibles."],
  "avoid": ["Botones ghost para acciones criticas: poca affordance.",
            "Tres o mas botones en fila: convertilo en menu."],
  "rules": ["Orden HIG: primario a la derecha en dialogos, a la izquierda en toolbars.",
            "Loading deshabilita el boton; nunca doble submit."]
},
"input": {
  "use": ["Datos cortos con formato predecible (email, busqueda, nombre)."],
  "avoid": ["Placeholders como unica etiqueta: desaparecen al escribir."],
  "rules": ["Errores inline bajo el campo, nunca dialogs.",
            "Icono lider solo cuando ayuda al scanning (busqueda)."]
},
"switch": {
  "use": ["Preferencias que aplican INMEDIATAMENTE al togglear."],
  "avoid": ["Opciones que requieren confirmar con un boton: usa checkbox."],
  "rules": ["Label siempre a la izquierda del control en listas de ajustes."]
},
"checkbox-radio": {
  "use": ["Checkbox: seleccion multiple pendiente de confirmar.",
          "Radio: 2-5 opciones exclusivas visibles de una vez."],
  "avoid": ["Radio con mas de 5 opciones: usa select o segmented."],
  "rules": ["Un grupo de radios nunca empieza sin opcion marcada si la eleccion es requerida."]
},
"slider": {
  "use": ["Valores continuos donde la precision exacta no es critica (volumen, brillo)."],
  "avoid": ["Rangos discretos largos: mejor select."],
  "rules": ["Thumb grande: la zona interactiva supera al elemento visual."]
},
"menu": {
  "use": ["Acciones secundarias que no merecen espacio permanente."],
  "avoid": ["Acciones frecuentes: quedan en toolbar."],
  "rules": ["Abre hacia arriba automaticamente si falta espacio abajo.",
            "Items con shortcut muestran kbd a la derecha."]
},
"tabs": {
  "use": ["Cambiar de contexto o documento sin perder el lugar."],
  "avoid": ["Pasos secuenciales de un flujo: eso es stepper."],
  "rules": ["Tab activo claramente elevado; nunca dos activos."]
},
"alert-banner": {
  "use": ["Estado del sistema que el usuario debe notar sin bloquearlo."],
  "avoid": ["Feedback de una accion del usuario: eso es toast."],
  "rules": ["Severidad = icono lider + tinte sutil. Jamas franjas laterales."]
},
"sidebar-nav": {
  "use": ["Navegacion primaria persistente entre vistas."],
  "avoid": ["Mas de ~8 items de primer nivel: agrupa en secciones."],
  "rules": ["Item activo lleno con accent; icono hereda blanco."]
},
"window-chrome": {
  "use": ["Ventanas de nivel app sobre el escritorio."],
  "avoid": ["Controles dentro de cards embebidas."],
  "rules": ["Cerrar con hover rojo: convencion de destruccion."]
},
"dialog": {
  "use": ["Decisiones irreversibles o informacion que bloquea la tarea."],
  "avoid": ["Formularios largos: mejor una ventana propia."],
  "rules": ["Un solo primary; cancelar siempre visible. ESC cierra."]
},
"segmented": {
  "use": ["Cambiar modo de vista de un mismo contenido."],
  "avoid": ["Destinos de navegacion distintos: tabs."],
  "rules": ["2-5 segmentos; textos cortos, nunca iconos solos si son ambiguos."]
},
"table": {
  "use": ["Comparacion escaneable de muchos registros homogeneos."],
  "avoid": ["Menos de 3 filas: lista simple."],
  "rules": ["Header secundario uppercase; seleccion llena con accent."]
},
"empty-state": {
  "use": ["Primer uso y resultados vacios: ensena el proximo paso."],
  "avoid": ["Culpar al usuario; tono neutro y accion claro."],
  "rules": ["Orbe + titulo corto + una sola accion primary."]
},
"progress-spinner-skeleton": {
  "use": ["Progress bar: duracion conocida. Spinner: desconocida y corta. Skeleton: layout predecible."],
  "avoid": ["Spinner para esperas mayores a 3s con progreso medible."],
  "rules": ["Indeterminado comunica vida, no progreso real."]
},
}

for name, g in G.items():
    p = pathlib.Path("spec") / f"{name}.json"
    if not p.exists():
        print("skip", name); continue
    d = json.loads(p.read_text())
    d["guidance"] = g
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1))
print("guidance agregado a", len(G), "widgets")
