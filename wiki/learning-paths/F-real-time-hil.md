---
title: "路线 F: 实时仿真与硬件在环"
type: learning-path
tags: [learning-path, real-time, hil, fpga, hardware]
difficulty: "★★☆"
estimated-time: "3-4 周"
created: "2026-05-10"
---

# 路线 F: 实时仿真与硬件在环

**难度**: ★★☆ | **预计时间**: 3-4 周 | **目标读者**: 实时仿真工程师

## 目标

掌握实时 EMT 仿真和硬件在环（HIL）仿真的核心技术。完成本路线后，应能理解实时仿真的约束（步长 deadline、通信延迟、I/O 同步），能解释 CPU-FPGA 协同仿真架构，并能设计 HIL 测试方案。

## 先修要求

- 路线 A（EMT 基础）或同等知识
- 基本的 EMT 求解流程理解
- 不要求硬件编程经验，但需要理解并行计算基本概念

## 学习路径

### Step 1: EMT 基础回顾（实时视角）

**页面**: [[emt-mathematical-foundation]]

从实时仿真角度重新审视 EMT 求解流程：一个时间步内的计算必须在固定时间内完成。

**要点**:
- 实时仿真与离线仿真的本质区别
- 固定步长 vs 变步长的实时约束
- 硬实时 vs 软实时的概念

---

### Step 2: 节点方程的高效求解

**页面**: [[nodal-analysis]]

理解节点分析法的计算瓶颈：LU 分解、前代回代。这是实时仿真优化的核心目标。

**要点**:
- 导纳矩阵的稀疏性利用
- 矩阵分解的计算复杂度
- 拓扑不变时的矩阵复用

**补充**: [[companion-circuit]]（伴随电路的高效实现）

---

### Step 3: 实时仿真概述

**页面**: [[real-time-simulation]]

系统学习实时 EMT 仿真的基本架构、平台对比和关键技术。

**要点**:
- 典型的实时仿真器架构（RTDS、HYPERSIM、eMEGASIM）
- 实时仿真的时间约束：计算时间 < 步长
- 任务调度：通信点、同步机制
- 多核/多处理器的负载均衡

---

### Step 4: 并行 EMT 计算

**页面**: [[parallel-computing]]

学习 EMT 仿真的并行化策略，这是实时仿真的核心技术。

**要点**:
- MATE（多区域戴维南等效）分网原理
- 传输线解耦：利用波传播时延自然分区
- 多线程并行：任务级并行与数据级并行
- 分布式并行处理器的通信拓扑

**补充**: [[multithreaded-parallel-computing]]、[[parallel-in-time]]

---

### Step 5: FPGA 加速仿真

**页面**: [[fpga-real-time-simulation]]

学习 FPGA 在实时仿真中的应用：小步长、高精度、低延迟。

**要点**:
- FPGA 与 CPU 的架构差异
- FPGA 侧的实现：管线化、并行化的求解器
- CPU-FPGA 协同仿真架构与通信
- 适用于 FPGA 的模型类型（MMC 子模块、LCC 阀组）

---

### Step 6: 硬件在环仿真

**页面**: [[hil-simulation]]

系统学习 HIL 仿真的原理、方案设计和注意事项。

**要点**:
- 信号级 HIL（Controller HIL）vs 功率级 HIL（Power HIL）
- 接口延迟对闭环稳定性的影响
- 延迟补偿方法（插值、外推、预测）
- I/O 接口的量化误差和时序抖动

---

### Step 7: 功率硬件在环

**页面**: [[hil-simulation]]

学习 PHIL 的进阶问题：功率接口、稳定性补偿和故障保护。

**要点**:
- 功率接口的理想变压器模型（ITM）
- 接口延迟导致的稳定性边界
- 阻尼阻抗法（DIM）等补偿技术
- 故障保护和紧急停机机制

---

### Step 8（可选）: 混合实时仿真

学习在实时环境下运行 EMT-TSA 混合仿真的特殊技术。

**补充**: [[electromechanical-electromagnetic-hybrid-simulation]]、[[fdne-model]]、[[multirate-method]]

## 核心概念对比

| 概念 | CPU 离线 | CPU 实时 | FPGA 实时 |
|------|:--------:|:--------:|:--------:|
| 步长 | 10-100 μs（受精度约束） | 30-50 μs | 0.5-5 μs |
| 求解方式 | 串行/并行 | 并行 | 硬件管线化 |
| 灵活性 | 高（任意模型） | 中（模型需适配） | 低（需硬件描述） |
| 瓶颈 | 仿真时间 | 计算 < 步长 | 硬件资源 |
| 典型平台 | PSCAD/EMTP | RTDS/HYPERSIM | OPAL-RT/NI |

## 验证方式

完成本路线后，应能：

1. **分析实时约束**：给定一个系统，估算其 EMT 实时仿真的最小可行步长
2. **设计并行方案**：为一个大系统设计 MATE 分网方案，考虑通信代价和负载均衡
3. **评估接口延迟**：分析 HIL 接口延迟对仿真闭环稳定性的影响
4. **选择实现平台**：根据步长、规模和 I/O 需求选择 CPU/FPGA 实现方案

## 进阶方向

- 主题 [[parallel-computing]] — 并行计算深化
- 路线 [[E-hybrid-simulation]] — 混合实时仿真
- 主题 [[wideband-oscillation-stability]] — 实时振荡分析

## 对应书稿章节

第四篇 解耦与混合仿真 + 第五篇 实时仿真：Ch17（并行求解）、Ch18（HIL 仿真）

## 关键来源论文

- Kuffel 等 (1995) — RTDS 实时仿真器
- Dufour 等 (2008) — HYPERSIM 实时仿真
- Ouquelle 等 (2009) — PHIL 接口技术
- Ren 等 (2017) — FPGA 实时仿真