---
title: "MMC宽频多尺度建模"
type: model
tags: [multiscale, mmc, wave-propagation-function, shifted-frequency-phasor, wide-frequency]
created: "2026-05-04"
updated: "2026-05-12"
---

# MMC宽频多尺度建模

## 定义与概述

MMC宽频多尺度建模是Ye (2021) 提出的基于波传播函数（Wave Propagation Function, WPF）和移频相量（Shifted Frequency Phasor, SFP）的MMC-HVDC系统建模方法。该方法可在同一仿真框架中处理从微秒级高频开关事件到秒级机电暂态的宽频带动态，避免传统方法需要在"全EMT高精度"和"平均值模型快但失真"之间二选一的困境。

## 核心原理

### 波传播函数（WPF）

用带上升时间的分段波形描述子模块输出电压在开通/关断过程中的传播行为，替代传统的二元电阻开关模型：

$$e_{sn}(t) = \begin{cases} \frac{t}{t_r}\sigma(t), & \text{if } t \leq t_r \\ \sigma(t), & \text{if } t > t_r \end{cases}$$

其中 $t_r$ 为IGBT开通/关断上升时间，$\sigma(t)$ 为单位阶跃函数。

### 移频相量（SFP）

将实信号构造为解析信号后乘以 $e^{-j\omega_s t}$ 将高频分量移至基带：

$$\underline{s}(t) = s(t) + j H[s(t)]$$
$$S[\underline{s}(t)] = \underline{s}(t) e^{-j\omega_s t}$$

- AC侧分量：$\omega_s = \omega_c$（载波频率移位）
- DC侧分量：$\omega_s = 0$（不移位）

### 多频率解耦策略

针对MMC拓扑的三个部分实施多频率解耦：
- AC系统：载波频率分量移位
- DC系统：基频/直流分量保持原频
- SM桥臂输出：多重频率移位

## 量化性能边界

**覆盖频带**：从微秒级的高频开关事件（EMT）到秒级的机电暂态（低频振荡）均可在同一仿真框架中处理（Ye 2021）。

**验证场景**：通过四类算例验证——直流故障、MMC内部子模块故障、功率振荡和风电功率波动，对比基线为全EMT模型（Ye 2021）。

**计算效率**：WPF减少子模块开关瞬态的详细二元电阻重组开销；SFP允许包络变量使用更大系统级时间步长。当前抽取文本未报告具体加速倍数。

**精度**：在功率振荡等低频段与全EMT模型具有高度一致性。MMC内部故障场景下，WPF方法相比AVM能捕捉SM级故障细节，相比DEM计算效率更高且无数值振荡（Ye 2021）。

**数据缺口声明**：Ye (2021) 原文前3页内容未给出可核验的误差百分比、CPU耗时、加速倍数或最大步长设置。不同多尺度建模方法在相同MMC-HVDC系统下的精度-效率对比缺乏统一基准。

## 适用边界

**适用条件**：
- MMC-HVDC系统宽频暂态仿真（同时含子模块开关瞬态、直流故障和系统级低频动态）
- 风电场经柔直并网的宽频交互分析
- 多时间尺度动态耦合场景

**失效边界**：
- 目标为器件级特性（IGBT损耗、驱动电路细节、真实开关波形尖峰）时需更详细模型
- 频谱严重混叠或非周期强扰动时移频相量的频带选择需重新校验

## 相关方法
- [[dynamic-phasor|动态相量]] - 移频分析理论基础
- [[shifted-frequency-analysis|移频分析]] - SFP方法基础
- [[numerical-integration|数值积分]] - 多尺度求解器

## 相关模型
- [[mmc-model|MMC模型]] - MMC通用建模框架
- [[fdne-model|频变网络等值]] - 外部网络宽频等值

## 来源论文

| 论文 | 年份 |
|------|------|
| [[wave-function-and-multiscale-modeling-of-mmc-hvdc-system-for-wide-frequency-tran|Wave Function and Multiscale Modeling of MMC-HVdc System for]] | 2021 |
## EMT中的作用

MMC宽频多尺度建模 在EMT仿真中主要用于：

- **建模对象**：描述MMC宽频多尺度建模在电力系统中的物理角色和电气特性
- **仿真场景**：适用于MMC宽频多尺度建模相关的电磁暂态分析、故障响应、控制交互等场景
- **模型接口**：提供MMC宽频多尺度建模的端口变量、状态方程和边界条件
- **验证基准**：可作为MMC宽频多尺度建模仿真模型正确性的验证基准

## 数学模型

### 基本方程

MMC宽频多尺度建模的数学模型基于以下基本物理定律：

$$
\text{待补充：基于MMC宽频多尺度建模的物理特性建立数学描述}
$$

### 状态空间表示

$$
\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u})
$$

$$
\mathbf{y} = \mathbf{g}(\mathbf{x}, \mathbf{u})
$$

其中 $\mathbf{x}$ 为状态向量，$\mathbf{u}$ 为输入向量，$\mathbf{y}$ 为输出向量。


*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*