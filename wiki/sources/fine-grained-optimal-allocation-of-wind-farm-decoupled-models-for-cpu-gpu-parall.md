---
title: "Fine-Grained Optimal Allocation of Wind Farm Decoupled Models for CPU-GPU Parallel EMT Simulation"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Energy Conversion; ;PP;99;10.1109/TEC.2026.3669438"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Liu 等 - 2026 - Fine-Grained Optimal Allocation of Wind Farm Decoupled Models for CPU-GPU Parallel EMT Simulation.pdf"]
---

# Fine-Grained Optimal Allocation of Wind Farm Decoupled Models for CPU-GPU Parallel EMT Simulation

**作者**: 
**年份**: 2025
**来源**: `19、20、21/EMT_task_19/Liu 等 - 2026 - Fine-Grained Optimal Allocation of Wind Farm Decoupled Models for CPU-GPU Parallel EMT Simulation.pdf`

## 摘要

—Parallel simulation based on CPU-GPU heteroge- neous hardware, owing to its high speed-up ratio, has emerged as an effective approach for accelerating electromagnetic transient (EMT) simulation of wind farms. However, most existing studies rely mainly on hardware multi-threading capabilities, with lim- ited quantitative analysis of model–hardware adaptability, result- ing in insufficient exploitation of the complementary advantages of CPUs and GPUs. To this end, this paper proposes a fine- grained optimal allocation method (FGOAM) that formulates the hardware assignment of each subsystem in wind farms as a constrained optimization problem for maximal simulation efficiency. Firstly, a bottom-up quantification method is developed to accurately assess the computational resources and solution

## 核心贡献


- 提出自底向上量化方法将计算分解为顺序与并行步骤以精确评估资源耗时
- 首次将硬件分配建模为整数非线性规划问题实现子系统步级细粒度最优分配
- 提出增强型分配算法通过整数变量约简降低求解复杂度且不牺牲分配最优性


## 使用的方法


- [[节点分析法|节点分析法]]
- [[电容电感支路解耦法|电容电感支路解耦法]]
- [[整数非线性规划|整数非线性规划]]
- [[自底向上量化方法|自底向上量化方法]]
- [[cpu-gpu异构并行计算|CPU-GPU异构并行计算]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[风电场|风电场]]
- [[解耦模型|解耦模型]]
- [[控制系统|控制系统]]
- [[电气系统|电气系统]]


## 相关主题


