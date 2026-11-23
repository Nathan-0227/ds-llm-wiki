# 逐頁稿 v2（讀者：完全不會的人；只能用大綱分配給該頁的證據卡；每行用 {卡名} 標來源）

## Graph 與 BFS / DFS
cards:
從迷宮、魚缸到裝軟體，認識電腦怎麼「走」一張圖
內容全部取自本人建立的資料結構 LLM Wiki，每一頁都標出講義頁碼

## 這些都是 Graph
cards: graph-basics
photo: G1 p.4, G1 p.5, G1 p.7, G1 p.14
網際網路、航班、套件相依、大腦神經連結，都可以畫成 Graph [G1 p.4-14] {graph-basics}
我們想問它問題：怎麼走（routing）？誰跟誰是一群？選課怎麼不違反先修？[G1 p.15] {graph-basics}

## Graph 只有兩樣東西：點和線
cards: graph-basics
visual: graph-example
點叫 vertex（V），線叫 edge（E），合起來寫成 G = (V,E) [G1 p.16] {graph-basics}
有線連在一起的點，互相叫 neighbors [G1 p.16] {graph-basics}
例：右圖的點 4 連了兩條線，degree 是 2，neighbors 是 2 和 3 [G1 p.16] {graph-basics}
線也可以有方向（directed edges）[G1 p.17] {graph-basics}

## 電腦怎麼記住一張圖？
cards: graph-representation
visual: representation
方法一：用 0/1 表格（矩陣），有線的地方填 1 [G1 p.16][G1 p.18] {graph-representation}
方法二 adjacency list：每個點記下自己的 neighbors [G1 p.21] {graph-representation}
表格查「有沒有線」最快：O(1) [G1 p.23] {graph-representation}
清單比較省空間：O(n + m)，線不多的圖適合用它 [G1 p.23] {graph-representation}

## 兩個小工具：Stack 與 Queue
cards: stack-and-queue
visual: stack-queue
Stack：後放進去的先拿出來（LIFO），只有一個出入口 [C3 p.4] {stack-and-queue}
Queue：先排隊的先出來（FIFO），從後面進、前面出 [C3 p.15] {stack-and-queue}
記住這句：不用遞迴寫的 DFS 用 stack，BFS 用 queue [G2 p.3][G2 p.6] {stack-and-queue}

## DFS：拿粉筆走迷宮
cards: dfs
photo: G1 p.41
想像你在迷宮裡，手上有粉筆和一條線 [G1 p.26] {dfs}
用粉筆記下每個地方：沒去過、去過但還有路沒走、全部走完 [G1 p.26] {dfs}
它叫 depth-first，因為會盡量往深處走（go as deep as we can）[G1 p.54] {dfs}
講義用一連串投影片，一步一步示範整個迷宮怎麼被探索 [G1 p.26-41] {dfs}
最後，從起點走得到的地方全部都會被走過 [G1 p.52] {dfs}

## 動手玩：DFS
cards: dfs-nonrecursive, example-graph-g
anim: dfs
按「下一步」，看 stack 怎麼長高、變矮 [G2 p.3] {dfs-nonrecursive}
有新鄰居就 push（往前走），沒路了就 pop（退回來）[G2 p.3] {dfs-nonrecursive}
從 v3 出發，走的順序：v3, v2, v1, v4, v5 [G2 p.4] {dfs-nonrecursive}
講義沒說先走哪個鄰居；這裡選編號小的，邊是看講義圖讀出的 [G2 p.3][G2 p.2] {example-graph-g}

## BFS：飛到天上往下看
cards: bfs
photo: G1 p.85
講義的比喻：如果我們會飛，用鳥瞰（bird's-eye view）來看 [G1 p.79][G1 p.81] {bfs}
先找一步（one step）能到的地方，再找兩步、三步（two、three steps）能到的 [G1 p.81] {bfs}
講義依「幾步能到」（steps），一步一步把點上色 [G1 p.81-85] {bfs}
規則：先把附近的走完，再往外擴（go as broadly as we can）[G1 p.89] {bfs}

