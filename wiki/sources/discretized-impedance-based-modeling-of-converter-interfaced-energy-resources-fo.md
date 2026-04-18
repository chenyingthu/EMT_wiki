---
title: "Discretized Impedance-Based Modeling of Converter-Interfaced Energy Resources for State-Variable-Based Real-Time EMT Simulators"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Open Journal of Power Electronics;2025;6; ;10.1109/OJPEL.2024.3525019"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/Vahabzadeh 等 - 2025 - Discretized Impedance-Based Modeling of Converter-Interfaced Energy Resources for State-Variable-Bas.pdf"]
---

# Discretized Impedance-Based Modeling of Converter-Interfaced Energy Resources for State-Variable-Based Real-Time EMT Simulators

**作者**: 
**年份**: 2025
**来源**: `13&14/files/Vahabzadeh 等 - 2025 - Discretized Impedance-Based Modeling of Converter-Interfaced Energy Resources for State-Variable-Bas.pdf`

## 摘要

Modern power systems are experiencing high penetration of voltage-source converter (VSC)- interfaced distributed energy resources and loads. Design, analysis, and reliable operation of such systems require extensive ofﬂine and real-time electromagnetic transient (EMT) simulations. This paper proposes discretized impedance-based modeling (DIBM) of VSCs for efﬁcient time-domain transient analysis in state-variable (SV)-based EMT simulators. Speciﬁcally, the VSC-based systems are ﬁrst represented as admittance-based models in Laplace domain, and then they are discretized and formulated to construct a Thévenin equivalent impedance matrix and history voltages that can be interfaced seamlessly with external systems in SV-based simulators. By replacing VSC subsystems with Thévenin equivalent circ

## 核心贡献


- 提出离散阻抗建模方法，将VSC导纳模型转化为离散戴维南等效电路以适配状态变量仿真器
- 消除接口步长延迟与虚拟缓冲电路，大幅降低系统状态变量数量并提升数值稳定性
- 实现VSC子系统与外部网络无缝接口，支持更大仿真步长且保持高瞬态分析精度


## 使用的方法


- [[离散阻抗建模|离散阻抗建模]]
- [[导纳建模|导纳建模]]
- [[戴维南等效电路|戴维南等效电路]]
- [[状态变量法|状态变量法]]
- [[数值离散化|数值离散化]]
- [[平均值模型|平均值模型]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[分布式能源|分布式能源]]
- [[并网滤波器|并网滤波器]]
- [[控制系统|控制系统]]
- [[七节点测试系统|七节点测试系统]]


## 相关主题


- [[实时电磁暂态仿真|实时电磁暂态仿真]]
- [[状态变量仿真|状态变量仿真]]
- [[换流器接口建模|换流器接口建模]]
- [[计算效率优化|计算效率优化]]
- [[数值稳定性|数值稳定性]]
- [[电力系统暂态分析|电力系统暂态分析]]


## 主要发现


- 经离线与实时平台验证，该方法在保持高波形精度的同时支持更大仿真步长
- 相比传统平均值模型，单步计算效率提升最高达四倍，显著降低实时仿真计算负担
- 成功消除接口延迟与虚拟缓冲电路，有效改善系统数值刚度并提升暂态仿真稳定性



## 方法细节

### 方法概述

本文提出离散阻抗建模（DIBM）方法，专为基于状态变量（SV）的实时电磁暂态（EMT）仿真器设计。首先，在拉普拉斯域建立含滤波器与控制系统的VSC导纳基模型（ABM），将其表示为传递函数矩阵。随后，采用梯形积分法则将连续ABM离散化为z域差分方程，并通过逆z变换得到时域离散形式。将离散模型整理为诺顿导纳形式，再通过矩阵求逆转换为戴维南等效形式（恒定阻抗矩阵与历史电压源）。最终，在SV仿真器中将阻抗矩阵实现为耦合电阻支路，历史电压项实现为受控电压源。该方法实现了VSC子系统与外部网络的无延迟同步求解，彻底消除了传统接口所需的虚拟缓冲电路，大幅降低了系统状态变量数量并提升了数值稳定性。

### 数学公式


**公式1**: $$s = \frac{2}{\Delta t}\frac{z-1}{z+1}$$

*梯形积分法则离散化替换公式，用于将拉普拉斯域连续传递函数转换为z域离散模型，保证二阶精度与数值稳定性*


**公式2**: $$i_{VSC,dq}(t) = G_{dq}^{PI} v_{PCC,dq}(t) + h_{dq}^{PI}(t)$$

*离散化后的诺顿导纳形式，G为恒定导纳矩阵，h为包含历史状态与参考电流的向量*


**公式3**: $$v_{PCC,abc}(t) = Z_{abc}^{PI} i_{VSC,abc}(t) + e_{abc}^{PI}(t)$$

*转换后的戴维南等效阻抗形式，Z为恒定阻抗矩阵，e为历史电压源，用于直接接入SV求解器*


**公式4**: $$Z_{abc}^{PI} = (G_{abc}^{PI})^{-1}, \quad e_{abc}^{PI}(t) = -(G_{abc}^{PI})^{-1} h_{abc}^{PI}(t)$$

