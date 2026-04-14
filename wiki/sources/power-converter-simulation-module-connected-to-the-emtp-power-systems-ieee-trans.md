---
title: "Power converter simulation module connected to the EMTP - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/31/59.76692.pdf.pdf"]
---

# Power converter simulation module connected to the EMTP - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `31/59.76692.pdf.pdf`

## 摘要

Presently the EMTP models converter valves as ideal switches in parallel with dampers designed to damp numerical oscillations introduced by the commutations. The converter network is modelled through branches with the appropriate TACS control circuits. It is assembled as any other EMTP network, without explicit topology recognition. A more efficient method, both in terms of solution and initialization, is based on a separately programmed module dedicated to power converter simulation and exploiting analytical knowledge. This paper presents the solution method used in such a module and its interface with the EMTP. Keywords : Digital simulation, EMTP, power converter 1. INTRODUCTION The EMTP (Electromagnetic transients program) [l] is a nodal analysis program based on the fixed time-step tra

## 核心贡献

- 针对EMT仿真中的问题进行了研究

## 使用的方法

- [[节点分析法|节点分析法]]
- [[固定步长梯形积分法|固定步长梯形积分法]]
- [[戴维南等效法|戴维南等效法]]
- [[后补偿法|后补偿法]]
- [[解析初始化技术|解析初始化技术]]
- [[独立模块接口技术|独立模块接口技术]]

## 涉及的模型

- [[电力变换器|电力变换器]]
- [[换流阀|换流阀]]
- [[六脉冲桥式换流器|六脉冲桥式换流器]]
- [[tacs控制电路|TACS控制电路]]

## 相关主题

- [[数字仿真|数字仿真]]
- [[电磁暂态仿真-emtp|电磁暂态仿真(EMTP)]]
- [[电力变换器仿真|电力变换器仿真]]
- [[非线性变拓扑网络|非线性变拓扑网络]]
- [[仿真初始化|仿真初始化]]

## 主要发现

Presently the EMTP models converter valves as ideal switches in parallel with dampers designed to damp numerical oscillations introduced by the commutations
