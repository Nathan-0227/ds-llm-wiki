# 圖的表示法：Adjacency Matrix 與 Adjacency List

## Option 1：Adjacency matrix（相鄰矩陣）
- 用 0/1 矩陣表示，列與行都是 vertices 1–4；對照 [G1 p.16] 的邊集合，1 出現在有邊的位置 [G1 p.16][G1 p.18]。
- 有向圖時列代表 Source、行代表 Destination [G1 p.20]。

## Option 2：Adjacency list（相鄰串列）
- 每個 vertex 存一串 neighbors；例如 4 的 neighbors 是 2 和 3 [G1 p.21]。
- 講義計算 DFS 執行時間時，假設圖用 linked-list format 儲存 [G1 p.56]；linked list 本身見 C4 [C4 p.2]。

## 兩種都支援的基本操作
- Edge Membership：邊 e 是否在 E 裡？Neighbor Query：vertex v 的 neighbors 是誰？[G1 p.22]
- vertices 也可以存其他資訊，例如名稱、IP address、演算法用的輔助資訊 [G1 p.22]。

## 取捨（n 個 vertices、m 條 edges）[G1 p.23]
| 操作 | Adjacency matrix | Adjacency list |
|---|---|---|
| Edge membership | O(1) [G1 p.23] | O(deg(v)) 或 O(deg(w)) [G1 p.23] |
| Neighbor query | O(n) [G1 p.23] | O(deg(v)) [G1 p.23] |
| Space | O(n^2) [G1 p.23] | O(n + m) [G1 p.23] |

- adjacency list 通常較適合 sparse graph（m ≪ n^2）[G1 p.23]。
- 講義在 adjacency list 那一欄註明：之後整門課都假設用這個表示法（this representation）[G1 p.23]。

相關：[[graph-basics]]、[[big-o]]
