# EMT Wiki 全面修订工作计划

## 工作体系概览

五阶段闭环：问题定位 → 工作计划 → 问题修订 → 工作记录 → 进展提交

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  1.问题定位  │ → │  2.工作计划  │ → │  3.问题修订  │ → │  4.工作记录  │ → │  5.进展提交  │
│  (诊断扫描)  │    │  (任务分片)  │    │  (执行修改)  │    │  (状态登记)  │    │  (验证归档)  │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
       ↑                                                                            ↓
       └──────────────────────────── 下一轮迭代 ←────────────────────────────────────┘
```

---

## 第一阶段：问题定位（诊断扫描）

### 1.1 自动化诊断脚本

**扫描维度：**
- 质量等级分布（A/B/C/D）
- 结构性缺失（定义、机制、边界、来源）
- 证据问题（强断言、无来源数字）
- 网络问题（断链、重复概念）
- 格式问题（破表、frontmatter错误）

**输出文件：**
```
reports/diagnostic-reports/
├── diagnostic-YYYY-MM-DD.json          # 完整诊断数据
├── priority-queue-high.json            # 高优先级任务
├── priority-queue-medium.json          # 中优先级任务
├── priority-queue-low.json             # 低优先级任务
└── issue-summary.md                    # 人工可读摘要
```

### 1.2 诊断执行命令

```bash
python3 tools/diagnostic_scan.py --full
```

**诊断报告内容：**
```json
{
  "scan_date": "2026-01-20",
  "total_pages": 1386,
  "grade_distribution": {"A": 1019, "B": 115, "C": 0, "D": 0},
  "issues": {
    "structural": [...],      // 结构缺失
    "evidence": [...],        // 证据问题
    "network": [...],         // 网络问题
    "format": [...]           // 格式问题
  },
  "priority_queue": {
    "high": [...],            // 影响>10页面的问题
    "medium": [...],          // 影响5-10页面
    "low": [...]              // 影响<5页面
  }
}
```

---

## 第二阶段：工作计划（任务分片）

### 2.1 分片策略

**分片维度（互斥且完备）：**

| 分片类型 | 说明 | 典型大小 |
|---------|------|---------|
| 按质量等级 | D级→C级→B级→A级 | 每批20-50页 |
| 按页面类型 | source/topic/method/model/entity | 每类一批 |
| 按主题簇 | MMC/VSC/FDNE/VectorFitting等 | 每簇5-15页 |
| 按目录范围 | methods/a-c*.md | 每批10-20页 |
| 按影响范围 | 高引用页面优先 | 每批5-10页 |

### 2.2 任务队列管理

**任务状态：**
- `pending`: 待分配
- `assigned`: 已分配给Agent
- `in-progress`: 正在修改
- `completed`: 已完成待验证
- `verified`: 已验证通过
- `blocked`: 阻塞（需人工决策）

**任务文件：**
```
plans/task-registry.json
```

**任务记录格式：**
```json
{
  "task_id": "wave-03-method-mmc",
  "shard_type": "topic-cluster",
  "pages": ["mmc-model.md", "avm-model.md", ...],
  "assigned_to": "agent-alpha",
  "status": "in-progress",
  "created": "2026-01-20",
  "started": "2026-01-20T10:00:00",
  "deadline": "2026-01-20T18:00:00",
  "dependencies": ["wave-02-source-mmc"],
  "expected_outcomes": ["add-boundary", "cleanup-assertions"]
}
```

### 2.3 工作波次规划

**Wave 1: 基础修复（第1-3天）**
- D级页面结构补全
- 破损表格修复
- 明显断链修复

**Wave 2: Method页清理（第4-7天）**
- 按主题簇分片（MMC/VSC/FDNE等）
- 降级强断言
- 补边界与失败模式

**Wave 3: Model页清理（第8-11天）**
- 设备建模层级统一
- 验证标准明确化

**Wave 4: Topic页清理（第12-14天）**
- 研究趋势综合
- 开放问题整理

**Wave 5: Entity/Tool页严谨化（第15-17天）**
- 工具版本/许可核查
- 能力边界明确

**Wave 6: 网络一致性回收（第18-20天）**
- 术语统一
- 概念边界清晰化
- 索引更新

---

## 第三阶段：问题修订（执行修改）

### 3.1 修订执行流程

**Agent执行步骤：**

1. **前置检查**
   ```bash
   python3 tools/check_page_status.py <page_path>
   # 检查：是否protected、是否有依赖未完成
   ```

2. **证据采样**
   - 读取目标页面
   - 读取3-8个代表性source页
   - 检查相邻页面定义

3. **诊断标记**
   - 标记结构缺失
   - 标记证据问题
   - 标记网络问题

4. **编辑执行**
   - 按page-revision-protocol.md执行
   - 小步提交（每页独立commit）

5. **自检**
   - 运行audit检查
   - 检查新增问题

6. **状态更新**
   - 更新page-revision-registry.md
   - 更新task-registry.json

### 3.2 修订脚本工具

```bash
# 单页修订
python3 tools/revise_page.py <page_path> --checklist <checklist_type>

