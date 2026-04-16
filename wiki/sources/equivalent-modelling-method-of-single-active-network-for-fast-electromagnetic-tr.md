---
title: "Equivalent Modelling Method of Single Active Network for Fast Electromagnetic Transient Simulation"
type: source
authors: ['未知']
year: 2025
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Gao 等 - 2021 - Equivalent Modelling Method of Single Active Bridge Converter by Pre-calculating the Current Zero-cr.pdf"]
---

# Equivalent Modelling Method of Single Active Network for Fast Electromagnetic Transient Simulation

**作者**: 
**年份**: 2025
**来源**: `18/Gao 等 - 2021 - Equivalent Modelling Method of Single Active Bridge Converter by Pre-calculating the Current Zero-cr.pdf`

## 摘要

As an important scheme for grid connection of photovoltaic, wind power and other DC power sources, modular isolated DC/DC converter (MIDC) has received extensive attention. The input parallel output series (IPOS) type single active bridge (SAB) converter is one of the common topologies of MIDC. Due to the high node admittance order, low simulation step size and the existence of uncontrolled rectifier bridge, its electromagnetic transient simulation efficiency is extremely low. This paper proposed an equivalent modeling method of SAB converter by the pre-calculating current zero-crossing. First, the topology and working principle of the SAB converter were analyzed to solve the inductor current expression in different modes. Secondly, the expression of the zero-crossing point of the inductan

## 核心贡献


- 提出基于电流过零点预计算的不控整流桥等效方法，避免插值计算
- 利用节点导纳矩阵对称性与稀疏性，推导SAB单元等效外端口方程
- 采用Lyapunov法证明等效模型稳定性，保障仿真数值收敛性


## 使用的方法


- [[电流过零点预计算|电流过零点预计算]]
- [[节点导纳矩阵等效|节点导纳矩阵等效]]
- [[梯形积分法离散化|梯形积分法离散化]]
- [[二值电阻等效|二值电阻等效]]
- [[lyapunov稳定性分析|Lyapunov稳定性分析]]


## 涉及的模型


- [[ipos型sab变换器|IPOS型SAB变换器]]
- [[不控整流桥|不控整流桥]]
- [[高频变压器|高频变压器]]
- [[igbt开关组|IGBT开关组]]
- [[midc|MIDC]]


## 相关主题


- [[电磁暂态仿真加速|电磁暂态仿真加速]]
- [[电力电子变换器等效建模|电力电子变换器等效建模]]
- [[直流电源并网|直流电源并网]]
- [[固定步长仿真|固定步长仿真]]
- [[数值稳定性分析|数值稳定性分析]]


## 主要发现


- 所提等效模型在PSCAD中验证，波形精度与详细模型高度一致
- 预计算过零点有效消除二极管插值开销，大幅提升高频开关仿真速度
- 模型在CCM与DCM模式下均保持稳定，加速比显著优于传统详细模型


