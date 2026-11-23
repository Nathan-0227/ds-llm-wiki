#!/usr/bin/env python3
"""簡報 Graph 的程式關卡。
用法：
  python3 scripts/graph_gates.py retrieve   # 節點1 檢索 wiki → topic-diffusion/sources.md
  python3 scripts/graph_gates.py coverage   # 關卡A 覆蓋率
  python3 scripts/graph_gates.py cards      # 節點2 產生證據卡（程式直接抽句，不經 AI）
  python3 scripts/graph_gates.py outline    # 關卡B 大綱檢查
  python3 scripts/graph_gates.py drafts     # 關卡C 逐頁稿出處／數字檢查
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
TOPIC = ROOT / "topic-graph"
PAGES = {p.stem: p for p in (WIKI / "concepts").glob("*.md")}
CITE = re.compile(r"\[((?:G\d|C\d+E?) p\.\d+(?:-\d+)?)\]")
NUM = re.compile(r"\d+(?:\.\d+)?")

# 零基礎讀者「一定要學到」的子題 → 需要哪個 wiki 頁（需求摘要第 1 點）
REQUIRED = {
    "圖的定義": "graph-basics", "表示法": "graph-representation", "stack/queue": "stack-and-queue",
    "DFS": "dfs", "DFS 實作": "dfs-nonrecursive", "BFS": "bfs", "BFS 實作": "bfs-queue",
    "範例圖": "example-graph-g", "複雜度": "big-o", "應用": "dfs-applications", "應用2": "bfs-applications",
}

def fail(msgs):
    print(f"❌ {len(msgs)} 個問題"); print("\n".join(msgs)); sys.exit(1)

def retrieve():
    TOPIC.mkdir(exist_ok=True)
    rows = ["# 節點1 檢索結果：與「Graph 與 BFS/DFS」相關的 wiki 頁", ""]
    for stem, p in sorted(PAGES.items()):
        t = p.read_text(encoding="utf-8")
        srcs = sorted(set(c.split()[0] for c in CITE.findall(t)))
        rows.append(f"- {stem}：{len(t.splitlines())} 行，來源 {', '.join(srcs)}")
    (TOPIC / "sources.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print("\n".join(rows))

def coverage():
    errs = [f"子題「{k}」缺 wiki 頁 {v}" for k, v in REQUIRED.items() if v not in PAGES]
    if len(PAGES) < 3:
        errs.append("相關頁少於 3 頁 → 停下，回去 ingest 更多資料")
    if errs: fail(errs)
    print(f"✅ 覆蓋率：{len(REQUIRED)} 個必學子題都有 wiki 頁（共 {len(PAGES)} 頁）")

def cards():
    d = TOPIC / "cards"; d.mkdir(parents=True, exist_ok=True)
    for stem, p in PAGES.items():
        facts = [l.strip() for l in p.read_text(encoding="utf-8").splitlines()
                 if CITE.search(l) and not l.strip().startswith("#")]
        (d / f"{stem}.md").write_text(f"# 證據卡：{stem}\n\n" + "\n".join(facts) + "\n", encoding="utf-8")
        print(f"cards/{stem}.md：{len(facts)} 句")

def parse_slides(path):
    slides, cur = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            cur = {"title": line[3:].strip(), "cards": [], "lines": []}; slides.append(cur)
        elif cur is not None and line.startswith("cards:"):
            cur["cards"] = [c.strip() for c in line[6:].split(",") if c.strip()]
        elif cur is not None and line.strip():
            cur["lines"].append(line.strip())
    return slides

def outline():
    slides = parse_slides(TOPIC / "outline.md"); errs = []
    if not 8 <= len(slides) <= 16: errs.append(f"頁數 {len(slides)} 不在 8–16")
    used = set()
    for i, s in enumerate(slides, 1):
        for c in s["cards"]:
            if c not in PAGES: errs.append(f"第{i}頁 引用不存在的卡 {c}")
            used.add(c)
    for k, v in REQUIRED.items():
        if v not in used: errs.append(f"必學子題「{k}」({v}) 沒有出現在任何一頁")
    if errs: fail(errs)
    print(f"✅ 大綱：{len(slides)} 頁，必學子題全覆蓋")

def drafts():
    slides = parse_slides(TOPIC / "drafts" / "slides.md"); errs = []
    card_text = {p.stem: p.read_text(encoding="utf-8") for p in (TOPIC / "cards").glob("*.md")}
    TAG = re.compile(r"\{([a-z\-]+)\}")
    SRCID = re.compile(r"\b(?:G\d|C\d+E?)\b")
    for i, s in enumerate(slides, 1):
        for line in s["lines"]:
            if line.startswith(("note:", "visual:", "quiz-answer:", "anim:", "photo:")) and "{" not in line:
                continue
            tags = TAG.findall(line)
            if not tags and s["cards"]:
                errs.append(f"第{i}頁 這行沒標來自哪張卡：{line[:35]}"); continue
            for t in tags:
                if t not in s["cards"]:
                    errs.append(f"第{i}頁 用了大綱沒分配給這頁的卡 {t}")
            src = "".join(card_text.get(t, "") for t in tags)
            body = SRCID.sub("", TAG.sub("", CITE.sub("", line)))
            for n in NUM.findall(body):
                if n not in src:
                    errs.append(f"第{i}頁 數字 {n} 在卡 {tags} 找不到")
            for sid in CITE.findall(line):
                if f"[{sid}]" not in src:
                    errs.append(f"第{i}頁 出處 {sid} 不在卡 {tags} 裡")
            if len(body) > 70:
                errs.append(f"第{i}頁 單行 {len(body)} 字，超過 70 字：{body[:25]}…")
        for line in s["lines"]:
            if line.startswith("photo:"):
                for ref in line[6:].split(","):
                    ok = False
                    sid, pg = ref.strip().split(" p.")
                    for t in s["cards"]:
                        for c in CITE.findall(card_text.get(t, "")):
                            cs, rng = c.split(" p."); a, _, b = rng.partition("-")
                            if cs == sid and int(a) <= int(pg) <= int(b or a): ok = True
                    if not ok: errs.append(f"第{i}頁 圖片 {ref.strip()} 不在本頁證據卡引用的頁碼範圍（AGENTS.md 第 11 節）")
        if len([l for l in s["lines"] if not l.startswith("photo:")]) > 7:
            errs.append(f"第{i}頁 {len(s['lines'])} 行，超過 7 行")
    if errs: fail(errs)
    print(f"✅ 逐頁稿：{len(slides)} 頁，出處、數字、長度全過")

{"retrieve": retrieve, "coverage": coverage, "cards": cards,
 "outline": outline, "drafts": drafts}[sys.argv[1]]()
