# 深度優先搜尋（Depth-First Search, DFS）

## 直覺
- 講義用「拿粉筆和一條線探索迷宮」說明 DFS [G1 p.26]。
- 每個地點有三種狀態：還沒去過（Not been there yet）、去過但出口還沒探完、去過且出口都探完 [G1 p.26]。
- 講義用一連串投影片一步一步示範這個迷宮怎麼被探索（explored）[G1 p.26-41]。
- 叫 depth-first 是因為「先盡量往深處走」（go as deep as we can），過程中隱含地建出一棵 DFS tree [G1 p.54]。

## 遞迴版虛擬碼（有 start/finish time）
- 每個 vertex 記錄狀態：Unvisited、In progress、All done，以及第一次進入的時間與完成的時間 [G1 p.42]。
- 講義說明這種寫法的 bookkeeping 比較多，但之後的應用會用到 [G1 p.42]。

[G1 p.43]
```
DFS(w, currentTime):
    w.startTime = currentTime
    currentTime++
    Mark w as in progress
    for v in w.neighbors:
        if v is unvisited:
            currentTime = DFS(v, currentTime)
            currentTime++
    w.finishTime = currentTime
    Mark w as all done
    return currentTime
```

## 性質
- DFS 會找到從起點出發能到達的所有 nodes；在無向圖中這叫 connected component [G1 p.52]。
- 要探索整張圖（explore the whole graph），講義的做法是重複做（Do it repeatedly）[G1 p.53]。
- DFS 在 directed graph 上也能用；講義例子是只走到 C、不走到 B [G1 p.57]。

## 執行時間
- 每條 edge 最多看兩次（兩個端點各一次），每個 vertex 最多拜訪一次，所以是 O(m+n) [G1 p.55]。
- 以 linked-list 格式的圖計算：每個 vertex 做 O(1) 的 bookkeeping 加上 O(deg(w)) 檢查 neighbors，總共 O(n + m) [G1 p.56]。

> ⚠ 兩種寫法：G1 用遞迴並記錄 start/finish time，並說明「這不是唯一的寫法，迭代版見課本」[G1 p.51]；G2 給的是用 stack 的非遞迴版本，見 [[dfs-nonrecursive]] [G2 p.3]。

相關：[[dfs-applications]]、[[bfs]]、[[stack-and-queue]]
