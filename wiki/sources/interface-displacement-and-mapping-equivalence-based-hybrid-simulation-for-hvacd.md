---
title: "Interface Displacement and Mapping Equivalence Based Hybrid Simulation for HVAC/DC Power Grids"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.3017084"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/24/TPWRD.2020.3017084.pdf.pdf"]
---

# Interface Displacement and Mapping Equivalence Based Hybrid Simulation for HVAC/DC Power Grids

**作者**: 
**年份**: 2020
**来源**: `24/TPWRD.2020.3017084.pdf.pdf`

## 摘要

—In the electromagnetic transient (EMT) and transient stability (TS) hybrid simulation, the entire power system is artificially split into two sub-grids, and sub-grids interact with each other via an interface. Thus interface distortions emerge, including latency and errors. The influence of interface latency is quantitated based on a demo circuit containing delayed interaction. Moreover, the principles of improving hybrid simulation interface accuracy are concluded. Inspired by the principles, a novel interface displacement (ID) and dynamic phasor mapping equivalence (DP-ME) interface scheme is proposed. The scheme makes sub-grids at opposite sides of an interface loosely coupled and avoids interface variable form conversion by applying two techniques. 1) Displacement of the partition int

## 核心贡献


- 提出接口位移技术将分区边界移至控制回路内部利用内置惯性实现松耦合
- 构建动态相量映射等效模型直接计算注入功率避免变量形式转换引入的延迟
- 基于Lambert W函数量化延迟影响机理推导提升混合仿真精度的理论原则


## 使用的方法


- [[动态相量法|动态相量法]]
- [[混合仿真|混合仿真]]
- [[接口位移技术|接口位移技术]]
- [[lambert-w函数分析|Lambert W函数分析]]
- [[网络等值|网络等值]]


## 涉及的模型


- [[换流器|换流器]]
- [[交流系统等值模型|交流系统等值模型]]
- [[可控电流源|可控电流源]]
- [[交直流电网|交直流电网]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[接口延迟|接口延迟]]
- [[交直流电网|交直流电网]]
- [[动态相量映射|动态相量映射]]
- [[网络分区|网络分区]]


## 主要发现


- 接口位移结合动态相量映射方案有效消除转换延迟显著提升混合仿真接口精度
- 实际交直流电网测试表明该方案结果与全电磁暂态仿真高度吻合验证了有效性
- 量化分析证实接口延迟引发特征根偏移利用内置惯性可大幅降低对稳定性的影响



## 方法细节

### 方法概述

本文提出一种基于接口位移（Interface Displacement, ID）与动态相量映射等效（Dynamic Phasor Mapping Equivalence, DP-ME）的EMT/TS混合仿真新架构。传统混合仿真通常在换流器母线处进行网络分区，需通过FFT或最小二乘法将EMT瞬时波形转换为TS基频相量，不可避免地引入至少一个基频周期的延迟及波形畸变。本方法首先将分区边界从换流器母线向EMT子网内部控制回路及内部移动，利用控制系统固有的低通滤波特性与内置惯性实现两侧子网的松耦合。其次，在位移后的接口处构建DP-ME等效模型，直接计算EMT向TS子网注入的功率，彻底规避变量形式转换过程。结合非迭代并行交互协议，该方案在保持计算效率的同时，从机理上消除了接口延迟与转换误差，并通过Lambert W函数量化分析验证了其对系统特征根偏移的抑制作用。

### 数学公式


**公式1**: $$$$u(s) = (R_1 + sL + R_2)i(s)$$$$

*线性化演示电路的动态方程，描述无延迟情况下TS侧电压源与EMT侧等效电流源之间的频域关系。*


**公式2**: $$$$\lambda_0 = -\frac{R_1 + R_2}{L}$$$$

*无延迟混合仿真系统的特征根，反映系统固有衰减特性。*


**公式3**: $$$$u(s) = (R_1 + sL) \times i(s) + R_2 \times i(s) \times e^{-\tau s}$$$$

*含接口总延迟$\tau$的系统特征方程，指数项$e^{-\tau s}$表征分区与变量转换引入的时滞效应。*


**公式4**: $$$$\lambda' = -\frac{R_1}{L} + W\left(-\frac{\tau e^{\tau R_1/L}}{L/R_2}\right) = -\frac{R_1}{L} + \frac{1}{\tau}W(z)$$$$

*基于Lambert W函数求得的含延迟系统特征根解析解，用于精确量化延迟$\tau$对系统稳定性的影响。*


### 算法步骤

1. 步骤1：系统分区与接口位移。将传统位于换流器交流母线的物理接口向EMT子网内部控制环路内部移动，利用控制器的数字滤波与响应惯性作为天然缓冲层，使EMT与TS子网在电气上实现松耦合。

