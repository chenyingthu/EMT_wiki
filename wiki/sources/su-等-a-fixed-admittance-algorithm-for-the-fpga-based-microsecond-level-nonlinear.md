---
title: "Su 等 | A fixed-admittance algorithm for the FPGA-based microsecond-level nonlinear real-time simulation of"
type: source
authors: ['Zhai Fang']
year: 2025
journal: ""
tags: ['fixed-admittance', 'real-time', 'fpga']
created: "2026-04-13"
sources: ["EMT_Doc/01/Su 等 - 2025 - A fixed-admittance algorithm for the FPGA-based microsecond-level nonlinear real-time simulation of.pdf"]
---

# Su 等 | A fixed-admittance algorithm for the FPGA-based microsecond-level nonlinear real-time simulation of

**作者**: Zhai Fang
**年份**: 2025
**来源**: `01/Su 等 - 2025 - A fixed-admittance algorithm for the FPGA-based microsecond-level nonlinear real-time simulation of.pdf`

## 摘要

—The hybrid high-voltage DC circuit breaker (DCCB) is equipment with the typical nonlinear response in fault-clearing. As an alternative or prior step to drive and control system testing, it is necessary to perform real-time simulations of the DCCB, which improves safety compared to circuit experiments. The response of equipment containing nonlinear components, represented by the DCCB, is more complex, with time scales of milliseconds or even microseconds. The key to realizing nonlinear real-time simulation is to efficiently and accurately solve circuits with nonlinear/time-varying components. In this paper, the concept

## 核心贡献

- 采用恒导纳ADC模型避免导纳矩阵重构，适用于实时仿真
- 实现了real-time仿真方法，满足硬件在环测试的实时性要求

## 使用的方法

- [[fixed-admittance]]

## 涉及的模型

- [[混合高压直流断路器-dccb|混合高压直流断路器(DCCB)]]
- [[金属氧化物压敏电阻-mov|金属氧化物压敏电阻(MOV)]]
- [[rlc等效行为模型|RLC等效行为模型]]

## 相关主题

- [[real-time-simulation]]

## 主要发现

—The hybrid high-voltage DC circuit breaker (DCCB) is equipment with the typical nonlinear response in fault-clearing

## 方法细节

### 方法概述

本文提出了基于虚拟元件的电磁暂态（VC-EMT）非线性实时仿真方法。核心创新是通过引入"虚拟元件"（virtual component）进行等效电路变换，将非线性/时变元件与虚拟开关并联，使得网络导纳矩阵保持恒定。具体而言，对于非线性电阻（如MOV），将其等效为时变导纳Yn(t)与虚拟开关导纳Yv(t)的并联组合，通过设计使得Yn(t) + Yv(t) = Yc（常数），从而在整个仿真过程中无需更新导纳矩阵的LU分解。该方法避免了传统电流源替代法的补偿滞后、补偿法的迭代计算以及分段线性法的矩阵频繁切换问题，适用于FPGA-based微秒级实时仿真。

### 数学公式


**公式1**: $$$G_n \cdot V_n(t) = M \cdot [I_h(t) + I_{inj}(t)]$$$

*电磁暂态仿真的广义节点分析方程，其中Gn为等效导纳矩阵，Vn(t)为节点电压向量，Ih(t)为历史电流源向量，Iinj(t)为注入电流源向量，M为关联矩阵*


**公式2**: $$$Y_n(t) + Yv(t) = Y_c$$$

*虚拟元件法的核心约束条件，确保非线性元件导纳Yn(t)与虚拟元件导纳Yv(t)之和恒为常数Yc，从而保持系统导纳矩阵不变*


**公式3**: $$$Y_c \geq \max\{Y_n(t), Y_v(t)\}$$$

*导纳常数Yc的选取约束，确保Yc不小于非线性导纳和虚拟导纳的最大值，保证实现可行性*


**公式4**: $$$I_{eq}(t) = I_h(t) + I_{virtual}(t)$$$

*等效历史电流源计算，通过调整虚拟元件的历史电流源Ivirtual(t)来补偿非线性特性变化，保持诺顿等效电路的一致性*


### 算法步骤

1. 电路预处理：识别网络中的非线性元件（如MOV、非线性电阻等），确定其时变导纳范围Yn(t)∈[Yn_min, Yn_max]

2. 虚拟构造：对每个非线性元件并联一个虚拟开关（断开状态），设计虚拟导纳Yv(t)使得Yn(t) + Yv(t) = Yc（常数），其中Yc ≥ max(Yn(t))