*诺顿到戴维南等效的转换关系，通过导纳矩阵求逆获得阻抗矩阵与历史电压源*


### 算法步骤

1. 步骤1：在拉普拉斯域推导VSC系统的导纳基模型（ABM）。根据所选控制策略（dq轴PI控制或αβ轴PR控制）及并网滤波器（RL或LCL），建立PCC电压、VSC输出电流与电流参考值之间的传递函数矩阵关系。

2. 步骤2：应用梯形积分法则进行离散化。将拉普拉斯算子s替换为离散映射公式，将连续传递函数矩阵转换为z域差分方程，确保数值稳定性与二阶精度。

3. 步骤3：执行逆z变换获取时域离散方程。将z域方程展开为当前时刻与历史时刻（t, t-Δt, t-2Δt等）变量的线性组合，分离出当前时刻电压/电流项与历史项。

4. 步骤4：构建诺顿导纳模型。将时域方程重组为i(t) = G v(t) + h(t)的标准形式，提取恒定导纳矩阵G和包含历史状态及控制参考量的历史向量h(t)。

5. 步骤5：坐标系变换（如适用）。若模型在dq或αβ坐标系下建立，利用Park或Clarke变换的伪逆矩阵将导纳矩阵G和历史向量h(t)转换至abc三相静止坐标系，得到G_abc和h_abc(t)。

6. 步骤6：转换为戴维南等效电路。对导纳矩阵求逆得到恒定阻抗矩阵Z_abc = G_abc^{-1}，并计算历史电压源e_abc(t) = -Z_abc h_abc(t)。

7. 步骤7：在SV仿真器中实现接口。将Z_abc建模为耦合的恒定电阻支路，将e_abc(t)建模为受控电压源，直接接入外部网络节点。该结构无需迭代求解或添加虚拟缓冲电路，实现VSC与外部网络的同步、无延迟求解。


### 关键参数

- **离散化方法**: 梯形积分法则（Trapezoidal Rule）

- **最大仿真步长**: 1 ms (1000 µs)

- **传统AVM最大稳定步长**: 约 80 µs

- **系统状态变量数(传统AVM/开关模型)**: 271

- **系统状态变量数(DIBM)**: 43

- **控制器类型**: dq轴PI控制 / αβ轴PR控制

- **求解器**: 固定步长 ode4



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 7节点VSC系统大信号暂态仿真 | 在t=0.1s时CPL有功指令增加1kW，t=0.4s时DER有功指令增加5kW。DIBM在5µs步长下与参考解完全吻合；在200µs步长下仍能保持高精度，PCC电压与线路功率波形无明显畸变或数值振荡。 | 相比传统AVM在80µs步长下易出现数值不稳定，DIBM在200µs步长下误差<0.5%，且计算耗时降低约75%。 |

| 实时仿真器（OPAL-RT）计算效率测试 | 在固定步长实时硬件在环环境中，DIBM模型成功运行于1ms步长，系统状态数从271降至43，单步计算时间显著缩短。 | 在相同仿真精度要求下，DIBM相比传统AVM实现高达4倍的单步计算速度提升，且彻底消除了接口延迟导致的数值发散问题。 |



## 量化发现

- 系统状态变量数量从271个大幅减少至43个，降幅达84.1%。
- 允许的最大仿真步长从传统AVM的约80µs提升至1ms（1000µs），步长扩大12.5倍。
- 在实时仿真器中，单步计算性能提升最高达4倍。
- 在200µs仿真步长下，DIBM输出波形与1µs步长参考解的误差保持在<0.5%以内。
- 完全消除虚拟缓冲电路（snubbers），系统数值刚度显著降低，无附加数值误差引入。


## 关键公式

### 戴维南等效接口方程

$$$v_{PCC,abc}(t) = Z_{abc} i_{VSC,abc}(t) + e_{abc}(t)$$$

*用于在SV仿真器中直接替代VSC子系统，实现与外部网络的无延迟同步求解*

### 梯形离散化映射公式

$$$s = \frac{2}{\Delta t}\frac{z-1}{z+1}$$$

*将连续拉普拉斯域导纳模型转换为离散z域模型的核心数学工具*

### 诺顿-戴维南等效转换公式

$$$Z_{abc} = (G_{abc})^{-1}, \quad e_{abc}(t) = -Z_{abc} h_{abc}(t)$$$

*将离散导纳模型转换为恒定阻抗矩阵与历史电压源，以适配SV求解器架构*



## 验证详情

- **验证方式**: 离线与实时电磁暂态仿真对比验证（大信号暂态响应、步长敏感性分析、计算效率评估）
- **测试系统**: 7节点VSC互联能源系统（含20台VSC，母线4/6为DERs，母线5/7为CPLs，母线1接电网等效源）
- **仿真工具**: MATLAB Simscape Electrical（离线仿真）, OPAL-RT（实时仿真）
- **验证结果**: 验证表明DIBM在大幅降低系统状态数（271→43）的同时，支持高达1ms的仿真步长且保持高精度（误差<0.5%）。相比传统AVM，计算效率提升最高4倍，彻底消除接口延迟与虚拟缓冲电路带来的数值不稳定问题，在离线与实时环境中均表现出优异的瞬态分析精度与计算性能。
