#!/usr/bin/env python3
"""Agrega generador Vue 3 a build.py (inserta antes de Flutter)."""
import pathlib

b = pathlib.Path("build/build.py")
s = b.read_text()

if "Vue 3 adapter" in s:
    print("ya existe"); raise SystemExit

anchor = "# ---------- Flutter theme ----------"

VUE_HEADER = (
    "/* Catalinas Design System - Vue 3 bindings (generated)\n"
    "   Requiere Vue 3 global. Uso:\n"
    "   Object.assign(app.components, CatalinasVue) */\n\n")

VUE_CODE = {
    "button":
        "export const CatButton = (props, ctx) => h('button', {\n"
        "  class: ['cat-btn', props.variant, props.size !== 'md' ? props.size : null,\n"
        "          props.loading ? 'loading' : null],\n"
        "  disabled: props.disabled,\n"
        "  onClick: () => ctx.emit('click')\n"
        "}, [props.icon, ctx.slots.default ? ctx.slots.default() : null]);",
    "switch":
        "export const CatSwitch = (props, ctx) => h('label', { class: 'cat-switch' }, [\n"
        "  h('input', { type: 'checkbox', checked: props.checked, disabled: props.disabled,\n"
        "    onChange: e => ctx.emit('change', e.target.checked) }),\n"
        "  h('span', { class: 'track' })\n"
        "]);",
    "badge-tooltip-kbd-avatar": [
        "export const CatBadge = (props) => h('span', { class: 'cat-badge' + (props.tone ? ' ' + props.tone : '') },\n"
        "  [props.dot ? h('span', { class: 'dot' }) : null], props.default);",
        "export const CatAvatar = (props) => h('span', { class: 'cat-avatar' },\n"
        "  props.src ? h('img', { src: props.src }) : props.initials,\n"
        "  props.online ? h('span', { class: 'presence' }) : null);",
    ],
    "card-toast": [
        "export const CatCard = (props) => h('div', { class: 'cat-card ' + (props.level || '') }, props.default);",
        "export const CatToast = (props, ctx) => h('div', { class: 'cat-toast ' + (props.tone === 'info' ? '' : props.tone) }, [\n"
        "  h('span', { class: 't-icon' }),\n"
        "  h('div', { style: 'flex:1' }, [h('b', props.title)]),\n"
        "  h('button', { class: 't-close', onClick: () => ctx.emit('close') }, 'x')\n"
        "]);",
    ],
}

vue = (
    "# ---------- Vue 3 adapter ----------\n"
    "VUE_HEADER = '''" + VUE_HEADER.replace("'''", "") + "'''\n\n"
    "VUE = {\n"
)
for k, v in VUE_CODE.items():
    items = v if isinstance(v, list) else [v]
    vue += f"    '{k}': [\n"
    for it in items:
        esc = it.replace("'''", "")
        vue += "        '''" + esc + "''',\n"
    vue += "    ],\n"
vue += "}\n\n"
vue += (
    "vue_parts = [VUE_HEADER]\n"
    "for sp in specs:\n"
    "    code = VUE.get(sp['name'])\n"
    "    if not code: continue\n"
    "    items = code if isinstance(code, list) else [code]\n"
    "    vue_parts.append('// ' + sp['name'] + '\\n\\n' + '\\n\\n'.join(items))\n"
    "(ROOT / 'web' / 'catalinas-vue.js').write_text('\\n\\n'.join(vue_parts) + '\\n')\n"
    "written.append('web/catalinas-vue.js')\n\n")

s = s.replace(anchor, vue + anchor, 1)
s = s.replace('"snippets", "api", "rtl"]', '"snippets", "api", "rtl", "vue"]')
b.write_text(s)
print("vue generator insertado")
