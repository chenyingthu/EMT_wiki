---
title: "路线 E: 混合仿真接口技术"
type: learning-path
tags: [learning-path, hybrid-simulation, co-simulation, interface]
difficulty: "★★★"
estimated-time: "3-4 周"
created: "2026-05-10"
---

# 路线 E: 混合仿真接口技术

**难度**: ★★★ | **预计时间**: 3-4 周 | **目标读者**: 系统仿真工程师

## 目标

掌握机电-电磁混合仿真的原理、接口技术和工程实现。完成本路线后，应能设计混合仿真方案，理解接口误差来源，并能解释 FDNE 在混合仿真中的作用。

## 先修要求

- 路线 A（EMT 基础）或同等知识
- 理解 EMT 和机电暂态的基本区别
- 基本电力系统分析知识

## 学习路径

### Step 1: 混合仿真概述

**页面**: [[electromechanical-electromagnetic-hybrid-simulation]]

理解混合仿真的基本概念：为什么需要混合仿真、域间变量如何转换、接口的基本时序。

**要点**:
- TSA → EMT 的相量→瞬时值转换
- EMT → TSA 的功率/阻抗等效回传
- 接口延迟的基本概念

---

### Step 2: EMT 数学基础（混合仿真视角）

**页面**: [[emt-mathematical-foundation]]

从混合仿真角度重新理解 DAE 求解：为什么电磁暂态需要 μs 级步长而机电暂态可以用 ms 级步长；刚性系统的本质。

---

### Step 3: 网络等值与接口技术

**页面**: [[network-equivalent]]

学习 FDNE 在混合仿真接口中的核心作用：把远端交流系统简化为等值导纳，保留宽频特性。

**要点**:
- Thevenin/Norton 等效在接口中的应用
- FDNE 的宽频建模原理
- Ward 等值与 FDNE 的对比

---

### Step 4: 多速率方法

**页面**: [[multirate-method]]

理解不同子系统使用不同步长的原理，这是混合仿真能否实用的关键。

**要点**:
- 多速率原理：快/慢子系统分区
- 接口插值技术（用于数据交换）
- 稳定性边界：接口延迟对仿真的影响

**补充**: [[interpolation-method]]（插值方法）

---

### Step 5: 频率相关网络等值

**页面**: [[fdne-model]]

深入学习 FDNE 的 EMT 实现：从频域采样数据到有理函数到时域递推。

**要点**:
- FDNE 的建模流程：频响 → VF 拟合 → 状态空间 → EMT 嵌入
- 无源性检查和强制
- 多端口 FDNE 的实现

**补充**: [[vector-fitting]]（矢量拟合）、[[passivity-enforcement]]（无源性强制）、[[wideband-modeling]]（宽频建模）

---

### Step 6: 模型降阶方法

**页面**: [[model-order-reduction]]

理解模型降阶在混合仿真中的应用：Kron 消去、Brune 综合、平衡截断。

---

### Step 7: 硬件在环与实时混合仿真

**页面**: [[hil-simulation]]

学习混合仿真在实时环境下的特殊问题：接口延迟补偿、I/O 同步、硬实时约束。

**要点**:
- 信号级 HIL vs 功率级 HIL
- 接口延迟对闭环稳定性的影响
- FDNE 在实时仿真中的实现约束

**补充**: [[real-time-simulation]]

---

### Step 8（可选）: 分网与并行

**页面**: [[multirate-and-network-partitioning]]

学习 MATE 等分网方法在大规模混合仿真中的应用。

**补充**: [[parallel-computing]]、[[multithreaded-parallel-computing]]

---

### Step 9（可选）: 动态相量接口

**页面**: [[dynamic-phasor]]

动态相量法作为 EMT-RMS 之间的一种中间表示，可作为混合仿真的接口桥梁。

**补充**: [[electromechanical-electromagnetic-hybrid]]

## 核心技术对比

| 接口方法 | 频率范围 | 精度 | 计算代价 | 适用场景 |
|---------|:-------:|:----:|:--------:|---------|
| 戴维南等效 | 工频附近 | 低 | 低 | 简单系统，远程网络 |
| FDNE | 宽频 | 高 | 中 | 精确宽频等值 |
| 动态相量接口 | 基波+指定谐波 | 中 | 中 | 含谐波场景 |
| 传输线解耦 | 取决于模型 | 高 | 低 | 地理上分散的系统 |
| MATE 分网 | 不限 | 高 | 中 | 大规模并行 |

## 验证方式

完成本路线后，应能：

1. **设计接口方案**：给定一个实际系统（如含 MMC-HVDC 的交直流电网），设计混合仿真的分区和接口方案
2. **评估接口误差**：分析接口延迟、插值误差和 FDNE 截断误差对仿真结果的影响
3. **选择等值方法**：根据研究需求（精度、频率范围、实时性）选择合适的接口等值方法
4. **解释无源性**：解释 FDNE 非无源性导致 EMT 发散的机制和强制方法

## 进阶方向

- 路线 [[D-power-electronics-mmc]] — MMC-HVDC 的混合仿真应用
- 路线 [[F-real-time-hil]] — 实时混合仿真
- 路线 [[H-model-order-reduction]] — 降阶方法

## 对应书稿章节

第四篇 解耦与混合仿真：Ch14（混合仿真接口）、Ch15（FDNE 等值）、Ch16（模型降阶）

## 关键来源论文

- Smart 等 (2009) — 混合仿真接口技术综述
- Liang 等 (2012) — FDNE 在混合仿真中的应用
- Kuffel 等 (1995) — 实时混合仿真实现
