---
title: "Stability of Algorithms for Electro-Magnetic-Transient Simulation of Networks with Switches and Non-linear Inductors"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2019.2919252"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/35/tpwrd.2019.2919252.pdf.pdf"]
---

# Stability of Algorithms for Electro-Magnetic-Transient Simulation of Networks with Switches and Non-linear Inductors

**作者**: 
**年份**: 2019
**来源**: `35/tpwrd.2019.2919252.pdf.pdf`

## 摘要

— This paper extends the analysis of the stability of electromagnetic transient simulation algorithms to non-linear systems with switching elements and non-linear inductor branches. A theoretical analysis based on common quadratic Lyapunov function (CQLF) theory is used to investigate the stability of numerical algorithms for the simulation of lumped strictly passive switched circuits (LSPSC). It is proved that only when certain fundamental physical properties, i.e., passivity and invariance of Lyapunov energy function are satisfied, does the widely used trapezoidal method result in stable simulations of such networks for any time-step size. This is different from the simulation of linear time invariant (LTI) systems where any real- world stable system has a stable simulation if an A-stabl

## 核心贡献



- 将EMT仿真算法的稳定性分析扩展至含开关元件与非线性电感的非线性系统
- 基于公共二次李雅普诺夫函数(CQLF)理论，证明了梯形法在满足无源性与能量函数不变性时对任意步长均稳定
- 证明了分段线性电感的仿真等价于集总严格无源开关电路(LSPSC)仿真，验证了梯形法的稳定性

## 使用的方法


- [[numerical-integration]]
- [[state-space]]

## 涉及的模型

- [[集中参数严格无源开关电路-lspsc|集中参数严格无源开关电路(LSPSC)]]
- [[非线性电感|非线性电感]]
- [[分段线性电感|分段线性电感]]
- [[开关元件|开关元件]]

## 相关主题


- [[passivity]]
- [[numerical-integration]]

## 主要发现



- 含开关的非线性系统仅当满足无源性和李雅普诺夫能量函数不变性时，梯形法才能保证任意步长下的仿真稳定
- 与线性时不变系统不同，非线性开关系统的各开关状态单独稳定不能保证整体仿真稳定
- 分段线性电感的EMT仿真可等效为集总严格无源开关电路仿真，使用梯形法同样具有稳定性