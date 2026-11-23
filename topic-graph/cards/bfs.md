# 證據卡：bfs

- 講義用「如果我們會飛」、「鳥瞰世界（bird's-eye view）」說明 BFS [G1 p.79][G1 p.81]。
- 依照「幾步能到」把 nodes 分層：zero steps、one step、two steps、three steps [G1 p.81]。
- 講義用一連串投影片，依「幾步能到」（steps）逐步上色 [G1 p.81-85]。
- 叫 breadth-first 是因為「先盡量往廣處走」（go as broadly as we can），過程中隱含地建出一棵 BFS tree [G1 p.89]。
- Li 是從起點 w 走 i 步能到的 nodes 集合 [G1 p.86]。
[G1 p.86]
- BFS 也會找到從起點能到達的所有 nodes，也可以用來找 connected components [G1 p.87]。
- BFS 的執行時間和 DFS 同理，是 O(n + m) [G1 p.88]。
- BFS 在 directed graph 上也能用 [G1 p.88]。
> ⚠ 兩種寫法：G1 用分層的 Li 串列 [G1 p.86]；G2 用 queue 實作，見 [[bfs-queue]] [G2 p.6]。
