---
title: "Extending the Frequency Bandwidth of Transient Stability Simulation Using Dynamic Phasors"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Power Systems;2022;37;1;10.1109/TPWRS.2021.3094451"
tags: ['dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/18/Kulasza 等 - 2022 - Extending the Frequency Bandwidth of Transient Stability Simulation Using Dynamic Phasors.pdf"]
---

# Extending the Frequency Bandwidth of Transient Stability Simulation Using Dynamic Phasors

**作者**: 
**年份**: 2021
**来源**: `18/Kulasza 等 - 2022 - Extending the Frequency Bandwidth of Transient Stability Simulation Using Dynamic Phasors.pdf`

## 摘要

—This paper presents a novel approach to dynamic phasor-based transient stability simulation. The proposed method is based on the modiﬁed nodal analysis (MNA) approach to circuit simulation, which is used to construct continuous differential- algebraic equations (DAEs). The proposed method makes use of the stamp technique, which makes it possible to construct a general purpose MNA-based simulator. Stamp-based models for common power system components are derived in this work. A new MNA- based synchronous machine model is presented, which represents machines as nonlinear inductances instead of subtransient equiva- lents. The resultant continuous DAEs are numerically solved using the general purpose variable step and variable order library IDA. Simulation results from the IEEE 68 bus test sy

## 核心贡献


- 提出基于改进节点分析的动态相量暂态稳定仿真方法，构建连续微分代数方程。
- 引入Stamp技术构建通用仿真器，推导常见电力元件的标准化伴随模型。
- 提出新型同步机模型，将其表征为非线性电感以替代传统次暂态等效电路。


## 使用的方法


- [[动态相量法|动态相量法]]
- [[改进节点分析法-mna|改进节点分析法(MNA)]]
- [[stamp技术|Stamp技术]]
- [[变步长变阶数值积分-ida|变步长变阶数值积分(IDA)]]
- [[连续微分代数方程-dae-构建|连续微分代数方程(DAE)构建]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[vsc-hvdc|VSC-HVDC]]
- [[交流电网|交流电网]]
- [[非线性电感模型|非线性电感模型]]


## 相关主题


- [[暂态稳定仿真|暂态稳定仿真]]
- [[频带扩展|频带扩展]]
- [[次同步振荡分析|次同步振荡分析]]
- [[大规模电网仿真|大规模电网仿真]]
- [[电力电子设备接入|电力电子设备接入]]


## 主要发现


- 在IEEE多节点测试系统中验证，动态相量仿真结果与电磁暂态仿真高度吻合。
- 计算效率显著提升，CPU耗时最高可达传统电磁暂态仿真的两百倍。
- 有效突破准稳态假设限制，可准确模拟含电力电子设备的大规模交流网络。


