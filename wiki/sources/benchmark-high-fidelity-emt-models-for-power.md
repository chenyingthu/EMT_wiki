---
title: "Benchmark High-Fidelity EMT Models for Power"
type: source
authors: ['未知']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/Marthi 等 - 2024 - Benchmark High-Fidelity EMT Models for Power Grid with PV Plants.pdf"]
---

# Benchmark High-Fidelity EMT Models for Power

**作者**: 
**年份**: 2023
**来源**: `10/Marthi 等 - 2024 - Benchmark High-Fidelity EMT Models for Power Grid with PV Plants.pdf`

## 摘要

—In recent times electromagnetic transient (EMT) modeling tools have been identiﬁed as one of the most important requirements in replicating, analyzing, and investigating the dynamics of the power grid with photovoltaic (PV) plants. However, there are no benchmark models for power grid with PVs to investigate emerging challenges with higher penetration of PVs (like trips and momentary cessations during faults from a region faraway). To this end, in this paper, benchmark high- ﬁdelity EMT dynamic models of power grid with large-scale PV plants are presented. The models are developed in PSCAD and PSCAD/Fortran. Simulation results for different use cases (events) and scenarios are presented. Index Terms—PV plant, EMT simulation, PV inverter. I. INTRODUCTION The penetration of large-scale inve

## 核心贡献


- 提出含多光伏电站的IEEE-39节点系统高保真EMT基准模型并开源
- 采用Kron降阶与多阶离散化技术显著提升大规模光伏阵列仿真计算速度
- 构建匹配实际硬件时序的多速率分层控制架构实现控制器协同仿真


## 使用的方法


- [[微分代数方程|微分代数方程]]
- [[二阶梯形积分|二阶梯形积分]]
- [[kron降阶法|Kron降阶法]]
- [[dae聚类与聚合|DAE聚类与聚合]]
- [[多阶离散化|多阶离散化]]
- [[混合离散化|混合离散化]]
- [[多速率仿真|多速率仿真]]
- [[lu分解|LU分解]]


## 涉及的模型


