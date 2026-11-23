#!/usr/bin/env python3
"""Wiki lint（AGENTS.md 第 8 節）。用法：python3 scripts/lint_wiki.py"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CITE = re.compile(r"\[((?:G\d|C\d+E?) p\.(\d+)(?:-(\d+))?)\]")
LINK = re.compile(r"\[\[([^\]]+)\]\]")
NUM = re.compile(r"\d+(?:\.\d+)?")
WORD = re.compile(r"[A-Za-z][A-Za-z\-]{2,}")
STOP = {"the", "and", "for", "with", "not", "are", "page", "wiki", "ingest"}
# 縮寫對照（G1 lint 第 1 輪誤判後加入）
ALIAS = {"dfs": "depth", "bfs": "breadth", "dag": "acyclic", "bst": "binary search tree", "adt": "abstract data type"}
SRCID = re.compile(r"\b(?:G\d|C\d+E?)(?: p\.\d+(?:-\d+)?)?\b")
INDEX = (ROOT / "wiki/index.md").read_text(encoding="utf-8")
PLANNED = set(re.findall(r"\[\[([^\]]+)\]\]", INDEX.split("## 待建頁面")[1])) if "## 待建頁面" in INDEX else set()
warnings = []

# 讀每份講義的每一頁
PAGE = {}
for f in (ROOT / "raw/text").glob("*.txt"):
    cur = None
    for line in f.read_text(encoding="utf-8").splitlines():
        m = re.match(r"=== (\S+) p\.(\d+) ===", line)
        if m:
            cur = (m.group(1), int(m.group(2))); PAGE[cur] = ""
        elif cur:
            PAGE[cur] += line + "\n"
NPAGES = {}
for (sid, p) in PAGE:
    NPAGES[sid] = max(NPAGES.get(sid, 0), p)

PAGES = {p.stem: p for p in (ROOT / "wiki").rglob("*.md")}
SKIP = {"index", "log"}
errors = []
for name, path in sorted(PAGES.items()):
    lines = path.read_text(encoding="utf-8").splitlines()
    in_code = in_front = False
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code; continue
        if s == "---":
            in_front = not in_front; continue
        if in_code or in_front or not s:
            continue
        where = f"{path.relative_to(ROOT)}:{i}"
        for t in LINK.findall(s):
            if t not in PAGES:
                (warnings if t in PLANNED else errors).append(f"{where} 連結 [[{t}]] 尚未建立")
        if name in SKIP or s.startswith(("相關：", "- 註（wiki）")) or s.startswith("|---"):
            continue
        if i < len(lines) and lines[i].strip().startswith("|---"):
            continue  # 表格標題列
        if s.startswith("#"):
            continue  # 標題交給 AI 審查（規則 5.3）
        cites = CITE.findall(s)
        if not cites:
            errors.append(f"{where} 沒有出處：{s[:40]}"); continue
        text = ""
        for _, sid, a, b in [(c[0], c[0].split()[0], c[1], c[2]) for c in cites]:
            a = int(a); b = int(b) if b else a
            if sid not in NPAGES:
                errors.append(f"{where} 來源 {sid} 不存在"); continue
            if b > NPAGES[sid]:
                errors.append(f"{where} {sid} 只有 {NPAGES[sid]} 頁，引用到 p.{b}")
            for p in range(a, b + 1):
                text += PAGE.get((sid, p), "")
        body = SRCID.sub("", LINK.sub("", CITE.sub("", s)))
        low = text.lower()
        words = [w for w in WORD.findall(body) if w.lower() not in STOP]
        if words and not any(w.lower() in low or ALIAS.get(w.lower(), "\0") in low for w in words):
            errors.append(f"{where} 英文術語 {words[:4]} 都不在所標頁")
        for n in NUM.findall(body):
            if n not in text:
                errors.append(f"{where} 數字 {n} 不在所標頁 {[c[0] for c in cites]}")

for w in warnings: print("⚠ 待建：" + w)
print(f"檢查 {len(PAGES)} 頁 wiki、{len(NPAGES)} 份講義（共 {len(PAGE)} 頁）")
if errors:
    print(f"❌ {len(errors)} 個問題"); print("\n".join(errors)); sys.exit(1)
print("✅ 全部通過")
