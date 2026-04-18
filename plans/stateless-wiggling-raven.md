# EMT Wiki 深度增强计划 — 从条目式到百科全书

## Context

当前 Wiki 的 699 篇 source pages 已有高层级摘要（核心贡献/方法/模型/主题/发现各3-5条），但缺乏技术深度。topic/method/model pages 有论文列表和简单分析，但同样缺少公式、算法细节、仿真数据。用户希望 Wiki 成为"电磁暂态仿真大百科全书、研究参考的 Bible"——同时丰富单个论文页和分类汇总页的深度。

**关键发现**：
- 已有的 `extracted_text/markdown_enhanced/` 只包含每篇论文的引言部分（15-40%），无方法细节和结果
- 现有 source pages 只有条目式摘要，下钻后无深度内容
- topic/model pages 有技术演进脉络，但缺乏具体公式和算法描述
- 需要完整 PDF 解析 + LLM 深度提取才能获得公式、参数、仿真结果等

## 方案：两阶段深度增强

### Phase 1: Source Pages 深度增强（699篇）

**工具**: `tools/deep_enrich_sources.py`

**输入**: 完整 PDF（用 MinerU 或 pdftotext 提取全文）+ 已有的 enhanced markdown

**LLM Prompt 设计**（每篇论文一次 LLM 调用，并发8）:
```
你是一位电磁暂态(EMT)仿真领域的专家。请详细分析以下论文内容，
提取所有技术细节，输出 JSON 格式：

{
  "detailed_abstract": "300-500字的详细摘要，包含核心技术内容",
  "core_contributions": [
    {"title": "贡献1名称", "description": "详细描述，包含数学公式引用"},
    ...
  ],
  "methodology": {
    "approach": "整体方法描述",
    "equations": [
      {"label": "eq1", "latex": "数学公式LaTeX", "description": "公式含义"}
    ],
    "algorithm_steps": ["步骤1", "步骤2", ...],
    "parameters": {"参数名": "值/范围/说明"}
  },
  "models_details": {
    "model_name": "模型名称",
    "assumptions": ["假设1", ...],
    "structure": "结构描述",
    "parameters": "关键参数"
  },
  "simulation_results": [
    {"test_case": "测试场景", "metric": "指标", "value": "数值结果", "comparison": "对比基线"}
  ],
  "quantitative_findings": [
    "具体数值型发现1（如：仿真速度提升X倍，误差<Y%）",
    ...
  ],
  "key_equations": ["文中最重要的公式LaTeX"],
  "validation": {"method": "仿真/实验/对比", "details": "验证方式详情"}
}
```

**写入 source page 的新 sections**（在现有 sections 下方追加）:
```markdown
## 摘要（保留原样）
## 核心贡献（扩展现有条目为详细描述）
## 使用的方法（保留wikilinks）
## 涉及的模型（保留wikilinks）
## 相关主题（保留wiklins）
## 主要发现（扩展现有条目）
## 方法细节（新增）  ← 含公式、算法步骤、参数
## 仿真结果（新增）  ← 含测试场景、数值结果、对比数据
## 关键公式（新增）  ← 重要方程LaTeX展示
```

**Checkpoint**: `.deep_enrich.json` — 支持断点续传

### Phase 2: Taxonomy Pages 深度增强（40个topic/method/model/entity页）

**工具**: `tools/deep_enrich_taxonomy.py`

**输入**: Phase 1 产出的所有 source pages + 已有的 topic/model analysis JSON

**对每个 taxonomy page 的增强**:

#### Method Pages（如 fixed-admittance.md）追加：
```markdown
## 核心原理详解（扩展现有原理描述）
### 数学基础
- 固定导纳矩阵的推导过程
- 数值积分方法（后向欧拉/梯形）的导纳矩阵形式
### 算法流程
1. 步骤1...
### 参数选取指南
- 不同场景下的最优参数策略
## 性能分析（汇总所有使用此方法的论文的性能数据）
| 论文 | 仿真规模 | 速度提升 | 精度 | 验证方式 |
|------|---------|---------|------|---------|
## 最佳实践与注意事项
## 与其他方法的对比
```

#### Model Pages（如 mmc-model.md）追加：
```markdown
## 各类模型数学描述（扩展现有模型类型）
### 详细模型 — 子模块级
- 电路方程
- 开关函数描述
### 平均值模型(AVM)
- 平均化推导
- 适用频率范围
### 等效模型
- 戴维南/诺顿等效推导
- 误差分析
## 仿真参数参考表（汇总所有论文中的MMC参数）
| 论文 | 电平数 | 子模块数 | 电容值 | 仿真步长 | 平台 |
|------|-------|---------|-------|---------|------|
## 模型选择指南
- 不同场景下应选择哪种模型
- 精度vs效率权衡
## 前沿研究方向（汇总所有论文提出的开放问题）
```

#### Topic Pages（如 real-time-simulation.md）追加：
```markdown
## 关键技术详解
## 硬件平台对比（RTDS、OPAL-RT、FPGA等）
## 实际应用案例汇总
## 研究趋势与开放问题
```

### Phase 3: 验证与质量检查

1. 随机抽查20篇 source pages，确认公式/结果/算法描述完整
2. 抽查10个 taxonomy pages，确认深度内容聚合正确
3. 统计所有 wikilinks 有效性（不指向不存在的页面）
4. 更新 index.md 统计
5. 更新 log.md

## 执行流程

```bash
# Phase 1: 先 dry-run 5篇验证质量
~/anaconda3/bin/python3 tools/deep_enrich_sources.py --dry-run --limit 5

# Phase 1: 批量增强 699 篇 source pages（8线程并发）
~/anaconda3/bin/python3 tools/deep_enrich_sources.py --concurrency 8

# Phase 2: 增强 40 个 taxonomy pages
~/anaconda3/bin/python3 tools/deep_enrich_taxonomy.py

# Phase 3: 验证
~/anaconda3/bin/python3 tools/validate_deep_enrichment.py
```

## 预估时间

- Phase 1: 699 × LLM调用 (~15s/篇) ÷ 8并发 ≈ 25-30 分钟
- Phase 2: 40 × LLM调用 (~30s/页) ≈ 20 分钟
- Phase 3: 5 分钟
- **总计: 约 50-60 分钟**

## 关键文件

**读取**:
- `wiki/sources/*.md` — 699 篇 source pages
- `wiki/topics/*.md`, `wiki/methods/*.md`, `wiki/models/*.md` — 40 个 taxonomy pages
- `extracted_text/markdown_enhanced/*.md` — 已有 LLM 增强版引言
- `wiki/sources/metadata.json` — 论文元数据

**写入/修改**:
- `wiki/sources/*.md` — 追加深度 sections
- `wiki/topics/*.md` — 追加深度内容
- `wiki/methods/*.md` — 追加深度内容
- `wiki/models/*.md` — 追加深度内容

**新创建**:
- `tools/deep_enrich_sources.py` — Phase 1 工具
- `tools/deep_enrich_taxonomy.py` — Phase 2 工具
- `tools/validate_deep_enrichment.py` — Phase 3 工具

## 验证标准

1. ✅ 每篇 source page 至少包含 1-3 个 LaTeX 公式（如果原文有）
2. ✅ 每篇 source page 有具体的仿真结果数据（如果原文有）
3. ✅ method pages 有完整的数学推导和算法描述
4. ✅ model pages 有参数参考表和模型选择指南
5. ✅ topic pages 有技术趋势和开放问题汇总
6. ✅ 所有 wikilinks 有效
7. ✅ 无"待分析"类占位符