2. 步骤2：构建DP-ME等效模型。在位移后的新接口处建立动态相量映射等效电路，直接读取EMT侧的瞬时电压/电流，通过等效阻抗网络实时计算注入TS侧的有功与无功功率，跳过FFT窗口与相量提取环节。

3. 步骤3：并行交互与数据同步。采用非迭代并行协议，TS侧以毫秒级步长提供基频等值戴维南/诺顿模型，EMT侧以微秒级步长运行。两侧在每个TS步长结束时通过DP-ME模型交换功率边界条件，无需等待相量转换完成。

4. 步骤4：延迟量化与稳定性校验。利用Lambert W函数解析计算接口延迟$\tau$引起的特征根偏移量$\Delta \lambda$，验证位移后接口延迟是否处于系统稳定裕度内，若满足条件则继续推进仿真，否则调整位移深度或等效参数。


### 关键参数

- **\tau**: 接口总延迟（含网络分区交互延迟与变量形式转换延迟，传统方法约20ms）

- **R_1, L, R_2**: 演示电路等效参数，分别代表TS侧内阻、线路电感与EMT侧等效内阻

- **W(z)**: Lambert W函数，用于求解含时滞超越方程的特征根，z为与延迟和电路参数相关的复变量

- **\lambda_0, \lambda'**: 无延迟与含延迟系统的特征根，用于评估接口延迟对数值稳定性的影响



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 设计的线性演示电路测试 | 通过Lambert W函数精确量化接口延迟$\tau$对特征根的影响。理论计算表明，当$\tau$控制在毫秒级时，特征根实部偏移量$\Delta \lambda$可通过解析式直接求得，验证了延迟导致系统响应发散或收敛变慢的机理。 | 相比传统非迭代协议引入的固定延迟，ID方案利用控制惯性将等效时间常数提升，使特征根偏移敏感度降低约1个数量级。 |

| 实际交直流电网混合仿真测试 | 在包含多回HVDC线路的实际电网中应用ID&DP-ME方案。仿真波形与全EMT仿真结果高度吻合，成功消除了传统方法中因FFT转换导致的约20ms延迟及高频分量丢失问题，接口功率交换误差显著降低。 | 与传统基频相量转换接口相比，本方案避免了1个基频周期的转换等待时间，接口数据交换延迟从~20ms降至微秒级控制步长同步延迟，整体仿真精度与全EMT基准的偏差控制在工程可接受范围内。 |



## 量化发现

- 传统接口变量转换（FFT/最小二乘）必然引入至少1个基频周期（约20ms）的固定延迟，且波形扰动时拟合误差显著增大。
- 含延迟系统的特征根由$\lambda_0 = -(R_1+R_2)/L$偏移至$\lambda' = -R_1/L + W(z)/\tau$，延迟$\tau$与特征根实部呈非线性映射关系，可通过Lambert W函数精确解析。
- 接口位移至控制回路内部后，利用控制系统的内置低通惯性，等效时间常数增大，使延迟对系统稳定性的影响呈指数级衰减。
- DP-ME模型实现瞬时值到注入功率的直接映射，彻底消除相量转换环节，接口数据交换延迟从毫秒级降至微秒级同步步长。


## 关键公式

### 含接口延迟的系统特征方程

$$$$u(s) = (R_1 + sL) \times i(s) + R_2 \times i(s) \times e^{-\tau s}$$$$

*用于分析非迭代并行交互协议下，网络分区与变量转换引入的总延迟$\tau$对系统动态响应的影响机理。*

### 基于Lambert W函数的延迟特征根解析解

$$$$\lambda' = -\frac{R_1}{L} + \frac{1}{\tau}W(z)$$$$

*在量化接口延迟对混合仿真稳定性影响时使用，提供超越方程的精确解析解，指导接口位移深度与延迟容忍度的设计。*



## 验证详情

- **验证方式**: 理论机理推导+对比仿真验证
- **测试系统**: 抽象线性演示电路（含电压源、电感、等效电流源）及实际交直流混合电网（含多端HVDC换流器与大规模交流网架）
- **仿真工具**: EMT/TS混合仿真平台（文中未明确具体商业软件，通常基于PSCAD/EMTDC与机电暂态程序联合架构）
- **验证结果**: 理论推导证实接口延迟导致特征根偏移的解析规律；实际电网测试表明，ID&DP-ME方案有效消除了传统接口的转换延迟与波形畸变，仿真轨迹与全EMT基准高度一致，验证了该架构在提升混合仿真接口精度与稳定性方面的有效性。
