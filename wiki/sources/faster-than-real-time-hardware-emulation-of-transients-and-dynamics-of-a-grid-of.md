---
title: "Faster-Than-Real-Time Hardware Emulation of Transients and Dynamics of a Grid of Microgrids"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Open Access Journal of Power and Energy;2023;10; ;10.1109/OAJPE.2022.3217601"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Cao 等 - 2023 - Faster-Than-Real-Time Hardware Emulation of Transients and Dynamics of a Grid of Microgrids.pdf"]
---

# Faster-Than-Real-Time Hardware Emulation of Transients and Dynamics of a Grid of Microgrids

**作者**: 
**年份**: 2023
**来源**: `19、20、21/EMT_task_19/Cao 等 - 2023 - Faster-Than-Real-Time Hardware Emulation of Transients and Dynamics of a Grid of Microgrids.pdf`

## 摘要

Enhanced environmental standards are leading to an increasing proportion of microgrids (MGs) being integrated with renewable energy resources in modern power systems, which brings new challenges to simulate such a complex system. In this work, comprehensive modeling of a grid of microgrids for faster-than-real-time (FTRT) emulation is proposed, which can be utilized in the energy control center for contingencies analysis and dynamic security assessment. Electromagnetic transient (EMT) modeling is applied to the microgrid in order to reﬂect the detailed device processes of the converter and renewable energy sources, while the AC grid utilizes the transient stability modeling to reduce the computational burden and obtain a high acceleration value over real-time execution. Consequently, a dyn

## 核心贡献


- 提出微电网EMT与主网暂态稳定混合建模架构，实现多尺度仿真共存。
- 设计动态电压注入接口策略，显著降低跨域数据通信开销与硬件资源占用。
- 基于FPGA并行计算架构实现超实时硬件仿真，系统加速比达51倍。


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[暂态稳定仿真|暂态稳定仿真]]
- [[动态电压注入接口|动态电压注入接口]]
- [[fpga并行计算|FPGA并行计算]]
- [[超实时仿真|超实时仿真]]


## 涉及的模型


- [[微电网|微电网]]
- [[光伏阵列|光伏阵列]]
- [[双馈感应发电机|双馈感应发电机]]
- [[电池储能系统|电池储能系统]]
- [[交流主网|交流主网]]
- [[电力电子变流器|电力电子变流器]]


## 相关主题


- [[超实时仿真|超实时仿真]]
- [[混合仿真|混合仿真]]
- [[并行计算|并行计算]]
- [[动态安全评估|动态安全评估]]
- [[硬件在环仿真|硬件在环仿真]]
- [[微电网群建模|微电网群建模]]


## 主要发现


- 三组案例仿真结果与Matlab/Simulink离线工具高度吻合，验证模型精度。
- FPGA平台实现51倍超实时加速，满足控制中心动态安全评估与故障分析需求。
- 动态注入接口有效隔离双仿真域，大幅降低通信延迟与硬件逻辑资源消耗。



## 方法细节

### 方法概述

本文提出一种面向微电网群的超实时（FTRT）硬件仿真架构。针对微电网内部电力电子变流器与可再生能源设备的快速开关动态，采用电磁暂态（EMT）建模以保留器件级细节；针对外部交流主网的大规模机电动态，采用暂态稳定（TS）建模以显著降低计算负担。为解决多尺度模型耦合难题，设计动态电压注入接口策略，实现EMT与TS仿真域之间的低延迟数据交互。利用FPGA的可重构性与高度并行计算能力，将线性化后的节点导纳矩阵与历史电流源模型映射至多块FPGA板卡，通过硬件级并行流水线与固定步长求解器，实现整体系统51倍于实时速度的超实时硬件仿真，为能量控制中心的故障预演与动态安全评估提供高效计算平台。

### 数学公式


**公式1**: $$$I_{pv} = N_p i_{irr} - N_p I_0 \left(e^{\frac{V_{pv}(t) + N_s N_p^{-1} R_s I_{pv}(t)}{N_s V_T}} - 1\right) - \frac{I_{pv}(t)R_s + N_p N_s^{-1} V_{pv}(t)}{R_p}$$$

*光伏阵列非线性输出电流方程，用于精确描述光伏电池在光照与温度变化下的伏安特性*


**公式2**: $$$G_{PVarray} = \frac{N_p (G_{dio} + G_p)}{N_s (G_{dio} R_s + R_s G_p) + N_s}$$$

*光伏阵列诺顿等效电导，将非线性电路线性化为两节点等效电路，便于FPGA并行节点导纳矩阵求解*


**公式3**: $$$J_{PVarray} = \frac{N_p (i_{irr} - I_{Deq})}{G_{dio} R_s + R_s G_p + 1}$$$

*光伏阵列诺顿等效电流源，配合等效电导构成历史电流源模型，实现EMT仿真中的递推计算*


**公式4**: $$$G_{dio} = \frac{\partial i_{dio}}{\partial v_{dio}} = \frac{I_0 \cdot e^{\frac{v_{dio}(t)}{V_T}}}{V_T}$$$

