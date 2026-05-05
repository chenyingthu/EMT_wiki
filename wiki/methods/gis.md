---
title: "Gis"
type: method
tags: [gis]
created: "2026-05-05"
---

# Gis

## 定义与边界

本文提出一种基于实测频变阻抗特性的磁芯非线性等效电路建模方法。首先，在不同直流偏置电流下测量磁芯的复阻抗频率特性，覆盖从线性区到深度饱和区的工作点。随后，针对每个偏置电流点，利用有理函数拟合与部分分式展开技术，将频变阻抗综合为由多个RL并联支路构成的线性集总参数等效电路（Foster网络）。接着，对各支路电阻和电感值随电流的变化进行平滑插值，并通过积分运算推导出EMTP软件所需的电压-电流(V-I)和磁链-电流(Φ-I)非线性特性曲线。最后，采用指数离散化策略将特性曲线外推至10 kA高电流范围，确保模型在宽频带（kHz~MHz）与宽电流范围内均能精确表征磁芯的频变损耗与磁饱和非线性，可直接嵌...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，gis在EMT仿真中用于解决特定问题。

基于相关研究，该方法在EMT仿真中的主要应用包括：
- 特定场景的电磁暂态分析
- 控制系统设计与验证
- 故障分析与保护协调

## 主要分支与机制

- 待补充（需要进一步研究确定具体分支）

## 形式化表达

- 待补充



## 适用边界与失败模式

- 待补充

**潜在失效模式**：
- 参数设置不当可能导致仿真不稳定
- 特定工况下可能产生数值误差
- 需要进一步研究确定具体失效边界

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统基础
- [[control-system]] - 控制系统基础

## 代表性来源

- [[an-efficient-and-accurate-calculation-of-electric-field-and-temperature-distribu]]
- [[application-of-emtp-in-the-research-of-uhv-ac-power-transmission]]
- [[an-improved-high-frequency-white-box-lossy-transformer-model-for-the-calculation]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
