---
title: "Efficient electromagnetic transient simulation for DFIG-based wind farms using fine-grained network partitioning"
type: source
authors: ['Jiale Yu']
year: 2024
journal: "International Journal of Electrical Power and Energy Systems, 162 (2024) 110297. doi:10.1016/j.ijepes.2024.110297"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/Yu 等 - 2024 - Efficient electromagnetic transient simulation for DFIG-based wind farms using fine-grained network.pdf"]
---

# Efficient electromagnetic transient simulation for DFIG-based wind farms using fine-grained network partitioning

**作者**: Jiale Yu
**年份**: 2024
**来源**: `13&14/files/Yu 等 - 2024 - Efficient electromagnetic transient simulation for DFIG-based wind farms using fine-grained network.pdf`

## 摘要

International Journal of Electrical Power and Energy Systems Efficient electromagnetic transient simulation for DFIG-based wind farms Jiale Yu, Haoran Zhao ∗, Yibao Jiang ∗, Bing Li, Linghan Meng, Futao Yang School of Electrical Engineering, Shandong University, Jinan, 250061, China Electromagnetic transient (EMT) simulation plays a critical role in understanding the dynamic behavior

## 核心贡献


- 建立核心设备全电磁暂态高效模型，避免频繁矩阵求逆，提升单机计算效率
- 提出设备级细粒度网络解耦方法，降低导纳矩阵维度，突破亚微秒步长限制
- 构建基于OpenMP的可扩展并行框架，计算流程简洁，适应大规模风电场仿真


## 使用的方法


- [[节点分析法|节点分析法]]
- [[细粒度网络解耦|细粒度网络解耦]]
- [[多线程并行计算|多线程并行计算]]
- [[开关函数法|开关函数法]]
- [[集中参数模型|集中参数模型]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[vsc-model|VSC]]
- [[变压器|变压器]]
- [[lcl滤波器|LCL滤波器]]
- [[输电线路|输电线路]]
- [[风电场|风电场]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[风电场建模|风电场建模]]
- [[网络解耦|网络解耦]]
- [[大规模系统仿真|大规模系统仿真]]


## 主要发现


- 50台风机规模下仿真速度提升两个数量级，最大相对误差仅1.68%，兼顾高效与高精度
- 细粒度解耦有效降低导纳矩阵维度，避免亚微秒步长限制，显著提升大规模仿真效率
- 基于OpenMP的并行框架具备强扩展性，随规模扩大仍保持高计算效率与良好加速比



## 方法细节

### 方法概述

本文提出一种面向双馈感应发电机（DFIG）风电场的设备级细粒度网络解耦与并行仿真方法。首先，基于加权数值积分法将电感、电容等动态元件离散化为诺顿等效电路（等效电导并联历史电流源），避免传统方法中因开关状态变化导致的导纳矩阵频繁重构。针对DFIG、变压器、背靠背变流器（VSC）及LCL滤波器等核心设备，推导其解耦等效电路与离散状态方程。通过引入单步近似法（$\psi^{n+1} \approx \psi^n$）消除DFIG dq轴电压与磁链方程的耦合，彻底避免每步矩阵求逆。随后，将单台风机电气系统划分为8个独立子系统，集电系统进一步解耦，使各子系统节点数不超过15，修正节点电压方程维度降至18以内。最后，基于OpenMP构建多线程并行计算框架，通过预存导纳矩阵逆矩阵、计算互联变量、并行求解各子系统状态变量，实现大规模风电场的高效电磁暂态仿真。

### 数学公式


**公式1**: $$$i_{km}(t) = G_{eq} u_{km}(t) + I_h(t-\Delta t)$$$

*动态元件离散化后的诺顿等效模型，$G_{eq}$为等效电导，$I_h$为历史电流源，用于将微分方程转化为代数方程。*


**公式2**: $$$i_{sd}^{n+1} = \frac{\left(\frac{L_{ls}}{\Delta t} - \frac{R_s}{2}\right)i_{sd}^n + u_{sd}^n + \omega \psi_{sq}^n - u_{md}^n}{\frac{L_{ls}}{\Delta t} + \frac{R_s}{2}}$$$

*DFIG定子d轴电流离散更新方程，通过单步近似消除磁链耦合，实现显式求解。*


**公式3**: $$$u_m^n = \frac{\frac{L_m}{L_A}u_A^n + \frac{L_m}{L_B}u_B^n - \frac{L_m}{L_A}i_A^n R_A - \frac{L_m}{L_B}i_B^n R_B}{\frac{L_m}{L_A} + \frac{L_m}{L_B} + 1}$$$

