---
title: "A Semi-Analytical Approach for State-Space Electromagnetic Transient Simulation"
type: source
year: 2024
journal: "IEEE Open Access Journal of Power and Energy;2024;11; ;10.1109/OAJPE.2024.3444272"
created: "2026-04-13"
sources: ["EMT_Doc/03/Xiong 等 - 2024 - A Semi-Analytical Approach for State-Space Electromagnetic Transient Simulation.pdf"]
---

# A Semi-Analytical Approach for State-Space Electromagnetic Transient Simulation

**年份**: 2024
**来源**: `03/Xiong 等 - 2024 - A Semi-Analytical Approach for State-Space Electromagnetic Transient Simulation.pdf`

## 摘要

This paper proposes a semi-analytical approach for efficient and accurate electromagnetic transient (EMT) simulation of a power grid. The approach first derives a high-order semi-analytical solution (SAS) of the grid’s state-space EMT model using the differential transformation (DT), and then evaluates the solution over enlarged, variable time steps to significantly accelerate the simulations while maintaining its high accuracy on detailed fast EMT dynamics. The approach also addresses switches during large time steps by using a limit violation detection algorithm with a binary search-enhanced quadratic interpolation. Case studies are conducted on EMT models of the IEEE 39-bus system and large-scale systems to demonstrate the merits of the new simulation approach against traditional numeri

## 核心贡献


- 基于微分变换推导状态空间EMT模型高阶半解析解，实现灵活选择求解阶数与步长
- 提出基于截断误差估计的多阶段变步长策略，在保持精度的同时显著提升计算效率
- 设计二分搜索增强二次插值的越限检测算法，精准定位大步长下的开关切换时刻


## 使用的方法


- [[半解析解法|半解析解法]]
- [[微分变换法|微分变换法]]
- [[状态空间法|状态空间法]]
- [[变步长仿真|变步长仿真]]
- [[密集输出机制|密集输出机制]]
- [[二分搜索增强二次插值|二分搜索增强二次插值]]


## 涉及的模型


- [[r-l-c电路|R-L-C电路]]
- [[vbr同步发电机模型|VBR同步发电机模型]]
- [[发电机控制器|发电机控制器]]
- [[逆变器型资源-ibr-模型|逆变器型资源(IBR)模型]]
- [[ieee-39节点系统|IEEE 39节点系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[状态空间建模|状态空间建模]]
- [[变步长算法|变步长算法]]
- [[开关事件处理|开关事件处理]]
- [[大规模电网仿真|大规模电网仿真]]


## 主要发现


- 在IEEE 39节点及大规模系统测试中，该方法相比传统数值法显著加速且保持高精度
- 变步长策略结合密集输出机制，可在扩大步长时准确重构内部高频动态细节
- 改进的越限检测算法能精准捕捉大步长下的开关切换时刻，有效避免仿真误差累积


