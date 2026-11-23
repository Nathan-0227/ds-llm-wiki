# 檢查紀錄 04：AI 審查 G1 ingest（新對話，只給 raw/text 與 wiki/）

結果：不支持 0、講反 0、部分支持 7（含 2 項「圖片內容、文字無法驗證」）

| 位置 | 問題 | 修法 |
|---|---|---|
| sources/G1:18 | 「多處提到 notebook」誇大（只有 2 處）；「不在 wiki 來源中」是 wiki 自述 | 改為只陳述講義提到 notebook，標 p.23、p.68 |
| graph-representation:4 | 「i 列 j 行為 1 代表有邊」p.18 沒有文字說明 | 改為「對照 p.16 的邊集合」並同時標兩頁 |
| graph-representation:9 | 「adjacency list 以 linked list 實作」C4 沒說 | 改引 G1 p.56「linked-list format」 |
| dfs:29 | 「每次從還沒走到的地方開始」來自圖片 | 刪掉 |
| dfs:30 | 「只沿著邊的方向走」是從例子推成通則 | 改為只描述講義例子 |
| bfs-applications:7 | Bacon number 的定義講義沒寫 | 改為講義原本的課前練習 |
| bfs-applications:9 | 「前一頁」位置錯誤（差 7 頁）；「矛盾」是詮釋 | 改為「講義文字不一致」並修正位置描述 |

觀察：這次沒有「不支持」，錯誤型態是**把圖片裡的資訊或自己的解讀寫成文字事實**。
lint 只能比對文字，抓不到這類問題 → 只能靠 AI 審查（或人工看圖）。
