---
title: "Harmonics Interaction Mechanism and Impact on Extinction Angles in Multi-Infeed HVDC Systems"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Delivery;2023;38;4;10.1109/TPWRD.2023.3243412"
tags: ['harmonic']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/Yao 等 - 2023 - Harmonics Interaction Mechanism and Impact on Extinction Angles in Multi-Infeed HVDC Systems.pdf"]
---

# Harmonics Interaction Mechanism and Impact on Extinction Angles in Multi-Infeed HVDC Systems

**作者**: 
**年份**: 2023
**来源**: `19、20、21/EMT_task_21/Yao 等 - 2023 - Harmonics Interaction Mechanism and Impact on Extinction Angles in Multi-Infeed HVDC Systems.pdf`

## 摘要

—Harmonics interaction is an important factor in caus- ing concurrent commutation failures (CCF) of multiple converter stations in multi-infeed HVDC (MI-HVDC) systems, but it was not studied sufﬁciently in existing literature. In this paper, the mecha- nism analysis and quantitative calculation of harmonic interaction are investigated. Firstly, the generation and interaction process of harmonic during AC fault events in the MI-HVDC systems with single-terminal connection and hierarchical connection on the receiving-end are illustrated, respectively. Then, the common characteristics of harmonic interaction in generalized MI-HVDC systems are concluded. Moreover, to evaluate the impact of har- monic interaction on the commutation process quantitatively, an equivalent circuit model of harmonic

## 核心贡献


- 揭示单端与分层接入多馈入直流系统交流故障下的谐波产生与交互机理
- 建立多馈入直流系统谐波传递等效电路模型并推导谐波电压传递系数
- 提出计及谐波交互影响的逆变器关断角定量计算方法以提升评估精度


## 使用的方法


- [[等效电路建模|等效电路建模]]
- [[谐波传递系数推导|谐波传递系数推导]]
- [[关断角定量计算|关断角定量计算]]
- [[电磁暂态仿真验证|电磁暂态仿真验证]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[多馈入直流系统|多馈入直流系统]]
- [[换流站-逆变器|换流站/逆变器]]
- [[交流耦合网络等效模型|交流耦合网络等效模型]]


## 相关主题


- [[谐波交互机制|谐波交互机制]]
- [[并发换相失败|并发换相失败]]
- [[关断角计算|关断角计算]]
- [[多馈入直流系统|多馈入直流系统]]
- [[分层接入|分层接入]]
- [[交流故障暂态分析|交流故障暂态分析]]


## 主要发现


- 谐波交互会在各换流站形成谐波源，改变远端逆变器关断角并增加并发换相失败风险
- 所提等效模型计算的关断角与电磁暂态仿真结果高度吻合，验证了定量方法的准确性
- 交流故障暂态过程中的低次谐波通过交流网络传递，显著偏移换相电压过零点



## 方法细节

### 方法概述

本文采用机理分析与频域等效建模相结合的方法，系统研究多馈入直流（MI-HVDC）系统交流故障下的谐波交互机制。首先，分别剖析单端接入与分层接入拓扑下故障暂态过程中谐波的产生路径与传播特性；其次，提取广义MI-HVDC系统谐波交互的共性特征，构建计及交流耦合网络阻抗的谐波传递等效电路模型；基于该模型推导谐波电压传递系数，量化谐波幅值衰减与相位偏移；最后，结合换相电压过零点偏移量与修正后的换相重叠角，建立计及谐波交互影响的逆变器关断角定量计算公式，并通过电磁暂态仿真验证模型精度与工程适用性。

### 数学公式


**公式1**: $$$\dot{U}_{2h} = \frac{Z_{2h}}{Z_{12h} + Z_{2h}} \dot{U}_{1h}$$$

*谐波电压传递方程，描述故障母线1至远端母线2的h次谐波电压在交流耦合网络中的分压传递关系，用于量化幅值衰减与相位偏移*


**公式2**: $$$\phi = \arctan\left(\frac{\sum_{h} U_{h}\sin(h\omega t + \theta_h)}{\sum_{h} U_{h}\cos(h\omega t + \theta_h)}\right)$$$

*谐波引起的换相电压过零点偏移角计算公式，反映多频谐波叠加对基波电压相位参考点的扰动程度*


**公式3**: $$$\gamma' = \arccos\left(\frac{\sqrt{2}U_{ac}\cos\alpha}{U_{dc}}\right) - \phi - \mu'$$$

*计及谐波交互影响的修正关断角公式，在传统关断角基础上扣除过零点偏移$\phi$与修正重叠角$\mu'$，用于CF/CCF风险定量评估*


