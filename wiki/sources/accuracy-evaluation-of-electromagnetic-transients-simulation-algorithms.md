---
title: "Accuracy Evaluation of Electromagnetic Transients Simulation Algorithms"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Delivery;2022;37;3;10.1109/TPWRD.2021.3099008"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Zhao 等 - 2022 - Accuracy Evaluation of Electromagnetic Transients Simulation Algorithms.pdf"]
---

# Accuracy Evaluation of Electromagnetic Transients Simulation Algorithms

**作者**: 
**年份**: 2022
**来源**: `05/Zhao 等 - 2022 - Accuracy Evaluation of Electromagnetic Transients Simulation Algorithms.pdf`

## 摘要

—This paper introduces a novel frequency domain tech- nique to globally evaluate the accuracy of electro-magnetic tran- sient simulations. It is shown that simulation accuracy at low frequencies can sometimes be poorer than at high frequency. A modiﬁed approach which quantiﬁes accuracy from a driving point as a function of frequency is also introduced that uses the Bilinear Transformation and Norton equivalents, to produce a “simulation accuracy spectrum”. This approach can be applied to large systems without explicitly forming state space equations. It also permits the accuracy analysis of networks with distributed components such as frequency dependent transmission lines. Two examples are used to verify the proposed technique, a small network with a frequency dependent transmission line 

## 核心贡献


- 提出频域全局评估方法，突破传统单一元件精度分析的局限性
- 结合双线性变换与诺顿等效，构建无需状态方程的仿真精度频谱
- 首次实现含频率相关线路等分布参数网络的系统级数值精度量化


## 使用的方法


- [[频域映射分析|频域映射分析]]
- [[双线性变换|双线性变换]]
- [[诺顿等效|诺顿等效]]
- [[状态空间法|状态空间法]]
- [[梯形积分|梯形积分]]
- [[驱动点导纳法|驱动点导纳法]]


## 涉及的模型


- [[频率相关输电线路|频率相关输电线路]]
- [[通用线路模型|通用线路模型]]
- [[lcc-model|LCC]]
- [[ieee-39节点系统|IEEE 39节点系统]]
- [[rlc集总网络|RLC集总网络]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[仿真精度评估|仿真精度评估]]
- [[数值积分误差|数值积分误差]]
- [[分布参数网络|分布参数网络]]
- [[频域建模|频域建模]]


## 主要发现


- 系统级评估表明低频段仿真误差可能大于高频段，颠覆传统认知
- 驱动点精度频谱可准确量化大电网在不同频段的数值积分仿真误差
- 所提方法在含通用线路模型的IEEE 39节点LCC-HVDC系统中验证有效


