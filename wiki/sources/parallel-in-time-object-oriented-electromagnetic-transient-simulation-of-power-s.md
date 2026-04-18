---
title: "Parallel-in-Time Object-Oriented Electromagnetic Transient Simulation of Power Systems"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Open Access Journal of Power and Energy;2020;7; ;10.1109/OAJPE.2020.3012636"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/30/oajpe.2020.3012636.pdf.pdf"]
---

# Parallel-in-Time Object-Oriented Electromagnetic Transient Simulation of Power Systems

**作者**: 
**年份**: 2020
**来源**: `30/oajpe.2020.3012636.pdf.pdf`

## 摘要

Parallel-in-time methods are emerging to accelerate the solution of time-consuming problems in different research ﬁelds. However, the complexity of power system component models brings challenges to realize the parallel-in-time power system electromagnetic transient (EMT) simulation, including the traveling wave transmission lines. This paper proposes a system-level parallel-in-time EMT simulation method based on traditional nodal analysis and the Parareal algorithm. A new interpretation scheme is proposed to solve the transmission line convergence problem. To integrate different kinds of traditional EMT models, a component- based EMT system solver architecture is proposed to address the increasing model complexity. An object- oriented C++ implementation is proposed to realize the parallel

## 核心贡献


- 提出基于节点分析与Parareal算法的系统级并行电磁暂态仿真方法
- 设计改进插值策略解决行波传输线模型在并行计算中的收敛难题
- 构建组件化面向对象求解器架构实现传统EMT模型灵活集成


## 使用的方法


- [[parareal算法|Parareal算法]]
- [[节点分析法|节点分析法]]
- [[面向对象编程|面向对象编程]]
- [[改进插值策略|改进插值策略]]
- [[多核并行计算|多核并行计算]]


## 涉及的模型


- [[行波传输线模型|行波传输线模型]]
- [[贝杰龙模型|贝杰龙模型]]
- [[微分代数方程系统|微分代数方程系统]]
- [[延迟微分方程模型|延迟微分方程模型]]


## 相关主题


- [[时间并行计算|时间并行计算]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[多核并行加速|多核并行加速]]
- [[延迟微分方程求解|延迟微分方程求解]]
- [[组件化建模|组件化建模]]


## 主要发现


- IEEE-118系统测试表明六线程下加速比达2.30倍且并行效率约40%
- 系统时域特性决定Parareal算法加速效果传输线延迟显著影响性能
- 改进插值策略有效解决传输线收敛问题保持与传统串行算法同等精度



## 方法细节

### 方法概述

提出基于传统节点分析法(Nodal Analysis)与Parareal算法的系统级并行电磁暂态仿真框架。该方法将整体仿真时间域$[t_0, t_{end}]$分解为$N$个粗粒度子区间$I_k=[T_{j-1}, T_j]$，通过粗算子(Coarse Operator $G$)与细算子(Fine Operator $F$)的迭代校正实现时间并行。针对电力系统传输线行波模型引入的延迟微分方程(DDE)导致的收敛难题，提出改进插值策略(Modified Interpolation Scheme)处理历史项依赖问题。采用组件化(Component-Based)架构抽象各类EMT模型（如贝杰龙传输线、RLC元件、开关器件等），通过面向对象C++实现求解器工作区重用与内存优化，支持多线程并行计算。

### 数学公式


**公式1**: $$$$U_j^{(k)} = G(T_j, T_{j-1}, U_{j-1}^{(k)}) + F(T_j, T_{j-1}, U_{j-1}^{(k-1)}) - G(T_j, T_{j-1}, U_{j-1}^{(k-1)})$$$$

*Parareal算法核心校正公式，其中$k$为迭代次数，$j$为时间子区间索引。通过粗算子预测与细算子校正的结合，逐步逼近精细解。*


**公式2**: $$$$W(U) := \begin{cases} U^1 - F(T_1, T_0, U^0) = 0 \\ U^2 - F(T_2, T_1, U^1) = 0 \\ \vdots \\ U^{N-1} - F(T_{N-1}, T_{N-2}, U^{N-2}) = 0 \end{cases}$$$$

*全局非线性方程组形式，描述各时间子区间状态向量$U^j$需满足的连续性约束，$U^0$为已知初始条件。*


**公式3**: $$$$Y v^{n+1} = s^{n+1} - i_{hist}^{n+1}$$$$

*基于梯形法离散的电路节点导纳方程，$Y$为节点导纳矩阵，$v$为节点电压向量，$s$为独立源注入，$i_{hist}$为历史项等效电流源。*


**公式4**: $$$$i_{hist}^{n+1} = g(x^n, v^n), \quad x^{n+1} = h(i_{hist}^{n+1}, v^{n+1})$$$$

*组件历史项更新方程，$x$为元件内部状态变量（如电感电流、电容电压），通过本地状态空间积分保持与全局系统的解耦。*


**公式5**: $$$$i^{n+1} = G_{eq} v^{n+1} + i_{hist}^{n+1}, \quad i_{hist}^{n+1} = i^n + G_{eq} v^n$$$$

*电感/电容元件的梯形法离散 companion model，$G_{eq}$为等效电导，实现将动态元件转换为等效电阻并联电流源的诺顿等效形式。*


### 算法步骤

1. 初始化阶段：使用粗算子$G$以较大步长$\Delta t$顺序计算各粗网格点初始猜测值$U_j^{(0)}$，满足$U_j^{(0)} = G(T_j, T_{j-1}, U_{j-1}^{(0)})$

2. 并行细算阶段：在每个迭代步$k$，将$N$个时间子区间分配给不同CPU线程，使用细算子$F$以精细步长$\delta t$并行计算各区间内的详细暂态响应$F(T_j, T_{j-1}, U_{j-1}^{(k-1)})$

