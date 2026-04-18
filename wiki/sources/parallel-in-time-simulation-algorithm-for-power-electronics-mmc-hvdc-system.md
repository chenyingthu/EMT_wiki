---
title: "Parallel-in-Time Simulation Algorithm for Power Electronics: MMC-HVdc System"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Journal of Emerging and Selected Topics in Power Electronics; ;PP;99;10.1109/JESTPE.2019.2947411"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/30/JESTPE.2019.2947411.pdf.pdf"]
---

# Parallel-in-Time Simulation Algorithm for Power Electronics: MMC-HVdc System

**作者**: 
**年份**: 2019
**来源**: `30/JESTPE.2019.2947411.pdf.pdf`

## 摘要

—The complexity in simulating power electron- ics like modular multilevel converters (MMCs) requires simulation algorithms to speed-up the process. Existing simulation algorithms exploit spatial parallelism to speed- up simulation. With rise in complexity of power electronics and presence of increased number of states within them, there are limits in the speed-up using spatial parallelism. In this paper, a temporal parallelism algorithm based on parallel-in-time methods is developed for simulation of power-electronics-systems. The temporal parallelism algorithm is based on computation of power-electronics- states on coarse and ﬁne time-steps using different models. The models of power-electronics-systems used in coarse and ﬁne time-steps are average-value and detailed models, respectively.

## 核心贡献


- 提出基于时间并行(MGRIT)的电磁暂态仿真算法，突破空间并行加速瓶颈
- 构建粗/细时间步状态转换方法，实现平均值与详细开关模型间的初值精确映射
- 设计双层迭代框架，粗步串行推进与细步并行计算结合，提升多状态系统仿真效率


## 使用的方法


- [[时间并行算法|时间并行算法]]
- [[多重网格时间缩减法-mgrit|多重网格时间缩减法(MGRIT)]]
- [[parareal算法|Parareal算法]]
- [[平均值模型|平均值模型]]
- [[详细开关模型|详细开关模型]]
- [[多时间步长迭代|多时间步长迭代]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[mmc-model|MMC]]
- [[电力电子系统|电力电子系统]]
- [[子模块-sm|子模块(SM)]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[时间并行仿真|时间并行仿真]]
- [[电力电子系统加速|电力电子系统加速]]
- [[多电平换流器建模|多电平换流器建模]]


## 主要发现


- 算法在5核并行下实现最高3.47倍加速，有效突破传统空间并行计算的性能瓶颈
- 所提状态转换方法能精确映射模型初值，仿真结果与详细参考模型高度吻合
- 时间并行框架显著降低含大量子模块MMC的电磁暂态仿真计算负担，保持数值稳定



## 方法细节

### 方法概述

本文提出基于多重网格时间缩减法(MGRIT)的并行时间仿真算法，用于解决MMC-HVdc等电力电子系统的电磁暂态仿真加速问题。算法采用双层时间步长架构：粗时间步(使用平均值模型)串行推进提供初始猜测，细时间步(使用详细开关模型)并行计算提供精度修正。通过提出的状态转换方法(Translation Method)实现粗/细模型间状态变量的双向映射，包括从粗状态初始化细状态以及基于细状态修正粗状态的迭代过程。该方法突破了传统空间并行方法受限于MMC臂数(6线程)的瓶颈，实现了时间维度上的并行加速。

### 数学公式


**公式1**: $$$\tilde{x}_{i}[k+1] = \mathcal{G}(\tilde{x}_{i}[k])$$$

*粗时间步状态更新方程，使用平均值模型(AVM)在粗时间步长T_coarse下串行计算，G表示粗算子*


**公式2**: $$$\hat{x}_{i}[k,j+1] = \mathcal{F}(\hat{x}_{i}[k,j])$$$

*细时间步状态更新方程，使用详细开关模型在细时间步长T_fine下并行计算，F表示细算子，j=0,...,Ns-1*


**公式3**: $$$x_{i}^{k} = \tilde{x}_{i}^{k} + A_{error}(\hat{x}_{i}^{k-1} - \tilde{x}_{i-1}^{k})$$$

*粗状态修正方程(Re-initialization)，利用第k-1次迭代细时间步计算结果与粗时间步的偏差修正当前粗状态，A_error为误差放大/修正矩阵*


