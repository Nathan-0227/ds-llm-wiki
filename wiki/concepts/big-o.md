# 時間複雜度與 Big-O

- 定義：如果存在正整數 a、b，使得所有 n ≧ b 時 f(n) ≦ a·g(n)，則 f(n) 是 O(g(n)) [C1 p.28]。
- 例：4n² + 100n = O(n²)，因為 n ≧ 100 時 4n² + 100n ≦ 5n²（講義上標在文字抽取中會變成 4n2）[C1 p.28]。
- 常數是 O(1)；不同底數的 log 只差常數倍，所以都寫 O(log n) [C1 p.28]。
- Time complexity 是程式需要的計算時間；Space complexity 是需要的記憶體 [C1 p.30]。
- 函數成長比較：n = 32 時，n² = 1,024，2ⁿ = 4,294,967,296 [C1 p.29]。

## 在圖演算法裡（n 個 vertices、m 條 edges）
- DFS、BFS 都是 O(n + m) [G1 p.56][G1 p.88]。
- 兩種表示法的 Space requirements：O(n²) 與 O(n + m)，見 [[graph-representation]] [G1 p.23]。

相關：[[graph-representation]]、[[dfs]]、[[bfs]]
