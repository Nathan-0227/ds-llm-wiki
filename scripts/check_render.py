#!/usr/bin/env python3
"""渲染檢查關卡：每頁截圖、檢查內容有沒有超出頁面（壓到 footer）、JS 錯誤、動畫最後畫面是否等於講義順序。"""
import sys, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
DECK = ROOT / "topic-graph/deck.html"; SHOTS = ROOT / "checks/render"; SHOTS.mkdir(parents=True, exist_ok=True)
WANT = {"dfs": "v3v2v1v4v5", "bfs": "v5v3v4v2v1"}
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1280, "height": 720})
    pg.on("pageerror", lambda e: errs.append(f"JS 錯誤：{e}"))
    pg.goto(DECK.as_uri()); pg.wait_for_timeout(1500)
    n = pg.locator(".slide").count()
    for i in range(1, n + 1):
        pg.evaluate(f"location.hash='#s{i}'"); pg.wait_for_timeout(250)
        bad = pg.evaluate("""() => { const s=document.querySelector('.slide.on'); const top=s.getBoundingClientRect().top;
            const lim=top+(650*s.getBoundingClientRect().height/720); const out=[];
            for (const el of s.querySelectorAll('li,p,table,svg,.cells,h2,.ctl')) { if (el.closest('footer')||el.closest('details')) continue;
              const r=el.getBoundingClientRect(); if (r.height && r.bottom>lim+1) out.push(el.tagName+':'+(el.textContent||'').trim().slice(0,20)); }
            return out; }""")
        if bad: errs.append(f"第 {i} 頁內容超出／壓到 footer：{bad[:3]}")
        pg.screenshot(path=str(SHOTS / f"s{i:02d}.png"))
        kind = pg.evaluate("document.querySelector('.slide.on .animwrap')?.dataset.anim || ''")
        if kind:
            for _ in range(30): pg.click(".slide.on [data-do=next]")
            got = pg.evaluate("[...document.querySelectorAll('.slide.on .seen .cells span')].map(x=>x.textContent).join('')")
            ok = got == WANT[kind]
            print(f"{'✅' if ok else '❌'} 第 {i} 頁 {kind.upper()} 動畫最後畫面：{got}（講義 {WANT[kind]}）")
            if not ok: errs.append(f"第 {i} 頁動畫順序不符")
            pg.screenshot(path=str(SHOTS / f"s{i:02d}-end.png"))
    b.close()
print(f"截圖 {n} 頁 → checks/render/")
if errs: print(f"❌ {len(errs)} 個問題"); print("\n".join(errs)); sys.exit(1)
print("✅ 渲染檢查全過")
