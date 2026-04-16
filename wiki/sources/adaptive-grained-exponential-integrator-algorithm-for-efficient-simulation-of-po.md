---
title: "Adaptive-Grained Exponential Integrator Algorithm for Efficient Simulation of Power Converter Systems"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;2;10.1109/TPWRD.2025.3539681"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Paull 等 - 2025 - Adaptive-Grained Exponential Integrator Algorithm for Efficient Simulation of Power Converter System.pdf"]
---

# Adaptive-Grained Exponential Integrator Algorithm for Efficient Simulation of Power Converter Systems

**作者**: 
**年份**: 2025
**来源**: `05/Paull 等 - 2025 - Adaptive-Grained Exponential Integrator Algorithm for Efficient Simulation of Power Converter System.pdf`

## 摘要

—Electromagnetic transient (EMT) simulation is increasingly important for complex power electronic converter system design and validation. This paper proposes an adaptive-grained exponential integrator (AGEI) algorithm designed to efﬁciently simulate power electronic networks. The AGEI algorithm relies on precomputation of carefully-chosen discretization steps to reduce memory burden. It then performs

## 核心贡献


- 提出自适应粒度指数积分算法，通过预计算离散步长降低内存负担。
- 结合事件驱动框架在开关事件间进行顺序积分，加速暂态过程求解。
- 采用变步长高阶积分策略动态调整项数，具备L稳定性适配刚性系统。


## 使用的方法


- [[指数积分法|指数积分法]]
- [[离散状态事件驱动仿真|离散状态事件驱动仿真]]
- [[状态空间方程法|状态空间方程法]]
- [[变步长高阶积分|变步长高阶积分]]


## 涉及的模型


- [[电力电子变换器详细模型|电力电子变换器详细模型]]
- [[刚性-非刚性电路网络|刚性/非刚性电路网络]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[电力电子系统仿真|电力电子系统仿真]]
- [[数值积分算法|数值积分算法]]
- [[开关事件处理|开关事件处理]]
- [[刚性系统求解|刚性系统求解]]


## 主要发现


- 硬件实验验证算法精度，典型变换器仿真速度较Simulink提升8倍以上。
- 相比PLECS速度提升3倍以上，在纯直流输入或刚性系统中效率增益更显著。
- 算法有效平衡运行时间与计算开销，消除数值振荡并保证高稳定性。


