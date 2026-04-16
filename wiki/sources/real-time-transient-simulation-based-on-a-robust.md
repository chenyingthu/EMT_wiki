---
title: "Real-Time Transient Simulation Based on a Robust"
type: source
authors: ['未知']
year: 2007
journal: ""
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/33/tpwrs.2007.907963.pdf.pdf"]
---

# Real-Time Transient Simulation Based on a Robust

**作者**: 
**年份**: 2007
**来源**: `33/tpwrs.2007.907963.pdf.pdf`

## 摘要

—Real-time digital simulation of large power systems requires not only signiﬁcant computational power but also simpler and accurate models. This paper proposes a new approach for transient simulation of power systems using a robust two-layer network equivalent model and an advanced PC-Cluster based parallel real-time simulator. Using a combination of well estab- lished ﬁtting and optimization methods, the generated low-order model is of high accuracy compared to its full model over a wide frequency bandwidth. The merits of this method are its robustness in terms of stability and positive-realness, its accuracy at not only transient frequencies but also at dc and power frequency, and its optimal order determination feature. To validate the new method, a realistic large-scale power system—th

## 核心贡献



- 提出了一种鲁棒的双层网络等值（TLNE）模型，将外部系统划分为表层（降阶频变线路模型）和深层（低阶FDNE），有效降低了大规模系统实时仿真的计算负担。
- 开发了基于PC集群的并行实时仿真架构，结合向量拟合与优化算法，实现了宽频带高精度低阶模型的自动生成与最优阶数确定。

## 使用的方法


- [[vector-fitting]]
- [[parallel]]
- [[real-time]]

## 涉及的模型


- [[fdne]]
- [[network-equivalent]]
- [[transmission-line]]

## 相关主题


- [[frequency-dependent]]
- [[passivity]]
- [[real-time]]

## 主要发现



- 所提低阶等值模型在宽频带范围内具有高精度，且在直流、工频及暂态频率下均能保持优异的准确性。
- 该方法在稳定性和正实性（无源性）方面具有强鲁棒性，能够自动确定最优模型阶数，并在PC集群上实现了20微秒步长的高效实时仿真，结果与ATP/EMTP全规模离线仿真高度吻合。