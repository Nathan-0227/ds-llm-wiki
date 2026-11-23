# 資料結構 LLM Wiki × Graph 與 BFS/DFS 教學簡報

TAICA 生成式AI：文字與圖像生成的原理與實務（115-1）第十週作業。

依 [Karpathy 的 LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 做法，把 CSE 215 資料結構講義（12 份）整理成知識庫，再用 Graph 流程產生教學 HTML 簡報。

- **首頁**：https://nathan-0227.github.io/ds-llm-wiki/
- **教學簡報**：https://nathan-0227.github.io/ds-llm-wiki/deck.html
- **Wiki 網頁版**：https://nathan-0227.github.io/ds-llm-wiki/wiki.html（公開版不含講義全文）

網頁由 `docs/` 資料夾提供（GitHub Pages：main 分支 /docs）。

## 資料夾
| 路徑 | 內容 |
|---|---|
| `00-需求訪談紀錄.md` | 先討論、後生成的訪談；需求變更；事後確認訪談 |
| `AGENTS.md` | 員工手冊（wiki 規則） |
| `wiki/` | `concepts/` 概念頁、`sources/` 來源頁、`index.md`、`log.md` |
| `topic-graph/` | 大綱、證據卡、逐頁稿、`deck.html` |
| `scripts/` | `lint_wiki.py`、`graph_gates.py`（關卡 A–C）、`check_traversal.py`、`build_deck.py`、`check_render.py`（關卡 E） |
| `checks/` | 每次執行的檢查紀錄 |
| `WORKFLOW.md`、`REFLECTION.md`、`流程圖.png` | Loop／Graph 設計與反思 |

## 沒有放進這個 repo 的東西
講義 PDF 與抽出的講義全文（`raw/`）是課程教材，**已從 git 歷史中移除**，所以 `lint_wiki.py` 需要在本地放回 `raw/text/` 才能執行。wiki 每一句仍標有講義頁碼（例如 `[G1 p.23]`）。

## 分工
主題、範圍、讀者、語言、出處粒度、是否要動畫與圖片、逐頁內容由我決定並確認；Claude（agent 模式）負責訪談提問、撰寫 wiki、寫檢查腳本、產生簡報，並用另一個 AI 對話做忠實度審查。詳見 `00-需求訪談紀錄.md`。
