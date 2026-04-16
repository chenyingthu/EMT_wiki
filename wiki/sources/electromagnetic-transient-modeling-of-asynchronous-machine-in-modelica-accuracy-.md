---
title: "Electromagnetic Transient Modeling of Asynchronous Machine in Modelica, Accuracy, and Performance Assessment"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Access;2024;12; ;10.1109/ACCESS.2024.3462255"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/16/Choi 等 - 2025 - Electromagnetic Transient Simulation of Large-Scale Inverter-Based Resources With High-Granularity.pdf"]
---

# Electromagnetic Transient Modeling of Asynchronous Machine in Modelica, Accuracy, and Performance Assessment

**作者**: 
**年份**: 2024
**来源**: `16/Choi 等 - 2025 - Electromagnetic Transient Simulation of Large-Scale Inverter-Based Resources With High-Granularity.pdf`

## 摘要

Classical EMT-type simulators are mostly programmed in procedural languages, e.g. Fortran or C. In these languages, the focus is mainly on the solution methods. Modern languages, such as Modelica, are declarative and primarily focused on modeling and simulation. Modelica offers a much higher abstraction level, which makes the codes more concise and understandable. This paper contributes to the electromagnetic transient modeling and simulation of asynchronous machines in Modelica. In this paper, the modeling of a three-phase squirrel cage (single and double cage) and wound-rotor induction machine in three different reference frames is described and implemented. The accuracy and performance of Modelica models are compared and validated with the classical modeling approach used in the referen

## 核心贡献


- 基于Modelica实现异步电机多参考系电磁暂态建模，摆脱固定步长求解限制
- 提出基于磁链状态变量的四阶非线性微分代数方程建模，提升计算效率
- 验证变步长求解器在电机顺序启动仿真中的优势，实现无附加阻尼直接收敛


## 使用的方法


- [[modelica方程建模|Modelica方程建模]]
- [[变步长求解器|变步长求解器]]
- [[park坐标变换|Park坐标变换]]
- [[磁链状态空间法|磁链状态空间法]]
- [[微分代数方程求解|微分代数方程求解]]


## 涉及的模型


- [[异步电机|异步电机]]
- [[单鼠笼感应电机|单鼠笼感应电机]]
- [[双鼠笼感应电机|双鼠笼感应电机]]
- [[绕线式感应电机|绕线式感应电机]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[声明式建模|声明式建模]]
- [[电机顺序启动|电机顺序启动]]
- [[故障与孤岛仿真|故障与孤岛仿真]]
- [[数值收敛性分析|数值收敛性分析]]


## 主要发现


- 变步长求解器结合Modelica模型在电机顺序启动暂态过程中实现快速高精度仿真
- 模型在不同容差下直接收敛，无需并联人工阻尼电阻即可有效消除数值振荡
- 与EMTP经典方法对比验证了声明式建模在暂态精度与计算效率上的等效性


