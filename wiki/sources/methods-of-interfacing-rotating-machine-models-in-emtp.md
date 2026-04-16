---
title: "Methods of Interfacing Rotating Machine Models in EMTP"
type: source
authors: ['未知']
year: 2010
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/26/Wang 等 - 2010 - Methods of interfacing rotating machine models in transient simulation programs.pdf"]
---

# Methods of Interfacing Rotating Machine Models in EMTP

**作者**: 
**年份**: 2010
**来源**: `26/Wang 等 - 2010 - Methods of interfacing rotating machine models in transient simulation programs.pdf`

## 摘要

—The electromagnetic transient programs (EMTP-like tools) are based on the nodal (or modiﬁed nodal) equations that enable an efﬁcient numerical solution and, subsequently, fast time-domain simulations. The state-variable-based simulation programs, such as Simulink, are also used for studying the dynamics of electrical systems. Both the ofﬂine and real-time versions of these two types of simulation tools are widely used by the researchers and engineers in industry and academia to study the transient phenomena and dynamics in power systems with rotating electrical machines. This paper provides a summary of the interfacing techniques that are utilized to integrate the general-purpose models of electrical machines with the rest of the power system network for these studies. The interfacing met

## 核心贡献


- 系统总结旋转电机与电网的间接与直接接口技术，阐明其在EMTP及状态变量程序中的实现机制。
- 分析不同接口方法的数值特性与局限性，为仿真步长选择与结果评估提供理论指导。
- 对比相域模型与dq0变换模型的适用边界，指导针对暂态工况正确选择电机建模方案。


## 使用的方法


- [[节点分析法|节点分析法]]
- [[状态变量法|状态变量法]]
- [[间接接口技术|间接接口技术]]
- [[直接接口技术|直接接口技术]]
- [[park变换|Park变换]]
- [[耦合电路相域建模|耦合电路相域建模]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[感应电机|感应电机]]
- [[相域模型|相域模型]]
- [[dq0参考系模型|dq0参考系模型]]
- [[刚体机械模型|刚体机械模型]]


## 相关主题


- [[接口技术|接口技术]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[emtp工具|EMTP工具]]
- [[状态变量仿真|状态变量仿真]]
- [[旋转电机建模|旋转电机建模]]
- [[数值稳定性|数值稳定性]]
- [[不对称工况分析|不对称工况分析]]


## 主要发现


- 间接接口法易引入数值延迟与界面振荡，直接接口法精度更高但计算负担显著增加。
- 相域模型可直接处理不对称故障，dq0模型依赖坐标变换，两者在暂态精度上存在差异。
- 合理匹配接口方法与仿真步长可有效抑制数值不稳定，确保电机电网联合暂态仿真收敛。


