---
title: "Current Trajectory Similarity"
type: method
tags: [current-trajectory-similarity]
created: "2026-05-05"
---

# Current Trajectory Similarity

## 定义与边界

本文提出一种基于EMTP/TACS的限流熔断器经验模型，核心思想是将复杂的电弧物理过程解耦为电压上升与下降两个独立阶段进行等效。在熔断起弧初期，电弧电压的快速爬升主要由介质恢复与电弧拉长主导，模型采用等效电容并联于主回路，利用$i=C rac{dv}{dt}$关系将电流变化率转化为电压上升率；在电弧稳定燃烧至熄弧阶段，采用分段非线性电阻拟合实测伏安特性，表征电流衰减与能量耗散过程。整个状态切换由TACS（Transient Analysis of Control Systems）逻辑模块实现，通过实时积分计算焦耳热并与熔断阈值比较，结合过渡电压阈值触发开关动作。该方法完全规避了传统Mayr/C...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，current-trajectory-similarity在EMT仿真中用于解决特定问题。

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

- [[empirical-model-of-a-current-limiting-fuse-using-emtp]]
- [[neutral-conductor-current-in-three-phase-networks-with-compact-fluorescent-lamps]]
- [[a-new-topology-for-current-limiting-hvdc-circuit-breaker]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
