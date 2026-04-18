---
title: "Analytical model building for Type-3 wind farm subsynchronous oscillation analysis"
type: source
authors: ['Lingling Fan']
year: 2021
journal: "Electric Power Systems Research, 201 (2021) 107566. doi:10.1016/j.epsr.2021.107566"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/09/Fan和Miao - 2021 - Analytical model building for Type-3 wind farm subsynchronous oscillation analysis.pdf"]
---

# Analytical model building for Type-3 wind farm subsynchronous oscillation analysis

**作者**: Lingling Fan
**年份**: 2021
**来源**: `09/Fan和Miao - 2021 - Analytical model building for Type-3 wind farm subsynchronous oscillation analysis.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Analytical model building for Type-3 wind farm subsynchronous Dept. of Electrical Engineering, University of South Florida, Tampa FL 33620 Many real-world scenarios confirmed insights developed based on the dq-frame nonlinear analytical model for doubly-fed induction generator (DFIG)-based type-3 wind subsynchronous resonance (SSR) study by the authors

## 核心贡献


- 提出包含锁相环动态的DFIG风电场dq坐标系非线性解析模型
- 构建模块化建模框架明确子系统接口与互联支持多种电网拓扑
- 模型兼具大信号时域仿真与小信号分析能力可复现低补偿度SSR


## 使用的方法


- [[dq坐标系解析建模|dq坐标系解析建模]]
- [[模块化建模|模块化建模]]
- [[状态空间法|状态空间法]]
- [[数值摄动线性化|数值摄动线性化]]
- [[小信号特征值分析|小信号特征值分析]]
- [[大信号时域仿真|大信号时域仿真]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[锁相环-pll|锁相环(PLL)]]
- [[转子侧变流器-rsc|转子侧变流器(RSC)]]
- [[网侧变流器-gsc|网侧变流器(GSC)]]
- [[串联补偿输电线路|串联补偿输电线路]]
- [[双质量轴系模型|双质量轴系模型]]


## 相关主题


- [[次同步谐振-ssr|次同步谐振(SSR)]]
- [[风电场建模|风电场建模]]
- [[动态建模|动态建模]]
- [[弱电网稳定性|弱电网稳定性]]
- [[变流器控制|变流器控制]]
- [[小信号稳定性分析|小信号稳定性分析]]


## 主要发现


- 引入PLL动态后成功复现低串补度下风电场次同步振荡现象
- PLL动态显著改变系统稳定裕度与振荡频率是SSR关键诱因
- 模块化模型可准确评估不同并网风机数量对系统SSR脆弱性影响



## 方法细节

### 方法概述

本文提出一种基于统一dq坐标系的模块化非线性解析建模方法。模型将风电场系统解耦为8个核心子系统（直流母线、网侧变流器控制、转子侧变流器控制、输电网络、GSC滤波器、DFIG电机、并联电容及锁相环）及4个坐标变换模块。通过引入电网同步dq坐标系与PLL跟踪dq坐标系的双参考系架构，精确刻画PLL动态对变流器控制指令的耦合影响。模型共包含26个状态变量与4个控制指令，采用数值摄动法进行线性化，支持大信号时域仿真与小信号特征值分析，可灵活适配辐射状、并联等多种电网拓扑，显著缩短模型开发周期并提升低串补度SSR复现精度。

### 数学公式


**公式1**: $$$L_1 \frac{dI_1}{dt} = V_{PCC} - V_c - R_1 I_1 - j\omega L_1 I_1 - V_\infty$$$

*串补RLC线路在电网dq坐标系下的电流动态方程，用于描述线路电感、电阻、串补电容与无穷大母线电压的相互作用。*


**公式2**: $$$R_g I_g + L_g \frac{dI_g}{dt} + jX_g I_g = V_g - V_{PCC} e^{-j\Delta\theta}$$$

*网侧变流器(GSC)滤波器动态方程，包含PLL坐标系与电网坐标系的角度差$\Delta\theta$，体现PLL动态对GSC输出电压的调制影响。*


**公式3**: $$$\tau \frac{dV_{DC}}{dt} = -P_r - P_g$$$

*直流母线电压动态方程，$\tau=0.0033$ s为直流时间常数，描述转子侧与网侧有功功率不平衡对直流电压的充放电作用。*


**公式4**: $$$C \frac{dV_{PCC}}{dt} + j\omega C V_{PCC} = I_w e^{j\Delta\theta} - I_n$$$

*PCC点并联电容动态方程，关联风电场注入电流$I_w$与电网吸收电流$I_n$，用于维持公共连接点电压稳定。*


### 算法步骤

1. 1. 子系统划分与接口定义：将系统解耦为8个物理/控制模块，明确各模块输入输出变量（如电压相量、电流相量、有功/无功功率、PLL角度差$\Delta\theta$）。

2. 2. 双dq坐标系构建：建立电网同步旋转坐标系($dq_g$)与PLL跟踪坐标系($dq_{PLL}$)，推导复数域坐标变换算子$e^{\pm j\Delta\theta}$，实现跨参考系变量映射。

3. 3. 状态空间方程推导：基于基尔霍夫定律、电机磁链方程及PI控制逻辑，列写各模块微分方程，整合为全局非线性状态空间模型$\dot{x}=f(x,u)$，共26个状态变量。

4. 4. 稳态工作点初始化：给定PCC电压、风速、转速及并网功率，通过潮流计算与迭代求解（GSC设为PV节点，PCC设为松弛节点），确定26个状态变量初值及PI控制器积分器初值，确保模型平启动。

5. 5. 线性化与仿真分析：调用MATLAB `linmod`函数在稳态点进行数值摄动线性化，获取雅可比矩阵进行特征值分析；或直接采用ODE求解器积分微分方程进行大扰动时域仿真。


### 关键参数

- **PLL_PI增益**: (60, 1400)

- **GSC电流控制PI**: (0.6, 8)

- **GSC直流电压控制PI**: (8, 400)

- **GSC交流电压控制PI**: (0.02, 20)

- **RSC电流控制PI**: (0.6, 8)

- **RSC转矩控制PI**: (0.02, 20)

- **RSC无功控制PI**: (0.83, 5)

- **直流母线时间常数_τ**: 0.0033 s

- **系统基准容量**: 200 MW (100台×2 MW DFIG)

- **GSC滤波电抗**: 0.3 pu



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 弱电网运行(拓扑1) | 线路电抗从0.8 pu突增至0.89 pu(t=1s)，3 Hz主导模态进入右半平面，引发持续振荡；PCC电压幅值与相角出现明显低频波动。 | 忽略PLL动态时系统保持稳定，引入PLL后3 Hz模态阻尼比显著下降，证明传统模型会高估弱电网稳定性。 |

| 串补度阶跃变化(拓扑2) | 串补度从5%降至1%时激发3 Hz弱电网振荡模态；升至10%时44 Hz次同步振荡(SSR)模态主导；串补度5%且线路电抗≤0.5 pu时系统失稳。 | 传统模型仅在串补度≥75%时预测SSR，新模型在串补度<10%时即可准确复现6-8 Hz低频SSR，与现场实测数据一致。 |

| 并联线路跳闸(拓扑3→2) | t=0.8s切除并联RL线路，串补度25%或50%时系统失稳；串补度5%时系统稳定但出现50 Hz弱阻尼振荡。 | 特征值轨迹与时域响应高度吻合，验证了模型在拓扑突变工况下的动态跟踪能力。 |

| 在线风机数量影响 | 在线风机从1台增至100台，10 Hz与3 Hz弱电网模态向右半平面移动；SSR模态(<60 Hz)右移，超同步模态(>60 Hz)左移。 | 量化揭示了风机集群规模对SSR脆弱性的非线性影响，为风电场扩容规划提供直接依据。 |



## 量化发现

- 模型共包含26个状态变量与4个控制指令，实现全系统解析表达，线性化计算耗时<0.5秒。
- 低串补度(<10%)下，SSR振荡频率实测为6-8 Hz，模型成功复现该频段特征，误差<0.5 Hz。
- 忽略PLL动态将导致稳定性预测偏乐观，引入PLL后3 Hz模态阻尼比下降约40%。
- 直流母线时间常数τ=0.0033 s，基于1150 V额定电压与0.01 F电容计算，对高频振荡抑制起关键作用。
- 风机转速从0.75 pu升至1.25 pu时，低串补(10%)下SSR模态左移(稳定性改善)，高串补(75%)下右移(稳定性恶化)，等效转子电阻变化幅度达30%。


## 关键公式

### GSC滤波器跨坐标系动态方程

$$$R_g I_g + L_g \frac{dI_g}{dt} + jX_g I_g = V_g - V_{PCC} e^{-j\Delta\theta}$$$

*用于精确耦合PLL动态与网侧变流器控制，是复现低串补度SSR的核心方程。*

### 直流母线功率平衡方程

$$$\tau \frac{dV_{DC}}{dt} = -P_r - P_g$$$

*在变流器有功功率快速波动时，描述直流电压动态响应，影响系统低频阻尼特性。*

### PCC并联电容动态方程

$$$C \frac{dV_{PCC}}{dt} + j\omega C V_{PCC} = I_w e^{j\Delta\theta} - I_n$$$

*用于多拓扑电网互联分析，决定公共连接点电压支撑能力与模态耦合强度。*



## 验证详情

- **验证方式**: 小信号特征值分析结合大信号时域仿真，对比含/不含PLL动态的模型差异，并与历史现场事件数据(中国华北、美国德州等)频率特征交叉验证。
- **测试系统**: 200 MW Type-3 DFIG风电场(100×2 MW)，连接含串补RLC线路、纯RL线路或并联拓扑的辐射状电网，参数基于MATLAB/SimScape标准测试平台。
- **仿真工具**: MATLAB/Simulink (自定义解析模型)，`linmod`函数用于数值摄动线性化，ODE求解器用于时域积分。
- **验证结果**: 新模型成功复现低串补度(<10%)下的次同步振荡现象，验证了PLL动态是诱发弱电网及低补偿SSR的关键因素；特征值轨迹与时域响应高度一致，为风电场并网规划与控制器参数整定提供高精度量化评估工具。
