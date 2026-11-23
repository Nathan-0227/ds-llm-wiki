# 逐頁稿（只能用大綱分配給該頁的證據卡；每行用 {卡名} 標來源）

## Graph 與 BFS / DFS
cards:
資料結構｜教學簡報
內容全部取自本人建立的資料結構 LLM Wiki，每一頁都標出講義頁碼

## 今天要學會的三件事
cards: graph-basics, dfs, bfs
① 什麼是 Graph：G = (V,E) [G1 p.16] {graph-basics}
② DFS：先盡量往深處走（go as deep as we can）[G1 p.54] {dfs}
③ BFS：先盡量往廣處走（go as broadly as we can）[G1 p.89] {bfs}

## 什麼是 Graph？
cards: graph-basics
visual: graph-example
Graph 由頂點 V（vertices）和邊 E（edges）組成，寫成 G = (V,E) [G1 p.16] {graph-basics}
有邊相連的 vertices 叫 neighbors；degree 是連出去的邊數 [G1 p.16] {graph-basics}
例：V = {1,2,3,4}，E = { {1,3}, {2,4}, {3,4}, {2,3} } [G1 p.16] {graph-basics}
有向圖的邊有方向，分成 in-degree 與 out-degree [G1 p.17] {graph-basics}
例子無所不在：internet、航班、套件相依、大腦神經連結 [G1 p.4-14] {graph-basics}

## 電腦怎麼存一張圖？
cards: graph-representation
visual: representation
Adjacency matrix：用 0/1 矩陣記錄哪兩個 vertices 之間有邊 [G1 p.16][G1 p.18] {graph-representation}
Adjacency list：每個 vertex 存一串 neighbors，例如 4 的 neighbors 是 2 和 3 [G1 p.21] {graph-representation}
Edge membership：matrix O(1)、list O(deg(v)) [G1 p.23] {graph-representation}
Neighbor query：matrix O(n)、list O(deg(v)) [G1 p.23] {graph-representation}
Space：matrix O(n^2)、list O(n + m)；list 較適合 sparse graph [G1 p.23] {graph-representation}

## 先備工具：Stack 與 Queue
cards: stack-and-queue
visual: stack-queue
Stack：Last-In-First-Out（LIFO），只有一端進出 [C3 p.4] {stack-and-queue}
操作：Push 放到頂端、Pop 移除頂端、Top 看頂端 [C3 p.6] {stack-and-queue}
Queue：First-In-First-Out（FIFO），從 rear 進、從 front 出 [C3 p.15] {stack-and-queue}
非遞迴 DFS 用 stack；BFS 用 queue [G2 p.3][G2 p.6] {stack-and-queue}

## DFS 的直覺：拿粉筆走迷宮
cards: dfs
講義用「拿粉筆和一條線探索迷宮」說明 DFS [G1 p.26] {dfs}
每個地點三種狀態：還沒去過、去過但出口沒探完、出口都探完 [G1 p.26] {dfs}
先盡量往深處走（go as deep as we can），過程中建出一棵 DFS tree [G1 p.54] {dfs}
DFS 會找到從起點能到達的所有 nodes（connected component）[G1 p.52] {dfs}

## 動手看：DFS 一步一步
cards: dfs-nonrecursive, example-graph-g
anim: dfs
看 stack 頂端：還有沒拜訪的鄰居就 push，沒有就 pop（backtrack）[G2 p.3] {dfs-nonrecursive}
圖 G 從 v3 開始，拜訪順序：v3, v2, v1, v4, v5 [G2 p.4] {dfs-nonrecursive}
講義沒說多個鄰居時先選誰；動畫用「編號小的先」，與講義順序一致 [G2 p.3][G2 p.4] {example-graph-g}

