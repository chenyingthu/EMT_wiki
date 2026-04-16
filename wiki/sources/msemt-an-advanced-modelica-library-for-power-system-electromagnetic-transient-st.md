---
title: "MSEMT: An Advanced Modelica Library for Power System Electromagnetic Transient Studies"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Delivery;2022;37;4;10.1109/TPWRD.2021.3111127"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/MSEMT An Advanced Modelica Library for Power System Electromagnetic Transient Studies.pdf"]
---

# MSEMT: An Advanced Modelica Library for Power System Electromagnetic Transient Studies

**作者**: 
**年份**: 2022
**来源**: `27&28/MSEMT An Advanced Modelica Library for Power System Electromagnetic Transient Studies.pdf`

## 摘要

—Electromagnetic Transient (EMT) simulation tools are typically developed using conventional procedural program- ming languages. On the other hand, modern high-level and equation-based programming languages, such as Modelica, are currently available. Modelica allows formulating models that are easy to develop, maintain and understand by expressing what needs to be computed without stating how it should be computed. This paper presents a Modelica-based simulator for electromagnetic transients. It is demonstrated that this approach offers signiﬁcant advantages for developing sophisticated models. Computational performance and accuracy are compared to a conventional EMT- type simulation tool. Index Terms—Declarative modeling, equation-based modeling, object-oriented modeling, MSEMT library, m

## 核心贡献


- 开发MSEMT库实现声明式电磁暂态建模，模型与求解器完全解耦
- 引入结构分析与撕裂算法，高效分解并求解电力网络中的大规模代数环
- 集成DAE求解器与事件根查找机制，精确捕捉暂态不连续点与刚性动态


## 使用的方法


- [[结构分析|结构分析]]
- [[blt分块排序|BLT分块排序]]
- [[撕裂算法|撕裂算法]]
- [[pantelides指标约简|Pantelides指标约简]]
- [[dassl-ida求解器|DASSL/IDA求解器]]
- [[变步长bdf积分|变步长BDF积分]]
- [[事件根查找机制|事件根查找机制]]
- [[fmi联合仿真接口|FMI联合仿真接口]]


## 涉及的模型


- [[基础rlc元件|基础RLC元件]]
- [[输电线路|输电线路]]
- [[线性电气网络|线性电气网络]]
- [[非线性设备|非线性设备]]
- [[同步电机|同步电机]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[声明式建模|声明式建模]]
- [[面向对象建模|面向对象建模]]
- [[微分代数方程求解|微分代数方程求解]]
- [[暂态不连续点处理|暂态不连续点处理]]
- [[模型与求解器解耦|模型与求解器解耦]]


## 主要发现


- MSEMT仿真精度与传统EMTP工具相当，验证了声明式建模的有效性
- DAE求解器结合根查找机制可精确捕捉开关事件，有效处理系统刚性问题
- 模型与求解器解耦架构显著降低复杂设备建模难度，提升代码可维护性


