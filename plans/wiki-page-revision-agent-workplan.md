# EMT Wiki 页面润色、修复与并发 Agent 工作计划

## 1. 目标

本计划用于指导多个 Agent 并发修订 `wiki/` 下的 EMT 知识网络页面，使页面从“自动生成的条目集合”逐步提升为“学术性、可审核、术语一致、边界清晰的 EMT 研究知识网络”。

本计划不替代既有 schema，而是作为执行层协议。所有 Agent 必须同时遵守：

- `schema/WIKI.md`：页面类型、目录、frontmatter、wikilink 基本约定。
- `schema/QUALITY.md`：A/B/C/D 质量等级与质量红旗。
- `wiki/standards/terms-and-notation.md`：术语、符号、命名与表达规范。
- `wiki/standards/page-revision-registry.md`：已完成页面、责任 Agent、保护状态和验证证据。

本轮工作的核心不是让页面更长，而是让页面中的每个结论都能回答三个问题：

1. 它是什么类型的证据？
2. 它适用于什么对象、算例、工具、版本或边界？
3. 它和相邻页面的概念边界是什么？

## 2. 页面类型职责

### 2.1 Source 页面

`wiki/sources/*.md` 只回答“这篇论文做了什么”。

必须保留并区分：

- 论文明确报告的贡献、方法、模型、算例、指标。
- Agent 从论文内容中做出的解释性归纳。
- 该论文能够支撑哪些 topic/method/model/entity 页面。

禁止：

- 把单篇论文的算例结果写成领域共识。
- 把论文作者的主张改写成已经被社区普遍接受的结论。
- 删除原始来源路径、年份、作者、journal、deep-review/deep-enrich 标记。

### 2.2 Topic 页面

`wiki/topics/*.md` 是研究方向综合页，不是论文列表。

必须回答：

- 该主题是什么，不是什么。
- 它在 EMT 仿真中解决什么问题。
- 主要分支、机制、方法路线是什么。
- 代表性论文分别贡献了什么。
- 适用边界、失败边界和开放问题是什么。

### 2.3 Method 页面

`wiki/methods/*.md` 是算法、数值方法或技术路线页面。

必须回答：

- 输入、输出、状态变量、接口变量是什么。
- 核心公式或算法步骤是什么。
- 方法依赖哪些假设。
- 与相邻方法的区别是什么。
- 何时不应使用该方法。

### 2.4 Model 页面

`wiki/models/*.md` 是设备、组件或控制结构的 EMT 建模页面。

必须回答：

- 物理对象和 EMT 等效对象是什么。
- 状态变量、代数变量、控制变量和接口变量是什么。
- 有哪些建模层级，如详细开关模型、平均值模型、等效模型。
- 各层级在精度、速度、可实时性和适用场景上的取舍。
- 验证通常需要什么测试系统、工具、基准和指标。

### 2.5 Entity 页面

`wiki/entities/*.md` 是工具、机构、学者或组织页面。

工具页必须特别谨慎：

- 版本、许可、是否开源、是否原生支持某接口，必须有官方资料或降级表述。
- 论文中“使用了某工具”不等于“该工具验证了该方法的通用有效性”。
- 工具页的价值是说明其在 EMT 生态中的角色、典型入口、适用边界和证据使用规则。

### 2.6 Test-system 页面

`wiki/test-systems/*.md` 是标准算例或 benchmark 页面。

必须回答：

- 系统拓扑、额定值、设备构成、控制策略和故障/扰动设置。
- 哪些论文使用它，分别验证什么。
- 哪些结论只对该 benchmark 成立，不能外推。

## 3. 证据等级纪律

所有 Agent 修改页面时，必须在心里给每个关键句标注证据等级。必要时可在正文显式写出“作者报告”“该算例中”“多篇文献常见”等限定语。

| 等级 | 含义 | 推荐写法 | 禁止写法 |
|------|------|----------|----------|
| E1 原文事实 | 论文、手册、标准或元数据直接给出 | “作者报告……”“论文算例设置为……” | 改写成领域共识 |
| E2 页面内推理 | 从同一论文可合理推出 | “可理解为……”“这说明在该工况下……” | 写成原文直接结论 |
| E3 跨论文综合 | 多篇来源共同支撑的趋势、分类、共识 | “多篇文献中常见……”“代表性路线包括……” | 无来源地写“主流/最优/首选” |
| E4 开放判断 | 编辑风险、待验证方向、边界提醒 | “需要进一步核查……”“不应外推为……” | 写成已经实现的功能或能力 |

