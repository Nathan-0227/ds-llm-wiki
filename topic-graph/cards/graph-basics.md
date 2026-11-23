# 證據卡：graph-basics

- 無向圖 G 由頂點集合 V（vertices）與邊集合 E（edges）組成，寫成 G = (V,E) [G1 p.16]。
- 一個 vertex 的 degree 是連出去的邊數；有邊相連的 vertices 稱為 neighbors [G1 p.16]。
- 例子：V = {1,2,3,4}，E = { {1,3}, {2,4}, {3,4}, {2,3} }；vertex 4 的 degree 是 2，neighbors 是 2 和 3 [G1 p.16]。
- 有向圖的邊有方向（DIRECTED edges），同樣寫成 G = (V,E) [G1 p.17]。
- in-degree 是進來的邊數，out-degree 是出去的邊數 [G1 p.17]。
- 例子：E = { (1,3), (2,4), (3,4), (4,3), (3,2) }；vertex 4 的 in-degree 是 2、out-degree 是 1 [G1 p.17]。
- 圖可以描述 internet、航班、套件相依、大腦神經連結等 [G1 p.4-14]。
- 我們想對圖回答問題，例如 routing、community detection、選課先修限制 [G1 p.15]。
- 樹（tree）的定義：有一個 root，其餘 nodes 分成互不相交的 subtrees [C5 p.4]。
- 講義中 DFS 與 BFS 執行時都會「隱含地建出一棵樹」，稱為 DFS tree / BFS tree，見 [[dfs]]、[[bfs]] [G1 p.54][G1 p.89]。
