---
title: "Combined transient and dynamic analysis of HVDC and FACTS systems"
type: source
authors: ['M. Sultan', 'J. Reeve', 'R. Adapa']
year: 2004
journal: "IEEE Transactions on Power Delivery;1998;13;4;10.1109/61.714495"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/Sultan 等 - 1998 - Combined transient and dynamic analysis of HVDC and facts systems.pdf"]
---

# Combined transient and dynamic analysis of HVDC and FACTS systems

**作者**: M. Sultan, J. Reeve, R. Adapa
**年份**: 2004
**来源**: `10/Sultan 等 - 1998 - Combined transient and dynamic analysis of HVDC and facts systems.pdf`

## 摘要

A new approach to HVDC and FACTS transient/dynamic simula- tion based on an interactive execution of an ac transient stability program (TSP) and the Electro-Magnetic Transients Program (EMTP) is described. Through the integration of the detailed tran- sient model of FACTS with the transient stability program, authentic simulation is achieved without simplifications. Both HVDC and Thyristor Controlled Series Capacitor (TCSC) systems are used to validate the approach, under different coupling situa- tions between both TSP arid EMTP. Keywords: FACTS, HVDC, EMTP, Frequency Dependent Net- work Equivalents, Transient Stability Simulation. I. INTRODUCTION The ac transient stability programs based on fundamental fre- quency, single-phase, phasor modeling techniques cannot directly represent the fa

## 核心贡献


- 提出EMTP与暂态稳定程序交互执行的混合仿真架构，实现全频段精确模拟
- 构建时变戴维南/诺顿频变等值模型，实现外部交流网络高精度映射
- 采用最小二乘拟合提取三相基波正序相量，实现双程序间高精度数据交互


## 使用的方法


- [[混合仿真|混合仿真]]
- [[频变网络等值|频变网络等值]]
- [[戴维南-诺顿等值|戴维南/诺顿等值]]
- [[最小二乘曲线拟合|最小二乘曲线拟合]]
- [[基波相量提取|基波相量提取]]
- [[时间步协调|时间步协调]]


## 涉及的模型


- [[vsc-hvdc|VSC-HVDC]]
- [[facts|FACTS]]
- [[tcsc|TCSC]]
- [[外部交流电网|外部交流电网]]
- [[频变等值模型|频变等值模型]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[暂态稳定仿真|暂态稳定仿真]]
- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]
- [[交直流相互作用|交直流相互作用]]


## 主要发现


- 频变等值模型有效抑制接口波形畸变，实现外部电网宽频响应的精确映射
- 交互策略成功协调双程序时间步，HVDC与TCSC算例验证了方法有效性
- 相量提取算法保障多接口数据交互精度，消除传统准稳态模型的简化误差



## 方法细节

### 方法概述

提出一种基于暂态稳定程序(TSP)与电磁暂态程序(EMTP)交互执行的混合仿真架构。核心思想是将外部交流电网通过时变诺顿频变等值模型(NFDE)映射至EMTP详细模型中，同时将EMTP接口母线的三相瞬时波形通过最小二乘曲线拟合提取基波正序相量，反馈至TSP更新负荷或电流源模型。该架构支持两种交互策略：(A)短期暂态交互，双程序按固定时间步长同步推进，适用于首摆暂态分析；(B)长期动态切换，EMTP运行至暂态平息后挂起，TSP接管并切换至准稳态模型继续仿真，兼顾全频段精度与计算效率。

### 数学公式


**公式1**: $$$v(t_k) \approx a_1 \cos(\omega t_k) + b_1 \sin(\omega t_k)$$$

*最小二乘曲线拟合模型，用于从EMTP输出的离散三相瞬时波形采样点中提取基波分量系数*


**公式2**: $$$V_1 = \sqrt{a_1^2 + b_1^2}, \quad \phi_1 = \arctan(b_1/a_1)$$$

*基波幅值与相位计算公式，结合对称分量法转换为TSP所需的正序电压/电流相量*


**公式3**: $$$\mathbf{I}_{eq}(s) = \mathbf{Y}_{eq}(s)\mathbf{V}_{bus}(s) + \mathbf{I}_{source}(s)$$$

*诺顿频变等值传递方程，其中$\mathbf{Y}_{eq}(s)$由N个串并联RLC支路构成，用于在宽频范围内精确拟合外部电网阻抗特性*


### 算法步骤

1. 初始化阶段：设定仿真起始时间$t=0$，TSP与EMTP均从系统稳态初始条件启动，确定接口母线位置。

2. 外部等值生成：TSP计算接口母线处的诺顿频变等值(NFDE)参数，并在当前TSP步长边界$T_i$将等值电路参数传递给EMTP。

3. EMTP详细求解：EMTP利用接收到的NFDE，以微秒级步长(如50μs)推进仿真至下一TSP步长边界$T_{i+1}$，完整记录接口母线三相瞬时电压与电流波形。

