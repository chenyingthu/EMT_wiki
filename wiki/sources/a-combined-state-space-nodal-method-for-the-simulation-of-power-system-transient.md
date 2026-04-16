---
title: "A combined state-space nodal method for the simulation of power system transients"
type: source
authors: ['未知']
year: 2011
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/01/Dufour 等 - 2011 - A combined state-space nodal method for the simulation of power system transients.pdf"]
---

# A combined state-space nodal method for the simulation of power system transients

**作者**: 
**年份**: 2011
**来源**: `01/Dufour 等 - 2011 - A combined state-space nodal method for the simulation of power system transients.pdf`

## 摘要

—This paper presents a new solution method that com- bines state-space and nodal analysis for the simulation of electrical systems. The presented ﬂexible clustering of state-space-described electrical subsystems into a nodal method offers several advantages for the efﬁcient solution of switched networks, nonlinear functions, and for interfacing with nodal model equations. This paper ex- tends the concept of discrete companion branch equivalent of the nodal approach to state-space described systems and enables nat- ural coupling between them. The presented solution method is si- multaneous and enables beneﬁtting from the advantages of two dif- ferent modeling approaches normally exclusive from one another. Index Terms—Electromagnetic transients, nodal analysis, real time, state space. I. IN

## 核心贡献


- 提出状态空间节点联合求解法，将状态空间子系统灵活聚类并映射至全局节点导纳矩阵
- 将节点法离散伴随支路等效扩展至状态空间系统，实现两类建模方法的自然同步耦合
- 采用同步求解策略，有效突破传统状态空间法在大规模开关网络与矩阵合成中的计算瓶颈


## 使用的方法


- [[状态空间法|状态空间法]]
- [[节点分析法|节点分析法]]
- [[梯形积分法|梯形积分法]]
- [[离散伴随支路等效|离散伴随支路等效]]
- [[灵活分组聚类|灵活分组聚类]]
- [[稀疏矩阵求解|稀疏矩阵求解]]


## 涉及的模型


- [[通用电气网络|通用电气网络]]
- [[开关网络|开关网络]]
- [[非线性分段线性元件|非线性分段线性元件]]
- [[电容电感储能元件|电容电感储能元件]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[混合求解架构|混合求解架构]]
- [[开关网络处理|开关网络处理]]
- [[网络等值技术|网络等值技术]]


## 主要发现


- 分组独立维护状态矩阵策略，显著降低大规模开关组合预计算所需的内存占用
- 联合框架兼容梯形积分，在保证数值精度的同时提升含非线性元件网络的求解效率
- 验证了该方法在实时仿真中处理复杂拓扑与频繁开关事件的高效性与数值稳定性