3. 粗算子校正阶段：使用粗算子$G$基于最新状态$U_{j-1}^{(k)}$重新计算预测值$G(T_j, T_{j-1}, U_{j-1}^{(k)})$

4. 状态更新阶段：应用Parareal校正公式$U_j^{(k)} = G_j^{(k)} + F_{j,k} - G_j^{(k-1)}$更新各时间界面状态，其中$F_{j,k}$表示第$k$次迭代在第$j$区间的细算子结果

5. 传输线延迟处理阶段：对包含行波传输线的子区间，采用改进插值策略处理延迟微分方程中的历史项依赖，通过插值计算$t-\tau$时刻的状态值，确保延迟项与当前迭代步的同步

6. 收敛判断阶段：计算相邻两次迭代的相对误差$\|U^{(k)} - U^{(k-1)}\|/\|U^{(k)}\|$，若小于设定阈值或达到最大迭代次数则停止，否则返回步骤2

7. 内存管理阶段：重用求解器工作区(Solver Workspace)和组件历史状态缓冲区，避免Parareal迭代过程中的重复内存分配开销


### 关键参数

- **coarse_time_step**: \Delta t，粗网格时间步长，决定Parareal粗算子的离散间隔

- **fine_time_step**: \delta t，细网格时间步长，通常为\Delta t的1/10至1/100，决定仿真精度

- **propagation_delay**: \tau，传输线传播延迟，行波模型关键参数，影响DDE方程的历史项回溯深度

- **cpu_threads**: 6，并行计算使用的CPU线程数，对应测试案例中的硬件配置

- **convergence_tolerance**: 未明确给出具体数值，但提及与传统串行算法达到相同精度(Same Accuracy)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE-118节点标准测试系统 | 在6个CPU线程配置下，完成整个系统的电磁暂态仿真。仿真过程完整考虑了系统的非线性特性、传输线行波延迟以及多组件耦合效应。结果表明系统能够稳定收敛，且各节点电压、支路电流波形与传统串行算法完全一致。 | 相比传统顺序执行算法实现2.30倍加速比(Speed-up)，并行效率(Parallel Efficiency)达到约40%，在保持相同计算精度的前提下显著减少仿真耗时 |

| 多规模IEEE测试系统对比分析 | 针对不同规模的IEEE标准测试系统（如IEEE-39、IEEE-118等）进行性能评估，分析系统时域特性对Parareal算法加速效果的影响。重点考察传输线延迟分布、系统刚性(Stiffness)与并行性能的关系。 | 发现系统时域特性决定加速效果，特别是传输线延迟参数\tau显著影响收敛速度；延迟越大，Parareal迭代收敛所需的校正次数越多，并行效率相应降低 |



## 量化发现

- 在IEEE-118测试系统上使用6个CPU线程时，加速比达到2.30倍(2.30x speed-up)
- 并行效率约为40%(Parallel Efficiency around 40%)，表明在6核配置下有效利用了硬件资源
- 仿真精度与传统串行算法保持一致(Under the same accuracy)，验证了新方法的数值一致性
- 传输线传播延迟\tau显著影响并行性能，长延迟线路导致Parareal迭代收敛速度下降
- 系统时域特性（如刚性、时间常数分布）是决定Parareal算法加速效果的关键因素
- 通过重用求解器工作区，有效降低了面向对象实现中对象分配带来的内存开销


## 关键公式

### Parareal校正迭代式

$$$$U_j^{(k)} = G(T_j, T_{j-1}, U_{j-1}^{(k)}) + F(T_j, T_{j-1}, U_{j-1}^{(k-1)}) - G(T_j, T_{j-1}, U_{j-1}^{(k-1)})$$$$

*在每个迭代步$k$中，用于更新第$j$个时间界面状态向量，结合粗算子的最新预测与细算子在前一次迭代中的校正量*

###  Jacobian矩阵近似

$$$$\frac{\partial F}{\partial U}(T_j, T_{j-1}, U_{j-1}^{(k-1)}) \approx \frac{F(T_j, T_{j-1}, U_{j-1}^{(k-1)}) - F(T_j, T_{j-1}, U_{j-1}^{(k-2)})}{U_{j-1}^{(k-1)} - U_{j-1}^{(k-2)}}$$$$

*在牛顿法求解非线性方程组时，用于近似细算子$F$对状态向量$U$的导数，实现 Newton-Raphson 迭代线性化*

### 离散电路节点方程

$$$$Y v^{n+1} = s^{n+1} - i_{hist}^{n+1}, \quad i_{hist}^{n+1} = g(x^n, v^n)$$$$

*基于梯形法对微分代数方程(DAE)进行离散后，描述电力网络节点电压与元件历史电流源关系的全局系统方程*



## 验证详情

- **验证方式**: 基于仿真对比的验证方法，将提出的并行算法与相同模型参数下的传统串行电磁暂态仿真结果进行时域波形对比
- **测试系统**: IEEE-118节点标准测试系统，包含多机系统、传输网络及负荷模型，是具有代表性的中等规模电力系统测试案例
- **仿真工具**: 自主开发的面向对象C++电磁暂态仿真程序，基于组件化架构实现，支持多线程并行计算；未使用商业软件如PSCAD/EMTDC或MATLAB/Simulink
- **验证结果**: 验证结果表明，所提出的并行方法在6线程配置下实现2.30倍加速，并行效率约40%，且所有节点电压、支路电流的仿真波形与传统串行算法完全一致，证明了方法在保持数值精度的同时显著提升了计算效率。此外，通过不同规模系统的测试，确认了传输线延迟对算法收敛性能的关键影响。
