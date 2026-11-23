#!/usr/bin/env python3
"""渲染節點：把通過關卡的 drafts/slides.md 機械式轉成 HTML（不改任何字）。
動畫步驟由程式依 G2 演算法產生，產生後先和講義順序比對，不一致就不輸出。"""
import re, json, html, sys, pathlib
from collections import deque

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = "https://claude.ai/artifact/YJhPEsseFaV1SrGyVWcrSU"
CITE = re.compile(r"\[((?:G\d|C\d+E?) p\.\d+(?:-\d+)?)\]")
TAG = re.compile(r"\{([a-z\-]+)\}")

# ---------- 讀稿 ----------
slides, cur = [], None
for line in (ROOT / "topic-graph/drafts/slides.md").read_text(encoding="utf-8").splitlines():
    if line.startswith("## "):
        cur = {"title": line[3:].strip(), "cards": [], "lines": [], "visual": None, "anim": None, "photo": []}; slides.append(cur)
    elif cur is None: continue
    elif line.startswith("cards:"): cur["cards"] = [c.strip() for c in line[6:].split(",") if c.strip()]
    elif line.startswith("visual:"): cur["visual"] = line[7:].strip()
    elif line.startswith("anim:"): cur["anim"] = line[5:].strip()
    elif line.startswith("photo:"): cur["photo"] = [x.strip() for x in line[6:].split(",")]
    elif line.strip(): cur["lines"].append(line.strip())

def esc(s): return html.escape(s, quote=False)
def render_line(s):
    cites = CITE.findall(s); tags = TAG.findall(s)
    body = esc(TAG.sub("", CITE.sub("", s)).strip())
    chips = "".join(f'<a class="cite" href="{WIKI}#raw-{c.split()[0]}" target="_blank" rel="noopener">{c}</a>' for c in cites)
    return body, chips, tags

# ---------- 動畫步驟（與 scripts/check_traversal.py 同一演算法）----------
EDGES = [("v1","v2"),("v2","v3"),("v2","v4"),("v3","v4"),("v3","v5"),("v4","v5")]
ADJ = {}
for a, b in EDGES: ADJ.setdefault(a, []).append(b); ADJ.setdefault(b, []).append(a)
for k in ADJ: ADJ[k].sort()

def dfs_steps(v):
    s, seen = [v], [v]; steps = [{"act": f"push {v}，標記 visited", "ds": [v], "seen": [v], "cur": v}]
    while s:
        x = s[-1]; nxt = [u for u in ADJ[x] if u not in seen]
        if not nxt:
            s.pop(); steps.append({"act": f"{x} 沒有未拜訪的鄰居 → pop（backtrack）", "ds": list(s), "seen": list(seen), "cur": s[-1] if s else None})
        else:
            u = nxt[0]; s.append(u); seen.append(u)
            steps.append({"act": f"{x} 的未拜訪鄰居裡選 {u} → push {u}", "ds": list(s), "seen": list(seen), "cur": u, "edge": [x, u]})
    return steps

def bfs_steps(v):
    q, seen = deque([v]), [v]; steps = [{"act": f"enqueue {v}，標記 visited", "ds": [v], "seen": list(seen), "cur": v}]
    while q:
        w = q.popleft(); steps.append({"act": f"dequeue {w}，檢查它的鄰居", "ds": list(q), "seen": list(seen), "cur": w})
        for u in ADJ[w]:
            if u not in seen:
                q.append(u); seen.append(u)
                steps.append({"act": f"{u} 還沒拜訪 → enqueue {u}", "ds": list(q), "seen": list(seen), "cur": w, "edge": [w, u]})
    return steps

def order_key(steps):
    first = []
    for st in steps:
        for x in st["seen"]:
            if x not in first: first.append(x)
    return lambda x: first.index(x) if x in first else 99

D, B = dfs_steps("v3"), bfs_steps("v5")
if D[-1]["seen"] != ["v3","v2","v1","v4","v5"] or B[-1]["seen"] != ["v5","v3","v4","v2","v1"]:
    sys.exit("❌ 動畫順序與講義（G2 p.4、p.7）不一致，停止渲染")

def code_block(page):
    t = (ROOT / f"wiki/concepts/{page}.md").read_text(encoding="utf-8")
    return re.search(r"```\n(.*?)```", t, re.S).group(1).rstrip()

