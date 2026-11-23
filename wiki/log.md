# Log

## [2026-11-23 20:26] setup | AGENTS.md、需求訪談紀錄
## [2026-11-23 20:50] ingest | G1 Lecture 9 Graphs, BFS and DFS
- 新增 sources/G1；concepts：graph-basics、graph-representation、dfs、bfs、dfs-applications、bfs-applications
- ⚠ 記錄：G1 p.95 O(n+m) 與 O(m) 並存；G1 遞迴 DFS vs G2 非遞迴（G2 待 ingest）

## [2026-11-23 21:00] ingest | G2 Nonrecursive DFS and BFS
- 新增 sources/G2；concepts：dfs-nonrecursive、bfs-queue、example-graph-g
- 範例圖 G 的邊從 G2 p.2 圖片讀出；scripts/check_traversal.py 核對 DFS 順序、stack 變化、BFS 順序 ✅
## [2026-11-23 21:05] ingest | C3、C4、C5、C1
- 新增 sources/C3、C4、C5、C1；concepts：stack-and-queue、tree-traversal、big-o
- ⚠ 記錄：C5 p.21 註解（leftChild）與程式碼（rightChild）不一致
- lint 抓到 4 句：2 句來源頁的「與 graph 相關」該頁沒提 graph、1 句引用圖片內容、1 句「8 個方向」是 AI 自己數的 → 改寫

## [2026-11-23 21:20] ingest（輕量）| C2、C7、C7E、C8、C10、C11
- 每份一頁來源頁：章節大綱（依各頁標題）＋關鍵定義／複雜度，逐句標頁碼

## [2026-11-23 21:45] 需求變更 | 簡報讀者改為完全不會的人、加入講義圖片
- dfs、bfs 各補一句，引用迷宮與鳥瞰的連續投影片頁碼範圍（簡報要用那些頁的圖）
- lint 抓到「16 張投影片」是自己數的數字（又一次同類型錯誤）→ 刪掉數字
