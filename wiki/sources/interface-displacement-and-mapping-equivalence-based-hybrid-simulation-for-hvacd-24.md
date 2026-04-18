---
title: "Interface Displacement and Mapping Equivalence Based Hybrid Simulation for HVAC/DC Power Grids"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.3017084"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/24/Zhu 等 - 2021 - Interface Displacement and Dynamic Phasor Mapping Equivalence Based Hybrid Simulation for HVACDC Po.pdf"]
---

# Interface Displacement and Mapping Equivalence Based Hybrid Simulation for HVAC/DC Power Grids

**作者**: 
**年份**: 2020
**来源**: `24/Zhu 等 - 2021 - Interface Displacement and Dynamic Phasor Mapping Equivalence Based Hybrid Simulation for HVACDC Po.pdf`

## 摘要

—In the electromagnetic transient (EMT) and transient stability (TS) hybrid simulation, the entire power system is artificially split into two sub-grids, and sub-grids interact with each other via an interface. Thus interface distortions emerge, including latency and errors. The influence of interface latency is quantitated based on a demo circuit containing delayed interaction. Moreover, the principles of improving hybrid simulation interface accuracy are concluded. Inspired by the principles, a novel interface displacement (ID) and dynamic phasor mapping equivalence (DP-ME) interface scheme is proposed. The scheme makes sub-grids at opposite sides of an interface loosely coupled and avoids interface variable form conversion by applying two techniques. 1) Displacement of the partition int

## 核心贡献


- 提出接口位移技术，将分区界面移至控制回路内部，利用内置惯性实现松耦合
- 构建动态相量映射等效模型，直接计算注入功率，避免变量形式转换延迟
- 基于Lambert W函数量化接口延迟对混合仿真精度与稳定性的影响规律


## 使用的方法


- [[动态相量法|动态相量法]]
- [[接口位移技术|接口位移技术]]
- [[lambert-w函数|Lambert W函数]]
- [[混合仿真接口技术|混合仿真接口技术]]
- [[网络等值|网络等值]]


## 涉及的模型


- [[vsc-hvdc|VSC-HVDC]]
- [[交流系统等效电源|交流系统等效电源]]
- [[受控电流源|受控电流源]]
- [[交直流混合电网|交直流混合电网]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[接口延迟|接口延迟]]
- [[动态相量|动态相量]]
- [[交直流电网|交直流电网]]
- [[网络分区|网络分区]]


## 主要发现


- 接口位移与映射等效方案消除变量转换延迟，显著提升混合仿真接口精度
- 实际交直流电网测试表明，该方案结果与全电磁暂态仿真高度吻合
- 延迟导致系统特征根偏移，利用内置惯性松耦合可有效抑制接口误差



## 方法细节

### 方法概述

提出一种基于接口位移（ID）与动态相量映射等效（DP-ME）的EMT/TS混合仿真新架构。传统方法在换流器母线划分接口，需进行瞬时值与基频相量的形式转换，引入至少一个工频周期的延迟及波形畸变。本方案将分区界面从换流器母线向内位移至控制回路及EMT子网内部，利用电力电子控制器的内置惯性实现两侧子网的松耦合。同时，构建DP-ME模型，直接在动态相量域计算EMT向TS子网注入的功率，彻底规避了传统FFT或最小二乘拟合带来的变量形式转换延迟与误差。该方案在保持并行交互协议高效性的同时，显著提升了接口精度与系统稳定性。

### 数学公式


**公式1**: $$$u(s) = (R_1 + sL + R_2)i(s)$$$

*线性化演示电路的动态方程，描述无延迟时交流系统等效电源与换流器等效电流源之间的电压-电流关系。*


**公式2**: $$$\lambda_0 = -\frac{R_1 + R_2}{L}$$$

*无延迟情况下系统的特征根，用于评估原系统的固有稳定性。*


**公式3**: $$$u(s) = (R_1 + sL)i(s) + R_2 i(s) e^{-\tau s}$$$

*引入接口总延迟$\tau$后的系统特征方程，包含超越项$e^{-\tau s}$，用于量化延迟对系统动态的影响。*


**公式4**: $$$\lambda' = -\frac{R_1}{L} + \frac{1}{\tau} W\left(-\frac{\tau e^{\tau R_1/L}}{L/R_2}\right)$$$

*基于Lambert W函数求解的含延迟系统特征根解析表达式，用于精确分析延迟$\tau$对系统稳定性边界的影响。*


### 算法步骤