## BFS 的直覺：從天上鳥瞰
cards: bfs
講義用「如果我們會飛」、「鳥瞰（bird's-eye view）」說明 BFS [G1 p.79][G1 p.81] {bfs}
依「幾步能到」分層：zero steps、one step、two steps… [G1 p.81] {bfs}
Li = 從起點 w 走 i 步能到的 nodes [G1 p.86] {bfs}
先盡量往廣處走（go as broadly as we can），過程中建出一棵 BFS tree [G1 p.89] {bfs}

## 動手看：BFS 一步一步
cards: bfs-queue, example-graph-g
anim: bfs
先拜訪自己，再拜訪所有鄰居，再拜訪鄰居的鄰居 [G2 p.5] {bfs-queue}
dequeue 一個 node，把它沒拜訪過的鄰居 enqueue [G2 p.6] {bfs-queue}
圖 G 從 v5 開始，拜訪順序：v5, v3, v4, v2, v1 [G2 p.7] {bfs-queue}

## DFS vs BFS
cards: stack-and-queue, dfs, bfs, tree-traversal
visual: compare-table
DFS：先往深處走；非遞迴版用 stack [G1 p.54][G2 p.3] {dfs}{stack-and-queue}
BFS：先往廣處走；用 queue [G1 p.89][G2 p.6] {bfs}{stack-and-queue}
兩者都會找到起點能到達的所有 nodes [G1 p.52][G1 p.87] {dfs}{bfs}
和樹對照：preorder／inorder／postorder 需要 stack，level-order 用 queue [C5 p.22] {tree-traversal}
BFS 的策略和 level-order 相似 [G2 p.5] {tree-traversal}

## 跑多快？執行時間
cards: big-o, graph-representation, dfs
f(n) 是 O(g(n))：n 夠大之後，f(n) 不超過 g(n) 的常數倍 [C1 p.28] {big-o}
DFS、BFS 都是 O(n + m)，n 是 vertices 數、m 是 edges 數 [G1 p.56][G1 p.88] {big-o}
原因：每條 edge 最多看兩次、每個 vertex 最多拜訪一次 [G1 p.55] {dfs}
用 adjacency list 時，每個 vertex 只要檢查自己的 neighbors [G1 p.56] {graph-representation}

## DFS 與 BFS 能做什麼
cards: dfs-applications, bfs-applications
DFS → topological sorting：照 finish time 的反序排，就不會違反相依 [G1 p.67] {dfs-applications}
例：安裝套件順序 dpkg、coreutils、tar、libbz2… [G1 p.68] {dfs-applications}
BFS → shortest path：在 Li 裡的 v，與起點的距離就是 i [G1 p.94] {bfs-applications}
BFS → bipartite：BFS tree 各層交替塗兩色，相鄰同色就不是 bipartite [G1 p.103] {bfs-applications}
兩者時間都是 O(n + m) [G1 p.117] {bfs-applications}

## 讀講義時要注意的地方
cards: bfs-applications, tree-traversal, dfs-nonrecursive
⚠ 同一頁同時出現 O(n+m) 與「time O(m)」[G1 p.95] {bfs-applications}
⚠ 非遞迴 inorder：註解寫 leftChild，程式碼卻寫 rightChild [C5 p.21] {tree-traversal}
DFS 有兩種寫法：G1 遞迴且記錄時間、G2 用 stack [G1 p.43][G2 p.3] {dfs-nonrecursive}
Wiki 不替講義改，只並列標註，讓讀者自己對照原文 {tree-traversal}

## 回顧＋小測驗
cards: example-graph-g, stack-and-queue, big-o
Q1 非遞迴 DFS 用 stack 還是 queue？ {stack-and-queue}
quiz-answer: stack [G2 p.3] {stack-and-queue}
Q2 圖 G 從 v5 做 BFS，拜訪順序是？ {example-graph-g}
quiz-answer: v5, v3, v4, v2, v1 [G2 p.7] {example-graph-g}
Q3 DFS 和 BFS 的執行時間是？ {big-o}
quiz-answer: O(n + m) [G1 p.56][G1 p.88] {big-o}

## 本簡報 ↔ Wiki 對應表
cards:
visual: mapping-table
