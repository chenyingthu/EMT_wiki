---
title: "Electromagnetic Transient Analysis Using a Frequency Dependent Network Equivalent for Power Systems Integrating Wind Generation Sources"
type: source
authors: ['未知']
year: 2024
journal: "2024 IEEE Power & Energy Society General Meeting (PESGM);2024; ; ;10.1109/PESGM51994.2024.10688470"
tags: ['frequency-dependent', 'network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/15/Electromagnetic transient analysis using a frequency dependent network equivalent for power systems_Verduzco-Durán 等_2024.pdf"]
---

# Electromagnetic Transient Analysis Using a Frequency Dependent Network Equivalent for Power Systems Integrating Wind Generation Sources

**作者**: 
**年份**: 2024
**来源**: `15/Electromagnetic transient analysis using a frequency dependent network equivalent for power systems_Verduzco-Durán 等_2024.pdf`

## 摘要

—This article addresses the application of a reduced order representation for analysis of power systems with wind gen- eration sources under fault conditions. A frequency-dependent network equivalent (FDNE) based on a rational function in the discrete-time is used to model the external area of the power system. The characterization of the frequency-dependent terminal admittance at the boundary busbar is carried out through the excitation of a constant voltage source at variable frequency modeled by a multisine signal. Parameter identiﬁcation techniques based on the recursive least squares method are applied. Regarding the wind energy conversion system (WECS), a type-4 wind turbine based on a permanent magnet synchronous generator with a full-scale back-to-back converter is used. The WECS c

## 核心贡献


- 提出基于离散时间有理函数的频变网络等值模型，实现外部电网降阶建模
- 采用多正弦信号激励与递推最小二乘法，完成边界母线频变导纳参数辨识
- 在含四型风电机组的两区域系统中验证等值模型，显著提升故障仿真效率


## 使用的方法


- [[fdne-model|FDNE]]
- [[离散时间有理函数逼近|离散时间有理函数逼近]]
- [[多正弦信号激励|多正弦信号激励]]
- [[递推最小二乘法参数辨识|递推最小二乘法参数辨识]]
- [[诺顿等值源集成|诺顿等值源集成]]


## 涉及的模型


- [[四型风力发电机组|四型风力发电机组]]
- [[永磁同步发电机-pmsg|永磁同步发电机(PMSG)]]
- [[全功率背靠背变流器|全功率背靠背变流器]]
- [[kundur两区域电力系统|Kundur两区域电力系统]]
- [[频变网络等值模型|频变网络等值模型]]


## 相关主题


- [[电磁暂态分析|电磁暂态分析]]
- [[动态等值与降阶建模|动态等值与降阶建模]]
- [[风电并网仿真|风电并网仿真]]
- [[故障暂态分析|故障暂态分析]]
- [[参数辨识|参数辨识]]
- [[计算效率优化|计算效率优化]]


## 主要发现


- 等值模型在单相与三相接地故障下能高精度复现全阶模型的暂态响应波形
- 相比全阶详细模型，FDNE显著降低CPU计算耗时，同时保持高仿真精度
- 仿真结果与PSCAD/EMTDC对比验证，证实了降阶等值方法的有效性


