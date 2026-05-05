---
title: "Hbsm"
type: method
tags: [hbsm]
created: "2026-05-05"
---

# Hbsm

## 定义与边界

0378-7796/© 2023 Elsevier B.V. All rights reserved. An accelerated detailed equivalent model for modular multilevel converters✩ Ramin Parvari a, Shaahin Filizadeh a,∗, Dharshana Muthumuni b a University of Manitoba, Winnipeg, MB R3T 5V6, Canada b Manitoba Hydro International, Winnipeg, MB R3P 1A3, C...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，hbsm在EMT仿真中用于解决特定问题。

基于相关研究，该方法在EMT仿真中的主要应用包括：
- 特定场景的电磁暂态分析
- 控制系统设计与验证
- 故障分析与保护协调

## 主要分支与机制

- 待补充（需要进一步研究确定具体分支）

## 形式化表达


### 核心数学表达

从相关研究提取的关键公式：

$$P_{T\_cond}=U_{CE}i_{CE}=(R_{T0}i_{CE}+U_{CE0})i_{CE}$$

$$P_{D\_cond}=U_D i_F=(R_{D0}i_F+U_{D0})i_F$$

$$P_{pa\_cond}=\left\{\int_{t_1}^{t_2} P_{T\_cond}[\rho_1 n_{pa}+\rho_2(N-n_{pa})]+P_{D\_cond}[\rho_2 n_{pa}+\rho_1(N-n_{pa})]d\tau\right\}/(t_2-t_1)$$

$$\rho_1=0,\ \rho_2=1,\ i_{pa}>0;\qquad \rho_1=1,\ \rho_2=0,\ i_{pa}<0$$

$$

*桥臂电流方向判别函数；用于确定半桥子模块中电流经IGBT还是二极管流通。*


**公式5**: $$





## 适用边界与失败模式


基于证据边界的分析：





**潜在失效模式**：
- 参数设置不当可能导致仿真不稳定
- 特定工况下可能产生数值误差
- 需要进一步研究确定具体失效边界

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统基础
- [[control-system]] - 控制系统基础

## 代表性来源

- [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters]]
- [[非隔离型直流变压器的快速电磁暂态等效建模方法]]
- [[适用于交直流混联电网的ch-mmc电磁暂态快速仿真模型-15]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