硬性规则：

- 不得把 E1 单篇论文结果提升为 E3 领域共识。
- 不得把 E2 推理写成 E1 原文事实。
- 不得把 E4 开放方向写成工具、模型或方法已经具备的能力。
- 任何数值指标必须绑定测试系统、工具、步长、基准、误差定义或论文来源。

## 4. 强断言处理规则

遇到以下表达必须审查：

- “首次”“首创”“突破”“完全”“彻底”“显著”“最优”“主流”“首选”
- “高精度”“高效率”“实时”“通用”“严格保证”“无缝”
- “误差 <x%”“提升 x 倍”“适用于所有”“无需代价”
- “开源”“免费”“官方”“兼容”“原生支持”

处理方式：

1. 有明确来源和条件：保留，但绑定论文、算例、指标、版本和适用范围。
2. 只有单篇论文声称：改为“作者报告在该算例中……”。
3. 没有来源：改为“常见用途”“研究方向”“可通过外部流程衔接”“需要核查”。
4. 工具、许可、版本相关：没有官方资料时，写“应以官方资料为准”。
5. 方法能力绝对化：补失败模式或适用边界。

示例：

- 不写：“该方法完全消除数值振荡。”
- 改写：“作者在该开关算例中报告该处理策略缓解了梯形积分数值振荡；是否适用于其他电路刚性和步长设置需要另行验证。”

- 不写：“ATP 原生支持 Python API。”
- 改写：“研究中可通过外部脚本生成输入文件、批量运行并解析输出，从而与 Python 数据分析流程衔接；是否存在官方 API 需查版本文档。”

## 5. 单页修订流程

每个 Agent 对每个页面按以下步骤执行。

### Step 1: 定位页面职责

先检查 `wiki/standards/page-revision-registry.md`。若页面已标记为 `protected`，普通 shard Agent 不得重写；若页面为 `in-progress`，不得并发编辑。

确认页面类型和职责。不要把 source 页面改成综述页，也不要把 taxonomy 页面改成论文摘要堆积。

### Step 2: 快速诊断

标记三类问题：

- 结构缺失：缺定义、机制、边界、代表性来源、相关页。
- 证据问题：强断言、无来源数字、论文结论外推、工具能力未核查。
- 网络问题：wikilink 不存在、概念重复、相邻页面边界冲突。

### Step 3: 证据采样

不要立刻全量读所有页面。

- 修 source 页：优先读该页本身、deep-review/deep-enrich 块和原始来源摘要。
- 修 topic/method/model 页：读取 3-8 个代表性 source 页，覆盖早期基础、典型改进和近期应用。
- 修 entity/tool 页：读取代表性来源页；涉及当前功能、许可、版本时，必须查官方资料或降级。
- 修短页：优先读取同名或相邻成熟页面作为风格参考。

### Step 4: 编辑策略

短页处理：

- 补“定义与边界”。
- 补“EMT 中的作用”。
- 补“核心机制”。
- 补“适用边界与失败模式”。
- 补少量代表性来源，不堆长表。

长页处理：

- 先修破损表格和重复条目。
- 压缩自动生成的重复“技术演进脉络”。
- 降级“首次/显著/最优/高精度”等强断言。
- 把论文列表整理成分类综合。
- 保留有用公式，但必须解释变量和作用。

自动生成块处理：

- 不盲删 deep-review/deep-enrich 标记。
- 可重组标记外的综合内容。
- 若必须改标记内内容，保持 marker 成对存在，不破坏工具跳过逻辑。

### Step 5: 交叉引用

- 只链接实际存在的页面。
- 每个链接要说明关系，例如“用于无源性后处理”“作为对比方法”“属于该模型的设备层级”。
- 相邻页面要写清边界，例如 `[[vector-fitting]]` 与 `[[prony-analysis]]`、`[[average-value-model]]` 与详细开关模型、`[[fdne-model]]` 与网络等值。

### Step 6: 自检

每个页面完成后，Agent 必须检查：

- 是否仍有无来源强断言。
- 是否有 “有效/良好/一致” 但缺少指标和场景。
- 是否有公式但没有变量解释。
- 是否把工具平台当成论文贡献。
- 是否新增不存在的 wikilink。
- 是否破坏 frontmatter、表格或 deep-review/deep-enrich marker。
- 是否已把完成状态、责任 Agent、验证证据写入 `wiki/standards/page-revision-registry.md`。

## 6. 推荐页面结构