4. 相量提取与转换：对$T_i$至$T_{i+1}$区间的EMTP波形数据应用最小二乘曲线拟合，提取三相基波幅值与相位，经对称分量法计算正序电压/电流相量。

5. TSP更新与求解：将提取的正序相量转换为TSP中的解耦负荷或电流源模型，TSP以毫秒级步长(如8ms/10ms)推进至$T_{i+1}$，更新全网机电暂态状态。

6. 循环或模式切换：重复步骤2-5直至仿真结束(策略A)；或在暂态平息后(如0.6s)挂起EMTP，将详细模型替换为准稳态模型，由TSP独立继续长期动态仿真(策略B)。


### 关键参数

- **EMTP时间步长**: 50 μs

- **TSP时间步长**: 8 ms (12节点系统) / 10 ms (IEEE 118节点系统)

- **TCSC容抗设定**: -j22.5 Ω

- **线路基准电抗**: 150 Ω

- **TCSC补偿度**: 15%

- **晶闸管导通角**: 43°

- **故障清除时间**: 3个周波 (约60ms)

- **策略B切换时间阈值**: 0.6 s

- **长期动态仿真时长**: 4 s



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| HVDC背靠背系统(8节点交流侧) | 在逆变器交流母线施加3周期三相故障。混合仿真准确再现了换相失败、直流电流跌落及电压恢复全过程，接口母线电压波形与全EMTP基准高度一致。 | 暂态波形与全EMTP基准完全吻合，验证了频变等值模型在弱交流系统下的接口保真度，无传统准稳态模型的简化误差。 |

| TCSC系统(12节点交流网络) | 线路1-2母线1处施加三相故障。混合策略A准确捕捉了避雷器动作、电容重投及TCSC快速阀控消除线路电流直流偏置的非线性暂态，直流偏置在故障清除后2个周波内消除。 | 策略A在12节点系统中CPU耗时为151.7秒，时间步长协调比达160:1，在保持微秒级暂态精度的同时实现了毫秒级机电暂态的高效耦合。 |

| TCSC系统(IEEE 118节点大电网) | 采用策略B，EMTP运行至0.6s后挂起，TSP切换至准稳态模型继续仿真至4s。完整记录了故障后发电机功角摇摆及系统长期动态恢复过程。 | 相比纯EMTP全频段微步长仿真，策略B避免了长时程计算的算力瓶颈，计算效率显著提升，且首摆暂态波形与策略A及全EMTP基准完全一致。 |



## 量化发现

- 混合仿真时间步长协调比达到160:1 (TSP 8ms / EMTP 50μs)，有效平衡了机电暂态与电磁暂态的计算尺度差异。
- 策略A在12节点测试系统中的CPU计算时间为151.7秒，验证了交互架构在中等规模系统中的可行性。
- TCSC快速阀控策略在故障清除后2个周波(约40ms)内成功消除线路电流直流偏置，混合模型精确复现了该非线性控制响应。
- 策略B支持仿真时长从首摆暂态(0.6s)无缝扩展至长期动态(4s)，避免了全EMTP微步长积分带来的指数级算力增长。
- 频变等值模型(NFDE)在宽频范围内精确拟合外部系统阻抗幅频特性，接口波形畸变与不对称问题得到有效抑制，关键电气量暂态偏差可忽略。


## 关键公式

### 基波正序相量提取公式

$$$V_1 = \sqrt{a_1^2 + b_1^2}, \quad \phi_1 = \arctan(b_1/a_1)$$$

*用于EMTP向TSP传递数据时，将三相瞬时波形转换为基波正序相量，消除高频谐波与不对称分量对机电暂态程序的干扰。*

### 诺顿频变等值传递方程

$$$\mathbf{I}_{eq}(s) = \mathbf{Y}_{eq}(s)\mathbf{V}_{bus}(s) + \mathbf{I}_{source}(s)$$$

*用于TSP向EMTP传递外部电网动态特性，通过频域导纳矩阵$\mathbf{Y}_{eq}(s)$实现外部网络宽频响应的精确映射。*



## 验证详情

- **验证方式**: 纯EMTP全详细仿真作为基准(Benchmark)，与TSP/EMTP混合仿真结果进行波形对比、暂态特征提取与计算耗时分析。
- **测试系统**: 2端背靠背HVDC系统(含8节点交流侧)；12节点交流系统(含TCSC)；IEEE 118节点系统(含TCSC)。
- **仿真工具**: EMTP (电磁暂态详细建模，50μs步长)，TSP (暂态稳定程序，基波相量域，8ms/10ms步长)。
- **验证结果**: 验证了混合架构在HVDC换相失败、TCSC避雷器动作/快速阀控/非线性补偿恢复等复杂暂态过程中的高保真度。策略A适用于首摆暂态，策略B实现暂态到长期动态的高效切换，大幅降低大系统仿真计算负担，同时保持接口数据交互精度，成功克服了传统TSP无法表征半导体开关离散动作与波形畸变的局限。
