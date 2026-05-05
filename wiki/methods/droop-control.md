---
title: "Droop Control"
type: method
tags: [droop-control]
created: "2026-05-05"
---

# Droop Control

## 定义与边界

提出一种基于构网型逆变器的光储混合电站黑启动控制与仿真方法。系统直流侧由光伏阵列与电池储能通过DC/DC变换器并联构成，交流侧采用H桥逆变器、LC滤波器及升压变压器。控制架构采用主从双层设计：主控制环基于下垂特性，根据PCC点注入的有功与无功功率实时调节电压幅值与频率；次控制环采用PI控制器消除稳态偏差，将电压与频率恢复至额定值。控制信号经dq同步旋转坐标系下的电压/电流双环嵌套处理生成参考电压，最终通过PWM调制驱动开关器件。黑启动过程中，直流母线电压由储能Buck-Boost变换器恒定控制，实现交直流侧解耦。储能优先供电，超出其放电上限后由光伏阵列补充。整体方案在PSCAD中搭建高保真电磁...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，droop-control在EMT仿真中用于解决特定问题。

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

- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]
- [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve]]
- [[active-damping-control-and-parameter-calculation-for-resonance-suppression-in-dc-distribution]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
