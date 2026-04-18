---
title: "High performance computing engines for the FPGA-based simulation of the ULM"
type: source
authors: ['Tarek Ould-Bachir']
year: 2020
journal: "Electric Power Systems Research, 190 (2021) 106716. doi:10.1016/j.epsr.2020.106716"
tags: ['fpga']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/j.epsr.2020.106716.pdf.pdf"]
---

# High performance computing engines for the FPGA-based simulation of the ULM

**作者**: Tarek Ould-Bachir
**年份**: 2020
**来源**: `19、20、21/EMT_task_21/j.epsr.2020.106716.pdf.pdf`

## 摘要

High performance computing engines for the FPGA-based simulation of the Tarek Ould-Bachira,⁎,1, Hossein Chalangarb,1, Keyhan Sheshyekanib, Jean Mahseredjianb a Department of Computer Engineering and Software Engineering, Polytechnique Montréal, Montreal, Canada b Department of Electrical Engineering, Polytechnique Montréal, Montreal, Canada This paper presents a design methodology for the FPGA-based simulation of the Universal Line Model (ULM).

## 核心贡献


- 提出ULM的FPGA设计方法，优化计算调度与历史项管理以降低延迟
- 采用深度流水线与浮点运算架构，实现250MHz主频与200ns仿真步长
- 基于状态空间法求解极留数拟合模型，提升硬件资源利用率与计算性能


## 使用的方法


- [[状态空间法|状态空间法]]
- [[极留数有理拟合|极留数有理拟合]]
- [[改进增广节点分析法-mana|改进增广节点分析法(MANA)]]
- [[深度流水线调度|深度流水线调度]]
- [[浮点运算架构|浮点运算架构]]
- [[线性插值时延处理|线性插值时延处理]]


## 涉及的模型


- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[输电线路|输电线路]]
- [[电缆|电缆]]
- [[诺顿等效电路|诺顿等效电路]]


## 相关主题


- [[fpga实时仿真|FPGA实时仿真]]
- [[硬件在环测试|硬件在环测试]]
- [[频率相关线路建模|频率相关线路建模]]
- [[行波故障定位|行波故障定位]]
- [[高性能计算架构|高性能计算架构]]


## 主要发现


- 仿真步长降至200ns且主频达250MHz，突破现有FPGA微秒级限制
- 与EMTP对比验证模型精度，满足行波故障定位硬件在环测试需求
- 优化调度策略有效降低延迟，浮点运算下实现高吞吐与低延迟平衡



## 方法细节

### 方法概述

本文提出一种面向FPGA的通用线路模型(ULM)高性能计算引擎设计方法。核心采用状态空间法对特征导纳($Y_c$)和传播函数($H$)的极留数有理拟合形式进行时域递推求解。为突破传统FPGA实现的微秒级步长限制，提出计算重调度策略(Method 2)，将历史项卷积核的数据通路从输入缓冲移至输出缓冲，大幅削减关键路径延迟。结合深度流水线架构与定制非标准浮点运算单元，在250MHz主频下实现极低延迟响应。网络侧采用改进增广节点分析法(MANA)并预计算开关组合逆矩阵，与ULM求解器串行执行。针对非整数倍步长的传播时延，采用环形缓冲区存储历史反射电流并结合线性插值技术，确保时域波形重构精度。

### 数学公式


**公式1**: $$$Y_c \simeq G_0 + \sum_{j=1}^{N_{Y_c}} \frac{R_j}{s - p_j}$$$

*特征导纳$Y_c$的频域极留数有理拟合表达式，用于提取状态空间模型参数*


**公式2**: $$$H \simeq \sum_{i=1}^{N_g} \left( \sum_{j=1}^{N_{H_i}} \frac{R_{i,j}}{s - p_{i,j}} \right) e^{-s\tau_i}$$$

*传播函数$H$的频域极留数拟合形式，包含模态组数、极点、留数及最小相位时延*


**公式3**: $$$x_{Y_j c}(t + \Delta t) = \alpha_{j Y_c} x_{Y_j c}(t) + \beta_{j Y_c} v_k(t)$$$

*特征导纳卷积核的状态向量递推更新方程*


**公式4**: $$$x_{i_{H,j}}(t + \Delta t) = \alpha_{i_{H,j}} x_{i_{H,j}}(t) + \beta_{i_{H,j}} \{ i_{rm}(t - \tau_i) + i_{rm}(t - \tau_i + \Delta t) \}$$$

*传播函数卷积核的状态向量递推更新方程，包含时延反射电流的线性插值项*


**公式5**: $$$i_{\text{hist}, k}(t + \Delta t) = 2i_{ik}(t + \Delta t) - i_{\text{hist}, \text{sh}k}(t + \Delta t)$$$

*终端$k$的总历史电流诺顿等效源计算式，用于下一时刻网络方程求解*


