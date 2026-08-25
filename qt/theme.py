"""Catalinas Design System — generated Qt theme module, do not edit."""

TOKENS = {
    "color": {
        "white": '#ffffff',
        "ink": {
            "hi": '#1c2436',
            "mid": '#59627a',
            "low": '#8d95a8',
            "faint": '#aab1c2',
        },
        "accent": {
            "base": '#5e9eff',
            "hover": '#4a8df2',
            "active": '#3d7ce0',
            "subtle_a": 'rgba(94, 158, 255, 0.22)',
            "subtle_b": 'rgba(94, 158, 255, 0.12)',
            "ring": 'rgba(94, 158, 255, 0.16)',
            "on": '#ffffff',
        },
        "danger": {
            "base": '#e8382d',
            "hover": '#c22b21',
            "soft": '#ef5a76',
        },
        "success": '#34c759',
        "warning": '#ff9f0a',
        "violet": '#a78bfa',
        "pink": '#f2a2c6',
        "ppt": '#e8776f',
        "doc_blue": '#5f8af5',
        "surface": {
            "glass_window": 'rgba(247, 249, 253, 0.68)',
            "glass_chip": 'rgba(255, 255, 255, 0.45)',
            "content": 'rgba(255, 255, 255, 0.87)',
            "card": 'rgba(255, 255, 255, 0.72)',
            "menu": 'rgba(246, 246, 250, 0.88)',
            "hover": 'rgba(0, 0, 0, 0.05)',
            "active": 'rgba(0, 0, 0, 0.09)',
            "selected_on_accent": 'rgba(255, 255, 255, 0.94)',
        },
        "dark": {
            "player_bg": 'rgba(24, 28, 42, 0.74)',
            "player_ink": '#eef0f7',
            "player_ink_dim": 'rgba(238, 240, 247, 0.45)',
        },
        "stroke": {
            "light": 'rgba(255, 255, 255, 0.55)',
            "dark": 'rgba(20, 30, 60, 0.08)',
            "softer": 'rgba(20, 30, 60, 0.05)',
            "menu": 'rgba(0, 0, 0, 0.09)',
            "input": 'rgba(20, 30, 60, 0.14)',
        },
        "wallpaper": {
            "fallback_1": '#dbe7ff',
            "fallback_2": '#ffe3f0',
            "fallback_3": '#ded4ff',
            "fallback_4": '#d3ecf5',
        },
    },
    "size": {
        "radius": {
            "xs": '4px',
            "sm": '6px',
            "md": '8px',
            "lg": '12px',
            "xl": '16px',
            "window": '12px',
            "menu_item": '4px',
            "pill": '999px',
        },
        "space": {
            "1": '2px',
            "2": '4px',
            "3": '6px',
            "4": '8px',
            "5": '10px',
            "6": '12px',
            "7": '14px',
            "8": '16px',
            "10": '20px',
            "12": '24px',
            "16": '32px',
            "20": '40px',
        },
        "control": {
            "h_sm": '26px',
            "h_md": '30px',
            "h_lg": '36px',
        },
        "icon": {
            "sm": '13px',
            "md": '15px',
            "lg": '17px',
        },
        "border": {
            "hairline": '1px',
            "focus_ring": '3px',
        },
    },
    "font": {
        "family_ui": "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'SF Pro Display', 'Segoe UI Variable Display', 'Segoe UI', system-ui, sans-serif",
        "family_mono": "ui-monospace, 'SF Mono', 'Cascadia Code', Menlo, Consolas, monospace",
        "size": {
            "2xs": '10px',
            "xs": '11px',
            "sm": '12px',
            "md": '12.5px',
            "base": '13px',
            "lg": '15px',
            "xl": '17px',
            "2xl": '20px',
            "3xl": '24px',
            "4xl": '32px',
        },
        "weight": {
            "regular": '400',
            "medium": '500',
            "semibold": '600',
            "demibold": '550',
            "bold": '700',
        },
        "family_alt": {
            "inter": "'Inter', var(--cat-font-family-ui)",
            "grotesk": "'Space Grotesk', var(--cat-font-family-ui)",
            "serif_text": "'Source Serif 4', Georgia, serif",
        },
    },
    "elevation": {
        "window": '0 18px 60px rgba(0, 0, 0, 0.26), 0 6px 18px rgba(0, 0, 0, 0.12)',
        "float": '0 16px 44px rgba(10, 12, 24, 0.30), 0 4px 12px rgba(10, 12, 24, 0.14)',
        "menu": '0 14px 40px rgba(0, 0, 0, 0.22), 0 2px 8px rgba(0, 0, 0, 0.10)',
        "panel": '0 6px 24px rgba(25, 35, 65, 0.08)',
        "chip_hover": 'inset 0 1px 0 rgba(255, 255, 255, 0.65)',
        "raised": '0 1px 2px rgba(0, 0, 0, 0.14)',
    },
    "blur": {
        "window": '46px',
        "float": '34px',
        "chip": '22px',
        "saturate_window": '1.7',
        "saturate_float": '1.6',
        "saturate_chip": '1.5',
    },
    "motion": {
        "fast": '120ms',
        "med": '180ms',
        "slow": '260ms',
        "ease_out": 'cubic-bezier(0.2, 0.7, 0.3, 1)',
        "spring": 'cubic-bezier(0.25, 0.8, 0.3, 1.2)',
    },
    "depth": {
        "z": {
            "wallpaper": '0',
            "desktop": '10',
            "window": '20',
            "toolbar": '30',
            "dropdown": '40',
            "float": '50',
            "toast": '60',
        },
        "opacity": {
            "chrome": '1',
            "content": '0.87',
            "note": 'Content is MORE opaque than chrome (spec 21): legibility > transparency',
        },
    },
    "semantic": {
        "accent_dynamic": '#5e9eff',
        "accent_ring": 'rgba(94, 158, 255, 0.16)',
        "sel_a": 'rgba(94, 158, 255, 0.22)',
        "sel_b": 'rgba(94, 158, 255, 0.12)',
        "wall_hue_1": '220',
        "wall_hue_2": '330',
        "hue_shift": '0deg',
        "wall_bright": '1',
        "glass_window": 'rgba(247, 249, 253, 0.68)',
        "slider_track": 'rgba(0, 0, 0, 0.14)',
        "chip_a": 'rgba(255, 255, 255, 0.55)',
        "chip_b": 'rgba(255, 255, 255, 0.55)',
        "chip_hover_a": 'rgba(255, 255, 255, 0.75)',
        "chip_hover_b": 'rgba(255, 255, 255, 0.75)',
        "tab_a": 'rgba(255, 255, 255, 0.78)',
        "tab_b": 'rgba(255, 255, 255, 0.78)',
        "seg_checked": '#ffffff',
        "input_a": 'rgba(255, 255, 255, 0.50)',
        "input_b": 'rgba(255, 255, 255, 0.50)',
        "input_focus_a": '#ffffff',
        "input_focus_b": '#ffffff',
        "statusbar_bg": 'rgba(255, 255, 255, 0.50)',
        "sidebar_bg": 'rgba(250, 250, 253, 0.45)',
        "panel_tint": 'rgba(255, 255, 255, 0.35)',
        "float_a": 'rgba(252, 253, 255, 0.74)',
        "float_b": 'rgba(252, 253, 255, 0.74)',
        "dropzone_bg": 'rgba(255, 255, 255, 0.25)',
        "toolbar_bg": 'rgba(120, 150, 255, 0.10)',
        "accent_hover_solid": '#4a8df2',
        "accent_active_solid": '#3d7ce0',
        "row_height": '38px',
    },
}

QSS_FILE = __file__.replace('theme.py', 'catalinas.qss')

def get(path, default=None):
    """TOKENS.get("color.accent.base") -> value"""
    cur = TOKENS
    for part in path.split('.'):
        if not isinstance(cur, dict) or part not in cur:
            return default
        cur = cur[part]
    return cur

def load_qss(app):
    """app.setStyleSheet(open(QSS_FILE).read()) helper"""
    from pathlib import Path
    app.setStyleSheet(Path(QSS_FILE).read_text())
