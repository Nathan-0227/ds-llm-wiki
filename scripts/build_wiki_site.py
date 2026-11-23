#!/usr/bin/env python3
"""把 wiki/ raw/ checks/ 等 markdown 打包成一個可瀏覽的 HTML（hash 路由：#forward-process）。"""
import re, json, pathlib, html, markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "wiki.html"

def page(pid, title, path, group):
    return {"id": pid, "title": title, "group": group, "path": str(path.relative_to(ROOT)), "md": path.read_text(encoding="utf-8")}

pages = [page("index", "Index", ROOT / "wiki/index.md", "首頁")]
for p in sorted((ROOT / "wiki/concepts").glob("*.md")):
    pages.append(page(p.stem, p.read_text(encoding="utf-8").splitlines()[0].lstrip("# "), p, "概念頁"))
ORDER = ["G1","G2","C3","C4","C5","C1","C2","C7","C7E","C8","C10","C11"]
for p in sorted((ROOT / "wiki/sources").glob("*.md"), key=lambda x: ORDER.index(x.stem)):
    t = [l for l in p.read_text(encoding="utf-8").splitlines() if l.startswith("# ")][0]
    pages.append(page(p.stem, t[2:], p, "來源頁"))
for sid in ORDER:
    p = ROOT / "raw/text" / f"{sid}.txt"
    d = page("raw-" + sid, f"raw/text/{sid}.txt", p, "原始講義文字"); d["md"] = "```\n" + d["md"] + "\n```"; pages.append(d)
pages += [
    page("interview", "需求訪談紀錄（先討論）", ROOT / "00-需求訪談紀錄.md", "過程紀錄"),
    page("agents", "AGENTS.md 員工手冊", ROOT / "AGENTS.md", "過程紀錄"),
    page("log", "wiki/log.md", ROOT / "wiki/log.md", "過程紀錄"),
]
for i, p in enumerate(sorted((ROOT / "checks").glob("*.md")), 1):
    pages.append(page(f"check-{i}", p.stem, p, "過程紀錄"))

ids = {p["id"] for p in pages}
for p in pages:
    md = re.sub(r"^---\n.*?\n---\n", lambda m: "```\n" + m.group(0).strip("-\n") + "\n```\n", p["md"], flags=re.S)
    md = re.sub(r"\[\[([^\]]+)\]\]", lambda m: f'<a class="wl" href="#{m.group(1)}">{m.group(1)}</a>' if m.group(1) in ids else m.group(0), md)
    md = re.sub(r"\[((G\d|C\d+E?) p\.\d+(?:-\d+)?)\]", lambda m: f'<a class="cite" href="#raw-{m.group(2)}">{m.group(1)}</a>', md)
    p["html"] = markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists"])
    del p["md"]

tpl = (ROOT / "scripts/wiki_template.html").read_text(encoding="utf-8")
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(tpl.replace("/*PAGES*/[]", json.dumps(pages, ensure_ascii=False)), encoding="utf-8")
print(f"{OUT.relative_to(ROOT)}：{len(pages)} 頁，{OUT.stat().st_size//1024} KB")
