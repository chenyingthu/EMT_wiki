---
title: "Frequency Control"
type: method
tags: [frequency-control]
created: "2026-05-05"
---

# Frequency Control

## 定义与边界

提出一种基于EMT仿真的自动化动态频率扫描工具，集成于PSCAD/EMTDC平台。该方法通过在系统稳态运行点注入多频正弦扰动信号（电流或电压），记录PCC处的电压电流响应，利用离散傅里叶变换（DFT）提取频域幅值与相位。为消除电力电子系统的频率耦合效应，扫描在dq0坐标系下进行。通过矩阵运算获取变流器与电网的阻抗/导纳矩阵，构建闭环传递函数，并计算开环增益矩阵的特征值。最终利用特征值的伯德图分析增益裕度与相位裕度，预测系统的临界短路比（CSCR）及振荡频率，实现黑盒模型下的稳定性评估。...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，frequency-control在EMT仿真中用于解决特定问题。

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

- [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-]]
- [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid]]
- [[development-of-high-frequency-supraharmonic-models-of-small-scale-amplt5kw-singl]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
