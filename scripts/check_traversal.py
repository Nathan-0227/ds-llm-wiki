#!/usr/bin/env python3
"""核對：照 G2 的演算法在圖 G 上跑，結果是否和講義寫的順序一致。
圖 G 的邊從 G2 p.2 的圖讀出；講義順序取自 G2 p.4（DFS）與 p.7（BFS）。"""
import sys
from collections import deque

EDGES = [("v1", "v2"), ("v2", "v3"), ("v2", "v4"), ("v3", "v4"), ("v3", "v5"), ("v4", "v5")]
ADJ = {}
for a, b in EDGES:
    ADJ.setdefault(a, []).append(b); ADJ.setdefault(b, []).append(a)
for k in ADJ: ADJ[k].sort()

LECTURE_DFS = ["v3", "v2", "v1", "v4", "v5"]          # G2 p.4
LECTURE_BFS = ["v5", "v3", "v4", "v2", "v1"]          # G2 p.7
LECTURE_DFS_STACKS = [["v3"], ["v3","v2"], ["v3","v2","v1"], ["v3","v2"], ["v3","v2","v4"],
                      ["v3","v2","v4","v5"], ["v3","v2","v4"], ["v3","v2"], ["v3"], []]  # G2 p.4

def dfs(v):  # G2 p.3
    s, seen, order, stacks = [v], {v}, [v], [[v]]
    while s:
        x = s[-1]
        nxt = [u for u in ADJ[x] if u not in seen]
        if not nxt: s.pop()
        else:
            u = nxt[0]; s.append(u); seen.add(u); order.append(u)
        stacks.append(list(s))
    return order, stacks

def bfs(v):  # G2 p.6
    q, seen, order = deque([v]), {v}, [v]
    while q:
        w = q.popleft()
        for u in ADJ[w]:
            if u not in seen:
                q.append(u); seen.add(u); order.append(u)
    return order

ok = True
d, st = dfs("v3"); b = bfs("v5")
for name, got, want in [("DFS 順序", d, LECTURE_DFS), ("DFS stack 變化", st, LECTURE_DFS_STACKS), ("BFS 順序", b, LECTURE_BFS)]:
    flag = got == want; ok &= flag
    print(f"{'✅' if flag else '❌'} {name}：程式 {got} ／ 講義 {want}")
sys.exit(0 if ok else 1)