Taxonomy 页面推荐使用以下结构。具体页面可按需要裁剪，但不应缺少定义、机制和边界。

```markdown
## 定义与边界
说明它是什么，不是什么。

## EMT 中的作用
说明它解决什么仿真问题。

## 核心机制
公式、算法、状态变量、接口变量或模型结构。

## 分类与变体
不同分支的区别和适用场景。

## 适用边界与失败模式
什么时候有效，什么时候容易失效。

## 代表性证据
用少量论文说明每类贡献，不堆长表。

## 与相关页面的关系
解释相邻方法、模型、主题的边界。

## 开放问题
只写真实未解决问题，不写宣传口号。
```

## 7. 并发 Agent 分片规则

### 7.1 分片方式

协调者每次只给 Agent 分配明确文件集合。推荐三种方式：

1. 按质量队列分片：从 `reports/wiki_quality_audit.md` 的 D/C 页中领取 5-20 个页面。
2. 按目录分片：如 `wiki/methods/a-c*.md` 或 `wiki/models/*converter*.md`。
3. 按主题簇分片：如 VF/FDNE/frequency-dependent-modeling 或 MMC/AVM/fixed-admittance。

### 7.2 文件所有权

Agent 只能修改自己 shard 内的页面。

开始修改前必须检查 `wiki/standards/page-revision-registry.md`：

- `protected` 页面默认不可修改，除非用户或协调者明确点名。
- `in-progress` 页面不得并发修改。
- `needs-review` 页面只能作为复审任务领取。
- `open` 页面可领取。

例外：

- 可以读取任意页面作为证据。
- 可以修复 shard 内页面中明显错误的 wikilink 文本。
- 不得顺手重写 shard 外页面。

### 7.3 禁止并发修改文件

以下文件由协调者统一更新，普通 shard Agent 不得修改：

- `wiki/index.md`
- `wiki/overview.md`
- `wiki/log.md`
- `reports/*`
- `.deep_enrich*.json`
- `.deep_review.json`
- 自动生成的审计 JSON
- backrefs 自动生成区

### 7.4 概念冲突处理

如果发现相邻页面定义冲突：

1. 当前页先采用保守定义。
2. 在交付报告中列出冲突页面、冲突句和建议处理方式。
3. 不在自己的 shard 中大范围重写其他页面。
4. 由协调者安排“概念合并/重命名/边界统一”任务。

### 7.5 页面保护登记

页面修订完成后，Agent 必须更新 `wiki/standards/page-revision-registry.md`：

| 字段 | 要求 |
|------|------|
| 页面 | 精确文件路径 |
| 类型 | source/topic/method/model/entity/test-system/standard/plan |
| 状态 | `protected`、`needs-review`、`in-progress` 或 `open` |
| 责任 Agent | Agent 名称或 shard 名称 |
| 完成日期 | YYYY-MM-DD |
| 验证证据 | quality/strict 分数、局部检查或人工 review |
| 保护说明 | 后续何时可以修改 |

未登记的页面不视为完成保护状态。

## 8. Agent 交付格式

每个 Agent 完成 shard 后必须提交以下信息：

```markdown
## Shard 完成报告

### 修改页面
- `wiki/...`

### 页面类型
- source/topic/method/model/entity/test-system

### 主要修订
- 补了哪些定义、机制、边界或代表性证据
- 删除或压缩了哪些重复/破损内容
- 降级了哪些强断言

### 证据使用
- 读取了哪些代表性来源页
- 哪些结论来自单篇论文
- 哪些结论是跨论文综合

### 剩余风险
- 需要官方资料核查的工具/版本/许可信息
- 需要人工确认的公式或数值
- 发现的概念冲突

### 验证
- 运行命令
- 结果摘要
```

## 9. 协调者工作流

协调者负责批量推进，不直接让所有 Agent 随意改全站。

### Phase 0: 建立任务队列

输入：

- `reports/wiki_quality_audit.md`
- `reports/wiki_strict_audit.md`
- `schema/QUALITY.md`

输出：

- D 级短页扩写队列。
- 长页强断言清理队列。
- 工具/实体页严谨化队列。
- 概念冲突/重复页面合并队列。

### Phase 1: D/C 页补结构

目标：

- 每个短页至少达到 B-level。
- 优先补定义、核心机制、边界、代表性来源。

推荐 shard：

- 5-10 个短 method 页。
- 3-8 个短 model 页。
- 3-5 个短 topic 页。

### Phase 2: 高影响长页清理

目标：