**公式4**: $$$\hat{x}_{i}[k,0] = \mathcal{T}(\tilde{x}_{i-1}[k])$$$

*状态转换方程(Translation)，将前一次迭代(i-1)的粗时间步k状态转换为当前迭代细时间步的初始状态，T为转换算子*


### 算法步骤

1. 初始化(Initialization)：在仿真窗口内，使用平均值模型串行计算粗时间步状态序列$\tilde{x}_{i}[0], \tilde{x}_{i}[1], ..., \tilde{x}_{i}[N]$，建立初始时间轨线

2. 状态转换(Translation)：将粗时间步状态$\tilde{x}_{i-1}[k]$通过转换方法映射为细时间步初始状态$\hat{x}_{i}[k,0]$，实现平均值模型到详细模型的状态变量初始化

3. 细时间步并行计算(Fine Operation)：将仿真窗口划分为多个细时间步区间，分配给不同计算核心并行执行详细开关模型仿真，计算$\hat{x}_{i}[k,1]$到$\hat{x}_{i}[k,N_s-1]$

4. 粗状态修正(Re-initialization)：根据细时间步并行计算结果与粗时间步预测值的偏差，利用公式$x_{i}^{k} = \tilde{x}_{i}^{k} + A_{error}(\hat{x}_{i}^{k-1} - \tilde{x}_{i-1}^{k})$更新粗时间步状态

5. 收敛判断：检查修正后的粗状态与上一次迭代的差异，若未满足收敛准则则返回步骤2继续迭代，否则进入下一个仿真窗口


### 关键参数

- **T_coarse**: 粗时间步长，包含多个细时间步

- **T_fine**: 细时间步长，量级为微秒级(~μs)

- **N_s**: 每个粗时间步包含的细时间步数量(图示中为8)

- **A_error**: 误差修正矩阵/放大因子，用于加权修正项

- **N_cores**: 并行计算核心数(论文测试中使用5核)

- **Simulation_Window**: 包含多个粗时间步的仿真窗口(T_window)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| MMC-HVdc系统电磁暂态仿真 | 在包含大量子模块(~1000s)的MMC-HVdc系统上测试，使用5个计算核心并行，记录到最高3.47倍的加速比。仿真结果与详细参考模型在电压、电流波形上高度吻合，误差控制在可接受范围内 | 相比传统空间并行方法(受限于6线程)实现3.47倍加速，突破了空间并行的性能瓶颈 |



## 量化发现

- 使用5个计算核心并行时，算法实现最高3.47倍的加速比(speed-up)
- 细时间步长为微秒级(~μs)，以满足电力电子开关过程的仿真精度要求
- 每个MMC臂包含约1000个子模块状态，传统空间并行方法在每个臂内部只能串行计算
- 传统空间并行方法受限于MMC的6个臂结构，最多只能利用6线程并行
- 算法通过时间并行度弥补了空间并行度的不足，适用于含大量状态的电力电子系统


## 关键公式

### 粗状态修正方程(MGRIT更新公式)

$$$x_{i}^{k} = \tilde{x}_{i}^{k} + A_{error}(\hat{x}_{i}^{k-1} - \tilde{x}_{i-1}^{k})$$$

*在细时间步并行计算完成后，用于修正粗时间步状态，结合平均值模型的快速预测和详细模型的精确结果，通过迭代逼近真实解*

### 状态转换方程

$$$\hat{x}_{i}[k,0] = \mathcal{T}(\tilde{x}_{i-1}[k])$$$

*在粗细时间步模型间转换状态变量，确保详细模型在细时间步开始时获得与平均值模型一致的初始条件，反之亦然*



## 验证详情

- **验证方式**: 与详细参考模型(Detailed Reference Model)进行对比验证，通过比较波形吻合度验证算法精度
- **测试系统**: MMC-HVdc系统，包含大量子模块(SMs)的高电压直流输电系统
- **仿真工具**: 基于MGRIT框架开发的并行时间仿真算法实现，具体商业仿真软件未明确提及，但针对电磁暂态(EMT)仿真环境
- **验证结果**: 所提算法在保证与详细参考模型高度吻合的仿真精度的同时，实现了3.47倍的计算加速，验证了时间并行方法在电力电子系统仿真中的有效性和准确性
