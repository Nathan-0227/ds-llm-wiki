# 證據卡：bfs-applications

- 兩個 vertices 間的 distance，是它們之間最短路徑的邊數 [G1 p.94]。
- 從 w 做 BFS，在 Li 裡的每個 v，w 到 v 的最短路徑長度就是 i [G1 p.94]。
- BFS tree 上的路徑就是一條最短路徑；如果找不到 v，distance 是無限大 [G1 p.94]。
- 講義的課前練習：Samuel L. Jackson 的 Bacon number（答案是 2）[G1 p.90]。
> ⚠ 講義文字不一致：同一頁寫「可以在 O(n+m) 找到 u 到 v 的最短路徑」，下一行又出現「time O(m)」[G1 p.95]；而講義另一頁給的 BFS 執行時間是 O(n + m) [G1 p.88]。
- 問題：一群魚放兩個魚缸，會打架的不能放同一缸，做得到嗎？[G1 p.97]
- Bipartite graph：可以把 vertices 塗成兩色，使同色之間沒有邊 [G1 p.98]。
- 做法：把 BFS tree 的各層交替塗兩種顏色；若從未把相連的兩個 nodes 塗成同色，就是 bipartite，否則不是 [G1 p.103]。
- 理由：若 BFS 把兩個 neighbors 塗成同色，代表找到一個 odd length 的 cycle，而 odd cycle 不可能用兩色塗好 [G1 p.115-116]。
- 時間 O(n + m) [G1 p.117]。