- 清理自动生成重复块、破表、强断言。
- 把“论文列表”压缩为“分类综合 + 代表性证据”。

优先对象：

- `wiki/methods/vector-fitting.md`
- `wiki/models/mmc-model.md`
- `wiki/topics/frequency-dependent-modeling.md`
- 其他质量分数不低但内容明显臃肿的页面。

### Phase 3: 工具/实体页严谨化

目标：

- 统一工具页证据纪律。
- 降级未核查的许可、版本、接口、功能主张。
- 增加“证据使用规则”和“适用边界”。

优先对象：

- `wiki/entities/atp-emtp.md`
- `wiki/entities/pscad-emtdc.md`
- `wiki/entities/emtp.md`
- `wiki/entities/rtds.md`
- `wiki/entities/cloudpss.md`
- `wiki/entities/matlab-simulink.md`

### Phase 4: 网络一致性回收

目标：

- 统一术语、符号、wikilink。
- 合并重复概念或写清边界。
- 更新索引和日志。

只有协调者执行：

- `tools/build_backrefs.py`
- `wiki/index.md`
- `wiki/log.md`

## 10. 验证门槛

### 10.1 单 Agent shard 验证

每个 shard 完成后至少运行：

```bash
python3 tools/audit_wiki_strict.py
python3 tools/audit_wiki_quality.py
```

如果只改少量 Markdown 且工具耗时过长，可由协调者集中运行；但 Agent 交付中必须说明未运行原因。

### 10.2 协调者批次验证

每个批次合并后运行：

```bash
pytest tests -q
python3 -m py_compile tools/*.py tests/test_wiki_tools.py
python3 tools/audit_wiki_strict.py
python3 tools/audit_wiki_quality.py
git diff --check
```

若准备提交，还需运行：

```bash
git diff --cached --check
```

### 10.3 通过标准

- strict audit 无新增 blocker。
- quality audit 中目标页面分数不下降，D/C 队列页面应提升。
- 无破损 frontmatter。
- 无新增明显不存在 wikilink。
- 无新增未绑定来源的强数字结论。
- deep-review/deep-enrich marker 成对存在。

## 11. 写作纪律

### 11.1 语言

- 使用简体中文。
- 首次出现术语使用“中文术语（English Term）”。
- 后续使用规范中文术语。
- 避免口号式、宣传式表达。

### 11.2 公式

- 公式必须解释变量。
- 公式必须说明作用：建模方程、接口方程、误差指标、算法步骤等。
- 不确定是否为原文公式时，写“典型形式”或“可写成”。

### 11.3 数值

数值结果必须包含至少三项上下文：

- 来源论文或算例。
- 测试系统/工具/工况。
- 指标定义和对照基准。

缺少上下文时，不写具体数值，或改为“作者报告有改善，但页面未保留足够参数复现该结论”。

### 11.4 表格

- 表格用于比较，不用于堆积无解释条目。
- 自动生成的长表可压缩为少量代表性行。
- 修复 `|----------||` 等破损表格。

### 11.5 删除与保留

优先删除：

- 重复段落。
- 破损自动表格。
- 无来源宣传语。
- 与页面职责无关的大段内容。

必须保留：

- frontmatter。
- 来源页 metadata 和 source 路径。
- deep-review/deep-enrich marker。
- 有证据价值的公式、参数、验证设置。

## 12. 本轮推荐起步任务

### Task A: 建立执行规范

- 将本计划作为后续 Agent 工作入口。
- 可选：把第 2-11 节拆出为 `wiki/standards/page-revision-protocol.md`，供所有 Agent 引用。

### Task B: 试点一组页面

选择 6-8 个页面试点：

- 1 个工具页：`wiki/entities/atp-emtp.md`
- 1 个长方法页：`wiki/methods/vector-fitting.md`
- 1 个长模型页：`wiki/models/mmc-model.md`
- 2 个 D 级短方法页：从 `reports/wiki_quality_audit.md` 选择
- 1 个 D/C 级短模型页：从 `reports/wiki_quality_audit.md` 选择
- 1 个 topic 页：从 `reports/wiki_quality_audit.md` 选择

试点目标不是全站覆盖，而是验证规范是否能让不同页面类型收敛到同一质量风格。

### Task C: 批量分片

试点通过后按目录和质量队列分片：

- Wave 1：D/C method 页。
- Wave 2：D/C model 页。
- Wave 3：D/C topic 页。
- Wave 4：entity/tool 页。
- Wave 5：高影响长页清理。

每个 wave 都必须有协调者做最终一致性回收。
