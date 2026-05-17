# Page Repair Queue — 二次修复队列

**触发条件**：已完成页面在后续审计中发现质量问题，需重新入队修复。

**格式**：`|| N | 页面 | 问题类型 | 发现时间 | 状态 |`

---

## 问题类型说明

| 问题类型 | 含义 | 修复策略 |
|---------|------|---------|
| DUP | `sep_count > 2`，历史残留块未清理 | 调用 `clean_page_before_write()` 后重新写入 |
| SRC_POLLUTION | 来源论文表格 > 5000 字，虚高 bc | 保留表格但截断到合理长度，清理污染正文 |
| LOW_BF | `block_formulas < 5` | 需判断：公式密集页可跳过，方法/模型页必须补充 |
| BC_LOW | `body_chars < 2000` | 全量重写，提升正文质量 |
| PLACEHOLDER | 含占位符 | 替换占位符为实际内容 |

---

## 待修复页面

| 序号 | 页面 | 问题类型 | 发现时间 | 状态 |
|------|------|---------|---------|------|
| 1 | wiki/models/converter/vsc-model.md | DUP(8→2) | 2026-05-17 | **completed** | 修复提交 e5982e5e，sep 8→2 |
| 2 | wiki/models/basic-component/constant-power-load.md | DUP(3→2) | 2026-05-17 | **completed** | 修复提交 e5982e5e，sep 3→2 |
| 3 | wiki/models/compensation/tcsc-model.md | DUP(3→2) | 2026-05-17 | **completed** | 修复提交 e5982e5e，sep 3→2 |
| 4 | wiki/methods/control/microgrid-control.md | DUP(3→2) | 2026-05-17 | **completed** | 修复提交 e5982e5e，sep 3→2 |
| 5 | wiki/topics/modeling-methods/dynamic-phasor.md | SRC_POLLUTION | 2026-05-17 | **false_positive** | regex bug 误报，实际 src=0，bc=4600/bf=22，质量合格 |
| 6 | wiki/methods/system-studies/simulation-tools-status.md | LOW_BF(3) | 2026-05-17 | **acceptable** | 工具方法论页面，字段完整性检查方法论，bf=3 符合页面类型，不需修复 |

---

## 修复工作流

1. 读取实际文件，测量各项指标，确认问题
2. 对于 **DUP**：调用 `clean_page_before_write()` → 重新 enrich 该页 → 验证
3. 对于 **SRC_POLLUTION**：识别污染来源论文章节 → 截断到 ≤5000 字 → 验证
4. 对于 **LOW_BF**：判断页面类型（工具对比页→可接受，方法页→重写补充公式）
5. 对于 **BC_LOW / PLACEHOLDER**：全量重写
6. 修复完成后更新本队列对应行为 `completed`
7. 在主队列 `page-enrichment-queue.md` 中同步更新状态

---

## 修复记录

（每条修复后追加）

| 序号 | 页面 | 修复操作 | 修复后指标 | 完成时间 |
|------|------|---------|---------|---------|