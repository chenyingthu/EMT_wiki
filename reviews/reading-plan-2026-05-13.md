# 读书郎工作计划 - 2026-05-13

## 目标

通过深度阅读EMT_Doc中的PDF文献，获取知识，将wiki页面从"条目罗列"提升为"知识传递"水平。

## 工作逻辑

1. **拿到一个wiki页面** → 了解要阅读的主题、关键词、参考文献
2. **到EMT_Doc中定位PDF** → 找到需要深度阅读的资料
3. **深度阅读PDF** → 摘录信息、做出笔记
4. **反写wiki页面** → 使其达到"知识传递、能力增长、图文并茂、清晰准确"的水平

## 优先级策略

### P0 - 核心知识断链（必须优先处理）

这些页面是EMT知识体系的关键节点，但内容极度薄弱（<50字），且有大量wikilinks指向其他页面，说明它们在知识网络中处于枢纽位置：

| 页面 | 字数 | Wikilinks | 说明 |
|------|------|-----------|------|
| `topics/simulation/real-time-simulation.md` | 10 | 155 | 实时仿真入口 |
| `topics/modeling-methods/frequency-dependent-modeling.md` | 19 | 176 | 频变建模入口 |
| `topics/modeling-methods/dynamic-phasor.md` | 23 | 99 | 动态相量法 |
| `topics/simulation/large-scale-system-simulation.md` | 5 | 74 | 大规模系统仿真 |
| `topics/component-modeling/power-electronics.md` | 5 | 63 | 电力电子主题入口 |
| `topics/renewable-storage/wind-farm-modeling.md` | 19 | 75 | 风电场建模 |
| `models/converter/mmc-model.md` | 32 | 45 | MMC模型（核心！） |
| `models/converter/lcc-model.md` | 40 | 42 | LCC模型（核心！） |
| `models/control/model-predictive-control.md` | 20 | 3 | 标注"内容待补充" |

### P1 - 重要方法/模型页（内容<100字）

这些页面有实质内容但不够深入，需要补充公式推导、物理机制解释、对比分析等。

### P2 - 一般薄弱页面

内容<200字但有一定基础，可以后续逐步提升。

## 每个页面的处理标准

### 知识传递水平

1. **定义清晰**：什么是这个概念？在EMT中的角色是什么？
2. **物理机制**：它为什么能工作？背后的物理/数学原理是什么？
3. **公式推导**：有核心公式的推导过程，不只是列出公式
4. **对比分析**：和其他方法/模型比有什么优劣？适用场景是什么？
5. **量化指标**：在什么条件下精度是多少？计算量是多少？
6. **边界条件**：什么情况下不适用？局限是什么？
7. **知识关联**：通过wikilink连接到相关页面，形成知识网络

### 图文并茂

- 有Mermaid流程图/结构图展示核心机制
- 有表格对比不同方法/模型的参数
- 有公式块展示数学表达

## 执行计划

### 第一批：P0核心页面（7个）

1. **MMC模型** (`models/converter/mmc-model.md`) - 53个相关PDF
2. **LCC模型** (`models/converter/lcc-model.md`) - 查找相关PDF
3. **实时仿真** (`topics/simulation/real-time-simulation.md`) - 查找相关PDF
4. **频变建模** (`topics/modeling-methods/frequency-dependent-modeling.md`) - 查找相关PDF
5. **动态相量法** (`topics/modeling-methods/dynamic-phasor.md`) - 查找相关PDF
6. **电力电子主题** (`topics/component-modeling/power-electronics.md`) - 查找相关PDF
7. **风电场建模** (`topics/renewable-storage/wind-farm-modeling.md`) - 查找相关PDF

### 第二批：P1页面（按优先级逐步处理）

### 第三批：P2页面（持续改进）

## 注意事项

- 每次只处理一个页面，确保深度和质量
- 阅读PDF时要摘录关键信息，不能凭记忆
- 修改wiki页面后要验证格式正确
- 保持中文学术表达风格，与现有页面一致
