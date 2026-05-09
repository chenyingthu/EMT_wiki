# EMT Wiki - Claude Code 配置

基于 [Karpathy LLM Wiki Pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 构建的电力系统电磁暂态（EMT）仿真领域知识库。

## 架构概览

```
EMT_LLM_Wiki/
├── EMT_Doc/              # Raw sources - 原始论文PDF（不可变）
│   ├── 01/, 02/, ...     # 按文件夹组织的699篇EMT论文
├── wiki/                 # The wiki - LLM生成的知识库
│   ├── index.md          # 内容索引（自动更新）
│   ├── overview.md       # EMT领域概览
│   ├── log.md            # 构建日志（按时间顺序）
│   ├── sources/          # 699篇来源页（每篇论文一个页面）
│   ├── topics/           # 90个主题页 → 9个二级分类（仿真、建模、稳定性、HVDC、保护、新能源、测试等）
│   ├── methods/          # 253个方法页 → 10个二级分类（数值方法、网络求解、输电线路、电力电子、控制、稳定性、信号处理、仿真技术、保护、系统分析）
│   ├── models/           # 87个模型页 → 11个二级分类（旋转电机、换流器、子模块、变压器、线路、新能源、保护、控制、补偿、等效、元件）
│   └── entities/         # 23个实体页 → 4个二级分类（机构、软件、企业、学者）
├── tools/                # CLI工具集
├── extracted_text/       # PDF提取的文本缓存
└── CLAUDE.md             # 本文件 - Schema配置
```

## 三层架构说明

### 1. Raw Sources（原始来源）
- **位置**: `EMT_Doc/` 文件夹（通过符号链接）
- **内容**: 699篇EMT领域学术论文PDF
- **规则**: 只读，永不修改。作为知识库的源头

### 2. The Wiki（知识库）
- **位置**: `wiki/` 目录
- **内容**: LLM生成的markdown文件
- **来源页结构**:
  ```yaml
  ---
  title: "论文标题"
  type: source
  year: 2024
  tags: [mmc, real-time, vector-fitting]
  sources: ["EMT_Doc/01/paper.pdf"]
  ---

  # 论文标题

  ## 摘要
  论文摘要内容

  ## 核心贡献
  - 贡献点1
  - 贡献点2

  ## 使用的方法
  - [[vector-fitting]]
  - [[real-time-simulation]]

  ## 涉及的模型
  - [[mmc-model]]

  ## 相关主题
  - [[co-simulation]]

  ## 主要发现
  研究发现总结

  <!-- deep-enrich:start -->
  ## 方法细节
  ...（LLM深度增强内容）
  <!-- deep-enrich:end -->
  ```

### 3. Schema（本文件）
- 定义wiki结构、命名约定和工作流
- 与Karpathy模式一致，LLM读取此文件理解如何维护wiki

## 命名约定

### Wiki链接格式
- **模型页**: `[[mmc-model]]`, `[[transformer-model]]`, `[[vsc-model]]`
- **方法页**: `[[vector-fitting]]`, `[[average-value-model]]`, `[[nodal-analysis]]`
- **主题页**: `[[co-simulation]]`, `[[real-time-simulation]]`, `[[dynamic-phasor]]`
- **实体页**: `[[pscad-emtdc]]`, `[[polytechnique-montreal]]`
- **来源页**: `[[smith-2024-mmc-modeling]]`

### 文件名约定
- 全部小写，空格用连字符替换
- 来源页: `作者-年份-短标题.md`
- 分类页: `名称-类别.md`（如 `mmc-model.md`）

## 工作流程

### 1. Ingest（摄入新论文）

当添加新PDF到 `EMT_Doc/` 时：

```bash
# Step 1: 提取PDF文本
python3 tools/extract_text.py EMT_Doc/XX/paper.pdf

# Step 2: 创建来源页
python3 tools/ingest_folder.py EMT_Doc/XX --folder-num XX

# Step 3: 规则分析（填充方法/模型/主题）
python3 tools/analyze_sources.py

# Step 4: 构建反向引用
python3 tools/build_backrefs.py

# Step 5: 深度增强（提取公式/算法/结果）
python3 tools/deep_enrich_sources.py --concurrency 8
```

**LLM任务**:
1. 读取PDF内容（通过extracted_text缓存）
2. 创建来源页，填写YAML frontmatter
3. 提取并写入：核心贡献、使用的方法、涉及的模型、相关主题、主要发现
4. 更新 `wiki/index.md` 添加新来源条目
5. 更新相关分类页（methods/, models/, topics/）添加反向引用
6. 在 `wiki/log.md` 追加摄入记录

### 2. Query（查询知识库）

用户提问时：

```
用户: "MMC模型有哪些最新进展？"

LLM:
1. 读取 wiki/index.md 找到相关页面
2. 读取 [[mmc-model]] 页面
3. 读取相关的来源页（如 [[zhang-2024-mmc-enhanced]], [[li-2023-mmc-realtime]]）
4. 综合答案，使用wikilink引用来源
5. （可选）将答案保存为新页面到 wiki/queries/
```

**答案格式**:
```markdown
## MMC模型最新进展

### 建模方法演进
- [[zhang-2024-mmc-enhanced]] 提出了改进的...
- [[li-2023-mmc-realtime]] 专注于实时仿真...

### 关键技术突破
...

### 来源
- [[mmc-model]]
- [[zhang-2024-mmc-enhanced]]
- [[li-2023-mmc-realtime]]
```

### 3. Lint（健康检查）

定期执行：

```bash
# 运行严格审计
python3 tools/strict_audit.py --output reports/wiki_strict_audit.json

# 深度增强低质量页面
python3 tools/deep_enrich_sources.py --retry-failed --concurrency 2
```

**检查项目**:
- 孤立页面（无入链）
- 断链（指向不存在的页面）
- 来源页缺少核心章节
- 量化发现中缺少数值证据
- 矛盾声明（同一主题不同结论）

## 工具参考

### 核心工具

| 工具 | 用途 | 示例 |
|------|------|------|
| `tools/ingest_folder.py` | 批量摄入PDF文件夹 | `python3 tools/ingest_folder.py EMT_Doc/01` |
| `tools/analyze_sources.py` | 规则分析填充分类 | `python3 tools/analyze_sources.py` |
| `tools/build_backrefs.py` | 构建分类页反向引用 | `python3 tools/build_backrefs.py` |
| `tools/deep_enrich_sources.py` | 深度增强来源页 | `python3 tools/deep_enrich_sources.py --concurrency 8` |
| `tools/strict_audit.py` | 严格质量审计 | `python3 tools/strict_audit.py` |

### 配置文件

- `.deep_enrich.json` - 深度增强检查点
- `.deep_review.json` - 深度审查记录
- `reports/wiki_strict_audit.json` - 严格审计报告

## 特殊文件格式

### 来源页深度增强标记

深度增强内容使用HTML注释标记：

```markdown
<!-- deep-enrich:start -->
## 方法细节
...
## 仿真结果
...
## 量化发现
...
## 关键公式
...
## 验证详情
...
## 适用边界
...
<!-- deep-enrich:end -->
```

**重要**: 重新生成时只替换标记内的内容，保留标记外的手动编辑。

### 量化发现要求

- 必须有数值证据（百分比、时间、误差等）
- 没有数值时必须写 "原文未报告可核验的数值结果"
- **禁止编造数字**

### 适用边界要求

- `valid_when`: 适用条件列表
- `invalid_when`: 失效边界列表
- `assumptions`: 关键假设（推断需标注"据方法推断"）
- `evidence_gaps`: 原文未给出的关键信息

## 分类体系

### 主题 (Topics)
- [[co-simulation]] - 混合仿真
- [[real-time-simulation]] - 实时仿真
- [[dynamic-phasor]] - 动态相量法
- [[parallel-computing]] - 并行计算
- [[frequency-dependent-modeling]] - 频率相关建模
- [[network-equivalent]] - 网络等值
- [[vsc-hvdc]] - VSC-HVDC
- [[ferroresonance]] - 铁磁谐振
- [[cable-modeling]] - 电缆建模
- [[harmonic-analysis]] - 谐波分析
- [[wind-farm-modeling]] - 风电场建模

### 方法 (Methods)
- [[vector-fitting]] - 矢量拟合
- [[average-value-model]] - 平均值模型
- [[nodal-analysis]] - 节点分析
- [[state-space-method]] - 状态空间法
- [[numerical-integration]] - 数值积分
- [[passivity-enforcement]] - 无源性强制
- [[multirate-method]] - 多速率方法
- [[fixed-admittance]] - 恒导纳模型
- [[interpolation-method]] - 插值方法
- [[prony-analysis]] - Prony分析

### 模型 (Models)
- [[mmc-model]] - MMC模型
- [[transmission-line-model]] - 输电线路模型
- [[transformer-model]] - 变压器模型
- [[synchronous-machine-model]] - 同步电机模型
- [[vsc-model]] - VSC模型
- [[fdne-model]] - FDNE模型
- [[cable-model]] - 电缆模型
- [[dfig-model]] - DFIG模型
- [[lcc-model]] - LCC模型
- [[pmsm-model]] - PMSM模型

## 用户提示词示例

### 摄入新论文
```
摄入 EMT_Doc/40/new_paper.pdf
- 提取元数据（标题、作者、年份）
- 创建来源页
- 分析使用的方法、模型、主题
- 更新index.md
```

### 查询知识库
```
查询: "矢量拟合算法在MMC建模中的应用"
- 搜索相关来源页
- 综合方法论和结果
- 生成带引用的回答
```

### 维护任务
```
运行lint检查:
1. 找出缺少深度增强章节的来源页
2. 检查孤立页面
3. 验证所有wikilink有效
4. 生成修复建议
```

## 集成说明

本项目使用Codex LLM进行深度增强（配置在 `~/.codex/config.toml`）。

LLM客户端配置在 `tools/llm_client.py`，支持:
- Codex (默认)
- OpenAI
- Anthropic

---

*基于 Karpathy LLM Wiki Pattern - 用于电力系统EMT仿真领域知识管理*
