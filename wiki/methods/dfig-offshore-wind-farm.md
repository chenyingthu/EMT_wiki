---
title: "Dfig Offshore Wind Farm"
type: method
tags: [dfig-offshore-wind-farm]
created: "2026-05-05"
---

# Dfig Offshore Wind Farm

## 定义与边界

Electrical Power and Energy Systems 148 (2023) 108928 0142-0615/© 2022 Elsevier Ltd. All rights reserved. Modeling for large-scale offshore wind farm using multi-thread State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University (NCE...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，dfig-offshore-wind-farm在EMT仿真中用于解决特定问题。

基于相关研究，该方法在EMT仿真中的主要应用包括：
- 特定场景的电磁暂态分析
- 控制系统设计与验证
- 故障分析与保护协调

## 主要分支与机制

- 待补充（需要进一步研究确定具体分支）

## 形式化表达

### 核心数学表达

DFIG转子侧功率：
$$P_r = s \cdot P_s$$

其中$s$为转差率：
$$s = rac{\omega_s - \omega_r}{\omega_s}$$

直流母线电压控制：
$$C_{dc} rac{dv_{dc}}{dt} = P_{gen} - P_{grid}$$




## 适用边界与失败模式

**适用条件**：
- 双馈感应风力发电机组建模
- 变速恒频运行范围（$s = \pm 0.3$）
- 海上风电场并网仿真

**失效边界**：
- 转差率超出设计范围
- 直流母线过压/欠压保护动作
- 电网故障导致Crowbar动作


**潜在失效模式**：
- 参数设置不当可能导致仿真不稳定
- 特定工况下可能产生数值误差
- 需要进一步研究确定具体失效边界

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统基础
- [[control-system]] - 控制系统基础

## 代表性来源

- [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin]]
- [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f]]
- [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