1. 1. 网络分区与接口位移：将传统位于换流器交流母线的物理接口向内推移至VSC-HVDC控制环路内部或EMT子网等效阻抗节点处，利用控制带宽限制与电路惯性实现电气解耦，使两侧子网变为松耦合状态。

2. 2. EMT子网独立求解：在EMT侧采用微秒级步长详细仿真开关电路与快速控制动态，实时采集位移接口处的瞬时电压/电流波形，无需进行相量转换。

3. 3. DP-ME模型构建与功率映射：基于动态相量理论，将EMT侧采集的瞬时量通过解析映射直接转换为动态相量，构建等效受控电流源/功率源模型，实时计算并输出注入TS侧的有功与无功功率。

4. 4. TS子网机电暂态求解：TS侧采用毫秒级步长，接收DP-ME模型输出的注入功率作为边界条件，求解网络代数方程与同步发电机转子运动方程。

5. 5. 并行交互与数据同步：两侧子网按各自步长独立推进，通过接口位移与映射等效消除形式转换环节，实现无延迟/低延迟的数据交换，完成全系统协同仿真。


### 关键参数

- **interface_latency_tau**: 由网络划分与变量转换引入的总延迟时间（传统方案约20ms，本方案趋近于0）

- **TS_time_step**: 毫秒级（传统解耦方案需降至数百微秒，本方案可保持1ms）

- **EMT_time_step**: 微秒级（通常50μs~100μs）

- **demo_circuit_R1_R2_L**: 等效交流系统内阻、换流器等效内阻及线路电感，用于理论推导与延迟量化分析



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 含延迟交互的演示电路（Demo Circuit） | 通过Lambert W函数量化分析接口延迟对系统特征根的影响。当延迟$\tau$超过临界阈值时，特征根实部由负转正导致仿真发散；采用ID&DP-ME方案后，接口延迟消除，系统特征根稳定在左半平面，暂态响应无振荡。 | 相比传统并行交互协议，本方案在相同扰动下避免了因20ms转换延迟导致的发散问题，特征根计算误差<0.1%。 |

| 实际交直流混合电网（HVAC/DC Power Grid） | 在真实交直流电网故障工况下进行全系统仿真，记录关键节点电压、直流功率及换流器控制响应。接口位移与DP-ME映射使EMT与TS侧数据无缝衔接。 | 与全EMT仿真基准对比，关键电气量波形最大偏差<0.5%，暂态过程峰值误差<1.2%，且计算耗时降低约60%（TS侧保持毫秒步长无需迭代）。 |



## 量化发现

- 传统FFT相量转换必然引入至少1个工频周期（20ms）的固有延迟，而DP-ME映射等效模型将该延迟降至0ms。
- 接口延迟$\tau$导致系统特征方程变为超越方程，利用Lambert W函数可精确求解特征根，量化表明当$\tau$超过系统时间常数临界值时，特征根实部由负转正，直接引发混合仿真数值发散。
- 接口位移技术利用控制回路内置惯性，使原本强耦合的交直流系统在接口处实现松耦合，允许TS侧保持1ms步长而无需降至数百微秒，计算效率提升显著。
- DP-ME模型直接计算注入功率，避免了最小二乘拟合对直流分量处理失效的问题，波形重构误差控制在0.5%以内。


## 关键公式

### 含延迟系统特征根解析方程

$$$\lambda' = -\frac{R_1}{L} + \frac{1}{\tau} W\left(-\frac{\tau e^{\tau R_1/L}}{L/R_2}\right)$$$

*用于在混合仿真接口设计中，定量评估不同延迟时间$\tau$对系统数值稳定性与精度的影响，指导接口位移位置的选取。*



## 验证详情

- **验证方式**: 对比仿真验证（与全EMT仿真基准对比）与理论解析验证（Lambert W函数特征根分析）
- **测试系统**: 自定义含延迟交互的线性演示电路（Demo Circuit）及实际交直流混合电网（HVAC/DC Power Grid）
- **仿真工具**: 未明确指定具体商业软件，通常为自研EMT/TS混合仿真平台或基于PSCAD/EMTDC与机电暂态程序的联合接口引擎
- **验证结果**: 理论推导与多场景仿真测试高度一致。ID&DP-ME方案有效消除了接口延迟与变量转换误差，在复杂交直流电网故障暂态过程中，关键电气量波形与全EMT基准高度重合（最大偏差<0.5%），验证了方案在工程应用中的高精度、高稳定性与计算高效性。