ANIM = {"dfs": {"steps": D, "ds": "Stack（頂端在右）", "code": code_block("dfs-nonrecursive"), "src": "G2 p.3"},
        "bfs": {"steps": B, "ds": "Queue（front → back）", "code": code_block("bfs-queue"), "src": "G2 p.6"}}

# ---------- 視覺 ----------
POS = {"v1": (60, 90), "v2": (190, 70), "v3": (320, 85), "v4": (140, 200), "v5": (310, 215)}
def graph_svg(edges, pos, cls="g"):
    e = "".join(f'<line data-e="{a}-{b}" x1="{pos[a][0]}" y1="{pos[a][1]}" x2="{pos[b][0]}" y2="{pos[b][1]}"/>' for a, b in edges)
    n = "".join(f'<g data-n="{k}" transform="translate({x},{y})"><circle r="24"/><text dy="6">{k}</text></g>' for k, (x, y) in pos.items())
    return f'<svg class="{cls}" viewBox="0 0 380 280" role="img" aria-label="graph">{e}{n}</svg>'

E16 = [("1","3"),("2","4"),("3","4"),("2","3")]
P16 = {"1": (70, 140), "2": (300, 60), "3": (190, 150), "4": (300, 230)}
VISUAL = {}
VISUAL["graph-example"] = graph_svg(E16, P16) + '<p class="cap">G1 p.16 的例子：V = {1,2,3,4}</p>'
mat = "".join("<tr><th>%s</th>%s</tr>" % (i, "".join(f"<td class={'one' if (str(i),str(j)) in E16 or (str(j),str(i)) in E16 else 'zero'}>{1 if (str(i),str(j)) in E16 or (str(j),str(i)) in E16 else 0}</td>" for j in range(1,5))) for i in range(1,5))
lst = "".join(f"<div class='row'><b>{v}</b>" + "".join(f"<span>{u}</span>" for u in sorted([b for a,b in E16 if a==v]+[a for a,b in E16 if b==v])) + "</div>" for v in "1234")
VISUAL["representation"] = f'<div class="rep"><div><h4>Adjacency matrix</h4><table class="mat"><tr><th></th><th>1</th><th>2</th><th>3</th><th>4</th></tr>{mat}</table></div><div><h4>Adjacency list</h4><div class="lst">{lst}</div></div></div><p class="cap">由 G1 p.16 的邊集合產生</p>'
VISUAL["stack-queue"] = '<div class="sq"><div><h4>Stack · LIFO</h4><div class="stack"><span>C</span><span>B</span><span>A</span></div><p>push／pop 都在頂端</p></div><div><h4>Queue · FIFO</h4><div class="queue"><em>front</em><span>A</span><span>B</span><span>C</span><em>rear</em></div><p>rear 進、front 出</p></div></div>'
VISUAL["compare-table"] = '<div class="cmp"><div class="dfs"><h4>DFS</h4><p>stack</p><p>往深處</p></div><div class="bfs"><h4>BFS</h4><p>queue</p><p>往廣處</p></div></div>'

def mapping_table():
    rows = []
    for i, s in enumerate(slides, 1):
        if not s["cards"]: continue
        cites = sorted({c for l in s["lines"] for c in CITE.findall(l)})
        links = "、".join(f'<a href="{WIKI}#{c}" target="_blank" rel="noopener">{c}</a>' for c in s["cards"])
        rows.append(f"<tr><td>{i}</td><td>{esc(s['title'])}</td><td>{links}</td><td>{'、'.join(cites)}</td></tr>")
    return f'<div class="map"><table><tr><th>頁</th><th>投影片</th><th>Wiki 頁</th><th>講義頁碼</th></tr>{"".join(rows)}</table></div>'

import base64
def photo_html(refs):
    figs = []
    for r in refs:
        sid, pg = r.split(" p.")
        f = ROOT / f"topic-graph/img/{sid}-p{pg}.jpg"
        b64 = base64.b64encode(f.read_bytes()).decode()
        figs.append(f'<figure><img src="data:image/jpeg;base64,{b64}" alt="講義 {r} 的投影片"><figcaption>講義 {r}</figcaption></figure>')
    return f'<div class="ph n{len(refs)}">{"".join(figs)}</div>'

