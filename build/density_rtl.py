#!/usr/bin/env python3
import json, pathlib

# 1) row height variable
p = pathlib.Path("spec/list-statusbar.json")
d = json.loads(p.read_text())
d["targets"]["web"]["css"] = [c.replace("height:38px", "height:var(--cat-size-row-h,38px)")
                              for c in d["targets"]["web"]["css"]]
p.write_text(json.dumps(d, ensure_ascii=False, indent=1))

# 2) density utilities + rtl emitter en build.py
b = pathlib.Path("build/build.py")
s = b.read_text()

anchor = 'util += ["@media (prefers-reduced-motion: reduce)'
add = '''util += [
 '[data-density="compact"]{--cat-size-control-h-sm:22px;--cat-size-control-h-md:26px;--cat-size-control-h-lg:30px;--cat-size-row-h:32px}',
 '[data-density="cozy"]{--cat-size-control-h-sm:24px;--cat-size-control-h-md:30px;--cat-size-control-h-lg:36px;--cat-size-row-h:38px}',
 '[data-density="comfortable"]{--cat-size-control-h-sm:28px;--cat-size-control-h-md:34px;--cat-size-control-h-lg:40px;--cat-size-row-h:44px}']

''' + anchor
assert anchor in s
s = s.replace(anchor, add, 1)

old_tail = '''print(f"catalinas build ok — {len(specs)} widgets, {len(FLAT)} tokens")
for w in written:
    print("  +", w)'''
new_tail = '''# ---------- RTL (experimental) ----------
if wants("rtl"):
    import re as _re
    css_src = (ROOT / "web" / "catalinas.css").read_text()
    def rtl_line(line):
        line = _re.sub(r"(padding-)left(:)", r"\\1TMPR\\2", line)
        line = _re.sub(r"(padding-)right(:)", r"\\1left\\2", line)
        line = _re.sub(r"(padding-)TMPR(:)", r"\\1right\\2", line)
        line = _re.sub(r"(margin-)left(:)", r"\\1TMPR\\2", line)
        line = _re.sub(r"(margin-)right(:)", r"\\1left\\2", line)
        line = _re.sub(r"(margin-)TMPR(:)", r"\\1right\\2", line)
        line = _re.sub(r"text-align:left", "text-align:TMPR", line)
        line = _re.sub(r"text-align:right", "text-align:left", line)
        line = _re.sub(r"text-align:TMPR", "text-align:right", line)
        line = _re.sub(r"([\\s;{])left:", r"\\1TMPR:", line)
        line = _re.sub(r"([\\s;{])right:", r"\\1left:", line)
        line = _re.sub(r"([\\s;{])TMPR:", r"\\1right:", line)
        line = _re.sub(r"border-top-left-radius", "BTLR", line)
        line = _re.sub(r"border-top-right-radius", "border-top-left-radius", line)
        line = _re.sub(r"BTLR", "border-top-right-radius", line)
        line = _re.sub(r"border-bottom-left-radius", "BBLR", line)
        line = _re.sub(r"border-bottom-right-radius", "border-bottom-left-radius", line)
        line = _re.sub(r"BBLR", "border-bottom-right-radius", line)
        return line
    body = "\\n".join(rtl_line(l) for l in css_src.splitlines())
    hdr = "/* Catalinas RTL (experimental) - flip direccional generado */"
    (ROOT / "web" / "catalinas.rtl.css").write_text(hdr + "\\n" + body + "\\n")
    written.append("web/catalinas.rtl.css")

print(f"catalinas build ok — {len(specs)} widgets, {len(FLAT)} tokens")
for w in written:
    print("  +", w)'''
assert old_tail in s
s = s.replace(old_tail, new_tail)
s = s.replace('"snippets", "api"]', '"snippets", "api", "rtl"]')
b.write_text(s)
print("build.py ok")