## 動手玩：BFS
cards: bfs-queue, example-graph-g, stack-and-queue, bfs
anim: bfs
按「下一步」，看 queue 怎麼排隊 [G2 p.6] {bfs-queue}
從隊伍前面拿出一個點（dequeue），把它還沒去過的鄰居排到後面（enqueue）[G2 p.6] {stack-and-queue}
從 v5 出發，走的順序：v5, v3, v4, v2, v1 [G2 p.7] {bfs-queue}
同樣是 BFS，有兩種寫法：G1 用一層一層的清單 Li、G2 用一個 queue [G1 p.86][G2 p.6] {bfs}

## DFS vs BFS
cards: stack-and-queue, dfs, bfs, tree-traversal
visual: compare-table
DFS：先往深處鑽，非遞迴寫法用 stack [G1 p.54][G2 p.3] {dfs}{stack-and-queue}
BFS：先往旁邊擴，用 queue [G1 p.89][G2 p.6] {bfs}{stack-and-queue}
兩個都能找到起點走得到的所有點 [G1 p.52][G1 p.87] {dfs}{bfs}
樹也一樣：一層一層走（level-order）用 queue，和 BFS 很像 [C5 p.22][G2 p.5] {tree-traversal}

## 它們跑得多快？
cards: big-o, graph-representation, dfs
每條線最多看兩次，每個點最多去一次 [G1 p.55] {dfs}
所以時間是 O(n + m)：n 是點的數量、m 是線的數量 [G1 p.55] {dfs}
O(...) 是在說：n 變大時，需要的量最多以什麼速度長（不管常數倍）[C1 p.28] {big-o}
DFS、BFS 都是 O(n + m) [G1 p.56][G1 p.88] {big-o}

## DFS 的用途：裝軟體要照什麼順序？
cards: dfs-applications, graph-basics
photo: G1 p.8
裝軟體時，有些套件必須先裝別的套件才能用 [G1 p.58] {dfs-applications}
這種「誰要先」的關係也是 Graph，而且不能繞圈（DAG）[G1 p.59] {dfs-applications}
做 DFS，照「走完的時間」（finish time）倒過來排，就是安全的安裝順序 [G1 p.67] {dfs-applications}

## BFS 的用途：最短距離與魚缸問題
cards: bfs-applications
photo: G1 p.97
最短距離：BFS 第 i 層的點，離起點剛好 i 步 [G1 p.94] {bfs-applications}
課前練習：Samuel L. Jackson 的 Bacon number 是多少？答案是 2 [G1 p.90] {bfs-applications}
魚缸問題：會打架的魚不能放同一缸，兩個缸放得下嗎？[G1 p.97] {bfs-applications}
做法：BFS 一層塗 A 色、一層塗 B 色；相鄰的同色就放不下 [G1 p.103] {bfs-applications}

## 講義裡的小錯誤與寫法差異
cards: bfs-applications, tree-traversal, dfs-nonrecursive
⚠ 同一頁同時寫了 O(n+m) 和「time O(m)」[G1 p.95] {bfs-applications}
⚠ 非遞迴 inorder：註解寫 leftChild，程式碼卻寫 rightChild [C5 p.21] {tree-traversal}
DFS 有兩種寫法：G1 用遞迴並記錄時間、G2 用 stack [G1 p.43][G2 p.3] {dfs-nonrecursive}
本 wiki 不替講義改 {tree-traversal}

## 小測驗
cards: example-graph-g, stack-and-queue, big-o
Q1 不用遞迴的 DFS 用 stack 還是 queue？ {stack-and-queue}
quiz-answer: stack [G2 p.3] {stack-and-queue}
Q2 從 v5 做 BFS，走的順序是？ {example-graph-g}
quiz-answer: v5, v3, v4, v2, v1 [G2 p.7] {example-graph-g}
Q3 DFS 和 BFS 要花多少時間？ {big-o}
quiz-answer: O(n + m) [G1 p.56][G1 p.88] {big-o}

## 本簡報 ↔ Wiki 對應表
cards:
visual: mapping-table