def theme(title):
    if "BFS" in title and "DFS" in title: return "both"
    if "DFS" in title: return "dfs"
    if "BFS" in title: return "bfs"
    return ""

# ---------- 組頁 ----------
out = []
for i, s in enumerate(slides, 1):
    kind = "cover" if i == 1 else ("anim" if s["anim"] else ("wide" if s["visual"] == "mapping-table" else ("vis" if (s["visual"] or s["photo"]) else "text")))
    items, quiz = [], []
    for l in s["lines"]:
        body, chips, _ = render_line(l)
        if l.startswith("quiz-answer:"):
            quiz[-1] += f'<button class="reveal" aria-expanded="false">看答案</button><span class="ans" hidden>{esc(body[12:].strip())} {chips}</span></li>'
        elif l.startswith("Q"):
            quiz.append(f"<li><b>{body}</b>")
        else:
            cls = " class=warn" if body.startswith("⚠") else ""
            items.append(f"<li{cls}>{body} {chips}</li>")
    content = ""
    if kind == "cover":
        content = f'<div class="cover"><div class="ctext"><div class="lines"><i></i><i></i><i></i></div><h1>{esc(s["title"])}</h1>' + "".join(f"<p>{esc(l)}</p>" for l in s["lines"]) + f'<p class="hint">按 → 或點右下角開始　·　Wiki：<a href="{WIKI}" target="_blank" rel="noopener">資料結構 LLM Wiki</a></p></div><div class="cart">{graph_svg(EDGES, POS, "g hero")}</div></div>'
    elif kind == "anim":
        a = s["anim"]
        content = f'''<h2>{esc(s["title"])}</h2><div class="animwrap" data-anim="{a}">
<div class="left">{graph_svg(EDGES, POS, "g big")}<div class="ctl"><button data-do="reset">重來</button><button data-do="prev">← 上一步</button><button data-do="next" class="pri">下一步 →</button><button data-do="play">自動播放</button></div></div>
<div class="right"><p class="act" aria-live="polite"></p><div class="ds"><h4>{ANIM[a]["ds"]}</h4><div class="cells"></div></div><div class="seen"><h4>拜訪順序</h4><div class="cells"></div></div>
<ul class="pts">{"".join(items)}</ul><details><summary>看虛擬碼（{ANIM[a]["src"]}，取自 wiki）</summary><pre>{esc(ANIM[a]["code"])}</pre></details></div></div>'''
    elif kind == "wide":
        content = f"<h2>{esc(s['title'])}</h2>" + mapping_table()
    else:
        vis = f'<div class="vis">{VISUAL[s["visual"]]}</div>' if s["visual"] else (photo_html(s["photo"]) if s["photo"] else "")
        qz = f'<ol class="quiz">{"".join(quiz)}</ol>' if quiz else ""
        two = "grid4" if len(s["photo"]) > 1 else ("two" if vis else "")
        content = f'<h2>{esc(s["title"])}</h2><div class="body {two}"><div><ul class="pts">{"".join(items)}</ul>{qz}</div>{vis}</div>'
    foot = "、".join(f'<a href="{WIKI}#{c}" target="_blank" rel="noopener">{c}</a>' for c in s["cards"])
    footer = f'<footer><span>Wiki：{foot}</span><span>{i} / {len(slides)}</span></footer>' if s["cards"] else f'<footer><span></span><span>{i} / {len(slides)}</span></footer>'
    out.append(f'<section class="slide {kind} {theme(s["title"])} {"photo" if s["photo"] else ""}" id="s{i}" aria-label="第 {i} 頁">{content}{footer}</section>')

tpl = (ROOT / "scripts/deck_template.html").read_text(encoding="utf-8")
page = tpl.replace("<!--SLIDES-->", "\n".join(out)).replace("/*ANIM*/{}", json.dumps({k: v["steps"] for k, v in ANIM.items()}, ensure_ascii=False))
(ROOT / "topic-graph/deck.html").write_text(page, encoding="utf-8")
print(f"✅ topic-graph/deck.html：{len(slides)} 頁；動畫 DFS {len(D)} 步、BFS {len(B)} 步（順序已與講義比對）")
