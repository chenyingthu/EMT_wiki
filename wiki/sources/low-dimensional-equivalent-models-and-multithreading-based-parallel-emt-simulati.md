---
title: "Low-Dimensional Equivalent Models and Multithreading-Based Parallel EMT Simulation Method for Multi-Converter Systems"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Energy Conversion;2025;40;1;10.1109/TEC.2024.3422080"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Xu 等 - 2025 - Low-Dimensional Equivalent Models and Multithreading-Based Parallel EMT Simulation Method for Multi-.pdf"]
---

# Low-Dimensional Equivalent Models and Multithreading-Based Parallel EMT Simulation Method for Multi-Converter Systems

**作者**: 
**年份**: 2025
**来源**: `25/Xu 等 - 2025 - Low-Dimensional Equivalent Models and Multithreading-Based Parallel EMT Simulation Method for Multi-.pdf`

## 摘要

—As the proportion of renewable energy generation in the grid increases, the number of voltage source converters (VSCs) has grown signiﬁcantly. It is therefore of great importance to study the multi-VSC systems using electromagnetic transient (EMT) simulation. This paper presents a novel approach to modeling multi-VSC circuits, comprising EMT low-dimensional equivalent models and a multithreading-based parallel simulation method. The decoupling between the VSC from the AC grid is initially achieved through the adoption of semi-implicit hybrid integration. This is followed by the synthesis of the equivalent circuit for each phase,whichresultsinthederivationoflow-dimensionalequivalent models of multi-VSC circuits. In addition, a parallel simulation algorithm for the VSC is proposed, which en

## 核心贡献


- 提出基于半隐式混合积分的VSC与电网解耦方法，实现内外节点并行求解
- 推导适配不同直流连接方式的多VSC低维等效电路，降低节点导纳矩阵维度
- 设计基于OpenMP的多线程并行算法，克服传统节点消元法的高串行缺陷


## 使用的方法


- [[半隐式混合积分|半隐式混合积分]]
- [[节点消元法|节点消元法]]
- [[等效电路综合|等效电路综合]]
- [[多线程并行计算|多线程并行计算]]
- [[openmp框架|OpenMP框架]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[vsc-model|VSC]]
- [[光伏电源单元|光伏电源单元]]
- [[滤波器|滤波器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[等效建模|等效建模]]
- [[新能源并网|新能源并网]]
- [[仿真加速|仿真加速]]


## 主要发现


- 在百兆瓦光伏电站串行仿真中，解耦与低维模型实现超八十倍计算加速
- 并行模式下获得两至三倍二次加速，且关键电气量仿真精度几乎无损失



## 方法细节

### 方法概述

本文提出一种面向多电压源换流器（VSC）系统的电磁暂态（EMT）低维等效建模与多线程并行仿真方法。首先，在滤波器接口处采用半隐式混合积分法（梯形法与中心差分法结合），通过引入半步长时延实现VSC内部节点与交流电网外部节点的解耦，从而打破传统节点导纳矩阵的高维时变特性。其次，针对各相电路进行等效综合，推导出适用于不同直流侧连接方式（直流侧独立或并联）的多VSC低维等效电路模型，大幅降低系统矩阵维度。最后，设计基于OpenMP框架的多线程并行算法，替代传统节点消元法（NEM）的串行求解过程，实现内外节点电压与历史电流源的并行更新与求解，在保证器件级仿真精度的同时显著提升计算效率。

### 数学公式


**公式1**: $$$\dot{x}(t) = Ax(t) + Bu(t)$$$

*线性系统连续状态方程，用于描述多VSC系统的动态特性，是后续矩阵分裂与离散化的基础。*


**公式2**: $$$\int \dot{x}_i(t) dt + D_i \int x_i(t) dt = \int \sum_{j=1, j\neq i}^N A_{\beta,ij} x_j(t) dt + \int u_i(t) dt$$$

*状态矩阵分裂后的积分形式，将系统划分为对角部分（$D_i$）与非对角耦合部分（$A_{\beta,ij}$），为解耦提供数学依据。*


**公式3**: $$$\begin{cases} x_1^{n+1} = \eta_1 x_1^{n-1/2} + \lambda_1 f_1(x_2^{n+1/2}, u_1^{n+1/2}) \\ x_2^{n+1/2} = \eta_2 x_2^{n-1/2} + \lambda_2 f_2(x_1^n, u_2^n) \end{cases}$$$

*半隐式混合积分离散化后的解耦更新方程，通过半步长交错更新实现子系统间的并行求解。*


**公式4**: $$$\begin{bmatrix} L_{gm} & 0 \\ 0 & C_m \end{bmatrix} \frac{d}{dt} \begin{bmatrix} i_{gm} \\ u_{Cm} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix} \begin{bmatrix} i_{gm} \\ u_{Cm} \end{bmatrix} + \begin{bmatrix} -u_{gm} \\ i_{Lm} \end{bmatrix}$$$

