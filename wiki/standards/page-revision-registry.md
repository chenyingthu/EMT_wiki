---
title: "页面修订登记表 (Page Revision Registry)"
type: reference
tags: [standards, revision, registry, ownership, protection]
created: "2026-05-09"
updated: "2026-05-09"
---

# 页面修订登记表 (Page Revision Registry)

本登记表记录已经按 `wiki/standards/page-revision-protocol.md` 完成修订、验证或保护的页面。后续 Agent 在领取 shard 前必须检查本表，避免重复修改或把已完成页面改坏。

## 状态定义

| 状态 | 含义 | 后续 Agent 是否可修改 |
|------|------|----------------------|
| `protected` | 页面已完成本轮修订并通过目标验证 | 默认不可修改，除非用户或协调者明确点名 |
| `batch-generated` | 页面通过批量脚本从Source自动生成 | 可修改，需要人工审查和完善 |
| `needs-review` | 页面已修订但仍有待核查项 | 可由协调者分配复审任务 |
| `in-progress` | 页面正在由某个 Agent 处理 | 不可并发修改 |

## 登记表

| 页面 | 类型 | 状态 | 责任Agent | 完成日期 | 验证证据 | 保护说明 |
|------|------|------|-----------|----------|----------|----------|
| wiki/methods/back-to-back-hvdc.md | method | protected | claude-code | 2026-05-09 | B/75, 补核心机制+方程 | 需加内容时重新开放 |
| wiki/methods/beerten-2012-mtdc-powerflow.md | method | protected | claude-code | 2026-05-09 | B/75, 补核心机制+方程 | 需加内容时重新开放 |
| wiki/methods/chb-dab.md | method | protected | claude-code | 2026-05-09 | B/75, 补核心机制+方程 | 需加内容时重新开放 |
| wiki/methods/dem.md | method | protected | claude-code | 2026-05-09 | B/65, 别名页保持短 | 缩写入口,保持简洁 |
| wiki/methods/yang-2018-dc-protection.md | method | protected | claude-code | 2026-05-09 | B/75, 补核心机制+方程 | 需加内容时重新开放 |
| wiki/entities/atp-emtp.md | entity | protected | claude-code | 2026-05-09 | A/95, 修正许可表述 | 工具描述已严谨化 |
| wiki/entities/cloudpss.md | entity | protected | claude-code | 2026-05-09 | A/85, 降级营销语言 | 需核查时重新开放 |
| wiki/entities/siemens.md | entity | protected | claude-code | 2026-05-09 | 降级强断言 | 需核查时重新开放 |
| wiki/entities/abb.md | entity | protected | claude-code | 2026-05-09 | 降级强断言 | 需核查时重新开放 |
| wiki/entities/psmodel.md | entity | protected | claude-code | 2026-05-09 | 降级营销语言 | 需核查时重新开放 |
| wiki/entities/tsinghua-university.md | entity | protected | claude-code | 2026-05-09 | 降级强断言 | 需核查时重新开放 |
| wiki/entities/china-epri.md | entity | protected | claude-code | 2026-05-09 | 降级'世界领先' | 需核查时重新开放 |
| wiki/entities/adpss.md | entity | protected | claude-code | 2026-05-09 | 降级强断言 | 需核查时重新开放 |
| wiki/entities/gole.md | entity | protected | claude-code | 2026-05-09 | 降级强断言(国际知名→学者,突破→贡献) | 需核查时重新开放 |
| wiki/entities/matlab-simulink.md | entity | protected | claude-code | 2026-05-09 | 降级强断言(核心角色→常用于) | 需核查时重新开放 |
| wiki/entities/adam-semlyen.md | entity | protected | claude-code | 2026-05-09 | 降级强断言(泰斗→学者) | 需核查时重新开放 |
| wiki/entities/ansys.md | entity | protected | claude-code | 2026-05-09 | 降级强断言(最权威→,金标准→参考) | 需核查时重新开放 |
| wiki/entities/bjorn-gustavsen.md | entity | protected | claude-code | 2026-05-09 | 降级强断言(技术突破→技术贡献) | 需核查时重新开放 |
| wiki/entities/cigre.md | entity | protected | claude-code | 2026-05-09 | 降级强断言(最重要→重要之一) | 需核查时重新开放 |
| wiki/entities/comsol.md | entity | protected | claude-code | 2026-05-09 | 降级强断言(全球领先→,核心角色→用于) | 需核查时重新开放 |
| wiki/entities/emtp.md | entity | protected | claude-code | 2026-05-09 | 降级强断言(最经典→经典) | 需核查时重新开放 |
| wiki/entities/ieee.md | entity | protected | claude-code | 2026-05-09 | 降级强断言(核心引领→,最具影响力→主要) | 需核查时重新开放 |
| wiki/entities/polytechnique-montreal.md | entity | protected | claude-code | 2026-05-09 | 降级强断言(国际领先→有研究成果) | 需核查时重新开放 |
| wiki/entities/university-manitoba.md | entity | protected | claude-code | 2026-05-09 | 降级强断言(最广泛→主要,奠基性→有持续研究) | 需核查时重新开放 |
| wiki/entities/mahseredjian.md | entity | protected | claude-code | 2026-05-09 | 降级强断言(突出贡献→研究贡献) | 需核查时重新开放 |
| wiki/entities/rtds.md | entity | protected | claude-code | 2026-05-09 | 降级强断言(广泛使用→用于) | 需核查时重新开放 |
| wiki/methods/exponential-integrator.md | method | protected | claude-code | 2026-05-10 | A/87, 新创建补充书稿缺口 | 新页面 |
| wiki/methods/corona-effect-modeling.md | method | protected | claude-code | 2026-05-10 | A/87, 新创建补充书稿缺口 | 新页面 |
| wiki/methods/jiles-atherton-model.md | method | protected | claude-code | 2026-05-10 | A/87, 新创建补充书稿缺口 | 新页面 |
| wiki/methods/parallel-in-time.md | method | protected | claude-code | 2026-05-10 | A/87, 新创建补充书稿缺口 | 新页面 |
| wiki/methods/low-rank-solver.md | method | protected | claude-code | 2026-05-10 | A/87, 新创建补充书稿缺口 | 新页面 |
| wiki/methods/runge-kutta-in-emt.md | method | protected | claude-code | 2026-05-10 | A/87, 新创建补充书稿缺口 | 新页面 |
