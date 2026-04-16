---
title: "Multiphase power flow solutions using EMTP and Newtons method - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multiphase power flow solutions using EMTP and Newtons method.pdf"]
---

# Multiphase power flow solutions using EMTP and Newtons method - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `27&28/Multiphase power flow solutions using EMTP and Newtons method.pdf`

## 摘要

This paper describes a reliable and veay flexible multiphase load-flow solution process which is applicable for large trans- mission systems (up to 500 nodes). The process consists of an interface between the Electromagnetic Transients Rogram (EMTP) and a newly developed multiphase load flow algo- rithm that is based on the Newton-Raphson metbod. Subjects discussed include derivation of basic algorithm, s~ucture of the Jacobian matrix, and convergence charactaistics. INTRODUCTION Well known and reliable methods exist today for solving AC single-phase power flow pblems. Most of tbese are based on the Newton-Raphson method, which has become the method of choice. Single-phase load flows always assume balanced rhree-phase system opeaation, aod are ideaUy suited for representing large transmiss

## 核心贡献


- 提出基于支路电流法与直角坐标的牛顿拉夫逊多相潮流算法，提升不平衡系统建模灵活性
- 实现算法与EMTP无缝接口，直接复用网络导纳矩阵，避免重复构建
- 为大型输电系统提供精确稳态初始化方案，有效支持后续电磁暂态仿真


## 使用的方法


- [[牛顿-拉夫逊法|牛顿-拉夫逊法]]
- [[支路电流法|支路电流法]]
- [[直角坐标法|直角坐标法]]
- [[雅可比矩阵构建|雅可比矩阵构建]]
- [[emtp接口集成|EMTP接口集成]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[pq负荷|PQ负荷]]
- [[电压源|电压源]]
- [[电流源|电流源]]
- [[输电线路|输电线路]]
- [[变压器|变压器]]


## 相关主题


- [[多相潮流计算|多相潮流计算]]
- [[不平衡系统分析|不平衡系统分析]]
- [[稳态初始化|稳态初始化]]
- [[emtp集成|EMTP集成]]
- [[大型输电网络|大型输电网络]]


## 主要发现


- 算法在500节点系统中验证可靠，有效克服传统EMTP相量法收敛性差的问题
- 支路电流法显著提升三角形接线与相间电源等复杂负荷的建模灵活性与精度
- 与EMTP集成可直接获取精确稳态导纳矩阵，为暂态仿真提供高质量初始条件