# 批量修订（一批shard）
python3 tools/revise_shard.py --task-id <task_id>

# 自动修复常见问题
python3 tools/auto_fix.py --issue-type <type> --scope <shard>
```

---

## 第四阶段：工作记录（状态登记）

### 4.1 页面修订登记系统

**文件位置：**
```
wiki/standards/page-revision-registry.md
```

**登记格式：**
```markdown
| 页面 | 类型 | 状态 | 责任Agent | 完成日期 | 验证证据 | 保护说明 |
|------|------|------|-----------|----------|----------|----------|
| wiki/methods/vector-fitting.md | method | protected | agent-alpha | 2026-01-20 | A/85 | 术语统一审查前只读 |
| wiki/models/mmc-model.md | model | in-progress | agent-beta | - | - | Wave 2进行中 |
| wiki/topics/co-simulation.md | topic | open | - | - | - | 待分配 |
```

**状态说明：**
- `open`: 可领取
- `assigned`: 已分配但未开始
- `in-progress`: 正在修改（锁定）
- `needs-review`: 待复审
- `protected`: 已保护（重大修改需协调者批准）

### 4.2 工作日志系统

**日志文件：**
```
wiki/log.md                    # 全局日志
plans/work-logs/               # 分片日志
├── wave-01-log.md
├── agent-alpha-log.md
└── ...
```

**日志格式：**
```markdown
## 2026-01-20 Wave 2 Method页清理

### 已完成
- vector-fitting.md: 降级3处强断言，补适用边界
- prony-analysis.md: 补公式变量解释，修wikilink

### 阻塞问题
- average-value-model.md: 与detailed-model边界冲突，需协调

### 下一步
- 继续处理FDNE主题簇
```

### 4.3 进度追踪仪表板

**文件：**
```
reports/progress-dashboard.json
reports/progress-dashboard.md     # 人工可读
```

**内容：**
```json
{
  "last_updated": "2026-01-20T12:00:00",
  "overall": {
    "total_pages": 1386,
    "A_grade": {"count": 1019, "target": 1200, "progress": 85},
    "B_grade": {"count": 115, "target": 150, "progress": 77},
    "protected": 45,
    "in_progress": 12,
    "open": 195
  },
  "current_wave": {
    "id": "wave-02",
    "name": "Method页清理",
    "progress": 65,
    "completed_tasks": 13,
    "total_tasks": 20
  }
}
```

---

## 第五阶段：进展提交（验证归档）

### 5.1 提交前验证

**每个shard完成后必须运行：**
```bash
# 1. 单元测试
pytest tests/test_wiki_tools.py -v

# 2. 严格审计
python3 tools/audit_wiki_strict.py --output reports/strict-audit-post.json
diff reports/strict-audit-pre.json reports/strict-audit-post.json

# 3. 质量审计
python3 tools/audit_wiki_quality.py --output reports/quality-audit-post.json

# 4. 链接检查
python3 tools/check_broken_links.py

# 5. Git检查
git diff --stat
git diff --check  # 检查空白错误
```

### 5.2 提交物清单

**必须提交：**
1. 修改的页面文件
2. page-revision-registry.md更新
3. task-registry.json状态更新
4. work-log.md记录
5. 验证报告（audit结果对比）

**可选提交：**
- 诊断报告（如发现问题）
- 概念冲突报告（如存在）

### 5.3 归档流程

```bash
# 1. 创建提交包
python3 tools/prepare_submission.py --task-id <task_id>