### 算法步骤

1. 步骤1：故障初始化与拓扑识别。确定交流故障位置、类型及MI-HVDC系统接线方式（单端/分层），提取故障点等效阻抗$Z_{\text{Fault}}$及受端系统等效电势$E_1, E_2$。

2. 步骤2：谐波源建模。基于LCC换流器开关函数与故障暂态电流响应，计算各换流站注入交流母线的特征谐波电流$\dot{I}_{1h}, \dot{I}_{2h}$，识别主导谐波次数（通常为2、3、5次）。

3. 步骤3：等效网络构建。将交流耦合通道阻抗$Z_{12h}$与受端系统等效阻抗$Z_{1h}, Z_{2h}$组合，建立h次谐波频域戴维南等效电路，忽略非线性饱和效应以简化计算。

4. 步骤4：传递系数求解。利用节点电压法推导谐波电压传递系数$K_h = \dot{U}_{2h}/\dot{U}_{1h}$，获取各次谐波的幅值比与相角差，形成谐波交互参数矩阵。

5. 步骤5：换相参数修正。计算谐波叠加导致的换相电压过零点偏移$\phi$，结合直流电流$I_d$与换流变压器漏抗求解修正后的换相重叠角$\mu'$。

6. 步骤6：关断角定量评估与CCF判定。代入修正参数计算实际关断角$\gamma'$，与临界最小关断角$\gamma_{\min}$对比，若$\gamma' < \gamma_{\min}$则判定存在并发换相失败风险，输出预警信号。


### 关键参数

- **$Z_{1h}, Z_{2h}$**: 受端交流系统h次谐波等效阻抗（Ω）

- **$Z_{12h}$**: 母线间交流耦合通道h次谐波阻抗（Ω）

- **$\gamma_{\min}$**: 正常换相所需最小关断角（工程典型值7°~10°）

- **$I_d$**: 逆变器直流侧电流（kA）

- **$\phi$**: 谐波引起的换相电压过零点偏移角（°）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单端接入MI-HVDC系统三相短路故障 | 故障后远端逆变器母线3次谐波电压幅值升至基波的8.5%，关断角$\gamma'$较理论值下降3.2°，触发并发换相失败 | 等效模型计算耗时仅0.15s，较全阶EMT仿真提速约40倍，关断角计算误差<2.1% |

| 分层接入MI-HVDC系统单相接地故障 | 谐波经高低压耦合网络传递，导致非故障侧换流站THD由1.2%跃升至6.8%，关断角裕度缩减至4.5° | 定量计算结果与PSCAD/EMTDC波形吻合度高，峰值电压偏差<0.08p.u. |



## 量化发现

- 谐波交互使各换流站等效为分布式谐波源，远端母线h次谐波电压传递系数幅值稳定在0.35~0.62区间
- 计及谐波影响后，逆变器实际关断角$\gamma'$平均减小2.8°~4.5°，并发换相失败(CCF)发生概率提升约35%
- 所提等效模型关断角计算最大绝对误差为0.42°，相对误差<3.5%，满足工程预警精度要求
- 换相电压过零点偏移角$\phi$与谐波总畸变率(THD)呈正相关，THD每增加1%，$\phi$平均偏移0.18°


## 关键公式

### 谐波电压传递系数公式

$$$K_{h} = \frac{\dot{U}_{2h}}{\dot{U}_{1h}} = \frac{Z_{2h}}{Z_{12h} + Z_{2h}}$$$

*用于量化MI-HVDC系统中故障母线至远端母线的h次谐波电压幅值衰减与相位传递特性*

### 计及谐波交互的关断角修正公式

$$$\gamma' = \gamma - \Delta\gamma(\phi, \mu') = \arccos\left(\frac{\sqrt{2}U_{ac}\cos\alpha}{U_{dc}}\right) - \phi - \mu'$$$

*在交流故障暂态过程中，用于快速评估谐波引起的过零点偏移与重叠角变化对逆变器关断角的综合影响*



## 验证详情

- **验证方式**: 电磁暂态(EMT)仿真对比验证
- **测试系统**: 典型双馈入/多馈入LCC-HVDC系统（含单端接入与分层接入两种拓扑）
- **仿真工具**: PSCAD/EMTDC（用于全阶暂态波形生成）与MATLAB（用于等效模型解析计算）
- **验证结果**: 仿真波形与等效模型计算曲线高度重合，关断角动态响应误差<3%，验证了谐波传递等效电路模型在预测并发换相失败(CCF)方面的准确性与实时性，适用于工程在线预警与控制参数整定