*VSC交流侧滤波器L/C元件的连续状态方程，用于推导离散化模型及后续等效电路参数。*


### 算法步骤

1. 系统拓扑划分与状态矩阵分裂：将多VSC系统划分为VSC内部子系统与交流电网/滤波器外部子系统，对全局状态矩阵A进行对角与非对角部分分离，明确各子系统间的耦合边界。

2. 半隐式混合积分离散化：在滤波器接口处，对电感与电容状态变量分别采用梯形积分法与中心差分法进行离散处理，构造具有半步长时延的离散化状态方程，从数学上切断内外节点的直接代数依赖。

3. 节点解耦与低维等效电路综合：利用离散方程实现VSC内外节点解耦，按相序独立推导各VSC的三节点低维等效电路；根据直流侧实际拓扑（独立运行或并联互联）动态适配等效导纳与历史电流源参数。

4. OpenMP多线程并行任务分配：基于OpenMP框架设计并行调度策略，将解耦后的内外节点电压求解、历史电流源更新及等效电路参数计算任务分配至独立线程，彻底消除传统节点消元法（NEM）的串行瓶颈。

5. 半步长数据同步与全局状态推进：在每个仿真步长内，各线程并行计算局部响应，通过半步长数据交换机制同步边界变量，完成全局状态迭代更新，输出高精度EMT波形。


### 关键参数

- **积分策略**: 梯形法与中心差分法混合（半隐式）

- **解耦机制**: 半步长时延交错更新

- **等效节点维度**: 单VSC降维至三节点等效电路

- **并行框架**: OpenMP多线程调度

- **适用直流拓扑**: 直流侧独立/并联多VSC场景



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 100MW并网光伏电站多VSC系统 | 在串行求解模式下，采用解耦与低维等效模型后，仿真计算时间大幅缩短，实现超过80倍的加速比；在开启OpenMP并行模式后，在串行加速基础上进一步获得2-3倍的二次加速，且内外节点电压与电流波形精度与全维模型高度一致。 | 串行加速>80倍，并行二次加速2-3倍，精度几乎无损 |



## 量化发现

- 100MW光伏电站串行仿真加速比超过80倍
- 多线程并行模式下实现2-3倍的二次加速
- 等效模型在保持器件级开关动态精度的同时，节点导纳矩阵维度显著降低
- 解耦算法有效克服了传统节点消元法的高串行缺陷，实现内外节点并行求解


## 关键公式

### 半隐式混合积分解耦更新方程

$$$\begin{cases} x_1^{n+1} = \eta_1 x_1^{n-1/2} + \lambda_1 f_1(x_2^{n+1/2}, u_1^{n+1/2}) \\ x_2^{n+1/2} = \eta_2 x_2^{n-1/2} + \lambda_2 f_2(x_1^n, u_2^n) \end{cases}$$$

*用于在滤波器接口处实现VSC内部状态与电网外部状态的半步长解耦，支撑内外节点并行求解*

### 滤波器L/C连续状态方程

$$$\begin{bmatrix} L_{gm} & 0 \\ 0 & C_m \end{bmatrix} \frac{d}{dt} \begin{bmatrix} i_{gm} \\ u_{Cm} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix} \begin{bmatrix} i_{gm} \\ u_{Cm} \end{bmatrix} + \begin{bmatrix} -u_{gm} \\ i_{Lm} \end{bmatrix}$$$

*描述VSC交流侧滤波器动态特性，是进行半隐式离散化与等效电路推导的基础*



## 验证详情

- **验证方式**: 仿真对比与物理实验平台验证
- **测试系统**: 100MW并网光伏电站（含多VSC并联运行）
- **仿真工具**: 基于OpenMP自主开发的EMT并行仿真框架（对比传统串行EMT求解器）
- **验证结果**: 在100MW光伏电站测试中，所提低维等效模型在串行模式下实现超80倍加速，结合OpenMP并行算法后获得2-3倍二次加速。物理实验平台验证表明，模型在大幅降低计算维度的同时，内外节点电压与电流波形精度几乎无损，有效兼顾了高精度与高效率。
