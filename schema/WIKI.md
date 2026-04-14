# EMT Wiki Schema

本文档定义 EMT Wiki 的结构、约定和工作流程。LLM Agent 在处理来源、回答问题、维护 Wiki 时，必须遵循本 schema。

## 目录结构

```
EMT_LLM_Wiki/
├── EMT_Doc/              # 原始来源（不可变）— 691 篇 PDF
├── wiki/
│   ├── overview.md       # EMT 领域概览
│   ├── index.md          # 全部内容索引
│   ├── log.md            # 追加式活动日志
│   ├── topics/           # 主题页（概念、理论）
│   ├── methods/          # 方法页（算法、求解技术）
│   ├── models/           # 模型页（设备、组件建模）
│   ├── entities/         # 实体页（学者、机构、工具）
│   └── sources/          # 来源摘要页（每篇或每批 PDF）
├── schema/WIKI.md        # 本文件
└── tools/
    └── extract_metadata.py  # PDF 元数据批量提取工具
```

## 命名约定

| 类型 | 目录 | 命名规则 | 示例 |
|------|------|----------|------|
| 来源 | `sources/` | `作者-年份-关键词.md` | `cao-2025-fixed-admittance-adc.md` |
| 主题 | `topics/` | `kebab-case.md` | `converter-driven-stability.md` |
| 方法 | `methods/` | `kebab-case.md` | `nodal-analysis.md` |
| 模型 | `models/` | `kebab-case.md` | `mmc-model.md` |
| 实体 | `entities/` | `kebab-case.md` | `wei-gu.md` |

所有文件名使用小写英文 kebab-case，内容为中文。

## 页面格式模板

### 来源页 (source)

```markdown
---
title: "论文标题"
type: source
authors: [作者1, 作者2]
year: 2025
journal: "期刊/会议名"
tags: [标签1, 标签2]
created: 2026-04-13
sources: ["EMT_Doc/01/文件名.pdf"]
---

## 摘要
[论文摘要]

## 核心贡献
- [贡献要点 1]
- [贡献要点 2]

## 使用的方法
- [[相关方法页]]

## 涉及的模型
- [[相关模型页]]

## 相关主题
- [[相关主题页]]

## 主要发现
[实验/仿真结果总结]

## 关键数据
| 指标 | 数值 |
|------|------|
| [指标名] | [值] |
```

### 主题页 (topic)

```markdown
---
title: "主题名称"
type: topic
tags: [标签1, 标签2]
created: 2026-04-13
updated: 2026-04-13
---

## 概述
[该主题的定义和范围]

## 核心概念
- [概念 1]
- [概念 2]

## 相关方法
- [[方法页]]

## 相关模型
- [[模型页]]

## 来源论文
| 论文 | 年份 | 贡献 |
|------|------|------|
| [[来源页]] | 2025 | [一句话贡献] |

## 发展脉络
[该主题的时间线和发展趋势]

## 开放问题
[尚未解决的研究问题]
```

### 方法页 (method)

```markdown
---
title: "方法名称"
type: method
tags: [标签]
created: 2026-04-13
updated: 2026-04-13
---

## 概述
[方法定义和适用范围]

## 原理
[核心算法/数学原理]

## 优缺点
| 优点 | 缺点 |
|------|------|
| [优点] | [缺点] |

## 应用该方法的论文
| 论文 | 年份 | 应用场景 |
|------|------|----------|
| [[来源页]] | 2025 | [场景描述] |

## 与其他方法的关系
- vs [[其他方法]]: [对比]
```

### 模型页 (model)

```markdown
---
title: "模型名称"
type: model
tags: [标签]
created: 2026-04-13
updated: 2026-04-13
---

## 概述
[模型定义和应用场景]

## 建模方法
[建模技术和数学描述]

## 适用场景
[适用范围和限制]

## 相关论文
| 论文 | 年份 | 改进点 |
|------|------|--------|
| [[来源页]] | 2025 | [改进描述] |

## 与其他模型的关系
- [[相关模型]]: [关系描述]
```

### 实体页 (entity)

```markdown
---
title: "实体名称"
type: entity
entity_type: person | institution | tool
tags: [标签]
created: 2026-04-13
---

## 概述
[学者/机构/工具的简介]

## 主要研究方向
- [方向 1]
- [方向 2]

## 相关论文
| 论文 | 年份 | 角色 |
|------|------|------|
| [[来源页]] | 2025 | 第一作者/通讯作者 |
```

