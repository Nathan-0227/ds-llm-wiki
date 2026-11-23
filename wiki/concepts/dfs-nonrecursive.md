# 非遞迴 DFS（用 Stack）

- G2 給出不用遞迴、改用 stack 的 DFS 演算法 [G2 p.3]。

[G2 p.3]
```
Algorithm dfs(v)
    s.createStack();
    s.push(v);
    mark v as visited;
    while (!s.isEmpty()) {
        let x be the node on the top of the stack s;
        if (no unvisited nodes are adjacent to x)
            s.pop();            // backtrack
        else {
            select an unvisited node u adjacent to x;
            s.push(u);
            mark u as visited;
        }
    }
```

- 重點：看 stack 頂端的 node；還有沒拜訪的鄰居就 push 進去往深處走，沒有就 pop（backtrack）[G2 p.3]。

## 範例：在圖 G 上從 v3 開始（[[example-graph-g]]）[G2 p.4]
| 動作 | stack |
|---|---|
| visit v3 | v3 [G2 p.4] |
| visit v2 | v3, v2 [G2 p.4] |
| visit v1 | v3, v2, v1 [G2 p.4] |
| backtrack | v3, v2 [G2 p.4] |
| visit v4 | v3, v2, v4 [G2 p.4] |
| visit v5 | v3, v2, v4, v5 [G2 p.4] |
| backtrack ×3 | v3, v2, v4 → v3, v2 → v3 [G2 p.4] |
| backtrack | empty [G2 p.4] |

- 拜訪順序：v3, v2, v1, v4, v5 [G2 p.4]。

> ⚠ 與 G1 的差異：G1 的 DFS 是遞迴版並記錄 start／finish time [G1 p.43]，G1 也說明迭代版要看課本 [G1 p.51]；G2 的非遞迴版不記錄時間 [G2 p.3]。

相關：[[dfs]]、[[stack-and-queue]]
