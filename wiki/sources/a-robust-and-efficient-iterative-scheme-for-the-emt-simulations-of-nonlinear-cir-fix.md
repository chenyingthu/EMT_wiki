---
title: "A Robust and Efficient Iterative Scheme for the EMT Simulations of Nonlinear Circuits"
type: source
year: 2011
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/03/pesgm.2012.6343922.pdf.pdf"]
---

# A Robust and Efficient Iterative Scheme for the EMT Simulations of Nonlinear Circuits

**年份**: 2011
**来源**: `03/pesgm.2012.6343922.pdf.pdf`

## 摘要

A Robust and Efficient Iterative Scheme for the EMT Simulations of Nonlinear Circuits This paper presents a robust and efficient iterative scheme for solving nonlinear circuits as a solution method for electromagnetic transient (EMT) simulations. In most EMT simulations, the characteristics of nonlinear components can be represented by piece-wise linear curves. With this assumption, the Newton-Raphson (NR) method shows high efficiency, but it is prone to get into an infinite loop resulting in no

## 核心贡献


- 提出双轴牛顿-拉夫逊法，利用非线性特性双轴信息显著提升迭代收敛性
- 构建分层混合迭代策略，按效率与收敛性优先级组合三种算法确保全局收敛


## 使用的方法


- [[牛顿-拉夫逊法|牛顿-拉夫逊法]]
- [[双轴牛顿-拉夫逊法|双轴牛顿-拉夫逊法]]
- [[katzenelson算法|Katzenelson算法]]
- [[分段线性化|分段线性化]]


## 涉及的模型


- [[非线性电路|非线性电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[非线性电路求解|非线性电路求解]]
- [[迭代收敛性分析|迭代收敛性分析]]


## 主要发现


- 分层策略在多数工况下由标准法快速求解，失败时自动切换保障收敛
- 结合双轴法与Katzenelson法，在增加少量计算量下实现绝对收敛
- 算例验证表明该方案迭代次数少，兼顾计算效率与数值稳定性


