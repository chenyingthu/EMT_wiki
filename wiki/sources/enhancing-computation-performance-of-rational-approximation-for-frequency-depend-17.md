---
title: "Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting"
type: source
authors: ['Alexandre', 'A.', 'Kida']
year: 2024
journal: "Electric Power Systems Research, 234 (2024) 110778. doi:10.1016/j.epsr.2024.110778"
tags: ['network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/17/Kida 等 - 2024 - Enhancing computation performance of rational approximation for frequency-dependent network equivale.pdf"]
---

# Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting

**作者**: Alexandre, A., Kida
**年份**: 2024
**来源**: `17/Kida 等 - 2024 - Enhancing computation performance of rational approximation for frequency-dependent network equivale.pdf`

## 摘要

0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex Alexandre A. Kida a,b,∗, Felipe N.F. Dicler c, Thomas M. Campello c,d, Loan T.F.W. Silva c, Antonio C.S. Lima c, Fernando A. Moreira a, Robson F.S. Dias c, Glauco N. Taranto c

## 核心贡献


- 提出复数矢量拟合用于导纳矩阵综合，解除极点共轭约束
- 基于C语言与底层线性代数库实现算法并行化，摆脱商业软件依赖
- 系统评估模型阶数、端口数与频点数量对多端口FDNE计算性能的影响


## 使用的方法


- [[复数矢量拟合|复数矢量拟合]]
- [[矢量拟合|矢量拟合]]
- [[有理逼近|有理逼近]]
- [[并行计算|并行计算]]
- [[频域实现|频域实现]]
- [[状态空间综合|状态空间综合]]


## 涉及的模型


- [[fdne-model|FDNE]]
- [[多端口导纳矩阵|多端口导纳矩阵]]
- [[状态空间模型|状态空间模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]
- [[并行计算|并行计算]]
- [[有理逼近|有理逼近]]
- [[无源性校验|无源性校验]]


## 主要发现


- CVF成功应用于导纳矩阵综合，有效解除极点共轭约束并提升拟合灵活性
- 并行C语言实现显著加速有理逼近计算，验证了多端口FDNE建模的可行性
- 算法性能随模型阶数、端口数与频点增加保持稳定，计算效率优于传统串行实现


