---
title: "Modeling for large-scale offshore wind farm using multi-thread parallel computing"
type: source
authors: ['Ming Zou']
year: 2023
journal: "International Journal of Electrical Power and Energy Systems, 148 (2023) 108928. doi:10.1016/j.ijepes.2022.108928"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/26/Zou 等 - 2023 - Modeling for large-scale offshore wind farm using multi-thread parallel computing.pdf"]
---

# Modeling for large-scale offshore wind farm using multi-thread parallel computing

**作者**: Ming Zou
**年份**: 2023
**来源**: `26/Zou 等 - 2023 - Modeling for large-scale offshore wind farm using multi-thread parallel computing.pdf`

## 摘要

Electrical Power and Energy Systems 148 (2023) 108928 0142-0615/© 2022 Elsevier Ltd. All rights reserved. Modeling for large-scale offshore wind farm using multi-thread State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University (NCEPU), 102206 Beijing, China Large-scale Offshore Wind Farms (OWFs) face difficulty when carrying out microsecond-level Electro-Magnetic

## 核心贡献


- 提出基于内部节点消元的单机集成等值建模方法，有效降低导纳矩阵阶数
- 设计相间解耦算法消除三相互阻抗，满足风机与集电线路并联等值条件
- 将OpenMP多线程并行技术融入全场求解流程，实现大规模风电场仿真加速


## 使用的方法


- [[节点分析法|节点分析法]]
- [[梯形积分法|梯形积分法]]
- [[内部节点消元|内部节点消元]]
- [[相间解耦|相间解耦]]
- [[多线程并行计算|多线程并行计算]]
- [[诺顿等值|诺顿等值]]


## 涉及的模型


- [[pmsg|PMSG]]
- [[全功率变流器|全功率变流器]]
- [[lc滤波器|LC滤波器]]
- [[变压器|变压器]]
- [[输电线路|输电线路]]
- [[风力发电机|风力发电机]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[风电场建模|风电场建模]]
- [[并行计算|并行计算]]
- [[网络等值|网络等值]]
- [[海上风电|海上风电]]


## 主要发现


- 所提等值模型相比详细模型最大相对误差低于0.96%，保持高精度动态特性
- 多线程并行计算大幅提升大规模海上风电场仿真速度，获得显著加速比
- 该方法克服短集电线路自然解耦限制，实现微秒级高效电磁暂态仿真



## 方法细节

### 方法概述

本文提出了一种面向大规模海上风电场(OWF)的电磁暂态(EMT)集成等值建模与多线程并行计算方法。首先，基于梯形积分法(TR)对永磁同步风机(PMSG)及其全功率变流器、LC滤波器、变压器等设备进行离散化，建立伴随电路模型。通过分块矩阵技术将节点划分为外部节点(EN)和内部节点(IN)，利用内部节点消元技术降低导纳矩阵阶数。针对风机模型存在三相互阻抗导致无法满足并联等值条件的问题，提出相间解耦算法：将节点导纳矩阵分解为对角部分和非对角部分，采用单时间步近似假设(u_EN(t)≈u_EN(t-Δt))消除相间耦合项影响，使各相解耦为独立的诺顿等值电路。最后，将OpenMP多线程并行计算技术融入全场求解流程，利用共享内存的'fork-join'架构实现各风机模型并行计算，显著加速大规模风电场仿真。

### 数学公式


**公式1**: $$$\begin{bmatrix} Y_{11} & Y_{12} \\ Y_{21} & Y_{22} \end{bmatrix} \begin{bmatrix} u_{EN} \\ u_{IN} \end{bmatrix} = \begin{bmatrix} 0 \\ J_{IN} \end{bmatrix} + \begin{bmatrix} i_{EN} \\ 0 \end{bmatrix}$$$

*分块矩阵形式的节点导纳方程，其中下标EN表示外部节点（保留节点），IN表示内部节点（待消去节点），Y_{11}为外部节点自导纳，Y_{22}为内部节点自导纳，Y_{12}和Y_{21}为互导纳矩阵*


**公式2**: $$$i_{EN}(t) = (Y_{11} - Y_{12}Y_{22}^{-1}Y_{21})u_{EN}(t) + Y_{12}Y_{22}^{-1}J_{IN}(t-\Delta t) \triangleq Gu_{EN}(t) + J(t-\Delta t)$$$

*消去内部节点后的诺顿等值方程，其中G为等值导纳矩阵，J(t-Δt)为历史项注入电流，通过舒尔补(Schur complement)运算实现内部节点消元*


**公式3**: $$$i_{EN}(t) = (Y_{diag} + Y_{rest})u_{EN}(t) + J(t-\Delta t)$$$

