---
title: "New investigations on the method of characteristics for the evaluation of line transients"
type: source
authors: ['T. Kauffmann']
year: 2018
journal: "Electric Power Systems Research, 160 (2018) 243-250. doi:10.1016/j.epsr.2018.03.004"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/New investigations on the method of characteristics for the evaluation of line transients.pdf"]
---

# New investigations on the method of characteristics for the evaluation of line transients

**作者**: T. Kauffmann
**年份**: 2018
**来源**: `27&28/New investigations on the method of characteristics for the evaluation of line transients.pdf`

## 摘要

to  render  the  MoC  faster  than  the  traveling  wave-based

## 核心贡献


- 提出基于矢量拟合的串联阻抗矩阵有理函数拟合流程，实现宽频带参数高效拟合
- 深入分析特征线法消除空间离散化的可行性，揭示其数值误差来源与稳定性限制
- 证明为提升精度必须对线路分段，从而否定了该方法在均匀线路上的计算优势


## 使用的方法


- [[特征线法-moc|特征线法(MoC)]]
- [[矢量拟合-vf|矢量拟合(VF)]]
- [[有理函数逼近|有理函数逼近]]
- [[模态变换|模态变换]]
- [[时域卷积计算|时域卷积计算]]
- [[空间离散化消除|空间离散化消除]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[电缆|电缆]]
- [[频变线路模型|频变线路模型]]
- [[串联阻抗矩阵|串联阻抗矩阵]]
- [[并联导纳矩阵|并联导纳矩阵]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频变参数建模|频变参数建模]]
- [[行波模型对比|行波模型对比]]
- [[数值稳定性分析|数值稳定性分析]]
- [[线路暂态分析|线路暂态分析]]


## 主要发现


- 消除空间离散化会引入线性化近似误差，导致模型数值精度受限且易失稳
- 模态延迟要求的大积分步长是引发数值问题的主因，需线路分段以改善精度
- 线路分段虽能提升精度与稳定性，但完全抵消了该方法相比行波模型的效率优势