*T型LLL支路中间节点电压求解公式，用于计算互联变量以实现两侧子系统解耦。*


### 算法步骤

1. 预处理与存储：根据风电场拓扑与元件参数，预先计算各子系统在不同开关状态下的修正节点导纳矩阵$G$及其逆矩阵$G^{-1}$，并存储至内存，避免仿真过程中重复求逆。

2. 初始化：调用预存数据，为储能元件（电感、电容）、开关器件（IGBT、断路器）及网络节点赋予合理的初始状态值，确保系统快速进入稳态。

3. 互联变量计算：在每一仿真步长$n$，利用上一时刻的端口电压与支路电流，代入T型LLL支路、VSC或LCL滤波器的离散解耦方程，计算边界节点电压或受控源电流值，作为当前时刻各子系统的注入量。

4. 并行状态求解：基于OpenMP将各子系统分配至不同CPU线程。各线程独立调用预存的$G^{-1}$，通过$u = G^{-1}i$求解当前时刻节点电压，并更新历史电流源$I_h$与内部状态变量。

5. 迭代推进：完成当前步长所有子系统求解后，同步数据并进入下一时刻$(n+1)\Delta t$，重复步骤3-4直至仿真结束。


### 关键参数

- **仿真步长**: 5 μs（满足集电线路解耦要求，避免亚微秒限制）

- **单台风机最大子系统节点数**: ≤15

- **修正节点方程最大维度**: ≤18

- **积分方法权重系数**: α（梯形法α=0.5，后向欧拉法α=1）

- **并行框架**: OpenMP多线程共享内存模型



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 50台DFIG风机大规模风电场 | 在50台风机规模下，所提方法实现高效仿真，最大相对误差仅为1.68%，同时保持微秒级步长稳定性。 | 相比Matlab/Simulink详细模型，仿真速度提升两个数量级（约100倍）。 |



## 量化发现

- 50台风机规模下仿真速度提升两个数量级（加速比达100倍）
- 最大相对误差控制在1.68%以内，兼顾高精度与高效率
- 单台风机子系统节点数降至≤15，修正节点导纳矩阵维度≤18，计算复杂度由O(N^3)大幅降低
- 仿真步长稳定在5 μs，突破传统细粒度解耦方法需亚微秒或纳秒步长的限制
- 基于OpenMP的并行框架随风机数量增加保持良好扩展性，加速比接近线性增长


## 关键公式

### 动态元件诺顿等效离散方程

$$$i_{km}(t) = G_{eq} u_{km}(t) + I_h(t-\Delta t)$$$

*用于将电感、电容、RL/RC支路转化为恒定导纳与历史电流源并联形式，是节点分析法的基础。*

### T型LLL支路解耦电压方程

$$$u_m^n = \frac{\frac{L_m}{L_A}u_A^n + \frac{L_m}{L_B}u_B^n - \frac{L_m}{L_A}i_A^n R_A - \frac{L_m}{L_B}i_B^n R_B}{\frac{L_m}{L_A} + \frac{L_m}{L_B} + 1}$$$

*用于计算变压器与DFIG等效电路中T型电感支路的中间节点电压，实现两侧电气系统的解耦。*

### 两电平VSC离散状态方程

$$$\begin{bmatrix} u_a^{n+1} \\ u_b^{n+1} \\ u_c^{n+1} \\ i_{dc}^{n+1} \end{bmatrix} = \begin{bmatrix} R_{on} & 0 & 0 & S_a & S_a-1 \\ 0 & R_{on} & 0 & S_b & S_b-1 \\ 0 & 0 & R_{on} & S_c & S_c-1 \\ S_a & S_b & S_c & 0 & 0 \end{bmatrix} \begin{bmatrix} i_a^n \\ i_b^n \\ i_c^n \\ u_{d1}^n \\ u_{d2}^n \end{bmatrix}$$$

*在单步近似假设下，利用开关函数与上一时刻状态量直接计算下一时刻端口电压与直流侧电流，实现变流器两侧解耦。*



## 验证详情

- **验证方式**: 仿真对比验证
- **测试系统**: 50台DFIG风机组成的大规模风电场（含集电系统与PCC）
- **仿真工具**: 自定义C语言/OpenMP并行代码（封装为DLL）调用至MATLAB环境，对比基准为MATLAB/Simulink详细模型
- **验证结果**: 验证表明所提细粒度解耦与并行框架在50台风机规模下实现约100倍加速，最大相对误差仅1.68%，导纳矩阵维度显著降低，且OpenMP多线程扩展性良好，满足大规模风电场高效高精度EMT仿真需求。