*相间解耦关键方程，将等值导纳矩阵G分解为对角元素矩阵Y_diag（各相自阻抗）和非对角元素矩阵Y_rest（相间互阻抗），为后续解耦处理奠定基础*


**公式4**: $$$u_{EN}(t) \approx u_{EN}(t-\Delta t)$$$

*单时间步近似假设，用于消除相间耦合项Y_rest的影响，假设当前时刻电压近似等于上一时刻电压，从而实现三相解耦*


### 算法步骤

1. 建立PMSG风机详细电路模型，包括永磁同步发电机、背靠背全功率变流器(FRC)、直流斩波器支路、LC滤波器和三相变压器

2. 采用梯形积分法(TR)对所有动态元件（电感、电容）进行离散化，构建伴随电路模型，确定等值电导和历史项电流源

3. 构建完整风机的节点导纳方程，通过分块矩阵技术将节点划分为外部节点(EN)和内部节点(IN)，形成式(1)所示的分块矩阵结构

4. 执行内部节点消元：通过矩阵运算计算舒尔补，得到消去内部节点后的等值导纳矩阵G = Y_{11} - Y_{12}Y_{22}^{-1}Y_{21}和等值历史项电流源，实现单机模型降阶

5. 相间解耦处理：将等值导纳矩阵G分解为对角部分Y_diag和非对角部分Y_rest，利用单时间步近似假设消除Y_rest项，使三相解耦为三个独立的单相诺顿等值电路

6. 将解耦后的风机模型与集电线路模型进行并联等值，构建整个风电场的降阶导纳矩阵

7. 利用OpenMP多线程并行技术，将各风机的历史项电流源计算、状态更新等计算密集型任务分配到多个CPU核心并行执行，采用'fork-join'模式实现并行加速

8. 求解整个风电场网络的节点电压方程，更新所有风机内部状态变量，进入下一时间步


### 关键参数

- **仿真步长**: 微秒级(microsecond-level)

- **积分方法**: 梯形积分法(Trapezoidal Rule, TR)

- **并行技术**: OpenMP多线程并行计算

- **编程语言**: C, C++, Fortran

- **架构模式**: fork-join共享内存架构

- **风机类型**: 永磁同步风机(PMSG) with Full Rated Converter (FRC)

- **消元方法**: 内部节点消元(Internal Node Elimination)基于舒尔补



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 大规模海上风电场详细模型与等值模型对比 | 在PSCAD/EMTDC平台上对比所提等值模型与详细模型的动态特性，测试包括三相短路故障、风速变化等暂态工况 | 所提等值模型相比详细模型的最大相对误差低于0.96%，在保证高精度的同时实现显著加速 |

| 多线程并行计算性能测试 | 对比串行算法与OpenMP多线程并行算法的仿真耗时，验证并行计算对大规模风电场的加速效果 | 多线程并行计算大幅提升大规模海上风电场仿真速度，获得显著加速比(large speedup factors)，克服短集电线路自然解耦限制 |



## 量化发现

- 所提等值模型相比详细模型的最大相对误差低于0.96%，能够精确模拟大规模海上风电场的动态特性
- 采用微秒级(microsecond-level)仿真步长进行电磁暂态仿真，满足电力电子开关器件精确建模需求
- 通过内部节点消元技术显著降低导纳矩阵阶数，减少矩阵重构和求逆运算的计算负担
- 相间解耦算法成功消除三相互阻抗影响，使风机模型满足诺顿并联等值条件，适用于短集电线路场景
- OpenMP多线程并行计算实现大规模风电场的高效仿真，在保持精度的同时获得显著加速比


## 关键公式

### 诺顿等值电路方程

$$$i_{EN}(t) = Gu_{EN}(t) + J(t-\Delta t)$$$

*消去内部节点后，将复杂风机等值为简单的诺顿等值电路，其中G为等值导纳，J为历史项电流源，用于后续与集电线路并联连接*

### 舒尔补等值导纳矩阵

$$$G = Y_{11} - Y_{12}Y_{22}^{-1}Y_{21}$$$

*内部节点消元的核心计算，通过矩阵分块和求逆运算，将内部节点的影响等效到外部节点，大幅降低系统导纳矩阵维度*



## 验证详情

- **验证方式**: 仿真验证与对比分析
- **测试系统**: 大规模海上风电场(OWF)系统，包含多台PMSG风机、集电网络和输电线路
- **仿真工具**: PSCAD/EMTDC电磁暂态仿真软件
- **验证结果**: 所提方法能够精确模拟大规模海上风电场的动态特性，与详细模型相比最大相对误差低于0.96%。通过集成OpenMP多线程并行计算，显著提升了微秒级步长的EMT仿真速度，克服了短集电线路不满足自然解耦条件的限制，实现了高效准确的大规模风电场电磁暂态仿真。