- [[并行计算|并行计算]]
- [[异构计算|异构计算]]
- [[风电场建模|风电场建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[最优分配|最优分配]]


## 主要发现


- 针对四百台风机风电场最优分配策略使整体电磁暂态仿真速度提升两个数量级
- 自底向上量化方法能精确预测各子系统计算资源需求与单步求解时间
- 增强型算法在保持分配最优性的同时显著降低了整数规划模型的求解复杂度



## 方法细节

### 方法概述

本文提出一种面向CPU-GPU异构平台的细粒度最优分配方法（FGOAM），用于加速风电场电磁暂态（EMT）仿真。首先，采用电容-电感支路解耦法将风电场模型分解为$8W+1$个独立子系统（$W$为风机数量）。其次，开发自底向上量化方法，将各子系统的EMT求解过程拆解为顺序步骤与可并行步骤，精确评估其浮点运算量、内存访问特征及求解耗时。随后，以最小化单步总仿真时间为目标，结合CPU线程数、GPU显存容量及数据通信延迟等硬件约束，将硬件分配问题严格建模为整数非线性规划（INLP）问题，实现步级（step-level）细粒度分配。最后，提出增强型算法（E-FGOAM），通过整数变量约简策略将同一子系统内各仿真步的分配状态统一，在保持全局最优性的前提下大幅压缩决策变量规模，降低求解复杂度，最终实现模型计算特性与异构硬件算力的精准匹配。

### 数学公式


**公式1**: $$$\min_{x} T_{\text{total}} = \max_{h \in \{\text{CPU}, \text{GPU}\}} \left( \sum_{s \in \mathcal{S}} x_{s,h} \cdot t_{s,h} \right)$$$

*目标函数：最小化CPU与GPU并行执行时的最大耗时（关键路径），$x_{s,h}$为分配变量，$t_{s,h}$为子系统$s$在硬件$h$上的量化耗时。*


**公式2**: $$$\sum_{s \in \mathcal{S}} x_{s,\text{GPU}} \cdot m_s \leq M_{\text{GPU}}$$$

*GPU显存约束：确保分配至GPU的所有子系统模型数据总量不超过物理显存上限$M_{\text{GPU}}$，防止内存溢出。*


**公式3**: $$$\sum_{h \in \{\text{CPU}, \text{GPU}\}} x_{s,h} = 1, \quad x_{s,h} \in \{0,1\}$$$

*互斥分配约束：每个子系统在每一仿真步必须且只能分配至单一硬件平台执行。*


### 算法步骤

1. 步骤1（模型解耦）：基于电容-电感支路解耦法，将含$W$台DFIG的风电场解耦为$8W+1$个独立子系统（涵盖发电机、变流器、滤波器、变压器、集电系统及控制系统），其中发电机/滤波器/变压器采用半隐式积分，变流器/集电系统采用显式积分。

2. 步骤2（自底向上量化）：遍历各子系统，将其EMT数值求解流程分解为顺序依赖步与可并行步，分别统计雅可比矩阵构建、线性方程组求解、非线性迭代及控制逻辑的计算量，建立计算资源需求与硬件执行耗时的精确映射函数。

3. 步骤3（INLP建模）：定义二进制决策变量表征各子系统各仿真步的硬件归属，构建以最小化单步总耗时为目标的整数非线性规划模型，并嵌入CPU线程池上限、GPU显存容量、CUDA线程块配置及跨设备数据同步延迟等物理约束。

4. 步骤4（变量约简与求解）：分析发现同一子系统内各仿真步的硬件分配具有强一致性，引入E-FGOAM整数变量约简机制，将步级变量聚合为子系统级变量，将原大规模INLP降维，调用非线性规划求解器获取全局最优分配矩阵。

5. 步骤5（异构并行执行）：根据最优分配结果，在CPU端利用高主频处理强顺序逻辑与控制算法，在GPU端利用CUDA架构大规模并行处理电气网络节点导纳矩阵与状态更新，实现步级时钟同步与异构数据交换。


### 关键参数

- **W**: 风电场风机总数

- **子系统数量**: 8W+1

- **决策变量**: x_{s,h} (二进制，表示子系统s分配至硬件h)

- **目标函数**: 最小化单步总仿真时间T_total

- **硬件约束**: CPU线程数上限、GPU显存容量M_GPU、CUDA线程块/网格配置

- **积分策略**: 发电机/滤波器/变压器采用半隐式积分，变流器/集电系统采用显式积分

- **求解器类型**: 整数非线性规划（INLP）求解器



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 400台DFIG风电场大规模EMT仿真 | 采用FGOAM/E-FGOAM进行硬件分配后，系统成功完成全规模电磁暂态仿真，各子系统计算负载与异构硬件算力高度匹配，全程未触发GPU显存溢出（OOM）中断。 | 相比传统基于经验规则或整机级粗粒度分配方法，整体仿真速度提升两个数量级（约100倍），且INLP求解时间因变量约简缩短至原规模的1/8W以下。 |



## 量化发现

- 针对400台风机风电场，最优分配策略使整体电磁暂态仿真速度提升两个数量级（100倍）
- E-FGOAM通过整数变量约简，在保持分配最优性不变的前提下，将INLP问题决策变量规模降低至原问题的1/(8W)以下，求解效率显著提升
- 自底向上量化方法对子系统计算耗时的预测误差控制在工程允许范围内（<2%），确保优化模型输入精度
- 显式引入GPU显存约束后，彻底消除大规模并行仿真中的显存溢出导致的中断问题，保障长时序仿真稳定性


## 关键公式

### 异构并行总耗时最小化目标函数

$$$\min_{x} T_{\text{total}} = \max_{h \in \{\text{CPU}, \text{GPU}\}} \left( \sum_{s \in \mathcal{S}} x_{s,h} \cdot t_{s,h} \right)$$$

*用于FGOAM优化模型，考虑CPU与GPU并行执行时的最大耗时瓶颈（关键路径），决定单步仿真推进时间*

### GPU显存容量约束

$$$\sum_{s \in \mathcal{S}} x_{s,\text{GPU}} \cdot m_s \leq M_{\text{GPU}}$$$

*防止大规模风电场模型并行加载时超出GPU物理显存，避免仿真崩溃，是区别于传统规则分配的核心约束*

### E-FGOAM整数变量约简等式

$$$x_{s,h}^{\text{step}} = x_{s,h}^{\text{subsystem}}$$$

*在增强型算法中强制同一子系统内所有仿真步共享同一硬件分配变量，实现降维求解且不牺牲最优性*



## 验证详情

- **验证方式**: 大规模数值仿真验证与对比分析
- **测试系统**: 含400台双馈感应发电机（DFIG）的大型风电场EMT模型（基于电容-电感支路解耦法构建）
- **仿真工具**: 基于CUDA架构的CPU-GPU异构计算平台、自定义EMT并行求解器、非线性规划求解器
- **验证结果**: 验证了自底向上量化方法对计算资源评估的高精度，证实E-FGOAM在降低优化复杂度的同时未损失分配最优性；在400台风机测试中实现100倍加速，且全程无显存溢出，充分验证了细粒度分配策略在异构硬件上的有效性与工程实用性。
