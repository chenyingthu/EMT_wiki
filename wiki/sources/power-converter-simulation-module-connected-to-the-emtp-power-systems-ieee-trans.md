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


- 提出专用换流器仿真模块与EMTP接口替代传统理想开关并联阻尼器模型
- 采用补偿法处理非线性支路避免换相时节点导纳矩阵重复重构与三角分解
- 将换流变压器内置于模块中消除空载导纳矩阵病态并支持饱和非线性建模


## 使用的方法


- [[节点分析|节点分析]]
- [[梯形积分法|梯形积分法]]
- [[补偿法|补偿法]]
- [[戴维南等值|戴维南等值]]
- [[状态空间法|状态空间法]]
- [[非线性支路建模|非线性支路建模]]


## 涉及的模型


- [[自然换相六脉动换流器|自然换相六脉动换流器]]
- [[换流变压器|换流变压器]]
- [[交直流网络|交直流网络]]
- [[电力电子阀|电力电子阀]]
- [[tacs控制系统|TACS控制系统]]


## 相关主题


- [[emtp仿真|EMTP仿真]]
- [[换流器建模|换流器建模]]
- [[混合仿真接口|混合仿真接口]]
- [[数值振荡抑制|数值振荡抑制]]
- [[变拓扑网络求解|变拓扑网络求解]]


## 主要发现


- 模块有效抑制梯形积分引发的数值振荡无需额外并联人工阻尼电路
- 基于解析知识实现换流器稳态初始化克服传统EMTP相量法初始化局限
- 补偿法结合非线性电流源模型显著提升含饱和变压器换流网络的求解效率


