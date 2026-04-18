---
title: "Accelerated Sparse Matrix-Based Computation of Electromagnetic Transients"
type: source
authors: ['未知']
year: 2019
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Abusalah 等 - 2020 - Accelerated Sparse Matrix-Based Computation of Electromagnetic Transients.pdf"]
---

# Accelerated Sparse Matrix-Based Computation of Electromagnetic Transients

**作者**: 
**年份**: 2019
**来源**: `05/Abusalah 等 - 2020 - Accelerated Sparse Matrix-Based Computation of Electromagnetic Transients.pdf`

## 摘要

This paper is related to research on parallelization methods for the simulation of electro- magnetic transients (EMTs). It presents an automatic parallelization approach based on the solution of sparse matrices resulting from the formulation of network equations. Modiﬁed-augmented-nodal analysis is used to formulate network equations. The selected sparse matrix solver is parallelized and adapted to improve performance by pivot validity testing and partial refactorization. Refactorization is needed when dealing with varying topology networks and nonlinear models. The EMT solver employs a fully iterative method for nonlinear functions. Conventional computer CPU-based parallelization is achieved and does not require any user intervention for given arbitrary network topologies. The presented a

## 核心贡献


- 提出基于KLU的自动并行方法，利用块三角分解实现任意拓扑网络无干预并行计算
- 引入主元检验与部分重分解技术，显著降低变拓扑与非线性迭代时的矩阵更新耗时
- 实现多线程分布式内存架构，无缝衔接潮流计算与时域电磁暂态全迭代求解


## 使用的方法


- [[修正增广节点分析法|修正增广节点分析法]]
- [[块三角分解|块三角分解]]
- [[klu稀疏矩阵求解|KLU稀疏矩阵求解]]
- [[部分重分解|部分重分解]]
- [[主元有效性检验|主元有效性检验]]
- [[全迭代牛顿法|全迭代牛顿法]]
- [[cpu多线程并行|CPU多线程并行]]


## 涉及的模型