*反并联二极管动态电导，用于非线性元件的伴随电路线性化处理*


**公式5**: $$$I_{Deq} = i_{dio} - G_{dio} \cdot v_{dio}$$$

*二极管等效历史电流源，用于补偿线性化过程中的非线性误差*


### 算法步骤

1. 建立微电网组件EMT模型：对光伏阵列、电池储能系统（BESS）及电力电子变流器进行详细电路级建模，利用诺顿等效与伴随电路法将非线性元件（如二极管、电池内阻）线性化为时变电导与电流源。

2. 建立交流主网暂态稳定模型：采用相量域或机电暂态模型描述主网动态，降低状态变量维度与计算复杂度，仅保留关键机电振荡模态。

3. 设计动态电压注入接口：在EMT微电网与TS主网边界处，通过实时提取主网节点电压/功率，经坐标变换与插值后注入微电网端口，实现多时间尺度数据同步与低延迟通信。

4. FPGA硬件映射与并行划分：将线性化后的节点导纳矩阵分解，利用FPGA的DSP切片与BRAM资源构建并行求解流水线，分配固定仿真步长（亚微秒级），实现多模块同步计算。

5. 超实时执行与闭环验证：在FPGA集群上以51倍速运行仿真，通过高速接口输出数据，并与Matlab/Simulink离线结果进行交叉验证，确保数值稳定性与精度。


### 关键参数

- **仿真步长**: 亚微秒级（sub-microsecond range）

- **系统加速比**: 51倍（Faster-Than-Real-Time）

- **硬件平台**: 多FPGA板卡并行架构

- **接口策略**: 动态电压注入接口

- **微电网核心组件**: 光伏阵列(PV)、双馈感应发电机(DFIG)、电池储能系统(BESS)、电力电子变流器



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 微电网群并网运行与故障扰动 | 在集成光伏、DFIG与BESS的微电网群中注入扰动，系统成功捕捉电力电子开关暂态与主网机电振荡，3个测试案例的仿真波形与离线基准高度一致。 | 相比传统实时仿真工具，计算速度提升51倍，满足动态安全评估的超实时需求。 |

| 多场景并行功率调度分析 | 利用FTRT架构同时运行多个故障与调度场景，验证了系统在能量控制中心进行预防性控制策略评估的可行性，硬件资源占用显著低于商用RTDS等实时仿真器。 | 支持更大规模系统扩展，单FPGA板卡逻辑资源利用率优化，通信延迟降低至微秒级以下。 |

| 接口策略通信开销测试 | 动态电压注入接口有效隔离了EMT与TS求解器，跨域数据交换稳定，未引入数值振荡或发散现象。 | 通信带宽需求显著降低，接口算法使混合仿真在51倍速下稳定运行，误差控制在工程允许范围内。 |



## 量化发现

- 系统整体仿真加速比达到51倍（Faster-Than-Real-Time），远超传统实时仿真器。
- FPGA仿真时间步长达到亚微秒级（sub-microsecond range），满足电力电子开关级EMT精度要求。
- 动态电压注入接口显著降低跨域通信开销与硬件逻辑资源占用，支持多FPGA板卡无缝扩展。
- 三个测试案例的仿真波形与Matlab/Simulink离线基准结果高度吻合，验证了混合建模架构的数值稳定性与工程适用性。


## 关键公式

### 光伏阵列非线性输出电流方程

$$$I_{pv} = N_p i_{irr} - N_p I_0 \left(e^{\frac{V_{pv}(t) + N_s N_p^{-1} R_s I_{pv}(t)}{N_s V_T}} - 1\right) - \frac{I_{pv}(t)R_s + N_p N_s^{-1} V_{pv}(t)}{R_p}$$$

*用于EMT仿真中精确描述光伏电池在光照与温度变化下的伏安特性*

### 光伏阵列诺顿等效电导

$$$G_{PVarray} = \frac{N_p (G_{dio} + G_p)}{N_s (G_{dio} R_s + R_s G_p) + N_s}$$$

*将非线性光伏电路线性化为两节点等效电路，便于FPGA并行节点导纳矩阵求解*

### 光伏阵列诺顿等效电流源

$$$J_{PVarray} = \frac{N_p (i_{irr} - I_{Deq})}{G_{dio} R_s + R_s G_p + 1}$$$

*配合等效电导构成历史电流源模型，实现EMT仿真中的递推计算*



## 验证详情

- **验证方式**: 离线仿真对比验证
- **测试系统**: 含多个微电网（集成光伏、DFIG、BESS）的交流主网互联系统
- **仿真工具**: Matlab/Simulink（离线基准）, FPGA硬件仿真平台（本文方法）
- **验证结果**: 三个典型工况下的EMT-暂态稳定混合仿真结果与Matlab/Simulink离线仿真波形高度吻合，验证了动态电压注入接口的数值稳定性、FPGA并行架构的51倍加速能力以及模型在超实时条件下的工程适用性。
