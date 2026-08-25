"""
Catalinas Design System - Qt/PySide6 adapter completo.

Capas:
  1. THEME      : carga tokens generados + aplica QSS + re-theming en runtime
                  (set_accent / set_wallpaper_hue / set_density)
  2. FACTORIES  : constructores de widgets con la anatomia del sistema
                  (button, switch, input, card, stat_card, sidebar, rows,
                   statusbar, tabbar, timeline, kv_list, meter, badge...)
  3. WIDGETS    : componentes con comportamiento propio
                  (Sparkline, Switch, ToastManager, CommandPalette, CatWindow)
  4. ICONS      : QIcon desde los mismos path SVG que usa la web

Requiere PySide6. Uso minimo:

    from PySide6.QtWidgets import QApplication
    from qt.catalinas_qt import Cat

    app = QApplication([])
    cat = Cat(app)                      # aplica el tema
    btn = cat.button("Aceptar", variant="primary")
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

from PySide6.QtCore import (
    QEasingCurve, QEvent, QPoint, QPointF, QRectF, QSize, Qt, QTimer, Property,
)
from PySide6.QtGui import (
    QColor, QFont, QIcon, QImage, QPainter, QPainterPath, QPen, QPixmap,
    QGuiApplication,
)
from PySide6.QtWidgets import (
    QApplication, QCheckBox, QDialog, QFileDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMessageBox, QPushButton, QScrollArea, QSizePolicy, QSlider, QStatusBar,
    QProgressBar, QVBoxLayout, QWidget, QGraphicsDropShadowEffect, QComboBox,
    QTextEdit,
)

try:
    from PySide6.QtSvg import QSvgRenderer
    _HAS_SVG = True
except ImportError:
    _HAS_SVG = False

# ---------------------------------------------------------------- tokens
sys.path.insert(0, str(Path(__file__).resolve().parent))
from qt.theme import TOKENS, get as _tok  # noqa: E402


def px(path, default=0):
    v = _tok(path, default)
    try:
        return float(str(v).replace("px", ""))
    except ValueError:
        return float(default)


DENSITY_SCALES = {
    "compact":     {"sm": 22, "md": 26, "lg": 30, "row": 32},
    "cozy":        {"sm": 24, "md": 30, "lg": 36, "row": 38},
    "comfortable": {"sm": 28, "md": 34, "lg": 40, "row": 44},
}


class CatTheme:
    """Tema runtime: aplica QSS y permite re-theming en vivo."""

    def __init__(self, app: QApplication | None = None):
        self.app = app or QApplication.instance()
        self.density = "cozy"
        self.accent_override: str | None = None
        self.hue_shift = 0
        self.base_hue = int(_tok("semantic.wall_hue_1", 220))
        self._apply()

    # ---------- color helpers ----------
    @staticmethod
    def _hsl(h, s, l, a=1.0):
        c = QColor()
        c.setHslF((h % 360) / 360.0, max(0.0, min(1.0, s)), max(0.0, min(1.0, l)), a)
        return c.name(QColor.HexArgb) if a < 1.0 else c.name()

    @property
    def accent(self) -> str:
        if self.accent_override:
            return self.accent_override
        h = (self.base_hue + self.hue_shift) % 360
        return self._hsl(h, 0.60, 0.55)

    @property
    def accent_dim(self) -> str:
        h = (self.base_hue + self.hue_shift) % 360
        return self._hsl(h, 0.55, 0.34)

    @property
    def accent_ring(self) -> str:
        h = (self.base_hue + self.hue_shift) % 360
        return self._hsl(h, 0.65, 0.60, 0.28)

    @property
    def ink(self):
        return {"hi": _tok("color.ink.hi"), "mid": _tok("color.ink.mid"),
                "low": _tok("color.ink.low"), "faint": _tok("color.ink.faint")}

    # ---------- QSS ----------
    def qss(self) -> str:
        d = DENSITY_SCALES[self.density]
        acc = self.accent
        ink = self.ink
        danger = _tok("color.danger.base")
        success = _tok("color.success")
        warning = _tok("color.warning")
        surf = lambda p: _tok(p)
        r_sm, r_md = px("size.radius.sm"), px("size.radius.md")
        return f"""
        * {{ font-family: '{_tok("font.family_ui").split(",")[0].strip("'")}';
             font-size: {_tok('font.size.base')}; color: {ink['mid']};
             selection-background-color: {acc}; }}
        QLabel, QFrame {{ background: transparent; }}

        /* ---- botones ---- */
        QPushButton[cat="primary"] {{ background:{acc}; color:white; border:none;
            border-radius:{r_sm}px; padding:7px 14px; font-weight:600;
            height:{d['md']}px; }}
        QPushButton[cat="primary"]:hover {{ background:{self.accent_dim}; }}
        QPushButton[cat="primary"]:pressed {{ background:{self._hsl(int((self.base_hue+self.hue_shift)%360), .6, .40)}; }}
        QPushButton[cat="secondary"] {{ background:rgba(255,255,255,140); color:{ink['hi']};
            border:1px solid {surf('color.stroke.input')}; border-radius:{r_sm}px; padding:7px 14px;
            height:{d['md']}px; font-weight:500; }}
        QPushButton[cat="secondary"]:hover {{ background:rgba(255,255,255,220); }}
        QPushButton[cat="danger"] {{ background:{danger}; color:white; border:none;
            border-radius:{r_sm}px; padding:7px 14px; height:{d['md']}px; font-weight:600; }}
        QPushButton[cat="danger"]:hover {{ background:{_tok('color.danger.hover')} }}
        QPushButton[cat="ghost"] {{ background:transparent; border:none; color:{ink['mid']};
            padding:7px 12px; height:{d['md']}px; }}
        QPushButton[cat="ghost"]:hover {{ background:rgba(255,255,255,120); color:{ink['hi']}; }}
        QPushButton:disabled {{ opacity:.45 }}
        QPushButton[flat="true"] {{ border:none; background:transparent; }}

        /* ---- inputs ---- */
        QLineEdit, QTextEdit, QComboBox {{ background:rgba(255,255,255,130);
            border:1px solid {surf('color.stroke.input')}; border-radius:10px;
            padding:6px 12px; color:{ink['hi']}; height:{d['md']}px; }}
        QLineEdit:focus, QTextEdit:focus, QComboBox:focus {{
            border-color:{acc}; background:rgba(255,255,255,235); }}

        /* ---- switch / check / radio ---- */
        QCheckBox::indicator{{ width:17px;height:17px;border-radius:4px;
            border:1.5px solid {surf('color.stroke.input')};background:rgba(255,255,255,160)}}
        QCheckBox::indicator:checked{{ background:{acc};border-color:transparent}}
        QRadioButton::indicator{{ width:17px;height:17px;border-radius:9px;
            border:1.5px solid {surf('color.stroke.input')};background:rgba(255,255,255,160)}}
        QRadioButton::indicator:checked{{ background:{acc};border-color:transparent}}

        /* ---- slider ---- */
        QSlider::groove:horizontal {{ height:4px; background:rgba(0,0,0,36);
            border-radius:2px; }}
        QSlider::sub-page:horizontal {{ background:{acc}; border-radius:2px; }}
        QSlider::handle:horizontal {{ width:15px;height:15px;margin:-6px 0;
            border-radius:8px;background:white;border:.5px solid rgba(0,0,0,38)}}

        /* ---- progress / meter ---- */
        QProgressBar {{ background:rgba(0,0,0,26); border:none;
            border-radius:3px; height:5px; text-align:center; }}
        QProgressBar::chunk {{ background:{acc}; border-radius:3px; }}

        /* ---- menus / combos ---- */
        QMenu {{ background:{surf('color.surface.menu')};
            border:1px solid {surf('color.stroke.menu')};
            border-radius:{r_md}px; padding:5px; }}
        QMenu::item {{ padding:5px 22px 5px 10px; border-radius:{r_sm}px;
            color:{ink['hi']}; }}
        QMenu::item:selected {{ background:{acc}; color:white; }}
        QMenu::separator {{ height:1px; background:{surf('color.stroke.dark')};
            margin:5px 8px; }}
        QComboBox QAbstractItemView {{ background:{surf('color.surface.menu')};
            border:1px solid {surf('color.stroke.menu')}; selection-background-color:{acc};
            selection-color:white; border-radius:{r_md}px; }}

        /* ---- tabs ---- */
        QTabBar::tab {{ background:transparent; color:{ink['mid']};
            padding:6px 14px; border-radius:7px; margin-right:4px; }}
        QTabBar::tab:selected {{ background:rgba(255,255,255,200);
            color:{ink['hi']}; font-weight:600;
            border:1px solid {surf('color.stroke.dark')}; }}

        /* ---- listas / arbol ---- */
        QListWidget, QTreeWidget, QTableWidget, QListView {{
            background:transparent; border:none; outline:none; }}
        QListWidget::item {{ height:{d['row']}px; border-radius:{r_sm}px; padding-left:8px; }}
        QListWidget::item:hover {{ background:rgba(255,255,255,130); color:{ink['hi']}; }}
        QListWidget::item:selected {{ background:{acc}; color:white; }}
        QTreeWidget::item:hover {{ background:rgba(0,0,0,14); border-radius:{px('size.radius.xs')}px; }}
        QTreeWidget::item:selected {{ background:{acc}; color:white; border-radius:{r_sm}px; }}

        /* ---- tabla ---- */
        QHeaderView::section {{ background:transparent; border:none;
            border-bottom:1px solid {surf('color.stroke.dark')}; padding:6px 12px;
            font-size:{_tok('font.size.xs')}; font-weight:500;
            letter-spacing:.4px; text-transform:uppercase; color:{ink['low']}; }}
        QTableWidget {{ gridline-color:transparent; background:transparent;
            border:none; alternate-background-color:transparent; }}
        QTableWidget::item {{ padding:6px 10px; }}
        QTableWidget::item:selected {{ background:{acc}; color:white; }}

        /* ---- scrollbars finos ---- */
        QScrollBar:vertical {{ width:8px; background:transparent; margin:2px; }}
        QScrollBar::handle:vertical {{ background:rgba(0,0,0,.18);
            border-radius:4px; min-height:28px; }}
        QScrollBar::handle:vertical:hover {{ background:rgba(0,0,0,.30); }}
        QScrollBar:horizontal {{ height:8px; background:transparent; margin:2px; }}
        QScrollBar::handle:horizontal {{ background:rgba(0,0,0,.18);
            border-radius:4px; min-width:28px; }}
        QScrollBar::add-line,QScrollBar::sub-line {{ height:0;width:0 }}
        """

    def _apply(self):
        if self.app:
            self.app.setStyleSheet(self.qss())

    # ---------- API publica de theming ----------
    def set_accent(self, hex_color: str):
        """Override manual del accent (ignora derivacion hasta clear_accent)."""
        self.accent_override = hex_color
        self._apply()

    def clear_accent(self):
        self.accent_override = None
        self._apply()

    def shift_hue(self, degrees: int):
        """Rotacion de hue estilo wallpaper-reactive."""
        self.hue_shift = degrees % 360
        self._apply()

    def set_density(self, name: str):
        assert name in DENSITY_SCALES, name
        self.density = name
        self._apply()

    def derive_accent_from_image(self, image_path: str):
        """Deriva el accent del hue dominante de una imagen (wallpaper)."""
        img = QImage(image_path)
        if img.isNull():
            return None
        small = img.scaled(8, 8, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        rs = gs = bs = n = 0
        best_w = 0
        best_h = self.base_hue
        from collections import defaultdict
        bins = defaultdict(lambda: [0, 0.0])
        for y in range(8):
            for x in range(8):
                c = small.pixelColor(x, y)
                h, s, l, _ = c.getHslF()
                if s < 0.06 or l < 0.15 or l > 0.95:
                    continue
                wgt = s * (1 - abs(l - 0.72))
                b = int(h * 24) % 24
                bins[b][0] += wgt
                bins[b][1] = h
                rs += c.red(); gs += c.green(); bs += c.blue(); n += 1
        if bins:
            bb = max(bins.items(), key=lambda kv: kv[1][0])
            self.base_hue = int(bb[1][1])
        self._apply()
        return self.accent


# ---------------------------------------------------------------- icons
ICON_PATHS = {
    "folder": "M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z",
    "doc": ("M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z "
            "M14 3v5h5 M9 13h6 M9 16h6"),
    "ppt": ("M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z "
            "M14 3v5h5 M9 14h6 M9 17h4"),
    "music": ("M9 18V6l10-2v12 M6.5 18a2.5 2.5 0 1 0 0-.01 M16.5 16a2.5 2.5 0 1 0 0-.01"),
    "img": ("M3 5h18v14H3z M21 16l-5-5-9 8"),
    "home": ("M3 11l9-8 9 8 M5 10v10h5v-6h4v6h5V10"),
    "cloud": "M6 19a5 5 0 1 1 .9-9.92A7 7 0 0 1 20 11a4 4 0 0 1-1 7.87z",
    "desktop": "M3 4h18v12H3z M8 20h8 m-4-4v4",
    "cat": ("M5 3l3 3h8l3-3v6a7 7 0 0 1-14 0z M10 12h.01 M14 12h.01"),
    "net": ("M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18z M3 12h18 "
            "M12 3c3 3.5 3 14.5 0 18 M12 3c-3 3.5-3 14.5 0 18"),
}


def icon(name: str, color: str = "#59627a", size: int = 16) -> QIcon:
    """QIcon desde los mismos paths que la web (single source visual)."""
    ic = QIcon()
    if not _HAS_SVG or name not in ICON_PATHS:
        return ic
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
           f'fill="none" stroke="{color}" stroke-width="2" '
           f'stroke-linecap="round" stroke-linejoin="round">'
           f'<path d="{ICON_PATHS[name]}"/></svg>')
    for scale in (1, 2):
        s = size * scale
        pm = QPixmap(s, s)
        pm.fill(Qt.transparent)
        r = QSvgRenderer(bytes(svg, "utf-8"))
        pt = QPainter(pm)
        r.render(pt)
        pt.end()
        ic.addPixmap(pm)
    return ic


# ---------------------------------------------------------------- factories
class Cat:
    """Namespace de factories. Instancialo con el theme activo."""

    def __init__(self, theme: CatTheme | None = None, app: QApplication | None = None):
        self.theme = theme or CatTheme(app)
        self.app = self.theme.app
        if self.app is None:
            raise RuntimeError("Crea QApplication primero")

    # helpers internos
    def _btn(self, text, variant, size="md", icon_name=None, parent=None):
        b = QPushButton(text, parent)
        b.setProperty("cat", variant)
        if size != "md":
            b.setProperty("size", size)
            f = b.font()
            f.setPointSize(11 if size == "sm" else 13)
            b.setFont(f)
        if icon_name:
            b.setIcon(icon(icon_name, "#ffffff" if variant in ("primary", "danger")
                           else self.theme.ink["mid"]))
        return b

    # ---------- acciones ----------
    def button(self, text="", *, variant="primary", size="md",
               icon_name=None, on_click=None, parent=None) -> QPushButton:
        b = self._btn(text, variant, size, icon_name, parent)
        if on_click:
            b.clicked.connect(on_click)
        return b

    def ghost_button(self, text="", **kw) -> QPushButton:
        return self.button(text, variant="ghost", **kw)

    def danger_button(self, text="", **kw) -> QPushButton:
        return self.button(text, variant="danger", **kw)

    # ---------- entrada ----------
    def field(self, label="", placeholder="", *, icon_name=None,
              error="", parent=None) -> tuple[QWidget, QLineEdit]:
        box = QWidget(parent)
        lay = QVBoxLayout(box)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(4)
        if label:
            lb = QLabel(label, box)
            lb.setStyleSheet(f"font-size:{_tok('font.size.xs')};"
                             f"font-weight:500;color:{self.theme.ink['mid']}")
            lay.addWidget(lb)
        holder = QWidget(box)
        hl = QHBoxLayout(holder)
        hl.setContentsMargins(0, 0, 0, 0)
        edit = QLineEdit(holder)
        edit.setPlaceholderText(placeholder)
        if icon_name:
            edit.setTextMargins(24, 0, 8, 0)
            ic = QLabel(holder)
            ic.setPixmap(icon(icon_name, self.theme.ink["low"], 13).pixmap(13, 13))
            ic.setStyleSheet("margin-left:10px")
            ic.setParent(edit)
            ic.move(10, (edit.height() - 13) // 2 or 8)
        hl.addWidget(edit)
        lay.addWidget(holder)
        if error:
            msg = QLabel(error, box)
            msg.setStyleSheet(f"color:{_tok('color.danger.base')};font-size:{_tok('font.size.xs')}")
            lay.addWidget(msg)
        return box, edit

    def switch(self, checked=False, on_change=None, parent=None) -> QCheckBox:
        sw = QCheckBox(parent)
        sw.setChecked(checked)
        sw.setText("")
        if on_change:
            sw.toggled.connect(on_change)
        return sw

    def slider(self, value=50, minimum=0, maximum=100, on_change=None, parent=None) -> QSlider:
        sl = QSlider(Qt.Horizontal, parent)
        sl.setRange(minimum, maximum)
        sl.setValue(value)
        if on_change:
            sl.valueChanged.connect(on_change)
        return sl

    # ---------- feedback ----------
    def progress(self, value=0, indeterminate=False, parent=None) -> QProgressBar:
        pr = QProgressBar(parent)
        pr.setRange(0, 100 if not indeterminate else 0)
        pr.setValue(value)
        pr.setTextVisible(False)
        pr.setFixedHeight(5)
        if indeterminate:
            pr.setRange(0, 0)
        return pr

    def meter(self, value_pct: int, parent=None) -> tuple[QWidget, callable]:
        wrap = QWidget(parent)
        lay = QVBoxLayout(wrap)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(4)
        bar = QProgressBar(wrap)
        bar.setValue(max(0, min(100, value_pct)))
        bar.setTextVisible(False)
        bar.setFixedHeight(5)
        col = (_tok("color.success") if value_pct < 60
               else _tok("color.warning") if value_pct < 85
               else _tok("color.danger.base"))
        bar.setStyleSheet(f"QProgressBar::chunk{{background:{col}}}")
        lab = QLabel(f"{value_pct}%", wrap)
        lab.setStyleSheet(f"font-size:{_tok('font.size.xs')};color:{self.theme.ink['low']}")
        lay.addWidget(bar)
        lay.addWidget(lab)

        def set_value(v):
            bar.setValue(v)
            lab.setText(f"{v}%")
            col = (_tok("color.success") if v < 60 else
                   _tok("color.warning") if v < 85 else
                   _tok("color.danger.base"))
            bar.setStyleSheet(f"QProgressBar::chunk{{background:{col}}}")
        return wrap, set_value

    def spinner(self, parent=None) -> QLabel:
        lb = QLabel(parent)
        lb.setText("Loading...")
        lb.setStyleSheet(f"color:{self.theme.ink['faint']};font-size:{_tok('font.size.sm')}")
        return lb

    # ---------- superficies ----------
    def card(self, *children, level="content", parent=None) -> QFrame:
        fr = QFrame(parent)
        fr.setObjectName("card")
        if level == "dark":
            bg = _tok("color.dark.player_bg")
            border = "rgba(255,255,255,.14)"
            fg = _tok("color.dark.player_ink")
        elif level == "float":
            bg = _tok("color.surface.card")
            border = _tok("color.stroke.light")
            fg = self.theme.ink["hi"]
        else:
            bg = {"content": _tok("color.surface.content"),
                  "chip": _tok("color.surface.glass_chip")}.get(level,
                                                                _tok("color.surface.card"))
            border = _tok("color.stroke.light")
            fg = self.theme.ink["hi"]
        fr.setStyleSheet(
            "#card{background:" + bg + ";border:1px solid " + border +
            ";border-radius:" + str(px('size.radius.lg')) + "px}" +
            ("#card QLabel,#card QPushButton{color:" + fg + "}" if level == "dark" else ""))
        lay = QVBoxLayout(fr)
        lay.setContentsMargins(16, 16, 16, 16)
        lay.setSpacing(8)
        for c in children:
            lay.addWidget(c)
        return fr

    def stat_card(self, label: str, value: str, delta: str = "",
                  up: bool = True, parent=None) -> QFrame:
        fr = QFrame(parent)
        fr.setMinimumWidth(130)
        fr.setStyleSheet(
            f"QFrame{{background:{_tok('color.surface.card')};"
            f"border:1px solid var(--cat-color-stroke-dark, rgba(20,30,60,.08));"
            f"border-radius:{px('size.radius.md')}px}}")
        lay = QVBoxLayout(fr)
        lay.setContentsMargins(14, 12, 14, 12)
        lay.setSpacing(2)
        l1 = QLabel(label); l1.setStyleSheet(f"font-size:{_tok('font.size.xs')};"
                                             f"color:{self.theme.ink['low']}")
        l2 = QLabel(value)
        f = l2.font(); f.setPointSize(15); f.setBold(True); l2.setFont(f)
        l2.setStyleSheet(f"color:{self.theme.ink['hi']}")
        col = _tok("color.success") if up else _tok("color.danger.base")
        arrow = "+" if up else ""
        l3 = QLabel(f"{arrow}{delta}" if delta and not delta.startswith(("+", "-")) else delta)
        l3.setStyleSheet(f"font-size:{_tok('font.size.xs')};font-weight:600;color:{col}")
        for wdg in (l1, l2, l3):
            lay.addWidget(wdg)
        return fr

    def badge(self, text, tone="neutral", dot=False, parent=None) -> QLabel:
        colors = {"accent": ACC if False else self.theme.accent,
                  "success": _tok("color.success"),
                  "danger": _tok("color.danger.base")}
        bg = colors.get(tone, "rgba(0,0,0,.07)")
        fg = "#fff" if tone in colors else self.theme.ink["mid"]
        lb = QLabel(("● " if dot else "") + text, parent)
        lb.setStyleSheet(f"background:{bg};color:{fg};border-radius:10px;"
                         f"padding:2px 8px;font-size:{_tok('font.size.2xs')};"
                         f"font-weight:600")
        return lb

    def avatar(self, initials: str, online=False, parent=None) -> QLabel:
        av = QLabel(initials, parent)
        av.setAlignment(Qt.AlignCenter)
        av.setFixedSize(32, 32)
        av.setStyleSheet(f"background:{self.theme.accent};color:#fff;"
                         f"border-radius:16px;font-weight:600;font-size:12px")
        if online:
            av.setText(f"{initials} ●")
        return av

    # ---------- navegacion ----------
    def sidebar(self, items: list[str], active_index: int = 0,
                sections: dict[int, str] | None = None,
                on_change=None, parent=None) -> QListWidget:
        lw = QListWidget(parent)
        lw.setFixedWidth(216)
        lw.setIconSize(QSize(16, 16))
        lw.setStyleSheet(
            f"QListWidget{{background:{_tok('color.surface.glass_chip')};"
            f"border-right:1px solid var(--cat-color-stroke-softer, rgba(20,30,60,.05));"
            f"padding:10px 8px}}")
        sections = sections or {}
        icon_keys = {}
        mapping = {"Documents": "folder", "Music": "music", "Pictures": "img",
                   "Desktop": "desktop", "Home": "home", "Network": "net",
                   "KittyDrive": "cloud"}
        for i, name in enumerate(items):
            it = QListWidgetItem(name)
            key = mapping.get(name, "folder")
            it.setIcon(icon(key, self.theme.ink["mid"], 16))
            if i in sections:
                sep = QListWidgetItem(sections[i])
                sep.setFlags(Qt.NoItemFlags)
                sep.setForeground(QColor(self.theme.ink["faint"]))
                f = sep.font(); f.setPointSize(8); f.setBold(True)
                sep.setFont(f)
                lw.addItem(sep)
                it = QListWidgetItem(name)
                it.setIcon(icon(key, self.theme.ink["mid"], 16))
            lw.addItem(it)
            if i == active_index:
                it.setSelected(True)
        if on_change:
            lw.currentRowChanged.connect(on_change)
        return lw

    def statusbar(self, left_title="", right_count="", parent=None) -> QFrame:
        fr = QFrame(parent)
        fr.setStyleSheet(f"QFrame{{background:{_tok('color.surface.glass_chip')};"
                         f"border-top:1px solid var(--cat-color-stroke-dark, rgba(20,30,60,.06));"
                         f"border-radius:{px('size.radius.sm')}px}}")
        lay = QHBoxLayout(fr)
        lay.setContentsMargins(14, 8, 14, 8)
        t = QLabel(left_title)
        t.setStyleSheet(f"font-weight:550;color:{self.theme.ink['hi']};font-size:12px")
        c = QLabel(right_count)
        c.setStyleSheet(f"font-size:11px;color:{self.theme.ink['mid']}")
        lay.addWidget(t)
        lay.addStretch(1)
        lay.addWidget(c)
        fr._title = t
        fr._count = c
        return fr

    # ---------- datos ----------
    def timeline(self, entries: list[tuple[str, str]], parent=None) -> QWidget:
        wrap = QWidget(parent)
        lay = QVBoxLayout(wrap)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(14)
        for i, (title, when) in enumerate(entries):
            row = QHBoxLayout()
            row.setSpacing(10)
            done = i > 0
            col = _tok("color.success") if done else self.theme.accent
            dot = QLabel()
            dot.setFixedSize(11, 11)
            dot.setStyleSheet(f"background:{col};border-radius:6px;"
                              f"border:3px solid var(--cat-color-accent-subtle-b, rgba(94,158,255,.12))")
            body = QLabel(f"<b style='color:{self.theme.ink['hi']}'>{title}</b>"
                          f"<br><span style='color:{self.theme.ink['faint']};font-size:11px'>{when}</span>")
            row.addWidget(dot, 0, Qt.AlignTop)
            row.addWidget(body, 1)
            lay.addLayout(row)
        return wrap

    def kv_list(self, pairs, parent=None):
        fr = QFrame(parent)
        lay = QVBoxLayout(fr)
        lay.setContentsMargins(2, 2, 2, 2)
        lay.setSpacing(0)
        for i, (k, v) in enumerate(pairs):
            row = QHBoxLayout()
            k1 = QLabel(k); k1.setStyleSheet(f"color:{self.theme.ink['mid']}")
            v1 = QLabel(v); v1.setStyleSheet(f"color:{self.theme.ink['hi']};font-weight:500")
            row.addWidget(k1); row.addStretch(1); row.addWidget(v1)
            lay.addLayout(row)
            if i < len(pairs) - 1:
                line = QFrame(); line.setFixedHeight(1)
                line.setStyleSheet(f"background:var(--cat-color-stroke-softer, rgba(20,30,60,.05))")
                lay.addWidget(line)
        return fr

    def stat_row(self, stats: list[tuple[str, str, str, bool]], parent=None) -> QWidget:
        wrap = QWidget(parent)
        lay = QHBoxLayout(wrap)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(10)
        for lbl, val, delta, up in stats:
            lay.addWidget(self.stat_card(lbl, val, delta, up))
        lay.addStretch(1)
        return wrap

    # ---------- ventanas ----------
    def window(self, title: str, kind: str = "glass", body: QWidget | None = None,
               sidebar: QListWidget | None = None,
               status: QFrame | None = None, parent=None) -> QWidget:
        win = QWidget(parent)
        win.setObjectName("win")
        if kind == "glass":
            base = (f"#win{{background:{_tok('color.surface.glass-window')};"
                    f"border:1px solid {_tok('color.stroke.light')};"
                    f"border-radius:{px('size.radius.window')}px}}")
        else:
            base = (f"#win{{background:white;"
                    f"border:1px solid {_tok('color.stroke.input')};"
                    f"border-radius:{px('size.radius.window')}px}}")
        win.setStyleSheet(base + f"\n#win QLabel{{color:{self.theme.ink['hi']}}}")
        root = QVBoxLayout(win)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        bar = QWidget(win)
        bl = QHBoxLayout(bar)
        bl.setContentsMargins(14, 10, 10, 8)
        ttl = QLabel(title)
        ttl.setStyleSheet(f"font-weight:600;font-size:{_tok('font.size.base')}")
        bl.addWidget(ttl)
        bl.addStretch(1)
        for role, glyph in (("min", "–"), ("max", "▢"), ("close", "✕")):
            b = QPushButton(glyph, bar)
            b.setFixedSize(28, 24)
            b.setCursor(Qt.PointingHandCursor)
            if role == "close":
                b.setToolTip("Cerrar")
            bl.addWidget(b)
        root.addWidget(bar)

        mid = QWidget(win)
        ml = QHBoxLayout(mid)
        ml.setContentsMargins(14, 0, 14, 0)
        ml.setSpacing(0)
        if sidebar:
            ml.addWidget(sidebar)
        content = QScrollArea(mid)
        content.setWidgetResizable(True)
        content.setFrameShape(QFrame.NoFrame)
        inner = body or QWidget()
        content.setWidget(inner)
        ml.addWidget(content, 1)
        root.addWidget(mid, 1)

        if status:
            st_wrap = QWidget(win)
            sl = QVBoxLayout(st_wrap)
            sl.setContentsMargins(14, 8, 14, 12)
            sl.addWidget(status)
            root.addWidget(st_wrap)
        return win

    # ---------- widgets complejos ----------
    def sparkline(self, values, kind="line", w=120, h=32, parent=None) -> QWidget:
        class Spark(QWidget):
            def __init__(s):
                super().__init__(parent)
                s.setFixedSize(w, h)
                s.values = list(values)

            def paintEvent(s, ev):
                pt = QPainter(s)
                pt.setRenderHint(QPainter.Antialiasing)
                col = QColor(self.theme.accent)
                pen = QPen(col, 2)
                pen.setCapStyle(Qt.RoundCap)
                pen.setJoinStyle(Qt.RoundJoin)
                pt.setPen(pen)
                if kind == "bars":
                    pt.setBrush(col)
                    n = len(s.values)
                    bw = w / n * .6
                    gap = w / n * .4
                    mx = max(s.values) or 1
                    for i, v in enumerate(s.values):
                        bh = (v / mx) * (h - 4)
                        pt.drawRoundedRect(QRectF(i * w / n + gap / 2, h - bh, bw, bh), 2, 2)
                else:
                    mx = max(s.values) or 1
                    mn = min(s.values)
                    rng = (mx - mn) or 1
                    pts = [QPointF(i / (len(s.values) - 1) * w,
                                   h - ((v - mn) / rng) * (h - 4) - 2)
                           for i, v in enumerate(s.values)]
                    pt.drawPolyline(*pts)
        return Spark()

    def command_palette(self, items: list[dict], placeholder="Escribe un comando...",
                        on_pick=None, parent=None) -> QDialog:
        dlg = QDialog(parent or self.app.activeWindow() or None)
        dlg.setWindowTitle("")
        dlg.setModal(True)
        dlg.setFixedWidth(520)
        dlg.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        dlg.setAttribute(Qt.WA_TranslucentBackground)
        lay = QVBoxLayout(dlg)
        lay.setContentsMargins(0, 0, 0, 0)
        inp = QLineEdit(dlg)
        inp.setPlaceholderText(placeholder)
        inp.setFixedHeight(44)
        inp.setStyleSheet("padding:0 16px;font-size:15px;border:none;"
                          "background:transparent;")
        lst = QListWidget(dlg)
        lst.setStyleSheet(f"QListWidget{{max-height:280px;padding:5px;border:none}}")
        lay.addWidget(inp)
        lay.addWidget(lst)

        all_items = list(items)

        def refill(q=""):
            lst.clear()
            for it in all_items:
                if isinstance(it, str):
                    it = {"label": it}
                if q and q.lower() not in it["label"].lower():
                    continue
                li = QListWidgetItem(it["label"])
                li.setData(Qt.UserRole, it)
                lst.addItem(li)
            if lst.count():
                lst.setCurrentRow(0)

        def pick(item):
            data = item.data(Qt.UserRole)
            dlg.accept()
            cb = (on_pick if on_pick else data.get("onSelect"))
            if cb:
                cb(data)

        refill()
        inp.textChanged.connect(refill)
        lst.itemClicked.connect(pick)
        inp.installEventFilter(dlg)
        dlg.keyPressEvent = lambda ev: (
            lst.keyPressEvent(ev) if ev.key() in (Qt.Key_Up, Qt.Key_Down)
            else QDialog.keyPressEvent(dlg, ev))
        dlg.show()
        inp.setFocus()
        return dlg

    def toasts(self, parent: QWidget) -> "ToastManager":
        return ToastManager(parent, self)


class ToastManager(QWidget):
    """Cola de toasts fijos arriba-derecha del parent."""

    def __init__(self, parent, cat: Cat):
        super().__init__(parent)
        self.cat = cat
        self.setFixedWidth(320)
        self.move(parent.width() - 340, 16)
        self.lay = QVBoxLayout(self)
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.setSpacing(8)

    def show_toast(self, tone="info", title="", message="", timeout=4200):
        colors = {"success": _tok("color.success"), "danger": _tok("color.danger.base"),
                  "warning": _tok("color.warning"), "info": self.cat.theme.accent}
        fr = QFrame(self)
        fr.setStyleSheet(
            f".cat-toast{{background:{_tok('color.surface.menu')};"
            f"border:1px solid {_tok('color.stroke.menu')};"
            f"border-radius:{px('size.radius.md')}px}}\n"
            f"QLabel{{color:{_tok('color.ink.hi')}}}\n"
            f"QPushButton{{color:{self.cat.theme.ink['low']}}}")
        lay = QHBoxLayout(fr)
        lay.setContentsMargins(12, 10, 8, 10)
        dot = QLabel()
        dot.setFixedSize(8, 8)
        dot.setStyleSheet(f"background:{colors.get(tone, colors['info'])};border-radius:4px")
        body = QLabel(f"<b style='font-size:12.5px'>{title}</b>"
                      + (f"<br><span style='font-size:11px;color:{self.cat.theme.ink['mid']}'>{message}</span>"
                         if message else ""))
        x = QPushButton("✕", fr)
        x.setFixedSize(22, 22)
        x.setFlat(True)
        lay.addWidget(dot, 0, Qt.AlignTop)
        lay.addWidget(body, 1)
        lay.addWidget(x, 0, Qt.AlignTop)

        def kill():
            fr.hide()
            fr.deleteLater()
        x.clicked.connect(kill)
        self.lay.addWidget(fr)
        self.show()
        if timeout:
            QTimer.singleShot(timeout, kill)
        return fr


# ---------------------------------------------------------------- demo
def run_demo():
    app = QApplication.instance() or QApplication(sys.argv)
    cat = Cat(CatTheme(app))

    root = QWidget()
    root.setWindowTitle("Catalinas Qt Demo")
    root.resize(980, 620)
    lay = QVBoxLayout(root)
    lay.setContentsMargins(24, 24, 24, 24)

    side_items = ["Home", "Documents", "Desktop", "Downloads",
                  "Pictures", "Music", "Cats", "Network"]
    side = cat.sidebar(side_items, active_index=1,
                       sections={2: "Favorites", 7: "Locations"})
    side.setCurrentRow(1)

    head = QHBoxLayout()
    head.addWidget(cat.button("+ Add New", variant="primary"))
    head.addStretch(1)
    _, search = cat.field("", "Buscar...", icon_name="doc")
    search.setClearButtonEnabled(True)
    search.setFixedWidth(220)
    head.addWidget(search)

    body = QWidget()
    bv = QVBoxLayout(body)
    bv.setContentsMargins(20, 14, 20, 14)
    bv.setSpacing(12)
    bv.addWidget(cat.stat_row([("Archivos", "67", "+4", True),
                               ("En nube", "98%", "+1%", True),
                               ("Espacio", "12 GB", "-3 GB", False)]))
    bv.addWidget(cat.timeline([("Sincronizacion iniciada", "hace 2 min"),
                               ("Backup completado", "hace 1 h")]))
    kvw = cat.kv_list([("Tamano", "4.33 GB"), ("Elementos", "67"),
                          ("Modificado", "Aug 25, 2026")])
    bv.addWidget(kvw)
    bv.addStretch(1)

    sb = cat.statusbar("No file selected", "4 folders and 67 files · 4.33 GB")

    win = cat.window("KittyDrive", kind="glass", body=body,
                     sidebar=side, status=sb)
    lay.addWidget(win, 1)

    player_zone = QWidget()
    pv = QVBoxLayout(player_zone)
    dark = cat.card(level="dark")
    dv = dark.layout()
    dv.addWidget(QLabel("<div align='center'><b>Masacre en el puticlub</b></div>"))
    art = QLabel()
    art.setFixedSize(120, 90)
    art.setAlignment(Qt.AlignCenter)
    art.setStyleSheet(f"background:{ACC_QT_DEMO_GRADIENT};border-radius:12px;margin:6px 20px")
    dv.addWidget(art)
    dv.addWidget(cat.progress(64))
    controls = QHBoxLayout()
    controls.addStretch(1)
    controls.addWidget(cat.button("Play/Pause", variant="danger"))
    controls.addStretch(1)
    dv.addLayout(controls)
    pv.addWidget(dark)
    lay.addWidget(player_zone)

    toasts = cat.toasts(root)
    QTimer.singleShot(600, lambda: toasts.show_toast(
        "success", "Backup completo", "4.33 GB sincronizados"))

    root.show()
    return app, root, cat


ACC_QT_DEMO_GRADIENT = ("radial-gradient?" if False else
                        "qlineargradient(x1:0,y1:0,x2:1,y2:1,"
                        "stop:0 #ffd9e8, stop:.5 #cdb6ff, stop:1 #3a3f63)")


if __name__ == "__main__":
    app, root, cat = run_demo()
    QTimer.singleShot(1500, app.quit)
    sys.exit(app.exec())
