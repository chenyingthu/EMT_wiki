---
title: "Decoupled Detailed Equivalent Model for Parallel and Multi-Rate EMT-Type Simulation of Modular Multilevel Converter With Battery Energy Storage"
type: source
authors: ['未知']
year: 2026
journal: "IEEE Transactions on Power Delivery;2026;41;2;10.1109/TPWRD.2025.3648650"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/12/Decoupled_Detailed_Equivalent_Model_for_Parallel_and_Multi-Rate_EMT-Type_Simulation_of_Modular_Multilevel_Converter_With_Battery_Energy_Storage.pdf"]
---

# Decoupled Detailed Equivalent Model for Parallel and Multi-Rate EMT-Type Simulation of Modular Multilevel Converter With Battery Energy Storage

**作者**: 
**年份**: 2026
**来源**: `12/Decoupled_Detailed_Equivalent_Model_for_Parallel_and_Multi-Rate_EMT-Type_Simulation_of_Modular_Multilevel_Converter_With_Battery_Energy_Storage.pdf`

## 摘要

—Modular multilevel converters (MMCs) integrated with battery energy storage systems (BESS) enable efﬁcient uti- lization of renewable energy resources such as wind and photo- voltaic, while enhancing reliability and scalability of high-voltage direct current systems. This paper proposes a decoupled detailed equivalent model (D-DEM) for BESS-integrated MMC for elec- tromagnetic transient (EMT) simulation. The proposed model can accurately represent the dynamics of the converter under deblock- ing and blocking modes. To efﬁciently utilize available hardware resources, a multi-rate simulation technique is adopted to sim- ulate the MMC subsystems with different time steps. Addition- ally, switching interpolation technique is proposed to accurately compensate for the intra-time-step switching 

## 核心贡献


- 提出解耦详细等效模型实现恒定导纳矩阵与节点缩减支持闭锁解锁状态
- 提出多速率仿真与开关插值技术实现变步长求解与步内开关事件精确补偿
- 开发CPU-GPU混合并行求解器大幅提升含储能MMC电磁暂态仿真效率


## 使用的方法


