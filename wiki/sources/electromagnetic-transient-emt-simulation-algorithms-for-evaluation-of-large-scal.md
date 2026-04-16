---
title: "Electromagnetic Transient (EMT) Simulation Algorithms for Evaluation of Large-Scale Extreme Fast Charging Systems (T&amp; D Models)"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2023;38;5;10.1109/TPWRS.2022.3212639"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/15/Electromagnetic transient (EMT) simulation algorithms for evaluation of large-scale extreme fast cha_Debnath和Choi_2023.pdf"]
---

# Electromagnetic Transient (EMT) Simulation Algorithms for Evaluation of Large-Scale Extreme Fast Charging Systems (T&amp; D Models)

**作者**: 
**年份**: 2023
**来源**: `15/Electromagnetic transient (EMT) simulation algorithms for evaluation of large-scale extreme fast cha_Debnath和Choi_2023.pdf`

## 摘要

—Simulation of high-ﬁdelity models of extreme fast charging (XFC) systems and large-area power grids with many XFCs can be time consuming in traditional simulators. Traditional simulators use a single method of discretization for all the com- ponents that results in imposing a large computational burden of inverting a large matrix as well as increased computations related to single method of discretization (that is typically a trapezoidal method). To overcome the problem of simulating large-area power grids with many XFCs, in this paper, advanced numerical simula- tion algorithms are applied for the ﬁrst time together to reduce the dimension of matrix inversion. The algorithms include numerical stiffness-based segregation, time constant-based segregation, clus- tering and aggregation on di

## 核心贡献


- 首次联合应用刚度分离时间常数分离DAE聚类与多阶积分算法降低矩阵求逆维度
- 提出基于状态空间法的混合离散策略替代单一梯形法有效减轻大规模系统计算负担
- 构建含数百个超快充站的高保真输配电EMT模型实现电力电子与电网协同高效仿真


## 使用的方法


- [[混合离散化|混合离散化]]
- [[多阶积分法|多阶积分法]]
- [[状态空间法|状态空间法]]
- [[微分代数方程聚类聚合|微分代数方程聚类聚合]]
- [[数值刚度分离|数值刚度分离]]
- [[时间常数分离|时间常数分离]]


## 涉及的模型


- [[超快充系统-xfc|超快充系统(XFC)]]
- [[两电平三相逆变器|两电平三相逆变器]]
- [[dc-dc升压变换器|DC-DC升压变换器]]
- [[配电网|配电网]]
- [[输电网|输电网]]
- [[ieee标准测试系统|IEEE标准测试系统]]
- [[同步发电机|同步发电机]]
- [[变压器|变压器]]
- [[输电线路|输电线路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[超快充系统建模|超快充系统建模]]
- [[输配电网协同仿真|输配电网协同仿真]]
- [[仿真加速算法|仿真加速算法]]
- [[高渗透率电力电子电网|高渗透率电力电子电网]]
- [[大规模系统仿真|大规模系统仿真]]


## 主要发现


- 在含十五个超快充站的配电网仿真中算法较传统软件实现最高十八倍加速比
- 在含三百个超快充站的输配电系统仿真中算法实现最高二百七十一倍加速比
- 混合离散与多阶积分策略有效解决单一梯形法导致的大矩阵求逆计算瓶颈


