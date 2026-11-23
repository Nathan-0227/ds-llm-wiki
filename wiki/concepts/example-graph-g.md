# 範例圖 G（G2 的 v1–v5）

- G2 的 DFS 與 BFS 範例都用名為 G 的圖，vertices 是 v1, v2, v3, v4, v5（圖是否相同、是否無向需看圖）[G2 p.2][G2 p.7]。
- 邊（從 G2 p.2 的圖讀出，文字抽取無法驗證，需看圖）：v1–v2、v2–v3、v2–v4、v3–v4、v3–v5、v4–v5 [G2 p.2]。
- DFS 從 v3 開始的拜訪順序：v3, v2, v1, v4, v5 [G2 p.4]。
- BFS 從 v5 開始的拜訪順序：v5, v3, v4, v2, v1 [G2 p.7]。
- 講義沒有說明有多個 unvisited 鄰居時選哪一個（講義未提供）[G2 p.3]；[G2 p.3]
- 註（wiki）：用上面看圖讀出的邊、照「編號小的先選」跑 G2 的演算法，結果與講義 p.4、p.7 的順序一致；見 scripts/check_traversal.py。

相關：[[dfs-nonrecursive]]、[[bfs-queue]]
