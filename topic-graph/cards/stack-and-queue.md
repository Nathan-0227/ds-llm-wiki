# 證據卡：stack-and-queue

- Stack 是 Last-In-First-Out（LIFO），只有一端可以進出 [C3 p.4]。
- 操作：IsEmpty、Top（看頂端）、Push（放到頂端）、Pop（移除頂端）[C3 p.6]。
- 可以用 linked list 實作：Push 就是在 top 前面接一個新 node [C4 p.19-20]。
- Queue 是 First-In-First-Out（FIFO）：資料從 rear 進、從 front 出 [C3 p.15]。
- Linear queue 的問題：前面還有空位，rear 卻已到底而 overflow [C3 p.16]。
- Circular queue：n 個位置最多只用 n-1 個，否則無法分辨滿和空 [C3 p.18]。
- 也可以用 linked list 實作：Push 接在 rear、Pop 從 front 刪除 [C4 p.21-22]。
- 非遞迴 DFS 用 stack：看頂端、push 新 node、沒路就 pop [G2 p.3]。
- BFS 用 queue：dequeue 一個 node，把它沒拜訪過的鄰居 enqueue [G2 p.6]。
- 二元樹的 preorder、inorder、postorder 都需要 stack；level-order 用 queue [C5 p.22]。
- C3 用一個 0／1 迷宮矩陣示範用 stack 記錄走過的位置（row、col、dir）[C3 p.29][C3 p.31]。
- 每格可以走的方向（Allowable Moves）：N、NE、E、SE、S、SW、W、NW [C3 p.30]。