- [[非线性模型|非线性模型]]
- [[时变开关模型|时变开关模型]]
- [[变压器分接头模型|变压器分接头模型]]
- [[电力电子换流器|电力电子换流器]]
- [[风电机组模型|风电机组模型]]
- [[分布参数输电线路|分布参数输电线路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[稀疏矩阵求解|稀疏矩阵求解]]
- [[自动网络分解|自动网络分解]]
- [[离线仿真加速|离线仿真加速]]
- [[非线性迭代求解|非线性迭代求解]]
- [[大规模电网仿真|大规模电网仿真]]


## 主要发现


- 所提算法在含电力电子与风电的大规模真实电网中显著缩短电磁暂态仿真时间
- 部分重分解策略有效减少非线性迭代过程中的完整矩阵分解次数，提升计算效率
- 自动块三角分解成功识别分布参数线路解耦子网，实现多核CPU负载均衡加速



## 方法细节

### 方法概述

本文提出一种基于稀疏矩阵求解的电磁暂态(EMT)自动并行加速方法。首先采用修正增广节点分析法(MANA)构建网络方程Ax=b。通过块三角分解(BTF)自动识别由分布参数线路解耦的子网络块，实现无用户干预的拓扑划分。针对传统KLU求解器在变拓扑与非线性迭代中频繁全量重分解的瓶颈，引入主元有效性检验与部分重分解技术。主元检验通过设定容差阈值判断是否需更新主元，避免无效重分解；部分重分解则定位动态列（非线性/时变元件），仅对变化列进行局部LU更新，保留静态列的分解结果。结合OpenMP分布式线程内存架构与基于浮点运算量(NFPO)的负载均衡策略，将各子块分配至多核CPU并行求解，实现从潮流初始化到时域全迭代求解的无缝衔接。

### 数学公式


**公式1**: $$$Ax = b$$$

*网络方程组，A为系数矩阵，x为未知量向量，b为已知量与历史项向量，用于每个时间步求解。*


**公式2**: $$$A_{BTF} = P_R A P_C$$$

*块三角分解公式，通过行列置换矩阵将原矩阵转化为块对角形式以实现子网络自动解耦。*


**公式3**: $$$\epsilon_p a_{new} > a_{old}$$$

*主元有效性检验条件，当新主元变化超过容差时触发全量重分解，否则复用原有LU模式。*


**公式4**: $$$NFPO_i = \sum_{j=1}^{n} \left[ \sum_{m=1}^{j-1} (2L_{len}(m) + 3L_{len}(j) + 2U_{len}(j)) \right] + n$$$

*第i个矩阵块的浮点运算量估算公式，用于多线程负载均衡与任务打包分配。*


### 算法步骤

1. 初始化与符号分析：仿真启动时仅执行一次AMD近似最小度排序，确定矩阵非零元模式与行列置换矩阵，该过程不随时间步变化。

2. 首次数值分解：对BTF划分出的每个独立子块执行完整LU分解，计算初始下三角矩阵L_i与上三角矩阵U_i。

3. 主元有效性检验：当矩阵元素因开关动作或非线性迭代发生变化时，复用原有非零模式进行重分解。逐列检查主元，若满足容差条件则丢弃旧主元并重新选主元，转至完整分解；否则保留原主元继续计算。

4. 部分重分解：识别包含非线性/时变模型的动态列。LU分解进行至首个动态列时暂停，记录部分L^p与U^p。当动态参数更新后，直接从该列恢复分解计算，无需从头开始，大幅降低计算开销。

5. 前代与回代：利用更新后的L_i与U_i矩阵，通过前向代入与后向代入快速求解线性方程组，得到当前时间步的节点电压与支路电流。

6. 并行调度与执行：基于NFPO公式估算各子块计算量，按k_d = NFPO/N_C阈值将子块打包分配至可用CPU核心，通过OpenMP启动独立线程在分布式栈内存中并行求解，最小化线程等待与内存访问延迟。


### 关键参数

- **pivot_tolerance**: 1% (默认值，用于主元有效性检验)

- **integration_step_HQ_grid**: 50 µs

- **integration_step_T0_grid**: 10 µs

- **simulation_duration_HQ**: 1 s

- **simulation_duration_T0**: 2 s

- **load_balancing_metric**: NFPO (浮点运算量估算，优于NNZ)

- **parallel_framework**: OpenMP (分布式线程内存架构)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Hydro-Quebec实际大电网(HQ-grid) | 41815阶矩阵，217个子块，最大块2898阶。12核并行下SMPEMT2耗时31s，平均迭代2.0次/步。 | 较传统EMTP单核求解器(1048s)加速33.8倍，较标准KLU单核(1216s)加速39倍；单核并行加速比达9.2倍，12核后趋于饱和。 |

| 含风电与详细IGBT模型的T0-grid(DM) | 4703阶矩阵，28个子块，最大块573阶。12核并行下SMPEMT2耗时204s，平均迭代5.91次/步。 | 较EMTP(2580s)加速12.6倍，较标准KLU(4379s)加速21.5倍；单核并行加速比达6.9倍。 |

| 含风电与平均值模型的T0-grid(AVM) | 相同拓扑但采用AVM简化模型。8核并行下SMPEMT2耗时27s，平均迭代1.7次/步。 | 较EMTP(253s)加速9.4倍，较标准KLU(336s)加速12.4倍；单核并行加速比达4.7倍。 |



## 量化发现

- 在含大量非线性电力电子器件的真实电网中，部分重分解策略使完整矩阵分解次数显著减少，12核并行下最高实现39倍计算加速。
- 主元有效性检验将默认容差设为1%，利用电路方程对角占优特性，主元变更频率极低，避免了90%以上的无效全量重分解。
- 基于NFPO的负载均衡策略有效克服了最大子块尺寸限制，HQ-grid在12核后加速比趋于饱和（最大9.2倍），T0-grid在8核后受限于最大子块计算瓶颈。
- 所有测试场景下，SMPEMT2与基准EMTP求解器的电压/电流波形完全重合，数值误差为0%，验证了算法的数学严格等价性。


## 关键公式

### 网络方程组

$$$Ax = b$$$

*每个时间步求解节点电压与支路电流的核心线性系统，A随开关状态与非线性迭代动态更新。*

### 主元有效性检验判据

$$$\epsilon_p a_{new} > a_{old}$$$

*在矩阵元素变化时判断是否需要触发昂贵的完整LU重分解，是提升变拓扑仿真效率的关键。*

### 子块计算复杂度估算公式

$$$NFPO_i = \sum_{j=1}^{n} \left[ \sum_{m=1}^{j-1} (2L_{len}(m) + 3L_{len}(j) + 2U_{len}(j)) \right] + n$$$

*用于OpenMP多线程任务分配，根据各子块LU分解与前代回代的浮点运算量实现动态负载均衡。*



## 验证详情

- **验证方式**: 离线仿真对比验证（波形重叠度分析与计算耗时统计）
- **测试系统**: 实际大规模电网：Hydro-Quebec电网(HQ-grid，含23181个RLC支路、349台同步机)与含风电/电力电子的T0-grid（含10个风电场、190个受控开关）
- **仿真工具**: EMTP (基准求解器), 改进版KLU (SMPEMT1/SMPEMT2), OpenMP并行框架, Intel Xeon E5-2650 v4 (24核/32GB RAM)
- **验证结果**: 在两种真实电网测试中，改进算法在保持波形零误差的前提下，将1秒/2秒时域仿真时间从千秒级压缩至数十秒级，最高实现39倍加速，且全程无需人工干预网络分割或模型简化，验证了其在复杂变拓扑与非线性迭代场景下的鲁棒性与高效性。
