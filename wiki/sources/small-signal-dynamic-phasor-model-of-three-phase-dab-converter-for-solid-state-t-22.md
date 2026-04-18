---
title: "Small Signal Dynamic Phasor Model of Three-Phase DAB Converter for Solid State Transformer"
type: source
authors: ['Maxime89']
year: 2018
journal: ""
tags: ['dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/22/TPWRD.2018.2817878.pdf.pdf"]
---

# Small Signal Dynamic Phasor Model of Three-Phase DAB Converter for Solid State Transformer

**作者**: Maxime89
**年份**: 2018
**来源**: `22/TPWRD.2018.2817878.pdf.pdf`

## 摘要

— The three-phase dual active bridge (3p-DAB) converter is widely addressed in emerging power systems applications such as solid-state transformer (SST), and dc microgrids. Its successful integration requires accurate modeling of its small-signal characteristics. Due to its dc-ac-dc structure, the DAB converter brings many challenges in small-signal modeling. The state-space averaging (SSA) has been the first proposed methodology to approximate the control-to-output, and line-to-output transfer functions of the 3p-DAB. However, as shown in this paper, SSA is not precise for the stability analysis of 3p-DAB converters. A generalized state-space averaging (GSSA) model based on the dynamic phasor concept is developed in this paper for the Y-∆ 3p-DAB. A hybrid SSA and GSSA model representation

## 核心贡献

- 建立了更精确的transformer电磁暂态模型，考虑了频率相关特性和非线性效应
- 应用动态相量法进行宽频暂态分析，兼顾计算效率和精度

## 使用的方法

- [[状态空间平均法-ssa|状态空间平均法(SSA)]]
- [[广义状态空间平均法-gssa|广义状态空间平均法(GSSA)]]
- [[动态相量法|动态相量法]]
- [[混合平均建模|混合平均建模]]
- [[时域开关级仿真|时域开关级仿真]]

## 涉及的模型

- [[transformer-model]]

## 相关主题

- [[dynamic-phasor]]

## 主要发现

— The three-phase dual active bridge (3p-DAB) converter is widely addressed in emerging power systems applications such as solid-state transformer (SST), and dc microgrids

## 方法细节

### 方法概述

本文提出了一种基于动态相量（dynamic phasor）概念的广义状态空间平均（GSSA）建模方法，专门用于Y-Δ连接的三相双有源桥（3p-DAB）变换器。针对传统状态空间平均（SSA）方法在处理3p-DAB稳定性分析时的不精确性问题，本文开发了混合SSA-GSSA模型表示方法。该方法通过GSSA处理变换器的高频交流链路动态特性，同时结合SSA处理直流侧变量，从而能够精确评估控制到输出、输入到输出以及输入/输出阻抗等全部传递函数。模型特别考虑了Y-Δ变压器连接方式（变比M=m√3），适用于0°≤d≤90°的正向功率传输模式。

### 数学公式


**公式1**: $$$G_{vd}(s) = \frac{\hat{v}_o(s)}{\hat{d}(s)}\bigg|_{\hat{v}_i(s)=0}$$$

*控制到输出传递函数，描述相移控制量d对输出电压vo的小信号影响，在输入电压扰动为零的条件下定义*


**公式2**: $$$G_{vg}(s) = \frac{\hat{v}_o(s)}{\hat{v}_i(s)}\bigg|_{\hat{d}(s)=0}$$$

*输入到输出传递函数（音频抑制率），描述输入电压vi对输出电压vo的小信号影响，在相移控制扰动为零的条件下定义*


**公式3**: $$$Z_{in}(s) = Z_D(s) = \frac{\hat{v}_i(s)}{\hat{i}_i(s)}\bigg|_{\hat{d}(s)=0}$$$

*驱动点输入阻抗，描述输入电流ii对输入电压vi的小信号响应，用于Middlebrook额外元件定理的稳定性分析*


**公式4**: $$$Z_N(s) = \frac{\hat{v}_i(s)}{\hat{i}_i(s)}\bigg|_{\hat{v}_o(s)=0}$$$

*零驱动点输入阻抗，描述输出电压短路（vo=0）条件下的输入阻抗，用于稳定性分析中的Null驱动点计算*


**公式5**: $$$Z_o(s) = -\frac{\hat{v}_o(s)}{\hat{i}_{load}(s)}\bigg|_{\hat{v}_i(s)=0, \hat{d}(s)=0}$$$

*输出阻抗，描述负载电流扰动iload对输出电压vo的影响，输入电压和相移控制均处于稳态*


### 算法步骤

1. 建立Y-Δ连接的3p-DAB变换器详细开关级模型，定义相移控制变量d（0°≤d≤90°），确定变压器变比M=m√3的Y-Δ连接关系

2. 应用广义状态空间平均（GSSA）方法，将时域交流变量展开为傅里叶级数形式，提取基频分量（动态相量）作为状态变量，建立包含高频交流链路动态的扩展状态空间模型

3. 在稳态工作点（vi, vo, d, io）附近进行小信号线性化，得到小信号状态空间方程，区分直流侧电容电压和交流侧电感电流的动态相量

4. 针对输入阻抗ZD(s)和ZN(s)的推导难点，采用混合建模策略：对直流侧和交流链路分别应用SSA和GSSA，建立统一的小信号等效电路模型

5. 通过代数变换和矩阵求逆，解析计算开环传递函数Gvd(s)、Gvg(s)、驱动点阻抗ZD(s)、零驱动点阻抗ZN(s)和输出阻抗Zo(s)的频域表达式

6. 在EMT-type仿真平台（如PSCAD/EMTDC）中实现详细开关级模型，与所提GSSA模型进行频域响应对比验证


### 关键参数

- **d**: 相移控制角，范围0°≤d≤90°（正向运行）或-90°≤d≤0°（反向运行），用于调节功率传输

- **M**: 变压器变比，对于Y-Δ连接M=m√3，其中m为匝数比

- **fs**: 开关频率，SSA方法假设控制穿越频率fφm≪fs

- **vi, vo**: 输入和输出直流电压，定义变换器稳态工作点

- **ii, io**: 输入和输出电流，用于阻抗计算

- **LA, LB, LC**: 三相变压器漏感或串联电感

- **Ci, Co**: 输入和输出直流滤波电容



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 开环控制到输出传递函数Gvd(s)频域验证 | 在EMT-type程序中进行详细开关级仿真，通过注入小信号扰动扫描0.1Hz到10kHz频段，GSSA模型与开关级仿真结果在全频段吻合，而传统SSA在接近开关频率fs的频段出现显著偏差 | GSSA模型在宽频范围内保持精度，SSA方法在高于fφm（控制穿越频率）的频段失去准确性，特别是在考虑Y-Δ变压器三相耦合效应时SSA误差显著增大 |

| 输入阻抗ZD(s)和ZN(s)验证 | 通过Middlebrook额外元件定理应用验证，GSSA模型正确预测了在特定频率下的阻抗交点特性，文本指出SSA无法精确评估这些阻抗参数用于稳定性分析 | GSSA模型首次实现了3p-DAB的ZD(s)和ZN(s)解析计算，而现有SSA文献中缺乏这些传递函数的准确表达式 |

| 闭环稳定性预测加速仿真 | 利用所提模型在EMT-type程序中实现加速稳定性预测，通过小信号模型直接计算闭环传递函数T(s)和闭环阻抗，避免长时间时域扫描仿真 | 相比纯时域开关级仿真，基于GSSA的稳定性预测显著减少了计算时间，适用于多变换器交互的直流微电网稳定性评估 |



## 量化发现

- 相移控制范围：正向运行0°≤d≤90°，反向运行-90°≤d≤0°，功率传输与相移角d呈正弦关系
- SSA方法精度限制：仅适用于控制穿越频率fφm远小于开关频率fs（fφm≪fs）的情况，在3p-DAB稳定性分析中不满足精度要求
- Y-Δ变压器变比关系：M=m√3，其中m为原副边匝数比，该连接方式相比Y-Y连接可降低开关应力并提高变压器利用率
- GSSA模型基于动态相量概念，通过保留基频交流分量的时变包络，消除了SSA的'交流变量变化远小于直流变量'的假设限制
- 模型验证频率范围：覆盖直流至接近开关频率fs的宽频段，GSSA在整个频段内保持与详细开关模型的一致性


## 关键公式

### 输入阻抗对（Driving Point和Null Driving Point）

$$$Z_D(s) = \frac{\hat{v}_i(s)}{\hat{i}_i(s)}\bigg|_{\hat{d}(s)=0}, \quad Z_N(s) = \frac{\hat{v}_i(s)}{\hat{i}_i(s)}\bigg|_{\hat{v}_o(s)=0}$$$

*用于Middlebrook额外元件定理的稳定性分析，是评估直流微电网中多变换器级联稳定性的关键参数，本文首次通过GSSA方法解析推导了3p-DAB的这些阻抗*

### 控制到输出传递函数

$$$G_{vd}(s) = \frac{\hat{v}_o(s)}{\hat{d}(s)}\bigg|_{\hat{v}_i(s)=0}$$$

*设计电压控制器Gc(s)和调制器Gm(s)的关键传递函数，用于闭环调节器设计和相位裕度分析*



## 验证详情

- **验证方式**: 详细时域开关级仿真对比验证（Electromagnetic Transients-type程序）
- **测试系统**: Y-Δ连接的三相双有源桥（3p-DAB）变换器，包含输入桥（S1-S6）、三相变压器（Y-Δ连接，变比M:m√3）、输出桥（S1'-S6'）、输入滤波电容Ci和输出滤波电容Co
- **仿真工具**: EMT-type程序（如PSCAD/EMTDC或类似电磁暂态仿真软件），支持详细IGBT/MOSFET开关模型和6步调制器（6-step modulator）实现
- **验证结果**: GSSA模型在宽频范围内与详细开关级仿真结果一致，成功预测了3p-DAB的小信号特性；SSA模型在稳定性分析中显示出不精确性，特别是在高频段和阻抗分析中。所提混合模型被用于加速EMT程序中的稳定性预测，避免了耗时的时域扫描过程
