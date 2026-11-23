# 證據卡：tree-traversal

- 樹有一個 root，其餘 nodes 分成互不相交的 subtrees [C5 p.4]。
- degree 是一個 node 的 subtree 數；leaf 是 degree 為零的 node [C5 p.6]。
- root 的 level 是 1，height（depth）是 nodes 的最大 level [C5 p.7]。
- Preorder：root → left subtree → right subtree [C5 p.16]。
- Inorder：left subtree → root → right subtree [C5 p.16]。
- Postorder：left subtree → right subtree → root [C5 p.16]。
- 在算術運算式樹上，三者分別得到 prefix、infix、postfix 運算式 [C5 p.17]。
[C5 p.19]
- C5 用 stack 模擬遞迴來做非遞迴 inorder [C5 p.21]。
> ⚠ 講義內部不一致：C5 p.21 的註解寫「move down leftChild fields」，但同一迴圈的程式碼寫的是 `currentNode = currentNode->rightChild` [C5 p.21]。依 inorder 的定義（先走 left subtree）[C5 p.16]，註解與程式碼至少有一處有誤；本 wiki 不替講義改。
- Preorder、inorder、postorder 都需要 stack；level-order 用 queue [C5 p.22]。
- 一層的 nodes 都拜訪完才往下一層 [C5 p.22]。
- 講義例子的 level-order 結果：+*E*D/CAB [C5 p.23]。
- G2 指出 BFS 和 level-order 相似，也是以 queue 為基礎 [G2 p.5]。
- Binary search tree：左 subtree 的 key 都比 root 小，右 subtree 都比 root 大，且左右也都是 BST [C5 p.37]。
- G1 的大綱與 Recap 列出「DFS 用於 BST 的 in-order traversal」[G1 p.2][G1 p.119]。
