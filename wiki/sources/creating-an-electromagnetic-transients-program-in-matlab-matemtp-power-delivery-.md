---
title: "Creating An Electromagnetic Transients Program In Matlab: MatEMTP - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/11/Creating_an_Electromagnetic_Transients_Program_in_MATLAB_MatEMTP.pdf"]
---

# Creating An Electromagnetic Transients Program In Matlab: MatEMTP - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `11/Creating_an_Electromagnetic_Transients_Program_in_MATLAB_MatEMTP.pdf`

## 摘要

The traditional method for developing electric network analysis computer programs is based on coding using a conventional computer language: FORTRAN, C or Pascal. The programming language of the EMTP (Electromagnetic Transients Program) is FORTRAN-77. Such a program has a closed architecture and uses a large number of code lines to satisfy requirements ranging from low level data manipulation to the actual solution mathematics which eventually become diluted and almost impossible to visualize. This paper pro- poses a new design idea suitable for EM" re-development in a high level programming context. It presents the creation of the transient analysis numerical simulator MatEMTP in the computational engine frame of MATLAB. This new approach to software engineering can afford a dramatic codi

## 核心贡献


- 提出基于MATLAB的MatEMTP架构，利用矩阵运算实现暂态仿真代码的模块化重构
- 构建增广稀疏网络方程，显式引入开关关联矩阵，支持任意拓扑切换且免重构导纳阵
- 设计向量化求解流程与数据解析器，消除冗余判断，显著提升代码可读性与计算效率


## 使用的方法


- [[改进节点分析法|改进节点分析法]]
- [[梯形积分法|梯形积分法]]
- [[后向欧拉法|后向欧拉法]]
- [[稀疏矩阵运算|稀疏矩阵运算]]
- [[向量化编程|向量化编程]]
- [[固定步长离散化|固定步长离散化]]


## 涉及的模型



- [[多相耦合元件|多相耦合元件]]
- [[理想开关|理想开关]]
- [[电压源|电压源]]
- [[通用无源支路|通用无源支路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[仿真软件架构|仿真软件架构]]
- [[时域网络分析|时域网络分析]]
- [[开关拓扑处理|开关拓扑处理]]
- [[稳态初始化|稳态初始化]]
- [[开源计算引擎|开源计算引擎]]


## 主要发现


- 验证表明MatEMTP与传统EMTP求解精度与耗时高度一致，具备工程可用性
- 增广矩阵公式有效消除非法开关回路，实现浮空节点与任意开关互联的稳定求解
- 向量化编程与内存预分配策略显著降低解释器开销，使高级语言仿真效率满足需求


