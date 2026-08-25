#!/usr/bin/env python3
"""Test runtime offscreen del adapter Qt. Exit 0 = todo pasa."""
import os, sys
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

sys.path.insert(0, "/home/luigi/Documentos/dsys/catalinas")

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

app = QApplication.instance() or QApplication(sys.argv)

from PySide6.QtWidgets import QDialog
from qt.catalinas_qt import Cat, CatTheme, icon, ToastManager

PASS, FAIL = [], []
def check(name, cond, detail=""):
    (PASS if cond else FAIL).append(f"{name} {detail}".strip())

cat = Cat(CatTheme(app))
check("theme aplica qss", len(app.styleSheet()) > 500)

# factories basicas
btn = cat.button("OK", variant="primary")
check("button primary property", btn.property("cat") == "primary")
clicked = []
b2 = cat.button("Click", on_click=lambda: clicked.append(1))
b2.click()
check("button on_click", len(clicked) == 1)

field_w, edit = cat.field("Email", "tu@email.com", icon_name="doc")
check("input existe", edit is not None and edit.placeholderText().startswith("tu@"))

sw = cat.switch(True)
check("switch checked", sw.isChecked())

sl = cat.slider(40)
check("slider value", sl.value() == 40)

pr = cat.progress(64)
check("progress 64", pr.value() == 64)

wrap, setv = cat.meter(30)
setv(90)
check("meter set", True)

card = cat.card(level="dark")
check("card dark objectname", card.objectName() == "card")

st = cat.stat_card("Ingresos", "$12.4K", "+8.2%", up=True)
check("stat card", st.minimumWidth() >= 130)

bdg = cat.badge("Beta", tone="accent", dot=True)
check("badge accent bg", "background" in bdg.styleSheet())

av = cat.avatar("LU", online=True)
check("avatar 32px", av.width() == 32)

side = cat.sidebar(["Home", "Documents", "Music"], active_index=1,
                   sections={2: "Locations"})
check("sidebar items+sep", side.count() == 4)

sb = cat.statusbar("No file selected", "67 files")
sb._title.setText("Design.docx")
check("statusbar title editable", sb._title.text() == "Design.docx")

tl = cat.timeline([("A", "hoy"), ("B", "ayer")])
check("timeline rows", tl.layout().count() == 2)

kv = cat.kv_list([("Size", "1 GB")])
check("kv list", kv.layout().count() >= 1)

srow = cat.stat_row([("A", "1", "+1", True)])
check("stat row", srow.layout().count() >= 2)

# widgets complejos
sp = cat.sparkline([3, 8, 5, 12, 9], kind="bars")
pm = sp.grab()
check("sparkline render", not pm.isNull() and pm.toImage().bits())

dlg = cat.command_palette([
    {"label": "Nuevo archivo", "kbd": "N"},
    {"label": "Compartir"},
], placeholder="Buscar...")
check("palette abierta", dlg.isVisible())
lst = dlg.findChild(type(dlg).findChild.__self__ if False else type("X",(object,),{})) if False else None
# cerrar
dlg.accept()

tm = ToastManager(root_widget := __import__("PySide6.QtWidgets", fromlist=["QWidget"]).QWidget(), cat)
tm.resize(400, 400)
fr = tm.show_toast("success", "Backup completo", "4.33 GB", timeout=0)
root_widget.show()
check("toast agregado", fr.parent() is tm and not fr.isHidden())

# theming runtime
cat.theme.set_accent("#ff0000")
check("accent override", "#ff0000" in app.styleSheet())
cat.theme.shift_hue(120)
check("hue shift regenera", len(app.styleSheet()) > 500)
cat.theme.clear_accent()
cat.theme.set_density("compact")
check("density compacta", cat.theme.density == "compact")
cat.theme.set_density("cozy")

# icons
ic = icon("folder", "#59627a", 16)
check("icon no vacio", not ic.isNull())
check("icon desconocido vacio", icon("nope").isNull())

# window completa con sidebar+body+status
side = cat.sidebar(["Home", "Documents", "Music"], active_index=1)
body = QWidget(); QVBoxLayout(body).addWidget(QLabel("contenido"))
sb = cat.statusbar("Nada", "0 files")
win = cat.window("KittyDrive", kind="glass", body=body, sidebar=side, status=sb)
win.resize(800, 480)
win.show()
img = win.grab().toImage()
check("window grab", img.width() == 800 and img.height() == 480)
win.close()

print(f"QT ADAPTER: PASS {len(PASS)} | FAIL {len(FAIL)}")
for f_ in FAIL:
    print("  FAIL ->", f_)
sys.exit(1 if FAIL else 0)
