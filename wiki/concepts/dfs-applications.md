# DFS 的應用

## Connected components
- DFS 找到起點能到達的所有 nodes；在無向圖中這叫 connected component [G1 p.52]。

## Topological sorting（拓撲排序）
- 問題：要怎麼安裝套件才不違反相依需求（dependency requirements）？[G1 p.58]
- 目標：找到一個 vertices 的排列，使所有相依需求都被滿足；也就是如果 v 排在 w 前面，就沒有從 w 到 v 的邊 [G1 p.59]。
- 前提：相依圖沒有 cycle，也就是 Directed Acyclic Graph（DAG）[G1 p.59]。
- 定理：在 DAG 上做 DFS，如果有邊 A → B，則 B.finishTime < A.finishTime [G1 p.66]。
- 所以照 DFS finish time 的反序安裝即可 [G1 p.67]。
- 做法：做 DFS，每當一個 vertex 標成 all done，就把它放到串列最前面 [G1 p.68]。
- 講義範例得到的順序：dpkg、coreutils、tar、libbz2、libselinux1、multiarch_support [G1 p.68]。

## In-order traversal of BSTs
- 講義大綱與 Recap 列出 DFS 也可用於 BST 的 in-order traversal [G1 p.2][G1 p.119]。
- 本份講義的文字中沒有展開這部分（講義未提供細節）；BST 與 inorder 見 [[tree-traversal]] [G1 p.119]。

相關：[[dfs]]