- [[多速率仿真|多速率仿真]]
- [[开关插值技术|开关插值技术]]
- [[节点分析法|节点分析法]]
- [[混合并行计算|混合并行计算]]
- [[等效电路建模|等效电路建模]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[bess|BESS]]
- [[子模块|子模块]]
- [[dc-dc变换器|DC-DC变换器]]
- [[详细等效模型|详细等效模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[多速率仿真|多速率仿真]]
- [[mmc-model|MMC]]
- [[储能系统集成|储能系统集成]]
- [[开关事件补偿|开关事件补偿]]


## 主要发现


- D-DEM在1微秒步长下与详细模型精度一致CPU单核仿真速度提升2.81倍
- 采用CPU-GPU混合并行求解器后仿真速度较纯CPU串行实现提升79倍
- 多速率与开关插值技术有效支持大时间步长同时保持闭锁解锁动态高精度



## 方法细节

### 方法概述

本文提出一种面向含储能模块化多电平换流器（BESS-MMC）的解耦详细等效模型（D-DEM）及混合并行多速率电磁暂态（EMT）仿真方法。传统耦合模型采用二值电阻模拟开关，导致导纳矩阵时变、节点高度耦合且需频繁LU分解。D-DEM通过引入开关函数（S和G）替代二值电阻，利用前向欧拉法显式离散化电容电压，将子模块（SM）侧与电池侧（BS）电路完全解耦，实现恒定导纳矩阵与节点方程降维（4×4降至1×1）。为兼顾精度与效率，采用多速率仿真架构：CPU以大步长求解低频变化的桥臂网络与SM侧开关函数，GPU以小步长并行求解高频切换的SM电容与BS侧DC-DC变换器。同步时刻通过时间平均电压传递数据以保证能量守恒。此外，提出开关插值技术，通过调制波与载波的线性插值精确计算步内开关过零点与导通占空比，补偿固定步长求解器无法捕捉的步内开关瞬态。最终基于CUDA架构开发CPU-GPU异构并行求解器，实现电气模型到并行计算内核的映射。

### 数学公式


**公式1**: $$$v_{CSM}(t+\Delta t) = v_{CSM}(t) + \frac{\Delta t}{C_{SM}} i_{CSM}(t)$$$

*子模块电容电压前向欧拉离散方程，用于显式更新电容状态并实现SM侧与BS侧电路解耦*


**公式2**: $$$i_{CSM,avg}(t) = d_{BS} i_{BS}(t) + d_{SM} i_{SM}(t)$$$

*开关插值平均电容电流方程，结合步内开关占空比计算等效平均电流，补偿步内开关事件引起的数值误差*


**公式3**: $$$V_{\alpha,x,j}(t+\Delta t_L) = \frac{\sum_{k=1}^{n} V_{\alpha,x,j}(t+k\Delta t_S)}{n}$$$

*多速率同步平均电压传递方程，GPU小步长向CPU大步长传递数据时使用，确保不同步长下的积分能量一致性*


**公式4**: $$$t_{z,BS} = \frac{\Delta t_S}{1 - r_{BS}} + t, \quad r_{BS} = \frac{m_{BS}(t+\Delta t_S) - c_{BS}(t+\Delta t_S)}{m_{BS}(t) - c_{BS}(t)}$$$

*步内开关过零点线性插值方程，通过调制波与载波在相邻步长的值精确计算开关动作发生的实际时刻*


### 算法步骤

1. 初始化系统拓扑、参数与初始状态，划分计算域：CPU负责大步长（$\Delta t_L$）网络求解，GPU负责小步长（$\Delta t_S$）SM电容与BS侧变换器求解。

2. CPU端执行当前大步长网络求解，获取桥臂电流$i_{x,j}$与SM侧开关函数$S$，将其保持恒定并发送至GPU端。

3. GPU端在单个$\Delta t_L$周期内执行$n=\Delta t_L/\Delta t_S$次小步长迭代。每次迭代利用开关插值技术计算调制波与载波交点$t_z$，推导占空比$d$与导通时间$t_{on}$，更新平均电容电流$i_{C,avg}$与电压$v_{CSM}$。

4. GPU端计算$\Delta t_L$周期内所有桥臂等效电压的算术平均值$V_{\alpha,x,j}$，在同步时刻回传至CPU端，替代瞬时值以避免高频波动引入的数值失真。

5. CPU端接收平均电压，更新恒定导纳矩阵网络方程，求解下一时刻系统状态。循环执行步骤2-5直至仿真结束，全程无需矩阵重分解。


### 关键参数

- **large_time_step**: 20 μs

- **small_time_step**: 5 μs

- **submodules_per_arm**: 400

- **GPU_hardware**: NVIDIA Turing GeForce RTX-2060 (1920 CUDA cores, 6GB GDDR6)

- **CPU_hardware**: Intel i7, 16GB RAM

- **integration_method**: Forward Euler (显式)

- **switching_model**: Switching function (S, G) 替代二值电阻

- **data_sync_ratio**: n = ΔtL / ΔtS = 4



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 400子模块/臂BESS-MMC纯CPU仿真对比 | 在Intel i7 CPU环境下运行D-DEM模型，导纳矩阵全时段保持恒定，消除传统模型因开关状态变化导致的频繁LU分解开销。 | 仿真速度比传统耦合详细等效模型（C-DEM）快2.81倍 |

| CPU-GPU混合并行多速率仿真 | 将高频SM电容与BS侧DC-DC变换器计算卸载至GPU并行执行，结合多速率数据同步与开关插值补偿机制。 | 整体求解速度比CPU-only串行实现快79倍 |

| 1μs高精度基准动态响应验证 | 在Simulink/Simscape中搭建1μs步长的详细模型（DM）作为基准，对比D-DEM在20μs/5μs多速率下的解锁与闭锁工况响应。 | 关键电气量（电容电压、桥臂电流、直流母线电压）波形高度吻合，验证了大步长下插值补偿的有效性 |



## 量化发现

- D-DEM模型将传统4×4节点方程降维至1×1电压方程，导纳矩阵实现全时段恒定，彻底消除网络矩阵重分解的计算瓶颈。
- 多速率仿真采用20μs（CPU）与5μs（GPU）双步长配置，在保证高频瞬态精度的前提下，计算负载降低约75%。
- 开关插值技术通过线性插值精确捕获步内开关事件，使大步长下的电容电压累积误差显著降低，避免为捕捉开关瞬态而被迫使用极小步长（如1μs）。
- CPU-GPU异构架构下，400子模块/臂的BESS-MMC系统仿真加速比达到79倍，较传统DEM提升2.81倍，证明并行映射策略的高效性。
- 同步数据传递采用$\Delta t_L$周期内的桥臂电压时间平均值，确保大小步长子系统间的能量积分一致性，瞬时值传递会导致的数值振荡被有效抑制。


## 关键公式

### 子模块电容电压前向欧拉离散方程

$$$v_{CSM}(t+\Delta t) = v_{CSM}(t) + \frac{\Delta t}{C_{SM}} i_{CSM}(t)$$$

*用于D-DEM中SM电容电压的显式更新，实现SM侧与BS侧电路解耦，支撑恒定导纳矩阵构建*

### 开关插值平均电容电流方程

$$$i_{CSM,avg}(t) = d_{BS} i_{BS}(t) + d_{SM} i_{SM}(t)$$$

*结合步内开关占空比计算平均电流，补偿固定步长求解器无法捕捉的步内开关瞬态，提升大步长精度*

### 多速率同步平均电压传递方程

$$$V_{\alpha,x,j}(t+\Delta t_L) = \frac{\sum_{k=1}^{n} V_{\alpha,x,j}(t+k\Delta t_S)}{n}$$$

*GPU小步长子系统向CPU大步长子系统传递数据时使用，保证不同步长下的积分能量守恒与数值稳定性*

### 步内开关过零点线性插值方程

$$$t_{z,BS} = \frac{\Delta t_S}{1 - r_{BS}} + t, \quad r_{BS} = \frac{m_{BS}(t+\Delta t_S) - c_{BS}(t+\Delta t_S)}{m_{BS}(t) - c_{BS}(t)}$$$

*通过调制波与载波在相邻步长的值线性插值，精确计算开关动作发生的实际时刻，用于推导占空比与导通时间*



## 验证详情

- **验证方式**: 纯数字仿真对比验证
- **测试系统**: 含电池储能系统的模块化多电平换流器（BESS-MMC），每桥臂配置400个子模块，集成半桥/全桥DC-DC变换器接口
- **仿真工具**: Simulink/Simscape Electrical（作为1μs步长详细模型基准），自定义CPU-GPU混合并行EMT求解器（CUDA C/C++实现）
- **验证结果**: 所提D-DEM在解锁与闭锁两种关键工况下，其动态响应波形与1μs步长详细模型高度一致。多速率与开关插值技术有效消除了大步长带来的数值误差，CPU-GPU并行架构在保持高精度的同时实现了79倍的计算加速，验证了模型在大规模HVDC系统EMT仿真中的工程适用性与显著的效率优势。
