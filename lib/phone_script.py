"""Turn a task's SCRIPT.md into a phone-sized PDF, one card per beat.

SCRIPT.md needs "## Intro", "## After you stop" and "## Numbers to expect" sections. Rows are
"| time | do | say |" tables; a row whose Do mentions CHECK becomes an orange card, and a line
starting with ⏱ becomes a purple pace card.
"""
import html
import re

STYLE = """
@page { size: 100mm 500mm; margin: 6mm; }
body { font-family: Helvetica, Arial, sans-serif; font-size: 11.5pt; color: #111; line-height: 1.35; }
h1 { font-size: 15pt; margin: 0 0 2mm; }
.sub { font-size: 9.5pt; color: #555; margin-bottom: 4mm; }
h2 { font-size: 12.5pt; background: #222; color: #fff; padding: 1.5mm 2.5mm; border-radius: 2mm; margin: 5mm 0 2mm; }
.beat { border-left: 1.2mm solid #2a6fdb; padding: 1mm 0 1.5mm 2.5mm; margin: 0 0 2.5mm; break-inside: avoid; }
.check { border-left-color: #d98a00; background: #fff6e0; }
.pace { border: 0.4mm solid #7a3fd1; background: #f3ecff; border-radius: 1.5mm; padding: 1.5mm 2.5mm; margin: 0 0 3mm; font-size: 10.5pt; }
.t { font-weight: bold; color: #2a6fdb; font-size: 10.5pt; }
.do span, .say span { display: inline-block; font-size: 7.5pt; font-weight: bold; color: #fff;
  border-radius: 1mm; padding: 0 1.2mm; margin-right: 1mm; vertical-align: 1px; }
.do span { background: #2a6fdb; } .say span { background: #1a8a4a; }
.say { margin-top: 1mm; }
code { font-family: Menlo, monospace; font-size: 9.5pt; background: #eef; padding: 0 0.6mm; border-radius: 0.8mm; }
table { border-collapse: collapse; font-size: 9pt; width: 100%; } td { border: 0.2mm solid #bbb; padding: 0.8mm 1.2mm; }
ul { padding-left: 4mm; font-size: 9.5pt; }
"""


def inline(text):
    # Odd pieces are code spans; keep their * (formulas like =B8*C8) out of the bold/italic rules.
    out = []
    for i, piece in enumerate(html.escape(text.strip()).split("`")):
        if i % 2:
            out.append(f"<code>{piece}</code>")
        else:
            piece = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", piece)
            out.append(re.sub(r"\*([^*]+)\*", r"<i>\1</i>", piece))
    return "".join(out)


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split(" | ")]


def build(script):
    title = script.splitlines()[0].lstrip("# ").split(":")[0]
    beats = script[script.index("## Intro"):script.index("## After you stop")]
    numbers = script[script.index("## Numbers to expect"):]

    out = []
    lines = beats.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("⏱"):
            paragraph = [line]
            for more in lines[i + 1:]:
                if not more.strip():
                    break
                paragraph.append(more)
            out.append(f'<div class="pace">{inline(" ".join(paragraph))}</div>')
        elif line.startswith("## "):
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("| ") and not line.startswith(("| Time", "|---")):
            time, do, *say = cells(line)
            kind = "beat check" if "CHECK" in do else "beat"
            out.append(f'<div class="{kind}"><div class="t">{inline(time)}</div>'
                       f'<div class="do"><span>DO</span> {inline(do)}</div>'
                       f'<div class="say"><span>SAY</span> {inline(" | ".join(say))}</div></div>')

    rows = [r for r in numbers.splitlines() if r.startswith("| ") and not r.startswith("|---")]
    table = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r.strip().strip("|").split("|"))
                    + "</tr>" for r in rows)
    bullets = "".join(f"<li>{inline(l[2:])}</li>" for l in numbers.splitlines() if l.startswith("- "))
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
            f"<style>{STYLE}</style></head><body><h1>{inline(title)}</h1>"
            '<div class="sub">Slower is fine (limit 50:59), but never skip a step. Orange cards are '
            "checks: if a number is off, press Command + Z and redo. Pause about 1 s after each click. "
            "Purple cards are pace checks against the clock. Never go silent for more than 45 s.</div>"
            + "".join(out) + f"<h2>Numbers to expect</h2><table>{table}</table><ul>{bullets}</ul></body></html>")
