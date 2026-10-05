#!/usr/bin/env python3
"""Render index.html from manifest.json. Videos are NOT in this repo; each clip's `src` is a hosted URL."""
import json,html
m=json.load(open('manifest.json'))
cards=[]
for c in m['clips']:
    if c.get('hold'): continue
    src=c['src'] or ''
    player=(f'<video controls preload="none" poster="posters/{c["id"]}.jpg" src="{html.escape(src)}"></video>' if src
            else f'<img src="posters/{c["id"]}.jpg" alt="{html.escape(c["title"])}"><div class="soon">video not yet hosted</div>')
    cards.append(f'''<article class="card"><div class="frame">{player}</div>
<h3>{html.escape(c["title"])}</h3>
<p class="meta">{html.escape(c["brand"])} · {c["date"]} · {c["dur"]}s · made with {html.escape(c["tool"])}</p>
<p>{html.escape(c["note"])}</p></article>''')
yt=''.join(f'<li>{html.escape(y["title"])} <span class="v">{y["views"]} views</span></li>' for y in m['youtube'])
open('index.html','w').write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(m["title"])} · GRYHAT</title>
<style>
:root{{--bg:#0b0f14;--card:#121923;--ink:#e6edf3;--mut:#8b98a5;--acc:#39c6ff}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 -apple-system,Inter,sans-serif}}
header{{padding:48px 24px 16px;max-width:1100px;margin:auto}}h1{{font-size:40px;margin:0 0 8px}}header p{{color:var(--mut);max-width:720px}}
.badge{{display:inline-block;border:1px solid var(--acc);color:var(--acc);border-radius:999px;padding:2px 10px;font-size:12px;letter-spacing:.08em;text-transform:uppercase}}
main{{max-width:1100px;margin:auto;padding:16px 24px 64px;display:grid;gap:24px;grid-template-columns:repeat(auto-fill,minmax(320px,1fr))}}
.card{{background:var(--card);border-radius:12px;overflow:hidden}}.frame{{position:relative;background:#000;aspect-ratio:16/9;display:flex;align-items:center;justify-content:center}}
.frame video,.frame img{{width:100%;height:100%;object-fit:contain}}.soon{{position:absolute;bottom:8px;right:8px;font-size:11px;color:var(--mut);background:#0008;padding:2px 6px;border-radius:4px}}
h3{{margin:12px 16px 2px;font-size:17px}}.meta{{margin:0 16px;color:var(--acc);font-size:13px}}.card p{{margin:6px 16px 16px;color:var(--mut);font-size:14px}}
section{{max-width:1100px;margin:auto;padding:0 24px 48px}}ul{{columns:2;gap:24px}}li{{margin:4px 0}}.v{{color:var(--mut);font-size:13px}}
footer{{text-align:center;color:var(--mut);padding:32px;font-size:13px}}a{{color:var(--acc)}}
</style></head><body>
<header><span class="badge">All AI-generated</span><h1>{html.escape(m["title"])}</h1><p>{html.escape(m["intro"])}</p></header>
<main>{''.join(cards)}</main>
<section><h2>Already on YouTube</h2><p style="color:var(--mut)">On <a href="https://www.youtube.com/@TheCitadelCyber">@TheCitadelCyber</a>.</p><ul>{yt}</ul></section>
<footer>GRYHAT Cybersecurity · Orange County, California · <a href="https://github.com/TheGRYHAT/iaigacb-framework">IAiGACB</a> · <a href="https://gryhat.com">gryhat.com</a></footer>
</body></html>''')
print("index.html rendered")
