# 用 Queue 實作 BFS

- BFS 的策略和 level-order 相似：先拜訪自己，再拜訪所有鄰居，再拜訪鄰居的鄰居 [G2 p.5]。
- 和 level-order 一樣，BFS 以 queue 為基礎 [G2 p.5]。

[G2 p.6]
```
Algorithm bfs(v)
    q.createQueue();
    q.enqueue(v);
    mark v as visited;
    while (!q.isEmpty()) {
        w = q.dequeue();
        for (each unvisited node u adjacent to w) {
            q.enqueue(u);
            mark u as visited;
        }
    }
```

## 範例：在圖 G 上從 v5 開始（[[example-graph-g]]）[G2 p.7]
| Visit | Queue（front → back） |
|---|---|
| v5 | v5 → empty [G2 p.7] |
| v3 | v3 [G2 p.7] |
| v4 | v3, v4 → v4 [G2 p.7] |
| v2 | v4, v2 → v2 → empty [G2 p.7] |
| v1 | v1 → empty [G2 p.7] |

- 拜訪順序：v5, v3, v4, v2, v1 [G2 p.7]。

> ⚠ 與 G1 的差異：G1 的 BFS 用分層串列 Li，第 i 層是走 i 步能到的 nodes [G1 p.86]；G2 用一個 queue [G2 p.6]。

相關：[[bfs]]、[[stack-and-queue]]、[[tree-traversal]]