- [[光伏电站|光伏电站]]
- [[光伏逆变器|光伏逆变器]]
- [[电站级控制器|电站级控制器]]
- [[变压器|变压器]]
- [[架空输电线路|架空输电线路]]
- [[地下电缆|地下电缆]]
- [[并联电容器|并联电容器]]
- [[ieee-39节点系统|IEEE-39节点系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[高比例光伏并网|高比例光伏并网]]
- [[逆变器并网资源建模|逆变器并网资源建模]]
- [[故障扰动分析|故障扰动分析]]
- [[多速率控制|多速率控制]]
- [[仿真加速技术|仿真加速技术]]
- [[基准模型开发|基准模型开发]]


## 主要发现


- 模型在多种故障与短路比场景下准确复现高渗透率光伏集群的部分功率损失动态
- Kron降阶与混合离散化有效缩减矩阵规模显著提升大规模光伏EMT仿真速度
- 多速率控制架构匹配实际硬件时序成功验证逆变器保护与电站级控制的协同仿真



## 方法细节

### 方法概述

本文提出面向高比例光伏电网的高保真电磁暂态（EMT）基准建模方法。首先基于实际组件参数（变压器阻抗、馈线L/C、滤波器、直流母线电容及阵列V-I特性）构建详细硬件拓扑。针对配电网络微分代数方程（DAE），采用二阶梯形积分法进行离散化，生成线性方程组$Ax=b$，其系数矩阵呈箭头型或双边界块对角结构。为突破大规模矩阵逐时间步求解的计算瓶颈，引入Kron降阶法消除内部节点，结合DAE聚类聚合、多阶离散化及基于数值刚度的混合离散化技术大幅缩减矩阵维度。控制层构建匹配实际硬件时序的多速率分层架构，逆变器控制器与电站级控制器（PPC）采用差异化步长协同运行，并集成交流过流、相过压及直流过压保护逻辑。最终将三座不同拓扑与容量的光伏电站接入IEEE-39节点系统，在PSCAD/Fortran环境中完成全系统高保真动态仿真。

### 数学公式


**公式1**: $$Ax = b$$

*通过二阶梯形积分法对配电网络/电缆的DAE进行离散化后得到的线性方程组，其中A为箭头型或双边界块对角稀疏矩阵，x为状态变量向量，b为激励向量。*


**公式2**: $$A_{\text{reduced}} = A_{BB} - A_{BI}A_{II}^{-1}A_{IB}$$

*Kron降阶法的核心矩阵运算公式，通过消去内部节点(I)保留边界节点(B)，将完整系统矩阵缩减为低维等效矩阵，显著降低LU分解的计算复杂度。*


### 算法步骤

1. 1. 组件参数提取与拓扑构建：收集变压器阻抗、馈线电感电容、滤波器参数、直流母线电容及光伏阵列V-I特性曲线，建立包含多逆变器模块、馈线、变压器及并联电容器的光伏电站详细硬件模型。

2. 2. DAE离散化与稀疏矩阵生成：对配电线路/电缆建立微分代数方程，采用二阶梯形积分法进行数值离散，形成线性系统$Ax=b$，并识别矩阵A的箭头型或双边界块对角稀疏结构。

3. 3. 矩阵降阶与数值加速：应用Kron降阶法对矩阵A执行节点消去操作，仅保留外部端口节点；结合DAE聚类聚合技术、多阶离散化策略及基于数值刚度的混合离散化算法，优化大规模系统的求解效率。

4. 4. 多速率控制与保护逻辑部署：配置逆变器控制步长（50–100 µs）与PPC控制步长（100–1000 ms），实现分层时序协同；在控制器中嵌入交流侧过流、交流相过压及直流母线过压三重保护算法。

5. 5. 系统集成与迭代求解：将三个不同配置的PV模型接入IEEE-39节点系统，在PSCAD/Fortran底层调用LU分解与前代回代算法，按多速率时间步进行逐周期电磁暂态迭代求解。


### 关键参数

- **逆变器控制步长**: 50–100 µs

- **PPC控制步长**: 100–1000 ms

- **IBR-1额定容量与配置**: 125 MW (50台1MW逆变器 + 30台2.5MW逆变器)

- **IBR-2额定容量与配置**: 125 MW (25台1MW逆变器 + 40台2.5MW逆变器)

- **IBR-3额定容量与配置**: 250 MW (双模块共59台1MW逆变器 + 54台2.5MW逆变器)

- **馈线与线路拓扑**: IBR-1/3为不对称馈线+不对称线路，IBR-2为不对称馈线+对称线路

- **电网接入节点**: IBR-1接Bus 1, IBR-2接Bus 3, IBR-3接Bus 30



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 不同位置线间故障扰动 (F-1, F-2, F-3) | 故障触发时间均为t=0.9932s。故障前稳态功率：IBR-1≈115 MW，IBR-2≈110 MW，IBR-3≈230 MW。F-1(L29)故障时，三站均出现部分有功功率损失；F-2(L28)故障因距IBR-1极近，IBR-1有功功率完全丧失(降至0 MW)，IBR-2/3部分损失；F-3(L16)故障因电气距离远，三站仅出现极小部分功率下降(估算<5%)。 | 与传统同步机主导电网故障时‘邻近电站完全脱网’的行为不同，该模型准确复现了高渗透率光伏集群‘部分功率损失’的分布式动态特征，与NERC加州实际扰动报告完全一致。 |

| 低短路比(SCR)弱电网工况 | 原系统SCR为B1=25, B3=27.5, B30=15；通过延长线路长度将SCR降至B1=10, B3=9, B30=8。在t=1.0s触发F-1线间故障，故障前IBR-2≈115 MW，IBR-3≈230 MW。低SCR下，IBR-2有功基本保持稳定，而IBR-3出现显著有功功率跌落，且跌落幅度明显高于高SCR工况。 | 相比高SCR基准工况，低SCR(8-10)场景下远端光伏电站(IBR-3)的故障穿越能力显著下降，有功功率损失比例增加约30%-40%，验证了弱电网对光伏集群动态稳定性的负面影响。 |



## 量化发现

- 多速率控制架构实现逆变器(50-100 µs)与PPC(100-1000 ms)的硬件级时序匹配，控制步长跨度达1000倍。
- 故障前稳态运行点精确设定为：IBR-1≈115 MW，IBR-2≈110 MW，IBR-3≈230 MW，总并网容量达470 MW。
- 短路比从25/27.5/15降至10/9/8后，相同故障位置下IBR-3的有功功率跌落幅度显著增大，验证了SCR<10时弱电网对逆变器稳定性的强约束。
- Kron降阶与混合离散化技术将双边界块对角矩阵规模大幅缩减，LU分解计算复杂度呈非线性下降，显著提升大规模光伏阵列EMT仿真速度。
- 故障电气距离与功率损失呈强正相关：极近故障(F-2)导致IBR-1功率降至0 MW，远距离故障(F-3)功率损失<5%，精准复现实际电网扰动特征。


## 关键公式

### 二阶梯形积分离散化线性系统

$$Ax = b$$

*用于配电网络/电缆DAE的数值离散，是EMT仿真中每个时间步求解网络状态的核心方程。*

### Kron降阶等效矩阵公式

$$A_{\text{reduced}} = A_{BB} - A_{BI}A_{II}^{-1}A_{IB}$$

*在大规模光伏阵列仿真中用于消除内部节点，保留边界端口，加速稀疏矩阵的LU分解与前代回代过程。*



## 验证详情

- **验证方式**: PSCAD全系统EMT仿真验证与NERC现场扰动事件行为对比分析
- **测试系统**: IEEE-39节点系统接入三个不同拓扑、容量与逆变器配置的大型光伏电站(IBR-1/2/3)
- **仿真工具**: PSCAD, PSCAD/Fortran
- **验证结果**: 模型成功复现了高渗透率光伏集群在电网故障下的‘部分功率损失’而非‘完全脱网’的动态特性。仿真结果表明，功率损失程度与故障电气距离高度相关，且在低短路比（弱电网）工况下，远端光伏电站的功率跌落更为显著。所有仿真波形与实际电网观测到的扰动特征完全一致，验证了基准模型的高保真度、计算效率及工程适用性。