## 工作流

### Ingest（摄入）

当用户要求处理新的 PDF 来源时：

1. **读取来源**：使用 `tools/extract_metadata.py` 提取元数据，或直接读取 PDF 内容
2. **讨论要点**：与用户讨论关键发现和需要强调的内容
3. **创建来源页**：在 `sources/` 下为每篇或每批论文创建摘要页
4. **更新主题页**：检查 `topics/` 中是否有相关主题页需要更新或新建
5. **更新方法页**：检查 `methods/` 中是否有相关方法页需要更新或新建
6. **更新模型页**：检查 `models/` 中是否有相关模型页需要更新或新建
7. **更新实体页**：如有新的学者、机构、工具，创建或更新 `entities/` 页
8. **更新索引**：更新 `index.md`
9. **记录日志**：在 `log.md` 末尾追加一条记录

批量摄入时（如处理整个编号文件夹），每篇论文生成一个来源页，然后综合生成/更新主题、方法、模型页。

### Query（查询）

当用户提问时：

1. **读取索引**：先读 `index.md` 定位相关页面
2. **搜索页面**：使用 grep 或阅读相关页面获取信息
3. **综合回答**：综合多页信息，给出带引用的回答
4. **归档有价值的答案**：如果查询产生了有价值的综合分析，将其保存为新的 wiki 页面
5. **记录日志**：在 `log.md` 记录查询

### Lint（健康检查）

定期检查 Wiki 健康状况：

1. **查找矛盾**：不同页面之间是否有冲突的陈述
2. **更新过时内容**：新来源是否已经推翻或更新了旧结论
3. **发现孤儿页**：没有入链的页面
4. **补充缺失页面**：被多次提及但没有独立页面的概念
5. **补充交叉引用**：缺少 `[[wikilink]]` 的地方
6. **修复格式**：确保所有页面都有正确的 frontmatter

## 交叉引用约定

使用 Obsidian wikilink 格式：`[[page-name]]`，链接到 `wiki/{type}/page-name.md`。

跨目录引用使用相对路径：`[[../methods/nodal-analysis|Nodal Analysis]]`

## 标签体系

常用标签分类：

| 分类 | 标签示例 |
|------|----------|
| 设备 | converter, transformer, transmission-line, cable, mmc, vsc, lcc, ibg |
| 方法 | adc, nodal-analysis, state-space, model-order-reduction, average-value, fixed-admittance |
| 场景 | real-time, fpga, hardware-in-loop, cosimulation, emt-ts, harmonic-analysis |
| 领域 | converter-driven-stability, renewable-energy, hvdc, distribution-system, microgrid |
| 工具 | pscad, rtds, opal-rt, emtp, matlab |

## 索引和日志格式

### index.md

```markdown
# EMT Wiki 索引

> 自动生成，每次 ingest 更新。

## 概览
- 总来源数：X
- 主题页：X
- 方法页：X
- 模型页：X
- 实体页：X

## 主题 (Topics)
| 页面 | 摘要 | 来源数 |
|------|------|--------|
| [[topic-name]] | [一句话摘要] | X |

## 方法 (Methods)
| 页面 | 摘要 | 来源数 |
|------|------|--------|
| [[method-name]] | [一句话摘要] | X |

## 模型 (Models)
| 页面 | 摘要 | 来源数 |
|------|------|--------|
| [[model-name]] | [一句话摘要] | X |

## 实体 (Entities)
| 页面 | 摘要 | 论文数 |
|------|------|--------|
| [[entity-name]] | [一句话摘要] | X |

## 来源 (Sources)
按编号文件夹分组：

### EMT_Doc/01/
| 页面 | 年份 | 标题 |
|------|------|------|
| [[source-name]] | 2025 | [标题] |
```

### log.md

```markdown
# EMT Wiki 日志

> 追加式记录，永不修改。每条以 `## [日期] 类型 | 标题` 开头。

## [2026-04-13] init | Wiki 初始化
- 创建目录结构和 schema
- 提取全部 691 篇 PDF 元数据

## [2026-04-13] ingest | 文件夹 01 批量摄入
- 来源: EMT_Doc/01/ (21 篇论文)
- 创建来源页: 21
- 创建/更新主题页: X
- 创建/更新方法页: X
- 创建/更新模型页: X
```
