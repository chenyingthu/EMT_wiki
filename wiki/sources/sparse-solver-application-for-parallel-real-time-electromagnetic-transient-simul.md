---
title: "Sparse solver application for parallel real-time electromagnetic transient simulations"
type: source
authors: ['B. Bruned']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109585. doi:10.1016/j.epsr.2023.109585"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/35/Bruned 等 - 2023 - Sparse solver application for parallel real-time electromagnetic transient simulations.pdf"]
---

# Sparse solver application for parallel real-time electromagnetic transient simulations

**作者**: B. Bruned
**年份**: 2023
**来源**: `35/Bruned 等 - 2023 - Sparse solver application for parallel real-time electromagnetic transient simulations.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Sparse solver application for parallel real-time electromagnetic B. Bruned a,*, J. Mahseredjian b, S. Denneti`ere a, A. Abusalah b, O. Saad c The main purpose of this research is to speed up real-time simulations of electromagnetic transients (EMTs) using sparse linear solver techniques. This paper presents the integration of a direct sparse linear solver (KLU) into a

## 核心贡献

- 设计了并行计算策略，加速大规模电网EMT仿真
- 实现了real-time仿真方法，满足硬件在环测试的实时性要求

## 使用的方法

- [[直接稀疏线性求解器-klu-mklu|直接稀疏线性求解器(KLU/MKLU)]]
- [[稀疏lu分解|稀疏LU分解]]
- [[网络并行求解|网络并行求解]]
- [[填充元减少技术|填充元减少技术]]
- [[部分重分解技术|部分重分解技术]]
- [[选主元技术|选主元技术]]
- [[节点分析法|节点分析法]]
- [[硬件在环仿真|硬件在环仿真]]
- [[补偿法|补偿法]]

## 涉及的模型

- [[实际电力系统网络模型|实际电力系统网络模型]]
- [[电力电子设备|电力电子设备]]
- [[可再生能源系统|可再生能源系统]]

## 相关主题

- [[parallel-computing]]
- [[real-time-simulation]]

## 主要发现

0378-7796/© 2023 Elsevier B

## 方法细节

### 方法概述

本文提出将改进的直接稀疏线性求解器MKLU（Modified KLU）集成到工业级实时仿真环境HYPERSIM中，替代传统的基于代码生成的GenCode求解器。核心策略包括：(1)采用填充元减少技术（AMD、COLAMD、Nested Dissection等排序算法）降低LU分解的非零元数量；(2)实现部分重分解技术（RefactChg和RefactVarOpt），在每个时间步仅重构矩阵中发生变化的列，避免完整重分解；(3)采用部分选主元（partial pivoting）策略确保数值稳定性；(4)结合两种并行化技术——基于传输线延迟的解耦（LD）和补偿法（CM）——实现大规模电网的并行实时求解。该方法专门针对电力系统电磁暂态（EMT）仿真中导纳矩阵稀疏、时变（由开关动作和非线性元件引起）的特点进行优化。

### 数学公式


**公式1**: $$$Y_n v_n = i_n$$$

*节点导纳矩阵方程，其中$Y_n$为网络导纳矩阵，$v_n$为节点电压向量，$i_n$为包含历史项注入的等效电流源向量*


**公式2**: $$$Y_n = L_n U_n$$$

*稀疏LU分解，将导纳矩阵分解为下三角矩阵$L_n$和上三角矩阵$U_n$的乘积*


**公式3**: $$$L_n x_n = i_n$$$

*前向代入过程，求解中间变量$x_n$*


**公式4**: $$$U_n v_n = x_n$$$

*后向代入过程，求解节点电压$v_n$*


**公式5**: $$$\tilde{Y}_n = P_n Y_n Q_n$$$

*矩阵重排序方程，$P_n$和$Q_n$为置换矩阵，用于减少LU分解过程中的填充元（fill-in）*


**公式6**: $$$Y_n = \begin{bmatrix} Y_f & Y_{fv} \\ Y_{vf} & Y_v \end{bmatrix}$$$

*矩阵分块形式，$Y_f$表示固定线性元件对应的导纳子矩阵，$Y_v$表示时变元件（开关、非线性元件）对应的导纳子矩阵，用于优化部分重分解*


### 算法步骤

1. 符号分析阶段：采用填充元减少排序算法（AMD、COLAMD或Nested Dissection）对导纳矩阵$Y_n$进行列置换，生成置换矩阵$P_n$和$Q_n$，将矩阵转换为边界块对角形式（bordered-block-diagonal form）以降低后续LU分解的计算复杂度

2. 初始数值分解：使用左看（left-looking）LU分解策略对排序后的矩阵进行完全分解，采用部分选主元（partial pivoting）策略，在每列中选择绝对值最大的元素作为主元，确保分解数值稳定性

3. 时间步迭代求解：在每个仿真时间步，首先执行前向代入$L_n x_n = i_n$求解中间变量，然后执行后向代入$U_n v_n = x_n$求解节点电压

4. 部分重分解（RefactChg）：检测导纳矩阵值发生变化的列，确定最小变化列索引$n_{chg}$，利用左看LU分解的特性，仅对从$n_{chg}$到矩阵维度$n$的列进行重构，保留$1$到$n_{chg}-1$列的原有分解结果