# 2. 本地验证
python3 tools/validate_submission.py --package <package_path>

# 3. 提交（由协调者执行）
git add -A
git commit -m "wave-02: 清理15个Method页，降级23处强断言

- vector-fitting.md: 补边界，修wikilink
- prony-analysis.md: 补公式解释
- ...

验证: strict audit无新增blocker
Coordinated-by: revision-coordinator"

# 4. 标记完成
python3 tools/mark_task_complete.py --task-id <task_id>
```

---

## Loop流程设计

### 主循环逻辑

```python
# pseudo-code for loop workflow
def main_loop():
    while True:
        # Phase 1: 问题定位
        diagnostic = run_diagnostic_scan()
        if diagnostic['total_issues'] == 0:
            print("✓ 所有问题已解决，退出循环")
            break

        # Phase 2: 工作计划
        tasks = create_task_plan(diagnostic)
        if not tasks:
            print("! 无法创建任务，等待人工干预")
            break

        # Phase 3: 问题修订
        for task in tasks:
            result = execute_revision(task)
            if result['status'] == 'blocked':
                escalate_to_human(task, result)
                continue

            # Phase 4: 工作记录
            update_registry(task, result)
            update_work_log(task, result)

            # Phase 5: 进展提交
            submit_progress(task, result)

        # 更新进度仪表板
        update_dashboard()

        # 短暂休息后继续
        sleep(600)  # 10分钟
```

### Cron设置

```bash
# 每10分钟执行一轮
*/10 * * * * cd /home/chenying/researches/EMT_LLM_Wiki && python3 tools/revision_loop.py
```

---

## 风险控制与应急预案

### 风险1：循环陷入无限迭代

**预防：**
- 每轮必须有可量化的进展指标
- 连续3轮无进展自动暂停，请求人工决策

**检测：**
```python
if last_3_rounds_progress == 0:
    pause_loop()
    alert("连续3轮无进展，需要人工干预")
```

### 风险2：多Agent并发冲突

**预防：**
- 严格的页面锁定机制（in-progress状态）
- 分片互斥（每个页面只在一个shard中）

**检测：**
```bash
python3 tools/check_concurrent_conflicts.py
```

### 风险3：质量倒退

**预防：**
- 每轮后对比audit结果
- 禁止分数下降超过阈值

**检测：**
```bash
python3 tools/check_quality_regression.py
```

### 风险4：概念冲突扩散

**预防：**
- 相邻页面同时修改时必须声明
- 概念冲突标记为blocked，由协调者统一处理

---

## 成功标准

### 退出条件

**必须全部满足：**
1. C/D级页面数量为0
2. strict audit无blocker
3. 无未解决的强断言问题
4. 所有页面已登记保护状态
5. page-revision-registry.md完整

**可选目标：**
- A级页面 > 1100个
- 平均质量分数 > 80

---

## 工具清单

| 工具 | 用途 | 阶段 |
|------|------|------|
| diagnostic_scan.py | 全面诊断扫描 | 1 |
| create_task_plan.py | 任务分片规划 | 2 |
| assign_tasks.py | 任务分配 | 2 |
| revise_page.py | 单页修订 | 3 |
| revise_shard.py | 批量修订 | 3 |
| auto_fix.py | 自动修复 | 3 |
| update_registry.py | 更新登记 | 4 |
| prepare_submission.py | 提交包准备 | 5 |
| validate_submission.py | 提交验证 | 5 |
| check_quality_regression.py | 质量倒退检查 | 5 |
| revision_loop.py | 主循环 | All |
| progress_dashboard.py | 进度更新 | 4/5 |

---

## 执行检查清单

- [ ] 创建diagnostic_scan.py
- [ ] 创建task-registry.json
- [ ] 创建/更新page-revision-registry.md
- [ ] 创建revision_loop.py
- [ ] 创建progress_dashboard.py
- [ ] 设置cron任务
- [ ] 试运行第一轮验证流程
- [ ] 确认所有工具可用

---

*计划版本: v1.0*
*创建日期: 2026-01-20*
*协调者: revision-coordinator*
