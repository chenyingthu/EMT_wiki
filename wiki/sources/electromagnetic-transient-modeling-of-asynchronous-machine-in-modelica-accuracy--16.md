---
title: "Electromagnetic Transient Modeling of Asynchronous Machine in Modelica, Accuracy, and Performance Assessment"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Access;2024;12; ;10.1109/ACCESS.2024.3462255"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/16/Masoom和Mahseredjian - 2024 - Electromagnetic Transient Modeling of Asynchronous Machine in Modelica, Accuracy, and Performance As.pdf"]
---

# Electromagnetic Transient Modeling of Asynchronous Machine in Modelica, Accuracy, and Performance Assessment

**作者**: 
**年份**: 2024
**来源**: `16/Masoom和Mahseredjian - 2024 - Electromagnetic Transient Modeling of Asynchronous Machine in Modelica, Accuracy, and Performance As.pdf`

## 摘要

Classical EMT-type simulators are mostly programmed in procedural languages, e.g. Fortran or C. In these languages, the focus is mainly on the solution methods. Modern languages, such as Modelica, are declarative and primarily focused on modeling and simulation. Modelica offers a much higher abstraction level, which makes the codes more concise and understandable. This paper contributes to the electromagnetic transient modeling and simulation of asynchronous machines in Modelica. In this paper, the modeling of a three-phase squirrel cage (single and double cage) and wound-rotor induction machine in three different reference frames is described and implemented. The accuracy and performance of Modelica models are compared and validated with the classical modeling approach used in the referen

## 核心贡献


- 基于声明式语言构建异步电机EMT详细模型，支持单双鼠笼及绕线转子结构
- 采用磁链作状态变量建立多参考系四阶模型，显著提升微分方程求解效率
- 验证变步长求解器在电机顺序启动中的优势，无需人工阻尼即可保证收敛


## 使用的方法


- [[声明式建模|声明式建模]]
- [[变步长求解器|变步长求解器]]
- [[坐标变换|坐标变换]]
- [[磁链状态空间法|磁链状态空间法]]
- [[梯形积分法|梯形积分法]]
- [[修正增广节点分析法|修正增广节点分析法]]


## 涉及的模型


- [[异步电机|异步电机]]
- [[单鼠笼感应电机|单鼠笼感应电机]]
- [[双鼠笼感应电机|双鼠笼感应电机]]
- [[绕线转子感应电机|绕线转子感应电机]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[基于方程建模|基于方程建模]]
- [[电机顺序启动|电机顺序启动]]
- [[故障与孤岛仿真|故障与孤岛仿真]]
- [[变步长求解器应用|变步长求解器应用]]


## 主要发现


- 变步长求解器在顺序启动仿真中兼具高精度与快速度，性能优于传统定步长
- 模型在不同容差下直接收敛，无需并联阻尼电阻即可有效抑制数值振荡
- 故障与孤岛工况结果与EMTP经典模型高度一致，验证了声明式建模准确性