**公式6**: $$$\Delta t_{\min} = \frac{1}{f_{\max}} \{ \ell_{NS} + \ell_{ULM} \}$$$

*最小仿真步长计算公式，由FPGA最高主频与节点求解器、ULM求解器总延迟决定*


### 算法步骤

1. 步骤1：求解当前仿真时刻的网络方程，获取线路各终端的节点电压与反射电流，即$v_k(t)$、$v_m(t)$、$i_{rk}(t)$和$i_{rm}(t)$。

2. 步骤2：利用步骤1得到的反射电流结果，更新用于存储历史反射电流的环形缓冲区，为后续时延插值提供数据。

3. 步骤3：针对线路的每个终端，利用公式(8)和(9)分别更新特征导纳状态向量$x_{Y_j c}(t + \Delta t)$与传播函数状态向量$x_{i_{H,j}}(t + \Delta t)$。

4. 步骤4：根据公式(10)和(11)，对更新后的状态向量进行求和，分别计算各终端的并联历史电流向量$i_{\text{hist}, \text{sh}}(t + \Delta t)$与入射电流向量$i_i(t + \Delta t)$。

5. 步骤5：利用公式(12)组合入射电流与并联历史电流，计算下一时刻各终端的总历史电流向量$i_{\text{hist}, k}(t + \Delta t)$和$i_{\text{hist}, m}(t + \Delta t)$。

6. 步骤6：将仿真时间推进一个步长$t = t + \Delta t$，返回步骤1进入下一轮迭代循环。


### 关键参数

- **f_max**: 250 MHz (FPGA最高运行主频)

- **Δt_min**: 200 ns (实现的最小仿真步长)

- **N_Yc**: 特征导纳拟合阶数

- **N_g**: 传播函数模态分组数量

- **N_Hi**: 第i个模态组的拟合阶数

- **τ_i**: 第i个模态组的最小相位传播时延

- **ℓ_NS**: 节点求解器(MANA)流水线延迟

- **ℓ_ULM**: ULM求解器最大延迟，取max(ℓ_Yc, ℓ_H)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 行波故障定位器(TWFL)硬件在环(HIL)测试场景 | FPGA实现的ULM模型成功将仿真步长压缩至200ns，主频稳定运行于250MHz。模型输出波形与EMTP离线参考结果高度吻合，满足TWFL所需的1MHz采样率与±300m故障定位精度要求。 | 较文献[7]中175MHz主频/1.42µs步长的FPGA实现，仿真步长缩短约7.1倍，计算吞吐量显著提升，且通过重调度策略将传播函数模块延迟降至单时钟周期。 |



## 量化发现

- FPGA主频达到250MHz，最小仿真步长降至200ns，突破现有FPGA微秒级限制
- 计算重调度策略使传播函数卷积核延迟ℓ_H降至单时钟周期(ℓ_H^ob)，大幅降低整体流水线深度
- 满足现代TWFL硬件在环测试所需的1MHz采样率(对应1µs步长)，并留有5倍裕度
- 采用定制非标准浮点运算格式，在资源占用与计算精度之间取得最优平衡
- 最小步长公式Δt_min = (ℓ_NS + ℓ_ULM)/f_max 验证了深度流水线与低延迟调度对实时性的决定性作用


## 关键公式

### 最小仿真步长约束方程

$$$\Delta t_{\min} = \frac{1}{f_{\max}} \{ \ell_{NS} + \ell_{ULM} \}$$$

*用于评估FPGA架构性能极限，指导流水线深度优化与主频提升策略*

### ULM诺顿等效历史电流合成方程

$$$i_{\text{hist}, k}(t + \Delta t) = 2i_{ik}(t + \Delta t) - i_{\text{hist}, \text{sh}k}(t + \Delta t)$$$

*在时域仿真中用于生成下一时刻注入网络求解器的等效电流源*

### 传播函数状态空间递推方程

$$$x_{i_{H,j}}(t + \Delta t) = \alpha_{i_{H,j}} x_{i_{H,j}}(t) + \beta_{i_{H,j}} \{ i_{rm}(t - \tau_i) + i_{rm}(t - \tau_i + \Delta t) \}$$$

*处理频率相关传播特性与非整数倍时延插值的核心计算单元*



## 验证详情

- **验证方式**: 与EMTP离线电磁暂态仿真结果进行波形对比验证，并结合硬件在环(HIL)测试需求进行性能评估
- **测试系统**: 含频率相关参数的输电线路与电缆网络模型（面向行波故障定位器TWFL测试）
- **仿真工具**: FPGA硬件实现平台、EMTP参考仿真软件、MANA网络求解器
- **验证结果**: FPGA实现的ULM模型在200ns步长下保持与EMTP一致的数值精度，历史项管理与重调度策略有效消除累积误差，完全满足亚微秒级实时仿真与TWFL硬件在环测试的严苛要求。
