---
title: "Including Magnetic Saturation in Voltage-Behind-Reactance Induction Machine Model for EMTP-Type Solution"
type: source
authors: ['Liwei Wang', 'Juri Jatskevich']
year: 2010
journal: "IEEE Transactions on Power Systems;2010;25;2;10.1109/TPWRS.2009.2032659"
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/23/Wang和Jatskevich - 2010 - Including Magnetic Saturation in Voltage-Behind-Reactance Induction Machine Model for EMTP-Type Solu.pdf"]
---

# Including Magnetic Saturation in Voltage-Behind-Reactance Induction Machine Model for EMTP-Type Solution

**作者**: Liwei Wang, Juri Jatskevich
**年份**: 2010
**来源**: `23/Wang和Jatskevich - 2010 - Including Magnetic Saturation in Voltage-Behind-Reactance Induction Machine Model for EMTP-Type Solu.pdf`

## 摘要

—A voltage-behind-reactance (VBR) machine model has been recently proposed for the electro-magnetic transient programs (EMTP)-type simulation programs. The VBR model greatly improves numerical accuracy and efﬁciency compared with the traditional and phase-domain (PD) models. This paper extends the previous research and presents an approach to include magnetic saturation into the VBR induction machine model. The presented method takes into account the axes static and dynamic cross saturation, whereas the nonlinear magnetic characteristic is represented using a piecewise-linear method that is suitable for the EMTP solution approach. Case studies verify the new saturable VBR model and show that it has improved numerical stability and accuracy even at large time steps. Index Terms—Electro-magn

## 核心贡献


- 提出将磁饱和引入VBR感应电机模型的方法适配EMTP求解架构
- 考虑dq轴静态与动态交叉饱和采用分段线性法表征非线性磁化特性
- 实现非迭代求解机制显著提升大时间步长下的数值稳定性与精度


## 使用的方法


- [[电压后电抗模型-vbr|电压后电抗模型(VBR)]]
- [[分段线性近似法|分段线性近似法]]
- [[任意参考系变换|任意参考系变换]]
- [[emtp型节点分析|EMTP型节点分析]]
- [[非迭代求解|非迭代求解]]


## 涉及的模型


- [[感应电机|感应电机]]
- [[vbr模型|VBR模型]]
- [[相域模型|相域模型]]
- [[主磁路饱和模型|主磁路饱和模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[磁饱和建模|磁饱和建模]]
- [[数值稳定性分析|数值稳定性分析]]
- [[大时间步长仿真|大时间步长仿真]]
- [[电机网络接口|电机网络接口]]


## 主要发现


- 新模型在较大时间步长下保持高数值稳定性避免传统模型发散问题
- 分段线性法实现非迭代求解大幅降低CPU耗时并提升计算效率
- 仿真结果与经典模型高度吻合验证了交叉饱和表征的准确性


