---
title: "Huang 等 | A Heterogeneous Multiscale Method for Efficient Simulation of Power Systems With Inverter-Based Reso"
type: source
authors: ['未知']
year: 2025
journal: ""
tags: ['ibg']
created: "2026-04-13"
sources: ["EMT_Doc/01/Huang 等 - 2025 - A Heterogeneous Multiscale Method for Efficient Simulation of Power Systems With Inverter-Based Reso.pdf"]
---

# Huang 等 | A Heterogeneous Multiscale Method for Efficient Simulation of Power Systems With Inverter-Based Reso

**作者**: 
**年份**: 2025
**来源**: `01/Huang 等 - 2025 - A Heterogeneous Multiscale Method for Efficient Simulation of Power Systems With Inverter-Based Reso.pdf`

## 摘要

—As inverter-based resources (IBRs) penetrate power systems, the dynamics become more complex, exhibiting multiple timescales, including electromagnetic transient (EMT) dynamics of power electronic controllers and electromechanical dynamics of synchronous generators. Consequently, the power system model becomes highly stiff, posing a challenge for efficient simulation using existing methods that focus on dynamics within a single timescale. This paper proposes a Heterogeneous Multiscale Method for highly efficient multi-timescale simulation of a power system represented by its EMT model. The new method alternates between the microscopic EMT model of the system and an automatically reduced macroscopic model, varying the step size accordingly to achieve significant acceleration while maintain

## 核心贡献


- 提出异构多尺度框架，实现EMT微观模型至宏观模型的在线自动降阶
- 引入核卷积方法近似宏观动态，无需显式降阶即可平滑衔接微宏观过程
- 结合半解析解法构建变步长机制，动态跳过非关键微观动态并保留关键暂态


## 使用的方法


- [[异构多尺度方法-hmm|异构多尺度方法(HMM)]]
- [[半解析解法-sas|半解析解法(SAS)]]
- [[变步长求解器|变步长求解器]]
- [[核卷积近似|核卷积近似]]
- [[微分变换|微分变换]]
- [[在线自动降阶|在线自动降阶]]


## 涉及的模型


- [[逆变器型资源-ibr|逆变器型资源(IBR)]]
- [[同步发电机|同步发电机]]
- [[全阶emt网络模型|全阶EMT网络模型]]
- [[ieee-39节点系统|IEEE 39节点系统]]
- [[两区域系统|两区域系统]]


## 相关主题


- [[多时间尺度仿真|多时间尺度仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[高渗透率ibr电网|高渗透率IBR电网]]
- [[刚性微分方程求解|刚性微分方程求解]]
- [[高效时域仿真|高效时域仿真]]


## 主要发现


- 在IEEE 39节点等系统中验证，算法在保持快慢动态精度的同时实现显著加速
- 半解析变步长机制有效跳过非关键微观暂态，大幅提升长时段仿真计算效率
- 理论严格证明了精度、复杂度与加速比的定量关系，确保多尺度仿真数值稳定