3. 诺顿等效转换：将非线性元件-虚拟元件组合转换为诺顿等效电路，计算等效导纳Geq = Yc和历史电流源Ih(t)

4. 导纳矩阵构建：基于恒定导纳Yc构建整个网络的导纳矩阵Gn，并在初始化阶段完成LU分解

5. 实时仿真循环（每时间步Δt=1μs）：(a) 根据当前非线性元件状态计算Yn(t)；(b) 计算虚拟元件历史电流源Ivirtual(t) = (Yc - Yn(t))·V(t-Δt) - Ih_nonlinear(t)；(c) 更新历史电流源向量Ih(t)；(d) 通过前代回代求解线性方程组Gn·Vn(t) = M·Ih(t)，得到节点电压；(e) 计算支路电流并更新历史电流源供下一步使用

6. 并行优化：利用FPGA的并行计算能力，对历史电流源更新和节点电压求解进行流水线处理，降低单步执行时间


### 关键参数

- **simulation_time_step**: 1 μs

- **test_system_voltage**: 500 kV

- **test_system_current**: 25 kA

- **maximum_admittance_error**: < 0.5%

- **virtual_component_type**: 并联断开开关（高阻态）

- **integration_method**: 梯形法（隐含在历史电流源计算中）

- **hardware_platform**: FPGA（Field-Programmable Gate Array）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 500kV/25kA混合DCCB故障开断全过程 | 仿真涵盖了电流上升阶段、缓冲电路充电阶段、能量吸收阶段和振荡阶段，包括两次子模块换流和两次支路换流过程。MOV在第二次支路换流开始时投入，整个过程在数毫秒内完成，其中换流持续时间约为数十至数百微秒 | 与传统电流源替代法（CSS）相比，避免了补偿滞后；与补偿法相比，无需网络解耦和迭代计算；与分段线性法相比，无需频繁切换导纳矩阵和插值处理 |

| MOV非线性特性验证 | 在分支换流过程和能量吸收阶段，MOV被等效为串联非线性RL电路；在振荡阶段，MOV被建模为并联RC电路。虚拟元件方法在两种建模方式下均保持了导纳矩阵恒定 | 与PSCAD/EMTDC离线仿真结果对比，最大误差小于0.5%，在1μs步长下实现了等效精度 |



## 量化发现

- 在1μs时间步长下实现了500kV/25kA混合DCCB的实时仿真，满足微秒级时间尺度要求
- 仿真最大误差小于0.5%（与PSCAD/EMTDC基准对比），在快速暂态过程（kA/μs或kV/μs应力条件）下保持高精度
- 导纳矩阵保持恒定，避免了每步的LU分解更新，计算复杂度从O(n³)降低为O(n²)的前代回代运算
- 消除了传统补偿法的迭代需求，单步计算时间确定，满足实时性硬约束
- 非线性元件占比低（DCCB中主要为MOV和电力电子子模块），虚拟构造仅针对少量非线性支路，存储需求显著低于预存储多组导纳矩阵的方法
- 支持连续、非周期性、不可预测参数变化（如故障清除过程中的MOV特性变化），无需插值抑制数值振荡


## 关键公式

### 恒导纳约束方程

$$$Y_n(t) + Y_v(t) = Y_c$$$

*虚拟元件法的核心，用于将时变非线性导纳转换为恒定等效导纳，适用于非线性电阻、电感、电容的诺顿等效建模*

### 节点分析基本方程

$$$G_n \cdot V_n(t) = M \cdot [I_h(t) + I_{inj}(t)]$$$

*EMT仿真的基础框架，VC-EMT方法通过保持Gn恒定，将矩阵求解转化为固定矩阵的重复前代回代过程*



## 验证详情

- **验证方式**: 对比验证（与商业离线仿真软件PSCAD/EMTDC对比）
- **测试系统**: 500kV/25kA混合高压直流断路器（Hybrid DCCB），包含机械快速开关、电力电子全桥子模块（SMt）和金属氧化物压敏电阻（MOV）
- **仿真工具**: PSCAD/EMTDC（作为基准离线仿真工具），FPGA-based实时仿真平台
- **验证结果**: 在1μs固定步长下，VC-EMT方法准确复现了DCCB故障清除过程中的非线性动态响应，包括MOV的电压钳位特性、能量吸收过程和后续振荡。与PSCAD结果对比显示，电压和电流波形的最大相对误差小于0.5%，验证了方法在微秒级时间尺度的准确性和实时可行性。该方法成功避免了传统方法的补偿滞后和迭代需求，适用于硬件在环（HIL）测试场景。
