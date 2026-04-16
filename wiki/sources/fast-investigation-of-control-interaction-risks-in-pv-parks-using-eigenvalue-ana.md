---
title: "Fast investigation of control interaction risks in PV parks using eigenvalue analysis in Modelica"
type: source
authors: ['A. Masoom']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112316. doi:10.1016/j.epsr.2025.112316"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Masoom 等 - 2026 - Fast investigation of control interaction risks in PV parks using eigenvalue analysis in Modelica.pdf"]
---

# Fast investigation of control interaction risks in PV parks using eigenvalue analysis in Modelica

**作者**: A. Masoom
**年份**: 2025
**来源**: `19、20、21/EMT_task_19/Masoom 等 - 2026 - Fast investigation of control interaction risks in PV parks using eigenvalue analysis in Modelica.pdf`

## 摘要

Fast investigation of control interaction risks in PV parks using eigenvalue a Hydro-Qu´ebec Research Institute, Varennes, QC J3 × 1S1, Canada b Department of Electrical Engineering, Polytechnique Montr´eal, Montreal, QC H3T 1J4, Canada c Department of Electrical and Electronics Engineering, Middle East Technical University, Turkey This paper contributes to the fast detection of control interaction risk in a PV park using the eigenvalue analysis

## 核心贡献


- 基于Modelica构建光伏场站EMT模型，自动提取线性化状态空间矩阵
- 无需简化模型，实现多工况下控制交互风险的快速特征值扫描与稳定性评估
- 结合EMT仿真与阻抗扫描验证，显著提升新能源并网稳定性分析效率与精度


## 使用的方法


- [[特征值分析|特征值分析]]
- [[modelica方程建模|Modelica方程建模]]
- [[微分代数方程线性化|微分代数方程线性化]]
- [[状态空间矩阵提取|状态空间矩阵提取]]
- [[阻抗扫描|阻抗扫描]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[模态分析|模态分析]]


## 涉及的模型


- [[光伏场站|光伏场站]]
- [[dc-ac变流器|DC-AC变流器]]
- [[升压变压器|升压变压器]]
- [[π型集电线路|π型集电线路]]
- [[含故障穿越逻辑的控制器|含故障穿越逻辑的控制器]]
- [[逆变器型资源|逆变器型资源]]
- [[保护系统|保护系统]]


## 相关主题


- [[控制交互风险|控制交互风险]]
- [[稳定性分析|稳定性分析]]
- [[新能源并网集成|新能源并网集成]]
- [[特征值与模态分析|特征值与模态分析]]
- [[阻抗稳定性分析|阻抗稳定性分析]]
- [[快速仿真评估|快速仿真评估]]


## 主要发现


- 相比传统方法，该框架在保持模型完整性的同时大幅缩短计算时间并提升精度
- 无需忽略输入滤波器等非线性环节，即可准确识别多工况下的潜在不稳定振荡模式
- 经EMT仿真与阻抗扫描交叉验证，该方法能有效定位控制交互风险并指导阻尼设计


