---
title: "Numerical Integration by the 2-Stage Diagonally"
type: source
authors: ['未知']
year: 2008
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/29/TPWRD.2008.923397.pdf.pdf"]
---

# Numerical Integration by the 2-Stage Diagonally

**作者**: 
**年份**: 2008
**来源**: `29/TPWRD.2008.923397.pdf.pdf`

## 摘要

—This paper proposes applying the two-stage di- agonally implicit Runge–Kutta (2S-DIRK) method of numerical integration to the calculation of electromagnetic transients (EMTs) in a power system. The accuracy and the numerical stability of 2S-DIRK are almost the same as those of the trapezoidal method, while 2S-DIRK does not produce sustained numerical oscilla- tion due to a sudden change of an inductor current or a capacitor voltage unlike the trapezoidal method. First, this paper reviews the 2S-DIRK integration scheme and derives the 2S-DIRK formulas of inductors and capacitors for both linear and nonlinear cases. Then, analytical comparisons of 2S-DIRK with the trapezoidal, backward Euler, and Gear–Shichman methods are carried out, and numerical examples which verify the analytical compa

## 核心贡献


- 提出将2S-DIRK积分法用于电磁暂态仿真，兼具梯形法精度稳定性且无数值振荡
- 推导线性与非线性电感电容的2S-DIRK等效电路公式，支持直接节点分析求解
- 证明该方法两阶段解耦特性，线性元件导纳矩阵无需重复分解，提升计算效率


## 使用的方法


- [[numerical-integration|数值积分]]
- [[梯形法|梯形法]]
- [[后向欧拉法|后向欧拉法]]
- [[numerical-integration|数值积分]]
- [[临界阻尼调整法|临界阻尼调整法]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[线性电感|线性电感]]
- [[线性电容|线性电容]]
- [[非线性电感|非线性电感]]
- [[非线性电容|非线性电容]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值积分|数值积分]]
- [[数值稳定性|数值稳定性]]
- [[数值振荡抑制|数值振荡抑制]]
- [[刚性电路求解|刚性电路求解]]
- [[等效电路建模|等效电路建模]]


## 主要发现


- 2S-DIRK精度与稳定性媲美梯形法，且彻底消除突变引发的持续数值振荡
- 线性元件两阶段导纳值相同，节点导纳矩阵无需重复分解，显著降低计算开销
- 相比CDA方法无需检测突变事件即可自动抑制振荡，算法实现更简便可靠