5. 优化部分重分解（RefactVarOpt）：先将网络节点按元件类型排序（线性元件节点在前，时变元件节点在后），形成分块矩阵$Y_n = \begin{bmatrix} Y_f & Y_{fv} \\ Y_{vf} & Y_v \end{bmatrix}$，然后仅对固定部分$Y_f$应用填充元减少排序，兼顾部分重分解效率和填充元优化

6. 主元有效性检验：在重分解前检查先前计算的主元是否仍然有效（是否接近零），若无效则触发完整重分解，避免因开关动作导致数值不稳定

7. 并行网络求解：采用传输线延迟（LD）技术将网络划分为多个子网络，各子网络独立求解；或采用补偿法（CM）实现无延迟的并行网络求解，通过子网络间的接口变量传递实现协调


### 关键参数

- **仿真步长**: 50μs（Case-1）和100μs（Case-2）

- **求解器类型**: MKLU（Modified KLU）直接稀疏求解器，基于左看（left-looking）LU分解

- **排序算法**: AMD（Approximate Minimum Degree）、COLAMD、Nested Dissection（使用Metis或Scotch图划分算法）

- **选主元策略**: Partial pivoting（部分选主元），在每列中选择绝对值最大元素作为主元

- **重分解策略**: RefactChg（基于变化列索引的部分重分解）和RefactVarOpt（基于变量类型排序的优化重分解）

- **并行化方法**: Line Delay（LD，传输线延迟解耦）和Compensation Method（CM，补偿法）

- **矩阵存储格式**: CSC（Compressed Sparse Column）格式



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Xavier配电网（Case-1） | 619节点大型线性配电网，仿真时长1秒，步长50μs，模拟单相接地故障。主要计算负担在于求解阶段（前向和后向代入），重构次数极少。采用补偿法（CM）进行并行加速。 | 相比传统GenCode求解器，MKLU结合填充元减少和部分重分解技术后，实时仿真性能提升显著 |

| GHOST微电网（Case-2） | 663节点微电网系统，仿真时长90秒，步长100μs，模拟电网故障导致的孤岛模式切换。同样采用补偿法（CM）并行化。 | 与基于代码生成且无选主元的GenCode求解器相比，MKLU在保持数值稳定性的同时实现了计算加速 |



## 量化发现

- 性能提升幅度：通过填充元减少（fill-in reduction）和部分重分解（partial refactorization）技术的结合应用，实时EMT仿真计算速度提升最高达50%
- 系统规模验证：在619节点（Xavier配电网）和663节点（GHOST微电网）的实际电力系统模型上验证了方法的有效性
- 数值稳定性：部分选主元（partial pivoting）技术对维持含开关动作（建模为$R_{open}/R_{close}$电阻）的电力系统仿真数值稳定性至关重要，而无选主元的GenCode求解器在此类情况下可能出现数值不稳定
- 部分重分解效率：RefactVarOpt方法通过将线性元件节点排序在前、时变元件节点排序在后，可将重分解限制在矩阵右下角的$Y_v$块，显著减少每时间步需要重构的列数（仅重构从$n_{chg}$到$n$的列）
- 计算时间分布：在测试案例中，主要计算负担集中于求解阶段（前向和后向代入），而非分解阶段，表明填充元减少对整体加速贡献显著
- 实时性要求：方法满足硬件在环（HIL）实时仿真的严格时序要求，在50μs和100μs步长下均能稳定运行


## 关键公式

### 节点导纳矩阵方程

$$$Y_n v_n = i_n$$$

*每个时间步需要求解的线性系统，$Y_n$为导纳矩阵，$v_n$为待求节点电压，$i_n$为等效电流源（包含历史项）*

### 填充元减少排序

$$$\tilde{Y}_n = P_n Y_n Q_n$$$

*在符号分析阶段应用，通过置换矩阵$P_n$和$Q_n$对原矩阵进行重排序，最小化LU分解过程中产生的填充元数量*

### 固定-时变分块矩阵

$$$Y_n = \begin{bmatrix} Y_f & Y_{fv} \\ Y_{vf} & Y_v \end{bmatrix}$$$

*用于RefactVarOpt部分重分解技术，将矩阵分为固定线性部分$Y_f$和时变部分$Y_v$，以最大化$n_{chg}$值，减少重分解计算量*



## 验证详情

- **验证方式**: 实时硬件在环（Hardware-In-the-Loop, HIL）仿真验证，对比分析
- **测试系统**: 两个实际电力系统案例：(1) Xavier配电网，619节点，含单相接地故障；(2) GHOST微电网，663节点，含孤岛模式切换
- **仿真工具**: HYPERSIM实时仿真环境（工业级EMT仿真平台），集成MKLU求解器替代原有GenCode求解器
- **验证结果**: MKLU求解器在HIL实时环境中成功替代传统GenCode求解器，首次实现工业级实时仿真环境中基于KLU的稀疏直接求解器集成。通过填充元减少和部分重分解技术实现高达50%的性能提升，同时通过部分选主元技术确保了含开关操作的复杂电网仿真的数值稳定性，解决了无选主元求解器在$R_{open}/R_{close}$开关建模场景下的数值不稳定问题。
